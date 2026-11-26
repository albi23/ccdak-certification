## Question 1 (Programming & Serialization):
Which of the following options best describe the benefits of the Confluent Schema Registry? 

- A. Confluent Schema Registry is included in your Kafka brokers and helps to retrieve schemas that describe the data models for the messages.
- B. Confluent Schema Registry provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and XML schemas.
- C. Confluent Schema Registry allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.
- D. Confluent Schema Registry is a distributed storage layer for schemas which uses Kafka as its underlying storage mechanism.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

Option C. Confluent Schema Registry enforces schema evolution rules through configurable compatibility settings. This ensures producers and consumers remain compatible as schemas change over time, which is a core benefit tested in the Confluent Certified Developer exam. Option D. Confluent Schema Registry is implemented as a distributed service that stores schemas in Kafka topics. Using Kafka as the underlying storage provides durability, fault tolerance, and scalability, which is a key architectural benefit. Incorrect: Option A. Schema Registry is not included inside Kafka brokers. It is a separate service that runs independently and communicates with Kafka, so this statement incorrectly describes its deployment model. Option B. While Schema Registry does provide a RESTful interface and supports Avro and JSON Schema, XML schema support is not standard, and this option does not clearly describe a primary benefit compared to the other choices.

**Detailed explanation of each option:**

1. ❌ **A. Confluent Schema Registry is included in your Kafka brokers and helps to retrieve schemas that describe the data models for the messages.**  
   **Incorrect**.

2. ❌ **B. Confluent Schema Registry provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and XML schemas.**  
   **Incorrect**.

3. ✅ **C. Confluent Schema Registry allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.**  
   **Correct**.

4. ✅ **D. Confluent Schema Registry is a distributed storage layer for schemas which uses Kafka as its underlying storage mechanism.**  
   **Correct**.

</details>

## Question 2 (Kafka Internals):
In which scenario do you want to set the broker config “unclean.leader.election.enable=true“?

- A. If you prioritize durability over scalability.
- B. If you prioritize durability over availability.
- C. If you prioritize scalability over availability.
- D. If you prioritize availability over durability.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The broker property unclean.leader.election.enable allows you to specify a preference of availability or durability. If availability is more important than avoiding data loss, ensure that this property is set to true. If preventing data loss is more important than availability, set this property to false. This setting operates as follows: If unclean.leader.election.enable is set to true (enabled), an out-of-sync replica will be elected as leader when there is no live in-sync replica (ISR). This preserves the availability of the partition, but there is a chance of data loss. If unclean.leader.election.enable is set to false and there are no live in-sync replicas, Kafka returns an error and the partition will be unavailable.

**Detailed explanation of each option:**

1. ❌ **A. If you prioritize durability over scalability.**  
   **Incorrect**.

2. ❌ **B. If you prioritize durability over availability.**  
   **Incorrect**.

3. ❌ **C. If you prioritize scalability over availability.**  
   **Incorrect**.

4. ✅ **D. If you prioritize availability over durability.**  
   **Correct**.

</details>

## Question 3 (Kafka Internals):
Which of the following options is the default cleanup policy for all user topics?

- A. log.cleanup.policy=compact
- B. log.cleanup.policy=max-size
- C. log.cleanup.policy=delete
- D. log.cleanup.policy=none

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, unlike other messaging systems, the messages on a topic are not immediately removed after they are consumed. Instead, the configuration of each topic determines how much space the topic is permitted and how it is managed.Concept of making data expire is called as Cleanup. It‘s a broker level configuration. It is important to restrict log segment to continue grow in size.Options for the cleanup policy are either “delete“ or “compact“ or both. The string designates the retention policy to use on old log segments. The default policy (“delete“) will discard old segments when their retention time or size limit has been reached. The “compact“ setting will enable log compaction on the topic.

**Detailed explanation of each option:**

1. ❌ **A. log.cleanup.policy=compact**  
   **Incorrect**.

2. ❌ **B. log.cleanup.policy=max-size**  
   **Incorrect**.

3. ✅ **C. log.cleanup.policy=delete**  
   **Correct**.

4. ❌ **D. log.cleanup.policy=none**  
   **Incorrect**.

</details>

## Question 4 (Kafka Setup and Operations):
Which of the following options best describes integration testing?

- A. Integration tests verify that end-to-end tests with other services work as expected.
- B. Integration tests verify that isolated functional blocks of code work as expected.
- C. Integration tests verify that production deployments work as expected.
- D. Integration tests verify that development environments behave as expected.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Unit testing, integration testing, and schema compatibility are all important steps in building resilient applications in a CI / CD pipeline.Integration testing is the phase in software testing in which individual software modules are combined and tested as a group. Integration testing is conducted to evaluate the compliance of a system or component with specified functional requirements. It occurs after unit testing and before validation testing.Further reading: Application Testing.

**Detailed explanation of each option:**

1. ✅ **A. Integration tests verify that end-to-end tests with other services work as expected.**  
   **Correct**.

2. ❌ **B. Integration tests verify that isolated functional blocks of code work as expected.**  
   **Incorrect**.

3. ❌ **C. Integration tests verify that production deployments work as expected.**  
   **Incorrect**.

4. ❌ **D. Integration tests verify that development environments behave as expected.**  
   **Incorrect**.

</details>

## Question 5 (Kafka Producers):
A company uses Kafka for its sales production application and created a producer to map all the orders into a topic with 5 partitions. The goal was to write all messages for a specific customer id ordered into the same partition, but because one customer orders twice as much products as all other customers together, this specific partition gets too large. The company tries to solve this issue and is looking for a way to give this customer its own partition and then use hash partitioning to map the rest of the accounts to other partitions. What‘s the best possible solution to achieve this?

- A. Adding a unique partition to the ProducerRecord for the specific customer.
- B. Implementing a custom partitioning strategy.
- C. Producing all messages for the specific customer with another hashing algorithm.
- D. Adding another partition and assigning a specific key to this newly created partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka messages are key-value pairs and while it is possible to create a ProducerRecord with just a topic and a value, with the key set to null by default, most applications produce records with keys.By default, all messages with the same key will go to the same partition. This means that if a process is reading only a subset of the partitions in a topic, all the records for a single key will be read by the same process.If a key exists and the default partitioner is used, Kafka will hash the key using the “murmur2“ algorithm, and use the result to map the message to a specific partition.However, Kafka does not limit you to just hash partitions, and sometimes there are good reasons to partition data differently. Using a custom partitioner its possible to map one customer to its own partition and then use hash partitioning to map the rest of the accounts to other partitions.

**Detailed explanation of each option:**

1. ❌ **A. Adding a unique partition to the ProducerRecord for the specific customer.**  
   **Incorrect**.

2. ✅ **B. Implementing a custom partitioning strategy.**  
   **Correct**.

3. ❌ **C. Producing all messages for the specific customer with another hashing algorithm.**  
   **Incorrect**.

4. ❌ **D. Adding another partition and assigning a specific key to this newly created partition.**  
   **Incorrect**.

</details>

## 🚫 Question 6 (Kafka Ecosystem):
What are possible deployment options for ksqlDB?

- A. Headless ksqlDB deployment
- B. Interactive ksqlDB deployment
- C. Controlled ksqlDB deployment
- D. Iterative ksqlDB deployment

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

ksqlDB provides two deployment options: – Headless ksqlDB deployment: The simplest deployment mode for ksqlDB is the headless mode, also called application mode. In the headless mode, you write all of your queries in a SQL file, and then start ksqlDB server instances with this file as an argument. Each server instance will read the given SQL file, compile the ksqlDB statements into Kafka Streams applications and start execution of the generated applications. Headless ksqlDB is recommended for production deployments. – Interactive ksqlDB deployment: The other option for running ksqlDB is interactive mode, in which you interact with the ksqlDB servers through a REST API either directly via your favorite REST clients, through ksqlDB CLI or through Confluent Control Center. Further reading: ksqlDB Deployment.

**Detailed explanation of each option:**

1. ✅ **A. Headless ksqlDB deployment**  
   **Correct**.

2. ✅ **B. Interactive ksqlDB deployment**  
   **Correct**.

3. ❌ **C. Controlled ksqlDB deployment**  
   **Incorrect**.

4. ❌ **D. Iterative ksqlDB deployment**  
   **Incorrect**.

</details>

## Question 7 (Kafka Producers):
Which of the following properties are mandatory for creating a Kafka producer?

- A. bootstrap.servers
- B. value.serializer
- C. key.serializer
- D. compression.type

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

