ARG SPARK_VERSION=3.1.1
ARG HADOOP_VERSION=3.2

FROM python-jdk:python-3.10.11-jdk-11.10.16

ENV SPARK_HOME=/opt/spark
ENV PATH=${SPARK_HOME}/bin:${PATH}
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

RUN apt-get install -y wget \
                       curl \
                       nano \ 
                       procps \
                       build-essential \
                       libreadline-gplv2-dev \
                       libncursesw5-dev \
                       libssl-dev \
                       libsqlite3-dev \
                       tk-dev \
                       libgdbm-dev \
                       libc6-dev \
                       libbz2-dev \
                       libffi-dev \
                       zlib1g-dev

ARG SPARK_VERSION
ARG HADOOP_VERSION
RUN wget --no-verbose -O apache-spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mkdir -p /opt/spark && \
    tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 && \
    rm -rf apache-spark.tgz

WORKDIR /opt/spark

RUN pip install pyspark==3.2.1
RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.1/delta-core_2.12-1.0.1.jar
RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar
RUN wget -P /opt/spark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar
RUN wget -P /opt/spark/jars https://jdbc.postgresql.org/download/postgresql-42.3.5.jar


RUN mkdir -p ${SPARK_LOG_DIR} && \
    touch ${SPARK_MASTER_LOG} && \
    touch ${SPARK_WORKER_LOG} && \
    ln -sf /dev/stdout ${SPARK_MASTER_LOG} && \
    ln -sf /dev/stdout ${SPARK_WORKER_LOG}

COPY ./start-spark.sh /opt/spark/

CMD ["bash", "start-spark.sh"]