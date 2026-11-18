## 🚫 Question 1 (Kafka Ecosystem):
Using ksqlDB or Kafka Streams, what happens to internal topics if automatic topic creation is turned off? (Choose one)

- A. ksqlDB and Kafka Streams applications will break as topics cannot be created.
- B. Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created.
- C. Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on.
- D. ksqlDB and Kafka Streams applications continue to work as topics are still created.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. “ksqlDB and Kafka Streams applications will break as topics cannot be created.” This is correct because both ksqlDB and Kafka Streams rely on internal topics (such as changelog and repartition topics) that must be created automatically. If automatic topic creation is disabled, these internal topics cannot be created, causing the applications to fail. This reflects the dependency of these frameworks on Kafka’s topic creation mechanism. Incorrect Option B. “Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created.” Incorrect because even existing applications may break if they need to create new internal topics during runtime. It is not limited to “new applications”; the issue affects all applications that rely on automatic topic creation. Option C. “Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on.” Incorrect because if automatic topic creation is turned off at the broker level, it applies universally. New applications cannot bypass this setting; they will also fail when internal topics need to be created. Option D. “ksqlDB and Kafka Streams applications continue to work as topics are still created.” Incorrect because with automatic topic creation disabled, topics are not created automatically. Applications will not continue to work unless topics are manually created beforehand, which contradicts the statement.

**Detailed explanation of each option:**

1. ✅ **A. ksqlDB and Kafka Streams applications will break as topics cannot be created.**  
   **Correct**.

2. ❌ **B. Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created.**  
   **Incorrect**.

3. ❌ **C. Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on.**  
   **Incorrect**.

4. ❌ **D. ksqlDB and Kafka Streams applications continue to work as topics are still created.**  
   **Incorrect**.

</details>

## Question 2 (Reliable Data Delivery):
In a Kafka topic with a replication factor of 3 and a min.insync.replicas setting of 2, how many brokers can become unavailable before a producer using acks=all encounters a situation where it cannot produce messages?

- A. 1
- B. 3
- C. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The correct answer is: 1 Explanation: The Kafka replication factor is set to 3, meaning each message is replicated to 3 brokers. The min.insync.replicas setting is set to 2, meaning a producer needs at least 2 replicas in sync for the write to be acknowledged when using acks=all. If 1 broker becomes unavailable, the remaining 2 replicas can still acknowledge the message, satisfying the min.insync.replicas setting. However, if 2 brokers become unavailable, only 1 replica will be left, and the producer cannot produce messages because the number of in-sync replicas falls below the required threshold of 2. Thus, only 1 broker can become unavailable before the producer cannot produce messages.

**Detailed explanation of each option:**

1. ✅ **A. 1**  
   **Correct**.

2. ❌ **B. 3**  
   **Incorrect**.

3. ❌ **C. 2**  
   **Incorrect**.

</details>

## Question 3 (Stream Processing):
You are implementing a Kafka Streams application to perform a stateless transformation on each record of a stream and output the results to a new topic. What Kafka Streams operation should you use?

- A. filter
- B. map
- C. through
- D. reduce

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

map: To perform a stateless transformation on each record of a stream and output the results to a new topic in a Kafka Streams application, you should use the map operation. The map operation allows you to apply a function to each record independently, transforming it as desired, and then sending the transformed records to a new topic or downstream processing step. This operation is suitable for stateless record-level transformations.

**Detailed explanation of each option:**

1. ❌ **A. filter**  
   **Incorrect**.

2. ✅ **B. map**  
   **Correct**.

3. ❌ **C. through**  
   **Incorrect**.

4. ❌ **D. reduce**  
   **Incorrect**.

</details>

## Question 4 (Programming & Serialization):
When using Java programming with Kafka, what does the KafkaConsumer class primarily represent?

- A. Producer
- B. Consumer
- C. Message
- D. Topic

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Consumer. In Java programming with Kafka, the KafkaConsumer class primarily represents the consumer. It is a part of the Kafka client library and is used to create Kafka consumers that can subscribe to Kafka topics and consume messages from them. The KafkaConsumer class provides methods and configurations to manage the consumption of messages from Kafka topics.

**Detailed explanation of each option:**

1. ❌ **A. Producer**  
   **Incorrect**.

2. ✅ **B. Consumer**  
   **Correct**.

3. ❌ **C. Message**  
   **Incorrect**.

4. ❌ **D. Topic**  
   **Incorrect**.

</details>

## Question 5 (Kafka Connect):
You want to sink data from a Kafka topic to S3 using Kafka Connect. There are 10 brokers in the cluster, the topic has 2 partitions with replication factor of 3. How many tasks will you configure for the S3 connector?

- A. 3
- B. 6
- C. 10
- D. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

2 The number of tasks for a Kafka Connect connector should generally match the number of partitions in the Kafka topic. This ensures optimal parallelism and efficient data processing. In this case, the Kafka topic has 2 partitions, so configuring 2 tasks for the S3 connector will allow the connector to process data from both partitions concurrently. This will maximize throughput and minimize latency. While there are 10 brokers and a replication factor of 3, these factors do not directly influence the number of tasks required for the S3 connector. The key factor is the number of partitions in the Kafka topic.

**Detailed explanation of each option:**

1. ❌ **A. 3**  
   **Incorrect**.

2. ❌ **B. 6**  
   **Incorrect**.

3. ❌ **C. 10**  
   **Incorrect**.

4. ✅ **D. 2**  
   **Correct**.

</details>

## Question 6 (Kafka Producers):
In a Kafka producer, you want to control the maximum amount of time a message can spend in the producer buffer waiting to be sent. Which configuration should you adjust?

- A. acks
- B. max.in.flight.requests.per.connection
- C. batch.size
- D. delivery.timeout.ms

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option: D. delivery.timeout.ms The delivery.timeout.ms configuration in a Kafka producer specifies the maximum time a message can wait in the producer buffer before being considered a delivery failure. This setting controls how long the producer will attempt to send the message before giving up. This is correct because the delivery.timeout.ms configuration controls the maximum amount of time a message can spend in the producer buffer waiting to be sent. If the message is not sent within this time frame, it will be considered a failure. The delivery.timeout.ms configuration defines an upper bound on the total time to wait for a complete send request, including the time spent waiting for acknowledgments from the broker and any retries that may occur. This setting effectively controls how long a message can spend in the producer buffer waiting to be sent, making it the correct choice for this scenario. Incorrect Options: A. acks: This configuration controls the level of acknowledgement required from the Kafka broker for a message to be considered successfully delivered. It doesn’t directly affect the time spent in the producer buffer. B. max.in.flight.requests.per.connection: This configuration limits the number of unacknowledged messages a producer can have outstanding for a single broker connection. It affects throughput but doesn’t directly control the timeout for messages in the buffer. C. batch.size: This configuration specifies the size of batches used to send messages to the broker. While it can impact latency by grouping messages, it doesn’t directly control the timeout for individual messages in the buffer.

**Detailed explanation of each option:**

1. ❌ **A. acks**  
   **Incorrect**.

2. ❌ **B. max.in.flight.requests.per.connection**  
   **Incorrect**.

3. ❌ **C. batch.size**  
   **Incorrect**.

4. ✅ **D. delivery.timeout.ms**  
   **Correct**.

</details>

## Question 7 (Kafka Setup and Operations):
There are five brokers in a cluster, a topic with 10 partitions and replication factor of 3, and a quota of producer_bytes_rate of 1 MB/sec has been specified for the client. What is the maximum throughput allowed for the client?

- A. 1 MB/s
- B. 10 MB/s
- C. 0.33 MB/s
- D. 5 MB/s

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

producer_bytes_rate = 1 MB/sec PER BROKER

But the quota is enforced PER CLIENT, not per broker!

The client sends to the PARTITION LEADER:
→ 10 partitions distributed across 5 brokers
(10 partitions / 5 brokers = 2 partitions per broker)
→ But quota = 1 MB/s applies to the ENTIRE client!

Quota = limit for the CLIENT as a whole
→ Does NOT multiply by the number of brokers
→ Does NOT multiply by the number of partitions
→ 1 MB/s = maximum throughput for the client!

**Detailed explanation of each option:**

1. ✅ **A. 1 MB/s**  
   **Correct**.

2. ❌ **B. 10 MB/s**  
   **Incorrect**.

3. ❌ **C. 0.33 MB/s**  
   **Incorrect**.

4. ❌ **D. 5 MB/s**  
   **Incorrect**.

</details>

## Question 8 (Kafka Internals):
In a scenario where a producer has sent a message to the leader broker for a topic partition, utilizing acks=1 and, as a result, the data hasn‘t been replicated to followers yet, what conditions need to be met for the consumer to receive and view the message?

- A. When the message has been fully replicated to all replicas
- B. When the high watermark has advanced
- C. Right away
- D. Never, the produce request will fail

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

When the high watermark has advanced Explanation: With acks=1, the leader can acknowledge immediately, but followers may lag. Kafka does not expose messages to consumers until they are fully replicated to all in-sync replicas (i.e., until the high watermark advances). This ensures consumers do not read messages that might be lost if the leader fails before replication. Other options: “Right away” → Incorrect: Consumers don’t see the message immediately; they wait for the high watermark. “When the message has been fully replicated to all replicas” → Slightly misleading: It must be all in-sync replicas, not necessarily every replica if some are offline. “Never, the produce request will fail” → Incorrect: Produce request succeeded (acks=1).

**Detailed explanation of each option:**

1. ❌ **A. When the message has been fully replicated to all replicas**  
   **Incorrect**.

2. ✅ **B. When the high watermark has advanced**  
   **Correct**.

3. ❌ **C. Right away**  
   **Incorrect**.

4. ❌ **D. Never, the produce request will fail**  
   **Incorrect**.

</details>

## 🚫 Question 9 (Kafka Ecosystem):
In a scenario where you want to create a new table in KSQL by aggregating data from an existing stream, what KSQL statement should you use?

