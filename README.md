# Procesamiento de Datos con Apache Spark y Kafka

## Descripción
Este proyecto implementa un sistema de procesamiento de datos en batch y en tiempo real utilizando Apache Spark y Apache Kafka.

## Dataset
Se utilizó un dataset de salarios con las siguientes variables:
- job_title
- experience_years
- education_level
- skills_count
- industry
- company_size
- location
- remote_work
- certifications
- salary

## Procesamiento en Batch
Se realizó:
- Carga de datos desde CSV
- Limpieza de datos (eliminación de valores nulos)
- Cálculo de salario promedio
- Análisis por tipo de trabajo y nivel educativo

## Procesamiento en Tiempo Real
Se implementó:
- Kafka como sistema de mensajería
- Producer para simular datos
- Spark Streaming para procesar datos en micro-batches

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

## Resultados
Se obtuvieron promedios de salario y análisis de datos en tiempo real mediante micro-batches.
