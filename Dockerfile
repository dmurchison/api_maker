FROM python:3.9-alpine AS base



# Environment var created in docker-compose.yml
ARG ENVIRONMENT

# This is to create a virtual environment
ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

# This is to avoid creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

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
ENV PYTHONDONTWRITEBYTECODE=1

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

