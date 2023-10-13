# [Factory Backend]()


## Содержание

[1. Описание проекта](README.md#Описание-проекта)  
[2. Функционал](README.md#Функционал)  
[3. Установка и запуск](README.md#Установка-и-запуск)  


## Описание проекта

Пример API с базовым функционалом аутентификации и регистрации пользователей, которое принимает сообщения и отправляет их в связанный с пользователем чат через Telegram bot.

:arrow_up: [к содержанию](README.md#Содержание)


## Функционал

#### Реализация и используемые технологии:

- Фреймворк Django + Django Rest Framework
- Хранение данных - SQLite
- Документация API на базе Swagger, ReDoc - drf-yasg
- Управление пользователями API, регистрация/авторизация по токену - djoser
- Асинхронное выполнение задач по рассылке - Celery + Redis

:arrow_up: [к содержанию](README.md#Содержание)


## Установка и запуск

#### Клонируйте проект локально и перейдите в папку `factory`:

```bash
git clone https://gitlab.com/exspa/factory-back.git
cd factory
```

#### Создайте виртуальное окружение для проекта:

```bash
python -m venv venv_factory
source venv_factory/bin/activate
```

#### Установите необходимые пакеты из файла `factory/requirements.txt`:
```bash
pip install -r factory/requirements.txt 
```

#### Сгенерировать секретный ключ Django:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### В файле `factory/.env.Example` замените шаблонные переменные окружения django, `SECRET_KEY` обязательно, остальные на усмотрение:

```python
# django
SECRET_KEY='django-example-_137^&*6*98_-38y47hh712-=7&738&&11'
DEBUG=True
ALLOWED_HOSTS='example.com'
```

#### Создайте и зарегистрируйте Telegram bot по [инструкции](https://core.telegram.org/bots/features#botfather) для получения токена, после замените переменную окружения в файле `factory/.env.Example`:

```python
# telegram bot
TELEGRAM_TOKEN='1234567890:ExAmple_2TheW4j3II8IDxKtCX_lLaTcN'
```

#### Установите сервер Redis локально в вашей операционной системе:

```bash
sudo apt-get update  
sudo apt-get install redis  
```

#### Или подключите через облачную базу данных Redis, тогда в файле `factory/.env.Example` замените переменные окружения:

```python
# celery
CELERY_ENDPOINT='redis://default:****@redis-11111.22.us-west-1-1.ec1.cloud.example.com:11111'
```

#### Создайте и примените миграции из каталога проекта `/factory/`:
```bash
python manage.py makemigrations 
python manage.py migrate 
```

#### Запуск проекта, выполните команды в отдельных консольных окнах:

 - `redis-server` - сервер Redis, если он установлен локально  
 - `celery -A factory worker -l INFO` - Celery из каталога проекта */factory/*
 - `python manage.py runserver` - запуск Django-проекта из каталога проекта */factory/*

:arrow_up: [к содержанию](README.md#Содержание)