#!/usr/bin/env python3
"""
extract_rfc.py — Extract data from an RFC to generate an ADR.

Usage:
    python extract_rfc.py RFC-0011

Steps:
1. Reads the specified RFC from rfcs/RFC-XXXX.md
2. Checks RFC status = Approved
3. Extracts: title, context, decision, alternatives, consequences, tech debt, metrics
4. Outputs the result to stdout as JSON for the agent
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Repository root — 4 levels up from scripts/
REPO_ROOT = Path(__file__).resolve().parents[4]
RFCS_DIR = REPO_ROOT / "rfcs"


def parse_args():
    parser = argparse.ArgumentParser(description="Extract data from RFC")
    parser.add_argument("rfc", help="RFC number, e.g. RFC-0011")
    return parser.parse_args()


def read_rfc(rfc_id: str) -> str:
    path = RFCS_DIR / f"{rfc_id}.md"
    if not path.exists():
        print(json.dumps({"error": f"File {path} not found."}), file=sys.stdout)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def check_status(rfc_text: str, rfc_id: str) -> str:
    m = re.search(r"\*\*Статус:\*\*\s*(.+)", rfc_text)
    if not m:
        print(json.dumps({"error": f"Could not determine status of {rfc_id}."}), file=sys.stdout)
        sys.exit(1)
    status = m.group(1).strip()
    if "approved" not in status.lower():
        print(
            json.dumps({
                "error": f"{rfc_id} has status '{status}'. ADR can only be generated from an RFC with Approved status."
            }),
            file=sys.stdout,
        )
        sys.exit(1)
    return status


def extract_title(rfc_text: str) -> str:
    m = re.match(r"#\s*RFC-\d+:\s*(.+)", rfc_text)
    return m.group(1).strip() if m else "Untitled"


def extract_section(rfc_text: str, heading: str) -> str:
    """Extract section text by heading (ATX ## or Setext ---).

    Two-pass matching: exact match first, then substring.
    Stops at the next heading of the same or higher level.
    """
    lines = rfc_text.splitlines()
    heading_lower = heading.lower()
    start = None
    matched_level = None

    for exact in [True, False]:
        for i, line in enumerate(lines):
            atx = re.match(r"^(#{1,6})\s+(.+)", line)
            if atx:
                level = len(atx.group(1))
                text = atx.group(2).strip().lower()
                match = (text == heading_lower) if exact else (heading_lower in text)
                if match:
                    start = i + 1
                    matched_level = level
                    break
            if (
                i + 1 < len(lines)
                and re.match(r"^-{2,}\s*$", lines[i + 1])
                and line.strip()
            ):
                text = line.strip().lower()
                match = (text == heading_lower) if exact else (heading_lower in text)
                if match:
                    start = i + 2
                    matched_level = 2
                    break
        if start is not None:
            break

    if start is None:
        return ""

    result_lines = []
    for j in range(start, len(lines)):
        line = lines[j]
        atx = re.match(r"^(#{1,6})\s+", line)
        if atx and len(atx.group(1)) <= matched_level:
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
        print(json.dumps({"error": "Format: RFC-XXXX (e.g. RFC-0011)"}), file=sys.stdout)
        sys.exit(1)

    rfc_text = read_rfc(rfc_id)
    check_status(rfc_text, rfc_id)

    result = {
        "rfc_id": rfc_id,
        "title": extract_title(rfc_text),
        "context": extract_field(rfc_text, ["Проблема и контекст", "Проблема", "Контекст"]),
        "decision": extract_field(
            rfc_text,
            ["Предлагаемое решение", "Решение", "Предлагаемое решение (1 параграф + схемы)"],
        ),
        "alternatives": extract_field(
            rfc_text, ["Альтернативы (кратко)", "Альтернативы", "Рассмотренные альтернативы"]
        ),
        "consequences": extract_field(
            rfc_text,
            [
                "Компромиссы",
                "Последствия",
                "Риски",
            ],
        ),
        "tech_debt": extract_field(
            rfc_text,
            ["Технический долг"],
        ),
        "metrics": extract_field(
            rfc_text,
            ["Метрики успеха", "Метрики"],
        ),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

