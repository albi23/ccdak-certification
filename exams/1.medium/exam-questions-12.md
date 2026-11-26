## Question 1 (Kafka Setup and Operations):
Which command can be used to create a Kafka topic to store your events?

- A. bin/zookeeper-topics.sh --create --topic first-topic --bootstrap-server localhost:9092
- B. bin/topics.sh --create --topic first-topic --bootstrap-server localhost:9092
- C. bin/kafka-topics.sh --create --topic first-topic --bootstrap-server localhost:9092
- D. bin/kafka-topics.sh --describe --topic first-topic --bootstrap-server localhost:9092

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, events are organized and stored in topics. A topic is identified by its name and you can have as many topics as you want. Before you can write your first events, you must create a topic with the following command: bin/kafka-topics.sh –create –topic first-topic –bootstrap-server localhost:9092 Configurations pertinent to topics have both a server default as well an optional per-topic override. If no per-topic configuration is given the server default is used (server.properties file). The override can be set at topic creation time by giving one or more –config options. The following example creates a topic named first-topic with a custom max message size as well as two partitions and a replication factor of three: bin/kafka-topics.sh –create –topic first-topic –bootstrap-server localhost:9092 –partitions 2 \ –replication-factor 3 –config max.message.bytes=64000 Further reading: Topic Configuration.

**Detailed explanation of each option:**

1. ❌ **A. bin/zookeeper-topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

2. ❌ **B. bin/topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

3. ✅ **C. bin/kafka-topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Correct**.

4. ❌ **D. bin/kafka-topics.sh --describe --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

</details>

## Question 2 (Kafka Producers):
Which of the following options are true for Kafka producers?

- A. Kafka producers have no need for group coordination.
- B. Kafka producers send a produce request to the leader of a topic partition.
- C. Kafka guarantees that all producer messages will be sent to the same partition.
- D. Kafka producers can send data with a key, in which case the data will be send round-robin to all available brokers.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

In Kafka, producers create and write messages to topic partitions. Some concepts of producers are: – Producers are conceptually much simpler than consumers since they have no need for group coordination. – Producers automatically know to which broker and partition to write to. – A producer partitioner maps each message to a topic partition, and the producer sends a produce request to the leader of that partition. – The partitioners shipped with Kafka guarantee that all messages with the same non-empty key will be sent to the same partition. – If producers send data without a key, then the data will be send round-robin to all available brokers. – Producers can choose to receive acknowledgement of data writes. Further reading: Producer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Kafka producers have no need for group coordination.**  
   **Correct**.

2. ✅ **B. Kafka producers send a produce request to the leader of a topic partition.**  
   **Correct**.

3. ❌ **C. Kafka guarantees that all producer messages will be sent to the same partition.**  
   **Incorrect**.

4. ❌ **D. Kafka producers can send data with a key, in which case the data will be send round-robin to all available brokers.**  
   **Incorrect**.

</details>

## Question 3 (Programming & Serialization):
Which of the following options are Avro primitive types?

- A. string
- B. bytes
- C. timestamp
- D. null

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

In Avro, primitive types have no specified attributes. The set of primitive type names is: – null: no value – boolean: a binary value – int: 32-bit signed integer – long: 64-bit signed integer – float: single precision (32-bit) IEEE 754 floating-point number – double: double precision (64-bit) IEEE 754 floating-point number – bytes: sequence of 8-bit unsigned bytes – string: unicode character sequence Further reading: Avro Primitive Types.

**Detailed explanation of each option:**

1. ✅ **A. string**  
   **Correct**.

2. ✅ **B. bytes**  
   **Correct**.

3. ❌ **C. timestamp**  
   **Incorrect**.

4. ✅ **D. null**  
   **Correct**.

</details>

## Question 4 (Kafka Setup and Operations):
After producing to a Kafka topic, which script helps you to check whether everything worked and there is any data in the topic?

- A. bin/kafka-topic-data.sh
- B. bin/kafka-console-consumer.sh
- C. bin/kafka-console-producer.sh
- D. bin/kafka-topics.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, events are organized and stored in topics.The bin/kafka-console-consumer.sh script helps you to read data from Kafka topics and outputs it to standard output.To read all available messages from a topic test_topic you can use the following command:bin/kafka-console-consumer.sh –bootstrap-sever localhost:9092 –from-beginning –topic test_topic

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-topic-data.sh**  
   **Incorrect**.

2. ✅ **B. bin/kafka-console-consumer.sh**  
   **Correct**.

3. ❌ **C. bin/kafka-console-producer.sh**  
   **Incorrect**.

4. ❌ **D. bin/kafka-topics.sh**  
   **Incorrect**.

</details>

## 🚫 Question 5 (Kafka Ecosystem):
What could be the reason if ksqlDB doesn‘t clean up its internal topics?

- A. Internal topics for ksqlDB need to be cleaned up manually.
- B. Topic deletion for ksqlDB in not configured in the sql.properties file.
- C. The property “delete.topic.enable“ is set to false.
- D. ksqlDB is not connected to the correct Kafka cluster.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

If ksqlDB doesn‘t clean up its internal topics make sure that your Kafka cluster is configured with the property delete.topic.enable=true.Further reading: ksqlDB Operations.

**Detailed explanation of each option:**

1. ❌ **A. Internal topics for ksqlDB need to be cleaned up manually.**  
   **Incorrect**.

2. ❌ **B. Topic deletion for ksqlDB in not configured in the sql.properties file.**  
   **Incorrect**.

3. ✅ **C. The property “delete.topic.enable“ is set to false.**  
   **Correct**.

4. ❌ **D. ksqlDB is not connected to the correct Kafka cluster.**  
   **Incorrect**.

</details>

## Question 6 (Kafka Consumers):
Using Kafka, how does a consumer commit an offset?

- A. Consumers produce messages to a special __consumer_offsets topic with the committed offset for each partition.
- B. Consumers store committed offsets for each partition in a local internal database.
- C. Committed offsets for each partition are stored together with the message in the original Kafka topic.
- D. Committed offsets for each partition are stored inside Zookeeper.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

As a consumer in the group reads messages from the partitions assigned by the coordinator, it must commit the offsets corresponding to the messages it has read. If the consumer crashes or is shut down, its partitions will be re-assigned to another member, which will begin consumption from the last committed offset of each partition. By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. To commit offsets the consumer produces a message to Kafka, to a special __consumer_offsets topic, with the committed offset for each partition. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Consumers produce messages to a special __consumer_offsets topic with the committed offset for each partition.**  
   **Correct**.

2. ❌ **B. Consumers store committed offsets for each partition in a local internal database.**  
   **Incorrect**.

3. ❌ **C. Committed offsets for each partition are stored together with the message in the original Kafka topic.**  
   **Incorrect**.

4. ❌ **D. Committed offsets for each partition are stored inside Zookeeper.**  
   **Incorrect**.

</details>

## Question 7 (Reliable Data Delivery):
Which of the following producer configurations best fits a company‘s requirement to have a very safe data pipeline without message loss?

- A. acks=1, replication.factor=3, min.insync.replicas=2
- B. acks=all, replication.factor=3, min.insync.replicas=2
- C. acks=all, replication.factor=2, min.insync.replicas=1
- D. acks=1, replication.factor=2, min.insync.replicas=1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To make your data fault-tolerant, safe and highly-available, every Kafka topic can be replicated, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i. e., there will always be three copies of your data. This replication is performed at the level of topic-partitions. acks=all means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. When used together, min.insync.replicas and acks allow you to enforce greater durability guarantees. A typical scenario would be to create a topic with a replication factor of 3, set min.insync.replicas to 2, and produce with acks of “all“. This will ensure that the producer raises an exception if a majority of replicas do not receive a write.

**Detailed explanation of each option:**

1. ❌ **A. acks=1, replication.factor=3, min.insync.replicas=2**  
   **Incorrect**.

2. ✅ **B. acks=all, replication.factor=3, min.insync.replicas=2**  
   **Correct**.

3. ❌ **C. acks=all, replication.factor=2, min.insync.replicas=1**  
   **Incorrect**.

4. ❌ **D. acks=1, replication.factor=2, min.insync.replicas=1**  
   **Incorrect**.

</details>

## Question 8 (Kafka Consumers):
A company disabled auto commit of offsets for their consumer application in order to have more control over the time at which offsets are committed. What‘s the simplest way to manually commit the offsets?

