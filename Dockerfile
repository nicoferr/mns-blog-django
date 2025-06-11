FROM python:3-slim

RUN apt-get update && apt-get dist-upgrade -y
RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

## Gunicorn permet de lancer le projet comme en production, contrairement à "py manage.py runserver" qui est un serveur DEV
## psycopg2 est le driver de db PostgreSQL
RUN pip install --no-cache-dir gunicorn psycopg2-binary

COPY . .

RUN mkdir -p /app/static
RUN chown -R appuser /app

USER appuser

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"]
