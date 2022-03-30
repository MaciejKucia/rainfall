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

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8081", "rainfall.app:app"]
