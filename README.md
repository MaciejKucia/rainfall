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
curl -v http://localhost:8080/health
```

## Run the production server

```bash
poetry run gunicorn --workers 4 --bind 0.0.0.0:8080 \
  --access-logfile - --access-logformat "{\"remote_ip\":\"%(h)s\",\"request_id\":\"%({X-Request-Id}i)s\",\"response_code\":\"%(s)s\",\"request_method\":\"%(m)s\",\"request_path\":\"%(U)s\",\"request_querystring\":\"%(q)s\",\"request_timetaken\":\"%(D)s\",\"response_length\":\"%(B)s\"}" \
  rainfall.__main__:app
curl -v http://localhost:8080/health
```

## Build and run container

```bash
docker build . -t mkucia/rainfall:latest
```

```bash
docker run -it -p8080:8080 mkucia/rainfall:latest
curl -v http://localhost:8080/health
```
