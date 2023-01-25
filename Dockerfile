FROM python:3.9-alpine AS base

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

RUN mkdir -p /usr/src/app/app

WORKDIR /usr/src/app
COPY app ./app
COPY main.py ./

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
USER user

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

