## Question 1 (Kafka Internals):
In Kafka, how is a topic partition structured? 

- A. Partitions are made of one segment that comes with two indexes.
- B. Partitions are made of one segment that comes with one index.
- C. Partitions are made of segments that come with one index.
- D. Partitions are made of segments that come with two indexes.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

A topic partition is an actual storage unit of Kafka messages which can be assumed as a Kafka message queue. The number of partitions per topic are configurable while creating it. Messages in a partition are segregated into multiple segments to ease finding a message by its offset. Each segment is composed of the following two indexes (files): – An offset to position index, that allows Kafka to find the starting position of a message. – A timestamp to offset index, that allows Kafka to find messages for a timestamp.

**Detailed explanation of each option:**

1. ❌ **A. Partitions are made of one segment that comes with two indexes.**  
   **Incorrect**.

2. ❌ **B. Partitions are made of one segment that comes with one index.**  
   **Incorrect**.

3. ❌ **C. Partitions are made of segments that come with one index.**  
   **Incorrect**.

4. ✅ **D. Partitions are made of segments that come with two indexes.**  
   **Correct**.

</details>

## Question 2 (Kafka Consumers):
A consumer has auto.offset.reset=latest, and the topic partition currently has data for offsets going from 45 to 2311. The consumer group never committed offsets for the topic before. Where will the consumer read from?

- A. it will crash
- B. offset 0
- C. offset 45
- D. offset 2311

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Latest means that data retrievals will start from where the offsets currently end

**Detailed explanation of each option:**

1. ❌ **A. it will crash**  
   **Incorrect**.

2. ❌ **B. offset 0**  
   **Incorrect**.

3. ❌ **C. offset 45**  
   **Incorrect**.

4. ✅ **D. offset 2311**  
   **Correct**.

</details>

## Question 3 (Reliable Data Delivery):
Which of the following producer configurations best fits a company‘s requirement to have a very safe data pipeline without message loss? 

- A. acks=all, replication.factor=3, min.insync.replicas=2
- B. acks=1, replication.factor=3, min.insync.replicas=2
- C. acks=all, replication.factor=2, min.insync.replicas=1
- D. acks=1, replication.factor=2, min.insync.replicas=1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To make your data fault-tolerant, safe and highly-available, every Kafka topic can be replicated, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i. e., there will always be three copies of your data. This replication is performed at the level of topic-partitions. acks=all means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. When used together, min.insync.replicas and acks allow you to enforce greater durability guarantees. A typical scenario would be to create a topic with a replication factor of 3, set min.insync.replicas to 2, and produce with acks of “all“. This will ensure that the producer raises an exception if a majority of replicas do not receive a write.

**Detailed explanation of each option:**

1. ✅ **A. acks=all, replication.factor=3, min.insync.replicas=2**  
   **Correct**.

2. ❌ **B. acks=1, replication.factor=3, min.insync.replicas=2**  
   **Incorrect**.

3. ❌ **C. acks=all, replication.factor=2, min.insync.replicas=1**  
   **Incorrect**.

4. ❌ **D. acks=1, replication.factor=2, min.insync.replicas=1**  
   **Incorrect**.

</details>

## Question 4 (Kafka Core Concepts):
Why can it be very challenging to add partitions later, if you are sending messages to partitions based on keys? 

- A. After adding partitions later, it cannot be guaranteed that new messages with the same key will go to the same partition.
- B. After adding partitions later, it cannot be guaranteed that old messages with the same key will still be on the same partition.
- C. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.
- D. After adding partitions later, it cannot be guaranteed that old messages will still exist.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Correct Option C. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.

**Detailed explanation of each option:**

1. ❌ **A. After adding partitions later, it cannot be guaranteed that new messages with the same key will go to the same partition.**  
   **Incorrect**.

2. ❌ **B. After adding partitions later, it cannot be guaranteed that old messages with the same key will still be on the same partition.**  
   **Incorrect**.

3. ✅ **C. After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.**  
   **Correct**.

4. ❌ **D. After adding partitions later, it cannot be guaranteed that old messages will still exist.**  
   **Incorrect**.

</details>

## Question 5 (Reliable Data Delivery):
Which Kafka API supports exactly-once delivery? 

- A. Streams API
- B. Producer API
- C. Consumer API
- D. Connect API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka supports three types of Message Delivery Guarantees: At-most once: Every message is persisted in Kafka at-most-once. Message loss is possible if the producer doesn‘t retry on failures. At-least-once: Every message is guaranteed to be persisted in Kafka at-least-once. There is no chance of message loss but the message can be duplicated if the producer retries when the message is already persisted. Exactly-once: Every message is guaranteed to be persisted in Kafka exactly once without any duplicates and data loss even where there is a broker failure or producer retry. Exactly-once processing can be achieved for Kafka -> Kafka workflows only using the Kafka Streams API. For Kafka -> Sink workflows, you need to use an idempotent consumer. Stream processing applications written in the Kafka Streams library can turn on exactly-once semantics by simply making a single config change, to set the config named processing.guarantee to exactly_once (default value is at_least_once), with no code change required. Further reading: Delivery Semantics.

**Detailed explanation of each option:**

1. ✅ **A. Streams API**  
   **Correct**.

2. ❌ **B. Producer API**  
   **Incorrect**.

3. ❌ **C. Consumer API**  
   **Incorrect**.

4. ❌ **D. Connect API**  
   **Incorrect**.

</details>

## Question 6 (Kafka Core Concepts):
In a point-to-point messaging domain, where are the messages exchanged between senders and receivers? 

- A. Sink
- B. Queue
- C. Bucket
- D. Topic

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In a point-to-point domain, message producers are called senders and consumers are called receivers. They exchange messages by means of a destination called a queue: senders produce messages to a queue; receivers consume messages from a queue. What distinguishes point-to-point messaging is that a message can be consumed by only one consumer.

**Detailed explanation of each option:**

1. ❌ **A. Sink**  
   **Incorrect**.

2. ✅ **B. Queue**  
   **Correct**.

3. ❌ **C. Bucket**  
   **Incorrect**.

4. ❌ **D. Topic**  
   **Incorrect**.

</details>

## Question 7 (Kafka Connect):
To continuously export data from Kafka into a target database, I should use

- A. Kafka Connect Sink
- B. Kafka Connect Source
- C. Kafka Streams
- D. Kafka Producer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Connect Sink is used to export data from Kafka to external databases and Kafka Connect Source is used to import from external databases into Kafka.

**Detailed explanation of each option:**

1. ✅ **A. Kafka Connect Sink**  
   **Correct**.

2. ❌ **B. Kafka Connect Source**  
   **Incorrect**.

3. ❌ **C. Kafka Streams**  
   **Incorrect**.

4. ❌ **D. Kafka Producer**  
   **Incorrect**.

</details>

## Question 8 (Kafka Ecosystem):
What‘s one of the five core Kafka APIs? 

- A. Admin API
- B. Python API
- C. Javascript API
- D. Messaging API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

