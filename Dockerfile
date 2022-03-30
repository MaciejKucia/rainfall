FROM python:3.9.12 as BUILDER

RUN pip3 install tox-poetry poetry

WORKDIR /tmp
COPY . .
RUN tox && poetry build -f wheel

FROM python:3.9.12

LABEL org.opencontainers.image.authors="maciej@kucia.net"
EXPOSE 8081

COPY --from=BUILDER /tmp/dist/*.whl /tmp/
RUN pip3 install /tmp/*.whl

ENV CONFIG_FILE="/etc/config.yaml"
COPY config.yaml /etc/config.yaml

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8081", \
    "--access-logfile", "-", \
    "--access-logformat", "{\"remote_ip\":\"%(h)s\",\"request_id\":\"%({X-Request-Id}i)s\",\"response_code\":\"%(s)s\",\"request_method\":\"%(m)s\",\"request_path\":\"%(U)s\",\"request_querystring\":\"%(q)s\",\"request_timetaken\":\"%(D)s\",\"response_length\":\"%(B)s\"}", \
    "rainfall.__main__:app"]