The first step in writing messages to Kafka is to create a producer object with the properties you want to pass to the producer. A Kafka producer has three mandatory properties: – bootstrap.servers: A list of host / port pairs to use for establishing the initial connection to the Kafka cluster. The client will make use of all servers irrespective of which servers are specified here for bootstrapping – this list only impacts the initial hosts used to discover the full set of servers. This list should be in the form host1:port1,host2:port2,…. Since these servers are just used for the initial connection to discover the full cluster membership (which may change dynamically), this list need not contain the full set of servers (you may want more than one, though, in case a server is down). – key.serializer: Name of a class that will be used to serialize the keys of the records we will produce to Kafka. Kafka brokers expect byte arrays as keys and values of messages. However, the producer interface allows, using parameterized types, any Java object to be sent as a key and value. This makes for very readable code, but it also means that the producer has to know how to convert these objects to byte arrays. – value.serializer: Name of a class that will be used to serialize the values of the records we will produce to Kafka. The same way you set key.serializer to a name of a class that will serialize the message key object to a byte array, you set value.serializer to a class that will serialize the message value object. Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ✅ **A. bootstrap.servers**  
   **Correct**.

2. ✅ **B. value.serializer**  
   **Correct**.

3. ✅ **C. key.serializer**  
   **Correct**.

4. ❌ **D. compression.type**  
   **Incorrect**.

</details>

## Question 8 (Kafka Consumers):
The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized. What‘s the only exception to this rule?

- A. Wakeup the consumer.
- B. Close the consumer.
- C. Get the metrics kept by the consumer.
- D. Commit offsets returned on the last poll.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. The only exception to this rule is wakeup(), which can safely be used from an external thread to interrupt an active operation. In this case, a WakeupException will be thrown from the thread blocking on the operation. This can be used to shutdown the consumer from another thread. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ✅ **A. Wakeup the consumer.**  
   **Correct**.

2. ❌ **B. Close the consumer.**  
   **Incorrect**.

3. ❌ **C. Get the metrics kept by the consumer.**  
   **Incorrect**.

4. ❌ **D. Commit offsets returned on the last poll.**  
   **Incorrect**.

</details>

## Question 9 (Kafka Internals):
A company has a Kafka cluster with 4 brokers. For a new streaming application, the company wants to create a production topic with two partitions that is resilient to one broker failure and one broker maintenance. What replication factor will the company specify while creating the topic?

- A. 5
- B. 2
- C. 3
- D. 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka replicates the log for each topic‘s partitions across a configurable number of servers (you can set this replication factor on a topic-by-topic basis). This allows automatic failover to these replicas when a server in the cluster fails so messages remain available in the presence of failures The total number of replicas including the leader constitute the replication factor. The Topic replication factor should always be greater than 1, otherwise it doesn‘t provide resilience to a single server failure. A replication factor of 2 is also not enough, because this does not provide resilience to a server failure and one server being down for maintenance. A replication factor of 5 is not possible, as the company only have 4 brokers in the Kafka cluster. Further reading: Kafka Replication.

**Detailed explanation of each option:**

1. ❌ **A. 5**  
   **Incorrect**.

2. ❌ **B. 2**  
   **Incorrect**.

3. ✅ **C. 3**  
   **Correct**.

4. ❌ **D. 1**  
   **Incorrect**.

</details>

## Question 10 (Kafka Setup and Operations):
Which CLI command can be used to find out all the partitions without a leader?

- A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
- B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions
- C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topics-with-overrides
- D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --unavailable-partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, the purpose of describing topics is to know the leader for the topic, the broker instances acting as replicas for the topic, and the number of partitions of a Kafka topic that has been created with. When describing Kafka topics you can set some additional properties to only show specific topics / partitions, e. g.: –topics-with-overrides: If set when describing topics, only show topics that have overridden configs. –unavailable-partitions: If set when describing topics, only show partitions whose leader is not available. –under-min-isr-partitions: If set when describing topics, only show partitions whose ISR count is less than the configured minimum. –under-replicated-partitions: If set when describing topics, only show under replicated partitions. Further reading: Topic Configurations.

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions**  
   **Incorrect**.

2. ❌ **B. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-min-isr-partitions**  
   **Incorrect**.

3. ❌ **C. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topics-with-overrides**  
   **Incorrect**.

4. ✅ **D. bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --unavailable-partitions**  
   **Correct**.

</details>

## Question 11 (Kafka Producers):
When sending a producer record to the Kafka broker, what does the send() method return?

- A. The send() method returns a Future Object with RecordMetadata.
- B. The send() method returns an Object with RecordMetadata.
- C. The send() method returns true if the call succeeded and false if the call did not succeed.
- D. The send() method returns 1 if the call succeeded and 0 if the call did not succeed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

KafkaProducer is a Kafka client that publishes records to the Kafka cluster. The send() method is asynchronous and it sends the ProducerRecord. The message will then be placed in a buffer and will be sent to the broker in a separate thread.The send() method returns a Future object with RecordMetadata.Further reading: Producer API.

**Detailed explanation of each option:**

1. ✅ **A. The send() method returns a Future Object with RecordMetadata.**  
   **Correct**.

2. ❌ **B. The send() method returns an Object with RecordMetadata.**  
   **Incorrect**.

3. ❌ **C. The send() method returns true if the call succeeded and false if the call did not succeed.**  
   **Incorrect**.

4. ❌ **D. The send() method returns 1 if the call succeeded and 0 if the call did not succeed.**  
   **Incorrect**.

</details>

## Question 12 (Kafka Consumers):
A company disabled auto commit of offsets for their consumer application in order to have more control over the time at which offsets are committed. What‘s a good way to manually commit the offsets, if the company does not want to block the application until the broker responds to the commit request?

- A. Use the poll() API.
- B. Use the commitAsync() API.
- C. Use await / async in the consumer application.
- D. Use the commitSync() API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. Automatic commits are convenient, but they dont give developers enough control to avoid duplicate messages. By setting auto.commit.offset=false, offsets will only be committed when the application explicitly chooses to do so. The simplest and most reliable of the commit APIs is commitSync(), but this will block the application until the broker responds to the commit request. Another option is the asynchronous commit API commitAsync(), which will not block the application and not limit the throughput of the application. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Use the poll() API.**  
   **Incorrect**.

2. ✅ **B. Use the commitAsync() API.**  
   **Correct**.

3. ❌ **C. Use await / async in the consumer application.**  
   **Incorrect**.

4. ❌ **D. Use the commitSync() API.**  
   **Incorrect**.

</details>

## Question 13 (Kafka Core Concepts):
In Kafka, if the property “auto.create.topics.enable“ is set to true, what are the circumstances under which a Kafka broker automatically creates a topic?

- A. If a producer sends a message to the topic.
- B. If a client requests metadata for the topic.
- C. If the number of partitions for the topic gets updated.
- D. If a consumer reads a message from the topic.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

The Kafka broker uses the auto.create.topics.enable property to control automatic topic creation. The default setting for the property enables automatic topic creation. If set to true, a Kafka broker automatically creates a topic under the following circumstances: – When a producer starts writing messages to the topic. – When a consumer starts reading messages from the topic. – When any client requests metadata for the topic.

**Detailed explanation of each option:**

1. ✅ **A. If a producer sends a message to the topic.**  
   **Correct**.

2. ✅ **B. If a client requests metadata for the topic.**  
   **Correct**.

3. ❌ **C. If the number of partitions for the topic gets updated.**  
   **Incorrect**.

4. ✅ **D. If a consumer reads a message from the topic.**  
   **Correct**.

</details>

## Question 14 (Kafka Internals):
Which of the following options are true for a Kafka Controller?

- A. At any time at least two Controller brokers must exist to perform majority votings.
- B. It is a Kafka broker which is elected by Zookeeper.
- C. It is a Kafka broker which is responsible for partition leader election.
- D. It is a Kafka broker which is responsible for consumer group rebalances.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

In a Kafka cluster, one (and only one) of the brokers serves as the controller, which is responsible for managing the states of partitions and replicas and for performing administrative tasks like reassigning partitions. The election of that broker happens thanks to Zookeeper.Kafka Controller registers handlers to be notified about changes in Zookeeper and propagate them across brokers in a Kafka cluster.Further reading: Controller Internals.

**Detailed explanation of each option:**

1. ❌ **A. At any time at least two Controller brokers must exist to perform majority votings.**  
   **Incorrect**.

2. ✅ **B. It is a Kafka broker which is elected by Zookeeper.**  
   **Correct**.

3. ✅ **C. It is a Kafka broker which is responsible for partition leader election.**  
   **Correct**.

4. ❌ **D. It is a Kafka broker which is responsible for consumer group rebalances.**  
   **Incorrect**.

</details>

## Question 15 (Kafka Setup and Operations):
How does Garbage Collection help to improve Kafka‘s overall performance?

- A. Garbage collection is a JVM process that automatically consumes messages to increase the fetch rate.
- B. Garbage collection is a JVM process that automatically frees up memory and removes unused pointers to objects.
- C. Garbage collection is a JVM process that removes old message keys but ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition.
- D. Garbage collection is a JVM process that automatically shuts down out of sync brokers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Java Garbage Collection is the process by which Java programs perform automatic memory management. Java programs compile to bytecode that can be run on a Java Virtual Machine, or JVM for short. When Java programs run on the JVM, objects are created on the heap, which is a portion of memory dedicated to the program. Eventually, some objects will no longer be needed. The garbage collector finds these unused objects and deletes them to free up memory.Further reading: Java Garbage Collection.