- A. Use the poll() API.
- B. Use the fetch() API.
- C. Use the commitSync() API.
- D. Use the close() API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. Automatic commits are convenient, but they dont give developers enough control to avoid duplicate messages. By setting auto.commit.offset=false, offsets will only be committed when the application explicitly chooses to do so. The simplest and most reliable of the commit APIs is commitSync(). This API will commit the latest offset returned by poll() and return once the offset is committed, throwing an exception if commit fails for some reason. Note: Make sure you call commitSync() after you are done processing all the records in the collection, or you risk missing messages. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Use the poll() API.**  
   **Incorrect**.

2. ❌ **B. Use the fetch() API.**  
   **Incorrect**.

3. ✅ **C. Use the commitSync() API.**  
   **Correct**.

4. ❌ **D. Use the close() API.**  
   **Incorrect**.

</details>

## Question 9 (Programming & Serialization):
A company produces Avro data on their production Kafka cluster that is integrated with the Confluent Schema Registry. After a schema change that is incompatible, the data gets rejected. Which component rejects the data?

- A. Kafka Broker
- B. Kafka Client
- C. Zookeeper
- D. Confluent Schema Registry

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Confluent Schema Registry provides a serving layer for your metadata. It provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas. It provides serializers that plug into Apache Kafka clients that handle schema storage and retrieval for Kafka messages that are sent in any of the supported formats.Schema Registry lives outside of and separately from your Kafka brokers. Your producers and consumers still talk to Kafka to publish and read data (messages) to topics. Concurrently, they can also talk to Schema Registry to send and retrieve schemas that describe the data models for the messages.Because all the schemas are stored inside the Confluent Schema Registry, that‘s the place where data gets rejected and incompatible schema changes are found.Further reading: Schema Registry Overview.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Broker**  
   **Incorrect**.

2. ❌ **B. Kafka Client**  
   **Incorrect**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ✅ **D. Confluent Schema Registry**  
   **Correct**.

</details>

## Question 10 (Kafka Internals):
If you deploy a Kafka cluster on 4 brokers and the underlying topic has a replication factor of 3 and the number of partitions for that topic are 12, on how many brokers will each partition live?

- A. 1
- B. 3
- C. 2
- D. 4

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To make your data fault-tolerant and highly-available, every Kafka topic can be replicated, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i. e., there will always be three copies of your data. This replication is performed at the level of topic-partitions.The total number of replicas including the leader constitute the replication factor.Further reading: Replication.

**Detailed explanation of each option:**

1. ❌ **A. 1**  
   **Incorrect**.

2. ✅ **B. 3**  
   **Correct**.

3. ❌ **C. 2**  
   **Incorrect**.

4. ❌ **D. 4**  
   **Incorrect**.

</details>

## Question 11 (Kafka Consumers):
Which of the following options are possible to subscribe a single consumer simultaneously to the topics orders-topic, customers-topic, sales-topic and stocks-topic?

- A. consumer.subscribe(“orders-topic“);
- B. consumer.subscribe(“customers-topic“);
- C. consumer.subscribe(“sales-topic“);
- D. consumer.subscribe(“stocks-topic“);
- E. consumer.subscribe(Arrays.asList(“orders-topic“, “customers-topic“, “sales-topic“, “stocks-topic“));
- F. consumer.subscribe(Pattern.compile(“.*topic“));

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** E, F

**Explanation:**

To begin the consumption of Kafka messages, you must first subscribe to the topics your application needs to read from. The subscribe method is not incremental: you must include the full list of topics that you want to consume from. You can change the set of topics you‘re subscribed to at any time – any topics previously subscribed to will be replaced by the new list when you call subscribe.There are the following two options to subscribe to topics.1: Subscribe to the given list of topics to get dynamically assigned partitions:public void subscribe(Collection topics)2: Subscribe to all topics matching specified pattern to get dynamically assigned partitions:public void subscribe(Pattern pattern)Further reading: Consumer API.

**Detailed explanation of each option:**

1. ❌ **A. consumer.subscribe(“orders-topic“);**  
   **Incorrect**.

2. ❌ **B. consumer.subscribe(“customers-topic“);**  
   **Incorrect**.

3. ❌ **C. consumer.subscribe(“sales-topic“);**  
   **Incorrect**.

4. ❌ **D. consumer.subscribe(“stocks-topic“);**  
   **Incorrect**.

5. ✅ **E. consumer.subscribe(Arrays.asList(“orders-topic“, “customers-topic“, “sales-topic“, “stocks-topic“));**  
   **Correct**.

6. ✅ **F. consumer.subscribe(Pattern.compile(“.*topic“));**  
   **Correct**.

</details>

## Question 12 (Kafka Setup and Operations):
Which security concept allows you to protect your data in transit instead of using the default unsecured PLAINTEXT protocol?

- A. Encryption - configured using the listener configuration and managing truststores and keystores.
- B. Authorization - configured using the LDAP Authorizer.
- C. Authentication - configured using SASL or mTLS.
- D. Encryption - configured using ACLs and RBAC.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

By default, there is no encryption or authentication, nor are ACLs configured. Any client can communicate to Kafka brokers using the PLAINTEXT port. Encrypting data in transit between brokers and applications mitigates risks for unintended interception of data across the network. Authentication and encryption are defined in Kafka per listener. By default, Kafka listeners use an unsecured PLAINTEXT protocol that is acceptable for development environments; however, all production environments should enable SSL encryption. Encryption on brokers is configured using the listener configuration and managing truststores and keystores. Further reading: Encryption with SSL.

**Detailed explanation of each option:**

1. ✅ **A. Encryption - configured using the listener configuration and managing truststores and keystores.**  
   **Correct**.

2. ❌ **B. Authorization - configured using the LDAP Authorizer.**  
   **Incorrect**.

3. ❌ **C. Authentication - configured using SASL or mTLS.**  
   **Incorrect**.

4. ❌ **D. Encryption - configured using ACLs and RBAC.**  
   **Incorrect**.

</details>

## Question 13 (Kafka Producers):
Consider the following producer example of how to use a callback: private class DemoProducerCallback implements Callback { @Override public void onCompletion(RecordMetadata recordMetadata, Exception e) { if (e != null) { e.printStackTrace(); } } } ProducerRecord record = new ProducerRecord<>(“topic“, “key“, “value“); producer.send(record, new DemoProducerCallback()); What‘s the main benefit for adding a callback when sending a record? 

- A. Receiving a success response from the broker the moment the leader replica received the message.
- B. Sending messages asynchronously and still handle error scenarios.
- C. Sending messages synchronously and still handle error scenarios.
- D. Getting the partition and the offset of the record after it was written.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In order to send messages asynchronously and still handle error scenarios, the producer supports adding a callback when sending a record. To use callbacks, you need a class that implements the org.apache.kafka.clients.producer.Callback interface, which has a single function – onCompletion(). The onCompletion() method is called when the broker response is received and if Kafka returned an error, onCompletion() will have a non null exception. The example “handles“ it by printing, but production code will probably have more robust error handling functions. Further reading: Interface Callback.

**Detailed explanation of each option:**

1. ❌ **A. Receiving a success response from the broker the moment the leader replica received the message.**  
   **Incorrect**.

2. ✅ **B. Sending messages asynchronously and still handle error scenarios.**  
   **Correct**.

3. ❌ **C. Sending messages synchronously and still handle error scenarios.**  
   **Incorrect**.

4. ❌ **D. Getting the partition and the offset of the record after it was written.**  
   **Incorrect**.

</details>

## Question 14 (Programming & Serialization):
A company wants to send binary data through the REST proxy, so the data needs to be base64 encoded. Which component needs to encode the binary data into base64?

- A. Kafka Broker
- B. Consumer
- C. Zookeeper
- D. Producer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The Confluent REST Proxy provides a RESTful interface to a Kafka cluster, making it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol or clients.The REST Proxy requires to receive data over REST that is already base64 encoded, hence it is the responsibility of the producer to encode the data.Further reading: Confluent REST APIs.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Broker**  
   **Incorrect**.

2. ❌ **B. Consumer**  
   **Incorrect**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ✅ **D. Producer**  
   **Correct**.

</details>

## Question 15 (Kafka Setup and Operations):
Using the Kafka CLI, which command can be used to display the Kafka version? 

