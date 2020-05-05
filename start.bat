manage.py collectstatic -v 3 --force-color --noinput
daphne -b 0.0.0.0 -p 25565 web.asgi:application