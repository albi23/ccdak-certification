## Question 1 (Kafka Internals):
In Kafka, how is a topic partition structured? 

- A. Partitions are made of one segment that comes with one index.
- B. Partitions are made of segments that come with one index.
- C. Partitions are made of one segment that comes with two indexes.
- D. Partitions are made of segments that come with two indexes.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

1. ❌ **A. Partitions are made of one segment that comes with one index.**  
   **Incorrect**.

2. ❌ **B. Partitions are made of segments that come with one index.**  
   **Incorrect**.

3. ❌ **C. Partitions are made of one segment that comes with two indexes.**  
   **Incorrect**.

4. ✅ **D. Partitions are made of segments that come with two indexes.**  
   A log file (the actual messages). An offset index (mapping offsets to physical file positions). A time index (mapping timestamps to offsets). Together, these two indexes allow efficient lookups by offset and by timestamp, which is the correct structure of a Kafka partition.

</details>

## Question 2 (Stream Processing):
Which approach should be used when transforming data from one Kafka topic to another one? 

- A. Use ksqlDB.
- B. Use Kafka Connect Sink.
- C. Use a Consumer to consume from one topic and a Producer to produce to another topic.
- D. Use Kafka Streams.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Streams is a client library for building streaming applications and microservices, where the input and output data are stored in Kafka clusters. Kafka‘s cluster architecture makes Kafka Streams fault-tolerant, highly-scalable, and especially elastic solution. Kafka Streams utilizes exactly-once processing (Kafka topic -> Kafka topic) semantics, connects directly to Kafka, and does not require any separate processing cluster. Kafka‘s Streams library is built on top of the Kafka producer and consumer clients, but it is significantly more powerful and also more expressive than the plain clients. Also it is much simpler and quicker to write a real-world application start to finish with Kafka Streams than with the plain consumer. Further reading: Kafka Streams.

**Detailed explanation of each option:**

1. ❌ **A. Use ksqlDB.**  
   **Incorrect**.

2. ❌ **B. Use Kafka Connect Sink.**  
   **Incorrect**.

3. ❌ **C. Use a Consumer to consume from one topic and a Producer to produce to another topic.**  
   **Incorrect**.

4. ✅ **D. Use Kafka Streams.**  
   **Correct**.

</details>

## Question 3 (Kafka Setup and Operations):
A company developed a sales producer application in their development environment without having any broker to client communication issues. The next step was to deploy the application into the cloud to scale globally in different regions worldwide. After copying the application into the cloud, the producer is able to connect to Kafka but unable to produce to the same Kafka topic because of an authorization issue. What‘s the likely issue? 

- A. Kafka topics cannot be copied into cloud environments and therefore it does not exist.
- B. RBAC is not enabled by default for cloud deployments.
- C. Producer and Consumer operate in different regions.
- D. ACLs are configured for specific host IPs only.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Access Control Lists (ACLs) provide important authorization controls for your enterprise‘s Kafka cluster data. The following command can be used to set the required ACLs to allow a specific user “Bob“ to read and write to the topic “test-topic“ from host “test-host“: bin/kafka-acls.sh –authorizer-properties zookeeper.connect=localhost:2181 –add –allow-principal User:Bob –allow-host test-host –operation read –operation write –topic test-topic This means, that the access to the topic test-topic is only allowed for the specified host. If you move the application to another host, the ACLs need to be updated. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Kafka topics cannot be copied into cloud environments and therefore it does not exist.**  
   **Incorrect**.

2. ❌ **B. RBAC is not enabled by default for cloud deployments.**  
   **Incorrect**.

3. ❌ **C. Producer and Consumer operate in different regions.**  
   **Incorrect**.

4. ✅ **D. ACLs are configured for specific host IPs only.**  
   **Correct**.

</details>

## Question 4 (Kafka Consumers):
A company is building a consumer application that processes events from a Kafka topic. What is the most important metric the company should monitor to ensure real-time processing? 

- A. records-per-request-avg
- B. bytes-consumed-total
- C. fetch-total
- D. records-lag-max

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The most important consumer fetch metric to ensure real-time-processing is records-lag-max. It‘s the maximum lag in terms of number of records for any partition (number of messages behind the broker). Further reading: Consumer Metrics.

**Detailed explanation of each option:**

1. ❌ **A. records-per-request-avg**  
   **Incorrect**.

2. ❌ **B. bytes-consumed-total**  
   **Incorrect**.

3. ❌ **C. fetch-total**  
   **Incorrect**.

4. ✅ **D. records-lag-max**  
   **Correct**.

</details>

## Question 5 (Kafka Consumers):
A company disabled auto commit of offsets for their consumer application in order to have more control over the time at which offsets are committed. What‘s a good way to manually commit the offsets, if the company does not want to block the application until the broker responds to the commit request?

- A. Use the commitAsync() API.
- B. Use the commitSync() API.
- C. Use the poll() API.
- D. Use await / async in the consumer application.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. Automatic commits are convenient, but they dont give developers enough control to avoid duplicate messages. By setting auto.commit.offset=false, offsets will only be committed when the application explicitly chooses to do so. The simplest and most reliable of the commit APIs is commitSync(), but this will block the application until the broker responds to the commit request. Another option is the asynchronous commit API commitAsync(), which will not block the application and not limit the throughput of the application. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Use the commitAsync() API.**  
   **Correct**.

2. ❌ **B. Use the commitSync() API.**  
   **Incorrect**.

3. ❌ **C. Use the poll() API.**  
   **Incorrect**.

4. ❌ **D. Use await / async in the consumer application.**  
   **Incorrect**.

</details>

## Question 6 (Kafka Producers):
Which of the following components is not part of the Kafka producer workflow?

- A. ProducerRecord
- B. Deserializer
- C. Serializer
- D. Partitioner

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, producers create and write messages to topic partitions. We start producing messages to Kafka by creating a ProducerRecord, which must include the topic we want to send the record to and a value. Optionally, we can also specify a key and / or partition (ProducerRecord).Once we send the ProducerRecord, the first thing the producer will do is serialize the key and value objects to ByteArrays so they can be sent over the network (Serializer).Next, the data is sent to a partitioner. If we specified a partition in the ProducerRecord, the partitioner doesn‘t do anything and simply returns the partition we specified. If we didn‘t, the partitioner will choose a partition for us (Partitioner).Further reading: Producer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. ProducerRecord**  
   **Incorrect**.

2. ✅ **B. Deserializer**  
   **Correct**.

3. ❌ **C. Serializer**  
   **Incorrect**.

4. ❌ **D. Partitioner**  
   **Incorrect**.

</details>

## Question 7 (Kafka Core Concepts):
Which of the following options is true about topic partitions?

- A. Ordering of messages is guaranteed across topic partitions.
- B. Once data is written to a partition, it can‘t be changed.
- C. Offsets have a meaning only for partitions from the same topic.
- D. Different partitions always have the same number of messages when using a round robin distribution.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, events are organized and durably stored in topics. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder. Topics are partitioned, meaning a topic is spread over a number of “buckets“ located on different Kafka brokers. Some of the main aspects about topic partitions in Kafka are: – Kafka guarantees that any consumer of a given topic-partition will always read that partition‘s events in exactly the same order as they were written. – Order is guaranteed only within a partition (not across partitions). – Partitions do not need to have the same number of messages. – Offsets only have a meaning for a specific partition. – Messages are kept only for a limited time in Kafka (default is one week). – Once the data is written to a partition, it can‘t be changed (immutability). – Data is assigned randomly to a partition unless a key is provided.

**Detailed explanation of each option:**

1. ❌ **A. Ordering of messages is guaranteed across topic partitions.**  
   **Incorrect**.

2. ✅ **B. Once data is written to a partition, it can‘t be changed.**  
   **Correct**.

3. ❌ **C. Offsets have a meaning only for partitions from the same topic.**  
   **Incorrect**.

4. ❌ **D. Different partitions always have the same number of messages when using a round robin distribution.**  
   **Incorrect**.

</details>

## Question 8 (Programming & Serialization):
Which of the following fields is optional in an Avro record? 

- A. name
- B. doc
- C. symbols
- D. fields

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. doc Correct because the doc field in Avro schemas is optional. It is used to provide human‑readable documentation or descriptions of the schema or record fields, but the schema can function perfectly without it. This makes doc the optional field among the listed choices. Incorrect Option A. name Incorrect because name is a required field in Avro records. It defines the name of the record type and is essential for schema definition. Option C. symbols Incorrect because symbols is required for enum types in Avro. It defines the set of valid values for the enum and cannot be omitted. Option D. fields Incorrect because fields is required in Avro records. It specifies the structure of the record, including the names and types of each field. Without fields, the record schema is incomplete.

