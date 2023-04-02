FROM python:3.11-alpine

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./coffee-freaks-api-client /code/coffee-freaks-api-client
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install "uvicorn[standard]"
COPY app /code/app

CMD ["uvicorn", "main:app", "--app-dir", "app"]