- A. CREATE TABLE
- B. AGGREGATE TABLE
- C. SUMMARIZE TABLE
- D. GENERATE TABLE

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

CREATE TABLE. Explanation: In a scenario where you want to create a new table in KSQL by aggregating data from an existing stream, you should use the CREATE TABLE statement. This statement allows you to define a new table schema and specify the aggregation logic to aggregate data from the source stream and populate the new table. The CREATE TABLE statement is commonly used for materializing aggregated results into a table for further analysis or querying.

**Detailed explanation of each option:**

1. ✅ **A. CREATE TABLE**  
   **Correct**.

2. ❌ **B. AGGREGATE TABLE**  
   **Incorrect**.

3. ❌ **C. SUMMARIZE TABLE**  
   **Incorrect**.

4. ❌ **D. GENERATE TABLE**  
   **Incorrect**.

</details>

## Question 10 (Kafka Connect):
You are using JDBC source connector to copy data from 3 tables to three Kafka topics. There is one connector created with max.tasks equal to 2 deployed on a cluster of 3 workers. How many tasks are launched?

- A. 3
- B. 2
- C. 1
- D. 6

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

2 tasks are launched. max.tasks: This configuration parameter in the JDBC Source Connector specifies the maximum number of tasks that the connector can create to read data from the source database. In this case: You’ve set max.tasks to 2, meaning the connector will create at most 2 tasks to process data from the three tables. Key points: The number of workers in the cluster does not directly determine the number of tasks launched. The max.tasks configuration controls the parallelism within the connector itself. The actual number of tasks running might be less than max.tasks depending on factors like data volume, available resources, and connector configuration. By setting max.tasks to 2, you’re instructing the connector to use at most two parallel threads to read and process data from the three tables. This allows for some level of parallelism but might not fully utilize all available resources in a three-worker cluster.

**Detailed explanation of each option:**

1. ❌ **A. 3**  
   **Incorrect**.

2. ✅ **B. 2**  
   **Correct**.

3. ❌ **C. 1**  
   **Incorrect**.

4. ❌ **D. 6**  
   **Incorrect**.

</details>

## Question 11 (Programming & Serialization):
In a consumer application that employs the KafkaAvroDeserializer for deserializing Avro messages, what occurs when the message schema is absent from the local cache of the AvroDeserializer?

- A. Throws DeserializationException
- B. Fails silently
- C. Fetches schema from Schema Registry
- D. Throws SerializationException

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Fetches schema from Schema Registry. When a consumer application using KafkaAvroDeserializer encounters an Avro message and the schema for that message is not present in the local cache, the deserializer will automatically contact the Schema Registry to fetch the schema. The Schema Registry is a service that stores Avro schemas for Kafka messages, and it allows producers and consumers to share a common schema for messages.The key points are:Fetches schema from Schema Registry: This is the standard behavior of KafkaAvroDeserializer. It ensures that messages can be deserialized correctly even if the consumer hasn‘t previously encountered the schema.Throws DeserializationException: This would typically occur if the schema cannot be retrieved from the Schema Registry or if the message cannot be deserialized even after fetching the schema.Fails silently: Kafka clients generally do not fail silently in the event of serious issues like missing schemas. They will throw an exception to notify the application of the problem.Throws SerializationException: This exception is more commonly associated with problems during serialization, not deserialization. In the context of a consumer using KafkaAvroDeserializer, a DeserializationException would be more relevant if there‘s an issue with the message format or schema.

**Detailed explanation of each option:**

1. ❌ **A. Throws DeserializationException**  
   **Incorrect**.

2. ❌ **B. Fails silently**  
   **Incorrect**.

3. ✅ **C. Fetches schema from Schema Registry**  
   **Correct**.

4. ❌ **D. Throws SerializationException**  
   **Incorrect**.

</details>

## Question 12 (Kafka Connect):
Which of the following options best describes Kafka Connect?

- A. Kafka Connect works as a centralized data hub for simple data integration between databases, key-value stores, search indexes, and file systems.
- B. Kafka Connect is a database purpose-built to help developers create stream processing applications on top of Apache Kafka.
- C. Kafka Connect provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas.
- D. Kafka Connect is a client library for building applications and microservices, where the input and output data are stored in an Kafka cluster.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Centralized data hub: Kafka Connect acts as a bridge between various data sources and Kafka, allowing you to easily connect and stream data from different systems into Kafka. Simple data integration: Kafka Connect provides connectors that simplify the process of integrating data from different sources, making it easier to build stream processing applications. Variety of data sources: Kafka Connect supports a wide range of data sources, including databases, key-value stores, search indexes, and file systems. The other options are incorrect: Database purpose-built for stream processing: Kafka Connect is not a database itself, but a tool for integrating data with Kafka. RESTful interface for storing schemas: Kafka Connect is not primarily used for storing schemas. It is used for connecting data sources to Kafka. Client library for building applications: Kafka Connect is not a client library for building applications. It is a tool for integrating data with Kafka. Therefore, Kafka Connect is a centralized data hub that simplifies data integration between various sources and Kafka.

**Detailed explanation of each option:**

1. ✅ **A. Kafka Connect works as a centralized data hub for simple data integration between databases, key-value stores, search indexes, and file systems.**  
   **Correct**.

2. ❌ **B. Kafka Connect is a database purpose-built to help developers create stream processing applications on top of Apache Kafka.**  
   **Incorrect**.

3. ❌ **C. Kafka Connect provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas.**  
   **Incorrect**.

4. ❌ **D. Kafka Connect is a client library for building applications and microservices, where the input and output data are stored in an Kafka cluster.**  
   **Incorrect**.

</details>

## Question 13 (Kafka Setup and Operations):
You want to control access to specific Kafka topics. What Kafka feature should you use for this purpose?

- A. Kafka Connect
- B. Kafka Streams
- C. ACLs (Access Control Lists)
- D. Producer Acknowledgment

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

ACLs (Access Control Lists). Explanation: To control access to specific Kafka topics and manage security in Kafka, you should use Access Control Lists (ACLs). ACLs allow you to define fine-grained access permissions for users and clients, specifying who can read from or write to particular topics, and what actions they can perform on those topics. Kafka ACLs are a fundamental security feature that helps you restrict and manage access to topics and maintain data privacy and security within your Kafka cluster.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect**  
   **Incorrect**.

2. ❌ **B. Kafka Streams**  
   **Incorrect**.

3. ✅ **C. ACLs (Access Control Lists)**  
   **Correct**.

4. ❌ **D. Producer Acknowledgment**  
   **Incorrect**.

</details>

## 🚫 Question 14 (Kafka Ecosystem):
In your KSQL query, how can you retrieve and process all the messages from a specific topic?

- A. Use KSQL CLI to set auto.offset.reset property to earliest
- B. KSQL reads from the beginning of a topic, by default.
- C. KSQL reads from the end of a topic. This cannot be changed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Use KSQL CLI to set auto.offset.reset property to earliest.By default, KSQL queries read from the end of a topic, meaning they only process new messages that arrive after the query starts. To read all messages from the beginning of a topic, you need to configure the auto.offset.reset property to earliest. This can be done in the KSQL CLI before running your query.You would typically set this property in the KSQL CLI session using a command like this:SET ‘auto.offset.reset‘ = ‘earliest‘;After setting this property, any KSQL queries executed in that session will process messages from the beginning of the topic. It‘s important to note that this setting will apply to all queries executed in that session until the property is changed or the session is closed.

**Detailed explanation of each option:**

1. ✅ **A. Use KSQL CLI to set auto.offset.reset property to earliest**  
   **Correct**.

2. ❌ **B. KSQL reads from the beginning of a topic, by default.**  
   **Incorrect**.

3. ❌ **C. KSQL reads from the end of a topic. This cannot be changed.**  
   **Incorrect**.

</details>

## Question 15 (Programming & Serialization):
You want to secure the communication between Confluent REST Proxy and Kafka brokers using SSL. What configuration setting should you adjust to specify the location of the SSL truststore file?

- A. ssl.keystore.location
- B. ssl.truststore.location
- C. security.protocol
- D. ssl.key.password

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

ssl.truststore.location. To secure the communication between Confluent REST Proxy and Kafka brokers using SSL, you should adjust the ssl.truststore.location configuration setting. This setting specifies the location of the SSL truststore file, which contains the trusted CA certificates used to verify the authenticity of the Kafka brokers during the SSL handshake process. It‘s essential to configure this setting with the correct path to the truststore file to establish secure SSL communication.

**Detailed explanation of each option:**

1. ❌ **A. ssl.keystore.location**  
   **Incorrect**.

2. ✅ **B. ssl.truststore.location**  
   **Correct**.

3. ❌ **C. security.protocol**  
   **Incorrect**.

4. ❌ **D. ssl.key.password**  
   **Incorrect**.

</details>

## Question 16 (Reliable Data Delivery):
Select all that apply (select THREE):

- A. min.insync.replicas only matters if acks=all
- B. min.insync.replicas is a producer setting
- C. min.insync.replicas matters regardless of the values of acks
- D. acks is a producer setting
- E. min.insync.replicas is a topic setting
- F. acks is a topic setting

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, E

**Explanation:**

Option A. min.insync.replicas only matters if acks=all Why correct: The min.insync.replicas setting ensures that a write is acknowledged only if the specified minimum number of replicas are in sync. This matters specifically when the producer sets acks=all, because the broker will require that minimum number of replicas to confirm the write. Option D. acks is a producer setting Why correct: The acks configuration is set on the producer side. It determines how many acknowledgments the producer requires before considering a request complete (e.g., acks=0, acks=1, acks=all). Option E. min.insync.replicas is a topic setting Why correct: The min.insync.replicas configuration is defined at the topic level (or broker level as a default). It specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. Incorrect Option B. min.insync.replicas is a producer setting Why incorrect: This is not a producer-side setting. It is configured at the topic or broker level. Option C. min.insync.replicas matters regardless of the values of acks Why incorrect: It only matters when acks=all. If acks=1 or acks=0, the producer does not wait for multiple replicas, so min.insync.replicas is irrelevant. Option F. acks is a topic setting Why incorrect: acks is strictly a producer-side configuration, not a topic-level setting.