**Detailed explanation of each option:**

1. ❌ **A. Garbage collection is a JVM process that automatically consumes messages to increase the fetch rate.**  
   **Incorrect**.

2. ✅ **B. Garbage collection is a JVM process that automatically frees up memory and removes unused pointers to objects.**  
   **Correct**.

3. ❌ **C. Garbage collection is a JVM process that removes old message keys but ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition.**  
   **Incorrect**.

4. ❌ **D. Garbage collection is a JVM process that automatically shuts down out of sync brokers.**  
   **Incorrect**.

</details>

## Question 16 (Kafka Consumers):
Which API can be used to shutdown a consumer from another thread?

- A. flush()
- B. wakeup()
- C. shutdown()
- D. close()

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. The only exception to this rule is wakeup(), which can safely be used from an external thread to interrupt an active operation. In this case, a WakeupException will be thrown from the thread blocking on the operation. This can be used to shutdown the consumer from another thread. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ❌ **A. flush()**  
   **Incorrect**.

2. ✅ **B. wakeup()**  
   **Correct**.

3. ❌ **C. shutdown()**  
   **Incorrect**.

4. ❌ **D. close()**  
   **Incorrect**.

</details>

## Question 17 (Kafka Connect):
Using Kafka Connect, which type of connectors are there to copy data between Kafka and another system?

- A. SinkConnectors to import data from another system.
- B. SinkConnectors to export data to another system.
- C. SourceConnectors to export data to another system.
- D. SourceConnectors to import data from another system.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other data systems. It makes it simple to quickly define connectors that move large data sets into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing with low latency. An export connector can deliver data from Kafka topics into secondary indexes like Elasticsearch or into batch systems such as Hadoop for offline analysis.You can use SourceConnectors for getting your data into Kafka and SinkConnectors to get your data out of Kafka. For example, JDBCSourceConnector would import a relational database into Kafka, and HDFSSinkConnector would export the contents of a Kafka topic to HDFS files.Further reading: Kafka Connect Concepts.

**Detailed explanation of each option:**

1. ❌ **A. SinkConnectors to import data from another system.**  
   **Incorrect**.

2. ✅ **B. SinkConnectors to export data to another system.**  
   **Correct**.

3. ❌ **C. SourceConnectors to export data to another system.**  
   **Incorrect**.

4. ✅ **D. SourceConnectors to import data from another system.**  
   **Correct**.

</details>

## Question 18 (Kafka Producers):
A Kafka producer has the retries property set to 2147483647 to resend any record whose send fails with a potentially transient error. Which of the following additional configurations could potentially change the ordering of records? 

- A. enable.idempotence=false
- B. max.in.flight.requests.per.connection=1
- C. enable.idempotence=true
- D. max.in.flight.requests.per.connection=5

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

1. ❌ **A. enable.idempotence=false**  
   Incorrect because disabling idempotence affects duplicate suppression and reliability, not ordering. Ordering is only impacted by multiple in‑flight requests.

2. ❌ **B. max.in.flight.requests.per.connection=1**  
   Incorrect because setting this to 1 ensures strict ordering. Only one request can be in flight at a time, so retries cannot cause out‑of‑order delivery.

3. ❌ **C. enable.idempotence=true**  
   Incorrect because enabling idempotence prevents duplicates and improves reliability. It does not cause ordering issues; in fact, it is recommended when retries are set high.

4. ✅ **D. max.in.flight.requests.per.connection=5**  
   Correct because when more than one request is allowed in flight, retries can cause later requests to succeed before earlier retried requests finish. This can lead to out‑of‑order delivery of records, especially when combined with very high retries.

</details>

## Question 19 (Kafka Producers):
Which of the following producer callback exceptions is non-retriable and therefore the message will not be sent again?

- A. TimeoutException
- B. NotEnoughReplicasException
- C. RecordTooLargeException
- D. UnknownTopicOrPartitionException

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, producers create and write messages to topic partitions. There are the following exceptions possible happening during callback. 1: Non-Retriable exceptions (fatal, the message will never be sent): – InvalidTopicException – OffsetMetadataTooLargeException – RecordBatchTooLargeException – RecordTooLargeException – UnknownServerException 2: Retriable exceptions (transient, may be covered by increasing the number of retries): – CorruptRecordException – InvalidMetadataException – NotEnoughReplicasAfterAppendException – NotEnoughReplicasException – OffsetOutOfRangeException – TimeoutException – UnknownTopicOrPartitionException Further reading: Exception Class.

**Detailed explanation of each option:**

1. ❌ **A. TimeoutException**  
   **Incorrect**.

2. ❌ **B. NotEnoughReplicasException**  
   **Incorrect**.

3. ✅ **C. RecordTooLargeException**  
   **Correct**.

4. ❌ **D. UnknownTopicOrPartitionException**  
   **Incorrect**.

</details>

## 🚫 Question 20 (Kafka Ecosystem):
Using ksqlDB, which of the following two options together allow you to use Avro data and integrate with Confluent Schema Registry?

- A. To use Avro data with ksqlDB you must have Schema Registry installed.
- B. Configure the “enable.avro.registry“ property in the ksqlDB server configuration and use the Confluent Control Center to point to the Schema Registry.
- C. Configure your Kafka cluster to use SQL as the default programming language.
- D. Configure the “ksql.schema.registry.url“ property in the ksqlDB server configuration to point to Schema Registry.

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

To be able to use Avro data and integrate with Confluent Schema Registry you need to do the following two steps: – Install the Confluent Schema Registry. This is included by default with Confluent Platform. – Configure the ksql.schema.registry.url property in the ksqlDB server configuration to point to Schema Registry. Important Note: Avro message values are supported. Avro keys are not yet supported.

**Detailed explanation of each option:**

1. ✅ **A. To use Avro data with ksqlDB you must have Schema Registry installed.**  
   **Correct**.

2. ❌ **B. Configure the “enable.avro.registry“ property in the ksqlDB server configuration and use the Confluent Control Center to point to the Schema Registry.**  
   **Incorrect**.

3. ❌ **C. Configure your Kafka cluster to use SQL as the default programming language.**  
   **Incorrect**.

4. ✅ **D. Configure the “ksql.schema.registry.url“ property in the ksqlDB server configuration to point to Schema Registry.**  
   **Correct**.

</details>

## Question 21 (Kafka Internals):
Which of the following designs of cluster replication should be used in a multi-cluster environment for analytics purposes only?

- A. Passive -> Active replication
- B. Active -> Passive replication
- C. Active -> Active replication
- D. Passive -> Passive replication

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

For Multi-datacenter use cases a replicator can be deployed across clusters and in multiple datacenters. Multi-datacenter deployments enable use-cases such as:– Active -> Active geo-localized deployments: allows users to access a near-by data center to optimize their architecture for low latency and high performance. Replication can be done in both sides and data can be produced and consumed in every cluster.– Active-> Passive disaster recover (DR) deployments: in an event of a partial or complete datacenter disaster, allow failing over applications to use Confluent Platform in a different datacenter.– Active -> Passive centralized analytics: Aggregate data from multiple Apache Kafka clusters into one location for organization-wide analytics. No producers will be used at the replicated cluster, it‘s just for consuming data for analytic purposes.Further reading: Cluster Replication Flows.

**Detailed explanation of each option:**

1. ❌ **A. Passive -> Active replication**  
   **Incorrect**.

2. ✅ **B. Active -> Passive replication**  
   **Correct**.

3. ❌ **C. Active -> Active replication**  
   **Incorrect**.

4. ❌ **D. Passive -> Passive replication**  
   **Incorrect**.

</details>

## Question 22 (Kafka Internals):
In Kafka, how often is log compaction evaluated?

- A. Every time a message is written to the active segment.
- B. Every time a message with an existing key is produced.
- C. Every time the active segment is closed.
- D. Every time a message with a new key is produced.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The main idea behind Log Compaction is to selectively remove records where there are most recent updates with the same primary key. Log compaction strategy ensures that Kafka will always retain at least the last known value for each message key within the log for a single topic partition. It is mostly used for scenarios such as restoring to the previous state before the application crashed or system failed, or while reloading cache after application restarts. In simple terms, Apache Kafka will keep the latest version of a record and delete the older versions with same key.Some important notes: – Offsets do not change when enabling log compaction.– Any consumer that is reading from the tail of a log (most current data) will still see all the messages sent to the topic.– Ordering of messages is kept.– Deleted records can still be seen by consumers for a period of “delete.retention.ms“ (default is 24 hours).– Log compaction is evaluated every time the active segment is closed.Log Compaction is configured by the properties “log.cleanup.policy=compact“ and “segment.ms“ (default 7 days). “Segment.ms“ is the maximum amount of time to wait to close the active segment.Further reading: Log Compaction Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Every time a message is written to the active segment.**  
   **Incorrect**.

2. ❌ **B. Every time a message with an existing key is produced.**  
   **Incorrect**.

3. ✅ **C. Every time the active segment is closed.**  
   **Correct**.

