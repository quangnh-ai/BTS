# Building Data Lakehouse

This project is designed to construct a data lakehouse. This data lakehouse will enable organizations to store, manage, and analyze large datasets in a cost-effective, secure, and scalable manner. The data lakehouse will provide a centralized repository for all data, allowing users to easily access and query the data with a unified interface.

## Setup
1. Build base image 
```bash
docker build -t python-jdk:python-3.10.11-jdk-11.10.16 ./docker/base_image
```
2. Build Spark, jupyterlab and Airflow Local Executor docker image
```bash
docker build -t spark:3.3.2-hadoop-3 ./docker/spark
docker build -t airflow:2.6.1-python-3.10 ./docker/airflow
docker build -t jupyterlab:python-3.10.11-spark-3.3.2 ./docker/jupyterlab
```
3. Deploy Platform

```bash
docker compose -f {name-to-file-compose-file}.yaml up -d
```
  - Create a bucket in minio to store our data (name it datalake)
  - Check and create folder `dag` in `workspace` folder if it not exists
  - Install jar files needed for our spark project

## Information and accout of the platform

- **Spark master UI:**    http://localhost:8080
- **Spark worker a UI:**  http://localhost:9091
- **Spark worker b UI:**  http://localhost:9092
- **Minio:**  http://localhost:9090 (username: `minioadmin`, password: `minioadmin`)
- **AirFlowLocalExecutor:** http://localhost:9099/login/  (username: `admin`, password: `airflow`)
- **MySQL:** http://localhost:3306  (username: `user`, password: `password`)
- **JupyterLab:** http://localhost:8888  (password: `admin123`)

## Example for spark-submit
```
docker exec -it master spark-submit --master spark://master:7077 \
        --deploy-mode client \
        --executor-memory 1G \
        --executor-cores 2 \
        /opt/workspace/demo_write_to_s3.py
```

## Built With
- Spark
- Minio
- Kafka
- Delta Lake
- Airflow
- Jupyterlab

