## 🚫 Question 1 (Kafka Ecosystem):
A company deployed a Kafka cluster on 10 brokers. The production topic has a replication factor of 3 and 5 topic partitions. Because most of the developers are very familiar with SQL, the company decided to use ksqlDB to process data using intuitive SQL-like syntax. For maximum parallelism, how many ksqlDB servers can be run without having idle servers?

- A. 10
- B. As many as the company wants.
- C. 3
- D. 5

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The maximum ksqlDB parallelism depends on the number of topic partitions. Idle servers will consume a small amount of resource. For example, if there are 10 ksqlDB servers and you run a query against a 5 partition input topic, only 5 servers perform the actual work, but the other 5 will run an “idle“ query. Further reading: ksqlDB Concepts.

**Detailed explanation of each option:**

1. ❌ **A. 10**  
   **Incorrect**.

2. ❌ **B. As many as the company wants.**  
   **Incorrect**.

3. ❌ **C. 3**  
   **Incorrect**.

4. ✅ **D. 5**  
   **Correct**.

</details>

## 🚫 Question 2 (Kafka Ecosystem):
Which of the following data formats are supported by ksqlDB?

- A. JSON
- B. XML
- C. DELIMITED
- D. Avro message values

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. JSON**  
   **Correct**.

2. ❌ **B. XML**  
   **Incorrect**.

3. ✅ **C. DELIMITED**  
   **Correct**.

4. ✅ **D. Avro message values**  
   **Correct**.

</details>

## Question 3 (Kafka Internals):
A client connects to a broker in the cluster and sends a fetch request for a partition in a topic. If it gets the exception “NotLeaderForPartitionException“ in the response, how does the client handle this situation?

- A. The client gets the broker id from Zookeeper that is hosting the leader replica for the topic and sends the request right to this broker.
- B. The client sends a fetch request to each broker in the topic until it finds the broker hosting the leader replica.
- C. The client sends a metadata request to the same broker for the topic and selects the broker hosting the leader replica.
- D. The client sends a metadata request to Zookeeper for the topic and selects the broker hosting the leader replica.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In case the consumer has the wrong leader of a partition, it will issue a metadata request. The Metadata request can be handled by any node, so clients know afterwards which broker are the designated leader for the topic partitions. The response contains metadata for each partition, with partitions grouped together by topic: – Leader: The node id of the Kafka broker currently acting as leader for this partition. If no leader exists because we are in the middle of a leader election this id will be -1. – Replicas: The set of alive nodes that currently acts as slaves for the leader for this partition. – ISR: The set subset of the replicas that are “caught up“ to the leader. – Broker: The node id, hostname, and port information for a Kafka broker. Note: Produce and consume requests can only be sent to the node hosting partition leader.

**Detailed explanation of each option:**

1. ❌ **A. The client gets the broker id from Zookeeper that is hosting the leader replica for the topic and sends the request right to this broker.**  
   **Incorrect**.

2. ❌ **B. The client sends a fetch request to each broker in the topic until it finds the broker hosting the leader replica.**  
   **Incorrect**.

3. ✅ **C. The client sends a metadata request to the same broker for the topic and selects the broker hosting the leader replica.**  
   **Correct**.

4. ❌ **D. The client sends a metadata request to Zookeeper for the topic and selects the broker hosting the leader replica.**  
   **Incorrect**.

</details>

## Question 4 (Kafka Consumers):
What happens if two consumers have the same group id and subscribe to the same topic? 

- A. Each consumer will be assigned all of the partitions in the topic.
- B. One consumer will be assigned all of the partitions in the topic and one consumer will be idle.
- C. Each consumer will be assigned one of the partitions in the topic.
- D. Each consumer will be assigned a subset of the partitions in the topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The group.id is a unique string that identifies the consumer group a consumer belongs to. This property is required if the consumer uses either the group management functionality by using subscribe(topic) or the Kafka-based offset management strategy. The basic idea is that if two consumers have the same group id and subscribe to the same topic, each will be assigned a subset of the partitions in the topic and will therefore only read a subset of the messages individually (but all the messages will be read by the group as a whole). If you need a consumer to see, on its own, every single message in the topics it is subscribed to – it will need a unique group.id. Further reading: Consumer Groups.

**Detailed explanation of each option:**

1. ❌ **A. Each consumer will be assigned all of the partitions in the topic.**  
   **Incorrect**.

2. ❌ **B. One consumer will be assigned all of the partitions in the topic and one consumer will be idle.**  
   **Incorrect**.

3. ❌ **C. Each consumer will be assigned one of the partitions in the topic.**  
   **Incorrect**.

4. ✅ **D. Each consumer will be assigned a subset of the partitions in the topic.**  
   **Correct**.

</details>

## Question 5 (Kafka Consumers):
Which API can be used to shutdown a consumer from another thread? 

- A. flush()
- B. close()
- C. shutdown()
- D. wakeup()

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. The only exception to this rule is wakeup(), which can safely be used from an external thread to interrupt an active operation. In this case, a WakeupException will be thrown from the thread blocking on the operation. This can be used to shutdown the consumer from another thread. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ❌ **A. flush()**  
   **Incorrect**.

2. ❌ **B. close()**  
   **Incorrect**.

3. ❌ **C. shutdown()**  
   **Incorrect**.

4. ✅ **D. wakeup()**  
   **Correct**.

</details>

## Question 6 (Kafka Core Concepts):
Which of the following options are true about topics in Kafka? 

- A. You can have as many topics as you want.
- B. A topic is identified by its unique id.
- C. The number of topics is limited to 500.
- D. Topics are always multi-producer and multi-subscriber.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

In Kafka, events are organized and durably stored in topics. – Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. – Topics have no quota and you can create as many topics as you want. – A topic is identified by its name (not ID) and topics are split into partitions.

**Detailed explanation of each option:**

1. ✅ **A. You can have as many topics as you want.**  
   **Correct**.

2. ❌ **B. A topic is identified by its unique id.**  
   **Incorrect**.

3. ❌ **C. The number of topics is limited to 500.**  
   **Incorrect**.

4. ✅ **D. Topics are always multi-producer and multi-subscriber.**  
   **Correct**.

</details>

## Question 7 (Kafka Consumers):
Which offset commit strategy should be used in an at-least once consuming scenario?

- A. Do not commit the offsets in Kafka, as this will be handled automatically.
- B. Commit the offsets in Kafka, during processing the data.
- C. Commit the offsets in Kafka, after processing the data.
- D. Commit the offsets in Kafka, before processing the data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

At-least once guarantee means you will definitely receive and process every message, but you may process some messages additional times in the face of a failure. For a consumer application at-least once processing means the consumer group receives a batch of messages from Kafka, transforms these and writes the results to a database. The consumer application has enable.auto.commit set to false and is programmed to commit their offsets back to Kafka once the database write succeeds. If the consumer fails after writing the data to the database but before saving the offsets back to Kafka, it will reprocess the same records next time it runs and save them to the database once more.

**Detailed explanation of each option:**

1. ❌ **A. Do not commit the offsets in Kafka, as this will be handled automatically.**  
   **Incorrect**.

2. ❌ **B. Commit the offsets in Kafka, during processing the data.**  
   **Incorrect**.

3. ✅ **C. Commit the offsets in Kafka, after processing the data.**  
   **Correct**.

4. ❌ **D. Commit the offsets in Kafka, before processing the data.**  
   **Incorrect**.

</details>

## Question 8 (Kafka Setup and Operations):
Using Kafka security features, how can you allow a specific user to read and write to the topic “test-topic“? 