**Detailed explanation of each option:**

1. ✅ **A. min.insync.replicas only matters if acks=all**  
   **Correct**.

2. ❌ **B. min.insync.replicas is a producer setting**  
   **Incorrect**.

3. ❌ **C. min.insync.replicas matters regardless of the values of acks**  
   **Incorrect**.

4. ✅ **D. acks is a producer setting**  
   **Correct**.

5. ✅ **E. min.insync.replicas is a topic setting**  
   **Correct**.

6. ❌ **F. acks is a topic setting**  
   **Incorrect**.

</details>

## Question 17 (Kafka Internals):
In a Kafka cluster where all topics have a replication factor of 3, an intern inadvertently halted a broker and unintentionally erased all the data stored on that broker‘s disk. What will occur when the broker is subsequently restarted?

- A. The broker will start, and other topics will also be deleted as the broker data on the disk got deleted
- B. The broker will start, and won‘t have any data. If the broker comes leader, we have a data loss
- C. The broker will start, and won‘t be online until all the data it needs to have is replicated from other leaders
- D. The broker will crash

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. The broker will start, and won’t be online until all the data it needs to have is replicated from other leaders Correct because in Kafka with a replication factor of 3, data is stored across multiple brokers. When a broker restarts after losing its local data, it will rejoin the cluster but remain out of sync. Kafka ensures that the broker fetches missing partitions from other replicas (leaders) before it is considered fully in-sync. This prevents data loss and maintains consistency. Incorrect Option A. The broker will start, and other topics will also be deleted as the broker data on the disk got deleted Incorrect because deleting data on one broker does not delete topics or partitions across the cluster. Other replicas maintain the data, so topics are not lost. Option B. The broker will start, and won’t have any data. If the broker comes leader, we have a data loss Incorrect because Kafka’s controller ensures that only in-sync replicas can become leaders. Since the restarted broker is initially out of sync, it will not be elected leader until replication is complete, preventing data loss. Option D. The broker will crash Incorrect because Kafka brokers are designed to handle disk loss gracefully. The broker will restart normally, but it will need to replicate data from other brokers before becoming fully operational.

**Detailed explanation of each option:**

1. ❌ **A. The broker will start, and other topics will also be deleted as the broker data on the disk got deleted**  
   **Incorrect**.

2. ❌ **B. The broker will start, and won‘t have any data. If the broker comes leader, we have a data loss**  
   **Incorrect**.

3. ✅ **C. The broker will start, and won‘t be online until all the data it needs to have is replicated from other leaders**  
   **Correct**.

4. ❌ **D. The broker will crash**  
   **Incorrect**.

</details>

## Question 18 (Kafka Producers):
Which of the following producer configurations can be used to increase the chances of batching messages? (Choose one)

- A. max.request.size=1048576
- B. batch.size=32768
- C. linger.ms=10
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Yes, the answer marked as correct — linger.ms=10 — is correct. Explanation: linger.ms: This setting adds a delay before sending a batch, allowing more messages to accumulate and thereby increasing the chances of batching. For example, setting linger.ms=10 means the producer will wait up to 10 milliseconds to fill up the batch before sending it. The other options: max.request.size=1048576: Limits the maximum size of a request but doesn’t directly help with batching. batch.size=32768: Controls the batch size in bytes, which can help, but increasing linger.ms is more directly associated with giving time to batch. acks=all: Controls message durability, not batching.

**Detailed explanation of each option:**

1. ❌ **A. max.request.size=1048576**  
   **Incorrect**.

2. ❌ **B. batch.size=32768**  
   **Incorrect**.

3. ✅ **C. linger.ms=10**  
   **Correct**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## Question 19 (Kafka Connect):
You want to configure a Kafka Connect Sink Connector to write data to an Amazon S3 bucket in an Avro format. Which configuration setting should you adjust to specify the Avro converter?

- A. connector.class
- B. format
- C. key.converter
- D. value.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

value.converter. Explanation: To specify the Avro converter for a Kafka Connect Sink Connector and configure it to write data to an Amazon S3 bucket in Avro format, you should adjust the value.converter configuration setting. This setting defines the converter used to serialize the values of Kafka records, and you can set it to the Avro converter implementation that is compatible with your specific use case.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ❌ **B. format**  
   **Incorrect**.

3. ❌ **C. key.converter**  
   **Incorrect**.

4. ✅ **D. value.converter**  
   **Correct**.

</details>

## Question 20 (Stream Processing):
We have a store selling shoes. What dataset is a great candidate to be modeled as a KTable in Kafka Streams?

- A. The transaction stream
- B. Money made until now
- C. Inventory contents right now
- D. Items returned

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The best dataset to be modeled as a KTable in Kafka Streams for a shoe store is: Inventory contents right now Explanation: KTable: Represents a table-like view of data with a key-value structure. It’s suitable for data that needs to be maintained as a current state and efficiently queried. Inventory: Key: Could be the shoe’s unique identifier (e.g., SKU, model, size, color). Value: The current quantity in stock. Why this fits KTable: Current State: Inventory is a constantly changing state. KTable efficiently maintains the latest inventory levels for each shoe. Efficient Queries: You can quickly query the inventory for specific shoes or get the overall stock levels. Updates: Changes to inventory (sales, returns, new shipments) can be efficiently updated in the KTable. Other options and why they might not be the best fit: Transaction Stream: This is more suited for a KStream as it represents a continuous stream of events (each transaction is an event). Money made until now: This could be a KTable, but it might be more efficiently calculated as an aggregation from the transaction stream. Items returned: This could also be a KStream representing a stream of return events. By modeling the inventory as a KTable, you can build efficient applications for tasks like: Real-time stock checks: Quickly determine if a specific shoe is in stock. Inventory management: Track stock levels, identify low stock items, and trigger reordering. Personalized recommendations: Recommend alternative sizes or colors based on real-time inventory.

**Detailed explanation of each option:**

1. ❌ **A. The transaction stream**  
   **Incorrect**.

2. ❌ **B. Money made until now**  
   **Incorrect**.

3. ✅ **C. Inventory contents right now**  
   **Correct**.

4. ❌ **D. Items returned**  
   **Incorrect**.

</details>

## Question 21 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for BACKWARD schema evolution? (Choose two)

- A. Add fields
- B. Delete fields
- C. Add optional fields
- D. Delete optional fields

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

A. Add fields (Incorrect) Adding a required field (one without a default value) is not backward compatible. If a new consumer expects a required field but receives an old record that doesn’t have it, the consumer will fail. This change is only allowed in Forward compatibility. B. Delete fields (Correct) In Backward compatibility, you can delete fields. When a new consumer (with the deleted field removed from its schema) receives an old record that still contains that field, the consumer simply ignores the extra data. C. Add optional fields (Correct) Adding a field with a default value (an optional field) is a classic backward-compatible change. If a new consumer expects this field but it’s missing in an old record, the consumer will automatically fill in the default value provided in the new schema. D. Delete optional fields (Incorrect) Deleting an optional field (a field that has a default value) is technically allowed in Forward and Full compatibility modes, but it is not the primary definition of a Backward change. In the context of the CCDAK exam, “Delete fields” (Option B) is the standard answer for Backward compatibility because the consumer simply ignores the extra data in the old record. Key Concept: Backward Compatibility In a Backward compatibility strategy, the goal is to ensure that a new consumer can still process data written by an old producer. CCDAK Quick Summary for Comparison To keep these straight for the exam, use this mental model: BACKWARD (New Consumer, Old Data): Allowed: Delete fields (consumer ignores extra data), Add optional fields (consumer uses default for missing data). Consumer update first: You can update consumers before producers. FORWARD (Old Consumer, New Data): Allowed: Add fields (old consumer ignores new data), Delete optional fields (old consumer uses its default for the now-missing data). Producer update first: You can update producers before consumers. FULL: Both of the above. You can only add or delete optional fields.

**Detailed explanation of each option:**

1. ❌ **A. Add fields**  
   **Incorrect**.

2. ✅ **B. Delete fields**  
   **Correct**.

3. ✅ **C. Add optional fields**  
   **Correct**.

4. ❌ **D. Delete optional fields**  
   **Incorrect**.

</details>

## Question 22 (Kafka Connect):
You want to configure a Kafka Connect Source Connector to read data from a MySQL database. Which configuration setting is crucial for specifying the JDBC connection URL?

- A. connector.class
- B. jdbc.connection.url
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

jdbc.connection.url. To configure a Kafka Connect Source Connector to read data from a MySQL database, the crucial configuration setting for specifying the JDBC connection URL is jdbc.connection.url. This setting should contain the JDBC connection URL that includes the necessary details like the hostname, port, database name, and authentication credentials required to establish a connection to the MySQL database. Providing the correct JDBC connection URL is essential for the connector to connect to the MySQL database and retrieve data for ingestion into Kafka topics.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. jdbc.connection.url**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## Question 23 (Kafka Connect):
You are using JDBC source connector to copy data from a table to Kafka topic. There is one connector created with max.tasks equal to 2 deployed on a cluster of 3 workers. How many tasks are launched?

- A. 1
- B. 2
- C. 3
- D. 6

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(See per-option explanations below.)

**Detailed explanation of each option:**

Input data:
→ 1 table  ← KEY POINT!
→ max.tasks = 2
→ 3 workers

Number of tasks = MIN(max.tasks, number of data sources)

MIN(2, 1) = 1 task ✅

1. ✅ **A. 1**  

