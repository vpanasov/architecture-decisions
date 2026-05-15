# RFC Validator Skill

## When to use
- Command "validate RFC-XXXX"

## How it works
1. Read RFC-XXXX from https://bz.incdb.team/display/DOCS/RFCs
2. Save RFC-XXXX content to rfcs/RFC-XXXX.md if not already saved
3. Run validation checks (see below)
4. Run scripts/extract_rfc.py RFC-XXXX and verify all JSON fields are non-empty
5. Generate validation report to validate/report-rfc-XXXX.md

## Validation checks

### 1. Metadata
- Автор is present and non-empty
- Статус is present and has a valid value
- Дата принятия is present
- Срок действия is present
- Начало реализации is present

### 2. Structural completeness
Required sections (check each exists and is non-empty):
- Проблема и контекст (or Проблема)
- Предлагаемое решение (or Решение)
- Альтернативы
- Компромиссы и технический долг (or Компромиссы + Технический долг)
- Метрики успеха (or Метрики)
- Источники (or References)

### 3. Links
- All Confluence links (https://bz.incdb.team/...) are accessible (HTTP 200)
- All external links return a valid HTTP response

### 4. ADR readiness
- Статус = Approved
- extract_rfc.py returns non-empty values for: title, context, decision, alternatives, consequences, tech_debt, metrics
- No ADR for this RFC already exists in adrs/

## Report format
The report is written to validate/report-rfc-XXXX.md using the structure:

```
# Validation Report: RFC-XXXX

**Date:** YYYY-MM-DD
**Status:** PASS | FAIL

## Metadata
| Field | Status | Value |
|-------|--------|-------|

## Structural completeness
| Section | Status |
|---------|--------|

## Links
| URL | Status | HTTP Code |
|-----|--------|-----------|

## ADR readiness
| Check | Status | Details |
|-------|--------|---------|

## Parser (extract_rfc.py)
| Field | Status | Length |
|-------|--------|--------|

## Summary
- Total checks: N
- Passed: N
- Failed: N
```

## Constraints
- Do not modify RFC content during validation
- Report must always be generated, even if all checks pass
- Overall status is FAIL if any check fails, PASS otherwise