**Detailed explanation of each option:**

1. ❌ **A. name**  
   **Incorrect**.

2. ✅ **B. doc**  
   **Correct**.

3. ❌ **C. symbols**  
   **Incorrect**.

4. ❌ **D. fields**  
   **Incorrect**.

</details>

## Question 9 (Kafka Producers):
A company uses Kafka for its sales production application and created a producer to map all the orders into a topic with 5 partitions. The goal was to write all messages for a specific customer id ordered into the same partition, but because one customer orders twice as much products as all other customers together, this specific partition gets too large. The company tries to solve this issue and is looking for a way to give this customer its own partition and then use hash partitioning to map the rest of the accounts to other partitions. What‘s the best possible solution to achieve this? 

- A. Adding a unique partition to the ProducerRecord for the specific customer.
- B. Adding another partition and assigning a specific key to this newly created partition.
- C. Producing all messages for the specific customer with another hashing algorithm.
- D. Implementing a custom partitioning strategy.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka messages are key-value pairs and while it is possible to create a ProducerRecord with just a topic and a value, with the key set to null by default, most applications produce records with keys. By default, all messages with the same key will go to the same partition. This means that if a process is reading only a subset of the partitions in a topic, all the records for a single key will be read by the same process. If a key exists and the default partitioner is used, Kafka will hash the key using the “murmur2“ algorithm, and use the result to map the message to a specific partition. However, Kafka does not limit you to just hash partitions, and sometimes there are good reasons to partition data differently. Using a custom partitioner its possible to map one customer to its own partition and then use hash partitioning to map the rest of the accounts to other partitions.

**Detailed explanation of each option:**

1. ❌ **A. Adding a unique partition to the ProducerRecord for the specific customer.**  
   **Incorrect**.

2. ❌ **B. Adding another partition and assigning a specific key to this newly created partition.**  
   **Incorrect**.

3. ❌ **C. Producing all messages for the specific customer with another hashing algorithm.**  
   **Incorrect**.

4. ✅ **D. Implementing a custom partitioning strategy.**  
   **Correct**.

</details>

## Question 10 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for FULL schema evolution? 

- A. Delete fields
- B. Add fields
- C. Add optional fields
- D. Delete optional fields

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

An important aspect of data management is schema evolution. After the initial schema is defined, applications may need to evolve it over time. When this happens, it‘s critical for the downstream consumers to be able to handle data encoded with both the old and the new schema seamlessly. When using Avro or other schema formats, one of the most important things is to manage the schemas and consider how these schemas should evolve. Confluent Schema Registry is built for exactly that purpose. The Confluent Schema Registry default compatibility type is BACKWARD. Allowed changes for FULL compatibility are: – Add optional fields – Delete optional fields FULL compatibility means schemas are both backward and forward compatible. Schemas evolve in a fully compatible way: old data can be read with the new schema, and new data can also be read with the last schema. Further reading: Avro Schema Evolution.

**Detailed explanation of each option:**

1. ❌ **A. Delete fields**  
   **Incorrect**.

2. ❌ **B. Add fields**  
   **Incorrect**.

3. ✅ **C. Add optional fields**  
   **Correct**.

4. ✅ **D. Delete optional fields**  
   **Correct**.

</details>

## Question 11 (Kafka Core Concepts):
Kafka is a distributed system consisting of servers and clients that communicate via a simple high-performance network protocol. Which network protocol is used by Kafka to achieve the high performance? 

- A. SMPT
- B. FTP
- C. UDP
- D. TCP

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D. TCP This is correct because Kafka uses the TCP protocol for communication between brokers and clients. TCP provides reliable, ordered, and error-checked delivery of data streams, which is essential for Kafka’s high-throughput and fault-tolerant messaging system. Its efficiency and reliability make it the backbone of Kafka’s performance. Incorrect Option A. SMPT Incorrect because SMTP (Simple Mail Transfer Protocol) is used for sending emails, not for distributed messaging systems like Kafka. Option B. FTP Incorrect because FTP (File Transfer Protocol) is used for transferring files between systems, not for broker-client communication in Kafka. Option C. UDP Incorrect because UDP (User Datagram Protocol) is lightweight but unreliable. It does not guarantee message delivery or ordering, which Kafka requires for consistency and durability.

**Detailed explanation of each option:**

1. ❌ **A. SMPT**  
   **Incorrect**.

2. ❌ **B. FTP**  
   **Incorrect**.

3. ❌ **C. UDP**  
   **Incorrect**.

4. ✅ **D. TCP**  
   **Correct**.

</details>

## 🚫 Question 12 (Kafka Ecosystem):
Which Confluent solution can be used as an overview dashboard to enable centralized management and monitoring of key components of the platform, including clusters, brokers, schemas, topics, messages, connectors, ksqlDB queries, security, replication and more? 

- A. Confluent Control Center
- B. Confluent Schema Registry
- C. Confluent Health+
- D. Confluent Metrics Reporter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. Confluent Control Center This is correct because Confluent Control Center provides a centralized dashboard for monitoring and managing Kafka clusters and Confluent Platform components. It allows administrators to oversee brokers, topics, connectors, schemas, security, replication, and ksqlDB queries all in one place. It is the dedicated solution for operational visibility and management. Incorrect Option B. Confluent Schema Registry Incorrect because the Schema Registry is specifically used to manage and enforce schemas for Kafka messages (Avro, JSON, ProtoBuf). It does not provide a centralized monitoring dashboard for clusters or other components. Option C. Confluent Health+ Incorrect because Health+ is a cloud-based monitoring and alerting service that provides proactive insights and support. While it helps with reliability, it is not the centralized dashboard for managing all platform components. Option D. Confluent Metrics Reporter Incorrect because the Metrics Reporter is used to export Kafka metrics to external monitoring systems like JMX or third-party tools. It does not provide a full overview dashboard for centralized management.

**Detailed explanation of each option:**

1. ✅ **A. Confluent Control Center**  
   **Correct**.

2. ❌ **B. Confluent Schema Registry**  
   **Incorrect**.

3. ❌ **C. Confluent Health+**  
   **Incorrect**.

4. ❌ **D. Confluent Metrics Reporter**  
   **Incorrect**.

</details>

## Question 13 (Kafka Internals):
A company has a Kafka cluster with 4 brokers. For a new streaming application, the company wants to create a production topic with two partitions that is resilient to one broker failure and one broker maintenance. What replication factor will the company specify while creating the topic? 

- A. A. Replication Factor = 3
- B. B. Replication Factor = 1
- C. C. Replication Factor = 5

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

1. ✅ **A. A. Replication Factor = 3**  
   Correct because with replication factor = 3, each partition will have one leader and two replicas distributed across different brokers. This ensures resilience: If one broker fails, the partition still has two replicas available. If another broker is under maintenance, the partition still maintains quorum with at least two replicas. If one broker fails, the partition still has two replicas available. If another broker is under maintenance, the partition still maintains quorum with at least two replicas. With 4 brokers available, replication factor 3 is the optimal balance between fault tolerance and resource usage.

2. ❌ **B. B. Replication Factor = 1**  
   Incorrect because replication factor 1 means no redundancy. If the broker hosting the leader fails or goes into maintenance, the partition becomes unavailable, violating the resilience requirement.

3. ❌ **C. C. Replication Factor = 5**  
   Incorrect because replication factor cannot exceed the number of brokers in the cluster. With only 4 brokers, replication factor 5 is invalid.

</details>

## Question 14 (Reliable Data Delivery):
Using the configuration “replication.factor=3“, “min.insync.replicas=2“ and “acks=all“, which exception will be thrown if two brokers are down?

- A. Exception: NOT_ENOUGH_REPLICAS.
- B. Exception: TIMEOUT.
- C. Exception: UNKNOWN_SERVER.
- D. Exception: UNKNOWN_TOPIC_OR_PARTITION.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka, producers create and write messages to topic partitions. Consider the following configuration: – replication factor=3: This means there will always be three copies of your data. This replication is performed at the level of topic-partitions. – acks=all: This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting. – min.insync.replicas=2: When a producer sets acks to “all“ (or “-1“), min.insync.replicas specifies that there need to be minimum two replicas that must acknowledge a write for the write to be considered successful. With a replication factor of 3 and two brokers are down, the minimum of in-sync replicas cannot be met. Therefore the producer will raise an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend). Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ✅ **A. Exception: NOT_ENOUGH_REPLICAS.**  
   **Correct**.