- A. Add an ACL with the --allow-principal and --allow-host properties for read and write operations.
- B. Use SASL as the default authentication service.
- C. Set the property “security.inter.broker.protocol“ to SSL and allow the specific user to connect to the broker.
- D. Enable mTLS authentication between the ZooKeeper servers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Apache Kafka ships with a pluggable, out-of-the-box Authorizer implementation that uses ZooKeeper to store all the ACLs. It is important to set ACLs because otherwise access to resources is limited to super users when an Authorizer is configured. The default behavior is that if a resource has no associated ACLs, then no one is allowed to access the resource, except super users. Access Control Lists (ACLs) provide important authorization controls for your enterprise‘s Kafka cluster data. The following command can be used to set the required ACLs to allow a specific user “Bob“ to read and write to the topic “test-topic“ from host “test-host“: bin/kafka-acls.sh –authorizer-properties zookeeper.connect=localhost:2181 –add –allow-principal User:Bob –allow-host test-host –operation read –operation write –topic test-topic Note: It‘s best practice to create one principal per application and give each principal only the ACLs it requires and no more. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Add an ACL with the --allow-principal and --allow-host properties for read and write operations.**  
   **Correct**.

2. ❌ **B. Use SASL as the default authentication service.**  
   **Incorrect**.

3. ❌ **C. Set the property “security.inter.broker.protocol“ to SSL and allow the specific user to connect to the broker.**  
   **Incorrect**.

4. ❌ **D. Enable mTLS authentication between the ZooKeeper servers.**  
   **Incorrect**.

</details>

## Question 9 (Stream Processing):
Which processing guarantees does Kafka Streams support? 

- A. exactly-once processing
- B. at-most-once processing
- C. at-least-once processing

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. exactly-once processing**  
   **Correct**.

2. ❌ **B. at-most-once processing**  
   **Incorrect**.

3. ✅ **C. at-least-once processing**  
   **Correct**.

</details>

## Question 10 (Programming & Serialization):
After a FORWARD schema evolution, which order of upgrading producer and consumer clients should you prefer? 

- A. Upgrade producers first.
- B. Upgrade consumers first.
- C. You can upgrade the producers and consumers independently.
- D. You cannot upgrade your client after a schema evolution.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The configured compatibility type has an implication on the order for upgrading client applications, i. e., the producers using schemas to write events to Kafka and the consumers using schemas to read events from Kafka. FORWARD or FORWARD_TRANSITIVE schema evolution: There is no assurance that consumers using the new schema can read data produced using older schemas. Therefore, first upgrade all producers to using the new schema and make sure the data already produced using the older schemas are not available to consumers, then upgrade the consumers.

**Detailed explanation of each option:**

1. ✅ **A. Upgrade producers first.**  
   **Correct**.

2. ❌ **B. Upgrade consumers first.**  
   **Incorrect**.

3. ❌ **C. You can upgrade the producers and consumers independently.**  
   **Incorrect**.

4. ❌ **D. You cannot upgrade your client after a schema evolution.**  
   **Incorrect**.

</details>

## Question 11 (Kafka Consumers):
Which offset commit strategy should be used in an at-most once consuming scenario? 

- A. Do not commit the offsets in Kafka, as this will be handled automatically.
- B. Commit the offsets in Kafka, during processing the data.
- C. Commit the offsets in Kafka, after processing the data.
- D. Commit the offsets in Kafka, before processing the data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

At-most once guarantee means the message will be processed exactly once, or not at all. For a consumer application at-most once processing means the consumer group receives a batch of messages from Kafka, transforms these and writes the results to a database. The consumer application has enable.auto.commit set to false and is programmed to commit their offsets back to Kafka prior to writing to the database. If the consumer fails after saving the offsets back to Kafka but before writing the data to the database, it will skip these records next time it runs and data will be lost. Further reading: Offset Management.

**Detailed explanation of each option:**

1. ❌ **A. Do not commit the offsets in Kafka, as this will be handled automatically.**  
   **Incorrect**.

2. ❌ **B. Commit the offsets in Kafka, during processing the data.**  
   **Incorrect**.

3. ❌ **C. Commit the offsets in Kafka, after processing the data.**  
   **Incorrect**.

4. ✅ **D. Commit the offsets in Kafka, before processing the data.**  
   **Correct**.

</details>

## Question 12 (Programming & Serialization):
Which of the following options best describes integration testing?

- A. Integration tests verify that end-to-end tests with other services work as expected.
- B. Integration tests verify that isolated functional blocks of code work as expected.
- C. Integration tests verify that development environments behave as expected.
- D. Integration tests verify that production deployments work as expected.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Unit testing, integration testing, and schema compatibility are all important steps in building resilient applications in a CI / CD pipeline. Integration testing is the phase in software testing in which individual software modules are combined and tested as a group. Integration testing is conducted to evaluate the compliance of a system or component with specified functional requirements. It occurs after unit testing and before validation testing. Further reading: Application Testing.

**Detailed explanation of each option:**

1. ✅ **A. Integration tests verify that end-to-end tests with other services work as expected.**  
   **Correct**.

2. ❌ **B. Integration tests verify that isolated functional blocks of code work as expected.**  
   **Incorrect**.

3. ❌ **C. Integration tests verify that development environments behave as expected.**  
   **Incorrect**.

4. ❌ **D. Integration tests verify that production deployments work as expected.**  
   **Incorrect**.

</details>

## Question 13 (Kafka Internals):
Which of the following options is true about log compaction? 

- A. Log compaction re-orders messages based on key hashes.
- B. Log compaction does not remove data from the active segment.
- C. Log compaction prevents from having duplicate data.
- D. Log compaction changes the message offsets.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Log Compaction ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition. It addresses use cases and scenarios such as restoring state after application crashes or system failure, or reloading caches after application restarts during operational maintenance. Some important notes about log compaction are: – Offsets of messages are immutable, they never change. Offsets are just skipped if a message is missing. – Any consumer that is reading from the tail of a log (most current data) will still see all the messages sent to the topic. There will be no log compaction at the active segment. Therefore compaction does not prevent from duplicate data. – Deleted records can still be seen by consumers for a period of “delete.retention.ms“. – Log compaction does not re-order data, it only removes some messages. Further reading: Kafka Compaction.

**Detailed explanation of each option:**

1. ❌ **A. Log compaction re-orders messages based on key hashes.**  
   **Incorrect**.

2. ✅ **B. Log compaction does not remove data from the active segment.**  
   **Correct**.

3. ❌ **C. Log compaction prevents from having duplicate data.**  
   **Incorrect**.

4. ❌ **D. Log compaction changes the message offsets.**  
   **Incorrect**.

</details>

## Question 14 (Kafka Consumers):
A company uses a consumer application to do complex big data calculations for the Kafka input data before writing the outputs into a data warehouse. The calculations take about 9 to 10 minutes to finish, but the consumer application rebalances even though the calculation is still running. What‘s the best solution to solve this problem? 

- A. Decrease max.poll.interval.ms to 600000.
- B. Decrease session.timeout.ms to 20000.
- C. Increase session.timeout.ms to 20000.
- D. Increase max.poll.interval.ms to 600000.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Once the consumer subscribes to topics, the poll loop handles all details of coordination, partition rebalances, heartbeats, and data fetching, leaving the developer with a clean API that simply returns available data from the assigned partitions. The max.poll.interval.ms configuration is the maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance in order to reassign the partitions to another member. Because the max.poll.interval.ms defaults to 5 minutes (300000 ms), but the processing takes about 9 to 10 minutes to finish we should at least double this value to solve the consumer issue. Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. Decrease max.poll.interval.ms to 600000.**  
   **Incorrect**.

2. ❌ **B. Decrease session.timeout.ms to 20000.**  
   **Incorrect**.

3. ❌ **C. Increase session.timeout.ms to 20000.**  
   **Incorrect**.

4. ✅ **D. Increase max.poll.interval.ms to 600000.**  
   **Correct**.

</details>