- A. bin/zookeeper.sh --version
- B. bin/kafka.sh --version
- C. bin/kafka-topics.sh --kafka-version
- D. bin/kafka-console-producer.sh --version

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D. bin/kafka-console-producer.sh --version The --version option is supported by Kafka command-line scripts to display the Kafka version associated with the installed Kafka distribution. However, this is not the most direct or reliable way to check the version across all Kafka CLI distributions. Depending on the Kafka version, the script may not support --version as expected. Incorrect: Option A. bin/zookeeper.sh --version There is no standard Kafka CLI script named zookeeper.sh. ZooKeeper is a separate coordination service, and this is not the correct command for checking the Kafka version. Option B. bin/kafka.sh --version There is no standard Kafka CLI script named kafka.sh in the usual Kafka distribution. Therefore, this command cannot be relied upon to display the Kafka version. Option C. bin/kafka-topics.sh --kafka-version The kafka-topics.sh command manages Kafka topics, and --kafka-version is not a supported option for displaying the Kafka version. Note: In practice, Kafka distributions commonly support checking the version with a command such as bin/kafka-broker-api-versions.sh --version, or by inspecting the installed Kafka distribution and its version information. The provided answer key may be questionable because support for --version can vary by script and Kafka release.

**Detailed explanation of each option:**

1. ❌ **A. bin/zookeeper.sh --version**  
   **Incorrect**.

2. ❌ **B. bin/kafka.sh --version**  
   **Incorrect**.

3. ❌ **C. bin/kafka-topics.sh --kafka-version**  
   **Incorrect**.

4. ✅ **D. bin/kafka-console-producer.sh --version**  
   **Correct**.

</details>

## Question 16 (Kafka Core Concepts):
Which of the following options are true for Kafka messages?

- A. Messages are immutable.
- B. Messages from the same producer will always go to the same topic partition.
- C. Messages with the same key will always go to the same topic partition.
- D. Messages with keys can be modified.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Kafka messages have the following properties: – Logs are append-only and data / messages are immutable. – Messages with the same key always go to the same topic partition. – Message ordering within a partition is guaranteed, but not across topic partitions. Important note: By default, you cannot control which message keys go to which partition, it‘s only guaranteed that the same key goes to the same partition. The default strategy is to choose a partition based on a hash of the key or use round-robin algorithm if the key is null. If you need a custom algorithm to map the messages to partitions you have the following options: – Implement a custom org.apache.kafka.clients.producer.Partitioner interface. – Specify the partition number directly in the Java ProducerRecord.

**Detailed explanation of each option:**

1. ✅ **A. Messages are immutable.**  
   **Correct**.

2. ❌ **B. Messages from the same producer will always go to the same topic partition.**  
   **Incorrect**.

3. ✅ **C. Messages with the same key will always go to the same topic partition.**  
   **Correct**.

4. ❌ **D. Messages with keys can be modified.**  
   **Incorrect**.

</details>

## Question 17 (Kafka Producers):
Which of the following options prevents the consistent mapping of keys to partitions using the default partitioner?

- A. Adding an additional topic partition.
- B. Regrouping the consumer application.
- C. Deleting one of the Kafka brokers.
- D. Adding an additional producer.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka messages are key-value pairs and while it is possible to create a ProducerRecord with just a topic and a value, with the key set to null by default, most applications produce records with keys. All messages with the same key will go to the same partition. This means that if a process is reading only a subset of the partitions in a topic, all the records for a single key will be read by the same process. If a key exists and the default partitioner is used, Kafka will hash the key using the “murmur2“ algorithm, and use the result to map the message to a specific partition. The mapping of keys to partitions is consistent only as long as the number of partitions in a topic does not change. So as long as the number of partitions is constant, you can be sure that, that the same key always goes to the same partition.

**Detailed explanation of each option:**

1. ✅ **A. Adding an additional topic partition.**  
   **Correct**.

2. ❌ **B. Regrouping the consumer application.**  
   **Incorrect**.

3. ❌ **C. Deleting one of the Kafka brokers.**  
   **Incorrect**.

4. ❌ **D. Adding an additional producer.**  
   **Incorrect**.

</details>

## Question 18 (Kafka Core Concepts):
What option best describes a Kafka Broker? 

- A. A Kafka Broker is a JVM process that runs on a machine and publishes streams of events.
- B. A Kafka Broker is a JVM process that runs on a machine and subscribes to streams of events.
- C. A Kafka Broker is a JVM process that runs on a machine and hosts topics.
- D. A Kafka Broker is a JVM process that runs on a machine and helps the communication between servers and clients.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. A Kafka Broker is a JVM process that runs on a machine and hosts topics Correct because a Kafka Broker is the central server process in Kafka that manages topics and partitions, stores records, and serves producer and consumer requests. Brokers handle message persistence, replication, and coordination with ZooKeeper/KRaft for cluster management. This is the most accurate description of a Kafka Broker’s role. Incorrect Option A. Publishes streams of events Incorrect because producers publish events to topics, not brokers. Brokers store and serve these events but do not originate them. Option B. Subscribes to streams of events Incorrect because consumers subscribe to topics to read events. Brokers facilitate the storage and delivery but do not subscribe themselves. Option D. Helps communication between servers and clients Incorrect because while brokers do act as intermediaries, this description is too vague and misleading. The broker’s primary role is hosting topics and partitions, not simply “helping communication.”

**Detailed explanation of each option:**

1. ❌ **A. A Kafka Broker is a JVM process that runs on a machine and publishes streams of events.**  
   **Incorrect**.

2. ❌ **B. A Kafka Broker is a JVM process that runs on a machine and subscribes to streams of events.**  
   **Incorrect**.

3. ✅ **C. A Kafka Broker is a JVM process that runs on a machine and hosts topics.**  
   **Correct**.

4. ❌ **D. A Kafka Broker is a JVM process that runs on a machine and helps the communication between servers and clients.**  
   **Incorrect**.

</details>

## Question 19 (Kafka Connect):
Which connector configurations are mandatory for every connector using Kafka Connect?

- A. The Java class for the connector.
- B. The key and value converter set by the worker.
- C. Unique connector name.
- D. The maximum number of tasks that should be created for this connector.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

Connector configurations are simple key-value mappings. For standalone mode these are defined in a properties file and passed to the Connect process on the command line. In distributed mode, they will be included in the JSON payload for the request that creates (or modifies) the connector.Most configurations are connector dependent, so they can‘t be outlined here. However, there are a few common options:– name: Unique name for the connector. Attempting to register again with the same name will fail.– connector.class: The Java class for the connector.– tasks.max: The maximum number of tasks that should be created for this connector. The connector may create fewer tasks if it cannot achieve this level of parallelism.– key.converter: (optional) Override the default key converter set by the worker.– value.converter: (optional) Override the default value converter set by the worker.Further reading: Kafka Connect.

**Detailed explanation of each option:**

1. ✅ **A. The Java class for the connector.**  
   **Correct**.

2. ❌ **B. The key and value converter set by the worker.**  
   **Incorrect**.

3. ✅ **C. Unique connector name.**  
   **Correct**.

4. ✅ **D. The maximum number of tasks that should be created for this connector.**  
   **Correct**.

</details>

## Question 20 (Kafka Consumers):
Which of the following options best describes the concept of rebalancing a consumer group?

- A. Rebalancing a consumer group re-assigns consumers so that each consumer receives messages from all the available topic partitions.
- B. Rebalancing a consumer group re-assigns partitions so that each consumer receives messages from all the available topic partitions.
- C. Rebalancing a consumer group re-assigns consumers so that each consumer group receives a proportional share of the consumers whenever new consumers arrive and old consumers leave.
- D. Rebalancing a consumer group re-assigns partitions so that each consumer receives a proportional share of the partitions whenever new group members arrive and old members leave.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application.The partitions of all the topics are divided among the consumers in the group. As new group members arrive and old members leave, the partitions are re-assigned so that each member receives a proportional share of the partitions. This is known as rebalancing the group.Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Rebalancing a consumer group re-assigns consumers so that each consumer receives messages from all the available topic partitions.**  
   **Incorrect**.

2. ❌ **B. Rebalancing a consumer group re-assigns partitions so that each consumer receives messages from all the available topic partitions.**  
   **Incorrect**.

3. ❌ **C. Rebalancing a consumer group re-assigns consumers so that each consumer group receives a proportional share of the consumers whenever new consumers arrive and old consumers leave.**  
   **Incorrect**.

4. ✅ **D. Rebalancing a consumer group re-assigns partitions so that each consumer receives a proportional share of the partitions whenever new group members arrive and old members leave.**  
   **Correct**.

</details>

## Question 21 (Kafka Consumers):
A company is developing a new sales strategy for which the Kafka topic receives all the underlying customer asked questions. Two different departments want to process all the available messages independently from each other. How should the consumption of these messages be organized when the topic has 3 partitions and the company aims for optimal resource usage and performance?

