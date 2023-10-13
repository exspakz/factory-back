#!/usr/bin/env sh

main () {

  echo "FACTORY RUN";
  export SECRET_KEY=$(tr -dc 'a-z0-9' < /dev/urandom | head -c50);
  python manage.py makemigrations &&
  python manage.py migrate &&
  celery -A factory worker -l INFO &
  gunicorn "$@" factory.wsgi:application
	
}
main "$@"