## Question 15 (Kafka Internals):
A company uses log compaction for their production topic. What happens if someone sends messages to this topic with a key and a null value?

- A. The producer will throw a runtime exception.
- B. Messages with a null value get ignored by Kafka by default.
- C. The broker will delete all messages for this specific key upon cleanup.
- D. A consumer cannot consume messages with a null value and will throw a runtime exception.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

A record with the same key from the record we want to delete is produced to the same topic and partition with a null payload. These records are called tombstones. A null payload is a payload with 0 bytes and it‘s possible to produce or consume null payloads in Kafka. Because the company uses log compaction, this tells Kafka to delete old records with the same key and keep only the most recent one in a topic partition. Log compaction also removes keys with null values completely. Note: Log compaction is not done immediately, and the time it takes to compact the log will depend on how the topic is configured, the cluster and the processing power of the cluster.

**Detailed explanation of each option:**

1. ❌ **A. The producer will throw a runtime exception.**  
   **Incorrect**.

2. ❌ **B. Messages with a null value get ignored by Kafka by default.**  
   **Incorrect**.

3. ✅ **C. The broker will delete all messages for this specific key upon cleanup.**  
   **Correct**.

4. ❌ **D. A consumer cannot consume messages with a null value and will throw a runtime exception.**  
   **Incorrect**.

</details>

## Question 16 (Kafka Consumers):
The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized. What‘s the only exception to this rule?

- A. Commit offsets returned on the last poll.
- B. Get the metrics kept by the consumer.
- C. Close the consumer.
- D. Wakeup the consumer.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. The only exception to this rule is wakeup(), which can safely be used from an external thread to interrupt an active operation. In this case, a WakeupException will be thrown from the thread blocking on the operation. This can be used to shutdown the consumer from another thread. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ❌ **A. Commit offsets returned on the last poll.**  
   **Incorrect**.

2. ❌ **B. Get the metrics kept by the consumer.**  
   **Incorrect**.

3. ❌ **C. Close the consumer.**  
   **Incorrect**.

4. ✅ **D. Wakeup the consumer.**  
   **Correct**.

</details>

## Question 17 (Kafka Setup and Operations):
In Kafka, if the property “auto.create.topics.enable“ is set to true, what are the circumstances under which a Kafka broker automatically creates a topic?

- A. If a consumer reads a message from the topic.
- B. If a producer sends a message to the topic.
- C. If a client requests metadata for the topic.
- D. If the number of partitions for the topic gets updated.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. If a consumer reads a message from the topic.**  
   **Correct**.

2. ✅ **B. If a producer sends a message to the topic.**  
   **Correct**.

3. ✅ **C. If a client requests metadata for the topic.**  
   **Correct**.

4. ❌ **D. If the number of partitions for the topic gets updated.**  
   **Incorrect**.

</details>

## Question 18 (Programming & Serialization):
Which curl command can be used to fetch a schema by globally unique ID 1? 

- A. curl -X GET http://localhost:8081/ids/1
- B. curl -X GET http://localhost:9092/ids/1
- C. curl -X GET http://localhost:9092/schemas/ids/1
- D. curl -X GET http://localhost:8081/schemas/ids/1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The best way to test the Schema Registry API is to use CURL (command line tool and library for transferring data with URLs) commands. First you need to start Schema Registry and its dependent services ZooKeeper and Kafka. To fetch a schema by globally unique ID 1 you can use the following command: curl -X GET http://localhost:8081/schemas/ids/1 Further reading: API Usage Examples.

**Detailed explanation of each option:**

1. ❌ **A. curl -X GET http://localhost:8081/ids/1**  
   **Incorrect**.

2. ❌ **B. curl -X GET http://localhost:9092/ids/1**  
   **Incorrect**.

3. ❌ **C. curl -X GET http://localhost:9092/schemas/ids/1**  
   **Incorrect**.

4. ✅ **D. curl -X GET http://localhost:8081/schemas/ids/1**  
   **Correct**.

</details>

## Question 19 (Kafka Consumers):
In Kafka, what is the most important consumer configuration? 

- A. heartbeat interval
- B. key deserializer
- C. fetch size
- D. session timeout

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. heartbeat interval**  
   **Incorrect**.

2. ❌ **B. key deserializer**  
   **Incorrect**.

3. ✅ **C. fetch size**  
   **Correct**.

4. ❌ **D. session timeout**  
   **Incorrect**.

</details>

## Question 20 (Kafka Consumers):
Which option is true about a consumer group coordinator in Kafka? 

- A. A group coordinator is one of the brokers.
- B. For every consumer there is one equivalent group coordinator.
- C. A consumer group has exactly two group coordinators.
- D. A group coordinator always is the leader broker.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The group coordinator is nothing but one of the brokers which receives heartbeats from all consumers of a consumer group. Every consumer group has exactly one group coordinator. If a consumer stops sending heartbeats, the coordinator will trigger a rebalance. When a consumer wants to join a consumer group, it sends a JoinGroup request to the group coordinator. The first consumer to join the group becomes the group leader.

**Detailed explanation of each option:**

1. ✅ **A. A group coordinator is one of the brokers.**  
   **Correct**.

2. ❌ **B. For every consumer there is one equivalent group coordinator.**  
   **Incorrect**.

3. ❌ **C. A consumer group has exactly two group coordinators.**  
   **Incorrect**.

4. ❌ **D. A group coordinator always is the leader broker.**  
   **Incorrect**.

</details>

## Question 21 (Kafka Consumers):
Which method can be used for a consumer to read messages from a specific topic?

- A. .subscribe()
- B. .consume()
- C. .read()
- D. .listen()

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The first step to start consuming records is to create a KafkaConsumer instance. Creating a KafkaConsumer is very similar to creating a KafkaProducer – you create a Java Properties instance with the properties you want to pass to the consumer. Once a consumer is created, the next step is to subscribe to one or more topics. The subcribe() method takes a list of topics as a parameter (as a list or with regular expression). For example using a list with a single topic element named test_topic: consumer.subscribe(Collections.singletonList(“test_topic“)); Kafka will deliver each message in the subscribed topics to one process in each consumer group. This is achieved by balancing the partitions between all members in the consumer group so that each partition is assigned to exactly one consumer in the group. Further reading: Consumer Client.

**Detailed explanation of each option:**

1. ✅ **A. .subscribe()**  
   **Correct**.

2. ❌ **B. .consume()**  
   **Incorrect**.

3. ❌ **C. .read()**  
   **Incorrect**.

4. ❌ **D. .listen()**  
   **Incorrect**.

</details>

## Question 22 (Reliable Data Delivery):
How could you guarantee that each message in Kafka will be written to an external system exactly once?

- A. Filtering keys with the Kafka Streams API.
- B. Using the consumer configuration “enable.idempotence=true“.
- C. Writing results to a system that has support for unique keys.
- D. Using record.topic() + record.partition() as the unique message key.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Some applications require not just at-least-once semantics (meaning no data loss), but also exactly-once semantics. While Kafka does not provide full exactly-once support at this time, consumers have few tricks available that allow them to guarantee that each message in Kafka will be written to an external system exactly once. The easiest and probably most common way to do exactly-once is by writing results to a system that has some support for unique keys. This includes all key-value stores, all relational databases, Elasticsearch, and probably many more data stores. When writing results to a system like a relational database or Elasticsearch, either the record itself contains a unique key (this is fairly common), or you can create a unique key using the topic, partition, and offset combination, which uniquely identifies a Kafka record. If you write the record as a value with a unique key, and later you accidentally consume the same record again, you will just write the exact same key and value. The data store will override the existing one, and you will get the same result that you would without the accidental duplicate. This pattern is called idempotent writes and is very common and useful.

**Detailed explanation of each option:**

1. ❌ **A. Filtering keys with the Kafka Streams API.**  
   **Incorrect**.

