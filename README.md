# Procesamiento de Datos con Apache Spark y Kafka

## Descripción

Este proyecto implementa un sistema de análisis de datos en batch y en tiempo real utilizando Apache Spark y Apache Kafka.

## Dataset

Se utilizó un dataset de salarios que incluye variables como:

* job_title
* experience_years
* education_level
* industry
* salary

## Procesamiento en Batch

Se cargó un archivo CSV y se realizaron análisis como:

* Promedio general de salario
* Promedio por tipo de trabajo
* Promedio por nivel educativo

## Procesamiento en Tiempo Real

Se simuló la llegada de datos mediante Kafka y se procesaron con Spark Streaming en micro-batches.

## Ejecución

### 1. Iniciar Zookeeper

/opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties

### 2. Iniciar Kafka

/opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties

### 3. Ejecutar Producer

python3 kafka_producer.py

### 4. Ejecutar Streaming

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_streaming_consumer.py

### 5. Ejecutar Batch

spark-submit batch_processing.py
