Приложение на Python 3 / Django / SQLite3.

зависимости:
Django==2.1.7

из директории /secproj:
python manage.py migrate
// будут созданы таблицы для админки, сессий, contenttypes и auth (без чего, возможно, Django не будет норм работать, если критично - я все это постараюсь отключить)

установить sqlite3, если не установлен и инициализировать db
sqlite3 db.sqlite3
sqlite> .read init-db.sql
sqlite> .exit

запустить встроенный в Django сервер
python manage.py runserver

http://127.0.0.1:8000/
