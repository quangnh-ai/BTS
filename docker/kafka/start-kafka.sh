#!/bin/bash

/opt/kafka/bin/kafka-storage.sh format --config /opt/kafka/config/server.properties --cluster-id ${KAFKA_CLUSTER_ID}

/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties