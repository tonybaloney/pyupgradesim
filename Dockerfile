ARG VERSION=3.11
FROM python:${VERSION}-slim-buster
COPY benchsite /app

WORKDIR /app
RUN python -m pip install -r requirements.txt

CMD python manage.py migrate && python manage.py loaddata seed.json && python -m gunicorn benchsite.wsgi:application --bind 0.0.0.0:8900 -w 4