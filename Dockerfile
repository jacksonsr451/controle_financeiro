# pull official base image
FROM python:3.9.5-slim-buster

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

ENV CONTAINER_HOME=/usr/www

COPY ./ /usr/www

# set work directory
WORKDIR $CONTAINER_HOME

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry install

RUN poetry run flask db upgrade