2. ❌ **B. Using the consumer configuration “enable.idempotence=true“.**  
   **Incorrect**.

3. ✅ **C. Writing results to a system that has support for unique keys.**  
   **Correct**.

4. ❌ **D. Using record.topic() + record.partition() as the unique message key.**  
   **Incorrect**.

</details>

## Question 23 (Kafka Internals):
Which of the following designs of cluster replication should be used in a multi-cluster environment for analytics purposes only?

- A. Active -> Passive replication
- B. Active -> Active replication
- C. Passive -> Passive replication
- D. Passive -> Active replication

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

For Multi-datacenter use cases a replicator can be deployed across clusters and in multiple datacenters. Multi-datacenter deployments enable use-cases such as: – Active -> Active geo-localized deployments: allows users to access a near-by data center to optimize their architecture for low latency and high performance. Replication can be done in both sides and data can be produced and consumed in every cluster. – Active-> Passive disaster recover (DR) deployments: in an event of a partial or complete datacenter disaster, allow failing over applications to use Confluent Platform in a different datacenter. – Active -> Passive centralized analytics: Aggregate data from multiple Apache Kafka clusters into one location for organization-wide analytics. No producers will be used at the replicated cluster, it‘s just for consuming data for analytic purposes. Further reading: Cluster Replication Flows.

**Detailed explanation of each option:**

1. ✅ **A. Active -> Passive replication**  
   **Correct**.

2. ❌ **B. Active -> Active replication**  
   **Incorrect**.

3. ❌ **C. Passive -> Passive replication**  
   **Incorrect**.

4. ❌ **D. Passive -> Active replication**  
   **Incorrect**.

</details>

## Question 24 (Stream Processing):
Which of the following options best describes a requirement for data co-partitioning using Kafka Streams joins?

- A. The input topics of the join must have the same replication factor.
- B. The input topics of the join must have the same topic configurations.
- C. The input topics of the join must have the same number of messages stored.
- D. The input topics of the join must have the same number of partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When joining streams or tables input data must be co-partitioned. This ensures that input records with the same key, from both sides of the join, are delivered to the same stream task during processing. It is the responsibility of the user to ensure data co-partitioning when joining. Data co-partitioning is required because KStream-KStream, KTable-KTable, and KStream-KTable joins are performed based on the keys of records (e. g., leftRecord.key == rightRecord.key). The requirements for data co-partitioning are: – The input topics of the join (left side and right side) must have the same number of partitions. – All applications that write to the input topics must have the same partitioning strategy so that records with the same key are delivered to same partition number. Important note: If possible, consider using global tables (GlobalKTable) for joining because they do not require data co-partitioning. Further reading: Joining Concepts.

**Detailed explanation of each option:**

1. ❌ **A. The input topics of the join must have the same replication factor.**  
   **Incorrect**.

2. ❌ **B. The input topics of the join must have the same topic configurations.**  
   **Incorrect**.

3. ❌ **C. The input topics of the join must have the same number of messages stored.**  
   **Incorrect**.

4. ✅ **D. The input topics of the join must have the same number of partitions.**  
   **Correct**.

</details>

## Question 25 (Kafka Consumers):
What‘s the main way to scale data consumption from a Kafka topic?

- A. Scale your consumer clients vertically by adding more CPUs.
- B. Refactor your topic and add more partitions to it.
- C. Scale the default ConsumerCoordinator horizontally by adding more clients.
- D. Add more consumers to the consumer group.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application. Let‘s take a topic with 5 partitions: – If there is only one consumer in the consumer group, the consumer will consume messages from all 5 topic partitions. – If there are two consumers in the consumer group, one consumer will consume messages from 2 partitions and the other one will consume messages from 3 partitions. – If there are five consumers in the consumer group, then each will read messages from a single partition. – If there are more than five consumers in the consumer group, some of the consumers will be idle and get no messages at all. So the main way to scale data consumption from a Kafka topic is by adding more consumers to a consumer group. It is common for Kafka consumers to do high-latency operations such as writing to a database. In this case, a single consumer can‘t possibly keep up with the rate data flows into the topic, and adding more consumers that share the load by having each consumer own just a subset of the partitions and messages is the main method of scaling. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Scale your consumer clients vertically by adding more CPUs.**  
   **Incorrect**.

2. ❌ **B. Refactor your topic and add more partitions to it.**  
   **Incorrect**.

3. ❌ **C. Scale the default ConsumerCoordinator horizontally by adding more clients.**  
   **Incorrect**.

4. ✅ **D. Add more consumers to the consumer group.**  
   **Correct**.

</details>

## Question 26 (Kafka Consumers):
Which of the following options best describes the concept of rebalancing a consumer group? 

- A. Rebalancing a consumer group re-assigns consumers so that each consumer receives messages from all the available topic partitions.
- B. Rebalancing a consumer group re-assigns partitions so that each consumer receives messages from all the available topic partitions.
- C. Rebalancing a consumer group re-assigns partitions so that each consumer receives a proportional share of the partitions whenever new group members arrive and old members leave.
- D. Rebalancing a consumer group re-assigns consumers so that each consumer group receives a proportional share of the consumers whenever new consumers arrive and old consumers leave.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application. The partitions of all the topics are divided among the consumers in the group. As new group members arrive and old members leave, the partitions are re-assigned so that each member receives a proportional share of the partitions. This is known as rebalancing the group. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Rebalancing a consumer group re-assigns consumers so that each consumer receives messages from all the available topic partitions.**  
   **Incorrect**.

2. ❌ **B. Rebalancing a consumer group re-assigns partitions so that each consumer receives messages from all the available topic partitions.**  
   **Incorrect**.

3. ✅ **C. Rebalancing a consumer group re-assigns partitions so that each consumer receives a proportional share of the partitions whenever new group members arrive and old members leave.**  
   **Correct**.

4. ❌ **D. Rebalancing a consumer group re-assigns consumers so that each consumer group receives a proportional share of the consumers whenever new consumers arrive and old consumers leave.**  
   **Incorrect**.

</details>

## Question 27 (Kafka Core Concepts):
Which of the following options are true for Kafka messages?

- A. Messages from the same producer will always go to the same topic partition.
- B. Messages with keys can be modified.
- C. Messages are immutable.
- D. Messages with the same key will always go to the same topic partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Messages from the same producer will always go to the same topic partition.**  
   **Incorrect**.

2. ❌ **B. Messages with keys can be modified.**  
   **Incorrect**.

3. ✅ **C. Messages are immutable.**  
   **Correct**.

4. ✅ **D. Messages with the same key will always go to the same topic partition.**  
   **Correct**.

</details>

## Question 28 (Kafka Producers):
Which of the following properties should be configured to aim for a high throughput producer application?

- A. linger.ms
- B. compression.type
- C. max.in.flight.requests.per.connection
- D. batch.size

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

To optimize for throughput, producers and consumers must move as much data as possible within a given amount of time. For high throughput, try maximizing the rate at which the data moves. The data rate should be the fastest possible rate. Producer configurations to achieve a high throughput application are: – compression.type: Producers usually send data that is text-based, for example with JSON data. In this case, it is important to apply compression to optimize for throughput. Compression is more effective the bigger the batch of messages being sent to Kafka. Possible values are: lz4 (recommended for performance),snappy, zstd, gzip. – batch.size: With batching strategy of Kafka producers, you can batch messages going to the same partition, which means they collect multiple messages to send together in a single request. The most important step you can take to optimize throughput is to tune the producer batching to increase the batch size and the time spent waiting for the batch to populate with messages. Larger batch sizes result in fewer requests, which reduces load on producers and the broker CPU overhead to process each request. – linger.ms: It‘s the number of milliseconds a producer is willing to wait before sending a batch out (defaults to 0). By introducing some lag, we increase the changes of messages being sent together in a batch. If the batch is full (batch.size) before the end of linger.ms period, it will be sent to Kafka right away. Further reading: Optimizing for Throughput.