There are five major APIs in Kafka: – The Producer API allows applications to send streams of data to topics in the Kafka cluster. – The Consumer API allows applications to read streams of data from topics in the Kafka cluster. – The Streams API allows transforming streams of data from input topics to output topics. – The Connect API allows implementing connectors that continually pull from some source system or application into Kafka or push from Kafka into some sink system or application. – The Admin API allows managing and inspecting topics, brokers, and other Kafka objects. Further reading: Kafka API documentation.

**Detailed explanation of each option:**

1. ✅ **A. Admin API**  
   **Correct**.

2. ❌ **B. Python API**  
   **Incorrect**.

3. ❌ **C. Javascript API**  
   **Incorrect**.

4. ❌ **D. Messaging API**  
   **Incorrect**.

</details>

## Question 9 (Kafka Setup and Operations):
After creating a Kafka topic, which script helps you to check whether the topic you created is available? 

- A. bin/kafka-topics.sh
- B. bin/kafka-configs.sh
- C. bin/kafka-console-consumer.sh
- D. bin/kafka-console-producer.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka, events are organized and stored in topics. The bin/kafka-topics.sh script can be used to create, delete, describe, list or change a topic. To list all available topics you can use the following command: bin/kafka-topics.sh –bootstrap-sever localhost:9092 –list

**Detailed explanation of each option:**

1. ✅ **A. bin/kafka-topics.sh**  
   **Correct**.

2. ❌ **B. bin/kafka-configs.sh**  
   **Incorrect**.

3. ❌ **C. bin/kafka-console-consumer.sh**  
   **Incorrect**.

4. ❌ **D. bin/kafka-console-producer.sh**  
   **Incorrect**.

</details>

## Question 10 (Stream Processing):
Using Kafka Streams, which of the supported join operations are windowed? 

- A. KTable-to-Ktable
- B. KStream-to-KTable
- C. KStream-to-Kstream
- D. KStream-to-GlobalKTable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Streams is a client library for building streaming applications and microservices, where the input and output data are stored in Kafka clusters. Using the Streams API, the following join operations are supported and depending on the operands, joins are either windowed or non-windowed: – KStream-to-KStream (windowed): Inner join, left join and outer join supported. – KTable-to-KTable (non-windowed): Inner join, left join and outer join supported. – KStream-to-KTable (non-windowed): Inner join and left join supported. Outer join not supported. – KStream-to-GlobalKTable (non-windowed): Inner join and left join supported. Outer join not supported. Further reading: Joining Concepts.

**Detailed explanation of each option:**

1. ❌ **A. KTable-to-Ktable**  
   **Incorrect**.

2. ❌ **B. KStream-to-KTable**  
   **Incorrect**.

3. ✅ **C. KStream-to-Kstream**  
   **Correct**.

4. ❌ **D. KStream-to-GlobalKTable**  
   **Incorrect**.

</details>

## Question 11 (Kafka Setup and Operations):
Which Java versions are supported by Kafka? 

- A. Java 11
- B. Java 5
- C. Java 8
- D. Java 16

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. Java 11**  
   **Correct**.

2. ❌ **B. Java 5**  
   **Incorrect**.

3. ✅ **C. Java 8**  
   **Correct**.

4. ❌ **D. Java 16**  
   **Incorrect**.

</details>

## Question 12 (Kafka Setup and Operations):
Which command can be used to create a Kafka topic to store your events? 

- A. bin/kafka-topics.sh --describe --topic first-topic --bootstrap-server localhost:9092
- B. bin/topics.sh --create --topic first-topic --bootstrap-server localhost:9092
- C. bin/zookeeper-topics.sh --create --topic first-topic --bootstrap-server localhost:9092
- D. bin/kafka-topics.sh --create --topic first-topic --bootstrap-server localhost:9092

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, events are organized and stored in topics. A topic is identified by its name and you can have as many topics as you want. Before you can write your first events, you must create a topic with the following command: bin/kafka-topics.sh –create –topic first-topic –bootstrap-server localhost:9092 Configurations pertinent to topics have both a server default as well an optional per-topic override. If no per-topic configuration is given the server default is used (server.properties file). The override can be set at topic creation time by giving one or more –config options. The following example creates a topic named first-topic with a custom max message size as well as two partitions and a replication factor of three: bin/kafka-topics.sh –create –topic first-topic –bootstrap-server localhost:9092 –partitions 2 \ –replication-factor 3 –config max.message.bytes=64000 Further reading: Topic Configuration.

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-topics.sh --describe --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

2. ❌ **B. bin/topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

3. ❌ **C. bin/zookeeper-topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Incorrect**.

4. ✅ **D. bin/kafka-topics.sh --create --topic first-topic --bootstrap-server localhost:9092**  
   **Correct**.

</details>

## Question 13 (Programming & Serialization):
What is the protocol used by Kafka clients to securely connect to the Confluent REST Proxy?

- A. SASL
- B. Kerberos
- C. HTTP
- D. HTTPS (SSL/TLS)

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

TLS – but it is still called SSL.

**Detailed explanation of each option:**

1. ❌ **A. SASL**  
   **Incorrect**.

2. ❌ **B. Kerberos**  
   **Incorrect**.

3. ❌ **C. HTTP**  
   **Incorrect**.

4. ✅ **D. HTTPS (SSL/TLS)**  
   **Correct**.

</details>

## Question 14 (Programming & Serialization):
In Avro, adding an element to an enum without a default is a __ schema evolution

- A. breaking
- B. backward
- C. full
- D. forward

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Since Confluent 5.4.0, Avro 1.9.1 is used. Since default value was added to enum complex type , the schema resolution changed from: (<1.9.1) if both are enums:** if the writer‘s symbol is not present in the reader‘s enum, then an error is signalled. **(>=1.9.1) if both are enums: if the writer‘s symbol is not present in the reader‘s enum and the reader has a default value, then that value is used, otherwise an error is signalled.

**Detailed explanation of each option:**

1. ✅ **A. breaking**  
   **Correct**.

2. ❌ **B. backward**  
   **Incorrect**.

3. ❌ **C. full**  
   **Incorrect**.

4. ❌ **D. forward**  
   **Incorrect**.

</details>

## 🚫 Question 15 (Kafka Ecosystem):
Which Confluent solution can be used as an overview dashboard to enable centralized management and monitoring of key components of the platform, including clusters, brokers, schemas, topics, messages, connectors, ksqlDB queries, security, replication and more? 

- A. Confluent Metrics Reporter
- B. Confluent Health+
- C. Confluent Control Center
- D. Confluent Schema Registry

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The Confluent Control Center is a self-hosted GUI with expert-designed dashboards to enable centralized management and monitoring of key components of the platform, including clusters, brokers, schemas, topics, messages, connectors, ksqlDB queries, security, replication and more. Confluent Control Center integrates with RBAC, which allows users to view their own permissions, manage other user‘s role bindings when they have the permissions to do so, and altogether maintain visibility over key operational metrics. This simplifies security management for the entire organization. With Confluent Platform, also monitoring functionality is tightly integrated across the components out of the box. The Confluent Metrics Reporter collects various metrics from Kafka brokers and produces the values to a Kafka topic. Further reading: Confluent Platform.

**Detailed explanation of each option:**

1. ❌ **A. Confluent Metrics Reporter**  
   **Incorrect**.

2. ❌ **B. Confluent Health+**  
   **Incorrect**.

