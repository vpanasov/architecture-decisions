# Architecture Decisions — LifePay / Fortis

Локальный репозиторий RFC и ADR документов, синхронизированных из Confluence ([RFCs](https://bz.incdb.team/display/DOCS/RFCs?src=contextnavpagetreemode), [ADR's](https://bz.incdb.team/display/DOCS/ADR%27s?src=contextnavpagetreemode)).

**Дата синхронизации:** 2026-06-29

---

## RFCs (Request for Comments)

| # | Название | Статус |
|---|---------|--------|
| [RFC-0001](https://bz.incdb.team/pages/viewpage.action?pageId=3411542161) | Подход к реализации единого продуктового портфеля | DRAFT |
| [RFC-0002](https://bz.incdb.team/pages/viewpage.action?pageId=3413606406) | Global Merchant Portal — объединение Fortis и LP на базе единой модульной архитектуры | APPROVED |
| [RFC-0008](https://bz.incdb.team/pages/viewpage.action?pageId=3419832738) | Интеграция Pyrus с 1С и HR-link для кадровых документов | IN REVIEW |
| [RFC-0009](https://bz.incdb.team/pages/viewpage.action?pageId=3419832833) | Unified Mobile POS — объединение retail-app и fortis-pos-app | DRAFT |
| [RFC-0010](https://bz.incdb.team/pages/viewpage.action?pageId=3420619494) | Собственный AI code-reviewer на Claude Agent SDK для Fortis GitLab | IN REVIEW |
| [RFC-0011](https://bz.incdb.team/pages/viewpage.action?pageId=3421831337) | Интеграция Pyrus и 1С через n8n | APPROVED |
| [RFC-0012](https://bz.incdb.team/pages/viewpage.action?pageId=3421831711) | Интеграция Pyrus и Correct для распознавания документов | APPROVED |
| [RFC-0013](https://bz.incdb.team/pages/viewpage.action?pageId=3423764705) | Взаимный кросс-мониторинг ключевых эндпоинтов между AWS и Yandex Cloud | REVISE |
| [RFC-0014](https://bz.incdb.team/pages/viewpage.action?pageId=3425697999) | Device2Host интеграция с вендором процессинга | APPROVED |
| [RFC-0016](https://bz.incdb.team/pages/viewpage.action?pageId=3438543020) | rf bypass – gateway доступа к зарубежным ресурсам, заблокированным по GeoIP | APPROVED |
| [RFC-0018](https://bz.incdb.team/pages/viewpage.action?pageId=3442704389) | Корпоративный LLM Gateway — вывод в Production на платформе PSP Life Pay | APPROVED |

## ADRs (Architecture Decision Records)

| # | Название | Статус |
|---|---------|--------|
| [ADR-0004](https://bz.incdb.team/pages/viewpage.action?pageId=3413606413) | Global Merchant Portal — объединение Fortis и LP | Accepted |
| [ADR-0007](https://bz.incdb.team/pages/viewpage.action?pageId=3420619495) | Собственный AI code-reviewer на Claude Agent SDK | Implemented |
| [ADR-0008](https://bz.incdb.team/pages/viewpage.action?pageId=3422421227) | Интеграция Pyrus и 1С через n8n | ACCEPTED |
| [ADR-0009](https://bz.incdb.team/pages/viewpage.action?pageId=3424485731) | Интеграция Pyrus и Correct для распознавания документов | Accepted |
| [ADR-0010](https://bz.incdb.team/pages/viewpage.action?pageId=3429498897) | Device2Host интеграция с вендором процессинга | Accepted |
| [ADR-0011](https://bz.incdb.team/pages/viewpage.action?pageId=3442704420) | rf bypass – gateway доступа к зарубежным ресурсам, заблокированным по GeoIP | Implemented |
| [ADR-0012](https://bz.incdb.team/pages/viewpage.action?pageId=3448995848) | Корпоративный LLM Gateway — вывод в Production на платформе PSP Life Pay | Accepted |

## Связи между документами

```
RFC-0001 (единый продуктовый портфель)
├── RFC-0002 → ADR-0004 (Global Merchant Portal)
└── RFC-0009 (Unified Mobile POS)

RFC-0010 → ADR-0007 (собственный AI code-reviewer)

RFC-0008 ──► RFC-0011 → ADR-0008 (Pyrus + 1С интеграции)
                         RFC-0012 → ADR-0009 (Pyrus + Correct распознавание документов)

RFC-0013 (кросс-мониторинг AWS ↔ YC)

RFC-0014 → ADR-0010 (Device2Host интеграция с VaultsPay)

RFC-0016 → ADR-0011 (rf bypass – gateway GeoIP)

RFC-0018 → ADR-0012 (Корпоративный LLM Gateway — Production на PSP-Cloud)
```

## Структура

```
architecture-decisions/
├── .claude/
│   └── skills/
│       ├── adr-governor/
│       │   ├── SKILL.md
│       │   └── scripts/
│       │       └── extract_rfc.py
│       └── rfc-validator/
│           └── SKILL.md
├── README.md
├── templates/
│   └── adr-template.md
├── rfcs/
│   ├── RFC-0001.md  — RFC-0016.md
│   └── images/
├── adrs/
│   ├── ADR-0004.md, ADR-0007.md — ADR-0011.md
└── validate/
    └── report-rfc-XXXX.md
```