**Detailed explanation of each option:**

1. ✅ **A. linger.ms**  
   **Correct**.

2. ✅ **B. compression.type**  
   **Correct**.

3. ❌ **C. max.in.flight.requests.per.connection**  
   **Incorrect**.

4. ✅ **D. batch.size**  
   **Correct**.

</details>

## Question 29 (Kafka Consumers):
What‘s one of the main tasks of the consumer group leader? 

- A. The group leader is one of the consumers in the consumer group and is responsible for sending requests to join the group.
- B. The group leader is one of the consumers in the consumer group and is responsible for assigning a subset of topic partitions to each consumer.
- C. The group leader is one of the consumers in the consumer group and receives heartbeats from all consumers to trigger a rebalance, if one of the consumers isn‘t alive.
- D. The group leader is one of the consumers in the consumer group and is responsible for storing all the consumer offsets to Kafka.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application. When a consumer wants to join a group, it sends a JoinGroup request to the group coordinator (one of the brokers). The first consumer to join the group becomes the group leader (one of the consumers in the consumer group). The leader receives a list of all consumers in the group from the group coordinator (this will include all consumers that sent a heartbeat recently and which are therefore considered alive) and is responsible for assigning a subset of partitions to each consumer. It uses an implementation of PartitionAssignor to decide which partitions should be handled by which consumer. Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. The group leader is one of the consumers in the consumer group and is responsible for sending requests to join the group.**  
   **Incorrect**.

2. ✅ **B. The group leader is one of the consumers in the consumer group and is responsible for assigning a subset of topic partitions to each consumer.**  
   **Correct**.

3. ❌ **C. The group leader is one of the consumers in the consumer group and receives heartbeats from all consumers to trigger a rebalance, if one of the consumers isn‘t alive.**  
   **Incorrect**.

4. ❌ **D. The group leader is one of the consumers in the consumer group and is responsible for storing all the consumer offsets to Kafka.**  
   **Incorrect**.

</details>

## Question 30 (Kafka Producers):
A Kafka producer has the retries property set to 2147483647 to resend any record whose send fails with a potentially transient error. Which of the following additional configurations could potentially change the ordering of records?

- A. enable.idempotence=true
- B. max.in.flight.requests.per.connection=5
- C. enable.idempotence=false
- D. max.in.flight.requests.per.connection=1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Configuring retries for a Kafka producer will cause the client to resend any record whose send fails with a potentially transient error. Note that this retry is no different than if the client resent the record upon receiving the error. Allowing retries without setting max.in.flight.requests.per.connection to 1 will potentially change the ordering of records because if two batches are sent to a single partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first. Note: One exception is the configuration “enable.idempotence=true“ which takes care of the out of ordering case on its own. Further reading: Retries Configuration.

**Detailed explanation of each option:**

1. ❌ **A. enable.idempotence=true**  
   **Incorrect**.

2. ✅ **B. max.in.flight.requests.per.connection=5**  
   **Correct**.

3. ❌ **C. enable.idempotence=false**  
   **Incorrect**.

4. ❌ **D. max.in.flight.requests.per.connection=1**  
   **Incorrect**.

</details>

## Question 31 (Stream Processing):
Which of the following Kafka Streams domain specific language operations are stateful? (Select three)

- A. Reduce
- B. Join
- C. Aggregate
- D. Filter

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

The KStream and KTable interfaces support a variety of transformation operations. Stateful transformations depend on state for processing inputs and producing outputs and require a state store associated with the stream processor. For example, in aggregating operations, a windowing state store is used to collect the latest aggregation results per window. In join operations, a windowing state store is used to collect all of the records received so far within the defined window boundary. After records are grouped by key via groupByKey or groupBy  and thus represented as either a KGroupedStream or a KGroupedTable, they can be transformed: – Aggregate: Aggregates the values of records by the grouped key. – Count: Counts the number of records by the grouped key. – Reduce: Combines the values of records by the grouped key. Streams and Tables can also be joined. All joins are stateful. To learn more about all the join operations, you can check out the Streams Join documentation. Further reading: Streams Stateful Operations.

**Detailed explanation of each option:**

1. ✅ **A. Reduce**  
   **Correct**.

2. ✅ **B. Join**  
   **Correct**.

3. ✅ **C. Aggregate**  
   **Correct**.

4. ❌ **D. Filter**  
   **Incorrect**.

</details>

## Question 32 (Kafka Internals):
If you deploy a Kafka cluster on 4 brokers and the underlying topic has a replication factor of 3 and the number of partitions for that topic are 12, on how many brokers will each partition live?

- A. 2
- B. 3
- C. 4
- D. 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. 2**  
   **Incorrect**.

2. ✅ **B. 3**  
   **Correct**.

3. ❌ **C. 4**  
   **Incorrect**.

4. ❌ **D. 1**  
   **Incorrect**.

</details>

## Question 33 (Programming & Serialization):
Using the Confluent Schema Registry, where are all schemas stored? 

- A. In the Schema Registry filesystem.
- B. In the _schemas Kafka topic.
- C. In the Confluent Control Center.
- D. In the ksqlDB _schemas table.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka is used as Schema Registry storage backend. The special Kafka topic (default _schemas), with a single partition, is used as a highly available write ahead log. All schemas, subject / version and ID metadata, and compatibility settings are appended as messages to this log. A Schema Registry instance therefore both produces and consumes messages under the _schemas topic. Further reading: Schema Registry Backend.

**Detailed explanation of each option:**

1. ❌ **A. In the Schema Registry filesystem.**  
   **Incorrect**.

2. ✅ **B. In the _schemas Kafka topic.**  
   **Correct**.

3. ❌ **C. In the Confluent Control Center.**  
   **Incorrect**.

4. ❌ **D. In the ksqlDB _schemas table.**  
   **Incorrect**.

</details>

## 🚫 Question 34 (Kafka Ecosystem):
Which ksqlDB queries read or write data to Kafka?

- A. CREATE TABLE AS SELECT
- B. COUNT
- C. CREATE STREAM AS SELECT
- D. EXPLAIN

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. CREATE TABLE AS SELECT**  
   **Correct**.

2. ✅ **B. COUNT**  
   **Correct**.

3. ✅ **C. CREATE STREAM AS SELECT**  
   **Correct**.

4. ❌ **D. EXPLAIN**  
   **Incorrect**.

</details>

## Question 35 (Kafka Setup and Operations):
Which of the following choices is best practice when it comes to Kafka security concepts?

- A. Create one custom user with a random generated password and send the credentials to specific users only.
- B. Create one principal per application and give each principal only the ACLs it requires and no more.
- C. Use fine-grained Access Control Lists for authentication to allow only specific users to connect to Kafka.
- D. Disable SSL for encryption of traffic as it reduces the overall client performance.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

By default, there is no encryption or authentication, nor are ACLs configured. Any client can communicate to Kafka brokers using the PLAINTEXT port. It is critical that access using this port is restricted to trusted clients only. Network segmentation and / or authorization ACLs can be used to restrict access to trusted IPs in such cases. If neither is used, then the cluster is wide open and can be accessed by anyone. While non-secured clusters are supported, as are a mix of authenticated, unauthenticated, encrypted and non-encrypted clients, it is recommended to secure the components in your deployment. For authorization it‘s a best practice to create one principal per application and give each principal only the ACLs it requires and no more. Note: ACLs are used for authorization, not for authentication. Further reading: Security Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Create one custom user with a random generated password and send the credentials to specific users only.**  
   **Incorrect**.

2. ✅ **B. Create one principal per application and give each principal only the ACLs it requires and no more.**  
   **Correct**.

