FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


FROM node:12-alpine AS builder
ENV PATH reactApp/app/node_modules/.bin:$PATH

RUN mkdir reactApp
WORKDIR /reactApp
COPY ./reactApp reactApp/app
COPY ./reactApp reactApp/app/package.json

RUN  npm install
RUN  npm install react

RUN adduser -D user
USER user
