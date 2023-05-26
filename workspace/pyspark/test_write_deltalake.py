import pyspark

spark = (
    pyspark.sql.SparkSession.builder.master('spark://spark-master:7077') 
    .appName("test_deltalake") 
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin")
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("sark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config("spark.jars", "./jars/delta-core_2.12-1.0.1.jar")
    .config("spark.jars", "./jars/hadoop-aws-3.2.0.jar")
    .config("spark.jars", "./jars/aws-java-sdk-bundle-1.11.375.jar")
    .getOrCreate()
)

data = spark.range(0, 5)
data.write.format("delta").save("s3a://delta-lake/test-delta-table-jupyter")

spark.stop()