from pyspark.sql import SparkSession
from datetime import date

today = date.today().strftime("%b-%d-%Y")

spark = (
    SparkSession.builder
    .appName('Test Deltalake')
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin")
    .config("fs.s3a.endpoint", "http://minio:9000")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("fs.s3a.connection.ssl.enabled", "false")
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config('spark.jars','/opt/spark/jars/aws-java-sdk-bundle-1.11.375.jar')
    .config('spark.jars','/opt/spark/jars/hadoop-aws-3.2.0.jar')
    .config('spark.jars','/opt/spark/jars/delta-core_2.12-1.0.1.jar')
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

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
