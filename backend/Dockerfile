# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11

EXPOSE 80 8000

RUN apt -y update
RUN apt -y install pkg-config python3-dev


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV DB_HOST=db_postgres

# Set the default directory where CMD will execute
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD ./backend/pyproject.toml /usr/src/app/
ADD ./backend/poetry.lock /usr/src/app/
# System Deps
# RUN apt-get update && apt-get install && apt-get clean
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
ADD ./backend/ /usr/src/app/

RUN poetry run python manage.py makemigrations accounts --noinput
RUN poetry run python manage.py makemigrations --noinput