2. ❌ **B. 2**  

3. ❌ **C. 3**  

4. ❌ **D. 6**  

</details>

## Question 24 (Kafka Connect):
What is the primary role of the Kafka Connect Offset Storage topic in a Kafka Connect setup?

- A. Storing Avro schemas for connectors.
- B. Managing task parallelism.
- C. Storing offsets for connector tasks.
- D. Storing logs for Kafka Connect workers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Storing offsets for connector tasks. Explanation: The primary role of the Kafka Connect Offset Storage topic in a Kafka Connect setup is to store the offsets for connector tasks. This topic is used to keep track of the last processed offset for each connector task, allowing for fault tolerance and resuming processing from where it left off in case of failures or restarts. It helps ensure that data is not duplicated and that the connectors can maintain their state across restarts.

**Detailed explanation of each option:**

1. ❌ **A. Storing Avro schemas for connectors.**  
   **Incorrect**.

2. ❌ **B. Managing task parallelism.**  
   **Incorrect**.

3. ✅ **C. Storing offsets for connector tasks.**  
   **Correct**.

4. ❌ **D. Storing logs for Kafka Connect workers.**  
   **Incorrect**.

</details>

## Question 25 (Kafka Consumers):
For a topic that receives all the orders for products available on an e-commerce site and has 4 partitions, what would be the most efficient way to arrange the consumers for both order fulfillment and monitoring applications to process messages independently while optimizing performance and resource utilization?

- A. Create two consumers groups for two applications with 8 consumers in each
- B. Create two consumer groups for two applications with 4 consumers in each
- C. Create 8 consumers in the same group with 4 consumers for each application
- D. Create four consumers in the same group, one for each partition - two for fulfilment and two for monitoring

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Create two consumer groups for two applications with 4 consumers in each.In Kafka, consumer groups are used to allow a group of consumers to jointly consume from a topic. Each consumer within a group reads from exclusive partitions of the topic, ensuring that each message is processed once per group.For optimal performance and resource usage in your scenario, where two applications (order fulfillment and monitoring) need to process all the messages independently, you should create two separate consumer groups, one for each application. This way, each application gets a copy of every message in the topic.Given that the topic has 4 partitions, you should ideally have up to 4 consumers in each group to maximize parallel processing while ensuring that each consumer has at least one partition to read from. More consumers than partitions in a group would result in some consumers being idle (as a partition can only be read by one consumer in a group at a time).So, the setup would be:One consumer group for the order fulfillment application with 4 consumers.Another consumer group for the monitoring application with 4 consumers.Each consumer group will independently read from all 4 partitions of the topic. This arrangement ensures that both applications process every message and maximizes the use of Kafka‘s parallel processing capabilities.

**Detailed explanation of each option:**

1. ❌ **A. Create two consumers groups for two applications with 8 consumers in each**  
   **Incorrect**.

2. ✅ **B. Create two consumer groups for two applications with 4 consumers in each**  
   **Correct**.

3. ❌ **C. Create 8 consumers in the same group with 4 consumers for each application**  
   **Incorrect**.

4. ❌ **D. Create four consumers in the same group, one for each partition - two for fulfilment and two for monitoring**  
   **Incorrect**.

</details>

## Question 26 (Kafka Producers):
What are the consequences of using the following line of code in your producer?
producer.send(producerRecord).get().

- A. It will force all brokers in Kafka to acknowledge the producerRecord
- B. Throughput will be decreased
- C. Compression will be increased
- D. Batching will be increased

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Throughput will be decreased Calling producer.send(producerRecord).get() makes the producer wait synchronously until the broker responds with the result of the send operation. Normally, send() is asynchronous, allowing the producer to continue sending additional records while previous records are being processed. Calling .get() blocks the calling thread, reducing the number of records that can be sent concurrently and therefore decreasing throughput. Incorrect: Option A. producer.send(producerRecord).get() will force all brokers in Kafka to acknowledge the producerRecord Incorrect. The .get() call waits for the result of the producer’s send operation. It does not require all Kafka brokers to acknowledge the record. Acknowledgment behavior is controlled by the producer’s acks configuration. Option B. Throughput will be decreased Correct answer is Option C, not B. This option is not technically different from C in the provided choices, so the quiz numbering indicates Option C is the intended correct answer. Option D. Compression will be increased Incorrect. Calling .get() does not change the producer’s compression configuration or cause Kafka to increase compression. Option E. Batching will be increased Incorrect. Waiting synchronously after every send generally works against effective batching because the producer application cannot continuously enqueue records while waiting for each send result. It does not increase the producer’s batching behavior.

**Detailed explanation of each option:**

1. ❌ **A. It will force all brokers in Kafka to acknowledge the producerRecord**  
   **Incorrect**.

2. ✅ **B. Throughput will be decreased**  
   **Correct**.

3. ❌ **C. Compression will be increased**  
   **Incorrect**.

4. ❌ **D. Batching will be increased**  
   **Incorrect**.

</details>

## Question 27 (Programming & Serialization):
In a scenario where Confluent REST Proxy is configured with API key authentication, what configuration setting should you adjust to specify the API key for a particular client?

- A. api.key
- B. client.api.key
- C. api.secret
- D. client.api.secret

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The correct configuration setting to specify the API key for a particular client in Confluent REST Proxy when using API key authentication is client.api.key. Here‘s a breakdown of the relevant configuration options: api.key: This setting, if present, would typically refer to a global API key for the REST Proxy itself, not for individual clients. client.api.key: This is the specific setting where you provide the API key for a particular client that will be accessing the REST Proxy. api.secret and client.api.secret: These settings are not relevant to API key authentication. They might be used in other authentication mechanisms, but not for API keys.

**Detailed explanation of each option:**

1. ❌ **A. api.key**  
   **Incorrect**.

2. ✅ **B. client.api.key**  
   **Correct**.

3. ❌ **C. api.secret**  
   **Incorrect**.

4. ❌ **D. client.api.secret**  
   **Incorrect**.

</details>

## Question 28 (Kafka Consumers):
You have a Kafka topic with three partitions. If you have two consumers in a consumer group, how are partitions assigned to consumers?

- A. One consumer gets all partitions, and the other gets none.
- B. Partitions are assigned randomly.
- C. Each consumer gets one partition.
- D. It depends on the consumer configuration.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

D. It depends on the consumer configuration. The precise assignment of partitions is governed by the partition.assignment.strategy configuration property in the Kafka consumer. This property specifies which PartitionAssignor implementation to use. Example Assignments for 3 Partitions (P0, P1, P2) and 2 Consumers (C1, C2): RangeAssignor (Default): This strategy assigns contiguous blocks of partitions. It typically sorts the partitions numerically and the consumers lexicographically, then divides the partitions into ranges. In this case, C1 would get two partitions (P0, P1) and C2 would get one partition (P2). RoundRobinAssignor: This strategy distributes partitions sequentially across consumers. C1 gets P0, C2 gets P1, C1 gets P2. The result is C1 gets two partitions (P0, P2) and C2 gets one partition (P1). StickyAssignor/CooperativeStickyAssignor: These attempt to minimize movement during rebalances while still aiming for a balanced distribution. In all common cases (Range and RoundRobin), the distribution will be uneven due to the indivisible nature of partitions. Therefore, the outcome is not a fixed assignment like the others, but depends entirely on the chosen strategy (partition.assignment.strategy). Incorrect: A. One consumer gets all partitions, and the other gets none. This is false for the default assignment strategies. The primary goal of a consumer group is load balancing and parallelism, which means partitions are actively distributed among all available, healthy consumers. The scenario described here would only happen if a consumer failed (triggering a rebalance where one consumer temporarily holds all partitions) or if a non-standard custom PartitionAssignor (like a FailoverAssignor) was used. B. Partitions are assigned randomly. This is false. The assignment is deterministic based on the chosen PartitionAssignor strategy (Range, RoundRobin, Sticky) and the sorted lists of consumers and partitions. It is a calculated process, not a random one, to ensure predictable and stable load balancing. C. Each consumer gets one partition. This is false because there are three partitions and only two consumers. Since a partition cannot be shared by consumers in the same group, and the goal is to consume all partitions, the total number of partitions (3) must be consumed by the two consumers. This means one consumer must get two partitions, and the other will get one.

**Detailed explanation of each option:**

1. ❌ **A. One consumer gets all partitions, and the other gets none.**  
   **Incorrect**.

2. ❌ **B. Partitions are assigned randomly.**  
   **Incorrect**.

3. ❌ **C. Each consumer gets one partition.**  
   **Incorrect**.

4. ✅ **D. It depends on the consumer configuration.**  
   **Correct**.

</details>

## Question 29 (Kafka Setup and Operations):
By default, what‘s the encryption mechanism used by Apache Kafka? (Choose one)

- A. SASL
- B. TLS
- C. Plaintext
- D. SSL

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The correct answer is: Plaintext. Explanation: By default, Apache Kafka does not enable encryption or any security mechanisms (like SSL/TLS or SASL) for communication between its clients and brokers. Therefore, communication happens in plaintext unless explicitly configured otherwise. To enable encryption, you would need to configure SSL/TLS for encrypted communication or SASL for authentication, but these are not enabled by default.

**Detailed explanation of each option:**

1. ❌ **A. SASL**  
   **Incorrect**.

2. ❌ **B. TLS**  
   **Incorrect**.

3. ✅ **C. Plaintext**  
   **Correct**.

4. ❌ **D. SSL**  
   **Incorrect**.

</details>

## 🚫 Question 30 (Kafka Setup and Operations):
You observe that a Kafka topic has uneven partition distribution among the brokers. What Kafka tool can you use to fix this issue?