- A. Create two consumer groups for two department applications with 6 consumers in each.
- B. Create 3 consumers in the same group, one for each partition. Split them among the department applications as needed for optimal performance and resource usage.
- C. Create 6 consumers in the same group with 3 consumers for each department application.
- D. Create two consumer groups for two department applications with 3 consumers in each.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka assigns the partitions of a topic to the consumer in a group, so that each partition is consumed by exactly one consumer in the group. Kafka guarantees that a message is only ever read by a single consumer in the group. Consumers can see the message in the order they were stored in the log. Only a single consumer from the same consumer group can access a single partition. If the number of consumers in a group exceeds the partition count, then the extra consumers remain idle. Kafka can use the idle consumers for failover. If there are more partitions than consumers, then some consumers will read from more than one partition. There should be two consumer groups, one for each department application so that all messages are delivered to both the applications. As there are 3 partitions for the topic, there should be 3 consumers in each consumer group, otherwise the extra consumers remain idle and will waste memory resources.

**Detailed explanation of each option:**

1. ❌ **A. Create two consumer groups for two department applications with 6 consumers in each.**  
   **Incorrect**.

2. ❌ **B. Create 3 consumers in the same group, one for each partition. Split them among the department applications as needed for optimal performance and resource usage.**  
   **Incorrect**.

3. ❌ **C. Create 6 consumers in the same group with 3 consumers for each department application.**  
   **Incorrect**.

4. ✅ **D. Create two consumer groups for two department applications with 3 consumers in each.**  
   **Correct**.

</details>

## Question 22 (Kafka Producers):
Consider the following producer record: ProducerRecord record = new ProducerRecord<>(“first“, “second“, “third“); Which of the three producer record arguments is the message key? 

- A. second
- B. first
- C. third

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka‘s ProducerRecord is a key / value pair to be sent to Kafka. This consists of a topic name to which the record is being sent, an optional partition number, and an optional key and value. If a valid partition number is specified that partition will be used when sending the record. If no partition is specified but a key is present a partition will be chosen using a hash of the key. If neither key nor partition is present a partition will be assigned in a round-robin fashion. The example uses the following constructor: ProducerRecord(String topic, K key, V value) -> Creates a key / value record to be sent to Kafka The following constructor could be used if you want to send the message to a specific partition: ProducerRecord(String topic, Integer partition, K key, V value) -> Creates a record to be sent to a specified topic and partition. Further reading: ProducerRecord API.

**Detailed explanation of each option:**

1. ✅ **A. second**  
   **Correct**.

2. ❌ **B. first**  
   **Incorrect**.

3. ❌ **C. third**  
   **Incorrect**.

</details>

## Question 23 (Kafka Producers):
Why can it be very challenging to add partitions later, if you are sending messages to partitions based on keys?

- A. After adding partitions later, it cannot be guaranteed that old messages with the same key will still be on the same partition.
- B. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.
- C. After adding partitions later, it cannot be guaranteed that old messages will still exist.
- D. After adding partitions later, it cannot be guaranteed that new messages with the same key will go to the same partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka messages are key-value pairs and while it is possible to create a ProducerRecord with just a topic and a value, with the key set to null by default, most applications produce records with keys. All messages with the same key will go to the same partition. This means that if a process is reading only a subset of the partitions in a topic, all the records for a single key will be read by the same process. If a key exists and the default partitioner is used, Kafka will hash the key using the “murmur2“ algorithm, and use the result to map the message to a specific partition. The mapping of keys to partitions is consistent only as long as the number of partitions in a topic does not change. So as long as the number of partitions is constant, you can be sure that, that the same key always goes to the same partition. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.

**Detailed explanation of each option:**

1. ❌ **A. After adding partitions later, it cannot be guaranteed that old messages with the same key will still be on the same partition.**  
   **Incorrect**.

2. ✅ **B. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.**  
   **Correct**.

3. ❌ **C. After adding partitions later, it cannot be guaranteed that old messages will still exist.**  
   **Incorrect**.

4. ❌ **D. After adding partitions later, it cannot be guaranteed that new messages with the same key will go to the same partition.**  
   **Incorrect**.

</details>

## Question 24 (Kafka Ecosystem):
What are the programming languages Apache Kafka is written in?

- A. PHP
- B. Scala
- C. Python
- D. Java

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Apache Kafka is a distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.It‘s open-source and developed by the Apache Software Foundation written in Scala and Java.Further reading: Apache Kafka.

**Detailed explanation of each option:**

1. ❌ **A. PHP**  
   **Incorrect**.

2. ✅ **B. Scala**  
   **Correct**.

3. ❌ **C. Python**  
   **Incorrect**.

4. ✅ **D. Java**  
   **Correct**.

</details>

## Question 25 (Programming & Serialization):
Which of the following options best describes the process of serialization and deserialization?

- A. Serialization is the process of producing key / value based Avro messages into a Kafka topic. Deserialization does the opposite of serialization, in which we consume key / value based Avro messages from a Kafka topic.
- B. Serialization is the process of converting bytes of arrays into the desired data type that are used for transmission. Deserialization does the opposite of serialization, in which we convert an object into a stream of bytes.
- C. Serialization is the process of consuming key / value based Avro messages from a Kafka topic. Deserialization does the opposite of serialization, in which we produce key / value based Avro messages into a Kafka topic.
- D. Serialization is the process of converting an object into a stream of bytes that are used for transmission. Deserialization does the opposite of serialization, in which we convert bytes of arrays into the desired data type.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When writing messages to Kafka you need to create a producer object with the properties you want to pass to the producer. Two of the three mandatory properties are (this concept is called serialization): – key.serializer: Name of a class that will be used to serialize the keys of the records we will produce to Kafka. Kafka brokers expect byte arrays as keys and values of messages. However, the producer interface allows, using parameterized types, any Java object to be sent as a key and value. This makes for very readable code, but it also means that the producer has to know how to convert these objects to byte arrays. – value.serializer: Name of a class that will be used to serialize the values of the records we will produce to Kafka. The same way you set key.serializer to a name of a class that will serialize the message key object to a byte array, you set value.serializer to a class that will serialize the message value object. The opposite properties are needed for consumers to read messages from Kafka (this concept is called deserialization): – key.deserializer / value.deserializer: Similar to the serializers defined for the producer, but rather than specifying classes that turn Java objects to byte arrays, you need to specify classes that can take a byte array and turn it into a Java object.

**Detailed explanation of each option:**

1. ❌ **A. Serialization is the process of producing key / value based Avro messages into a Kafka topic. Deserialization does the opposite of serialization, in which we consume key / value based Avro messages from a Kafka topic.**  
   **Incorrect**.

2. ❌ **B. Serialization is the process of converting bytes of arrays into the desired data type that are used for transmission. Deserialization does the opposite of serialization, in which we convert an object into a stream of bytes.**  
   **Incorrect**.

3. ❌ **C. Serialization is the process of consuming key / value based Avro messages from a Kafka topic. Deserialization does the opposite of serialization, in which we produce key / value based Avro messages into a Kafka topic.**  
   **Incorrect**.

4. ✅ **D. Serialization is the process of converting an object into a stream of bytes that are used for transmission. Deserialization does the opposite of serialization, in which we convert bytes of arrays into the desired data type.**  
   **Correct**.

</details>

## 🚫 Question 26 (Kafka Setup and Operations):
What file systems should you choose for your production deployment of Kafka?

- A. FAT12
- B. HFS
- C. ext4
- D. XFS

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

You should run Kafka on XFS or ext4. – XFS is a very high performance, scalable file system and is routinely deployed in the most demanding applications. It‘s RHEL 7 is the default file system and is supported on all architectures. – Ext4 does not scale to the same size as XFS, is fully supported on all architectures and will still continue to see active development and support. Further reading: Production Deployment.

**Detailed explanation of each option:**

1. ❌ **A. FAT12**  
   **Incorrect**.

2. ❌ **B. HFS**  
   **Incorrect**.

3. ✅ **C. ext4**  
   **Correct**.

4. ✅ **D. XFS**  
   **Correct**.

</details>

## Question 27 (Programming & Serialization):
Which of the following options best describes unit testing?

- A. Unit tests verify that end-to-end tests with other services work as expected.
- B. Unit tests verify that production deployments work as expected.
- C. Unit tests verify that isolated functional blocks of code work as expected.
- D. Unit tests verify that development environments behave as expected.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Unit testing, integration testing, and schema compatibility are all important steps in building resilient applications in a CI/CD pipeline.Unit tests run very quickly and verify that isolated functional blocks of code work as expected. They can test the logic of your application with minimal dependencies on other services.Further reading: Application Testing.

