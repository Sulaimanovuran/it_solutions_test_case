#!/bin/sh

# Выполнение миграций
python manage.py migrate

# Сбор статических файлов
python manage.py collectstatic --noinput

# Запуск приложения
exec "$@"
