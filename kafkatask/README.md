Requirements for this task:
-kafka
-kafka-python package (pip install kafka-python)


Process to execute:
-Go to the kafka server location and open cmd prompt
-Start zookeeper (bin/windows/zookeeper-server-start.bat config/zookeeper.properties)
-start Kafka broker (bin/windows/kafka-server-start.bat config/server.properties)
-Create topic using topic.py fi
-Start producer using producer.py file (now data is being sent to producer line by line from the given csv file)
-Start Consumer using consumer.py file in another cmd prompt/ide window (you can now see the data which is being sent via the producer)
