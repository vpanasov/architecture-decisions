#!/usr/bin/env python3
"""
extract_adr.py — Извлечение данных из RFC для генерации ADR.

Использование:
    python extract_adr.py RFC-0011

Скрипт:
1. Читает указанный RFC из rfcs/RFC-XXXX.md
2. Проверяет статус RFC = Approved
3. Извлекает: название, контекст, решение, альтернативы, последствия
4. Выводит результат в stdout как JSON для агента
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Корень репозитория — 4 уровня вверх от scripts/
REPO_ROOT = Path(__file__).resolve().parents[4]
RFCS_DIR = REPO_ROOT / "rfcs"


def parse_args():
    parser = argparse.ArgumentParser(description="Извлечение данных из RFC")
    parser.add_argument("rfc", help="Номер RFC, например RFC-0011")
    return parser.parse_args()


def read_rfc(rfc_id: str) -> str:
    path = RFCS_DIR / f"{rfc_id}.md"
    if not path.exists():
        print(json.dumps({"error": f"Файл {path} не найден."}), file=sys.stdout)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def check_status(rfc_text: str, rfc_id: str) -> str:
    m = re.search(r"\*\*Статус:\*\*\s*(.+)", rfc_text)
    if not m:
        print(json.dumps({"error": f"Не удалось определить статус {rfc_id}."}), file=sys.stdout)
        sys.exit(1)
    status = m.group(1).strip()
    if "approved" not in status.lower():
        print(
            json.dumps({
                "error": f"{rfc_id} имеет статус «{status}». ADR можно генерировать только из RFC со статусом Approved."
            }),
            file=sys.stdout,
        )
        sys.exit(1)
    return status


def extract_title(rfc_text: str) -> str:
    m = re.match(r"#\s*RFC-\d+:\s*(.+)", rfc_text)
    return m.group(1).strip() if m else "Без названия"


def extract_section(rfc_text: str, heading: str) -> str:
    """Извлекает текст секции по заголовку (ATX ## или Setext ---)."""
    lines = rfc_text.splitlines()
    start = None
    heading_lower = heading.lower()

    for i, line in enumerate(lines):
        if re.match(r"^#{1,6}\s+", line) and heading_lower in line.lower():
            start = i + 1
            break
        if (
            heading_lower in line.lower()
            and i + 1 < len(lines)
            and re.match(r"^-{2,}\s*$", lines[i + 1])
        ):
            start = i + 2
            break

    if start is None:
        return ""

    result_lines = []
    for j in range(start, len(lines)):
        line = lines[j]
        if re.match(r"^#{1,2}\s+", line):
            break
        if (
            j + 1 < len(lines)
            and re.match(r"^-{2,}\s*$", lines[j + 1])
            and line.strip()
            and not line.startswith("#")
            and not line.startswith("*")
            and not line.startswith("-")
        ):
            break
        result_lines.append(line)

    return "\n".join(result_lines).strip()


def extract_field(rfc_text: str, candidates: list[str]) -> str:
    for heading in candidates:
        text = extract_section(rfc_text, heading)
        if text:
            return text
    return ""


def main():
    args = parse_args()
    rfc_id = args.rfc.upper()

    if not re.match(r"^RFC-\d{4}$", rfc_id):
        print(json.dumps({"error": "Формат: RFC-XXXX (например RFC-0011)"}), file=sys.stdout)
        sys.exit(1)

    rfc_text = read_rfc(rfc_id)
    check_status(rfc_text, rfc_id)

    result = {
        "rfc_id": rfc_id,
        "title": extract_title(rfc_text),
        "context": extract_field(rfc_text, ["Проблема и контекст", "Проблема", "Контекст"]),
        "solution": extract_field(
            rfc_text,
            ["Предлагаемое решение", "Решение", "Предлагаемое решение (1 параграф + схемы)"],
        ),
        "alternatives": extract_field(
            rfc_text, ["Альтернативы (кратко)", "Альтернативы", "Рассмотренные альтернативы"]
        ),
        "consequences": extract_field(
            rfc_text,
            [
                "Компромиссы / Технический долг",
                "Компромиссы",
                "Технический долг",
                "Последствия",
                "Риски",
            ],
        ),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

