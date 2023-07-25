ARG KAFKA_VERSION=2.13-3.4.0

FROM python-jdk:python-3.10.11-jdk-11.10.16

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wget
ARG KAFKA_VERSION
RUN wget --no-verbose -O apache-kafka.tgz https://dlcdn.apache.org/kafka/3.4.0/kafka_${KAFKA_VERSION}.tgz
RUN mkdir -p /opt/kafka
RUN tar -xf apache-kafka.tgz -C /opt/kafka --strip-components=1
RUN rm -rf apache-kafka.tgz

WORKDIR /opt/kafka

RUN cd /opt/kafka
RUN mkdir data
RUN mkdir data/metadata-logs
RUN mkdir data/kraft-combined-logs
RUN mkdir logs

ENV LOG_DIR=/opt/kafka/logs

COPY ./start-kafka.sh /opt/kafka/

CMD ["bash", "start-kafka.sh"]