4. ❌ **D. Every time a message with a new key is produced.**  
   **Incorrect**.

</details>

## Question 23 (Stream Processing):
A company uses the Kafka Streams API to filter and reduce an input topic into another output topic. Their streams application takes a lot of time and resources to recover the state from Kafka. What can they do in order to speed up recovery? 

- A. Disable encryption in order to speed up recovery.
- B. Any Kafka Streams application is stateless, so nothing can be done to speed up recovery.
- C. Store the Kafka Streams state in a cloud database to always recover from the nearest data center.
- D. Store the Kafka Streams state on a persistent volume.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Although any Kafka Streams application is stateless as the state is stored in Kafka, it can take a while and lots of resources to recover the state from Kafka. In order to speed up recovery, it is advised to store the Kafka Streams state on a persistent volume, so that only the missing part of the state needs to be recovered.

**Detailed explanation of each option:**

1. ❌ **A. Disable encryption in order to speed up recovery.**  
   **Incorrect**.

2. ❌ **B. Any Kafka Streams application is stateless, so nothing can be done to speed up recovery.**  
   **Incorrect**.

3. ❌ **C. Store the Kafka Streams state in a cloud database to always recover from the nearest data center.**  
   **Incorrect**.

4. ✅ **D. Store the Kafka Streams state on a persistent volume.**  
   **Correct**.

</details>

## 🚫 Question 24 (Kafka Setup and Operations):
If you want to change a broker setting for your entire Kafka cluster, what‘s the best possible solution for this?

- A. Change the broker configuration in all of your brokers‘ configuration files and restart all the brokers one by one to make this setting active.
- B. Change the broker configuration in the Zookeeper configuration file and restart the cluster to make this setting active.
- C. Change the broker configuration in one of your brokers‘ configuration files and restart the cluster to make this setting active.
- D. Change the broker configuration in the Zookeeper configuration file and restart all the brokers one by one to make this setting active.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka, if you want to change a broker property for your entire cluster you need to follow the two steps: – Change the configuration for every broker in every file “server.properties“. – Proceed to a rolling restart of all of your brokers to restart them one by one.

**Detailed explanation of each option:**

1. ✅ **A. Change the broker configuration in all of your brokers‘ configuration files and restart all the brokers one by one to make this setting active.**  
   **Correct**.

2. ❌ **B. Change the broker configuration in the Zookeeper configuration file and restart the cluster to make this setting active.**  
   **Incorrect**.

3. ❌ **C. Change the broker configuration in one of your brokers‘ configuration files and restart the cluster to make this setting active.**  
   **Incorrect**.

4. ❌ **D. Change the broker configuration in the Zookeeper configuration file and restart all the brokers one by one to make this setting active.**  
   **Incorrect**.

</details>

## Question 25 (Kafka Consumers):
What happens for a consumer with the configuration “auto.offset.reset=none“, if there is no initial offset in Kafka or if the current offset does not exist any more on the server?

- A. The consumer restores the offset history from the official Kafka archive.
- B. The consumer automatically resets the offset to the earliest offset.
- C. The consumer throws an exception.
- D. The consumer automatically resets the offset to the latest offset.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The consumer configuration “auto.offset.reset“ tells the consumer what to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server (e. g. because that data has been deleted).There are the following options:– earliest: Automatically reset the offset to the earliest offset.– latest: Automatically reset the offset to the latest offset.– none: Throw exception to the consumer if no previous offset is found for the consumer‘s group.– anything else: Throw exception to the consumer.Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. The consumer restores the offset history from the official Kafka archive.**  
   **Incorrect**.

2. ❌ **B. The consumer automatically resets the offset to the earliest offset.**  
   **Incorrect**.

3. ✅ **C. The consumer throws an exception.**  
   **Correct**.

4. ❌ **D. The consumer automatically resets the offset to the latest offset.**  
   **Incorrect**.

</details>

## Question 26 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for FORWARD schema evolution? 

- A. Add optional fields
- B. Delete optional fields
- C. Delete fields
- D. Add fields

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Option B. Delete optional fields In FORWARD schema evolution, new consumers using the updated schema must be able to read data produced with the old schema. Removing optional fields is allowed because old data may still be successfully read without requiring those fields. Option D. Add fields Adding new fields is allowed in FORWARD compatibility as long as the fields have default values. This ensures that new consumers can read older data that does not contain the newly added fields. Incorrect: Option A. Add optional fields Adding optional fields is typically associated with BACKWARD compatibility. In FORWARD compatibility, the focus is on ensuring new schemas can read old data, not on how old consumers handle new fields. Option C. Delete fields Deleting required (non-optional) fields breaks FORWARD compatibility because new consumers expecting those fields will not be able to correctly read older data that includes them.

**Detailed explanation of each option:**

1. ❌ **A. Add optional fields**  
   **Incorrect**.

2. ✅ **B. Delete optional fields**  
   **Correct**.

3. ❌ **C. Delete fields**  
   **Incorrect**.

4. ✅ **D. Add fields**  
   **Correct**.

</details>

## Question 27 (Kafka Producers):
If you are producing messages to a Kafka topic, which producer property needs to be set if you want to receive leader acknowledgment of data writes?

- A. acks=leader
- B. acks=0
- C. acks=1
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, producers create and write messages to topic partitions and Producers can choose to receive acknowledgement of data writes, which can be configured using the acks property. It is the number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent. The following settings are allowed: acks=0: If set to zero then the producer will not wait for any acknowledgment from the server at all. No guarantee can be made that the server has received the record in this case (possible data loss). acks=1: This will mean the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers. In this case should the leader fail immediately after acknowledging the record but before the followers have replicated it then the record will be lost (limited data loss). acks=all: This means the leader will wait for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost as long as at least one in-sync replica remains alive. This is the strongest available guarantee. This is equivalent to the acks=-1 setting (no data loss). Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. acks=leader**  
   **Incorrect**.

2. ❌ **B. acks=0**  
   **Incorrect**.

3. ✅ **C. acks=1**  
   **Correct**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## 🚫 Question 28 (Kafka Ecosystem):
Which of the following data formats are supported by ksqlDB?

- A. Avro message values
- B. DELIMITED
- C. JSON
- D. XML

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

ksqlDB currently supports the following formats: – DELIMITED (e. g. comma-separated value) – JSON – Avro message values are supported. Avro keys are not yet supported. This requires Schema Registry and ksql.schema.registry.url in the ksqlDB server configuration file. – KAFKA (for example, a BIGINT that‘s serialized using Kafka‘s standard LongSerializer).

**Detailed explanation of each option:**

1. ✅ **A. Avro message values**  
   **Correct**.

2. ✅ **B. DELIMITED**  
   **Correct**.

3. ✅ **C. JSON**  
   **Correct**.

4. ❌ **D. XML**  
   **Incorrect**.

</details>

## Question 29 (Kafka Consumers):
A company built a consumer application to automatically commit offsets of processed messages. What happens if the committed offset is larger than the offset of the last message the client actually processed?

- A. All messages between the last processed offset and the committed offset will be missed by the consumer group.
- B. All messages between the last processed offset and the committed offset will be processed twice by the consumer group.
- C. You need to set the property “enable.auto.commit“ to true in order to process all messages between the last processed offset and the committed offset.
- D. The consumer application throws a runtime error because it does not know where to start processing messages.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

As a consumer in the group reads messages from the partitions assigned by the coordinator, it must commit the offsets corresponding to the messages it has read. If the consumer crashes or is shut down, its partitions will be re-assigned to another member, which will begin consumption from the last committed offset of each partition. By default, the consumer is configured to auto-commit offsets. Using auto-commit gives you “at least once“ delivery. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there. – If the committed offset is smaller than the offset of the last message the client processed, the messages between the last processed offset and the committed offset will be processed twice. – If the committed offset is larger than the offset of the last message the client actually processed, all messages between the last processed offset and the committed offset will be missed by the consumer group. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. All messages between the last processed offset and the committed offset will be missed by the consumer group.**  
   **Correct**.

2. ❌ **B. All messages between the last processed offset and the committed offset will be processed twice by the consumer group.**  
   **Incorrect**.

3. ❌ **C. You need to set the property “enable.auto.commit“ to true in order to process all messages between the last processed offset and the committed offset.**  
   **Incorrect**.

4. ❌ **D. The consumer application throws a runtime error because it does not know where to start processing messages.**  
   **Incorrect**.

</details>

## Question 30 (Kafka Setup and Operations):
The new security team of a company configured the Confluent Server Authorizer to be able to capture, protect, and preserve authorization activity into topics in their production Kafka cluster. Which concept name best describes this security configuration which helps to track user and application access across the platform?