**Detailed explanation of each option:**

1. ❌ **A. Unit tests verify that end-to-end tests with other services work as expected.**  
   **Incorrect**.

2. ❌ **B. Unit tests verify that production deployments work as expected.**  
   **Incorrect**.

3. ✅ **C. Unit tests verify that isolated functional blocks of code work as expected.**  
   **Correct**.

4. ❌ **D. Unit tests verify that development environments behave as expected.**  
   **Incorrect**.

</details>

## Question 28 (Kafka Consumers):
Which offset commit strategy should be used in an at-least once consuming scenario?

- A. Commit the offsets in Kafka, after processing the data.
- B. Do not commit the offsets in Kafka, as this will be handled automatically.
- C. Commit the offsets in Kafka, during processing the data.
- D. Commit the offsets in Kafka, before processing the data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

At-least once guarantee means you will definitely receive and process every message, but you may process some messages additional times in the face of a failure.For a consumer application at-least once processing means the consumer group receives a batch of messages from Kafka, transforms these and writes the results to a database. The consumer application has enable.auto.commit set to false and is programmed to commit their offsets back to Kafka once the database write succeeds. If the consumer fails after writing the data to the database but before saving the offsets back to Kafka, it will reprocess the same records next time it runs and save them to the database once more.

**Detailed explanation of each option:**

1. ✅ **A. Commit the offsets in Kafka, after processing the data.**  
   **Correct**.

2. ❌ **B. Do not commit the offsets in Kafka, as this will be handled automatically.**  
   **Incorrect**.

3. ❌ **C. Commit the offsets in Kafka, during processing the data.**  
   **Incorrect**.

4. ❌ **D. Commit the offsets in Kafka, before processing the data.**  
   **Incorrect**.

</details>

## Question 29 (Kafka Setup and Operations):
Which of the following options is true for the kafka-console-consumer CLI? 

- A. When used with the default options it always uses the same group id.
- B. When used with the default options it uses the group id of the last created consumer group.
- C. When used with the default options it uses a random group id.
- D. When used with the default options it does not use a group id.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. When used with the default options it uses a random group id. Correct because by default, the kafka-console-consumer CLI does not require you to specify a consumer group. If you don’t provide --group, it automatically generates a random group id each time. This means the consumer will not commit offsets persistently, and every run starts fresh from the default offset behavior (usually latest unless overridden). Incorrect Option A. Incorrect because the CLI does not always use the same group id. Without explicitly setting --group, it generates a new random one each time. Option B. Incorrect because there is no concept of “last created consumer group” being reused. Consumer groups must be explicitly defined with --group. Option D. Incorrect because the CLI does use a group id — it just generates a random one if none is specified. Saying it does not use a group id at all is inaccurate.

**Detailed explanation of each option:**

1. ❌ **A. When used with the default options it always uses the same group id.**  
   **Incorrect**.

2. ❌ **B. When used with the default options it uses the group id of the last created consumer group.**  
   **Incorrect**.

3. ✅ **C. When used with the default options it uses a random group id.**  
   **Correct**.

4. ❌ **D. When used with the default options it does not use a group id.**  
   **Incorrect**.

</details>

## Question 30 (Reliable Data Delivery):
How could you guarantee that each message in Kafka will be written to an external system exactly once?

- A. Writing results to a system that has support for unique keys.
- B. Using record.topic() + record.partition() as the unique message key.
- C. Using the consumer configuration “enable.idempotence=true“.
- D. Filtering keys with the Kafka Streams API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Some applications require not just at-least-once semantics (meaning no data loss), but also exactly-once semantics. While Kafka does not provide full exactly-once support at this time, consumers have few tricks available that allow them to guarantee that each message in Kafka will be written to an external system exactly once.The easiest and probably most common way to do exactly-once is by writing results to a system that has some support for unique keys. This includes all key-value stores, all relational databases, Elasticsearch, and probably many more data stores. When writing results to a system like a relational database or Elasticsearch, either the record itself contains a unique key (this is fairly common), or you can create a unique key using the topic, partition, and offset combination, which uniquely identifies a Kafka record.If you write the record as a value with a unique key, and later you accidentally consume the same record again, you will just write the exact same key and value. The data store will override the existing one, and you will get the same result that you would without the accidental duplicate. This pattern is called idempotent writes and is very common and useful.

**Detailed explanation of each option:**

1. ✅ **A. Writing results to a system that has support for unique keys.**  
   **Correct**.

2. ❌ **B. Using record.topic() + record.partition() as the unique message key.**  
   **Incorrect**.

3. ❌ **C. Using the consumer configuration “enable.idempotence=true“.**  
   **Incorrect**.

4. ❌ **D. Filtering keys with the Kafka Streams API.**  
   **Incorrect**.

</details>

## Question 31 (Kafka Setup and Operations):
What‘s the use of the Kafka Admin API?

- A. The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects.
- B. The Admin API supports managing Zookeeper configuration.
- C. The Admin API supports managing the producer and consumer communication.
- D. The Admin API supports managing background processes for overall performance tuning.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects. To use the Admin API, add the following Maven dependency to your Java project: org.apache.kafka kafka-clients 2.8.0

**Detailed explanation of each option:**

1. ✅ **A. The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects.**  
   **Correct**.

2. ❌ **B. The Admin API supports managing Zookeeper configuration.**  
   **Incorrect**.

3. ❌ **C. The Admin API supports managing the producer and consumer communication.**  
   **Incorrect**.

4. ❌ **D. The Admin API supports managing background processes for overall performance tuning.**  
   **Incorrect**.

</details>

## Question 32 (Kafka Producers):
What happens if a Kafka producer produces messages faster than the broker can take them?

- A. The data retention period increases for unprocessed messages.
- B. Kafka automatically scales up the number of brokers to process messages faster.
- C. Data records will be buffered in memory and the buffer will fill up over time.
- D. The producer gets blocked until the broker processed all messages.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

If a Kafka producer produces messages faster than the broker can take, the records will be buffered in memory. The default buffer memory is 33554432 bytes (32 MB). The buffer will full up over time and fill back down when the throughput of the broker increases. If the buffer is full, then the .send() method will start to block and won‘t return right away. The configuration “max.block.ms“ is the time the .send() method will block before throwing an exception. If an exception is thrown this usually means the brokers are down and cannot process any data.

**Detailed explanation of each option:**

1. ❌ **A. The data retention period increases for unprocessed messages.**  
   **Incorrect**.

2. ❌ **B. Kafka automatically scales up the number of brokers to process messages faster.**  
   **Incorrect**.

3. ✅ **C. Data records will be buffered in memory and the buffer will fill up over time.**  
   **Correct**.

4. ❌ **D. The producer gets blocked until the broker processed all messages.**  
   **Incorrect**.

</details>

## Question 33 (Kafka Setup and Operations):
When creating a Kafka topic, which parameter can be used to execute the topic creation only if it does not already exist?

- A. --if-available
- B. --if-exists
- C. --if-not-created
- D. --if-not-exists

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Using the script bin/kafka-topics.sh, you can set the property –if-exists to ensure that the topic to delete or update exists. Similarly, you can use –if-not-exists to ensure that the topic to create or change does not exist.–if-exists: If set when altering or deleting or describing topics, the action will only execute if the topic exists.–if-not-exists: If set when creating topics, the action will only execute if the topic does not already exist.All of Kafka‘s command line tools have additional options: run the kafka-topics.sh command without any arguments to display usage information.Further reading: Kafka Topic Configuration.

**Detailed explanation of each option:**

1. ❌ **A. --if-available**  
   **Incorrect**.

2. ❌ **B. --if-exists**  
   **Incorrect**.

3. ❌ **C. --if-not-created**  
   **Incorrect**.

4. ✅ **D. --if-not-exists**  
   **Correct**.

</details>

## Question 34 (Kafka Consumers):
What‘s the main way to scale data consumption from a Kafka topic?

- A. Scale the default ConsumerCoordinator horizontally by adding more clients.
- B. Refactor your topic and add more partitions to it.
- C. Add more consumers to the consumer group.
- D. Scale your consumer clients vertically by adding more CPUs.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application. Let‘s take a topic with 5 partitions: – If there is only one consumer in the consumer group, the consumer will consume messages from all 5 topic partitions. – If there are two consumers in the consumer group, one consumer will consume messages from 2 partitions and the other one will consume messages from 3 partitions. – If there are five consumers in the consumer group, then each will read messages from a single partition. – If there are more than five consumers in the consumer group, some of the consumers will be idle and get no messages at all. So the main way to scale data consumption from a Kafka topic is by adding more consumers to a consumer group. It is common for Kafka consumers to do high-latency operations such as writing to a database. In this case, a single consumer can‘t possibly keep up with the rate data flows into the topic, and adding more consumers that share the load by having each consumer own just a subset of the partitions and messages is the main method of scaling. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Scale the default ConsumerCoordinator horizontally by adding more clients.**  
   **Incorrect**.

