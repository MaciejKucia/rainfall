# rainfall

Rainfall is a Python-based HTTP microservice.

Project dependencies are managed by [poetry](https://python-poetry.org/).

## Lint and test

```bash
pip3 install --user tox-poetry
tox
```

## Run the development server

```bash
poetry run python -m rainfall
curl -v http://localhost:8081/health
```

## Run the production server

```bash
poetry run gunicorn --workers 4 --bind 0.0.0.0:8081 rainfall.app:app
curl -v http://localhost:8081/health
```
