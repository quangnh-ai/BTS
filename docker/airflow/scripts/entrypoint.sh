#!/bin/bash

airflow db migrate


case "$1" in
    webserver)
        airflow users create \
            --username "$AIRFLOW_DEFAULT_USERNAME" \
            --firstname "$AIRFLOW_DEFAULT_FIRST_NAME" \
            --lastname "$AIRFLOW_DEFAULT_LAST_NAME" \
            --role Admin \
            --email "$AIRFLOW_DEFAULT_EMAIL" \
            --password "$AIRFLOW_DEFAULT_PASSWORD"
        airflow webserver
        ;;
    scheduler)
        airflow scheduler
        ;;
    worker)
        airflow celery worker
        ;;
    flower)
        airflow celery flower
        ;;
esac