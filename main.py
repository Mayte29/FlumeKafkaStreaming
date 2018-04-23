from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

if __name__ == "__main__":

    # Crear el Spark Context para conectar con el cluster de Spark
    sparkContext = SparkContext(appName="PythonStreamingKafkaTweetCount")

    # Establecer el Intervalo del Batch del Contexto de Streaming. (Ejemplo: 15 segundos)
    streamingContext = StreamingContext(sparkContext, 15)

    # Crear el stream de kafka para consumir los datos de Twitter, indicando el puerto de zookeeper
    kafkaStream = KafkaUtils.createStream(streamingContext, 'localhost:2181', 'spark-streaming', {'twitter': 1})

    # APARTADO A: Parsear los tweets como un json
    parsed = kafkaStream.map(lambda v: json.loads(v[1]))

    # APARTADO B: Contar el número de tweets por usuario
    tweetsNumberByUser = parsed.map(lambda tweet: (tweet['user']["screen_name"], 1)).reduceByKey(lambda x, y: x + y)

    # APARTADO C: Contar el número de tweets por ventana de tiempo
    tweetsNumberByTimeWindo = kafkaStream.countByWindow(60, 5).map(lambda x: ('Tweets totales (agrupados en un minuto): %s' % x))

    # APARTADO D: Obtener los autores y mostrarlos
    authors = parsed.map(lambda tweet: tweet['user']['screen_name'])
    authors.pprint()

    # Mostrar el número de tweets por usuario
    tweetsCountsByUser.pprint()

    return streamingContext

# Start Execution of Streams
streamingContext.start()
streamingContext.awaitTermination()