- A. RBAC tracking
- B. Audit logs
- C. ACL decisions
- D. Log replication

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka does not provide a mechanism for maintaining a record of authorization decisions out of the box. Operators are required to capture and parse unstructured logs from brokers in order to build observations on ACL decisions. Confluent Platform complements Kafka with structured audit logs, which provide a way to capture, protect, and preserve authorization activity into Kafka topics. The primary value of audit logs is that they provide data you can use to assess security risks in your local and remote Kafka clusters. They contain all of the information necessary to follow a user‘s interaction with your local or remote Kafka clusters, and provide a way to: – Track user and application access across the platform. – Identify abnormal behavior and anomalies. – Proactively monitor and resolve security risks. Note: Before configuring and using audit logs, you must configure the Confluent Server Authorizer. Further reading: Audit Log Concepts.

**Detailed explanation of each option:**

1. ❌ **A. RBAC tracking**  
   **Incorrect**.

2. ✅ **B. Audit logs**  
   **Correct**.

3. ❌ **C. ACL decisions**  
   **Incorrect**.

4. ❌ **D. Log replication**  
   **Incorrect**.

</details>

## Question 31 (Kafka Consumers):
Consider the following consumer example: while (true) { ConsumerRecords<String, String> records = consumer.poll(100); for (ConsumerRecords<String, String> record : records) { System.out.printf(“topic = %s, partition = %s, offset = %d, customer = %s, country = %s\n“, record.topic(), record.partition(), record.offset(), record.key(), record.value()); } try { consumer.commitSync(); } catch (CommitFailedException e) { log.error(“commit failed“, e) } } Which delivery guarantee does this consumer use? 

- A. At-most once delivery.
- B. Exactly once delivery.
- C. At-least once delivery.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. At-least once delivery Why correct: In this code, the consumer processes records first and then commits offsets synchronously (commitSync()). If a failure occurs after processing but before committing, the same records may be re-processed when the consumer restarts. This guarantees that every message is processed at least once, but duplicates are possible. Incorrect Option A. At-most once delivery Why incorrect: At-most once delivery would require committing offsets before processing. That way, if a failure occurs after committing but before processing, the message is lost. Since this code commits after processing, it does not provide at-most once semantics. Option B. Exactly once delivery Why incorrect: Exactly once delivery requires integration with Kafka transactions and idempotent producers/consumers. This code does not use transactions or idempotent writes, so duplicates are possible. Therefore, it cannot guarantee exactly once semantics.

**Detailed explanation of each option:**

1. ❌ **A. At-most once delivery.**  
   **Incorrect**.

2. ❌ **B. Exactly once delivery.**  
   **Incorrect**.

3. ✅ **C. At-least once delivery.**  
   **Correct**.

</details>

## Question 32 (Kafka Setup and Operations):
A company has problems with the performance of their Kafka application and wants to optimize and tune the clients. How could the company measure their bandwidth in an easy way as a first baseline?

- A. Measure your bandwidth using the Kafka topic performance configuration settings.
- B. Measure your bandwidth using the Kafka tool “kafka-client-performance“.
- C. Measure your bandwidth using the Kafka Streams API.
- D. Measure your bandwidth using the Kafka tools “kafka-producer-perf-test“ and “kafka-consumer-perf-test“.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

After you complete unit and integration testing, you can benchmark and optimize your applications based on your service goals to tune performance.Benchmark testing is important because there is no one-size-fits-all recommendation for the configuration parameters you need to develop Kafka applications to Confluent Cloud. Proper configuration always depends on the use case, other features you have enabled, the data profile, and more. You should run benchmark tests if you plan to tune Kafka clients beyond the defaults.First, measure your bandwidth using the Kafka tools kafka-producer-perf-test and kafka-consumer-perf-test.Further reading: Optimizing and Tuning.

**Detailed explanation of each option:**

1. ❌ **A. Measure your bandwidth using the Kafka topic performance configuration settings.**  
   **Incorrect**.

2. ❌ **B. Measure your bandwidth using the Kafka tool “kafka-client-performance“.**  
   **Incorrect**.

3. ❌ **C. Measure your bandwidth using the Kafka Streams API.**  
   **Incorrect**.

4. ✅ **D. Measure your bandwidth using the Kafka tools “kafka-producer-perf-test“ and “kafka-consumer-perf-test“.**  
   **Correct**.

</details>

## Question 33 (Stream Processing):
Which of the following joins does not require input topics to be having the same number of partitions?

- A. KStream-KStream
- B. KTable-KTable
- C. KStream-GlobalKTable
- D. KStream-KTable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When joining streams or tables input data must be co-partitioned. This ensures that input records with the same key, from both sides of the join, are delivered to the same stream task during processing. It is the responsibility of the user to ensure data co-partitioning when joining. Data co-partitioning is required because KStream-KStream, KTable-KTable, and KStream-KTable joins are performed based on the keys of records (e. g., leftRecord.key == rightRecord.key). The requirements for data co-partitioning are: – The input topics of the join (left side and right side) must have the same number of partitions. – All applications that write to the input topics must have the same partitioning strategy so that records with the same key are delivered to same partition number. Note: If possible, consider using global tables (GlobalKTable) for joining because they do not require data co-partitioning. Further reading: Joining Concepts.

**Detailed explanation of each option:**

1. ❌ **A. KStream-KStream**  
   **Incorrect**.

2. ❌ **B. KTable-KTable**  
   **Incorrect**.

3. ✅ **C. KStream-GlobalKTable**  
   **Correct**.

4. ❌ **D. KStream-KTable**  
   **Incorrect**.

</details>

## Question 34 (Stream Processing):
Which processing guarantees does Kafka Streams support?

- A. exactly-once processing
- B. at-least-once processing
- C. at-most-once processing

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

Kafka Streams supports at-least-once and exactly-once processing guarantees: – At-least-once semantics: Records are never lost but may be redelivered. If your stream processing application fails, no data records are lost and fail to be processed, but some data records may be re-read and therefore re-processed. At-least-once semantics is enabled by default (processing.guarantee=“at_least_once“) in your Streams configuration. – Exactly-once semantics: Records are processed once. Even if a producer sends a duplicate record, it is written to the broker exactly once. Exactly-once stream processing is the ability to execute a read-process-write operation exactly one time. All of the processing happens exactly once, including the processing and the materialized state created by the processing job that is written back to Kafka. To enable exactly-once semantics, set processing.guarantee=“exactly_once“ in your Streams configuration. Note: Exactly-once processing is guaranteed for Kafka -> Kafka workflows only. Further reading: Streams Processing Guarantees.

**Detailed explanation of each option:**

1. ✅ **A. exactly-once processing**  
   **Correct**.

2. ✅ **B. at-least-once processing**  
   **Correct**.

3. ❌ **C. at-most-once processing**  
   **Incorrect**.

</details>

## Question 35 (Kafka Consumers):
What happens for a consumer application when closing one of the consumers cleanly?

- A. The consumer application will consume messages with one consumer less.
- B. The consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately.
- C. The consumer application breaks with the exception NOT_ENOUGH_CONSUMERS.
- D. The Kafka broker will notify the group coordinator that one consumer is leaving, and the group coordinator will trigger a rebalance immediately.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The way consumers maintain membership in a consumer group and ownership of the partitions assigned to them is by sending heartbeats to a Kafka broker designated as the group coordinator (this broker can be different for different consumer groups). As long as the consumer is sending heartbeats at regular intervals, it is assumed to be alive, well, and processing messages from its partitions. Heartbeats are sent when the consumer polls (i. e., retrieves records) and when it commits records it has consumed.When closing a consumer cleanly, the consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately, reducing the gap in processing.

**Detailed explanation of each option:**

1. ❌ **A. The consumer application will consume messages with one consumer less.**  
   **Incorrect**.

2. ✅ **B. The consumer will notify the group coordinator that it is leaving, and the group coordinator will trigger a rebalance immediately.**  
   **Correct**.

3. ❌ **C. The consumer application breaks with the exception NOT_ENOUGH_CONSUMERS.**  
   **Incorrect**.

4. ❌ **D. The Kafka broker will notify the group coordinator that one consumer is leaving, and the group coordinator will trigger a rebalance immediately.**  
   **Incorrect**.

</details>

## Question 36 (Stream Processing):
Which of the following Kafka Streams domain specific language operations are stateful?

- A. Aggregate
- B. Filter
- C. Reduce
- D. Join

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

The KStream and KTable interfaces support a variety of transformation operations. Stateful transformations depend on state for processing inputs and producing outputs and require a state store associated with the stream processor. For example, in aggregating operations, a windowing state store is used to collect the latest aggregation results per window. In join operations, a windowing state store is used to collect all of the records received so far within the defined window boundary. After records are grouped by key via groupByKey or groupBy  and thus represented as either a KGroupedStream or a KGroupedTable, they can be transformed: – Aggregate: Aggregates the values of records by the grouped key. – Count: Counts the number of records by the grouped key. – Reduce: Combines the values of records by the grouped key. Streams and Tables can also be joined. All joins are stateful. To learn more about all the join operations, you can check out the Streams Join documentation. Further reading: Streams Stateful Operations.

**Detailed explanation of each option:**

1. ✅ **A. Aggregate**  
   **Correct**.

2. ❌ **B. Filter**  
   **Incorrect**.

