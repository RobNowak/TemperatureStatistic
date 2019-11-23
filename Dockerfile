# Dockerfile to create a docker container to measure the temperature with a DS18B20
FROM alpine:3.10.3

RUN apk add --no-cache python3

RUN pip install prometheus_client

COPY temperature_statistic.py TemperatureStatistic/temperature_statistic.py

EXPOSE 8000

ENTRYPOINT ["/usr/bin/python", "TemperatureStatistic/temperature_statistic.py"]