2. ❌ **B. Refactor your topic and add more partitions to it.**  
   **Incorrect**.

3. ✅ **C. Add more consumers to the consumer group.**  
   **Correct**.

4. ❌ **D. Scale your consumer clients vertically by adding more CPUs.**  
   **Incorrect**.

</details>

## Question 35 (Kafka Consumers):
A company monitors their production consumer application and observed that the fetch-rate is very high, but each fetch is small. How could the company increase throughput in this situation?

- A. Increase fetch.max.bytes.
- B. Decrease fetch.max.bytes.
- C. Decrease fetch.min.bytes.
- D. Increase fetch.min.bytes.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

fetch.min.bytes is the minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request. The default setting of 1 byte means that fetch requests are answered as soon as a single byte of data is available or the fetch request times out waiting for data to arrive. Setting this to something greater than 1 will cause the server to wait for larger amounts of data to accumulate which can improve server throughput a bit at the cost of some additional latency.Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. Increase fetch.max.bytes.**  
   **Incorrect**.

2. ❌ **B. Decrease fetch.max.bytes.**  
   **Incorrect**.

3. ❌ **C. Decrease fetch.min.bytes.**  
   **Incorrect**.

4. ✅ **D. Increase fetch.min.bytes.**  
   **Correct**.

</details>

## Question 36 (Stream Processing):
What kind of Kafka Streams window has fixed-size, is non-overlapping and gap-less?

- A. Hopping time window
- B. Sliding time window
- C. Tumbling time window
- D. Session window

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Windowing lets you control how to group records that have the same key for stateful operations such as aggregations or joins into so-called windows. Windows are tracked per record key. The Kafka Streams DSL (Domain Specific Language) supports the following types of windows: – Tumbling time window (time-based): Fixed-size, non-overlapping, gap-less windows. – Hopping time window (time-based): Fixed-size, overlapping windows. – Sliding time window (time-based): Fixed-size, overlapping windows that work on differences between record timestamps. – Session window (session-based): Dynamically-sized, non-overlapping, data-driven windows.

**Detailed explanation of each option:**

1. ❌ **A. Hopping time window**  
   **Incorrect**.

2. ❌ **B. Sliding time window**  
   **Incorrect**.

3. ✅ **C. Tumbling time window**  
   **Correct**.

4. ❌ **D. Session window**  
   **Incorrect**.

</details>

## Question 37 (Kafka Consumers):
Which option is true about a consumer group coordinator in Kafka?

- A. For every consumer there is one equivalent group coordinator.
- B. A group coordinator always is the leader broker.
- C. A group coordinator is one of the brokers.
- D. A consumer group has exactly two group coordinators.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The group coordinator is nothing but one of the brokers which receives heartbeats from all consumers of a consumer group. Every consumer group has exactly one group coordinator. If a consumer stops sending heartbeats, the coordinator will trigger a rebalance.When a consumer wants to join a consumer group, it sends a JoinGroup request to the group coordinator. The first consumer to join the group becomes the group leader.

**Detailed explanation of each option:**

1. ❌ **A. For every consumer there is one equivalent group coordinator.**  
   **Incorrect**.

2. ❌ **B. A group coordinator always is the leader broker.**  
   **Incorrect**.

3. ✅ **C. A group coordinator is one of the brokers.**  
   **Correct**.

4. ❌ **D. A consumer group has exactly two group coordinators.**  
   **Incorrect**.

</details>

## Question 38 (Kafka Core Concepts):
In a point-to-point messaging domain, where are the messages exchanged between senders and receivers?

- A. Queue
- B. Bucket
- C. Topic
- D. Sink

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In a point-to-point domain, message producers are called senders and consumers are called receivers. They exchange messages by means of a destination called a queue: senders produce messages to a queue; receivers consume messages from a queue. What distinguishes point-to-point messaging is that a message can be consumed by only one consumer.

**Detailed explanation of each option:**

1. ✅ **A. Queue**  
   **Correct**.

2. ❌ **B. Bucket**  
   **Incorrect**.

3. ❌ **C. Topic**  
   **Incorrect**.

4. ❌ **D. Sink**  
   **Incorrect**.

</details>

## Question 39 (Kafka Setup and Operations):
Using Kafka security features, how can you allow a specific user to read and write to the topic “test-topic“?

- A. Use SASL as the default authentication service.
- B. Add an ACL with the --allow-principal and --allow-host properties for read and write operations.
- C. Set the property “security.inter.broker.protocol“ to SSL and allow the specific user to connect to the broker.
- D. Enable mTLS authentication between the ZooKeeper servers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Apache Kafka ships with a pluggable, out-of-the-box Authorizer implementation that uses ZooKeeper to store all the ACLs. It is important to set ACLs because otherwise access to resources is limited to super users when an Authorizer is configured. The default behavior is that if a resource has no associated ACLs, then no one is allowed to access the resource, except super users. Access Control Lists (ACLs) provide important authorization controls for your enterprise‘s Kafka cluster data. The following command can be used to set the required ACLs to allow a specific user “Bob“ to read and write to the topic “test-topic“ from host “test-host“: bin/kafka-acls.sh –authorizer-properties zookeeper.connect=localhost:2181 –add –allow-principal User:Bob –allow-host test-host –operation read –operation write –topic test-topic Note: It‘s best practice to create one principal per application and give each principal only the ACLs it requires and no more. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Use SASL as the default authentication service.**  
   **Incorrect**.

2. ✅ **B. Add an ACL with the --allow-principal and --allow-host properties for read and write operations.**  
   **Correct**.

3. ❌ **C. Set the property “security.inter.broker.protocol“ to SSL and allow the specific user to connect to the broker.**  
   **Incorrect**.

4. ❌ **D. Enable mTLS authentication between the ZooKeeper servers.**  
   **Incorrect**.

</details>

## Question 40 (Kafka Internals):
When you enable SSL encryption within Kafka, which feature cannot be used then anymore?

- A. Data Compression
- B. Data Batching
- C. Zero Copy Data Transfer
- D. Horizontally Scaling

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Most traditional data systems use random-access memory (RAM) for data storage, as RAM provides extremely low latencies. Kafka avoids Random Access Memory, it achieves low latency message delivery through Zero Copy Principle. A zero copy optimization consists on removing the second and third data copies, making the data being transferred directly from the read buffer to the socket buffer. Since SSL allows to encrypt data in flight, we no longer send over wire the same data that is stored on the Broker. This means that when SSL is enabled, zero copy optimization is lost, since the Broker needs to decrypt and encrypt the data.

**Detailed explanation of each option:**

1. ❌ **A. Data Compression**  
   **Incorrect**.

2. ❌ **B. Data Batching**  
   **Incorrect**.

3. ✅ **C. Zero Copy Data Transfer**  
   **Correct**.

4. ❌ **D. Horizontally Scaling**  
   **Incorrect**.

</details>

## Question 41 (Stream Processing):
Which of the following options describe the concept of stream-table duality best?

- A. A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table.
- B. A table can be considered a changelog of a stream, where each data record in the table captures a state change of the stream.
- C. A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream.
- D. A stream can be considered a snapshot, at a point in time, of the latest value for each key in a table.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Kafka Streams is a library for building streaming applications, specifically applications that transform input Kafka topics into output Kafka topics. When implementing stream processing use cases in practice, you typically need both streams and also databases and any stream processing technology must therefore provide first-class support for streams and tables. Kafka‘s Streams API provides such functionality through its core abstractions for streams and tables and the stream-table duality describes the close relationship between streams and tables: – Stream as Table: A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table. A stream is thus a table in disguise, and it can be easily turned into a ‘real‘ table by replaying the changelog from beginning to end to reconstruct the table. – Table as Stream: A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream (a stream‘s data records are key-value pairs). A table is thus a stream in disguise, and it can be easily turned into a ‘real‘ stream by iterating over each key-value entry in the table. Further reading: Kafka Streams Concepts.

**Detailed explanation of each option:**

1. ✅ **A. A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table.**  
   **Correct**.

2. ❌ **B. A table can be considered a changelog of a stream, where each data record in the table captures a state change of the stream.**  
   **Incorrect**.

