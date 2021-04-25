FROM python:3.6.13-alpine

WORKDIR /usr/src/app

COPY app/* .

CMD [ "python", "./main.py" ]