3. ✅ **C. Reduce**  
   **Correct**.

4. ✅ **D. Join**  
   **Correct**.

</details>

## Question 37 (Stream Processing):
The following Kafka Streams example demonstrates how to use the reduce function to sum odd numbers. final StreamsBuilder builder = new StreamsBuilder(); final KStream input = builder.stream(“numbers-topic“); final KTable sumOfOddNumbers = input .filter((k, v) -> v % 2 != 0) .selectKey((k, v) -> 1) .groupByKey() .reduce((v1, v2) -> v1 + v2); sumOfOddNumbers.toStream().to(“sum-of-odd-numbers-topic“); builder.build(); What‘s an appropriate topic configuration for the topic “sum-of-odd-numbers-topic“? 

- A. cleanup.policy=compact
- B. flush.messages=9223372036854775807
- C. file.delete.delay.ms=60000
- D. cleanup.policy=delete

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams is a client library for building streaming applications and microservices, where the input and output data are stored in Kafka clusters.The reduce function combines the values of (non-windowed) records by the grouped key (in the example the key is always 1). The current record value is combined with the last reduced value, and a new reduced value (in the example the sum) is returned.The result is aggregated into a table with the sum as the value. We have to enable log compaction for this topic to align the topic‘s cleanup policy with KTable semantics.Further reading: Full Code Example.

**Detailed explanation of each option:**

1. ✅ **A. cleanup.policy=compact**  
   **Correct**.

2. ❌ **B. flush.messages=9223372036854775807**  
   **Incorrect**.

3. ❌ **C. file.delete.delay.ms=60000**  
   **Incorrect**.

4. ❌ **D. cleanup.policy=delete**  
   **Incorrect**.

</details>

## Question 38 (Kafka Producers):
Which of the following properties should be configured to aim for a high throughput producer application?

- A. max.in.flight.requests.per.connection
- B. batch.size
- C. compression.type
- D. linger.ms

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

Option B. batch.size Correct because increasing batch.size allows the producer to batch more records together before sending them to the broker. Larger batches reduce the overhead per message and improve throughput, though at the cost of slightly higher latency. Option C. compression.type Correct because enabling compression (e.g., snappy, lz4, or zstd) reduces the size of data sent over the network. Smaller payloads mean fewer bytes transmitted, improving throughput and reducing broker storage usage. Option D. linger.ms Correct because increasing linger.ms allows the producer to wait a bit longer before sending a batch, giving more time for additional records to accumulate. This results in larger batches and higher throughput, though it introduces a small delay. Incorrect Option A. max.in.flight.requests.per.connection Incorrect in this context because while increasing this property can improve concurrency, it does not directly optimize throughput in the same way as batching and compression. Moreover, setting it too high can cause message reordering issues when retries are enabled, which is risky for applications requiring strict ordering.

**Detailed explanation of each option:**

1. ❌ **A. max.in.flight.requests.per.connection**  
   **Incorrect**.

2. ✅ **B. batch.size**  
   **Correct**.

3. ✅ **C. compression.type**  
   **Correct**.

4. ✅ **D. linger.ms**  
   **Correct**.

</details>

## Question 39 (Kafka Setup and Operations):
To produce messages with key-value delimiters to a Kafka topic, which two properties need to be set using the “kafka-console-producer“ CLI?

- A. --property key && --property separator
- B. --property parse.key && --property key.separator
- C. --property parse.key && --property separator
- D. --property key && --property key.separator

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

It is possible to define a key-value delimiter for the given producer instance. The delimiter can vary each time you run the tool. For example, if you run the tool with the delimiter set to – and then a second time using :, Kafka will know how to store the data. The first term is always stored as the key, the second as the value. As a result, when the data written this way is consumed, the keys and values are consumed irrespective of what delimiter was used when the records were written to the topic. To produce messages with key-value delimiters, you need to set two properties, parse.key and key.separator. Both properties can be set with the –properties option: bin/kafka-console-producer.sh –topic test_topic –bootstrap-server 127.0.0.1:9092 –property parse.key=true –property key.separator=“:“ Further reading: Producer Example.

**Detailed explanation of each option:**

1. ❌ **A. --property key && --property separator**  
   **Incorrect**.

2. ✅ **B. --property parse.key && --property key.separator**  
   **Correct**.

3. ❌ **C. --property parse.key && --property separator**  
   **Incorrect**.

4. ❌ **D. --property key && --property key.separator**  
   **Incorrect**.

</details>

## 🚫 Question 40 (Kafka Ecosystem):
A company deployed a Kafka cluster on 10 brokers. The production topic has a replication factor of 3 and 5 topic partitions. Because most of the developers are very familiar with SQL, the company decided to use ksqlDB to process data using intuitive SQL-like syntax. For maximum parallelism, how many ksqlDB servers can be run without having idle servers?

- A. As many as the company wants.
- B. 10
- C. 5
- D. 3

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The maximum ksqlDB parallelism depends on the number of topic partitions.Idle servers will consume a small amount of resource. For example, if there are 10 ksqlDB servers and you run a query against a 5 partition input topic, only 5 servers perform the actual work, but the other 5 will run an “idle“ query.Further reading: ksqlDB Concepts.

**Detailed explanation of each option:**

1. ❌ **A. As many as the company wants.**  
   **Incorrect**.

2. ❌ **B. 10**  
   **Incorrect**.

3. ✅ **C. 5**  
   **Correct**.

4. ❌ **D. 3**  
   **Incorrect**.

</details>

## Question 41 (Kafka Core Concepts):
What‘s the main advantage of Kafka‘s pub / sub message communication model over classical request / response (point-to-point) systems?

- A. Scalability
- B. Reliability
- C. Decoupling
- D. Performance

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In the request / reply messaging model, the message sender sends a message on one queue, and then it waits for the response from the receiver. with this model, the send cares about the message status thats it received or not yet.The publish / subscribe messaging or normally called pub / sub messaging is a form of asynchronous. In this domain, the message producers are called publishers and the message consumers are called subscribers. The publisher produces messages to a topic then all subscribers which subscribed to that topic will receive the sending messages and consume them.A difference is in the point-to-point model, the message sender must know the receiver but in the publish / subscribe model the message publishers do not need to know where the message will be consumed. This characteristic provides a high decoupling for the application when applying the pub / sub message model.

**Detailed explanation of each option:**

1. ❌ **A. Scalability**  
   **Incorrect**.

2. ❌ **B. Reliability**  
   **Incorrect**.

3. ✅ **C. Decoupling**  
   **Correct**.

4. ❌ **D. Performance**  
   **Incorrect**.

</details>

## Question 42 (Kafka Setup and Operations):
Which of the following choices is best practice when it comes to Kafka security concepts?

- A. Create one principal per application and give each principal only the ACLs it requires and no more.
- B. Use fine-grained Access Control Lists for authentication to allow only specific users to connect to Kafka.
- C. Disable SSL for encryption of traffic as it reduces the overall client performance.
- D. Create one custom user with a random generated password and send the credentials to specific users only.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

By default, there is no encryption or authentication, nor are ACLs configured. Any client can communicate to Kafka brokers using the PLAINTEXT port. It is critical that access using this port is restricted to trusted clients only. Network segmentation and / or authorization ACLs can be used to restrict access to trusted IPs in such cases. If neither is used, then the cluster is wide open and can be accessed by anyone. While non-secured clusters are supported, as are a mix of authenticated, unauthenticated, encrypted and non-encrypted clients, it is recommended to secure the components in your deployment. For authorization it‘s a best practice to create one principal per application and give each principal only the ACLs it requires and no more. Note: ACLs are used for authorization, not for authentication. Further reading: Security Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Create one principal per application and give each principal only the ACLs it requires and no more.**  
   **Correct**.

2. ❌ **B. Use fine-grained Access Control Lists for authentication to allow only specific users to connect to Kafka.**  
   **Incorrect**.

3. ❌ **C. Disable SSL for encryption of traffic as it reduces the overall client performance.**  
   **Incorrect**.

4. ❌ **D. Create one custom user with a random generated password and send the credentials to specific users only.**  
   **Incorrect**.

</details>

## Question 43 (Kafka Internals):
A client connects to a broker in the cluster and sends a fetch request for a partition in a topic. If it gets the exception “NotLeaderForPartitionException“ in the response, how does the client handle this situation?

- A. The client sends a metadata request to the same broker for the topic and selects the broker hosting the leader replica.
- B. The client sends a fetch request to each broker in the topic until it finds the broker hosting the leader replica.
- C. The client sends a metadata request to Zookeeper for the topic and selects the broker hosting the leader replica.
- D. The client gets the broker id from Zookeeper that is hosting the leader replica for the topic and sends the request right to this broker.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In case the consumer has the wrong leader of a partition, it will issue a metadata request. The Metadata request can be handled by any node, so clients know afterwards which broker are the designated leader for the topic partitions. The response contains metadata for each partition, with partitions grouped together by topic: – Leader: The node id of the Kafka broker currently acting as leader for this partition. If no leader exists because we are in the middle of a leader election this id will be -1. – Replicas: The set of alive nodes that currently acts as slaves for the leader for this partition. – ISR: The set subset of the replicas that are “caught up“ to the leader. – Broker: The node id, hostname, and port information for a Kafka broker. Note: Produce and consume requests can only be sent to the node hosting partition leader.