3. ✅ **C. A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream.**  
   **Correct**.

4. ❌ **D. A stream can be considered a snapshot, at a point in time, of the latest value for each key in a table.**  
   **Incorrect**.

</details>

## Question 42 (Kafka Core Concepts):
For the initial connection to a Kafka cluster, why can it be useful to set the “bootstrap-server“ property to a comma-separated list of host and port pairs that are the addresses of the Kafka brokers instead of just using one host and port pair?

- A. In case one of the brokers is experiencing a down time.
- B. You need to connect to at least two brokers to get connected to the whole cluster.
- C. Not every broker knows everything about the other brokers, topics and partitions.
- D. If you use just one host and port pair you can only produce and consume to this specific broker.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The bootstrap.server property is a comma-separated list of host and port pairs that are the addresses of the Kafka brokers in a “bootstrap“ Kafka cluster that a Kafka client connects to initially to bootstrap itself. A host and port pair uses : as the separator (e. g. hostname:9092, hostname:9093). bootstrap.server provides the initial hosts that act as the starting point for a Kafka client to discover the full set of alive servers in the cluster. Since these servers are just used for the initial connection to discover the full cluster membership (which may change dynamically), this list does not have to contain the full set of servers (you may want more than one, though, in case a server is down). Advantages of Kafka Broker Discovery: – every broker is also called a “bootstrap server“ – that means that you only need to connect to one broker, and you will be connected to the whole cluster – each broker knows about all other brokers, topics and partitions (metadata), even though he does not need all the data

**Detailed explanation of each option:**

1. ✅ **A. In case one of the brokers is experiencing a down time.**  
   **Correct**.

2. ❌ **B. You need to connect to at least two brokers to get connected to the whole cluster.**  
   **Incorrect**.

3. ❌ **C. Not every broker knows everything about the other brokers, topics and partitions.**  
   **Incorrect**.

4. ❌ **D. If you use just one host and port pair you can only produce and consume to this specific broker.**  
   **Incorrect**.

</details>

## Question 43 (Kafka Consumers):
When creating a new Kafka consumer, which of the following options can be used as the partition assignment strategy?

- A. WeightedAssignor
- B. RangeAssignor
- C. ResourceBasedAssignor
- D. RoundRobinAssignor

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

The first step to start consuming records is to create a KafkaConsumer instance. Creating a KafkaConsumer is very similar to creating a KafkaProducer – you create a Java Properties instance with the properties you want to pass to the consumer.A PartitionAssignor is a class that, given consumers and topics they subscribed to, decides which partitions will be assigned to which consumer. By default, Kafka has two assignment strategies:– RangeAssignor (default): Assigns to each consumer a consecutive subset of partitions from each topic it subscribes to. So if consumers C1 and C2 are subscribed to two topics, T1 and T2, and each of the topics has three partitions, then C1 will be assigned partitions 0 and 1 from topics T1 and T2, while C2 will be assigned partition 2 from those topics. Because each topic has an uneven number of partitions and the assignment is done for each topic independently, the first consumer ends up with more partitions than the second. This happens whenever Range assignment is used and the number of consumers does not divide the number of partitions in each topic neatly.– RoundRobinAssignor: Takes all the partitions from all subscribed topics and assigns them to consumers sequentially, one by one. If C1 and C2 described previously used RoundRobin assignment, C1 would have partitions 0 and 2 from topic T1 and partition 1 from topic T2. C2 would have partition 1 from topic T1 and partitions 0 and 2 from topic T2. In general, if all consumers are subscribed to the same topics (a very common scenario), RoundRobin assignment will end up with all consumers having the same number of partitions (or at most 1 partition difference).Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. WeightedAssignor**  
   **Incorrect**.

2. ✅ **B. RangeAssignor**  
   **Correct**.

3. ❌ **C. ResourceBasedAssignor**  
   **Incorrect**.

4. ✅ **D. RoundRobinAssignor**  
   **Correct**.

</details>

## Question 44 (Kafka Consumers):
Which consumer becomes the group leader of a consumer application?

- A. The first consumer to join the group.
- B. The group leader is elected by the Kafka brokers.
- C. The last consumer to join the group.
- D. The group leader is elected by the group coordinator.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

When a consumer wants to join a group, it sends a JoinGroup request to the group coordinator. The first consumer to join the group becomes the group leader. The leader receives a list of all consumers in the group from the group coordinator (this will include all consumers that sent a heartbeat recently and which are therefore considered alive) and is responsible for assigning a subset of partitions to each consumer.

**Detailed explanation of each option:**

1. ✅ **A. The first consumer to join the group.**  
   **Correct**.

2. ❌ **B. The group leader is elected by the Kafka brokers.**  
   **Incorrect**.

3. ❌ **C. The last consumer to join the group.**  
   **Incorrect**.

4. ❌ **D. The group leader is elected by the group coordinator.**  
   **Incorrect**.

</details>

## Question 45 (Kafka Setup and Operations):
Which Kafka metric could be used if there is a lot of load on the system and you want to figure out what could be the problem for lag spikes?

- A. Reassigning Partitions
- B. Bytes In Per Sec
- C. Partition Count
- D. Under Replicated Partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The Confluent Control Center monitors a lot of important operational broker metrics aggregated across the cluster, and per broker or per topic where applicable.The metric UnderReplicatedPartitions monitors the number of partitions that have problems with the ISR (in-sync replicas). Replicas that are added as part of a reassignment will not count toward this value. Alert if value is greater than 0.UnderReplicatedPartitions means that data is not being replicated to enough number of brokers thereby increasing the probability of data loss should those replicas fail or die. If you have under replicated partitions, it typically points to a problem with one or more brokers and you are having a lot of load on the system. You should root cause the problem immediately to avoid any data loss.Further reading: Kafka Monitoring.

**Detailed explanation of each option:**

1. ❌ **A. Reassigning Partitions**  
   **Incorrect**.

2. ❌ **B. Bytes In Per Sec**  
   **Incorrect**.

3. ❌ **C. Partition Count**  
   **Incorrect**.

4. ✅ **D. Under Replicated Partitions**  
   **Correct**.

</details>

## Question 46 (Reliable Data Delivery):
Which Kafka API supports exactly-once delivery? 

- A. Connect API
- B. Consumer API
- C. Streams API
- D. Producer API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C (Streams API): Kafka Streams API natively supports exactly-once (EOS) semantics through transactional producers and state management, ensuring read-process-write operations complete exactly once even with failures. Incorrect Option A (Connect API): Kafka Connect provides at-least-once delivery by default; exactly-once requires additional connector-specific configuration and isn’t native to the API. Option B (Consumer API): Supports at-least-once or at-most-once; lacks built-in transactional guarantees for exactly-once processing. Option D (Producer API): Transactional producers enable idempotent exactly-once delivery to topics, but don’t handle end-to-end processing semantics like Streams API.

**Detailed explanation of each option:**

1. ❌ **A. Connect API**  
   **Incorrect**.

2. ❌ **B. Consumer API**  
   **Incorrect**.

3. ✅ **C. Streams API**  
   **Correct**.

4. ❌ **D. Producer API**  
   **Incorrect**.

</details>

## Question 47 (Kafka Setup and Operations):
Which CLI command can be used to find out all the partitions where one or more of the replicas for the partition are not in-sync with the leader?

- A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
- B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --list --under-min-isr-partitions
- C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --list --under-replicated-partitions
- D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The purpose of describing topics is to know the leader for the topic, the broker instances acting as replicas for the topic, and the number of partitions of a Kafka topic that has been created with. When describing Kafka topics you can set some additional properties to only show specific topics / partitions, e. g.: –topics-with-overrides: If set when describing topics, only show topics that have overridden configs. –unavailable-partitions: If set when describing topics, only show partitions whose leader is not available. –under-min-isr-partitions: If set when describing topics, only show partitions whose ISR count is less than the configured minimum. –under-replicated-partitions: If set when describing topics, only show under replicated partitions. This basically means the cluster is overloaded and followers are not able to catch up on leaders (not in-sync). Further reading: Topic Configurations.

**Detailed explanation of each option:**

1. ✅ **A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions**  
   **Correct**.

2. ❌ **B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --list --under-min-isr-partitions**  
   **Incorrect**.

3. ❌ **C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --list --under-replicated-partitions**  
   **Incorrect**.

4. ❌ **D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions**  
   **Incorrect**.

</details>

## Question 48 (Kafka Setup and Operations):
By default, what is the encryption mechanism used by Apache Kafka?

