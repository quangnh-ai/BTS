FROM python:3.10.13-slim


ENV AIRFLOW_HOME=/airflow
ENV PYTHON_VERSION=3.10
ENV AIRFLOW_VERSION=2.7.1
ENV CONSTRAINT_URL=https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

ENV AIRFLOW_UID=50000
ENV AIRFLOW_DEFAULT_USERNAME=admin
ENV AIRFLOW_DEFAULT_PASSWORD=admin
ENV AIRFLOW_DEFAULT_FISRT_NAME=admin
ENV AIRFLOW_DEFAULT_LAST_NAME=admin
ENV AIRFLOW_DEFAULT_EMAIL=admin@admin.com

RUN apt-get update
RUN pip install "apache-airflow[redis, celery, ssh, postgres]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

RUN mkdir /airflow
WORKDIR /airflow
RUN mkdir logs
RUN mkdir dags
RUN mkdir plugins
RUN useradd -ms /bin/bash airflow


RUN chown -R airflow: ${AIRFLOW_HOME}
USER airflow

COPY ./scripts/entrypoint.sh entrypoint.sh
ENTRYPOINT [ "/airflow/entrypoint.sh" ]