2. ❌ **B. Exception: TIMEOUT.**  
   **Incorrect**.

3. ❌ **C. Exception: UNKNOWN_SERVER.**  
   **Incorrect**.

4. ❌ **D. Exception: UNKNOWN_TOPIC_OR_PARTITION.**  
   **Incorrect**.

</details>

## Question 15 (Kafka Connect):
Using Kafka Connect Source to read data from an external database, which processes do the actual work and execute connectors and tasks? 

- A. Transformers
- B. Workers
- C. Brokers
- D. Converters

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. Workers This is correct because Kafka Connect workers are the processes that actually run connectors and tasks. Workers manage the lifecycle of connectors, distribute tasks, and handle the execution of source and sink connectors. They are the backbone of Kafka Connect, ensuring data is ingested from external systems into Kafka. Incorrect Option A. Transformers Incorrect because Single Message Transforms (SMTs) are used to modify messages as they pass through Kafka Connect. They do not execute connectors or tasks; they only apply lightweight transformations. Option C. Brokers Incorrect because Kafka brokers are responsible for storing and serving data in Kafka topics. They do not run connectors or tasks — that is the responsibility of Kafka Connect workers. Option D. Converters Incorrect because Converters handle the serialization and deserialization of data between Kafka Connect and Kafka topics (e.g., JSON, Avro, ProtoBuf). They do not execute connectors or tasks.

**Detailed explanation of each option:**

1. ❌ **A. Transformers**  
   **Incorrect**.

2. ✅ **B. Workers**  
   **Correct**.

3. ❌ **C. Brokers**  
   **Incorrect**.

4. ❌ **D. Converters**  
   **Incorrect**.

</details>

## Question 16 (Kafka Ecosystem):
What‘s one of the five core Kafka APIs? 

- A. Admin API
- B. Javascript API
- C. Python API
- D. Messaging API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

1. ✅ **A. Admin API**  
   Producer API Consumer API Streams API Connector API Admin API

2. ❌ **B. Javascript API**  
   **Incorrect**.

3. ❌ **C. Python API**  
   **Incorrect**.

4. ❌ **D. Messaging API**  
   **Incorrect**.

</details>

## Question 17 (Kafka Producers):
Which of the following options is a producer sender metric? 

- A. bytes-consumed-rate
- B. records-lag-max
- C. commit-latency-avg
- D. batch-size-avg

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The only producer sender metric is the batch-size-avg. It‘s the average number of bytes sent per partition per-request. All other metrics are consumer metrics: – commit-latency-avg: The average time taken for a commit request. – bytes-consumed-rate: The average number of bytes consumed per second. – records-lag-max: The maximum lag in terms of number of records for any partition in this window.

**Detailed explanation of each option:**

1. ❌ **A. bytes-consumed-rate**  
   **Incorrect**.

2. ❌ **B. records-lag-max**  
   **Incorrect**.

3. ❌ **C. commit-latency-avg**  
   **Incorrect**.

4. ✅ **D. batch-size-avg**  
   **Correct**.

</details>

## Question 18 (Kafka Internals):
Which of the following options is the default cleanup policy for all user topics? 

- A. log.cleanup.policy=compact
- B. log.cleanup.policy=max-size
- C. log.cleanup.policy=none
- D. log.cleanup.policy=delete

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, unlike other messaging systems, the messages on a topic are not immediately removed after they are consumed. Instead, the configuration of each topic determines how much space the topic is permitted and how it is managed. Concept of making data expire is called as Cleanup. It‘s a broker level configuration. It is important to restrict log segment to continue grow in size. Options for the cleanup policy are either “delete“ or “compact“ or both. The string designates the retention policy to use on old log segments. The default policy (“delete“) will discard old segments when their retention time or size limit has been reached. The “compact“ setting will enable log compaction on the topic.

**Detailed explanation of each option:**

1. ❌ **A. log.cleanup.policy=compact**  
   **Incorrect**.

2. ❌ **B. log.cleanup.policy=max-size**  
   **Incorrect**.

3. ❌ **C. log.cleanup.policy=none**  
   **Incorrect**.

4. ✅ **D. log.cleanup.policy=delete**  
   **Correct**.

</details>

## Question 19 (Kafka Setup and Operations):
Which Java versions are supported by Kafka? 

- A. Java 11
- B. Java 16
- C. Java 8
- D. Java 5

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Option A. Java 11 This is correct because Kafka supports Java 11 as one of its long-term support (LTS) versions. It is widely used in production environments and officially supported for running Kafka brokers and clients. Option C. Java 8 This is correct because Kafka continues to support Java 8, another LTS version. Many legacy systems still rely on Java 8, and Kafka maintains compatibility with it. Incorrect Option B. Java 16 Incorrect because Kafka does not officially support Java 16. It was a short-term release and not intended for long-term production use. Kafka focuses on LTS versions like Java 8 and 11. Option D. Java 5 Incorrect because Java 5 is far too old and unsupported. Kafka requires modern JVM features that are not available in Java 5.

**Detailed explanation of each option:**

1. ✅ **A. Java 11**  
   **Correct**.

2. ❌ **B. Java 16**  
   **Incorrect**.

3. ✅ **C. Java 8**  
   **Correct**.

4. ❌ **D. Java 5**  
   **Incorrect**.

</details>

## Question 20 (Kafka Setup and Operations):
Under the hood, which process is used by Kafka brokers that handles the deletion of unused objects or some objects that are inaccessible to free up memory resources to tune the overall performance? 

- A. Data Compression
- B. Message Batching
- C. Garbage Collection
- D. Zookeeper Cleaning

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Garbage Collection This is correct because Kafka brokers run on the JVM, and Garbage Collection (GC) is the process that automatically reclaims memory by deleting unused or inaccessible objects. This helps optimize memory usage and overall broker performance. Incorrect Option A. Data Compression Incorrect because data compression reduces the size of messages stored or transmitted, but it does not handle memory cleanup of unused objects. Option B. Message Batching Incorrect because message batching improves throughput by grouping multiple messages together before sending, but it does not manage memory reclamation. Option D. Zookeeper Cleaning Incorrect because ZooKeeper is used for metadata management and coordination in Kafka (though newer versions use KRaft instead). It does not perform memory cleanup for Kafka brokers.

**Detailed explanation of each option:**

1. ❌ **A. Data Compression**  
   **Incorrect**.

2. ❌ **B. Message Batching**  
   **Incorrect**.

3. ✅ **C. Garbage Collection**  
   **Correct**.

4. ❌ **D. Zookeeper Cleaning**  
   **Incorrect**.

</details>

## Question 21 (Kafka Consumers):
A company uses a production consumer application with a large number of consumers. Even for lower activity hours of the day the consumers are using a lot of CPU when fetching messages. Increasing which consumer property is a good choice to possibly reduce the load on both the consumer and the broker? 

- A. session.timeout.ms
- B. auto.offset.reset
- C. fetch.min.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Most of the consumer parameters have reasonable defaults and do not require modification, but some have implications on the performance and availability of the consumers: fetch.min.bytes: The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request. The default setting of 1 byte means that fetch requests are answered as soon as a single byte of data is available or the fetch request times out waiting for data to arrive. Setting this to something greater than 1 will cause the server to wait for larger amounts of data to accumulate which can improve server throughput a bit at the cost of some additional latency. Setting fetch.min.bytes to a higher number reduces the load on both the consumer and the broker as they have to handle fewer back-and-forth messages in cases where the topics don‘t have much new activity (or for lower activity hours of the day). You will want to set this parameter higher than the default also if the consumer is using too much CPU when there isn‘t much data available, or reduce load on the brokers when you have large number of consumers. Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. session.timeout.ms**  
   **Incorrect**.

2. ❌ **B. auto.offset.reset**  
   **Incorrect**.

3. ✅ **C. fetch.min.bytes**  
   **Correct**.

</details>

## 🚫 Question 22 (Kafka Setup and Operations):
Running Kafka in production, how much memory should a machine at least have as a decent choice for storing and caching messages? 

- A. 64 GB
- B. 8 GB
- C. 32 GB
- D. 16 GB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka relies heavily on the filesystem for storing and caching messages. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel‘s pagecache. A machine with 64 GB of RAM is a decent choice, but 32 GB machines are not uncommon. Less than 32 GB tends to be counterproductive (you end up needing many, many small machines). Further reading: Production Deployment.

**Detailed explanation of each option:**

1. ❌ **A. 64 GB**  
   **Incorrect**.

