# API Maker

**Asynchronous API queries made with passion.**


## The Set Up

### Pipenv
  **`/Pipfile`**
  ```Pipfile
    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    fastapi = "*"
    uvicorn = "*"
    pydantic = "*"

    [dev-packages]
    mypy = "*"
    pytest = "*"

    [requires]
    python_version = "3.9"
  ```

  - If you haven't already install pipenv
    - `$ pip3 install pipenv`
  - Once pipenv is installed you just have to create the directory and start a shell...
    - `$ mkdir new_project`
    - `$ cd new_project`
    - `$ pipenv shell`
    - `$ exit`
    - `$ pipenv install`


### Docker
  **`/Dockerfile`**
  ```Dockerfile
    FROM python:3.9-alpine AS base

    # Environment var created in docker-compose.yml
    ARG ENVIRONMENT

    # This is to create a virtual environment
    ENV PYROOT /pyroot
    ENV PYTHONUSERBASE ${PYROOT}
    ENV PATH=${PATH}:${PYROOT}/bin

    # This is to install pipenv
    RUN PIP_USER=1 pip install pipenv
    COPY Pipfile* ./

    # If the environment is test, install dev dependencies
    # else install only prod dependencies
    RUN if [ "$ENVIRONMENT" = "test" ]; then PIP_USER=1 pipenv install --system --deploy --ignore-pipfile --dev; \
        else PIP_USER=1 pipenv install --system --deploy --ignore-pipfile; fi



    FROM python:3.9-alpine

    # This is the final image that will be used in production

    ENV PYROOT /pyroot
    ENV PYTHONUSERBASE ${PYROOT}
    ENV PATH=${PATH}:${PYROOT}/bin

    # This is to avoid creating .pyc files
    ENV PYTHONDONTWRITEBYTECODE 1

    # This is to avoid buffering stdout and stderr
    RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
    COPY --chown=myapp:user --from=base ${PYROOT}/ ${PYROOT}/

    # Create the app directory
    RUN mkdir -p /usr/src/app/
    WORKDIR /usr/src

    # Copy the app code
    COPY --chown=myapp:user app ./app

    USER 1234

    # The final command to run the app
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
  ```

  - Build the image...
    - `$ docker build -t api_maker_dock:latest .`
  - Build the container...
    - `$ docker run --name api_maker_cont -p 8080:8080 api_maker_dock:latest`
  - After running this for the first time continue using this command...
    - `$ docker rm api_maker_cont && docker build -t api_maker_dock:latest . && docker run --name api_maker_cont -p 8080:8080 api_maker_dock:latest`


  **`/docker-compose.yml`**
  ```yaml
    version: "3"

    services:
      app:
        build:
          context: .
          args:
            - ENVIRONMENT=local
        ports:
          - "8080:8080"
        entrypoint: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
        volumes:
          - ./app:/usr/src/app


    # Testing environment
      app-test:
        build:
          context: .
          args:
            - ENVIRONMENT=test
        volumes:
          - .:/usr/src    
  ```
  - Once the docker-compose.yml file is created use the following command to build and run the image/container
    - `$ docker-compose up --build`
  - To run tests against the live docker container run:
    - `$ docker-compose down`
    - `$ docker-compose up --build -d`
  - Now that the docker container is running you can run the tests against it and continue development...
    - `$ docker-compose exec -T app-test pytest tests`


## Other Dependencies

### Development
  - fastapi
  - uvicorn
  - pydantic
### Testing
  - mypy
  - pytest
  - pytest-asyncio
  - pytest-cov
    - `pytest --cov=app tests/`