3. ❌ **C. Use fine-grained Access Control Lists for authentication to allow only specific users to connect to Kafka.**  
   **Incorrect**.

4. ❌ **D. Disable SSL for encryption of traffic as it reduces the overall client performance.**  
   **Incorrect**.

</details>

## Question 36 (Kafka Consumers):
Using Kafka, how does a consumer commit an offset?

- A. A. Committed offsets for each partition are stored inside Zookeeper.
- B. B. Consumers store committed offsets for each partition in a local internal database.
- C. C. Committed offsets for each partition are stored together with the message in the original Kafka topic.
- D. D. Consumers produce messages to a special __consumer_offsets topic with the committed offset for each partition

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. A. Committed offsets for each partition are stored inside Zookeeper.**  
   **Incorrect**.

2. ❌ **B. B. Consumers store committed offsets for each partition in a local internal database.**  
   **Incorrect**.

3. ❌ **C. C. Committed offsets for each partition are stored together with the message in the original Kafka topic.**  
   **Incorrect**.

4. ✅ **D. D. Consumers produce messages to a special __consumer_offsets topic with the committed offset for each partition**  
   **Correct**.

</details>

## Question 37 (Kafka Internals):
A company configured a Kafka cluster with the parameters –log.retention.hours = 200, –log.retention.minutes = 200 and –log.retention.ms = 200. With this configuration, how long will log data be retained before old log segments will be discarded to free up space?

- A. 200 hours
- B. 200 minutes
- C. 200 milliseconds
- D. 200 seconds

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

If more than one similar config is specified, the smaller unit size will take precedence. – log.retention.hours: The number of hours to keep a log file before deleting it (in hours), tertiary to log.retention.ms property. – log.retention.minutes: The number of minutes to keep a log file before deleting it (in minutes), secondary to log.retention.ms property. If not set, the value in log.retention.hours is used. – log.retention.ms: The number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. If set to -1, no time limit is applied.

**Detailed explanation of each option:**

1. ❌ **A. 200 hours**  
   **Incorrect**.

2. ❌ **B. 200 minutes**  
   **Incorrect**.

3. ✅ **C. 200 milliseconds**  
   **Correct**.

4. ❌ **D. 200 seconds**  
   **Incorrect**.

</details>

## Question 38 (Kafka Core Concepts):
What‘s the main advantage of Kafka‘s pub / sub message communication model over classical request / response (point-to-point) systems? 

- A. Decoupling
- B. Scalability
- C. Reliability
- D. Performance

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In the request / reply messaging model, the message sender sends a message on one queue, and then it waits for the response from the receiver. with this model, the send cares about the message status thats it received or not yet. The publish / subscribe messaging or normally called pub / sub messaging is a form of asynchronous. In this domain, the message producers are called publishers and the message consumers are called subscribers. The publisher produces messages to a topic then all subscribers which subscribed to that topic will receive the sending messages and consume them. A difference is in the point-to-point model, the message sender must know the receiver but in the publish / subscribe model the message publishers do not need to know where the message will be consumed. This characteristic provides a high decoupling for the application when applying the pub / sub message model.

**Detailed explanation of each option:**

1. ✅ **A. Decoupling**  
   **Correct**.

2. ❌ **B. Scalability**  
   **Incorrect**.

3. ❌ **C. Reliability**  
   **Incorrect**.

4. ❌ **D. Performance**  
   **Incorrect**.

</details>

## Question 39 (Kafka Internals):
If a topic has a replication factor of 4 and 6 partitions, what maximum number of brokers can be stopped without impacting the topic availability?

- A. 1
- B. 3
- C. 2
- D. 4

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Correct

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

## Question 40 (Kafka Setup and Operations):
What tool can be used together with Kafka to mirror a source Kafka cluster into a target Kafka cluster? 

- A. MirrorMaker
- B. Kafka Connect
- C. Schema Registry
- D. Streams API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

With MirrorMaker, Kafka administrators can replicate topics, topic configurations, consumer groups, and ACLs from one or more source Kafka clusters to one or more target Kafka clusters, i. e., across cluster environments. Multi-datacenter deployments enable use-cases such as: – Active -> Active geo-localized deployments: allows users to access a near-by data center to optimize their architecture for low latency and high performance. Replication can be done in both sides and data can be produced and consumed in every cluster. – Active-> Passive disaster recover (DR) deployments: in an event of a partial or complete datacenter disaster, allow failing over applications to use Confluent Platform in a different datacenter. – Active -> Passive centralized analytics: Aggregate data from multiple Apache Kafka clusters into one location for organization-wide analytics. No producers will be used at the replicated cluster, it‘s just for consuming data for analytic purposes. – Aggregation (e. g., from many clusters to one): A->K, B->K, C->K. – Fan-out (e. g., from one to many clusters): K->A, K->B, K->C. – Forwarding: A->B, B->C, C->D. The tool uses a Kafka consumer to consume messages from the source cluster, and re-publishes those messages to the local (target) cluster using an embedded Kafka producer. Further reading: Cluster Replication Flows.

**Detailed explanation of each option:**

1. ✅ **A. MirrorMaker**  
   **Correct**.

2. ❌ **B. Kafka Connect**  
   **Incorrect**.

3. ❌ **C. Schema Registry**  
   **Incorrect**.

4. ❌ **D. Streams API**  
   **Incorrect**.

</details>

## Question 41 (Kafka Consumers):
When creating a new Kafka consumer, which of the following options can be used as the partition assignment strategy? 

- A. ResourceBasedAssignor
- B. RoundRobinAssignor
- C. RangeAssignor
- D. WeightedAssignor

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

The first step to start consuming records is to create a KafkaConsumer instance. Creating a KafkaConsumer is very similar to creating a KafkaProducer – you create a Java Properties instance with the properties you want to pass to the consumer. A PartitionAssignor is a class that, given consumers and topics they subscribed to, decides which partitions will be assigned to which consumer. By default, Kafka has two assignment strategies: – RangeAssignor (default): Assigns to each consumer a consecutive subset of partitions from each topic it subscribes to. So if consumers C1 and C2 are subscribed to two topics, T1 and T2, and each of the topics has three partitions, then C1 will be assigned partitions 0 and 1 from topics T1 and T2, while C2 will be assigned partition 2 from those topics. Because each topic has an uneven number of partitions and the assignment is done for each topic independently, the first consumer ends up with more partitions than the second. This happens whenever Range assignment is used and the number of consumers does not divide the number of partitions in each topic neatly. – RoundRobinAssignor: Takes all the partitions from all subscribed topics and assigns them to consumers sequentially, one by one. If C1 and C2 described previously used RoundRobin assignment, C1 would have partitions 0 and 2 from topic T1 and partition 1 from topic T2. C2 would have partition 1 from topic T1 and partitions 0 and 2 from topic T2. In general, if all consumers are subscribed to the same topics (a very common scenario), RoundRobin assignment will end up with all consumers having the same number of partitions (or at most 1 partition difference). Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. ResourceBasedAssignor**  
   **Incorrect**.

2. ✅ **B. RoundRobinAssignor**  
   **Correct**.

3. ✅ **C. RangeAssignor**  
   **Correct**.

4. ❌ **D. WeightedAssignor**  
   **Incorrect**.

</details>

## Question 42 (Kafka Setup and Operations):
A company has problems with the performance of their Kafka application and wants to optimize and tune the clients. How could the company measure their bandwidth in an easy way as a first baseline?

- A. Measure your bandwidth using the Kafka tools “kafka-producer-perf-test“ and “kafka-consumer-perf-test“.
- B. Measure your bandwidth using the Kafka tool “kafka-client-performance“.
- C. Measure your bandwidth using the Kafka topic performance configuration settings.
- D. Measure your bandwidth using the Kafka Streams API.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