2. ❌ **B. 8 GB**  
   **Incorrect**.

3. ✅ **C. 32 GB**  
   **Correct**.

4. ❌ **D. 16 GB**  
   **Incorrect**.

</details>

## Question 23 (Kafka Consumers):
In a consumer group application, what internal consumer mechanism can be used to detect the application being down? 

- A. Poll thread
- B. Offset thread
- C. Push thread
- D. Heartbeat thread

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Consumers in a group talk to a consumer group coordinator. To detect consumers that have processing issues or are down, there is a poll and a heartbeat mechanism: – Heartbeat thread: Heartbeats are sent periodically to the broker. If no heartbeat is sent during that period, the consumer is considered dead. – Poll thread: This is particularly relevant for Big Data frameworks like Spark in case the processing takes a lot of time. This mechanism detects data processing issues.

**Detailed explanation of each option:**

1. ❌ **A. Poll thread**  
   **Incorrect**.

2. ❌ **B. Offset thread**  
   **Incorrect**.

3. ❌ **C. Push thread**  
   **Incorrect**.

4. ✅ **D. Heartbeat thread**  
   **Correct**.

</details>

## Question 24 (Kafka Setup and Operations):
Which broker property needs to be used to specify that a broker belongs to a particular rack? 

- A. broker.zone
- B. availability.rack
- C. broker.rack
- D. availability.zone

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The rack awareness feature spreads replicas of the same partition across different racks. This extends the guarantees Kafka provides for broker-failure to cover rack-failure, limiting the risk of data loss should all the brokers on a rack fail at once. The feature can also be applied to other broker groupings such as availability zones in EC2 (Amazon Web Services concept). You can specify that a broker belongs to a particular rack by adding a property to the broker config: broker.rack=my-rack-id Further reading: Kafka Racks.

**Detailed explanation of each option:**

1. ❌ **A. broker.zone**  
   **Incorrect**.

2. ❌ **B. availability.rack**  
   **Incorrect**.

3. ✅ **C. broker.rack**  
   **Correct**.

4. ❌ **D. availability.zone**  
   **Incorrect**.

</details>

## Question 25 (Kafka Setup and Operations):
After creating a Kafka topic, which script helps you to check whether the topic you created is available?

- A. bin/kafka-console-producer.sh
- B. bin/kafka-console-consumer.sh
- C. bin/kafka-configs.sh
- D. bin/kafka-topics.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, events are organized and stored in topics.The bin/kafka-topics.sh script can be used to create, delete, describe, list or change a topic.To list all available topics you can use the following command:bin/kafka-topics.sh –bootstrap-sever localhost:9092 –list

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-console-producer.sh**  
   **Incorrect**.

2. ❌ **B. bin/kafka-console-consumer.sh**  
   **Incorrect**.

3. ❌ **C. bin/kafka-configs.sh**  
   **Incorrect**.

4. ✅ **D. bin/kafka-topics.sh**  
   **Correct**.

</details>

## Question 26 (Kafka Setup and Operations):
A company created a production topic named prod_topic. The retention period for prod_topic should be 10 days. How could you accomplish this in the most efficient way? 

- A. Set the broker configuration retention.ms=864000000.
- B. Set the topic configuration retention.days=10.
- C. Set the broker configuration retention.days=10.
- D. Set the topic configuration retention.ms=864000000.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The property retention.ms can be configured at topic level while creating topics or by altering topics. It shouldn‘t be set at the broker level (log.retention.ms) as this would impact all the topics in the cluster, not just the one we are interested in. The retention.ms configuration controls the maximum time in milliseconds we will retain a log before we will discard old log segments to free up space if we are using the “delete“ retention policy. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied. The default value is 604800000 (7 days).

**Detailed explanation of each option:**

1. ❌ **A. Set the broker configuration retention.ms=864000000.**  
   **Incorrect**.

2. ❌ **B. Set the topic configuration retention.days=10.**  
   **Incorrect**.

3. ❌ **C. Set the broker configuration retention.days=10.**  
   **Incorrect**.

4. ✅ **D. Set the topic configuration retention.ms=864000000.**  
   **Correct**.

</details>

## 🚫 Question 27 (Kafka Ecosystem):
What are the main benefits of using ksqlDB together with Kafka? 

- A. ksqlDB allows you to query, read, write, and process data in Kafka in real-time and at scale using intuitive SQL-like syntax.
- B. ksqlDB just requires a Python runtime environment and you are ready to operate your Kafka cluster at real-time and at scale using intuitive SQL-like syntax.
- C. ksqlDB allows you to use SQL-like syntax to setup your Kafka cluster.
- D. ksqlDB does not require proficiency with a programming language such as Java or Scala, and you don‘t have to install a separate processing cluster technology.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

Option A. ksqlDB allows you to query, read, write, and process data in Kafka in real time and at scale using intuitive SQL-like syntax. ksqlDB enables stream processing directly on Kafka data using SQL-like statements. Developers can create streams and tables, filter and transform events, join streams, and run continuous queries without writing extensive application code. Option D. ksqlDB does not require proficiency with a programming language such as Java or Scala, and you don’t have to install a separate processing cluster technology. ksqlDB simplifies stream processing by providing a SQL-like interface instead of requiring developers to build stream-processing applications using Java or Scala. It runs as a service that integrates with Kafka, avoiding the need to deploy a separate stream-processing framework such as Apache Flink for these workloads. Incorrect: Option B. ksqlDB just requires a Python runtime environment and you are ready to operate your Kafka cluster at real time and at scale using intuitive SQL-like syntax. ksqlDB is not simply a Python runtime or a tool for operating a Kafka cluster. It is a stream-processing database that runs as a service and uses Kafka for event streaming. It does not require Python as its defining runtime dependency. Option C. ksqlDB allows you to use SQL-like syntax to set up your Kafka cluster. ksqlDB is used to query and process data in Kafka, not to provision or configure the Kafka cluster itself. Kafka cluster setup and administration are separate tasks.

**Detailed explanation of each option:**

1. ✅ **A. ksqlDB allows you to query, read, write, and process data in Kafka in real-time and at scale using intuitive SQL-like syntax.**  
   **Correct**.

2. ❌ **B. ksqlDB just requires a Python runtime environment and you are ready to operate your Kafka cluster at real-time and at scale using intuitive SQL-like syntax.**  
   **Incorrect**.

3. ❌ **C. ksqlDB allows you to use SQL-like syntax to setup your Kafka cluster.**  
   **Incorrect**.

4. ✅ **D. ksqlDB does not require proficiency with a programming language such as Java or Scala, and you don‘t have to install a separate processing cluster technology.**  
   **Correct**.

</details>

## Question 28 (Kafka Setup and Operations):
If you are setting up a multi-broker cluster in Kafka on different machines, which broker property needs to be unique for each node?

- A. broker.id
- B. log.dir
- C. all of the other options need to be unique for each node
- D. port

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

For Kafka, a single broker is just a cluster of size one, so nothing much changes other than starting a few more broker instances if you want to set up a multi-broker cluster. Only the broker.id property needs to be unique and permanent for each node in the cluster. Note: If you run multiple brokers on the same machine you should definitely override the port and log directory as well, because you want to keep the brokers from all trying to register on the same port or overwrite each others data. Further reading: Kafka Quickstart.

**Detailed explanation of each option:**

1. ✅ **A. broker.id**  
   **Correct**.

2. ❌ **B. log.dir**  
   **Incorrect**.

3. ❌ **C. all of the other options need to be unique for each node**  
   **Incorrect**.

4. ❌ **D. port**  
   **Incorrect**.

</details>

## Question 29 (Kafka Internals):
Which Kafka broker is responsible for partition leader election? 

- A. Partition leader
- B. Zookeeper node
- C. In-sync replica
- D. Controller

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In a Kafka cluster, one (and only one) of the brokers serves as the controller, which is responsible for managing the states of partitions and replicas and for performing administrative tasks like reassigning partitions. The election of that broker happens thanks to Zookeeper. Kafka Controller registers handlers to be notified about changes in Zookeeper and propagate them across brokers in a Kafka cluster. Further reading: Controller Internals.

**Detailed explanation of each option:**

1. ❌ **A. Partition leader**  
   **Incorrect**.

2. ❌ **B. Zookeeper node**  
   **Incorrect**.

3. ❌ **C. In-sync replica**  
   **Incorrect**.

4. ✅ **D. Controller**  
   **Correct**.

</details>

## Question 30 (Kafka Consumers):
Which offset commit strategy should be used in an at-most once consuming scenario? 