- A. Kafka Connect
- B. Kafka Streams
- C. Kafka Manager
- D. Kafka Mirror Maker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Manager. Explanation: Kafka Manager is a tool commonly used for monitoring and managing Kafka clusters. One of its features is the ability to manage and reassign topic partitions to brokers to achieve a more even distribution. If you observe an uneven partition distribution among the brokers in your Kafka cluster, you can use Kafka Manager to help rebalance the partitions across brokers, ensuring better utilization of cluster resources and improving performance.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect**  
   **Incorrect**.

2. ❌ **B. Kafka Streams**  
   **Incorrect**.

3. ✅ **C. Kafka Manager**  
   **Correct**.

4. ❌ **D. Kafka Mirror Maker**  
   **Incorrect**.

</details>

## Question 31 (Kafka Producers):
A Kafka producer application wants to send log messages to a topic that does not include any key. What are the properties that are mandatory to configure for the producer configuration? (select three)

- A. key.serializer
- B. value
- C. key
- D. bootstrap.servers
- E. value.serializer
- F. partition

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, E

**Explanation:**

bootstrap.servers – This property specifies the Kafka brokers to connect to. value.serializer – This property defines the serializer for the message value. key.serializer – Although the producer will not use a key, this property still needs to be specified (usually set to a no-op serializer if no key is provided).

**Detailed explanation of each option:**

1. ✅ **A. key.serializer**  
   **Correct**.

2. ❌ **B. value**  
   **Incorrect**.

3. ❌ **C. key**  
   **Incorrect**.

4. ✅ **D. bootstrap.servers**  
   **Correct**.

5. ✅ **E. value.serializer**  
   **Correct**.

6. ❌ **F. partition**  
   **Incorrect**.

</details>

## Question 32 (Kafka Producers):
Your producer is producing at a very high rate and the batches are completely full each time. How can you improve the producer throughput? (select two)

- A. Decrease batch.size
- B. Enable compression
- C. Increase batch.size
- D. Decrease linger.ms
- E. Increase linger.ms
- F. Disable compression

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

Enable compression Compression (e.g., lz4, snappy) reduces the size of data sent over the network. This improves network efficiency and increases throughput. Increase batch.size A larger batch.size allows more records per batch, reducing the number of requests sent. This leads to fewer network calls and higher throughput. Why the others are incorrect: Decrease batch.size: Opposite of what you want. It reduces throughput by sending smaller batches. Decrease linger.ms: Reduces wait time, can lower batching efficiency, and reduce throughput. Increase linger.ms: Only useful when batches aren’t already full. In your case, batches are already full — so it won’t help. Disable compression: Will increase data size sent over the network — hurts throughput.

**Detailed explanation of each option:**

1. ❌ **A. Decrease batch.size**  
   **Incorrect**.

2. ✅ **B. Enable compression**  
   **Correct**.

3. ✅ **C. Increase batch.size**  
   **Correct**.

4. ❌ **D. Decrease linger.ms**  
   **Incorrect**.

5. ❌ **E. Increase linger.ms**  
   **Incorrect**.

6. ❌ **F. Disable compression**  
   **Incorrect**.

</details>

## Question 33 (Kafka Producers):
What is returned by a producer.send() call in the Java API?

- A. Future<ProducerRecord> object
- B. Future<RecordMetadata> object
- C. Unit
- D. A Boolean indicating if the call succeeded

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

B. Future<RecordMetadata> object The producer.send() method is designed for asynchronous message sending and returns a java.util.concurrent.Future object parameterized by RecordMetadata. The Future object allows the application thread to proceed immediately without waiting for the broker’s acknowledgment. The RecordMetadata object, which is contained within the Future, holds the details of the message once it has been successfully persisted by the broker, including the topic, partition number, and offset where the message was written. This metadata is crucial for guaranteed delivery semantics. Incorrect: A. Future<ProducerRecord> object This is incorrect. The ProducerRecord is the object that is passed into the send() method (the input message), not the type returned in the Future. The Future returns the metadata about the result of sending the record (RecordMetadata). C. Unit Unit is a type used in some languages to signify no meaningful return value (similar to void). This is false because the send() method returns the Future<RecordMetadata> object, which is highly meaningful as it allows the application to track the status, persistence, and location of the submitted message. D. A Boolean indicating if the call succeeded This is false. A simple boolean return would imply an immediate synchronous success/fail check. The successful return of the Future object only means the record was successfully placed into the producer’s internal send buffer. The actual success of persistence on the broker is determined later when the broker responds, and this final success/failure is retrieved by checking the Future object (e.g., using .get()).

**Detailed explanation of each option:**

1. ❌ **A. Future<ProducerRecord> object**  
   **Incorrect**.

2. ✅ **B. Future<RecordMetadata> object**  
   **Correct**.

3. ❌ **C. Unit**  
   **Incorrect**.

4. ❌ **D. A Boolean indicating if the call succeeded**  
   **Incorrect**.

</details>

## Question 34 (Kafka Internals):
Scenario: You have a Kafka cluster with 6 brokers: Rack A → brokers 0 and 1 Rack B → brokers 2 and 3 Rack C → brokers 4 and 5 You create a topic with 10 partitions and a replication factor of 3. For partition 0, the leader is on broker 4 (Rack C) and the first replica is on broker 2 (Rack B). The question asks: Which two brokers are eligible to host the final replica?

- A. broker 4 and 5
- B. broker 0 and 1
- C. broker2 and 3
- D. broker 5 and 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. broker 0 and 1. The correct answer is brokers 0 and 1, because Kafka’s rack-aware replica assignment attempts to distribute replicas across different racks to improve fault tolerance. Given the cluster configuration: Rack Brokers Rack A Broker 0, Broker 1 Rack B Broker 2, Broker 3 Rack C Broker 4, Broker 5 The partition has a replication factor of 3: Leader: Broker 4 (Rack C). First replica: Broker 2 (Rack B). Final replica: Must be placed in Rack A. Therefore, either Broker 0 or Broker 1 is eligible to host the final replica. Both brokers belong to Rack A, which is different from the racks hosting the leader and first replica. Incorrect Option A. broker 4 and 5. Incorrect because both brokers belong to Rack C, where the partition leader (Broker 4) already resides. Broker 4 cannot host another replica of the same partition, and placing the final replica on Broker 5 would violate rack diversity. Option C. broker 2 and 3. Incorrect because both brokers belong to Rack B, where the first replica (Broker 2) already resides. Broker 2 cannot host another replica of the same partition, and Broker 3 would not provide rack diversity. Option D. broker 5 and 1. Incorrect because Broker 5 belongs to Rack C, which already hosts the leader (Broker 4). Broker 1 is eligible, but Broker 5 is not eligible under the rack-aware placement requirement.

**Detailed explanation of each option:**

1. ❌ **A. broker 4 and 5**  
   **Incorrect**.

2. ✅ **B. broker 0 and 1**  
   **Correct**.

3. ❌ **C. broker2 and 3**  
   **Incorrect**.

4. ❌ **D. broker 5 and 1**  
   **Incorrect**.

</details>

## Question 35 (Programming & Serialization):
A producer application is using KafkaAvroSerializer to send messages of Avro type to Kafka. What happens if the schema is not present in the local cache for schemas but exists in Schema Registry? (Choose one)

- A. The producer throws a warning but creates the schema.
- B. The Kafka broker throws an exception.
- C. The schema gets fetched from the Schema Registry.
- D. The producer registers the schema to the Schema Registry.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. The producer throws a warning but creates the schema.**  
   **Incorrect**.

2. ❌ **B. The Kafka broker throws an exception.**  
   **Incorrect**.

3. ✅ **C. The schema gets fetched from the Schema Registry.**  
   **Correct**.

4. ❌ **D. The producer registers the schema to the Schema Registry.**  
   **Incorrect**.

</details>

## Question 36 (Reliable Data Delivery):
In a Kafka producer application configured for Exactly-Once Semantics, what is the role of the transactional.id configuration property?

- A. It specifies the producer‘s unique identifier
- B. It defines the Kafka topic for Exactly-Once Semantics
- C. It enables idempotent producer behavior
- D. It sets the isolation level for transactions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

It specifies the producer‘s unique identifier. Explanation: In a Kafka producer application configured for Exactly-Once Semantics, the transactional.id configuration property specifies the producer‘s unique identifier. This identifier is used to associate the producer with a specific transactional context, allowing the producer to participate in transactions and ensuring that messages are produced with strong guarantees of exactly-once processing semantics when combined with the necessary transactional operations in your code.

**Detailed explanation of each option:**

1. ✅ **A. It specifies the producer‘s unique identifier**  
   **Correct**.

2. ❌ **B. It defines the Kafka topic for Exactly-Once Semantics**  
   **Incorrect**.

3. ❌ **C. It enables idempotent producer behavior**  
   **Incorrect**.

4. ❌ **D. It sets the isolation level for transactions**  
   **Incorrect**.

</details>

## Question 37 (Kafka Internals):
Kafka cluster: 6 brokers Rack A → brokers 0, 1 Rack B → brokers 2, 3 Rack C → brokers 4, 5 Topic: 10 partitions, replication factor = 3 Partition 0: Leader → broker 4 (Rack C) First replica → broker 2 (Rack B) Question: Which broker can host the last replica? (Choose two)

- A. 5
- B. 1
- C. 3
- D. 0

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Option B. Broker 1 Correct because broker 1 is on Rack A, which is not yet represented. Kafka’s rack‑aware replica assignment ensures replicas are spread across racks for fault tolerance. Since racks B and C are already used (brokers 2 and 4), the last replica must be placed on Rack A. Option D. Broker 0 Correct for the same reason as broker 1. Broker 0 is also on Rack A, ensuring rack diversity. Either broker 0 or broker 1 can host the final replica, satisfying the replication factor of 3 across different racks. Incorrect Option A. Broker 5 Incorrect because broker 5 is on Rack C, which already hosts the leader (broker 4). Placing another replica on the same rack reduces fault tolerance. Option C. Broker 3 Incorrect because broker 3 is on Rack B, which already hosts a replica (broker 2). Again, this would violate rack‑aware distribution.