- A. SASL
- B. SSL
- C. TLS
- D. Plaintext

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D – Plaintext By default, Apache Kafka communicates in plaintext with no encryption. Security features such as SSL/TLS or SASL must be explicitly configured by administrators. This default behavior highlights the importance of securing Kafka clusters manually. Incorrect Option A – SASL Incorrect because SASL is an authentication mechanism, not the default encryption method. It can be combined with SSL/TLS but is not enabled by default. Option B – SSL Incorrect because SSL must be configured manually. Kafka does not enable SSL encryption automatically. Option C – TLS Incorrect because TLS, like SSL, requires explicit configuration in Kafka’s server and client properties. It is not the default.

**Detailed explanation of each option:**

1. ❌ **A. SASL**  
   **Incorrect**.

2. ❌ **B. SSL**  
   **Incorrect**.

3. ❌ **C. TLS**  
   **Incorrect**.

4. ✅ **D. Plaintext**  
   **Correct**.

</details>

## Question 49 (Reliable Data Delivery):
Using the configuration “replication.factor=3“, “min.insync.replicas=2“ and “acks=all“, what happens if two brokers are down and a consumer group tries to consume from Kafka?

- A. There will be a NOT_ENOUGH_REPLICAS exception.
- B. A new broker will be initialized and synced with the remaining replica.
- C. The consumer application waits until enough replicas are back up.
- D. The remaining replica returns the data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, producers create and write messages to topic partitions and consumers read data from these partitions.With acks=all and a replication factor of 3 and two brokers are down, the minimum of in-sync replicas cannot be met. Therefore a producer would raise an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend).For a consumer though, it‘s still possible to read data from the remaining replica.

**Detailed explanation of each option:**

1. ❌ **A. There will be a NOT_ENOUGH_REPLICAS exception.**  
   **Incorrect**.

2. ❌ **B. A new broker will be initialized and synced with the remaining replica.**  
   **Incorrect**.

3. ❌ **C. The consumer application waits until enough replicas are back up.**  
   **Incorrect**.

4. ✅ **D. The remaining replica returns the data.**  
   **Correct**.

</details>

## Question 50 (Stream Processing):
Which of the following Kafka Streams domain specific language operations are stateless? 

- A. GroupBy
- B. Branch
- C. Count
- D. FlatMapValues

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

GroupBy Stateful groupBy reorganizes the stream into keyed groups for aggregation. Often used before aggregations, so it’s considered stateful. Branch Stateless Splits a stream into multiple streams based on a predicate. No history or state is maintained. Count Stateful Counts events over a window or per key → requires maintaining state. FlatMapValues Stateless Transforms each record into zero or more records. Each record is processed independently.

**Detailed explanation of each option:**

1. ❌ **A. GroupBy**  
   **Incorrect**.

2. ✅ **B. Branch**  
   **Correct**.

3. ❌ **C. Count**  
   **Incorrect**.

4. ✅ **D. FlatMapValues**  
   **Correct**.

</details>

## Question 51 (Kafka Consumers):
How to see if a consumer group is committing offsets at all, or how often offsets are being committed?

- A. Consumer offsets are automatically stored and visualized in the Confluent Control Center.
- B. Read the consumer log located under /bin/log/consumer-log.txt
- C. Use the consumer group to consume from the internal partition called __consumer_offsets.
- D. Use the console consumer to consume the internal topic called __consumer_offsets.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

It is sometimes useful to see what offsets are being committed for the cluster‘s consumer groups. You may want to see if a particular group is committing offsets at all, or how often offsets are being committed. This can be done by using the console consumer to consume the special internal topic called __consumer_offsets. All consumer offsets are written as messages to this topic. In order to decode the messages in this topic, you must use the formatter class kafka.coordinator.GroupMeta dataManager$OffsetsMessageFormatter.

**Detailed explanation of each option:**

1. ❌ **A. Consumer offsets are automatically stored and visualized in the Confluent Control Center.**  
   **Incorrect**.

2. ❌ **B. Read the consumer log located under /bin/log/consumer-log.txt**  
   **Incorrect**.

3. ❌ **C. Use the consumer group to consume from the internal partition called __consumer_offsets.**  
   **Incorrect**.

4. ✅ **D. Use the console consumer to consume the internal topic called __consumer_offsets.**  
   **Correct**.

</details>

## Question 52 (Kafka Consumers):
Which concept can be used to fetch a specific message with specific offsets or to replay data for a consumer?

- A. Use the fetch() API.
- B. Use the commitSync() API.
- C. Use the assign() and seek() APIs.
- D. Use the poll() API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. If you want to start reading all messages from the beginning of the partition, or you want to skip all the way to the end of the partition and start consuming only new messages, there are APIs specifically for that: seekToBeginning(TopicPartition tp) and seekToEnd(TopicPartition tp). However, sometimes you want to start reading at a different offset for specific partitions: 1: The consumer can manually assign specific partitions using assign(Collection). 2: Kafka allows specifying the position using seek(TopicPartition, long) to specify the new position (offset) a consumer can read from. Further reading: Consumer APIs.

**Detailed explanation of each option:**

1. ❌ **A. Use the fetch() API.**  
   **Incorrect**.

2. ❌ **B. Use the commitSync() API.**  
   **Incorrect**.

3. ✅ **C. Use the assign() and seek() APIs.**  
   **Correct**.

4. ❌ **D. Use the poll() API.**  
   **Incorrect**.

</details>

## Question 53 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for BACKWARD schema evolution? 

- A. Add fields
- B. Delete optional fields
- C. Add optional fields
- D. Delete fields

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

An important aspect of data management is schema evolution. After the initial schema is defined, applications may need to evolve it over time. When this happens, it‘s critical for the downstream consumers to be able to handle data encoded with both the old and the new schema seamlessly. When using Avro or other schema formats, one of the most important things is to manage the schemas and consider how these schemas should evolve. Confluent Schema Registry is built for exactly that purpose. The Confluent Schema Registry default compatibility type is BACKWARD. Allowed changes for BACKWARD compatibility are: – Delete fields – Add optional fields BACKWARD compatibility means that consumers using the new schema X can read data produced with the new schema X or the last schema X – 1. Further reading: Avro Schema Evolution.

**Detailed explanation of each option:**

1. ❌ **A. Add fields**  
   **Incorrect**.

2. ❌ **B. Delete optional fields**  
   **Incorrect**.

3. ✅ **C. Add optional fields**  
   **Correct**.

4. ✅ **D. Delete fields**  
   **Correct**.

</details>

## Question 54 (Kafka Consumers):
Which method can be used for a consumer to read messages from a specific topic?

- A. .listen()
- B. .subscribe()
- C. .consume()
- D. .read()

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The first step to start consuming records is to create a KafkaConsumer instance. Creating a KafkaConsumer is very similar to creating a KafkaProducer – you create a Java Properties instance with the properties you want to pass to the consumer. Once a consumer is created, the next step is to subscribe to one or more topics. The subcribe() method takes a list of topics as a parameter (as a list or with regular expression). For example using a list with a single topic element named test_topic: consumer.subscribe(Collections.singletonList(“test_topic“)); Kafka will deliver each message in the subscribed topics to one process in each consumer group. This is achieved by balancing the partitions between all members in the consumer group so that each partition is assigned to exactly one consumer in the group. Further reading: Consumer Client.

**Detailed explanation of each option:**

1. ❌ **A. .listen()**  
   **Incorrect**.

2. ✅ **B. .subscribe()**  
   **Correct**.

3. ❌ **C. .consume()**  
   **Incorrect**.

4. ❌ **D. .read()**  
   **Incorrect**.

</details>

## Question 55 (Kafka Core Concepts):
What happens if you try to produce to a topic that does not yet exist?

- A. There will be a runtime error.
- B. The topic gets created with the default server settings without any errors or warnings.
- C. A warning appears but the topic still gets created with the default server settings.
- D. It depends on the broker setting “auto.create.topic.enable“.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

If the broker setting auto.create.topic.enable is set to true, then Kafka will automatically create the topic with the default broker settings num.partitions and default.replication.factor.The option defaults to true.Hence it depends on the broker setting auto.create.topic.enable.

**Detailed explanation of each option:**

1. ❌ **A. There will be a runtime error.**  
   **Incorrect**.

2. ❌ **B. The topic gets created with the default server settings without any errors or warnings.**  
   **Incorrect**.

3. ❌ **C. A warning appears but the topic still gets created with the default server settings.**  
   **Incorrect**.

4. ✅ **D. It depends on the broker setting “auto.create.topic.enable“.**  
   **Correct**.

</details>
