Day 5 Report — Module 8 Capstone
1) Student
Name: Miras

Group: IB-23-5B

Token:D1-IB-23-5b-01-1A3F

Repo: devnet-day1-IB-23-5B-Akhmetov

2) YANG (8.3.5)
Evidence files:

artifacts/day5/yang/ietf-interfaces.yang

artifacts/day5/yang/pyang_version.txt

artifacts/day5/yang/pyang_tree.txt (содержит структуру +--rw interfaces)

Screenshot: Модуль успешно скомпилирован через pyang.

3) Webex (8.6.7)
Room title contains token_hash8: Yes (согласно логике day5_summary_builder.py)

Message text contains token_hash8: Yes

Evidence files:

me.json, rooms_list.json, room_create.json, message_post.json, messages_list.json

4) Packet Tracer Controller REST (8.8.3)
external_access_check contains “empty ticket”: Yes

serviceTicket saved: Yes (сохранен в serviceTicket.txt)

Evidence files:

external_access_check.json, network_devices.json, hosts.json

postman_collection.json, postman_environment.json

pt_internal_output.txt (вывод Python-скрипта из PT)

5) Commands output (paste exact)
Plaintext
devasc@labvm:~/Desktop/devnet-day1-IB-23-5B-Akhmetov$ python3 src/day5_summary_builder.py
Summary Day 5 built successfully.

devasc@labvm:~/Desktop/devnet-day1-IB-23-5B-Akhmetov$ python3 -m pytest -q tests/test_day5_module8.py
...                                                                 [100%]
3 passed in 0.15s
6) Problems & fixes (at least 1)
Problem: Ошибка json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) при запуске тестов. Также была ошибка 500 Internal Server Error в Postman при запросе тикета методом GET.

Fix:

Исправлены пути выполнения команд: все операции теперь проводятся из корня репозитория, чтобы файлы artifacts/ не создавались пустыми.

В Postman метод запроса изменен с GET на POST для эндпоинта /api/v1/ticket.

Proof: Команда pytest теперь возвращает статус passed, а summary.json содержит валидный JSON-объект.