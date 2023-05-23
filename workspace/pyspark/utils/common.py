from pyspark.sql import SparkSession

def create_spark_session(
        app_name: str="",
        s3_access_key: str="minioadmin",
        s3_secret_key: str="minioadmin",
        s3_endpoint: str="http://minio:9000",
        executeor_memory: str="2G",
        executor_cores: str="2",
        driver_memory: str="2G",
        driver_cores: str="2"
):
    spark_session = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.executor.memory", executeor_memory)
        .config("spark.executor.cores", executor_cores)
        .config("spark.driver.memory", driver_memory)
        .config("spark.driver.cores", driver_cores)
        .config("spark.hadoop.fs.s3a.access.key", s3_access_key)
        .config("spark.hadoop.fs.s3a.secret.key", s3_secret_key)
        .config("fs.s3a.endpoint", s3_endpoint)
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
    spark_session.sparkContext.setLogLevel("ERROR")
    return spark_session