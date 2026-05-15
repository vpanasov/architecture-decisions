# Validation Report: RFC-0014

**Date:** 2026-05-15
**Status:** FAIL

## Metadata

| Field | Status | Value |
|-------|--------|-------|
| Автор | PASS | Небелёнов Евгений |
| Статус | PASS | Approved |
| Дата принятия | PASS | 2026-05-14 |
| Срок действия | PASS | 2026-09-14 |
| Начало реализации | PASS | 2026-04-28 |

## Structural completeness

| Section | Status |
|---------|--------|
| Проблема и контекст | PASS |
| Предлагаемое решение | PASS |
| Альтернативы | PASS |
| Компромиссы и технический долг | PASS |
| Метрики успеха | PASS |
| Источники | PASS |

## Links

| URL | Status | HTTP Code |
|-----|--------|-----------|
| https://bz.incdb.team/pages/viewpage.action?pageId=3404890763 | PASS | 200 |
| https://bz.incdb.team/pages/viewpage.action?pageId=3404890767 | PASS | 200 |
| https://bz.incdb.team/pages/viewpage.action?pageId=3416523022 | PASS | 200 |
| https://bz.incdb.team/pages/viewpage.action?pageId=3422421223 | PASS | 200 |
| https://bz.incdb.team/pages/viewpage.action?pageId=3416522931 | PASS | 200 |
| https://bz.incdb.team/pages/viewpage.action?pageId=3363537138 | PASS | 200 |
| https://rulebook.centralbank.ae/en/rulebook/retail-payment-services-and-card-schemes-regulation | FAIL | 403 |

## ADR readiness

| Check | Status | Details |
|-------|--------|---------|
| Статус = Approved | PASS | Approved |
| ADR not yet exists | FAIL | ADR-0010.md already exists for RFC-0014 |

## Parser (extract_rfc.py)

| Field | Status | Length |
|-------|--------|--------|
| title | PASS | 49 |
| context | PASS | 1482 |
| decision | PASS | 850 |
| alternatives | PASS | 397 |
| consequences | PASS | 791 |
| tech_debt | PASS | 380 |
| metrics | PASS | 398 |

## Summary

- Total checks: 22
- Passed: 20
- Failed: 2
- **FAIL:** External link https://rulebook.centralbank.ae/... returned HTTP 403
- **FAIL:** ADR-0010.md already exists for RFC-0014
