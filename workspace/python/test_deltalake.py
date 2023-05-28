from pyspark.sql import SparkSession
from datetime import date
# from utils.common import create_spark_session

today = date.today().strftime("%b-%d-%Y")


if __name__ == "__main__":

    spark_session = (
        SparkSession.builder
        .appName('Test Deltalake')
        .master('spark://spark-master:7077') 
        .config("spark.executor.memory", '2G')
        .config("spark.executor.cores", '2')
        .config("spark.driver.memory", '2G')
        .config("spark.driver.cores", '2')
        .config("spark.hadoop.fs.s3a.access.key", 'minioadmin')
        .config("spark.hadoop.fs.s3a.secret.key", 'minioadmin')
        .config("fs.s3a.endpoint", "http://minio:9000")
        .config("fs.s3a.connection.ssl.enabled", "false")
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config('spark.jars','/opt/spark/jars/aws-java-sdk-bundle-1.11.1026.jar')
        .config('spark.jars','/opt/spark/jars/hadoop-aws-3.3.2.jar')
        .config('spark.jars','/opt/spark/jars/delta-core_2.12-2.3.0.jar')
        .config('spark.jars', '/opt/spark/jars/delta-storage-2.3.0.jar')
        .getOrCreate()
    )
    spark_session.sparkContext.setLogLevel("ERROR")

    table_name = 'Customer'
    data = [("John", "Doe", 25), ("Jane", "Doe", 23), ("Bob", "Smith", 30)]
    columns = ["first_name", "last_name", "age"]
    df = spark_session.createDataFrame(data, columns)
    print("processing data")
    df.show()
    print("DONE")
    df.write.format("delta").mode("overwrite").save("s3a://delta-lake/test-delta-table")# for table_name in tables_names:
    print(f"{table_name} table done!")

    delta_path = "s3a://delta-lake/test-delta-table"
    df_load = spark_session.read.format("delta").load(delta_path)
    df_load.show()

    spark_session.stop()
