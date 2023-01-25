# API Maker

**This is an application for users to experiment creating and making calls to their own API's and see how they work with the FastAPI Framework.**

#

## Pipenv
  - If you haven't already install pipenv
    - `$ pip3 install pipenv`
  - Once pipenv is installed you just have to create the directory and start a shell...
    - `$ mkdir new_project`
    - `$ cd new_project`
    - `$ pipenv shell`
    - `$ exit`
    - `$ pipenv install`


## Docker
  ```Dockerfile
    FROM python:3.9-alpine AS base
    ENV PYROOT /pyroot
    ENV PYTHONUSERBASE ${PYROOT}
    ENV PATH=${PATH}:${PYROOT}/bin
    RUN PIP_USER=1 pip install pipenv
    COPY Pipfile* ./
    RUN PIP_USER=1 pipenv install --system --deploy --ignore-pipfile
    FROM python:3.9-alpine
    ENV PYROOT /pyroot
    ENV PYTHONUSERBASE ${PYROOT}
    ENV PATH=${PATH}:${PYROOT}/bin
    RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
    COPY --chown=user:myapp --from=base ${PYROOT}/ ${PYROOT}/
    RUN mkdir -p /usr/src/app/
    WORKDIR /usr/src
    COPY --chown=user:myapp app ./app
    USER 1234
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
  ```
  - Build the image...
    - `$ docker build -t api_maker_dock:latest .`
  - Build the container...
    - `$ docker run --name api_maker_cont -p 8080:8080 api_maker_dock:latest`
  - After running this for the first time continue using this command...
    - `$ docker rm api_maker_cont && docker build -t api_maker_dock:latest . && docker run --name api_maker_cont -p 8080:8080 api_maker_dock:latest`

#

## Other Dependencies
  - ### Development
    - `fastapi`
    - `uvicorn`
    - `pydantic`
  - ### Testing
    - `pytest`
    - `mypy`