- A. Do not commit the offsets in Kafka, as this will be handled automatically.
- B. Commit the offsets in Kafka, after processing the data.
- C. Commit the offsets in Kafka, during processing the data.
- D. Commit the offsets in Kafka, before processing the data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D. Commit the offsets in Kafka, before processing the data. This is correct because in an at-most once scenario, the consumer commits the offset before processing the message. This ensures that even if the consumer crashes during processing, the message will not be reprocessed. The trade-off is that some data may be lost, but duplicates are avoided — which aligns with the definition of at-most once delivery semantics. Incorrect Option A. Do not commit the offsets in Kafka, as this will be handled automatically. Incorrect because offsets are not automatically committed unless auto-commit is enabled, and even then, it does not guarantee at-most once semantics. Explicit control is required to ensure the desired behavior. Option B. Commit the offsets in Kafka, after processing the data. Incorrect because committing after processing ensures at-least once semantics. If the consumer crashes after processing but before committing, the same message may be reprocessed, violating at-most once guarantees. Option C. Commit the offsets in Kafka, during processing the data. Incorrect because committing during processing is not a valid or reliable strategy. Offsets must be committed either before or after processing, not in the middle, as this introduces inconsistency and does not align with Kafka’s offset management model.

**Detailed explanation of each option:**

1. ❌ **A. Do not commit the offsets in Kafka, as this will be handled automatically.**  
   **Incorrect**.

2. ❌ **B. Commit the offsets in Kafka, after processing the data.**  
   **Incorrect**.

3. ❌ **C. Commit the offsets in Kafka, during processing the data.**  
   **Incorrect**.

4. ✅ **D. Commit the offsets in Kafka, before processing the data.**  
   **Correct**.

</details>

## Question 31 (Kafka Consumers):
Which of the following options are true for Kafka consumers? 

- A. Consumers read data in order within each topic partition.
- B. Consumer offsets are stored in Zookeeper.
- C. Consumers can read data from more than one partition.
- D. If you have more consumers than partitions, some consumers will read data from the same partition.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Option A. Consumers read data in order within each topic partition. Kafka guarantees message ordering within a single partition. A consumer reads records in partition order, based on their offsets. However, Kafka does not guarantee a total ordering across multiple partitions. Option C. Consumers can read data from more than one partition. A Kafka consumer can subscribe to a topic with multiple partitions and consume records from each assigned partition. Within a consumer group, partitions are assigned among consumers, allowing processing to scale horizontally. Incorrect: Option B. Consumer offsets are stored in ZooKeeper. In modern Kafka, consumer group offsets are stored in the internal Kafka topic __consumer_offsets, not ZooKeeper. Older Kafka versions used ZooKeeper for some consumer-offset management, but this is not the standard approach today. Option D. If you have more consumers than partitions, some consumers will read data from the same partition. Within a consumer group, each partition is assigned to at most one consumer at a time. If the group has more consumers than partitions, some consumers will remain idle rather than sharing a partition. Consumers in different groups can independently read the same partition.

**Detailed explanation of each option:**

1. ✅ **A. Consumers read data in order within each topic partition.**  
   **Correct**.

2. ❌ **B. Consumer offsets are stored in Zookeeper.**  
   **Incorrect**.

3. ✅ **C. Consumers can read data from more than one partition.**  
   **Correct**.

4. ❌ **D. If you have more consumers than partitions, some consumers will read data from the same partition.**  
   **Incorrect**.

</details>

## Question 32 (Programming & Serialization):
A producer application is using KafkaAvroSerializer to send messages of Avro type to Kafka. What happens if the schema is not present in the local cache for schemas? 

- A. The producer registers the schema to the Schema Registry.
- B. The Kafka broker throws an exception.
- C. The producer throws a warning but creates the schema.
- D. The schema gets fetched from the Schema Registry.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

1. ✅ **A. The producer registers the schema to the Schema Registry.**  
   Correct because when using KafkaAvroSerializer, if the schema is not found in the local cache, the producer will register the schema with the Schema Registry before sending the message. This ensures that the schema is available for consumers to deserialize messages consistently. The schema ID is then cached locally for subsequent messages, avoiding repeated registration.

2. ❌ **B. The Kafka broker throws an exception.**  
   Incorrect because the broker does not handle schema registration. Schema management is handled by the Schema Registry, not the Kafka broker.

3. ❌ **C. The producer throws a warning but creates the schema.**  
   Incorrect because the producer does not “create” schemas. It registers schemas with the Schema Registry; warnings alone are not the mechanism for schema handling.

4. ❌ **D. The schema gets fetched from the Schema Registry.**  
   Incorrect because fetching occurs on the consumer side when deserializing messages. On the producer side, if the schema is missing in the cache, it is registered, not fetched.

</details>

## Question 33 (Stream Processing):
What‘s the most appropriate way of modeling a retail store‘s data in Kafka Streams? 

- A. Sales of products as stream, orders placed for new products as stream, shipments of products that arrive as stream, customer as table.
- B. Sales of products as table, orders placed for new products as table, shipments of products that arrive as table, customer as stream.
- C. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka is an event streaming platform. Conceptually, an event has a key, value, and timestamp. Events are captured into event streams. An event stream records the history of what has happened in the world as a sequence of events. Compared to an event stream, a table represents the state of the world at a particular point in time, typically now. A table is a view of an event stream, and this view is continuously being updated whenever a new event is captured. – A stream provides immutable data. It supports only inserting (appending) new events, whereas existing events cannot be changed. Streams are persistent, durable, and fault tolerant. Events in a stream can be keyed, and you can have many events for one key. – A table provides mutable data. New events – rows – can be inserted, and existing rows can be updated and deleted. Here, an event‘s key aka row key identifies which row is being mutated. Like streams, tables are persistent, durable, and fault tolerant. The core streams in retail are sales of products, orders placed for new products, and shipments of products that arrive. The core tables in retail are customer data and the “inventory on hand“, which is computed off the sale and shipment streams which add and subtract from our stock of products on hand. Further reading: Streams and Tables in Kafka.

**Detailed explanation of each option:**

1. ✅ **A. Sales of products as stream, orders placed for new products as stream, shipments of products that arrive as stream, customer as table.**  
   **Correct**.

2. ❌ **B. Sales of products as table, orders placed for new products as table, shipments of products that arrive as table, customer as stream.**  
   **Incorrect**.

3. ❌ **C. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.**  
   **Incorrect**.

</details>

## Question 34 (Kafka Setup and Operations):
How does Garbage Collection help to improve Kafka‘s overall performance? 

- A. Garbage collection is a JVM process that removes old message keys but ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition.
- B. Garbage collection is a JVM process that automatically shuts down out of sync brokers.
- C. Garbage collection is a JVM process that automatically consumes messages to increase the fetch rate.
- D. Garbage collection is a JVM process that automatically frees up memory and removes unused pointers to objects.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Java Garbage Collection is the process by which Java programs perform automatic memory management. Java programs compile to bytecode that can be run on a Java Virtual Machine, or JVM for short. When Java programs run on the JVM, objects are created on the heap, which is a portion of memory dedicated to the program. Eventually, some objects will no longer be needed. The garbage collector finds these unused objects and deletes them to free up memory. Further reading: Java Garbage Collection.

**Detailed explanation of each option:**

1. ❌ **A. Garbage collection is a JVM process that removes old message keys but ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition.**  
   **Incorrect**.

2. ❌ **B. Garbage collection is a JVM process that automatically shuts down out of sync brokers.**  
   **Incorrect**.

3. ❌ **C. Garbage collection is a JVM process that automatically consumes messages to increase the fetch rate.**  
   **Incorrect**.

4. ✅ **D. Garbage collection is a JVM process that automatically frees up memory and removes unused pointers to objects.**  
   **Correct**.

</details>

## 🚫 Question 35 (Kafka Ecosystem):
Which of the following options can be used to interact with the ksqlDB servers through a REST API in the interactive deployment mode?

- A. ksqlDB CLI
- B. Favorite REST client
- C. Confluent Control Center
- D. Kafka Streams API

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Option A. ksqlDB CLI The ksqlDB CLI provides an interactive command-line interface for executing ksqlDB statements. It communicates with the ksqlDB server through its REST API, allowing users to create streams and tables, run queries, and manage ksqlDB applications. Option B. Favorite REST client A REST client can interact directly with the ksqlDB server’s REST API. Tools such as Postman or curl can send HTTP requests to execute statements, manage queries, and retrieve information from the server. Option C. Confluent Control Center Confluent Control Center provides a graphical interface for managing and monitoring Kafka and ksqlDB deployments. Where supported and configured, it can interact with ksqlDB through the server’s REST API. Incorrect: Option D. Kafka Streams API The Kafka Streams API is a Java library for developing stream-processing applications that consume from and produce to Kafka topics. It is not a REST client for interacting directly with ksqlDB servers.

