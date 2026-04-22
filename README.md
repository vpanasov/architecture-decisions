# Architecture Decisions — LifePay / Fortis

Локальный репозиторий RFC и ADR документов, синхронизированных из Confluence ([RFCs](https://bz.incdb.team/display/DOCS/RFCs?src=contextnavpagetreemode), [ADR's](https://bz.incdb.team/display/DOCS/ADR%27s?src=contextnavpagetreemode)).

**Дата синхронизации:** 2026-04-22

---

## RFCs (Request for Comments)

| # | Название | Статус |
|---|---------|--------|
| [RFC-0001](rfcs/RFC-0001.md) | Подход к реализации единого продуктового портфеля | DRAFT |
| [RFC-0002](rfcs/RFC-0002.md) | Global Merchant Portal — объединение Fortis и LP на базе единой модульной архитектуры | APPROVED |
| [RFC-0003](rfcs/RFC-0003.md) | AI Sales Dashboard — Claude Code чат с аналитическими скилами | Revise |
| [RFC-0004](rfcs/RFC-0004.md) | Автодозвон LifePay — MVP автоматизации исходящих звонков | Approved с замечаниями |
| [RFC-0005](rfcs/RFC-0005.md) | Ontology Service — корпоративная база знаний с AI-агрегацией | Approved с замечаниями |
| [RFC-0006](rfcs/RFC-0006.md) | Интеграция Greptile в корпоративный GitLab — пилот 14 дней | APPROVED |
| [RFC-0007](rfcs/RFC-0007.md) | Корпоративный LLM Gateway — архитектурное решение (MVP) | На рассмотрении архкома |
| [RFC-0008](rfcs/RFC-0008.md) | Интеграция Pyrus с 1С и HR-link для кадровых документов | Draft |
| [RFC-0009](rfcs/RFC-0009.md) | Unified Mobile POS — объединение retail-app и fortis-pos-app | DRAFT |
| [RFC-0010](rfcs/RFC-0010.md) | Собственный AI code-reviewer на Claude Agent SDK для Fortis GitLab | DRAFT |
| [RFC-0011](rfcs/RFC-0011.md) | Интеграция Pyrus и 1С через n8n | APPROVED |

## ADRs (Architecture Decision Records)

| # | Название | Статус |
|---|---------|--------|
| [ADR-0001](adrs/ADR-0001.md) | Выбор подхода к созданию глобального ИТ-продукта | Draft |
| [ADR-0002](adrs/ADR-0002.md) | Выбор подхода к проектированию ядра платформы | Draft |
| [ADR-0003](adrs/ADR-0003.md) | Складской и логистический контур — вне AdminArea | Draft |
| [ADR-0004](adrs/ADR-0004.md) | Global Merchant Portal — объединение Fortis и LP | Accepted |
| [ADR-0005](adrs/ADR-0005.md) | LLM Gateway MVP на внешнем VPS | Accepted |
| [ADR-0006](adrs/ADR-0006.md) | Интеграция Greptile в корпоративный GitLab (пилот) | Superseded |
| [ADR-0007](adrs/ADR-0007.md) | Собственный AI code-reviewer на Claude Agent SDK | Implemented |

## Связи между документами

```
RFC-0001 (единый продуктовый портфель)
├── ADR-0001 (подход к глобальному продукту)
│   └── ADR-0002 (проектирование ядра платформы)
│       └── ADR-0003 (склад вне AdminArea)
├── RFC-0002 → ADR-0004 (Global Merchant Portal)
└── RFC-0009 (Unified Mobile POS)

RFC-0006 → ADR-0006 (Greptile пилот) ──[superseded by]──► RFC-0010 → ADR-0007 (собственный AI code-reviewer)

RFC-0007 → ADR-0005 (LLM Gateway)

RFC-0008 ──► RFC-0011 (Pyrus + 1С интеграции)
```

## Структура

```
architecture-decisions/
├── README.md
├── rfcs/
│   ├── RFC-0001.md  — RFC-0011.md
└── adrs/
    ├── ADR-0001.md  — ADR-0007.md
```
