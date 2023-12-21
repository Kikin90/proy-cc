# syntax=docker/dockerfile:1
FROM python:alpine3.17
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/