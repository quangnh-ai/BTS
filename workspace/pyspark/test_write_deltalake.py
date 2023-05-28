import pyspark
from pyspark.sql import SparkSession

spark_session = (
    SparkSession.builder
    .appName('Test Deltalake')
    .config("spark.executor.memory", '2G')
    .config("spark.executor.cores", '2')
    .config("spark.driver.memory", '2G')
    .config("spark.driver.cores", '2')
    .config("spark.hadoop.fs.s3a.access.key", 'minioadmin')
    .config("spark.hadoop.fs.s3a.secret.key", 'minioadmin')
    .config("fs.s3a.endpoint", "http://minio:9000")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("fs.s3a.connection.ssl.enabled", "false")
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

data = spark_session.range(0, 5)
data.write.format("delta").save("s3a://delta-lake/test-delta-table-jupyter")

spark_session.stop()