**Detailed explanation of each option:**

1. ✅ **A. ksqlDB CLI**  
   **Correct**.

2. ✅ **B. Favorite REST client**  
   **Correct**.

3. ✅ **C. Confluent Control Center**  
   **Correct**.

4. ❌ **D. Kafka Streams API**  
   **Incorrect**.

</details>

## Question 36 (Stream Processing):
Which of the following options best describes the difference between stateless and stateful operations?

- A. Stateless transformations require a state store while stateful transformations do not require a state store.
- B. Stateless transformations do not require state for processing while stateful transformations depend on state for processing inputs.
- C. Stateful transformations do not require state for processing while stateless transformations depend on state for processing inputs.
- D. Stateless transformations always lead into KStreams while stateful transformations lead into KTables.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The KStream and KTable interfaces support a variety of transformation operations. The available transformations can be either stateful or stateless:– Stateless transformations do not require state for processing and they do not require a state store associated with the stream processor, for example filtering.– Stateful transformations depend on state for processing inputs and producing outputs and require a state store associated with the stream processor. For example, in aggregating operations, a windowing state store is used to collect the latest aggregation results per window. In join operations, a windowing state store is used to collect all of the records received so far within the defined window boundary.

**Detailed explanation of each option:**

1. ❌ **A. Stateless transformations require a state store while stateful transformations do not require a state store.**  
   **Incorrect**.

2. ✅ **B. Stateless transformations do not require state for processing while stateful transformations depend on state for processing inputs.**  
   **Correct**.

3. ❌ **C. Stateful transformations do not require state for processing while stateless transformations depend on state for processing inputs.**  
   **Incorrect**.

4. ❌ **D. Stateless transformations always lead into KStreams while stateful transformations lead into KTables.**  
   **Incorrect**.

</details>

## Question 37 (Kafka Consumers):
A company built a consumer application to automatically commit offsets of processed messages. What happens if the committed offset is larger than the offset of the last message the client actually processed? 

- A. The consumer application throws a runtime error because it does not know where to start processing messages.
- B. All messages between the last processed offset and the committed offset will be processed twice by the consumer group.
- C. All messages between the last processed offset and the committed offset will be missed by the consumer group.
- D. You need to set the property “enable.auto.commit“ to true in order to process all messages between the last processed offset and the committed offset.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

As a consumer in the group reads messages from the partitions assigned by the coordinator, it must commit the offsets corresponding to the messages it has read. If the consumer crashes or is shut down, its partitions will be re-assigned to another member, which will begin consumption from the last committed offset of each partition. By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. – If the committed offset is smaller than the offset of the last message the client processed, the messages between the last processed offset and the committed offset will be processed twice. – If the committed offset is larger than the offset of the last message the client actually processed, all messages between the last processed offset and the committed offset will be missed by the consumer group. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. The consumer application throws a runtime error because it does not know where to start processing messages.**  
   **Incorrect**.

2. ❌ **B. All messages between the last processed offset and the committed offset will be processed twice by the consumer group.**  
   **Incorrect**.

3. ✅ **C. All messages between the last processed offset and the committed offset will be missed by the consumer group.**  
   **Correct**.

4. ❌ **D. You need to set the property “enable.auto.commit“ to true in order to process all messages between the last processed offset and the committed offset.**  
   **Incorrect**.

</details>

## Question 38 (Stream Processing):
What‘s a benefit of using a GlobalKTable when joining input data?

- A. Input data does not need to be co-partitioned.
- B. Joins against a GlobalKTable are always windowed and therefore more efficient.
- C. Input topics of the join automatically have the same number of partitions.
- D. Decreased local storage consumption compared to the KTable because not the entire topic is tracked.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Like a KTable, a GlobalKTable is an abstraction of a changelog stream, where each data record represents an update. A GlobalKTable differs from a KTable in the data that they are being populated with, i. e. which data from the underlying Kafka topic is being read into the respective table. If you read the input topic into a GlobalKTable, then the local GlobalKTable instance of each application instance will be populated with data from all partitions of the topic (when using a KTable you only read data from one partition). More convenient and / or efficient joins are the main benefit of this concept. Also, when joining against a global table, the input data does not need to be co-partitioned. GlobalKTables can also be used to “broadcast“ information to all the running instances of your application. The downsides of global tables are the increased local storage consumption and the increased network and Kafka broker load because the entire topic is read. Further reading: GlobalKTable Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Input data does not need to be co-partitioned.**  
   **Correct**.

2. ❌ **B. Joins against a GlobalKTable are always windowed and therefore more efficient.**  
   **Incorrect**.

3. ❌ **C. Input topics of the join automatically have the same number of partitions.**  
   **Incorrect**.

4. ❌ **D. Decreased local storage consumption compared to the KTable because not the entire topic is tracked.**  
   **Incorrect**.

</details>

## 🚫 Question 39 (Kafka Setup and Operations):
Running Kafka in production, what‘s a proper value for setting the java heap size?

- A. 6 MB
- B. 6 KB
- C. 6 TB
- D. 6 GB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka relies heavily on the filesystem for storing and caching messages. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel‘s page cache.In most cases, Kafka can run optimally with 6 GB of RAM for heap space. For especially heavy production loads, use machines with 32 GB or more. Extra RAM will be used to bolster OS page cache and improve client throughput. While Kafka can run with less RAM, its ability to handle load is hampered when less memory is available.

**Detailed explanation of each option:**

1. ❌ **A. 6 MB**  
   **Incorrect**.

2. ❌ **B. 6 KB**  
   **Incorrect**.

3. ❌ **C. 6 TB**  
   **Incorrect**.

4. ✅ **D. 6 GB**  
   **Correct**.

</details>

## Question 40 (Programming & Serialization):
Which of the following message schema formats are supported out-of-the-box with Confluent Platform, with serializers, deserializers, and command line tools available for each format?

- A. JSON
- B. Avro
- C. ProtoBuf
- D. Bytes

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Option A. JSON This is correct because Confluent Platform provides built-in support for JSON Schema. It includes serializers, deserializers, and CLI tools to register and validate schemas in Schema Registry. Option B. Avro This is correct because Avro is the most widely used schema format in Kafka and Confluent. It has full support with serializers, deserializers, and command line tools, making it a standard choice for schema evolution and compatibility checks. Option C. ProtoBuf This is correct because Confluent also supports Protocol Buffers (ProtoBuf) out-of-the-box. It provides serializers, deserializers, and Schema Registry integration, enabling efficient binary serialization with schema evolution capabilities. Incorrect Option D. Bytes Incorrect because while Kafka can handle raw byte arrays, Confluent Platform does not provide schema support, serializers, deserializers, or CLI tools for Bytes in the same way it does for Avro, JSON, and ProtoBuf. Bytes are schema-less and therefore not part of the supported schema formats with tooling.

**Detailed explanation of each option:**

1. ✅ **A. JSON**  
   **Correct**.

2. ✅ **B. Avro**  
   **Correct**.

3. ✅ **C. ProtoBuf**  
   **Correct**.

4. ❌ **D. Bytes**  
   **Incorrect**.

</details>

## Question 41 (Kafka Setup and Operations):
A company wants to mirror its production topic from the Europe region to 4 different regions worldwide. The environment should be highly available in every region and it should be possible to produce to the topic from everywhere. Using Mirror Maker, what kind of mirroring is this? 

- A. Aggregation
- B. Active -> Passive
- C. Active -> Active
- D. Forwarding

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

With MirrorMaker, Kafka administrators can replicate topics, topic configurations, consumer groups, and ACLs from one or more source Kafka clusters to one or more target Kafka clusters, i. e., across cluster environments. Multi-datacenter deployments enable use-cases such as: – Active -> Active geo-localized deployments: allows users to access a near-by data center to optimize their architecture for low latency and high performance. Replication can be done in both sides and data can be produced and consumed in every cluster. – Active-> Passive disaster recover (DR) deployments: in an event of a partial or complete datacenter disaster, allow failing over applications to use Confluent Platform in a different datacenter. – Active -> Passive centralized analytics: Aggregate data from multiple Apache Kafka clusters into one location for organization-wide analytics. No producers will be used at the replicated cluster, it‘s just for consuming data for analytic purposes. – Aggregation (e. g., from many clusters to one): A->K, B->K, C->K. – Fan-out (e. g., from one to many clusters): K->A, K->B, K->C. – Forwarding: A->B, B->C, C->D. Further reading: Cluster Replication Flows.

