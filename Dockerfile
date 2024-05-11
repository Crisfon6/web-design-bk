FROM python:3.9.5-slim

WORKDIR /app

# Install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    musl-dev \
    postgresql \
    libpq-dev

COPY ./api /app

RUN pip install --no-cache-dir -r requirements.txt