**Detailed explanation of each option:**

1. ❌ **A. 5**  
   **Incorrect**.

2. ✅ **B. 1**  
   **Correct**.

3. ❌ **C. 3**  
   **Incorrect**.

4. ✅ **D. 0**  
   **Correct**.

</details>

## Question 38 (Kafka Setup and Operations):
How will you find out all the partitions where one or more of the replicas for the partition are not in-sync with the leader?

- A. kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
- B. kafka-topics.sh --broker-list localhost:9092 --describe --under-replicated-partitions
- C. kafka-topics.sh --zookeeper localhost:2181 --describe --unavailable- partitions
- D. kafka-topics.sh --zookeeper localhost:2181 --describe --under-replicated-partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To find out all the partitions where one or more replicas are not in-sync with the leader in Kafka, you should use the under-replicated-partitions option. Here’s why: Under-replicated partitions: This specifically indicates that one or more replicas are lagging behind the leader and are not in sync. This is the condition you’re looking for. Unavailable partitions: This indicates partitions that are completely unavailable, meaning there is no leader or replicas available. While this is a problem, it’s not the same as under-replication. Also, the kafka-topics.sh command can connect to kafka in two ways. Using the zookeeper flag, or the bootstrap-server flag. Bootstrap server is the modern way to connect to a kafka cluster. Therefore, the correct command is: kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions

**Detailed explanation of each option:**

1. ✅ **A. kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions**  
   **Correct**.

2. ❌ **B. kafka-topics.sh --broker-list localhost:9092 --describe --under-replicated-partitions**  
   **Incorrect**.

3. ❌ **C. kafka-topics.sh --zookeeper localhost:2181 --describe --unavailable- partitions**  
   **Incorrect**.

4. ❌ **D. kafka-topics.sh --zookeeper localhost:2181 --describe --under-replicated-partitions**  
   **Incorrect**.

</details>

## Question 39 (Kafka Core Concepts):
Which of the following options is not a Kafka guarantee? (Choose one)

- A. Consumers read messages in the order stored in a topic-partition and total ordering is guaranteed.
- B. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition.
- C. With a replication factor of N, producers and consumers can tolerate up to N - 1 brokers being down.
- D. Messages are appended to a topic-partition in the order they are sent.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. Consumers read messages in the order stored in a topic-partition and total ordering is guaranteed. This is the correct answer because Kafka guarantees message ordering within a single partition, not across all partitions of a topic. Key points: Kafka preserves the order of messages within each topic-partition. Consumers reading from the same partition receive messages in partition order. Kafka does not guarantee a total ordering across multiple partitions. If a topic has multiple partitions, messages in different partitions can be consumed independently and in different orders. Therefore, claiming that total ordering is guaranteed is incorrect. This statement is not a Kafka guarantee. Incorrect Option B. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition. This is generally a Kafka guarantee when using the default key-based partitioning strategy. Kafka uses the message key to determine the partition. With a constant partition count and consistent partitioning strategy, the same key maps to the same partition. This ensures messages with the same key are routed to the same partition. Option C. With a replication factor of N, producers and consumers can tolerate up to N – 1 brokers being down. This describes Kafka’s replication-based fault tolerance, assuming appropriate replica placement and configuration. Each partition has one leader and multiple replicas. Replication provides redundancy if brokers fail. With a replication factor of N, up to N – 1 replicas can be unavailable while one replica remains. However, actual producer and consumer availability depends on settings such as min.insync.replicas, acks, and leader election. Option D. Messages are appended to a topic-partition in the order they are sent. This is a Kafka guarantee within a topic-partition. Kafka appends messages to a partition sequentially. Messages receive increasing offsets within that partition. Consumers read messages according to their offsets.

**Detailed explanation of each option:**

1. ✅ **A. Consumers read messages in the order stored in a topic-partition and total ordering is guaranteed.**  
   **Correct**.

2. ❌ **B. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition.**  
   **Incorrect**.

3. ❌ **C. With a replication factor of N, producers and consumers can tolerate up to N - 1 brokers being down.**  
   **Incorrect**.

4. ❌ **D. Messages are appended to a topic-partition in the order they are sent.**  
   **Incorrect**.

</details>

## Question 40 (Kafka Setup and Operations):
How does Kafka handle security for data in transit between producers and brokers?

- A. No encryption
- B. SSL/TLS encryption
- C. IP whitelisting
- D. Consumer authentication

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. SSL/TLS encryption Correct because Kafka supports SSL/TLS encryption to secure data in transit between producers, brokers, and consumers. This ensures that messages are encrypted during transmission, protecting against eavesdropping and man-in-the-middle attacks. SSL/TLS also provides authentication through certificates, strengthening Kafka’s security posture. Incorrect Option A. No encryption Incorrect because Kafka does not leave data unprotected by default when security is enabled. Without SSL/TLS, data would be transmitted in plaintext, but Kafka provides encryption mechanisms to prevent this. Option C. IP whitelisting Incorrect because IP whitelisting is a network-level access control mechanism, not a method for securing data in transit. While it can restrict which clients connect, it does not encrypt or secure the actual data flow. Option D. Consumer authentication Incorrect because authentication ensures that only authorized consumers can connect, but it does not secure the data in transit. Authentication is important, but encryption (SSL/TLS) is the mechanism that protects the data itself during transmission.

**Detailed explanation of each option:**

1. ❌ **A. No encryption**  
   **Incorrect**.

2. ✅ **B. SSL/TLS encryption**  
   **Correct**.

3. ❌ **C. IP whitelisting**  
   **Incorrect**.

4. ❌ **D. Consumer authentication**  
   **Incorrect**.

</details>

## Question 41 (Kafka Connect):
You are troubleshooting a Kafka Connect Sink Connector that is not writing records to a target database. What Kafka tool can help you view the status and details of connectors, tasks, and worker configurations?

- A. Kafka Manager
- B. Kafka Streams
- C. Kafka Control Center
- D. Kafka Connect REST API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The correct answer is Kafka Connect REST API. Reason: To troubleshoot a Kafka Connect Sink Connector, the Kafka Connect REST API provides a way to view the status and details of connectors, tasks, and worker configurations. This API allows you to interact with Kafka Connect, monitor connector statuses, and retrieve configuration details, which is critical for troubleshooting. While other tools like Kafka Manager, Kafka Streams, and Kafka Control Center are useful in managing and monitoring Kafka clusters, they do not specifically provide the detailed status and configurations of Kafka Connectors like the Kafka Connect REST API does. So, the answer is Kafka Connect REST API.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Manager**  
   **Incorrect**.

2. ❌ **B. Kafka Streams**  
   **Incorrect**.

3. ❌ **C. Kafka Control Center**  
   **Incorrect**.

4. ✅ **D. Kafka Connect REST API**  
   **Correct**.

</details>

## Question 42 (Programming & Serialization):
I am producing Avro data on my Kafka cluster that is integrated with the Confluent Schema Registry. After a schema change that is incompatible, I know my data will be rejected. Which component will reject the data?

- A. The Kafka Broker
- B. The Kafka Producer itself
- C. Zookeeper
- D. The Confluent Schema Registry

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

D. The Confluent Schema Registry The Confluent Schema Registry is the authoritative service that stores all schemas and enforces the defined compatibility rules (e.g., BACKWARD, FORWARD, FULL) for each schema subject. When a Kafka producer’s Avro serializer detects a new schema (or the schema changes), it sends an API request (usually HTTP) to the Schema Registry to register the new version. The Schema Registry server receives this request and runs the necessary compatibility check against the existing latest schema for that subject. If the check fails (i.e., the change is incompatible), the Schema Registry rejects the request and sends an error response back to the client. This rejection stops the serialization process and prevents the message from ever reaching the Kafka Broker. Incorrect: A. The Kafka Broker The Kafka Broker’s role is message storage and replication. It operates at the byte level and does not possess the logic to validate application-level data schemas like Avro or communicate with the Schema Registry for compatibility checks. It relies on the client (producer) to send valid messages. B. The Kafka Producer itself The Kafka Producer is the client application that initiates the schema registration request and receives the rejection response from the Schema Registry. It is the component that throws the final SerializationException to the application, but it is the Schema Registry server that makes the decision to reject the schema based on compatibility rules. The producer is the consumer of the rejection, not the component that performs the compatibility validation logic. C. Zookeeper Zookeeper (or the Kafka Controller in KRaft) manages the metadata, state, and coordination of the Kafka cluster. It is not involved in application-level data governance, schema storage, or compatibility checking, which are functions delegated entirely to the Schema Registry.

**Detailed explanation of each option:**

1. ❌ **A. The Kafka Broker**  
   **Incorrect**.

2. ❌ **B. The Kafka Producer itself**  
   **Incorrect**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ✅ **D. The Confluent Schema Registry**  
   **Correct**.

</details>

## Question 43 (Programming & Serialization):
If I want to send binary data through the REST proxy to topic “test_binary“, it needs to be base64 encoded. A consumer connecting directly into the Kafka topic “test_binary“ will receive

- A. json data
- B. avro data
- C. base64 encoded data, it will need to decode it
- D. binary data

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Base64 encoded data, it will need to decode it Correct because when binary data is sent through the Kafka REST Proxy, it must be base64 encoded to be transmitted as JSON. The Kafka topic stores the encoded payload exactly as sent. Therefore, a consumer connecting directly to the topic will receive the base64 encoded string, not the raw binary. The consumer must explicitly decode the base64 string back into binary before using it. Incorrect Option A. JSON data Incorrect because the REST Proxy wraps the payload in JSON for transmission, but the actual Kafka topic stores the encoded binary string, not JSON. Consumers reading directly from Kafka do not see JSON formatting. Option B. Avro data Incorrect because Avro serialization requires a schema and is not the default format for binary data sent through REST Proxy. Unless explicitly configured with Avro, the topic will not store Avro data. Option D. Binary data Incorrect because the REST Proxy does not send raw binary directly into Kafka. It always encodes binary into base64 before writing to the topic.

