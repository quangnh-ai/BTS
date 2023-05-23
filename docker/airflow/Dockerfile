ARG AIRFLOW_VERSION="2.6.1"

FROM apache/airflow:slim-${AIRFLOW_VERSION}-python3.10
USER root
# INSTALL TOOLS
RUN apt-get update \
&& apt-get -y install libaio-dev \
&& apt-get install postgresql-client

COPY requirements.txt .

USER airflow
RUN pip install -r requirements.txt
# ENTRYPOINT SCRIPT
COPY ./scripts/init.sh /init.sh

CMD ["bash", "/init.sh"]