3. ✅ **C. Confluent Control Center**  
   **Correct**.

4. ❌ **D. Confluent Schema Registry**  
   **Incorrect**.

</details>

## Question 16 (Stream Processing):
Your streams application is reading from an input topic that has 5 partitions. You run 5 instances of your application, each with num.streams.threads set to 5. How many stream tasks will be created and how many will be active?

- A. 5 created, 5 active
- B. 25 created, 25 active
- C. 5 created, 1 active
- D. 25 created, 5 active

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. 5 created, 5 active**  
   **Incorrect**.

2. ❌ **B. 25 created, 25 active**  
   **Incorrect**.

3. ❌ **C. 5 created, 1 active**  
   **Incorrect**.

4. ✅ **D. 25 created, 5 active**  
   **Correct**.

</details>

## Question 17 (Kafka Setup and Operations):
If you are setting up a multi-broker cluster in Kafka on different machines, which broker property needs to be unique for each node? 

- A. all of the other options need to be unique for each node
- B. port
- C. log.dir
- D. broker.id

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

For Kafka, a single broker is just a cluster of size one, so nothing much changes other than starting a few more broker instances if you want to set up a multi-broker cluster. Only the broker.id property needs to be unique and permanent for each node in the cluster. Note: If you run multiple brokers on the same machine you should definitely override the port and log directory as well, because you want to keep the brokers from all trying to register on the same port or overwrite each others data. Further reading: Kafka Quickstart.

**Detailed explanation of each option:**

1. ❌ **A. all of the other options need to be unique for each node**  
   **Incorrect**.

2. ❌ **B. port**  
   **Incorrect**.

3. ❌ **C. log.dir**  
   **Incorrect**.

4. ✅ **D. broker.id**  
   **Correct**.

</details>

## 🚫 Question 18 (Kafka Ecosystem):
What are the main benefits of using ksqlDB together with Kafka? 

- A. ksqlDB allows you to use SQL-like syntax to setup your Kafka cluster.
- B. ksqlDB allows you to query, read, write, and process data in Kafka in real-time and at scale using intuitive SQL-like syntax.
- C. ksqlDB just requires a Python runtime environment and you are ready to operate your Kafka cluster at real-time and at scale using intuitive SQL-like syntax.
- D. ksqlDB does not require proficiency with a programming language such as Java or Scala, and you don‘t have to install a separate processing cluster technology.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. ksqlDB allows you to use SQL-like syntax to setup your Kafka cluster.**  
   **Incorrect**.

2. ✅ **B. ksqlDB allows you to query, read, write, and process data in Kafka in real-time and at scale using intuitive SQL-like syntax.**  
   **Correct**.

3. ❌ **C. ksqlDB just requires a Python runtime environment and you are ready to operate your Kafka cluster at real-time and at scale using intuitive SQL-like syntax.**  
   **Incorrect**.

4. ✅ **D. ksqlDB does not require proficiency with a programming language such as Java or Scala, and you don‘t have to install a separate processing cluster technology.**  
   **Correct**.

</details>

## Question 19 (Kafka Core Concepts):
What option best describes a Kafka Broker? 

- A. A Kafka Broker is a JVM process that runs on a machine and helps the communication between servers and clients.
- B. A Kafka Broker is a JVM process that runs on a machine and publishes streams of events.
- C. A Kafka Broker is a JVM process that runs on a machine and hosts topics.
- D. A Kafka Broker is a JVM process that runs on a machine and subscribes to streams of events.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

A Kafka Broker is nothing more, nothing less, than a JVM process that runs on a machine and hosts topics. Each broker is identified with its unique ID (integer) and acts as the middleman between producers and consumers. The broker receives messages from producers and allows consumers to fetch messages by topic, partition and offset. Further reading: Broker Configs.

**Detailed explanation of each option:**

1. ❌ **A. A Kafka Broker is a JVM process that runs on a machine and helps the communication between servers and clients.**  
   **Incorrect**.

2. ❌ **B. A Kafka Broker is a JVM process that runs on a machine and publishes streams of events.**  
   **Incorrect**.

3. ✅ **C. A Kafka Broker is a JVM process that runs on a machine and hosts topics.**  
   **Correct**.

4. ❌ **D. A Kafka Broker is a JVM process that runs on a machine and subscribes to streams of events.**  
   **Incorrect**.

</details>

## Question 20 (Reliable Data Delivery):
Using the configuration “replication.factor=3“, “min.insync.replicas=2“ and “acks=all“, which exception will be thrown if two brokers are down? 

- A. Exception: UNKNOWN_SERVER.
- B. Exception: TIMEOUT.
- C. Exception: NOT_ENOUGH_REPLICAS.
- D. Exception: UNKNOWN_TOPIC_OR_PARTITION.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, producers create and write messages to topic partitions. Consider the following configuration: – replication factor=3: This means there will always be three copies of your data. This replication is performed at the level of topic-partitions. – acks=all: This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting. – min.insync.replicas=2: When a producer sets acks to “all“ (or “-1“), min.insync.replicas specifies that there need to be minimum two replicas that must acknowledge a write for the write to be considered successful. With a replication factor of 3 and two brokers are down, the minimum of in-sync replicas cannot be met. Therefore the producer will raise an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend). Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. Exception: UNKNOWN_SERVER.**  
   **Incorrect**.

2. ❌ **B. Exception: TIMEOUT.**  
   **Incorrect**.

3. ✅ **C. Exception: NOT_ENOUGH_REPLICAS.**  
   **Correct**.

4. ❌ **D. Exception: UNKNOWN_TOPIC_OR_PARTITION.**  
   **Incorrect**.

</details>

## Question 21 (Kafka Producers):
If you are producing messages to a Kafka topic, which producer property needs to be set if you want to receive leader acknowledgment of data writes?

- A. acks=1
- B. acks=0
- C. acks=leader
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka, producers create and write messages to topic partitions and Producers can choose to receive acknowledgement of data writes, which can be configured using the acks property. It is the number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. The following settings are allowed: acks=0: If set to zero then the producer will not wait for any acknowledgment from the server at all. No guarantee can be made that the server has received the record in this case (possible data loss). acks=1: This will mean the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers. In this case should the leader fail immediately after acknowledging the record but before the followers have replicated it then the record will be lost (limited data loss). acks=all: This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting (no data loss). Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ✅ **A. acks=1**  
   **Correct**.

2. ❌ **B. acks=0**  
   **Incorrect**.

3. ❌ **C. acks=leader**  
   **Incorrect**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## Question 22 (Kafka Internals):
In Kafka, how often is log compaction evaluated?

- A. Every time a message with an existing key is produced.
- B. Every time a message with a new key is produced.
- C. Every time a message is written to the active segment.
- D. Every time the active segment is closed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The main idea behind Log Compaction is to selectively remove records where there are most recent updates with the same primary key. Log compaction strategy ensures that Kafka will always retain at least the last known value for each message key within the log for a single topic partition. It is mostly used for scenarios such as restoring to the previous state before the application crashed or system failed, or while reloading cache after application restarts. In simple terms, Apache Kafka will keep the latest version of a record and delete the older versions with same key. Some important notes: – Offsets do not change when enabling log compaction. – Any consumer that is reading from the tail of a log (most current data) will still see all the messages sent to the topic. – Ordering of messages is kept. – Deleted records can still be seen by consumers for a period of “delete.retention.ms“ (default is 24 hours). – Log compaction is evaluated every time the active segment is closed. Log Compaction is configured by the properties “log.cleanup.policy=compact“ and “segment.ms“ (default 7 days). “Segment.ms“ is the maximum amount of time to wait to close the active segment. Further reading: Log Compaction Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Every time a message with an existing key is produced.**  
   **Incorrect**.