**Detailed explanation of each option:**

1. ❌ **A. json data**  
   **Incorrect**.

2. ❌ **B. avro data**  
   **Incorrect**.

3. ✅ **C. base64 encoded data, it will need to decode it**  
   **Correct**.

4. ❌ **D. binary data**  
   **Incorrect**.

</details>

## Question 44 (Kafka Connect):
Which of the following is not considered an internal Kafka Connect topic?

- A. connect-status
- B. connect-offsets
- C. connect-jars
- D. connect-configs

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

connect-jarsIn Kafka Connect, there are several internal topics that are used for managing the state and configuration of connectors. These include:connect-status: This topic stores the state of all connectors and tasks, including whether they are running, paused, or failed.connect-offsets: This topic stores the offsets for each source connector, keeping track of the data that has already been read and processed.connect-configs: This topic stores the configuration of all connectors and tasks.However, there is no internal topic named connect-jars. Kafka Connect does not use a dedicated topic for storing connector jars or plugins. Instead, connector plugins are typically provided as part of the Kafka Connect runtime environment or are placed in a directory where Kafka Connect can load them upon startup.

**Detailed explanation of each option:**

1. ❌ **A. connect-status**  
   **Incorrect**.

2. ❌ **B. connect-offsets**  
   **Incorrect**.

3. ✅ **C. connect-jars**  
   **Correct**.

4. ❌ **D. connect-configs**  
   **Incorrect**.

</details>

## 🚫 Question 45 (Kafka Ecosystem):
You are dealing with a scenario where events in a Kafka topic have timestamps, and you want to calculate the difference in time between consecutive events in KSQL. What KSQL function should you use for timestamp difference calculation?

- A. TIMESTAMPDIFF
- B. DATEDIFF
- C. TIMEDELTA
- D. TIMESPAN

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

TIMESTAMPDIFF. To calculate the difference in time between consecutive events with timestamps in KSQL, you should use the TIMESTAMPDIFF function. The TIMESTAMPDIFF function allows you to compute the time difference between two timestamp values, which can be useful for analyzing the time intervals between events in a Kafka stream or table.

**Detailed explanation of each option:**

1. ✅ **A. TIMESTAMPDIFF**  
   **Correct**.

2. ❌ **B. DATEDIFF**  
   **Incorrect**.

3. ❌ **C. TIMEDELTA**  
   **Incorrect**.

4. ❌ **D. TIMESPAN**  
   **Incorrect**.

</details>

## Question 46 (Reliable Data Delivery):
A kafka topic has a replication factor of 3 and min.insync.replicas setting of 1. What is the maximum number of brokers that can be down so that a producer with acks=all can still produce to the topic?

- A. 3
- B. 1
- C. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In the given scenario with a Kafka topic having: Replication factor of 3: This means there are 3 copies of the data stored across different brokers. min.insync.replicas setting of 1: This indicates that at least 1 replica needs to be in sync (have the latest data) for the producer with acks=all to acknowledge successful write. Here’s how this configuration affects producer behavior with acks=all: acks=all: The producer waits for an acknowledgment from all in-sync replicas before considering the write successful. Now, let’s analyze the number of brokers that can be down while still allowing writes: Option A (3): Incorrect. If 3 brokers are down, all replicas would be down, violating the min.insync.replicas requirement. The producer wouldn’t be able to write. Option B (1): Incorrect. Even with 1 broker down, there might not be an in-sync replica remaining (depending on which broker goes down) if the other two replicas haven’t caught up yet. The min.insync.replicas requirement wouldn’t be met. Option C (2): Correct. With a replication factor of 3 and min.insync.replicas of 1, you can tolerate a maximum of 2 brokers being down. This is because: Even if 2 brokers are down, 1 out of the 3 replicas will still be up (assuming it’s in sync). This remaining in-sync replica satisfies the min.insync.replicas setting, allowing the producer with acks=all to successfully write data. Therefore, with this configuration, you can have a maximum of 2 brokers down while maintaining data availability for writes with acks=all.

**Detailed explanation of each option:**

1. ❌ **A. 3**  
   **Incorrect**.

2. ❌ **B. 1**  
   **Incorrect**.

3. ✅ **C. 2**  
   **Correct**.

</details>

## Question 47 (Reliable Data Delivery):
A kafka topic has a replication factor of 3 and min.insync.replicas setting of 2. How many brokers can go down before a producer with acks=1 can‘t produce?

- A. 1
- B. 3
- C. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

2 brokers Here’s the breakdown: Replication factor of 3: This means that each message is replicated to 3 brokers in the cluster. min.insync.replicas of 2: This setting requires that a message must be written to at least 2 replicas before the producer receives a successful acknowledgment. Therefore, if 2 brokers go down, there will still be 1 broker with the replicated message. Since the min.insync.replicas setting is 2, the producer can still successfully produce messages. However, if 3 brokers go down, there will be no remaining brokers with the replicated message. In this case, the producer will fail to produce messages with acks=1, as it requires at least 2 replicas to acknowledge the message.

**Detailed explanation of each option:**

1. ❌ **A. 1**  
   **Incorrect**.

2. ❌ **B. 3**  
   **Incorrect**.

3. ✅ **C. 2**  
   **Correct**.

</details>

## Question 48 (Programming & Serialization):
Which of the following options best describe the benefits of the Confluent Schema Registry?

- A. Confluent Schema Registry is a distributed storage layer for schemas which uses Kafka as its underlying storage mechanism.
- B. Confluent Schema Registry is included in your Kafka brokers and helps to retrieve schemas that describe the data models for the messages.
- C. Confluent Schema Registry allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.
- D. Confluent Schema Registry provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and XML schemas.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. “Confluent Schema Registry allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.” This is correct because Schema Registry enforces schema evolution rules (backward, forward, full compatibility). It ensures producers and consumers can evolve schemas safely without breaking applications. It supports multiple schema formats such as Avro, JSON Schema, and Protobuf. Incorrect Option A. “Confluent Schema Registry is a distributed storage layer for schemas which uses Kafka as its underlying storage mechanism.” Incorrect because Schema Registry is not simply a storage layer built on Kafka. While it can leverage Kafka for distribution, schemas are managed independently by the Schema Registry service. Option B. “Confluent Schema Registry is included in your Kafka brokers and helps to retrieve schemas that describe the data models for the messages.” Incorrect because Schema Registry is a separate service, not embedded in Kafka brokers. It does help retrieve schemas, but the claim of being “included in brokers” is factually wrong. Option D. “Confluent Schema Registry provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and XML schemas.” Incorrect because Schema Registry does provide a RESTful interface, but it supports Avro, JSON Schema, and Protobuf. XML is not supported, making this option invalid.

**Detailed explanation of each option:**

1. ❌ **A. Confluent Schema Registry is a distributed storage layer for schemas which uses Kafka as its underlying storage mechanism.**  
   **Incorrect**.

2. ❌ **B. Confluent Schema Registry is included in your Kafka brokers and helps to retrieve schemas that describe the data models for the messages.**  
   **Incorrect**.

3. ✅ **C. Confluent Schema Registry allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.**  
   **Correct**.

4. ❌ **D. Confluent Schema Registry provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and XML schemas.**  
   **Incorrect**.

</details>

## Question 49 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for FORWARD schema evolution?

- A. Delete optional fields
- B. Delete fields
- C. Add fields
- D. Add optional fields

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The correct answer is C. Add fields. A. Delete optional fields (Incorrect) Deleting an optional field is actually a Backward compatible change. In Forward evolution, if a new producer deletes a field that an old consumer expects to find, the old consumer may fail to process the record because it doesn’t know the field is gone. B. Delete fields (Incorrect) Similar to option A, deleting any field prevents an old consumer from reading new data if that consumer’s schema still requires that field. C. Add fields (Correct) In Forward compatibility, the primary allowed change is adding new fields. Since old consumers are using an older version of the schema, they will simply ignore the new fields they don’t recognize. This allows the old consumer to continue functioning without error even though the data format has evolved. D. Add optional fields (Incorrect) While adding an optional field is generally safe, it is specifically the requirement for Backward compatibility (ensuring new consumers can provide a default value for missing data in old records). For Forward compatibility, the fields added don’t strictly need to be optional because the old consumer isn’t looking for them anyway. Key Concept: Forward Compatibility In a Forward compatibility strategy, the goal is to transition from Schema V1 to Schema V2 without breaking consumers still running V1. The old consumer receives a V2 record, sees a field it doesn’t recognize, and ignores it while processing the rest of the record successfully. CCDAK Quick Reference BACKWARD: New consumers can read old data. (Rule: Add optional fields or Delete fields). FORWARD: Old consumers can read new data. (Rule: Add fields or Delete optional fields). FULL: Both Forward and Backward compatible. (Rule: Only add or delete optional fields).

**Detailed explanation of each option:**

✅ C — Add fields (without default value)

Old schema: {name, age}
New schema:  {name, age, email} ← no default

Old consumer reads new data:
→ New data has "email" field
→ Old consumer does NOT know "email" field
→ Simply ignores unknown field ✅
→ FORWARD compatible ✅


❌ A — Delete optional fields (with default value)

Old schema: {name, age, email(default="")}
New schema:  {name, age}

Old consumer reads new data:
→ New data does NOT have "email"
→ Old schema has default="" → uses it ✅
→ FORWARD compatible ✅

BUT also BACKWARD compatible!
→ This is FULL compatible, not only FORWARD
→ Not EXCLUSIVELY forward!


❌ B — Delete fields (without default value)

Old schema: {name, age, email} ← no default
New schema:  {name, age}

