from pyspark.sql import SparkSession
from datetime import date
from utils.common import create_spark_session

today = date.today().strftime("%b-%d-%Y")


if __name__ == "__main__":

    spark = create_spark_session(
        app_name='Test Deltalake',
        s3_access_key="minioadmin",
        s3_secret_key="minioadmin",
        s3_endpoint="http://minio:9000",
        executeor_memory="2G",
        executor_cores="2",
        driver_memory="2G",
        driver_cores="2"
    )

    table_name = 'Customer'
    data = [("John", "Doe", 25), ("Jane", "Doe", 23), ("Bob", "Smith", 30)]
    columns = ["first_name", "last_name", "age"]
    df = spark.createDataFrame(data, columns)
    print("processing data")
    df.show()
    print("DONE")
    df.write.format("delta").mode("overwrite").save("s3a://delta-lake/test-delta-table")# for table_name in tables_names:
    print(f"{table_name} table done!")

    delta_path = "s3a://delta-lake/test-delta-table"
    df_load = spark.read.format("delta").load(delta_path)
    df_load.show()

    spark.stop()
