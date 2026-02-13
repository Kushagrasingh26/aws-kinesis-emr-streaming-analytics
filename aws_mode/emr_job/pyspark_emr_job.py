from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, count as _count, sum as _sum

spark = SparkSession.builder.appName("EMRStreamingAnalytics").getOrCreate()

# Placeholder: In real EMR, connect to Kinesis via Spark connector.
# For GitHub, we show transformation logic that would run once data is landed in S3.

df = spark.read.json("s3://YOUR_BUCKET/landing/events/")

agg = (
    df.withColumn("event_ts", col("event_time").cast("timestamp"))
    .groupBy(window(col("event_ts"), "5 minutes"), col("event_type"))
    .agg(_count("*").alias("event_count"), _sum("amount").alias("total_amount"))
)

agg.write.mode("overwrite").parquet("s3://YOUR_BUCKET/curated/analytics/")
