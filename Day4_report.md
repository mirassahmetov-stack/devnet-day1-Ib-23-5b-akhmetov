# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name:Miras
- Group:Ib-23-5B
- Token:D1-IB-23-5b-01-1A3F
- Repo:4

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt:yes
- artifacts/day4/docker/sampleapp_token_proof.txt:yes
- artifacts/day4/docker/sampleapp_docker_ps.txt:yes
- artifacts/day4/docker/sampleapp_build_log.txt:yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt:yes
- artifacts/day4/jenkins/buildapp_console.txt:yes
- artifacts/day4/jenkins/testapp_console.txt:yes
- artifacts/day4/jenkins/pipeline_script.groovy:yes
- artifacts/day4/jenkins/pipeline_console.txt:yes
- artifacts/day4/jenkins/jenkins_url.txt:yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt:yes
- artifacts/day4/security/login_v1.txt:yes
- artifacts/day4/security/signup_v2.txt:yes
- artifacts/day4/security/login_v2.txt:yes
- artifacts/day4/security/db_tables.txt:yes
- artifacts/day4/security/db_user_hash_sample.txt:yes


## 4) Short reflection (5–8 lines)
Самым сложным сегодня была борьба с Git и вложенными репозиториями в папке DevNet. Из-за скрытых файлов .git основной репозиторий видел папку как пустой сабмодуль, и файлы никак не хотели попадать в коммит — пришлось полностью сбрасывать индекс через git rm --cached. Также возникли трудности с путями в Docker и Ansible, так как структура лаб отличается от структуры моего основного репо. Главная ошибка безопасности, которую я исправил — хранение паролей в открытом виде. В Lab 6.5.10 я внедрил хеширование паролей (v2), что делает базу данных устойчивой к утечкам, так как даже при доступе к таблице злоумышленник не увидит реальные пароли пользователей.

## 5) Problems & fixes (at least 1)
Мирас, чтобы твой отчет за 4-й день выглядел солидно и прошел любую проверку, давай оформим раздел «Problems & fixes» на основе того реального ада с Git, через который мы только что прошли. Это самый весомый технический кейс за сегодня.

## 5) Problems & fixes
Problem: При попытке закоммитить файлы из папки DevNet в основной репозиторий, Git выдавал предупреждение warning: adding embedded git repository. Сама папка отображалась на GitHub как «белая иконка» (пустой сабмодуль), и файлы внутри неё были недоступны, хотя физически они находились на диске. Обычный git add . не помогал, так как Git считал эту директорию отдельным независимым проектом.

Fix:

Физически удалил скрытую папку метаданных .git внутри проблемного подкаталога: rm -rf DevNet/DevNet/.git.

Принудительно очистил индекс Git, чтобы он «забыл» папку как сабмодуль: git rm -r --cached ..

Передобавил файлы заново уже как обычный контент: git add ..

Сделал коммит и отправил в ветку main.

Proof:
В выводе терминала после повторного git add . исчезло желтое предупреждение «embedded git repository», а команда git status наконец-то показала список файлов в состоянии new file, а не «nothing to commit». На GitHub папка DevNet стала открываться и отображать содержимое.