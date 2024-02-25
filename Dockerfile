FROM python:3.9.13-slim

RUN apt-get update && apt-get install -y postgresql libpq-dev python-dev gcc

COPY requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install pyproject-toml && pip install -r requirements.txt

COPY app /app

WORKDIR /app

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