2. ❌ **B. Every time a message with a new key is produced.**  
   **Incorrect**.

3. ❌ **C. Every time a message is written to the active segment.**  
   **Incorrect**.

4. ✅ **D. Every time the active segment is closed.**  
   **Correct**.

</details>

## Question 23 (Kafka Consumers):
Which of the following options is true for the “kafka-console-consumer“ CLI?

- A. When used with the default options it uses a random group id.
- B. When used with the default options it does not use a group id.
- C. When used with the default options it always uses the same group id.
- D. When used with the default options it uses the group id of the last created consumer group.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The kafka-console-consumer tool can be useful in a couple of ways: – Acting as an independent consumer of particular topics. This can be useful to compare results against a consumer program that you‘ve written. – To test general topic consumption without the need to write any consumer code. When used with the default options and no consumer group is specified, the kafka-console-consumer generates a random consumer group. Note: Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want.

**Detailed explanation of each option:**

1. ✅ **A. When used with the default options it uses a random group id.**  
   **Correct**.

2. ❌ **B. When used with the default options it does not use a group id.**  
   **Incorrect**.

3. ❌ **C. When used with the default options it always uses the same group id.**  
   **Incorrect**.

4. ❌ **D. When used with the default options it uses the group id of the last created consumer group.**  
   **Incorrect**.

</details>

## Question 24 (Programming & Serialization):
Which of the following options best describes the process of serialization and deserialization? 

- A. Serialization is the process of consuming key / value based Avro messages from a Kafka topic. Deserialization does the opposite of serialization, in which we produce key / value based Avro messages into a Kafka topic.
- B. Serialization is the process of converting bytes of arrays into the desired data type that are used for transmission. Deserialization does the opposite of serialization, in which we convert an object into a stream of bytes.
- C. Serialization is the process of converting an object into a stream of bytes that are used for transmission. Deserialization does the opposite of serialization, in which we convert bytes of arrays into the desired data type.
- D. Serialization is the process of producing key / value based Avro messages into a Kafka topic. Deserialization does the opposite of serialization, in which we consume key / value based Avro messages from a Kafka topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When writing messages to Kafka you need to create a producer object with the properties you want to pass to the producer. Two of the three mandatory properties are (this concept is called serialization): – key.serializer: Name of a class that will be used to serialize the keys of the records we will produce to Kafka. Kafka brokers expect byte arrays as keys and values of messages. However, the producer interface allows, using parameterized types, any Java object to be sent as a key and value. This makes for very readable code, but it also means that the producer has to know how to convert these objects to byte arrays. – value.serializer: Name of a class that will be used to serialize the values of the records we will produce to Kafka. The same way you set key.serializer to a name of a class that will serialize the message key object to a byte array, you set value.serializer to a class that will serialize the message value object. The opposite properties are needed for consumers to read messages from Kafka (this concept is called deserialization): – key.deserializer / value.deserializer: Similar to the serializers defined for the producer, but rather than specifying classes that turn Java objects to byte arrays, you need to specify classes that can take a byte array and turn it into a Java object.

**Detailed explanation of each option:**

1. ❌ **A. Serialization is the process of consuming key / value based Avro messages from a Kafka topic. Deserialization does the opposite of serialization, in which we produce key / value based Avro messages into a Kafka topic.**  
   **Incorrect**.

2. ❌ **B. Serialization is the process of converting bytes of arrays into the desired data type that are used for transmission. Deserialization does the opposite of serialization, in which we convert an object into a stream of bytes.**  
   **Incorrect**.

3. ✅ **C. Serialization is the process of converting an object into a stream of bytes that are used for transmission. Deserialization does the opposite of serialization, in which we convert bytes of arrays into the desired data type.**  
   **Correct**.

4. ❌ **D. Serialization is the process of producing key / value based Avro messages into a Kafka topic. Deserialization does the opposite of serialization, in which we consume key / value based Avro messages from a Kafka topic.**  
   **Incorrect**.

</details>

## Question 25 (Programming & Serialization):
Which of the following fields is optional in an Avro record? 

- A. doc
- B. fields
- C. symbols
- D. name

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. doc**  
   **Correct**.

2. ❌ **B. fields**  
   **Incorrect**.

3. ❌ **C. symbols**  
   **Incorrect**.

4. ❌ **D. name**  
   **Incorrect**.

</details>

## Question 26 (Kafka Core Concepts):
Which of the following options is true about topic partitions? 

- A. Different partitions always have the same number of messages when using a round robin distribution.
- B. Ordering of messages is guaranteed across topic partitions.
- C. Once data is written to a partition, it can‘t be changed.
- D. Offsets have a meaning only for partitions from the same topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, events are organized and durably stored in topics. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder. Topics are partitioned, meaning a topic is spread over a number of “buckets“ located on different Kafka brokers. Some of the main aspects about topic partitions in Kafka are: – Kafka guarantees that any consumer of a given topic-partition will always read that partition‘s events in exactly the same order as they were written. – Order is guaranteed only within a partition (not across partitions). – Partitions do not need to have the same number of messages. – Offsets only have a meaning for a specific partition. – Messages are kept only for a limited time in Kafka (default is one week). – Once the data is written to a partition, it can‘t be changed (immutability). – Data is assigned randomly to a partition unless a key is provided.

**Detailed explanation of each option:**

1. ❌ **A. Different partitions always have the same number of messages when using a round robin distribution.**  
   **Incorrect**.

2. ❌ **B. Ordering of messages is guaranteed across topic partitions.**  
   **Incorrect**.

3. ✅ **C. Once data is written to a partition, it can‘t be changed.**  
   **Correct**.

4. ❌ **D. Offsets have a meaning only for partitions from the same topic.**  
   **Incorrect**.

</details>

## Question 27 (Kafka Setup and Operations):
Which of the following statements are true regarding the number of partitions of a topic?

- A. We can remove partitions in a topic using the kafka-topics.sh command
- B. The number of partitions in a topic cannot be altered
- C. We can remove partitions in a topic by removing a broker
- D. We can add partitions in a topic using the kafka-topics.sh command
- E. We can add partitions in a topic by adding a broker to the cluster

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

We can only add partitions to an existing topic, and it must be done using the kafka-topics.sh command

**Detailed explanation of each option:**

1. ❌ **A. We can remove partitions in a topic using the kafka-topics.sh command**  
   **Incorrect**.

2. ❌ **B. The number of partitions in a topic cannot be altered**  
   **Incorrect**.

3. ❌ **C. We can remove partitions in a topic by removing a broker**  
   **Incorrect**.

4. ✅ **D. We can add partitions in a topic using the kafka-topics.sh command**  
   **Correct**.

