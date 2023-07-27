FROM python:3.10.11
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip && pip install poetry==1.3.1

COPY poetry.lock pyproject.toml /app/

RUN poetry export -f requirements.txt -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install --require-hashes -r requirements.txt && \
    pip install gunicorn==20.1.0 && \
    pip uninstall --yes poetry
