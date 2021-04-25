FROM python:3.9.4-alpine

WORKDIR /usr/src/app

COPY app .
COPY config.json .

CMD [ "python", "./main.py" ]