5. ❌ **E. We can add partitions in a topic by adding a broker to the cluster**  
   **Incorrect**.

</details>

## Question 28 (Kafka Consumers):
Which consumer becomes the group leader of a consumer application? 

- A. The group leader is elected by the Kafka brokers.
- B. The group leader is elected by the group coordinator.
- C. The last consumer to join the group.
- D. The first consumer to join the group.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Correct: Option D. The first consumer to join the group. In Apache Kafka consumer groups, the group coordinator designates one consumer as the group leader, and this is typically the first consumer that successfully joins the group. The leader is responsible for performing partition assignment and distributing the assignment to the other consumers in the group.

**Detailed explanation of each option:**

1. ❌ **A. The group leader is elected by the Kafka brokers.**  
   **Incorrect**.

2. ❌ **B. The group leader is elected by the group coordinator.**  
   **Incorrect**.

3. ❌ **C. The last consumer to join the group.**  
   **Incorrect**.

4. ✅ **D. The first consumer to join the group.**  
   **Correct**.

</details>

## Question 29 (Stream Processing):
Which of the following options best describes the difference between stateless and stateful operations? 

- A. Stateless transformations do not require state for processing while stateful transformations depend on state for processing inputs.
- B. Stateful transformations do not require state for processing while stateless transformations depend on state for processing inputs.
- C. Stateless transformations always lead into KStreams while stateful transformations lead into KTables.
- D. Stateless transformations require a state store while stateful transformations do not require a state store.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The KStream and KTable interfaces support a variety of transformation operations. The available transformations can be either stateful or stateless: – Stateless transformations do not require state for processing and they do not require a state store associated with the stream processor, for example filtering. – Stateful transformations depend on state for processing inputs and producing outputs and require a state store associated with the stream processor. For example, in aggregating operations, a windowing state store is used to collect the latest aggregation results per window. In join operations, a windowing state store is used to collect all of the records received so far within the defined window boundary.

**Detailed explanation of each option:**

1. ✅ **A. Stateless transformations do not require state for processing while stateful transformations depend on state for processing inputs.**  
   **Correct**.

2. ❌ **B. Stateful transformations do not require state for processing while stateless transformations depend on state for processing inputs.**  
   **Incorrect**.

3. ❌ **C. Stateless transformations always lead into KStreams while stateful transformations lead into KTables.**  
   **Incorrect**.

4. ❌ **D. Stateless transformations require a state store while stateful transformations do not require a state store.**  
   **Incorrect**.

</details>

## 🚫 Question 30 (Kafka Setup and Operations):
What file systems should you choose for your production deployment of Kafka?

- A. XFS
- B. ext4
- C. FAT12
- D. HFS

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. XFS**  
   **Correct**.

2. ✅ **B. ext4**  
   **Correct**.

3. ❌ **C. FAT12**  
   **Incorrect**.

4. ❌ **D. HFS**  
   **Incorrect**.

</details>

## Question 31 (Kafka Internals):
In Kafka, how many leaders can each topic partition have?

- A. As many as there are brokers in the cluster.
- B. As many as there are partitions for the topic.
- C. A partition only has followers.
- D. Exactly one leader.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Every topic partition has exactly one partition leader which handles all the read / write requests of that partition. If replication factor is greater than 1, the additional partition replications acts as partition followers. Kafka guarantees every partition replica resides on a different broker (whether if it is the leader or a follower), so maximum replication factor is the brokers number. Every partition follower is reading messages from the partition leader (acts like a kind of consumer) and does not serve any consumers of that partition (only the partition leader serves read / writes). Further reading: Replication.

**Detailed explanation of each option:**

1. ❌ **A. As many as there are brokers in the cluster.**  
   **Incorrect**.

2. ❌ **B. As many as there are partitions for the topic.**  
   **Incorrect**.

3. ❌ **C. A partition only has followers.**  
   **Incorrect**.

4. ✅ **D. Exactly one leader.**  
   **Correct**.

</details>

## Question 32 (Kafka Setup and Operations):
What‘s the use of the Kafka Admin API? 

- A. The Admin API supports managing Zookeeper configuration.
- B. The Admin API supports managing the producer and consumer communication.
- C. The Admin API supports managing background processes for overall performance tuning.
- D. The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects. To use the Admin API, add the following Maven dependency to your Java project:

**Detailed explanation of each option:**

1. ❌ **A. The Admin API supports managing Zookeeper configuration.**  
   **Incorrect**.

2. ❌ **B. The Admin API supports managing the producer and consumer communication.**  
   **Incorrect**.

3. ❌ **C. The Admin API supports managing background processes for overall performance tuning.**  
   **Incorrect**.

4. ✅ **D. The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects.**  
   **Correct**.

</details>

## Question 33 (Kafka Setup and Operations):
Which security concept allows you to protect your data in transit instead of using the default unsecured PLAINTEXT protocol? 

- A. Authentication - configured using SASL or mTLS.
- B. Encryption - configured using the listener configuration and managing truststores and keystores.
- C. Encryption - configured using ACLs and RBAC.
- D. Authorization - configured using the LDAP Authorizer.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

By default, there is no encryption or authentication, nor are ACLs configured. Any client can communicate to Kafka brokers using the PLAINTEXT port. Encrypting data in transit between brokers and applications mitigates risks for unintended interception of data across the network. Authentication and encryption are defined in Kafka per listener. By default, Kafka listeners use an unsecured PLAINTEXT protocol that is acceptable for development environments; however, all production environments should enable SSL encryption. Encryption on brokers is configured using the listener configuration and managing truststores and keystores. Further reading: Encryption with SSL.

**Detailed explanation of each option:**

1. ❌ **A. Authentication - configured using SASL or mTLS.**  
   **Incorrect**.

2. ✅ **B. Encryption - configured using the listener configuration and managing truststores and keystores.**  
   **Correct**.

3. ❌ **C. Encryption - configured using ACLs and RBAC.**  
   **Incorrect**.

4. ❌ **D. Authorization - configured using the LDAP Authorizer.**  
   **Incorrect**.

</details>

## Question 34 (Kafka Producers):
In Kafka, what are the most important producer configurations?

- A. acks
- B. replication factor
- C. compression
- D. batch size

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

The most important producer configurations are: – acks: The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. – compression: The compression type for all data generated by the producer. The default is none (i. e. no compression). – batch size: The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. Further reading: Kafka Producer Configs.

**Detailed explanation of each option:**

1. ✅ **A. acks**  
   **Correct**.

2. ❌ **B. replication factor**  
   **Incorrect**.

3. ✅ **C. compression**  
   **Correct**.

4. ✅ **D. batch size**  
   **Correct**.

</details>

## Question 35 (Kafka Setup and Operations):
Under the hood, which process is used by Kafka brokers that handles the deletion of unused objects or some objects that are inaccessible to free up memory resources to tune the overall performance? 

- A. Data Compression
- B. Garbage Collection
- C. Zookeeper Cleaning
- D. Message Batching

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Java, process of deallocating memory is handled automatically by the garbage collector. Kafka brokers as JVMs rely heavily on the garbage collector for overall performance tuning. The biggest benefit of Java garbage collection is that it automatically handles the deletion of unused objects or some objects that are inaccessible to free up memory resources. Garbage collection prevents several potential bugs that occur in manually managed memory, such as dangling pointers, double free errors, and several types of memory leaks.