**Detailed explanation of each option:**

1. ❌ **A. Aggregation**  
   **Incorrect**.

2. ❌ **B. Active -> Passive**  
   **Incorrect**.

3. ✅ **C. Active -> Active**  
   **Correct**.

4. ❌ **D. Forwarding**  
   **Incorrect**.

</details>

## Question 42 (Kafka Producers):
In Kafka, what are the most important producer configurations?

- A. batch size
- B. compression
- C. replication factor
- D. acks

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

The most important producer configurations are: – acks: The number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. – compression: The compression type for all data generated by the producer. The default is none (i. e. no compression). – batch size: The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. Further reading: Kafka Producer Configs.

**Detailed explanation of each option:**

1. ✅ **A. batch size**  
   **Correct**.

2. ✅ **B. compression**  
   **Correct**.

3. ❌ **C. replication factor**  
   **Incorrect**.

4. ✅ **D. acks**  
   **Correct**.

</details>

## Question 43 (Kafka Producers):
Due to network errors a producer can introduce duplicate messages in Kafka, for example, if a message is processed, but the acknowledgment never reaches the producer. Which producer configuration can be used to guarantee a stable and safe pipeline without processing duplicate messages? 

- A. max.in.flight.requests=1
- B. enable.idempotence=true
- C. retries=Integer.MAX_VALUE
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

When a producer sends messages to a topic, things can go wrong, such as short connection failures. When this happens, any messages that are pending acknowledgements can either be resent or discarded. The messages may have been successfully written to the topic, or not, there is no way to know. If we resend then we may duplicate the message, but if we dont resend then the message may essentially be lost. The idempotent producer feature addresses these issues ensuring that messages always get delivered, in the right order and without duplicates. All you need to do to turn this feature on is use the producer configuration “enable.idempotence=true“. Further reading: Idempotent Producer Configuration.

**Detailed explanation of each option:**

1. ❌ **A. max.in.flight.requests=1**  
   **Incorrect**.

2. ✅ **B. enable.idempotence=true**  
   **Correct**.

3. ❌ **C. retries=Integer.MAX_VALUE**  
   **Incorrect**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## Question 44 (Kafka Consumers):
Which of the following property should be configured to aim for a high throughput consumer application? 

- A. group.id
- B. fetch.min.bytes
- C. heartbeat.interval.ms
- D. fetch.max.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A way to optimize for consumer throughput is to adjust how much data consumers receive from each fetch from the leader broker. You can increase how much data the consumers get from the leader for each fetch request by increasing the configuration parameter fetch.min.bytes. This parameter sets the minimum number of bytes expected for a fetch response from a consumer. Increasing this also reduces the number of fetch requests made, reducing the broker CPU overhead to process each fetch, thereby also improving throughput. Assuming the application allows it, use also consumer groups with multiple consumers to parallelize consumption. Parallelizing consumption may improve throughput because multiple consumers can balance the load, processing multiple partitions simultaneously. Further reading: Optimizing for Throughput.

**Detailed explanation of each option:**

1. ❌ **A. group.id**  
   **Incorrect**.

2. ✅ **B. fetch.min.bytes**  
   **Correct**.

3. ❌ **C. heartbeat.interval.ms**  
   **Incorrect**.

4. ❌ **D. fetch.max.bytes**  
   **Incorrect**.

</details>

## Question 45 (Kafka Consumers):
What happens for a consumer application when closing one of the consumers cleanly? 

- A. The consumer application will consume messages with one consumer less.
- B. The consumer application breaks with the exception NOT_ENOUGH_CONSUMERS.
- C. The Kafka broker will notify the group coordinator that one consumer is leaving, and the group coordinator will trigger a rebalance immediately.
- D. The consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The way consumers maintain membership in a consumer group and ownership of the partitions assigned to them is by sending heartbeats to a Kafka broker designated as the group coordinator (this broker can be different for different consumer groups). As long as the consumer is sending heartbeats at regular intervals, it is assumed to be alive, well, and processing messages from its partitions. Heartbeats are sent when the consumer polls (i. e., retrieves records) and when it commits records it has consumed. When closing a consumer cleanly, the consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately, reducing the gap in processing.

**Detailed explanation of each option:**

1. ❌ **A. The consumer application will consume messages with one consumer less.**  
   **Incorrect**.

2. ❌ **B. The consumer application breaks with the exception NOT_ENOUGH_CONSUMERS.**  
   **Incorrect**.

3. ❌ **C. The Kafka broker will notify the group coordinator that one consumer is leaving, and the group coordinator will trigger a rebalance immediately.**  
   **Incorrect**.

4. ✅ **D. The consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately.**  
   **Correct**.

</details>

## Question 46 (Kafka Producers):
Which of the following properties are mandatory for creating a Kafka producer?

- A. bootstrap.servers
- B. key.serializer
- C. compression.type
- D. value.serializer

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

The first step in writing messages to Kafka is to create a producer object with the properties you want to pass to the producer. A Kafka producer has three mandatory properties: – bootstrap.servers: A list of host / port pairs to use for establishing the initial connection to the Kafka cluster. The client will make use of all servers irrespective of which servers are specified here for bootstrapping – this list only impacts the initial hosts used to discover the full set of servers. This list should be in the form host1:port1,host2:port2,…. Since these servers are just used for the initial connection to discover the full cluster membership (which may change dynamically), this list need not contain the full set of servers (you may want more than one, though, in case a server is down). – key.serializer: Name of a class that will be used to serialize the keys of the records we will produce to Kafka. Kafka brokers expect byte arrays as keys and values of messages. However, the producer interface allows, using parameterized types, any Java object to be sent as a key and value. This makes for very readable code, but it also means that the producer has to know how to convert these objects to byte arrays. – value.serializer: Name of a class that will be used to serialize the values of the records we will produce to Kafka. The same way you set key.serializer to a name of a class that will serialize the message key object to a byte array, you set value.serializer to a class that will serialize the message value object. Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ✅ **A. bootstrap.servers**  
   **Correct**.

2. ✅ **B. key.serializer**  
   **Correct**.

3. ❌ **C. compression.type**  
   **Incorrect**.

4. ✅ **D. value.serializer**  
   **Correct**.

</details>

## Question 47 (Kafka Consumers):
In a consumer group application, what internal consumer mechanism can be used to detect a data processing issue? 

- A. Poll thread
- B. Push thread
- C. Heartbeat thread
- D. Offset thread

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Consumers in a group talk to a consumer group coordinator. To detect consumers that have processing issues or are down, there is a poll and a heartbeat mechanism: – Heartbeat thread: Heartbeats are sent periodically to the broker. If no heartbeat is sent during that period, the consumer is considered dead. – Poll thread: This is particularly relevant for Big Data frameworks like Spark in case the processing takes a lot of time. This mechanism detects data processing issues.

**Detailed explanation of each option:**

1. ✅ **A. Poll thread**  
   **Correct**.

2. ❌ **B. Push thread**  
   **Incorrect**.

3. ❌ **C. Heartbeat thread**  
   **Incorrect**.

4. ❌ **D. Offset thread**  
   **Incorrect**.

</details>

## Question 48 (Kafka Producers):
Which properties must be set when producing messages to Kafka by creating a ProducerRecord? 

- A. Topic
- B. Value
- C. Partition
- D. Key

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

Option A. Topic Required – Specifies the Kafka topic where message will be written. Option B. Value Required – Contains the actual message data/payload to send. Incorrect Option C. Partition Optional – Kafka automatically assigns partition using key hash or round-robin if omitted. Option D. Key Optional – Used for partitioning but null key allowed. Enables deterministic routing.

**Detailed explanation of each option:**

1. ✅ **A. Topic**  
   **Correct**.

2. ✅ **B. Value**  
   **Correct**.

3. ❌ **C. Partition**  
   **Incorrect**.

4. ❌ **D. Key**  
   **Incorrect**.

</details>

## Question 49 (Stream Processing):
Using Kafka Streams, which of the supported join operations are windowed? 

