from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Training').getOrCreate()
df = spark.read.csv("Python3/Pyspark/Houserent.csv", header=True)
print(df.show())