**Detailed explanation of each option:**

1. ❌ **A. Data Compression**  
   **Incorrect**.

2. ✅ **B. Garbage Collection**  
   **Correct**.

3. ❌ **C. Zookeeper Cleaning**  
   **Incorrect**.

4. ❌ **D. Message Batching**  
   **Incorrect**.

</details>

## Question 36 (Kafka Consumers):
Which concept can be used to fetch a specific message with specific offsets or to replay data for a consumer? 

- A. Use the commitSync() API.
- B. Use the fetch() API.
- C. Use the poll() API.
- D. Use the assign() and seek() APIs.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. If you want to start reading all messages from the beginning of the partition, or you want to skip all the way to the end of the partition and start consuming only new messages, there are APIs specifically for that: seekToBeginning(TopicPartition tp) and seekToEnd(TopicPartition tp). However, sometimes you want to start reading at a different offset for specific partitions: 1: The consumer can manually assign specific partitions using assign(Collection). 2: Kafka allows specifying the position using seek(TopicPartition, long) to specify the new position (offset) a consumer can read from. Further reading: Consumer APIs.

**Detailed explanation of each option:**

1. ❌ **A. Use the commitSync() API.**  
   **Incorrect**.

2. ❌ **B. Use the fetch() API.**  
   **Incorrect**.

3. ❌ **C. Use the poll() API.**  
   **Incorrect**.

4. ✅ **D. Use the assign() and seek() APIs.**  
   **Correct**.

</details>

## 🚫 Question 37 (Kafka Ecosystem):
Where are KSQL-related data and metadata stored?

- A. Kafka Topics
- B. Schema Registry
- C. Zookeeper
- D. PostgreSQL database

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. Kafka Topics**  
   **Correct**.

2. ❌ **B. Schema Registry**  
   **Incorrect**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ❌ **D. PostgreSQL database**  
   **Incorrect**.

</details>

## 🚫 Question 38 (Kafka Ecosystem):
Using ksqlDB, which of the following two options together allow you to use Avro data and integrate with Confluent Schema Registry?

- A. Configure your Kafka cluster to use SQL as the default programming language.
- B. Configure the “ksql.schema.registry.url“ property in the ksqlDB server configuration to point to Schema Registry.
- C. To use Avro data with ksqlDB you must have Schema Registry installed.
- D. Configure the “enable.avro.registry“ property in the ksqlDB server configuration and use the Confluent Control Center to point to the Schema Registry.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Configure your Kafka cluster to use SQL as the default programming language.**  
   **Incorrect**.

2. ✅ **B. Configure the “ksql.schema.registry.url“ property in the ksqlDB server configuration to point to Schema Registry.**  
   **Correct**.

3. ✅ **C. To use Avro data with ksqlDB you must have Schema Registry installed.**  
   **Correct**.

4. ❌ **D. Configure the “enable.avro.registry“ property in the ksqlDB server configuration and use the Confluent Control Center to point to the Schema Registry.**  
   **Incorrect**.

</details>

## Question 39 (Kafka Core Concepts):
Kafka is a distributed system consisting of servers and clients that communicate via a simple high-performance network protocol. Which network protocol is used by Kafka to achieve the high performance? 

- A. SMPT
- B. TCP
- C. FTP
- D. UDP

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka uses a binary protocol over TCP. The protocol defines all APIs as request response message pairs. The server guarantees that on a single TCP connection, requests will be processed in the order they are sent and responses will return in that order as well. Further reading: Network Protocol.

**Detailed explanation of each option:**

1. ❌ **A. SMPT**  
   **Incorrect**.

2. ✅ **B. TCP**  
   **Correct**.

3. ❌ **C. FTP**  
   **Incorrect**.

4. ❌ **D. UDP**  
   **Incorrect**.

</details>

## Question 40 (Kafka Consumers):
A company monitors their production consumer application and observed that the fetch-rate is very high, but each fetch is small. How could the company increase throughput in this situation? 

- A. Decrease fetch.max.bytes.
- B. Decrease fetch.min.bytes.
- C. Increase fetch.min.bytes.
- D. Increase fetch.max.bytes.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Decrease fetch.max.bytes.**  
   **Incorrect**.

2. ❌ **B. Decrease fetch.min.bytes.**  
   **Incorrect**.

3. ✅ **C. Increase fetch.min.bytes.**  
   **Correct**.

4. ❌ **D. Increase fetch.max.bytes.**  
   **Incorrect**.

</details>

## Question 41 (Programming & Serialization):
Which of the following options best describes unit testing? 

- A. Unit tests verify that development environments behave as expected.
- B. Unit tests verify that production deployments work as expected.
- C. Unit tests verify that isolated functional blocks of code work as expected.
- D. Unit tests verify that end-to-end tests with other services work as expected.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Unit testing, integration testing, and schema compatibility are all important steps in building resilient applications in a CI/CD pipeline. Unit tests run very quickly and verify that isolated functional blocks of code work as expected. They can test the logic of your application with minimal dependencies on other services. Further reading: Application Testing.

**Detailed explanation of each option:**

1. ❌ **A. Unit tests verify that development environments behave as expected.**  
   **Incorrect**.

2. ❌ **B. Unit tests verify that production deployments work as expected.**  
   **Incorrect**.

3. ✅ **C. Unit tests verify that isolated functional blocks of code work as expected.**  
   **Correct**.

4. ❌ **D. Unit tests verify that end-to-end tests with other services work as expected.**  
   **Incorrect**.

</details>

## Question 42 (Kafka Consumers):
What happens for a consumer with the configuration “auto.offset.reset=none“, if there is no initial offset in Kafka or if the current offset does not exist any more on the server?

- A. The consumer automatically resets the offset to the latest offset.
- B. The consumer automatically resets the offset to the earliest offset.
- C. The consumer throws an exception.
- D. The consumer restores the offset history from the official Kafka archive.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The consumer configuration “auto.offset.reset“ tells the consumer what to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server (e. g. because that data has been deleted). There are the following options: – earliest: Automatically reset the offset to the earliest offset. – latest: Automatically reset the offset to the latest offset. – none: Throw exception to the consumer if no previous offset is found for the consumer‘s group. – anything else: Throw exception to the consumer. Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. The consumer automatically resets the offset to the latest offset.**  
   **Incorrect**.

2. ❌ **B. The consumer automatically resets the offset to the earliest offset.**  
   **Incorrect**.

3. ✅ **C. The consumer throws an exception.**  
   **Correct**.

4. ❌ **D. The consumer restores the offset history from the official Kafka archive.**  
   **Incorrect**.

</details>

## Question 43 (Kafka Consumers):
A company disabled auto commit of offsets for their consumer application in order to have more control over the time at which offsets are committed. What‘s the simplest way to manually commit the offsets? 

