FROM docker:latest

RUN apk update && apk upgrade
RUN apk add --no-cache python3 py3-pip
RUN apk add bash
RUN apk add git

WORKDIR /code
COPY ./requirements.dev.txt /code/requirements.dev.txt
COPY ./coffee-freaks-api-client /code/coffee-freaks-api-client
RUN pip install --ignore-installed --no-cache-dir --upgrade -r /code/requirements.dev.txt
