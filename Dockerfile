ARG PYTHON=python:3.9-alpine
FROM $PYTHON AS build
WORKDIR /usr/app

# Установка C зависимостей
RUN apk add --no-cache --update \
            gcc \
            libc-dev \
            linux-headers \
            postgresql-dev \
            libusb-dev \
            libffi-dev

# Установка зависимостей python
RUN python3 -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"
COPY factory/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

## Stage two ##
FROM $PYTHON

# Установка зависимостей C, создание пользователя
RUN apk add --no-cache \
            libusb-dev \
            py3-magic \
 && adduser -D cobra \
 && mkdir /usr/app \
 && chown cobra:cobra /usr/app
WORKDIR /usr/app

# Подготовка кода и окружения
COPY --chown=cobra:cobra --from=build /usr/app/venv ./venv
COPY --chown=cobra:cobra /factory .
COPY --chown=cobra:cobra --chmod=700 docker.entrypoint.sh entrypoint.sh

# Sec
USER cobra
ENV PATH="/usr/app/venv/bin:$PATH"
EXPOSE 8000

# Переменные среды
ENV TELEGRAM_TOKEN=qwe
ENV CELERY_ENDPOINT='redis://user:pass@redis:6379'

# Запуск
RUN SECRET_KEY=qwe python /usr/app/manage.py collectstatic --noinput --clear --link
ENTRYPOINT ["/usr/app/entrypoint.sh"]
CMD ["--bind", "0.0.0.0:8000", "--workers=1"]