- A. Use the close() API.
- B. Use the commitSync() API.
- C. Use the poll() API.
- D. Use the fetch() API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. Automatic commits are convenient, but they dont give developers enough control to avoid duplicate messages. By setting auto.commit.offset=false, offsets will only be committed when the application explicitly chooses to do so. The simplest and most reliable of the commit APIs is commitSync(). This API will commit the latest offset returned by poll() and return once the offset is committed, throwing an exception if commit fails for some reason. Note: Make sure you call commitSync() after you are done processing all the records in the collection, or you risk missing messages. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Use the close() API.**  
   **Incorrect**.

2. ✅ **B. Use the commitSync() API.**  
   **Correct**.

3. ❌ **C. Use the poll() API.**  
   **Incorrect**.

4. ❌ **D. Use the fetch() API.**  
   **Incorrect**.

</details>

## Question 44 (Kafka Producers):
When sending a producer record to the Kafka broker, what does the send() method return?

- A. The send() method returns an Object with RecordMetadata.
- B. The send() method returns true if the call succeeded and false if the call did not succeed.
- C. The send() method returns a Future Object with RecordMetadata.
- D. The send() method returns 1 if the call succeeded and 0 if the call did not succeed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

KafkaProducer is a Kafka client that publishes records to the Kafka cluster. The send() method is asynchronous and it sends the ProducerRecord. The message will then be placed in a buffer and will be sent to the broker in a separate thread. The send() method returns a Future object with RecordMetadata. Further reading: Producer API.

**Detailed explanation of each option:**

1. ❌ **A. The send() method returns an Object with RecordMetadata.**  
   **Incorrect**.

2. ❌ **B. The send() method returns true if the call succeeded and false if the call did not succeed.**  
   **Incorrect**.

3. ✅ **C. The send() method returns a Future Object with RecordMetadata.**  
   **Correct**.

4. ❌ **D. The send() method returns 1 if the call succeeded and 0 if the call did not succeed.**  
   **Incorrect**.

</details>

## Question 45 (Kafka Consumers):
A company is developing a new sales strategy for which the Kafka topic receives all the underlying customer asked questions. Two different departments want to process all the available messages independently from each other. How should the consumption of these messages be organized when the topic has 3 partitions and the company aims for optimal resource usage and performance? 

- A. Create two consumer groups for two department applications with 6 consumers in each.
- B. Create 6 consumers in the same group with 3 consumers for each department application.
- C. Create 3 consumers in the same group, one for each partition. Split them among the department applications as needed for optimal performance and resource usage.
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

2. ❌ **B. Create 6 consumers in the same group with 3 consumers for each department application.**  
   **Incorrect**.

3. ❌ **C. Create 3 consumers in the same group, one for each partition. Split them among the department applications as needed for optimal performance and resource usage.**  
   **Incorrect**.

4. ✅ **D. Create two consumer groups for two department applications with 3 consumers in each.**  
   **Correct**.

</details>

## Question 46 (Kafka Producers):
What happens if you write the following code in your producer? producer.send(producerRecord).get()

- A. Compression will be increased
- B. Throughput will be decreased
- C. Batching will be increased
- D. It will force all brokers in Kafka to acknowledge the producerRecord

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Using Future.get() to wait for a reply from Kafka will limit throughput.

**Detailed explanation of each option:**

1. ❌ **A. Compression will be increased**  
   **Incorrect**.

2. ✅ **B. Throughput will be decreased**  
   **Correct**.

3. ❌ **C. Batching will be increased**  
   **Incorrect**.

4. ❌ **D. It will force all brokers in Kafka to acknowledge the producerRecord**  
   **Incorrect**.

</details>

## Question 47 (Kafka Internals):
Which of the following options are true for a Kafka Controller?

- A. It is a Kafka broker which is responsible for partition leader election.
- B. At any time at least two Controller brokers must exist to perform majority votings.
- C. It is a Kafka broker which is elected by Zookeeper.
- D. It is a Kafka broker which is responsible for consumer group rebalances.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

In a Kafka cluster, one (and only one) of the brokers serves as the controller, which is responsible for managing the states of partitions and replicas and for performing administrative tasks like reassigning partitions. The election of that broker happens thanks to Zookeeper. Kafka Controller registers handlers to be notified about changes in Zookeeper and propagate them across brokers in a Kafka cluster. Further reading: Controller Internals.

**Detailed explanation of each option:**

1. ✅ **A. It is a Kafka broker which is responsible for partition leader election.**  
   **Correct**.

2. ❌ **B. At any time at least two Controller brokers must exist to perform majority votings.**  
   **Incorrect**.

3. ✅ **C. It is a Kafka broker which is elected by Zookeeper.**  
   **Correct**.

4. ❌ **D. It is a Kafka broker which is responsible for consumer group rebalances.**  
   **Incorrect**.

</details>

## Question 48 (Kafka Producers):
Which of the following components is not part of the Kafka producer workflow? 

- A. Partitioner
- B. ProducerRecord
- C. Serializer
- D. Deserializer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, producers create and write messages to topic partitions. We start producing messages to Kafka by creating a ProducerRecord, which must include the topic we want to send the record to and a value. Optionally, we can also specify a key and / or partition (ProducerRecord). Once we send the ProducerRecord, the first thing the producer will do is serialize the key and value objects to ByteArrays so they can be sent over the network (Serializer). Next, the data is sent to a partitioner. If we specified a partition in the ProducerRecord, the partitioner doesn‘t do anything and simply returns the partition we specified. If we didn‘t, the partitioner will choose a partition for us (Partitioner). Further reading: Producer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Partitioner**  
   **Incorrect**.

2. ❌ **B. ProducerRecord**  
   **Incorrect**.

3. ❌ **C. Serializer**  
   **Incorrect**.

4. ✅ **D. Deserializer**  
   **Correct**.

</details>

## Question 49 (Kafka Core Concepts):
What is a generic unique id that I can use for messages I receive from a consumer?

- A. topic + partition + offset
- B. topic + timestamp
- C. topic + partition + timestamp

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. topic + partition + offset**  
   **Correct**.

2. ❌ **B. topic + timestamp**  
   **Incorrect**.

3. ❌ **C. topic + partition + timestamp**  
   **Incorrect**.

</details>

## Question 50 (Kafka Setup and Operations):
For the initial connection to a Kafka cluster, why can it be useful to set the “bootstrap-server“ property to a comma-separated list of host and port pairs that are the addresses of the Kafka brokers instead of just using one host and port pair? 

- A. In case one of the brokers is experiencing a down time.
- B. Not every broker knows everything about the other brokers, topics and partitions.
- C. If you use just one host and port pair you can only produce and consume to this specific broker.
- D. You need to connect to at least two brokers to get connected to the whole cluster.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The bootstrap.server property is a comma-separated list of host and port pairs that are the addresses of the Kafka brokers in a “bootstrap“ Kafka cluster that a Kafka client connects to initially to bootstrap itself. A host and port pair uses : as the separator (e. g. hostname:9092, hostname:9093). bootstrap.server provides the initial hosts that act as the starting point for a Kafka client to discover the full set of alive servers in the cluster. Since these servers are just used for the initial connection to discover the full cluster membership (which may change dynamically), this list does not have to contain the full set of servers (you may want more than one, though, in case a server is down). Advantages of Kafka Broker Discovery: – every broker is also called a “bootstrap server“ – that means that you only need to connect to one broker, and you will be connected to the whole cluster – each broker knows about all other brokers, topics and partitions (metadata), even though he does not need all the data