Old consumer reads new data:
→ New data does NOT have "email"
→ Old schema expects "email" with no default
→ ERROR! ❌
→ NOT FORWARD compatible!
→ This is BACKWARD compatible only!


❌ D — Add optional fields (with default value)

Old schema: {name, age}
New schema:  {name, age, email(default="")}

Old consumer reads new data:
→ New data has "email" field
→ Old consumer simply ignores unknown field ✅
→ FORWARD compatible ✅

BUT also BACKWARD compatible!
→ This is FULL compatible, not only FORWARD
→ Not EXCLUSIVELY forward!

</details>

## Question 50 (Kafka Internals):
Suppose you have 6 brokers and you decide to create a topic with 10 partitions and a replication factor of 3. The brokers 0 and 1 are on rack A, the brokers 2 and 3 are on rack B, and the brokers 4 and 5 are on rack C. If the leader for partition 0 is on broker 4, and the first replica is on broker 2, which broker should host the last replica to preserve rack-aware placement?

- A. 5
- B. 2
- C. 0
- D. 3
- E. 1

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** C, E

**Explanation:**

With rack-aware replica placement, Kafka spreads a partition's replicas across as many distinct racks as possible. Current placement:
- Leader: broker 4 → rack C
- First replica: broker 2 → rack B

Racks C and B are already used, so the last replica should go on the only remaining rack, **rack A** (brokers 0 and 1). Broker 0 is a valid choice too, but it is not offered here; among the given options only **broker 1 (rack A)** preserves rack diversity.

**Detailed explanation of each option:**

1. ❌ **A. 5**  
   **Incorrect**. Broker 5 is on rack C, the same rack as the leader (broker 4) — it would reduce rack diversity.

2. ❌ **B. 2**  
   **Incorrect**. Broker 2 already hosts the first replica; the same broker cannot host two replicas of the same partition.

3. ✅ **C. 0**  
   **Correct**. Broker 1 is on rack A, which is not yet used by this partition, so it maintains replicas across three distinct racks (A, B, C).

4. ❌ **D. 3**  
   **Incorrect**. Broker 3 is on rack B, the same rack as the existing first replica (broker 2), so it does not add rack-level diversity.

5. ✅ **E. 1**  
   **Correct**. Broker 1 is on rack A, which is not yet used by this partition, so it maintains replicas across three distinct racks (A, B, C).


</details>

## Question 51 (Kafka Core Concepts):
Scenario: You are asked: Which of the following options is not a Kafka guarantee?

- A. With a replication factor of N, producers and consumers can tolerate up to N - 1 brokers being down.
- B. Consumers read messages in the order stored in a topic-partition and total ordering is guaranteed.
- C. Messages are appended to a topic-partition in the order they are sent.
- D. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. Consumers read messages in the order stored in a topic‑partition and total ordering is guaranteed. Correct because Kafka guarantees ordering only within a single partition, not across the entire topic. There is no global ordering across multiple partitions. Therefore, the statement that “total ordering is guaranteed” is not true and is the correct answer to the question. Incorrect Option A. With a replication factor of N, producers and consumers can tolerate up to N − 1 brokers being down. Incorrect because this is a valid Kafka guarantee. With replication factor N, Kafka can tolerate up to N − 1 broker failures while still maintaining data availability. Option C. Messages are appended to a topic‑partition in the order they are sent. Incorrect because Kafka guarantees that messages sent by a producer to a single partition are appended in the order they are produced. This ordering is preserved per partition. Option D. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition. Incorrect because Kafka uses a consistent hashing mechanism for keys. As long as the partition count does not change, the same key will always map to the same partition, ensuring deterministic placement.

**Detailed explanation of each option:**

1. ❌ **A. With a replication factor of N, producers and consumers can tolerate up to N - 1 brokers being down.**  
   **Incorrect**.

2. ✅ **B. Consumers read messages in the order stored in a topic-partition and total ordering is guaranteed.**  
   **Correct**.

3. ❌ **C. Messages are appended to a topic-partition in the order they are sent.**  
   **Incorrect**.

4. ❌ **D. As long as the number of partitions remains constant for a topic, the same key will always go to the same partition.**  
   **Incorrect**.

</details>

## 🚫 Question 52 (Kafka Setup and Operations):
You are using Confluent REST Proxy in a secure environment, and you want to enforce the use of SSL for all communications. What configuration setting should you adjust to achieve this?

- A. ssl.required
- B. ssl.enabled
- C. security.protocol
- D. ssl.key.password

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The correct configuration setting to enforce the use of SSL for all communications with Confluent REST Proxy in a secure environment is: security.protocol Explanation: security.protocol This setting controls the security protocol used for communication. 1 By setting it to “SSL” or “TLS” (depending on your specific SSL/TLS version requirements), you explicitly mandate that all connections must be encrypted. 1. Deploy Secure Standalone REST Proxy in Confluent Platform Other options and their purposes: ssl.required: This setting is often used in conjunction with security.protocol. It further enforces the use of SSL/TLS by making it mandatory for all connections. ssl.enabled: This setting generally controls whether SSL/TLS is enabled or disabled. However, it’s often considered less granular than security.protocol. ssl.key.password: This setting is used to specify the password for the private key used for SSL/TLS encryption. It’s crucial for securing the server’s identity. Example Configuration: YAML listeners: - name: plain port: 8082 protocol: PLAINTEXT - name: https port: 8083 protocol: HTTPS security.protocol: SSL In this example: The plain listener allows unencrypted connections (for demonstration or testing purposes). The https listener enforces SSL/TLS communication by setting security.protocol to “SSL”. Important Notes: Ensure that the necessary SSL certificates and keys are properly configured and accessible to the Confluent REST Proxy. Refer to the official Confluent documentation for the most accurate and up-to-date configuration guidelines. Always prioritize security best practices when configuring any system, including proper certificate management and key protection. By setting security.protocol to “SSL” or “TLS”, you effectively enforce the use of secure encryption for all communication with your Confluent REST Proxy, enhancing the security and confidentiality of your data.

**Detailed explanation of each option:**

1. ❌ **A. ssl.required**  
   **Incorrect**.

2. ❌ **B. ssl.enabled**  
   **Incorrect**.

3. ✅ **C. security.protocol**  
   **Correct**.

4. ❌ **D. ssl.key.password**  
   **Incorrect**.

</details>

## 🚫 Question 53 (Kafka Ecosystem):
Using ksqlDB or Kafka Streams, what happens to internal topics if automatic topic creation is turned off? (Choose one)

- A. ksqlDB and Kafka Streams applications will break as topics cannot be created.
- B. Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on.
- C. Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created.
- D. ksqlDB and Kafka Streams applications continue to work as topics are still created.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. ksqlDB and Kafka Streams applications will break as topics cannot be created. When automatic topic creation is disabled in Kafka, the broker will not automatically create topics when applications attempt to use topics that do not already exist. Both ksqlDB and Kafka Streams rely on internal Kafka topics to maintain application state and processing information. Examples of internal topics include: ** repartition topics:** Used when records need to be redistributed between partitions. Changelog topics: Used to store state-store updates and support recovery. Internal processing topics: Used to support stream processing operations. If these required topics do not exist and automatic creation is disabled, applications cannot successfully create or use them unless the topics are provisioned separately. Therefore, the applications can fail when required internal topics cannot be created. Incorrect Option B. Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on. Incorrect because new applications do not automatically override the Kafka broker’s automatic topic creation setting. The broker-level configuration applies to topic creation requests regardless of whether the application is new or existing. Option C. Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created. Incorrect because existing applications may also require new internal topics during processing, scaling, repartitioning, or state-store changes. Disabling automatic topic creation can therefore affect both existing and new applications. Option D. ksqlDB and Kafka Streams applications continue to work as topics are still created. Incorrect because disabling automatic topic creation prevents Kafka brokers from automatically creating missing topics. Required internal topics must be created explicitly or provisioned through the appropriate application and administrative mechanisms.

**Detailed explanation of each option:**

1. ✅ **A. ksqlDB and Kafka Streams applications will break as topics cannot be created.**  
   **Correct**.

2. ❌ **B. Existing ksqlDB and Kafka Streams applications will break but new applications use the default topic creation property, which is turned on.**  
   **Incorrect**.

3. ❌ **C. Existing ksqlDB and Kafka Streams applications continue to work but new applications will break as topics cannot be created.**  
   **Incorrect**.

4. ❌ **D. ksqlDB and Kafka Streams applications continue to work as topics are still created.**  
   **Incorrect**.

</details>

## Question 54 (Kafka Connect):
What is the recommended method for importing data from external databases?

- A. Confluent REST Proxy
- B. Kafka Connect Sink
- C. Kafka Streams
- D. Kafka Connect Source

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Connect SourceTo import data from external databases into Kafka, you should use Kafka Connect with a Source connector. Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. A Source connector is used to import data from an external system into Kafka.Kafka Connect Source: This is the correct choice for importing data from external databases. Source connectors can read from external systems (like databases) and write that data to Kafka topics.The other options serve different purposes:Confluent REST Proxy: This is used to produce and consume messages from Kafka topics via RESTful HTTP APIs. It‘s not specifically designed for importing data from external databases.Kafka Connect Sink: This is the opposite of a Source connector. Sink connectors are used to export data from Kafka topics to external systems, not to import data into Kafka.Kafka Streams: This is a client library for building applications and microservices that process and analyze data stored in Kafka. While Kafka Streams can read data from Kafka topics, it‘s not used for importing data from external databases into Kafka.

**Detailed explanation of each option:**

1. ❌ **A. Confluent REST Proxy**  
   **Incorrect**.

2. ❌ **B. Kafka Connect Sink**  
   **Incorrect**.

3. ❌ **C. Kafka Streams**  
   **Incorrect**.

4. ✅ **D. Kafka Connect Source**  
   **Correct**.

</details>
