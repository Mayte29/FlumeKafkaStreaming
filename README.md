# FlumeKafkaStreaming
Práctica Flume Kafka Streaming

.He creado una carpeta en /opt llamada practica-flume donde he guardado el fichero agentePractica.conf que adjunto.

.Para lanzar el agente Flume lanzar este comando:

flume-ng agent --conf ./conf --conf-file /opt/practica-flume/agentePractica.conf -name a1 -Dflume.root.logger=INFO,console