**Detailed explanation of each option:**

1. ✅ **A. In case one of the brokers is experiencing a down time.**  
   **Correct**.

2. ❌ **B. Not every broker knows everything about the other brokers, topics and partitions.**  
   **Incorrect**.

3. ❌ **C. If you use just one host and port pair you can only produce and consume to this specific broker.**  
   **Incorrect**.

4. ❌ **D. You need to connect to at least two brokers to get connected to the whole cluster.**  
   **Incorrect**.

</details>

## Question 51 (Stream Processing):
What‘s a benefit of using a GlobalKTable when joining input data? 

- A. Input topics of the join automatically have the same number of partitions.
- B. Joins against a GlobalKTable are always windowed and therefore more efficient.
- C. Decreased local storage consumption compared to the KTable because not the entire topic is tracked.
- D. Input data does not need to be co-partitioned.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Like a KTable, a GlobalKTable is an abstraction of a changelog stream, where each data record represents an update. A GlobalKTable differs from a KTable in the data that they are being populated with, i. e. which data from the underlying Kafka topic is being read into the respective table. If you read the input topic into a GlobalKTable, then the local GlobalKTable instance of each application instance will be populated with data from all partitions of the topic (when using a KTable you only read data from one partition). More convenient and / or efficient joins are the main benefit of this concept. Also, when joining against a global table, the input data does not need to be co-partitioned. GlobalKTables can also be used to “broadcast“ information to all the running instances of your application. The downsides of global tables are the increased local storage consumption and the increased network and Kafka broker load because the entire topic is read. Further reading: GlobalKTable Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Input topics of the join automatically have the same number of partitions.**  
   **Incorrect**.

2. ❌ **B. Joins against a GlobalKTable are always windowed and therefore more efficient.**  
   **Incorrect**.

3. ❌ **C. Decreased local storage consumption compared to the KTable because not the entire topic is tracked.**  
   **Incorrect**.

4. ✅ **D. Input data does not need to be co-partitioned.**  
   **Correct**.

</details>

## Question 52 (Kafka Setup and Operations):
Which CLI command can be used to find out all the partitions without a leader? 

- A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topics-with-overrides
- B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions
- C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --unavailable-partitions
- D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, the purpose of describing topics is to know the leader for the topic, the broker instances acting as replicas for the topic, and the number of partitions of a Kafka topic that has been created with. When describing Kafka topics you can set some additional properties to only show specific topics / partitions, e. g.: –topics-with-overrides: If set when describing topics, only show topics that have overridden configs. –unavailable-partitions: If set when describing topics, only show partitions whose leader is not available. –under-min-isr-partitions: If set when describing topics, only show partitions whose ISR count is less than the configured minimum. –under-replicated-partitions: If set when describing topics, only show under replicated partitions.

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topics-with-overrides**  
   **Incorrect**.

2. ❌ **B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions**  
   **Incorrect**.

3. ✅ **C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --unavailable-partitions**  
   **Correct**.

4. ❌ **D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions**  
   **Incorrect**.

</details>

## Question 53 (Reliable Data Delivery):
Using the configuration “replication.factor=3“, “min.insync.replicas=2“ and “acks=all“, what happens if two brokers are down and a consumer group tries to consume from Kafka?

- A. A new broker will be initialized and synced with the remaining replica.
- B. There will be a NOT_ENOUGH_REPLICAS exception.
- C. The remaining replica returns the data.
- D. The consumer application waits until enough replicas are back up.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, producers create and write messages to topic partitions and consumers read data from these partitions. With acks=all and a replication factor of 3 and two brokers are down, the minimum of in-sync replicas cannot be met. Therefore a producer would raise an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend). For a consumer though, it‘s still possible to read data from the remaining replica.

**Detailed explanation of each option:**

1. ❌ **A. A new broker will be initialized and synced with the remaining replica.**  
   **Incorrect**.

2. ❌ **B. There will be a NOT_ENOUGH_REPLICAS exception.**  
   **Incorrect**.

3. ✅ **C. The remaining replica returns the data.**  
   **Correct**.

4. ❌ **D. The consumer application waits until enough replicas are back up.**  
   **Incorrect**.

</details>

## Question 54 (Programming & Serialization):
A company produces Avro data on their production Kafka cluster that is integrated with the Confluent Schema Registry. After a schema change that is incompatible, the data gets rejected. Which component rejects the data?

- A. Kafka Client
- B. Kafka Broker
- C. Zookeeper
- D. Confluent Schema Registry

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Correct:

**Detailed explanation of each option:**

1. ❌ **A. Kafka Client**  
   **Incorrect**.

2. ❌ **B. Kafka Broker**  
   **Incorrect**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ✅ **D. Confluent Schema Registry**  
   **Correct**.

</details>

## Question 55 (Kafka Setup and Operations):
Which Kafka metric could be used if there is a lot of load on the system and you want to figure out what could be the problem for lag spikes? 

- A. Reassigning Partitions
- B. Under Replicated Partitions
- C. Bytes In Per Sec
- D. Partition Count

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Reassigning Partitions**  
   **Incorrect**.

2. ✅ **B. Under Replicated Partitions**  
   **Correct**.

3. ❌ **C. Bytes In Per Sec**  
   **Incorrect**.

4. ❌ **D. Partition Count**  
   **Incorrect**.

</details>

## Question 56 (Kafka Producers):
You want to send a message of size 3 MB to a topic with default message size configuration. How does KafkaProducer handle large messages?

- A. MessageSizeTooLarge exception will be thrown, KafkaProducer retries until the number of retries are exhausted
- B. MessageSizeTooLarge exception will be thrown, KafkaProducer will not retry and return exception immediately
- C. KafkaProducer divides messages into sizes of max.request.size and sends them in order
- D. KafkaProducer divides messages into sizes of message.max.bytes and sends them in order

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

MessageSizeTooLarge is not a retryable exception.

**Detailed explanation of each option:**

1. ❌ **A. MessageSizeTooLarge exception will be thrown, KafkaProducer retries until the number of retries are exhausted**  
   **Incorrect**.

2. ✅ **B. MessageSizeTooLarge exception will be thrown, KafkaProducer will not retry and return exception immediately**  
   **Correct**.

3. ❌ **C. KafkaProducer divides messages into sizes of max.request.size and sends them in order**  
   **Incorrect**.

4. ❌ **D. KafkaProducer divides messages into sizes of message.max.bytes and sends them in order**  
   **Incorrect**.

</details>

## Question 57 (Stream Processing):
We want the average of all events in every five-minute window updated every minute. What kind of Kafka Streams window will be required on the stream?

- A. Hopping window
- B. Session window
- C. Tumbling window
- D. Sliding window

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

A hopping window is defined by two properties: the window‘s size and its advance interval (aka “hop“), e.g., a hopping window with a size 5 minutes and an advance interval of 1 minute.

**Detailed explanation of each option:**

1. ✅ **A. Hopping window**  
   **Correct**.

2. ❌ **B. Session window**  
   **Incorrect**.

3. ❌ **C. Tumbling window**  
   **Incorrect**.

4. ❌ **D. Sliding window**  
   **Incorrect**.

</details>
