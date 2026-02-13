from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, window, sum as _sum, count as _count
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("SimulatedKinesisStreaming").getOrCreate()

schema = (
    StructType()
    .add("event_time", StringType())
    .add("user_id", StringType())
    .add("event_type", StringType())
    .add("product_id", StringType())
    .add("amount", DoubleType())
)

# Spark will tail this file as it grows
raw = (
    spark.readStream.format("text")
    .option("path", "outputs/kinesis_stream.jsonl")
    .load()
)

parsed = raw.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Windowed aggregates like streaming analytics
agg = (
    parsed.withColumn("event_ts", col("event_time").cast("timestamp"))
    .groupBy(window(col("event_ts"), "1 minute"), col("event_type"))
    .agg(
        _count("*").alias("event_count"),
        _sum("amount").alias("total_amount")
    )
)

query = (
    agg.writeStream.format("parquet")
    .option("path", "outputs/analytics_parquet")
    .option("checkpointLocation", "outputs/checkpoints")
    .outputMode("append")
    .start()
)

query.awaitTermination()