After you complete unit and integration testing, you can benchmark and optimize your applications based on your service goals to tune performance. Benchmark testing is important because there is no one-size-fits-all recommendation for the configuration parameters you need to develop Kafka applications to Confluent Cloud. Proper configuration always depends on the use case, other features you have enabled, the data profile, and more. You should run benchmark tests if you plan to tune Kafka clients beyond the defaults. First, measure your bandwidth using the Kafka tools kafka-producer-perf-test and kafka-consumer-perf-test. Further reading: Optimizing and Tuning.

**Detailed explanation of each option:**

1. ✅ **A. Measure your bandwidth using the Kafka tools “kafka-producer-perf-test“ and “kafka-consumer-perf-test“.**  
   **Correct**.

2. ❌ **B. Measure your bandwidth using the Kafka tool “kafka-client-performance“.**  
   **Incorrect**.

3. ❌ **C. Measure your bandwidth using the Kafka topic performance configuration settings.**  
   **Incorrect**.

4. ❌ **D. Measure your bandwidth using the Kafka Streams API.**  
   **Incorrect**.

</details>

## Question 43 (Kafka Setup and Operations):
By default, Kafka ships with no authentication. Which of the following authentication mechanisms and protocols can be used with the Confluent Platform to enable authentication for Kafka brokers?

- A. mTLS
- B. SASL/PLAIN
- C. HTTP Basic Auth
- D. ACLs

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Confluent Platform supports the following authentication mechanisms and protocols for Kafka brokers: SASL: SASL (Simple Authentication Security Layer) is a framework that provides developers of applications and shared libraries with mechanisms for authentication, data integrity-checking, and encryption. The supported SASL mechanisms are: – SASL using JAAS Kafka uses the Java Authentication and Authorization Service (JAAS) for SASL configuration. You must provide JAAS configurations for all SASL authentication mechanisms. This topic explains how to configure JAAS for SASL. – SASL/GSSAPI (Kerberos) SASL/GSSAPI uses your Kerberos or Active Directory server for authentication. – SASL/OAUTHBEARER Only suitable for use in non-production Kafka installations, SASL/OAUTHBEARER enables the use the OAuth 2 Authorization framework in a SASL context to create and validate unsecured JSON web tokens for authentication. – SASL/PLAIN SASL/PLAIN uses a simple username and password for authentication. – SASL/SCRAM SASL/SCRAM uses usernames and passwords stored in ZooKeeper. Credentials are created during installation. – Delegation Tokens (SASL/SSL) Performs authentication based on delegation tokens that use a lightweight authentication mechanism that you can use to complement existing SASL/SSL methods. Delegation tokens are shared secrets between Kafka brokers and clients. – LDAP Performs client authentication with LDAP (or AD) across all of your Kafka clusters that use SASL/PLAIN. mTLS: With mTLS (mutual TLS) authenticationalso known as “two-way authentication“  both Kafka clients and servers use TLS certificates to verify each other‘s identities to ensure that traffic is secure and trusted in both directions. HTTP Basic Auth: You can use HTTP Basic Authentication to authenticate with the Admin REST APIs using a username and password pair, which are presented to the REST Proxy server using the Authorization HTTP header. SSL: You can configure SSL for encryption, but you can also configure SSL for authentication using SSL certificates. Note: ACLs (Access Control Lists) or used for authorization, not for authentication. Further reading: Authentication Methods.

**Detailed explanation of each option:**

1. ✅ **A. mTLS**  
   **Correct**.

2. ✅ **B. SASL/PLAIN**  
   **Correct**.

3. ✅ **C. HTTP Basic Auth**  
   **Correct**.

4. ❌ **D. ACLs**  
   **Incorrect**.

</details>

## Question 44 (Kafka Producers):
What happens if a Kafka producer produces messages faster than the broker can take them?

- A. Data records will be buffered in memory and the buffer will fill up over time.
- B. The data retention period increases for unprocessed messages.
- C. The producer gets blocked until the broker processed all messages.
- D. Kafka automatically scales up the number of brokers to process messages faster.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

If a Kafka producer produces messages faster than the broker can take, the records will be buffered in memory. The default buffer memory is 33554432 bytes (32 MB). The buffer will full up over time and fill back down when the throughput of the broker increases. If the buffer is full, then the .send() method will start to block and won‘t return right away. The configuration “max.block.ms“ is the time the .send() method will block before throwing an exception. If an exception is thrown this usually means the brokers are down and cannot process any data.

**Detailed explanation of each option:**

1. ✅ **A. Data records will be buffered in memory and the buffer will fill up over time.**  
   **Correct**.

2. ❌ **B. The data retention period increases for unprocessed messages.**  
   **Incorrect**.

3. ❌ **C. The producer gets blocked until the broker processed all messages.**  
   **Incorrect**.

4. ❌ **D. Kafka automatically scales up the number of brokers to process messages faster.**  
   **Incorrect**.

</details>

## Question 45 (Kafka Consumers):
Which offset commit strategy should you use for a consumer log application, if it‘s ok if messages will be lost? 

- A. At-least once
- B. Exactly once
- C. At-most once
- D. Auto-commit

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

At-most once guarantee means the message will be processed exactly once, or not at all. For a consumer application at-most once processing means the consumer group receives a batch of messages from Kafka, transforms these and writes the results to a database. The consumer application has enable.auto.commit set to false and is programmed to commit their offsets back to Kafka prior to writing to the database. If the consumer fails after saving the offsets back to Kafka but before writing the data to the database, it will skip these records next time it runs and data will be lost. Usually perfectly fine for log applications, where it‘s ok if some log messages will be lost. Further reading: Offset Management.

**Detailed explanation of each option:**

1. ❌ **A. At-least once**  
   **Incorrect**.

2. ❌ **B. Exactly once**  
   **Incorrect**.

3. ✅ **C. At-most once**  
   **Correct**.

4. ❌ **D. Auto-commit**  
   **Incorrect**.

</details>

## Question 46 (Stream Processing):
Which of the following options describe the concept of stream-table duality best? 

- A. A table can be considered a changelog of a stream, where each data record in the table captures a state change of the stream.
- B. A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table.
- C. A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream.
- D. A stream can be considered a snapshot, at a point in time, of the latest value for each key in a table.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

Kafka Streams is a library for building streaming applications, specifically applications that transform input Kafka topics into output Kafka topics. When implementing stream processing use cases in practice, you typically need both streams and also databases and any stream processing technology must therefore provide first-class support for streams and tables. Kafka‘s Streams API provides such functionality through its core abstractions for streams and tables and the stream-table duality describes the close relationship between streams and tables: – Stream as Table: A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table. A stream is thus a table in disguise, and it can be easily turned into a ‘real‘ table by replaying the changelog from beginning to end to reconstruct the table. – Table as Stream: A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream (a stream‘s data records are key-value pairs). A table is thus a stream in disguise, and it can be easily turned into a ‘real‘ stream by iterating over each key-value entry in the table. Further reading: Kafka Streams Concepts.

**Detailed explanation of each option:**

1. ❌ **A. A table can be considered a changelog of a stream, where each data record in the table captures a state change of the stream.**  
   **Incorrect**.

2. ✅ **B. A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table.**  
   **Correct**.

3. ✅ **C. A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream.**  
   **Correct**.

4. ❌ **D. A stream can be considered a snapshot, at a point in time, of the latest value for each key in a table.**  
   **Incorrect**.

</details>

## Question 47 (Programming & Serialization):
A company wants to send binary data through the REST proxy, so the data needs to be base64 encoded. Which component needs to encode the binary data into base64? 

- A. Zookeeper
- B. Producer
- C. Consumer
- D. Kafka Broker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The Confluent REST Proxy provides a RESTful interface to a Kafka cluster, making it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol or clients. The REST Proxy requires to receive data over REST that is already base64 encoded, hence it is the responsibility of the producer to encode the data. Further reading: Confluent REST APIs.

