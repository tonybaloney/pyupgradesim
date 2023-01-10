ARG VERSION=3.11
FROM python:${VERSION}-slim-buster
COPY benchsite /app

WORKDIR /app
RUN python -m pip install -r requirements.txt && rm -f db.sqlite3 && python manage.py migrate && python manage.py loaddata seed.json

CMD gunicorn benchsite.wsgi:application --bind 0.0.0.0:80 -w 4