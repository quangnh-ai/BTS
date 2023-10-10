FROM spark:3.3.2-hadoop-3

ENV AIRFLOW_HOME=/opt/airflow
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

RUN mkdir /opt/airflow
WORKDIR /opt/airflow

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm -rf /opt/airflow/requirements.txt

RUN mkdir logs
RUN mkdir dags
RUN mkdir plugins
RUN useradd -ms /bin/bash airflow


RUN chown -R airflow: ${AIRFLOW_HOME}
USER airflow

COPY ./entrypoint.sh entrypoint.sh
ENTRYPOINT [ "/opt/airflow/entrypoint.sh" ]