**Detailed explanation of each option:**

1. ❌ **A. Zookeeper**  
   **Incorrect**.

2. ✅ **B. Producer**  
   **Correct**.

3. ❌ **C. Consumer**  
   **Incorrect**.

4. ❌ **D. Kafka Broker**  
   **Incorrect**.

</details>

## Question 48 (Kafka Setup and Operations):
The new security team of a company configured the Confluent Server Authorizer to be able to capture, protect, and preserve authorization activity into topics in their production Kafka cluster. Which concept name best describes this security configuration which helps to track user and application access across the platform?

- A. Log replication
- B. ACL decisions
- C. RBAC tracking
- D. Audit logs

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka does not provide a mechanism for maintaining a record of authorization decisions out of the box. Operators are required to capture and parse unstructured logs from brokers in order to build observations on ACL decisions. Confluent Platform complements Kafka with structured audit logs, which provide a way to capture, protect, and preserve authorization activity into Kafka topics. The primary value of audit logs is that they provide data you can use to assess security risks in your local and remote Kafka clusters. They contain all of the information necessary to follow a user‘s interaction with your local or remote Kafka clusters, and provide a way to: – Track user and application access across the platform. – Identify abnormal behavior and anomalies. – Proactively monitor and resolve security risks. Note: Before configuring and using audit logs, you must configure the Confluent Server Authorizer. Further reading: Audit Log Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Log replication**  
   **Incorrect**.

2. ❌ **B. ACL decisions**  
   **Incorrect**.

3. ❌ **C. RBAC tracking**  
   **Incorrect**.

4. ✅ **D. Audit logs**  
   **Correct**.

</details>

## Question 49 (Kafka Producers):
Which of the following producer callback exceptions is non-retriable and therefore the message will not be sent again?

- A. UnknownTopicOrPartitionException
- B. TimeoutException
- C. NotEnoughReplicasException
- D. RecordTooLargeException

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, producers create and write messages to topic partitions. There are the following exceptions possible happening during callback. 1: Non-Retriable exceptions (fatal, the message will never be sent): – InvalidTopicException – OffsetMetadataTooLargeException – RecordBatchTooLargeException – RecordTooLargeException – UnknownServerException 2: Retriable exceptions (transient, may be covered by increasing the number of retries): – CorruptRecordException – InvalidMetadataException – NotEnoughReplicasAfterAppendException – NotEnoughReplicasException – OffsetOutOfRangeException – TimeoutException – UnknownTopicOrPartitionException Further reading: Exception Class.

**Detailed explanation of each option:**

1. ❌ **A. UnknownTopicOrPartitionException**  
   **Incorrect**.

2. ❌ **B. TimeoutException**  
   **Incorrect**.

3. ❌ **C. NotEnoughReplicasException**  
   **Incorrect**.

4. ✅ **D. RecordTooLargeException**  
   **Correct**.

</details>

## Question 50 (Stream Processing):
Which of the following joins does not require input topics to be having the same number of partitions? 

- A. KStream-KStream
- B. KStream-KTable
- C. KTable-Ktable
- D. KStream-GlobalKTable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When joining streams or tables input data must be co-partitioned. This ensures that input records with the same key, from both sides of the join, are delivered to the same stream task during processing. It is the responsibility of the user to ensure data co-partitioning when joining. Data co-partitioning is required because KStream-KStream, KTable-KTable, and KStream-KTable joins are performed based on the keys of records (e. g., leftRecord.key == rightRecord.key). The requirements for data co-partitioning are: – The input topics of the join (left side and right side) must have the same number of partitions. – All applications that write to the input topics must have the same partitioning strategy so that records with the same key are delivered to same partition number. Note: If possible, consider using global tables (GlobalKTable) for joining because they do not require data co-partitioning. Further reading: Joining Concepts.

**Detailed explanation of each option:**

1. ❌ **A. KStream-KStream**  
   **Incorrect**.

2. ❌ **B. KStream-KTable**  
   **Incorrect**.

3. ❌ **C. KTable-Ktable**  
   **Incorrect**.

4. ✅ **D. KStream-GlobalKTable**  
   **Correct**.

</details>

## Question 51 (Stream Processing):
What kind of Kafka Streams window has fixed-size, is non-overlapping and gap-less? 

- A. Sliding time window
- B. Session window
- C. Hopping time window
- D. Tumbling time window

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Windowing lets you control how to group records that have the same key for stateful operations such as aggregations or joins into so-called windows. Windows are tracked per record key. The Kafka Streams DSL (Domain Specific Language) supports the following types of windows: – Tumbling time window (time-based): Fixed-size, non-overlapping, gap-less windows. – Hopping time window (time-based): Fixed-size, overlapping windows. – Sliding time window (time-based): Fixed-size, overlapping windows that work on differences between record timestamps. – Session window (session-based): Dynamically-sized, non-overlapping, data-driven windows.

**Detailed explanation of each option:**

1. ❌ **A. Sliding time window**  
   **Incorrect**.

2. ❌ **B. Session window**  
   **Incorrect**.

3. ❌ **C. Hopping time window**  
   **Incorrect**.

4. ✅ **D. Tumbling time window**  
   **Correct**.

</details>

## Question 52 (Kafka Producers):
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

## Question 53 (Kafka Internals):
In which scenario do you want to set the broker config “unclean.leader.election.enable=true“?

- A. If you prioritize durability over scalability.
- B. If you prioritize availability over durability.
- C. If you prioritize scalability over availability.
- D. If you prioritize durability over availability.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The broker property unclean.leader.election.enable allows you to specify a preference of availability or durability. If availability is more important than avoiding data loss, ensure that this property is set to true. If preventing data loss is more important than availability, set this property to false. This setting operates as follows: If unclean.leader.election.enable is set to true (enabled), an out-of-sync replica will be elected as leader when there is no live in-sync replica (ISR). This preserves the availability of the partition, but there is a chance of data loss. If unclean.leader.election.enable is set to false and there are no live in-sync replicas, Kafka returns an error and the partition will be unavailable.

**Detailed explanation of each option:**

1. ❌ **A. If you prioritize durability over scalability.**  
   **Incorrect**.

2. ✅ **B. If you prioritize availability over durability.**  
   **Correct**.

3. ❌ **C. If you prioritize scalability over availability.**  
   **Incorrect**.

4. ❌ **D. If you prioritize durability over availability.**  
   **Incorrect**.

</details>

## Question 54 (Kafka Connect):
Which connector configurations are mandatory for every connector using Kafka Connect?

- A. Unique connector name.
- B. The maximum number of tasks that should be created for this connector.
- C. The Java class for the connector.
- D. The key and value converter set by the worker.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Connector configurations are simple key-value mappings. For standalone mode these are defined in a properties file and passed to the Connect process on the command line. In distributed mode, they will be included in the JSON payload for the request that creates (or modifies) the connector. Most configurations are connector dependent, so they can‘t be outlined here. However, there are a few common options: – name: Unique name for the connector. Attempting to register again with the same name will fail. – connector.class: The Java class for the connector. – tasks.max: The maximum number of tasks that should be created for this connector. The connector may create fewer tasks if it cannot achieve this level of parallelism. – key.converter: (optional) Override the default key converter set by the worker. – value.converter: (optional) Override the default value converter set by the worker. Further reading: Kafka Connect.

**Detailed explanation of each option:**

1. ✅ **A. Unique connector name.**  
   **Correct**.

2. ✅ **B. The maximum number of tasks that should be created for this connector.**  
   **Correct**.

3. ✅ **C. The Java class for the connector.**  
   **Correct**.

4. ❌ **D. The key and value converter set by the worker.**  
   **Incorrect**.

</details>
