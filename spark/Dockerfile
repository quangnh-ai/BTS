ARG SPARK_VERSION=3.3.2
ARG HADOOP_VERSION=3

FROM python-jdk:python-3.11.3-jdk-11.10.16

ENV SPARK_HOME=/opt/spark
ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV SPARK_LOG_DIR=/opt/spark/logs
ENV SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out
ENV SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out
ENV SPARK_WORKER_WEBUI_PORT=8080
ENV SPARK_WORKER_PORT=7000
ENV SPARK_MASTER_URL=spark://spark-master:7077
ENV SPARK_MODE=master

RUN apt-get update && apt-get upgrade -y


RUN apt-get update && apt-get install -y --no-install-recommends wget

ARG SPARK_VERSION
ARG HADOOP_VERSION
RUN wget --no-verbose -O apache-spark.tgz https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mkdir -p /opt/spark && \
    tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 && \
    rm -rf apache-spark.tgz

WORKDIR /opt/spark

RUN mkdir -p ${SPARK_LOG_DIR} && \
    touch ${SPARK_MASTER_LOG} && \
    touch ${SPARK_WORKER_LOG} && \
    ln -sf /dev/stdout ${SPARK_MASTER_LOG} && \
    ln -sf /dev/stdout ${SPARK_WORKER_LOG}

COPY ./start-spark.sh /opt/spark/
COPY ./install-package.sh /opt/spark/

CMD ["bash", "start-spark.sh"]