- A. KStream-to-KTable
- B. KTable-to-KTable
- C. KStream-to-GlobalKTable
- D. KStream-to-Kstream

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D. KStream‑to‑KStream Correct because KStream‑to‑KStream joins are windowed joins. Since streams are unbounded and continuously flowing, a time window must be defined to determine which records from each stream should be joined together. Without a window, the join would be ambiguous because events could arrive at different times. Incorrect Option A. KStream‑to‑KTable Incorrect because this join is not windowed. A KStream record is joined with the latest value of the KTable for the matching key at the time of processing. Option B. KTable‑to‑KTable Incorrect because this join is also not windowed. It produces a new KTable by joining the current values of two tables based on keys. Option C. KStream‑to‑GlobalKTable Incorrect because this join is not windowed. A KStream record is joined with the corresponding entry in the GlobalKTable using a foreign key mapping, without requiring a time window.

**Detailed explanation of each option:**

1. ❌ **A. KStream-to-KTable**  
   **Incorrect**.

2. ❌ **B. KTable-to-KTable**  
   **Incorrect**.

3. ❌ **C. KStream-to-GlobalKTable**  
   **Incorrect**.

4. ✅ **D. KStream-to-Kstream**  
   **Correct**.

</details>

## Question 50 (Kafka Producers):
Which acknowledgment configuration should be used for a producer to maximize performance? 

- A. acks=all
- B. acks=leader
- C. acks=1
- D. acks=0

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, producers create and write messages to topic partitions and producers can choose to receive acknowledgement of data writes, which can be configured using the acks property. It is the number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. If acks=0 then the producer will not wait for any acknowledgment from the server at all. No guarantee can be made that the server has received the record in this case. However, because the producer is not waiting for any response from the server, it can send messages as fast as the network will support, so this setting can be used to achieve very high throughput. Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. acks=all**  
   **Incorrect**.

2. ❌ **B. acks=leader**  
   **Incorrect**.

3. ❌ **C. acks=1**  
   **Incorrect**.

4. ✅ **D. acks=0**  
   **Correct**.

</details>

## Question 51 (Kafka Setup and Operations):
Which command line script can be used to manage Kafka ACLs? 

- A. bin/kafka-acls.sh
- B. bin/acls.sh
- C. bin/kafka-security.sh
- D. bin/kafka-authorization.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Authorization allows you to define the actions they are permitted to take once connected to the Kafka cluster. Apache Kafka ships with an out-of-box authorization mechanism to establish ACL configurations to protect specific Kafka resources. Kafka ACLs are stored within ZooKeeper and are managed with the kafka-acls.sh command line script. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ✅ **A. bin/kafka-acls.sh**  
   **Correct**.

2. ❌ **B. bin/acls.sh**  
   **Incorrect**.

3. ❌ **C. bin/kafka-security.sh**  
   **Incorrect**.

4. ❌ **D. bin/kafka-authorization.sh**  
   **Incorrect**.

</details>

## Question 52 (Kafka Connect):
Using Kafka Connect, which type of connectors are there to copy data between Kafka and another system? 

- A. SourceConnectors to import data from another system.
- B. SourceConnectors to export data to another system.
- C. SinkConnectors to export data to another system.
- D. SinkConnectors to import data from another system.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other data systems. It makes it simple to quickly define connectors that move large data sets into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing with low latency. An export connector can deliver data from Kafka topics into secondary indexes like Elasticsearch or into batch systems such as Hadoop for offline analysis. You can use SourceConnectors for getting your data into Kafka and SinkConnectors to get your data out of Kafka. For example, JDBCSourceConnector would import a relational database into Kafka, and HDFSSinkConnector would export the contents of a Kafka topic to HDFS files. Further reading: Kafka Connect Concepts.

**Detailed explanation of each option:**

1. ✅ **A. SourceConnectors to import data from another system.**  
   **Correct**.

2. ❌ **B. SourceConnectors to export data to another system.**  
   **Incorrect**.

3. ✅ **C. SinkConnectors to export data to another system.**  
   **Correct**.

4. ❌ **D. SinkConnectors to import data from another system.**  
   **Incorrect**.

</details>

## Question 53 (Kafka Consumers):
Which of the following options is a consumer fetch metric? 

- A. request-latency-avg
- B. bytes-consumed-rate
- C. compression-rate-avg
- D. batch-size-max

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The only consumer fetch metric is the bytes-consumed-rate. It‘s the average number of bytes consumed per second. All other metrics are producer metrics: – batch-size-max: The max number of bytes sent per partition per-request. – compression-rate-avg: The average compression rate of record batches, defined as the average ratio of the compressed batch size over the uncompressed size. – request-latency-avg: The average request latency in ms.

**Detailed explanation of each option:**

1. ❌ **A. request-latency-avg**  
   **Incorrect**.

2. ✅ **B. bytes-consumed-rate**  
   **Correct**.

3. ❌ **C. compression-rate-avg**  
   **Incorrect**.

4. ❌ **D. batch-size-max**  
   **Incorrect**.

</details>

## Question 54 (Kafka Producers):
A Kafka producer is producing at a very high rate and the batches are completely full each time. Which of the following additional configurations help to improve the producer throughput? 

- A. Increase batch.size
- B. Enable compression
- C. Increase linger.ms
- D. Decrease linger.ms

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

To optimize for throughput, producers and consumers must move as much data as possible within a given amount of time. For high throughput, try maximizing the rate at which the data moves. The data rate should be the fastest possible rate. Producer configurations to achieve a high throughput application are: – compression.type: Producers usually send data that is text-based, for example with JSON data. In this case, it is important to apply compression to optimize for throughput. Compression is more effective the bigger the batch of messages being sent to Kafka. Possible values are: lz4 (recommended for performance),snappy, zstd, gzip. – batch.size: With batching strategy of Kafka producers, you can batch messages going to the same partition, which means they collect multiple messages to send together in a single request. The most important step you can take to optimize throughput is to tune the producer batching to increase the batch size and the time spent waiting for the batch to populate with messages. Larger batch sizes result in fewer requests, which reduces load on producers and the broker CPU overhead to process each request. – linger.ms: It‘s the number of milliseconds a producer is willing to wait before sending a batch out (defaults to 0). By introducing some lag, we increase the changes of messages being sent together in a batch. If the batch is full (batch.size) before the end of linger.ms period, it will be sent to Kafka right away. Note: As the batch is full each time, it does not help to change the linger.ms configuration. Enabling compression can also help make more compact batches and increase the throughput of your producer. Further reading: Optimizing for Throughput.

**Detailed explanation of each option:**

1. ✅ **A. Increase batch.size**  
   **Correct**.

2. ✅ **B. Enable compression**  
   **Correct**.

3. ❌ **C. Increase linger.ms**  
   **Incorrect**.

4. ❌ **D. Decrease linger.ms**  
   **Incorrect**.

</details>

## Question 55 (Stream Processing):
A company uses the Kafka Streams API to filter and reduce an input topic into another output topic. Their streams application takes a lot of time and resources to recover the state from Kafka. What can they do in order to speed up recovery? 

- A. Any Kafka Streams application is stateless, so nothing can be done to speed up recovery.
- B. Disable encryption in order to speed up recovery.
- C. Store the Kafka Streams state on a persistent volume.
- D. Store the Kafka Streams state in a cloud database to always recover from the nearest data center.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Although any Kafka Streams application is stateless as the state is stored in Kafka, it can take a while and lots of resources to recover the state from Kafka. In order to speed up recovery, it is advised to store the Kafka Streams state on a persistent volume, so that only the missing part of the state needs to be recovered.

**Detailed explanation of each option:**

1. ❌ **A. Any Kafka Streams application is stateless, so nothing can be done to speed up recovery.**  
   **Incorrect**.

2. ❌ **B. Disable encryption in order to speed up recovery.**  
   **Incorrect**.

3. ✅ **C. Store the Kafka Streams state on a persistent volume.**  
   **Correct**.

4. ❌ **D. Store the Kafka Streams state in a cloud database to always recover from the nearest data center.**  
   **Incorrect**.

</details>

## Question 56 (Kafka Producers):
Which of the following options are true regarding multi-threaded-message processing for Java Kafka clients? 

- A. One Kafka producer can be safely used in multiple threads.
- B. The Kafka producer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.
- C. One Kafka consumer can be safely used in multiple threads.
- D. The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. Kafka producers are thread safe, which means one Kafka producer can be safely used in multiple threads. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ✅ **A. One Kafka producer can be safely used in multiple threads.**  
   **Correct**.

2. ❌ **B. The Kafka producer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.**  
   **Incorrect**.

3. ❌ **C. One Kafka consumer can be safely used in multiple threads.**  
   **Incorrect**.

4. ✅ **D. The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.**  
   **Correct**.

</details>
