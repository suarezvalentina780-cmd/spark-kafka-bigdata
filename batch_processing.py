from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("BatchJobs").getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("job_salary_prediction_dataset.csv", header=True, inferSchema=True)

print("\n=== DATOS ORIGINALES ===")
df.show(5, truncate=False)

df = df.dropna()

print("\n=== PROMEDIO GENERAL ===")
df.select(avg("salary").alias("salario_promedio")).show()

print("\n=== SALARIO POR CARGO ===")
df.groupBy("job_title") \
  .agg(avg("salary").alias("salario_promedio")) \
  .orderBy("salario_promedio", ascending=False) \
  .show(truncate=False)

print("\n=== SALARIO POR NIVEL EDUCATIVO ===")
df.groupBy("education_level") \
  .agg(avg("salary").alias("salario_promedio")) \
  .orderBy("salario_promedio", ascending=False) \
  .show(truncate=False)

spark.stop()