**Detailed explanation of each option:**

1. ✅ **A. The client sends a metadata request to the same broker for the topic and selects the broker hosting the leader replica.**  
   **Correct**.

2. ❌ **B. The client sends a fetch request to each broker in the topic until it finds the broker hosting the leader replica.**  
   **Incorrect**.

3. ❌ **C. The client sends a metadata request to Zookeeper for the topic and selects the broker hosting the leader replica.**  
   **Incorrect**.

4. ❌ **D. The client gets the broker id from Zookeeper that is hosting the leader replica for the topic and sends the request right to this broker.**  
   **Incorrect**.

</details>

## Question 44 (Kafka Consumers):
A company is building a consumer application that processes events from a Kafka topic. What is the most important metric the company should monitor to ensure real-time processing?

- A. fetch-total
- B. records-per-request-avg
- C. bytes-consumed-total
- D. records-lag-max

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The most important consumer fetch metric to ensure real-time-processing is records-lag-max.It‘s the maximum lag in terms of number of records for any partition (number of messages behind the broker).Further reading: Consumer Metrics.

**Detailed explanation of each option:**

1. ❌ **A. fetch-total**  
   **Incorrect**.

2. ❌ **B. records-per-request-avg**  
   **Incorrect**.

3. ❌ **C. bytes-consumed-total**  
   **Incorrect**.

4. ✅ **D. records-lag-max**  
   **Correct**.

</details>

## Question 45 (Kafka Setup and Operations):
By default, Kafka ships with no authentication. Which of the following authentication mechanisms and protocols can be used with the Confluent Platform to enable authentication for Kafka brokers?

- A. mTLS
- B. ACLs
- C. HTTP Basic Auth
- D. SASL/PLAIN

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

Confluent Platform supports the following authentication mechanisms and protocols for Kafka brokers: SASL: SASL (Simple Authentication Security Layer) is a framework that provides developers of applications and shared libraries with mechanisms for authentication, data integrity-checking, and encryption. The supported SASL mechanisms are: – SASL using JAAS Kafka uses the Java Authentication and Authorization Service (JAAS) for SASL configuration. You must provide JAAS configurations for all SASL authentication mechanisms. This topic explains how to configure JAAS for SASL. – SASL/GSSAPI (Kerberos) SASL/GSSAPI uses your Kerberos or Active Directory server for authentication. – SASL/OAUTHBEARER Only suitable for use in non-production Kafka installations, SASL/OAUTHBEARER enables the use the OAuth 2 Authorization framework in a SASL context to create and validate unsecured JSON web tokens for authentication. – SASL/PLAIN SASL/PLAIN uses a simple username and password for authentication. – SASL/SCRAM SASL/SCRAM uses usernames and passwords stored in ZooKeeper. Credentials are created during installation. – Delegation Tokens (SASL/SSL) Performs authentication based on delegation tokens that use a lightweight authentication mechanism that you can use to complement existing SASL/SSL methods. Delegation tokens are shared secrets between Kafka brokers and clients. – LDAP Performs client authentication with LDAP (or AD) across all of your Kafka clusters that use SASL/PLAIN. mTLS: With mTLS (mutual TLS) authenticationalso known as “two-way authentication“  both Kafka clients and servers use TLS certificates to verify each other‘s identities to ensure that traffic is secure and trusted in both directions. HTTP Basic Auth: You can use HTTP Basic Authentication to authenticate with the Admin REST APIs using a username and password pair, which are presented to the REST Proxy server using the Authorization HTTP header. SSL: You can configure SSL for encryption, but you can also configure SSL for authentication using SSL certificates. Note: ACLs (Access Control Lists) or used for authorization, not for authentication. Further reading: Authentication Methods.

**Detailed explanation of each option:**

1. ✅ **A. mTLS**  
   **Correct**.

2. ❌ **B. ACLs**  
   **Incorrect**.

3. ✅ **C. HTTP Basic Auth**  
   **Correct**.

4. ✅ **D. SASL/PLAIN**  
   **Correct**.

</details>

## Question 46 (Kafka Internals):
A company uses log compaction for their production topic. What happens if someone sends messages to this topic with a key and a null value?

- A. The producer will throw a runtime exception.
- B. The broker will delete all messages for this specific key upon cleanup.
- C. A consumer cannot consume messages with a null value and will throw a runtime exception.
- D. Messages with a null value get ignored by Kafka by default.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A record with the same key from the record we want to delete is produced to the same topic and partition with a null payload. These records are called tombstones. A null payload is a payload with 0 bytes and it‘s possible to produce or consume null payloads in Kafka. Because the company uses log compaction, this tells Kafka to delete old records with the same key and keep only the most recent one in a topic partition. Log compaction also removes keys with null values completely. Note: Log compaction is not done immediately, and the time it takes to compact the log will depend on how the topic is configured, the cluster and the processing power of the cluster.

**Detailed explanation of each option:**

1. ❌ **A. The producer will throw a runtime exception.**  
   **Incorrect**.

2. ✅ **B. The broker will delete all messages for this specific key upon cleanup.**  
   **Correct**.

3. ❌ **C. A consumer cannot consume messages with a null value and will throw a runtime exception.**  
   **Incorrect**.

4. ❌ **D. Messages with a null value get ignored by Kafka by default.**  
   **Incorrect**.

</details>

## Question 47 (Stream Processing):
Which of the following options best describes a requirement for data co-partitioning using Kafka Streams joins?

- A. The input topics of the join must have the same number of messages stored.
- B. The input topics of the join must have the same number of partitions.
- C. The input topics of the join must have the same topic configurations.
- D. The input topics of the join must have the same replication factor.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

When joining streams or tables input data must be co-partitioned. This ensures that input records with the same key, from both sides of the join, are delivered to the same stream task during processing. It is the responsibility of the user to ensure data co-partitioning when joining. Data co-partitioning is required because KStream-KStream, KTable-KTable, and KStream-KTable joins are performed based on the keys of records (e. g., leftRecord.key == rightRecord.key). The requirements for data co-partitioning are: – The input topics of the join (left side and right side) must have the same number of partitions. – All applications that write to the input topics must have the same partitioning strategy so that records with the same key are delivered to same partition number. Important note: If possible, consider using global tables (GlobalKTable) for joining because they do not require data co-partitioning. Further reading: Joining Concepts.

**Detailed explanation of each option:**

1. ❌ **A. The input topics of the join must have the same number of messages stored.**  
   **Incorrect**.

2. ✅ **B. The input topics of the join must have the same number of partitions.**  
   **Correct**.

3. ❌ **C. The input topics of the join must have the same topic configurations.**  
   **Incorrect**.

4. ❌ **D. The input topics of the join must have the same replication factor.**  
   **Incorrect**.

</details>

## Question 48 (Kafka Producers):
Which of the following producer configurations can be used to increase the chances of batching messages?

- A. acks=all
- B. max.request.size=1048576
- C. linger.ms=10
- D. batch.size=32768

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

With batching strategy of Kafka producers, you can batch messages going to the same partition, which means they collect multiple messages to send together in a single request. The most important step you can take to optimize throughput is to tune the producer batching to increase the batch size and the time spent waiting for the batch to populate with messages. Larger batch sizes result in fewer requests, which reduces load on producers and the broker CPU overhead to process each request.linger.ms is the number of milliseconds a producer is willing to wait before sending a batch out (defaults to 0). By introducing some lag, we increase the changes of messages being sent together in a batch. If the batch is full (batch.size) before the end of linger.ms period, it will be sent to Kafka right away.Further reading: Batching Messages.

**Detailed explanation of each option:**

1. ❌ **A. acks=all**  
   **Incorrect**.

2. ❌ **B. max.request.size=1048576**  
   **Incorrect**.

3. ✅ **C. linger.ms=10**  
   **Correct**.

4. ❌ **D. batch.size=32768**  
   **Incorrect**.

</details>

## Question 49 (Kafka Setup and Operations):
Which Kafka CLI script should you use to produce to a topic?

- A. bin/kafka-console-consumer.sh
- B. bin/kafka-producer.sh
- C. bin/kafka-topics.sh
- D. bin/kafka-console-producer.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The kafka-console-producer tool is used to write messages to a topic in a text based format. To start producing messages to a topic test_topic, you need to run the tool and specify a server as well as the topic: bin/kafka-console-producer.sh –bootstrap-server 127.0.0.1:9092 –topic test_topic Once the tool is running you can start typing messages to produce to the topic: >my first message >my second message >… Further reading: Producer Example.

**Detailed explanation of each option:**

1. ❌ **A. bin/kafka-console-consumer.sh**  
   **Incorrect**.

2. ❌ **B. bin/kafka-producer.sh**  
   **Incorrect**.

