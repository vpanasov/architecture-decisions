# ADR Governor Skill

## Когда использовать
- Команда "generate adr from RFC-XXXX"

## Как работает
1. Прочитать RFC-XXXX из https://bz.incdb.team/display/DOCS/RFCs
2. Проверить статус RFC-XXXX = Approved. Если нет, то прервать с сообщением.
3. Определить номер для ADR-XXXX: max(существующие ADR) + 1.
4. Запустить scripts/extract_adr.py:
	- Извлечь из RFC-XXXX: контекст, решение, альтернативы, последствия, техдолг
5. Сформировать ADR-XXXX по шаблону templates/adr-template.md
  - Поставить в ADR-XXXX Статус = Accepted
6. Записать ADR-XXXX в adrs/ADR-XXXX-<name>.md

## Скрипты
- extract_adr.py: Извлечение данных из RFC-XXXX (выводит JSON в stdout)

## Шаблоны
- templates/adr-template.md

## Ограничения
- Работать с RFC-XXXX только в статусе Accepted
- Всегда указывать "Сгенерирован: AI-агент (adr-governor)" в метаданных ADR-XXXX
- Не изменять содержание решения из RFC-XXXX (только извлечение данных)
- Все даты в ADR (Дата принятия, Дата внедрения) оставлять пустыми — заполняются вручную
- Все ссылки в References должны быть активными и вести на страницы-источники в Confluence (https://bz.incdb.team/...)

