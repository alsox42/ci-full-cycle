FROM python:3.10

RUN mkdir app
WORKDIR /app

COPY . /app

CMD [ "python", "main.py" ]