3. ❌ **C. bin/kafka-topics.sh**  
   **Incorrect**.

4. ✅ **D. bin/kafka-console-producer.sh**  
   **Correct**.

</details>

## Question 50 (Programming & Serialization):
Using the Confluent Schema Registry, where are all schemas stored?

- A. In the Confluent Control Center.
- B. In the Schema Registry filesystem.
- C. In the ksqlDB _schemas table.
- D. In the _schemas Kafka topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka is used as Schema Registry storage backend. The special Kafka topic (default _schemas), with a single partition, is used as a highly available write ahead log. All schemas, subject / version and ID metadata, and compatibility settings are appended as messages to this log.A Schema Registry instance therefore both produces and consumes messages under the _schemas topic.Further reading: Schema Registry Backend.

**Detailed explanation of each option:**

1. ❌ **A. In the Confluent Control Center.**  
   **Incorrect**.

2. ❌ **B. In the Schema Registry filesystem.**  
   **Incorrect**.

3. ❌ **C. In the ksqlDB _schemas table.**  
   **Incorrect**.

4. ✅ **D. In the _schemas Kafka topic.**  
   **Correct**.

</details>

## Question 51 (Kafka Connect):
Which of the following options best describes Kafka Connect?

- A. Kafka Connect is a database purpose-built to help developers create stream processing applications on top of Apache Kafka.
- B. Kafka Connect provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas.
- C. Kafka Connect is a client library for building applications and microservices, where the input and output data are stored in an Kafka cluster.
- D. Kafka Connect works as a centralized data hub for simple data integration between databases, key-value stores, search indexes, and file systems.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other data systems. It makes it simple to quickly define connectors that move large data sets into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing with low latency. An export connector can deliver data from Kafka topics into secondary indexes like Elasticsearch or into batch systems such as Hadoop for offline analysis.You can use SourceConnectors for getting your data into Kafka and SinkConnectors to get your data out of Kafka.Further reading: Kafka Connect Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect is a database purpose-built to help developers create stream processing applications on top of Apache Kafka.**  
   **Incorrect**.

2. ❌ **B. Kafka Connect provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas.**  
   **Incorrect**.

3. ❌ **C. Kafka Connect is a client library for building applications and microservices, where the input and output data are stored in an Kafka cluster.**  
   **Incorrect**.

4. ✅ **D. Kafka Connect works as a centralized data hub for simple data integration between databases, key-value stores, search indexes, and file systems.**  
   **Correct**.

</details>

## Question 52 (Kafka Consumers):
Which of the following property should be configured to aim for a high throughput consumer application?

- A. heartbeat.interval.ms
- B. fetch.max.bytes
- C. group.id
- D. fetch.min.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

A way to optimize for consumer throughput is to adjust how much data consumers receive from each fetch from the leader broker. You can increase how much data the consumers get from the leader for each fetch request by increasing the configuration parameter fetch.min.bytes. This parameter sets the minimum number of bytes expected for a fetch response from a consumer. Increasing this also reduces the number of fetch requests made, reducing the broker CPU overhead to process each fetch, thereby also improving throughput.Assuming the application allows it, use also consumer groups with multiple consumers to parallelize consumption. Parallelizing consumption may improve throughput because multiple consumers can balance the load, processing multiple partitions simultaneously.Further reading: Optimizing for Throughput.

**Detailed explanation of each option:**

1. ❌ **A. heartbeat.interval.ms**  
   **Incorrect**.

2. ❌ **B. fetch.max.bytes**  
   **Incorrect**.

3. ❌ **C. group.id**  
   **Incorrect**.

4. ✅ **D. fetch.min.bytes**  
   **Correct**.

</details>

## Question 53 (Kafka Internals):
In Kafka, how many leaders can each topic partition have?

- A. Exactly one leader.
- B. A partition only has followers.
- C. As many as there are brokers in the cluster.
- D. As many as there are partitions for the topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Every topic partition has exactly one partition leader which handles all the read / write requests of that partition. If replication factor is greater than 1, the additional partition replications acts as partition followers. Kafka guarantees every partition replica resides on a different broker (whether if it is the leader or a follower), so maximum replication factor is the brokers number. Every partition follower is reading messages from the partition leader (acts like a kind of consumer) and does not serve any consumers of that partition (only the partition leader serves read / writes). Further reading: Replication.

**Detailed explanation of each option:**

1. ✅ **A. Exactly one leader.**  
   **Correct**.

2. ❌ **B. A partition only has followers.**  
   **Incorrect**.

3. ❌ **C. As many as there are brokers in the cluster.**  
   **Incorrect**.

4. ❌ **D. As many as there are partitions for the topic.**  
   **Incorrect**.

</details>

## Question 54 (Kafka Setup and Operations):
A company configured a Kafka cluster with the parameters –log.retention.hours = 200, –log.retention.minutes = 200 and –log.retention.ms = 200. With this configuration, how long will log data be retained before old log segments will be discarded to free up space?

- A. 200 seconds
- B. 200 hours
- C. 200 milliseconds
- D. 200 minutes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

If more than one similar config is specified, the smaller unit size will take precedence.– log.retention.hours: The number of hours to keep a log file before deleting it (in hours), tertiary to log.retention.ms property.– log.retention.minutes: The number of minutes to keep a log file before deleting it (in minutes), secondary to log.retention.ms property. If not set, the value in log.retention.hours is used.– log.retention.ms: The number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. If set to -1, no time limit is applied.

**Detailed explanation of each option:**

1. ❌ **A. 200 seconds**  
   **Incorrect**.

2. ❌ **B. 200 hours**  
   **Incorrect**.

3. ✅ **C. 200 milliseconds**  
   **Correct**.

4. ❌ **D. 200 minutes**  
   **Incorrect**.

</details>

## Question 55 (Programming & Serialization):
After a FORWARD schema evolution, which order of upgrading producer and consumer clients should you prefer?

- A. Upgrade consumers first.
- B. Upgrade producers first.
- C. You can upgrade the producers and consumers independently.
- D. You cannot upgrade your client after a schema evolution.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The configured compatibility type has an implication on the order for upgrading client applications, i. e., the producers using schemas to write events to Kafka and the consumers using schemas to read events from Kafka.FORWARD or FORWARD_TRANSITIVE schema evolution: There is no assurance that consumers using the new schema can read data produced using older schemas. Therefore, first upgrade all producers to using the new schema and make sure the data already produced using the older schemas are not available to consumers, then upgrade the consumers.Further reading: Schema Evolution and Compatibility.

**Detailed explanation of each option:**

1. ❌ **A. Upgrade consumers first.**  
   **Incorrect**.

2. ✅ **B. Upgrade producers first.**  
   **Correct**.

3. ❌ **C. You can upgrade the producers and consumers independently.**  
   **Incorrect**.

4. ❌ **D. You cannot upgrade your client after a schema evolution.**  
   **Incorrect**.

</details>

## Question 56 (Kafka Internals):
Which of the following options is true about log compaction?

- A. Log compaction re-orders messages based on key hashes.
- B. Log compaction changes the message offsets.
- C. Log compaction does not remove data from the active segment.
- D. Log compaction prevents from having duplicate data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Log Compaction ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition. It addresses use cases and scenarios such as restoring state after application crashes or system failure, or reloading caches after application restarts during operational maintenance. Some important notes about log compaction are: – Offsets of messages are immutable, they never change. Offsets are just skipped if a message is missing. – Any consumer that is reading from the tail of a log (most current data) will still see all the messages sent to the topic, because log compaction never touches the active segment. Note that compaction only guarantees the last value per key is kept — it does not deduplicate messages in general, so option D is false. – Deleted records can still be seen by consumers for a period of “delete.retention.ms“. – Log compaction does not re-order data, it only removes some messages. Further reading: Kafka Compaction.

**Detailed explanation of each option:**

1. ❌ **A. Log compaction re-orders messages based on key hashes.**  
   **Incorrect**.

2. ❌ **B. Log compaction changes the message offsets.**  
   **Incorrect**.

3. ✅ **C. Log compaction does not remove data from the active segment.**  
   **Correct**.

4. ❌ **D. Log compaction prevents from having duplicate data.**  
   **Incorrect**.

</details>

## 🚫 Question 57 (Kafka Setup and Operations):
Running Kafka in production, how much memory should a machine at least have as a decent choice for storing and caching messages?

- A. 8 GB
- B. 16 GB
- C. 64 GB
- D. 32 GB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka relies heavily on the filesystem for storing and caching messages. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel‘s pagecache.A machine with 64 GB of RAM is a decent choice, but 32 GB machines are not uncommon. Less than 32 GB tends to be counterproductive (you end up needing many, many small machines).Further reading: Production Deployment.

**Detailed explanation of each option:**

1. ❌ **A. 8 GB**  
   **Incorrect**.

2. ❌ **B. 16 GB**  
   **Incorrect**.

3. ❌ **C. 64 GB**  
   **Incorrect**.

4. ✅ **D. 32 GB**  
   **Correct**.

</details>
