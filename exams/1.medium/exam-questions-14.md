## Question 1 (Kafka Consumers):
Which of the following options are true regarding multi-threaded-message processing for Java Kafka clients?(Choose two)

- A. The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.
- B. The Kafka producer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.
- C. One Kafka producer can be safely used in multiple threads.
- D. One Kafka consumer can be safely used in multiple threads.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Multithreading is the ability of a central processing unit (CPU) to provide multiple threads of execution concurrently, supported by the operating system. In situations where the work can be divided into smaller units, which can be run in parallel, without negative effects on data consistency, multithreading can be used to improve application performance. When implementing a multi-threaded consumer architecture, it is important to note that the Kafka consumer is not thread safe. Multi-threaded access must be properly synchronized, which can be tricky. This is why the single-threaded model is commonly used. Kafka producers are thread safe, which means one Kafka producer can be safely used in multiple threads. Further reading: Confluent Multi-Threaded Consumer.

**Detailed explanation of each option:**

1. ✅ **A. The Kafka consumer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.**  
   **Correct**.

2. ❌ **B. The Kafka producer is not thread-safe and it is the responsibility of the user to ensure that multi-threaded access is properly synchronized.**  
   **Incorrect**.

3. ✅ **C. One Kafka producer can be safely used in multiple threads.**  
   **Correct**.

4. ❌ **D. One Kafka consumer can be safely used in multiple threads.**  
   **Incorrect**.

</details>

## Question 2 (Kafka Core Concepts):
You are designing a Kafka topic and want to ensure that messages are retained for a specified duration. What configuration should you adjust?

- A. Replication factor
- B. Producer acknowledgment setting
- C. Consumer fetch size
- D. Topic retention period

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The configuration you should adjust is the “Topic retention period.“ Explanation: Adjusting the topic retention period in Kafka allows you to control how long messages are retained in a topic. This duration is specified in the configuration of the Kafka topic. Setting an appropriate retention period ensures that messages are retained for the desired duration before being automatically deleted. This configuration is crucial for various use cases where data persistence and retention policies are essential, such as auditing, compliance, or downstream data processing requirements.

**Detailed explanation of each option:**

1. ❌ **A. Replication factor**  
   **Incorrect**.

2. ❌ **B. Producer acknowledgment setting**  
   **Incorrect**.

3. ❌ **C. Consumer fetch size**  
   **Incorrect**.

4. ✅ **D. Topic retention period**  
   **Correct**.

</details>

## 🚫 Question 3 (Kafka Ecosystem):
In a scenario where you want to create a new stream in KSQL by selecting specific fields from an existing stream and renaming them while also converting the data types of certain fields. What KSQL statement should you use for this operation?

- A. CREATE STREAM
- B. SELECT
- C. RENAME STREAM
- D. GENERATE STREAM

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In KSQL, to create a new stream by selecting specific fields from an existing stream, renaming them, and converting data types, you should use the following statement: CREATE STREAM … AS SELECT Explanation: The CREATE STREAM … AS SELECT statement in KSQL is used to create a new stream by selecting specific fields from an existing stream and applying transformations as needed. This includes renaming fields and converting data types.

**Detailed explanation of each option:**

1. ✅ **A. CREATE STREAM**  
   **Correct**.

2. ❌ **B. SELECT**  
   **Incorrect**.

3. ❌ **C. RENAME STREAM**  
   **Incorrect**.

4. ❌ **D. GENERATE STREAM**  
   **Incorrect**.

</details>

## Question 4 (Reliable Data Delivery):
Due to network errors a producer can introduce duplicate messages in Kafka, for example, if a message is processed, but the acknowledgment never reaches the producer. Which producer configuration can be used to guarantee a stable and safe pipeline without processing duplicate messages?(Choose one)

- A. max.in.flight.requests=1
- B. acks=all
- C. enable.idempotence=true
- D. retries=Integer.MAX_VALUE

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When a producer sends messages to a topic, things can go wrong, such as short connection failures. When this happens, any messages that are pending acknowledgements can either be resent or discarded. The messages may have been successfully written to the topic, or not, there is no way to know. If we resend then we may duplicate the message, but if we dont resend then the message may essentially be lost.The idempotent producer feature addresses these issues ensuring that messages always get delivered, in the right order and without duplicates. All you need to do to turn this feature on is use the producer configuration “enable.idempotence=true“.Further reading: Idempotent Producer Configuration.

**Detailed explanation of each option:**

1. ❌ **A. max.in.flight.requests=1**  
   **Incorrect**.

2. ❌ **B. acks=all**  
   **Incorrect**.

3. ✅ **C. enable.idempotence=true**  
   **Correct**.

4. ❌ **D. retries=Integer.MAX_VALUE**  
   **Incorrect**.

</details>

## Question 5 (Kafka Consumers):
In a consumer group application, what internal consumer mechanism can be used to detect the application being down?(Choose one)

- A. Heartbeat thread
- B. Poll thread
- C. Push thread
- D. Offset thread

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Consumers in a group talk to a consumer group coordinator. To detect consumers that have processing issues or are down, there is a poll and a heartbeat mechanism:– Heartbeat thread: Heartbeats are sent periodically to the broker. If no heartbeat is sent during that period, the consumer is considered dead.– Poll thread: This is particularly relevant for Big Data frameworks like Spark in case the processing takes a lot of time. This mechanism detects data processing issues.

**Detailed explanation of each option:**

1. ✅ **A. Heartbeat thread**  
   **Correct**.

2. ❌ **B. Poll thread**  
   **Incorrect**.

3. ❌ **C. Push thread**  
   **Incorrect**.

4. ❌ **D. Offset thread**  
   **Incorrect**.

</details>

## Question 6 (Kafka Setup and Operations):
A company wants to mirror its production topic from the Europe region to 4 different regions worldwide. The environment should be highly available in every region and it should be possible to produce to the topic from everywhere. Using Mirror Maker, what kind of mirroring is this?(Choose one)

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

## Question 7 (Kafka Consumers):
In Kafka, what is the most important consumer configuration for throughput/performance? (Choose one)

- A. fetch size
- B. session timeout
- C. heartbeat interval
- D. key deserializer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

For consumer **throughput/performance**, the fetch sizing configurations (`fetch.min.bytes`, `fetch.max.bytes`, `max.partition.fetch.bytes`) are the most impactful: they control how much data the consumer pulls per fetch request, directly affecting network round-trips and throughput. `session.timeout.ms` and `heartbeat.interval.ms` govern group-membership/liveness detection, not throughput, and the `key.deserializer` is a mandatory functional setting but does not tune performance.

**Detailed explanation of each option:**

1. ✅ **A. fetch size**  
   **Correct**. Fetch sizing controls how much data is retrieved per request and is the primary lever for consumer throughput.

2. ❌ **B. session timeout**  
   **Incorrect**. Controls failure detection within the consumer group, not throughput.

3. ❌ **C. heartbeat interval**  
   **Incorrect**. Controls how often heartbeats are sent to the coordinator, not throughput.

4. ❌ **D. key deserializer**  
   **Incorrect**. Mandatory to function, but it does not tune performance.


</details>

## Question 8 (Kafka Producers):
Which acknowledgment configuration should be used for a producer to maximize performance?(Choose one)

- A. acks=1
- B. acks=leader
- C. acks=0
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka, producers create and write messages to topic partitions and producers can choose to receive acknowledgement of data writes, which can be configured using the acks property. It is the number of acknowledgments the producer requires the leader to have received before considering a request complete. This controls the durability of records that are sent.If acks=0 then the producer will not wait for any acknowledgment from the server at all. No guarantee can be made that the server has received the record in this case. However, because the producer is not waiting for any response from the server, it can send messages as fast as the network will support, so this setting can be used to achieve very high throughput.Further reading: Producer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. acks=1**  
   **Incorrect**.

2. ❌ **B. acks=leader**  
   **Incorrect**.

3. ✅ **C. acks=0**  
   **Correct**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## Question 9 (Kafka Producers):
A Kafka producer is producing at a very high rate and the batches are completely full each time. Which of the following additional configurations help to improve the producer throughput? (Choose two)

- A. Decrease linger.ms
- B. Increase linger.ms
- C. Enable compression
- D. Increase batch.size

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

To optimize for throughput, producers and consumers must move as much data as possible within a given amount of time. For high throughput, try maximizing the rate at which the data moves. The data rate should be the fastest possible rate. Producer configurations to achieve a high throughput application are: – compression.type: Producers usually send data that is text-based, for example with JSON data. In this case, it is important to apply compression to optimize for throughput. Compression is more effective the bigger the batch of messages being sent to Kafka. Possible values are: lz4 (recommended for performance),snappy, zstd, gzip. – batch.size: With batching strategy of Kafka producers, you can batch messages going to the same partition, which means they collect multiple messages to send together in a single request. The most important step you can take to optimize throughput is to tune the producer batching to increase the batch size and the time spent waiting for the batch to populate with messages. Larger batch sizes result in fewer requests, which reduces load on producers and the broker CPU overhead to process each request. – linger.ms: It‘s the number of milliseconds a producer is willing to wait before sending a batch out (defaults to 0). By introducing some lag, we increase the changes of messages being sent together in a batch. If the batch is full (batch.size) before the end of linger.ms period, it will be sent to Kafka right away. Note: As the batch is full each time, it does not help to change the linger.ms configuration. Enabling compression can also help make more compact batches and increase the throughput of your producer. Further reading: Optimizing for Throughput.

**Detailed explanation of each option:**

1. ❌ **A. Decrease linger.ms**  
   **Incorrect**.

2. ❌ **B. Increase linger.ms**  
   **Incorrect**.

3. ✅ **C. Enable compression**  
   **Correct**.

4. ✅ **D. Increase batch.size**  
   **Correct**.

</details>

## Question 10 (Stream Processing):
A Kafka Streams application is processing records in a hopping window, and you need to output the intermediate results at fixed intervals. What Kafka Streams operation should you use for this fixed interval output requirement?

- A. filter
- B. map
- C. windowedBy
- D. suppress

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

o achieve fixed interval output for intermediate results in a Kafka Streams application processing records in a hopping window, you should use the suppress operation. Explanation: The suppress operation in Kafka Streams is used to control the emission of intermediate results within a specified time interval. It is particularly useful for scenarios where you want to produce output at fixed intervals and avoid emitting results for every event in the stream.

**Detailed explanation of each option:**

1. ❌ **A. filter**  
   **Incorrect**.

2. ❌ **B. map**  
   **Incorrect**.

3. ❌ **C. windowedBy**  
   **Incorrect**.

4. ✅ **D. suppress**  
   **Correct**.

</details>

## Question 11 (Kafka Core Concepts):
What are the drawbacks or shortcomings of using request/response communication?

- A. Cost
- B. Coupling
- C. Scalability
- D. Reliability

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The primary disadvantage of request/response communication is Coupling.Explanation:Coupling: In a request/response model, the client and server are tightly coupled. This means the client is dependent on the server‘s availability and response time. If the server is down or slow, the client‘s operation is directly affected. This tight coupling can lead to issues in maintainability and flexibility, especially in large, distributed systems.Cost: While cost can be a factor in any communication model, it‘s not a direct disadvantage of the request/response model itself. Costs are more related to the resources used, such as server capacity, network bandwidth, etc., rather than the communication pattern.Scalability: Request/response can be scalable, especially with modern architectures and technologies. However, scalability might be challenged in high-load scenarios due to the synchronous nature of request/response, but this is more of an operational challenge than a fundamental disadvantage of the model.Reliability: This model can be made reliable with the implementation of various techniques like retries, acknowledgments, and fault tolerance mechanisms. The model itself doesn‘t inherently reduce reliability; rather, reliability depends on the implementation and infrastructure supporting the model.

**Detailed explanation of each option:**

1. ❌ **A. Cost**  
   **Incorrect**.

2. ✅ **B. Coupling**  
   **Correct**.

3. ❌ **C. Scalability**  
   **Incorrect**.

4. ❌ **D. Reliability**  
   **Incorrect**.

</details>

## Question 12 (Programming & Serialization):
Using Avro schemas, what type of schema changes are allowed for FULL schema evolution?(Choose two)

- A. Add optional fields
- B. Add fields
- C. Delete fields
- D. Delete optional fields

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

An important aspect of data management is schema evolution. After the initial schema is defined, applications may need to evolve it over time. When this happens, it‘s critical for the downstream consumers to be able to handle data encoded with both the old and the new schema seamlessly. When using Avro or other schema formats, one of the most important things is to manage the schemas and consider how these schemas should evolve. Confluent Schema Registry is built for exactly that purpose. The Confluent Schema Registry default compatibility type is BACKWARD. Allowed changes for FULL compatibility are: – Add optional fields – Delete optional fields FULL compatibility means schemas are both backward and forward compatible. Schemas evolve in a fully compatible way: old data can be read with the new schema, and new data can also be read with the last schema. Further reading: Avro Schema Evolution.

**Detailed explanation of each option:**

1. ✅ **A. Add optional fields**  
   **Correct**.

2. ❌ **B. Add fields**  
   **Incorrect**.

3. ❌ **C. Delete fields**  
   **Incorrect**.

4. ✅ **D. Delete optional fields**  
   **Correct**.

</details>

## Question 13 (Kafka Connect):
A Kafka Connect Sink Connector is failing to write records to an Oracle database. What could be a potential reason for this issue?

- A. Incorrect connector.class setting
- B. Missing topics configuration
- C. Incorrect database connection URL
- D. Incompatible data types

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Incorrect database connection URL Correct because the most common reason a Kafka Connect Sink Connector fails to write to a database is an invalid or misconfigured JDBC connection string. If the Oracle database connection URL is incorrect (wrong hostname, port, service name, or syntax), the connector cannot establish a connection, and all writes will fail. This aligns with real‑world troubleshooting: always verify the JDBC URL and credentials first. Incorrect Option A. Incorrect connector.class setting Incorrect because if the connector.class is wrong, the connector would fail to start at all, not specifically fail when writing records. The scenario describes a connector that is running but failing to write, which points to a connection issue rather than a misconfigured class. Option B. Missing topics configuration Incorrect because missing topics would prevent the connector from consuming data from Kafka, not specifically cause failures when writing to Oracle. The connector would simply have no data to process, rather than failing on database writes. Option D. Incompatible data types Incorrect because while incompatible data types can cause individual record write errors, they are not the primary reason for a connector failing entirely to write records. The exam question emphasizes a broader configuration issue, not schema mismatch.

**Detailed explanation of each option:**

1. ❌ **A. Incorrect connector.class setting**  
   **Incorrect**.

2. ❌ **B. Missing topics configuration**  
   **Incorrect**.

3. ✅ **C. Incorrect database connection URL**  
   **Correct**.

4. ❌ **D. Incompatible data types**  
   **Incorrect**.

</details>

## Question 14 (Programming & Serialization):
You are migrating from an older version of Avro schema to a new version that includes changes. How does Confluent Schema Registry manage the compatibility of these schema versions during the migration process?

- A. By enforcing strict schema rules
- B. By automatically updating consumers
- C. By using schema validation
- D. By employing compatibility settings

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. By enforcing strict schema rules**  
   **Incorrect**.

2. ❌ **B. By automatically updating consumers**  
   **Incorrect**.

3. ❌ **C. By using schema validation**  
   **Incorrect**.

4. ✅ **D. By employing compatibility settings**  
   **Correct**.

</details>

## Question 15 (Kafka Internals):
You have a cluster with 3 brokers, and you aim to create a topic with a single partition that can withstand the failure of one broker and one broker undergoing maintenance. What replication factor should you set when creating the topic?

- A. 6
- B. 1
- C. 3
- D. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

For a topic to be resilient to one broker failure and one broker maintenance simultaneously in a cluster with 3 brokers, you should specify a replication factor of 3 while creating the topic.Explanation:A replication factor of 3 means that each message in the topic‘s partition will be replicated across all three brokers. This setup ensures that if one broker goes down (failure) and another needs to undergo maintenance, there is still one broker available with a copy of the data, ensuring the topic‘s availability and fault tolerance.A replication factor of 6 is not feasible since there are only 3 brokers in the cluster.A replication factor of 1 would mean no replication. If the broker hosting that partition fails or undergoes maintenance, the data in the partition would be unavailable.A replication factor of 2 would allow for resilience to either one broker failure or maintenance, but not both simultaneously. If one broker fails and another is under maintenance, there would be no available copy of the data.Therefore, a replication factor of 3 is the most appropriate choice in this scenario.

**Detailed explanation of each option:**

1. ❌ **A. 6**  
   **Incorrect**.

2. ❌ **B. 1**  
   **Incorrect**.

3. ✅ **C. 3**  
   **Correct**.

4. ❌ **D. 2**  
   **Incorrect**.

</details>

## Question 16 (Kafka Consumers):
Which of the following options are true for Kafka consumers?(Choose two)

- A. Consumers can read data from more than one partition.
- B. Consumer offsets are stored in Zookeeper.
- C. If you have more consumers than partitions, some consumers will read data from the same partition.
- D. Consumers read data in order within each topic partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Some concepts of consumers are: – Consumers read data from a topic partition identified by its name. – Consumers know which broker to read from. – In case of broker failures, consumers know how to recover. – Data is read in order within each topic partition. – A consumer can read from more than one partition but one partition is read from one consumer. – Consumer offsets are are stored as messages in a separate topic named “__consumer_offsets“. – Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application. – If there are more consumers than partitions, some consumers will be inactive (idle). Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Consumers can read data from more than one partition.**  
   **Correct**.

2. ❌ **B. Consumer offsets are stored in Zookeeper.**  
   **Incorrect**.

3. ❌ **C. If you have more consumers than partitions, some consumers will read data from the same partition.**  
   **Incorrect**.

4. ✅ **D. Consumers read data in order within each topic partition.**  
   **Correct**.

</details>

## Question 17 (Kafka Core Concepts):
What kind of universal unique identifier can be utilized for messages retrieved by a consumer?

- A. topic + partition + timestamp
- B. topic + timestamp
- C. topic + partition + offset

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

A generic unique identifier for messages received from a Kafka consumer would be:topic + partition + offsetExplanation:Topic + Partition + Offset: This combination is unique for each message within a Kafka cluster. The topic identifies the stream of data, the partition specifies the segment within the topic (as each topic can have multiple partitions), and the offset is a unique identifier for each message within a partition. Together, they uniquely identify a message.Topic + Partition + Timestamp: While this might seem unique, it‘s possible (though unlikely) for two messages in the same partition to have the same timestamp, especially if they are produced in rapid succession. Therefore, this combination cannot guarantee uniqueness.Topic + Timestamp: This is even less specific and can lead to collisions in high-throughput scenarios where multiple messages are produced with the same timestamp in different partitions of the same topic.

**Detailed explanation of each option:**

1. ❌ **A. topic + partition + timestamp**  
   **Incorrect**.

2. ❌ **B. topic + timestamp**  
   **Incorrect**.

3. ✅ **C. topic + partition + offset**  
   **Correct**.

</details>

## 🚫 Question 18 (Kafka Connect):
You are configuring a Kafka Connect Source Connector to read data from a Twitter stream. What configuration setting should you adjust to specify the Twitter API key?

- A. connector.class
- B. twitter.api.key
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To specify the Twitter API key when configuring a Kafka Connect Source Connector for reading data from a Twitter stream, you should adjust the configuration setting: twitter.api.key Explanation: The twitter.api.key configuration setting is typically used in Kafka Connect Source Connectors designed for reading data from Twitter streams. This setting allows you to provide the API key required for authenticating and accessing the Twitter API. When configuring the Kafka Connect Source Connector for Twitter, you would set the twitter.api.key parameter to the actual API key associated with your Twitter developer account. This key is essential for establishing a connection to the Twitter API and accessing the desired data streams. The other options: connector.class: This configuration setting specifies the class implementing the connector and is not specifically for providing the Twitter API key. topics: This setting is used to specify the Kafka topics from which the connector should consume data. key.converter: This setting determines the converter used for the key in the Kafka messages but is not related to specifying the Twitter API key.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. twitter.api.key**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## Question 19 (Stream Processing):
How can you naturally represent and structure the data from an e-commerce website, which sells custom-made products, using Kafka Streams?

- A. Purchase as stream, Product as table, Customer as table
- B. Purchase as stream, Product as stream, Customer as stream
- C. Purchase as table, Product as table, Customer as table
- D. Purchase as stream, Product as table, Customer as stream

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The natural way of modeling this data in Kafka Streams would typically be:Purchase as stream, Product as table, Customer as tableExplanation:Purchase as stream: Purchases are events that happen over time, and it‘s natural to represent them as a stream of events. Each purchase event can be a record in the stream.Product as table: Products are typically static or slowly changing data, such as product details, prices, and descriptions. They can be represented as a table or a state store in Kafka Streams, where the data is maintained as a snapshot that can be queried by joining with the purchase stream.Customer as table: Similarly, customer data, including information like customer profiles and addresses, is typically considered as static or slowly changing data. It‘s represented as a table or a state store that can be joined with the purchase stream.This modeling approach allows you to process purchase events as they occur in real-time while efficiently querying product and customer data from tables when needed for enriching or analyzing purchase events.

**Detailed explanation of each option:**

1. ✅ **A. Purchase as stream, Product as table, Customer as table**  
   **Correct**.

2. ❌ **B. Purchase as stream, Product as stream, Customer as stream**  
   **Incorrect**.

3. ❌ **C. Purchase as table, Product as table, Customer as table**  
   **Incorrect**.

4. ❌ **D. Purchase as stream, Product as table, Customer as stream**  
   **Incorrect**.

</details>

## Question 20 (Kafka Setup and Operations):
In the context of mirroring a “sales“ topic from the Americas region to the European region and subsequently reading it solely for analytics purposes, what type of mirroring arrangement does this represent?

- A. Passive-Passive
- B. Active-Passive
- C. Active-Active

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The scenario described is an example of Active-Passive mirroring.Explanation:Active-Passive: In this setup, the “sales“ topic in the Americas region is actively being produced to (Active), while the mirrored topic in the European region is only being used for reading or consuming data (Passive). The European region does not contribute any new data to the topic; it only mirrors the data from the Americas region for analytics purposes. This is a classic example of an active-passive replication model, where one system is the primary source of data, and the other is a secondary system used for data consumption or backup.Active-Active: In an active-active setup, both systems would be actively producing and consuming data, potentially even replicating data to each other. This is not the case in your scenario.Passive-Passive: This would imply that neither system is actively producing data to the topic, which does not fit your scenario as the Americas region is actively producing data.

**Detailed explanation of each option:**

1. ❌ **A. Passive-Passive**  
   **Incorrect**.

2. ✅ **B. Active-Passive**  
   **Correct**.

3. ❌ **C. Active-Active**  
   **Incorrect**.

</details>

## Question 21 (Kafka Consumers):
A company uses a consumer application to do complex big data calculations for the Kafka input data before writing the outputs into a data warehouse. The calculations take about 9 to 10 minutes to finish, but the consumer application rebalances even though the calculation is still running. What‘s the best solution to solve this problem?(Choose one)

- A. Increase session.timeout.ms to 20000.
- B. Decrease session.timeout.ms to 20000.
- C. Increase max.poll.interval.ms to 600000.
- D. Decrease max.poll.interval.ms to 600000.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Once the consumer subscribes to topics, the poll loop handles all details of coordination, partition rebalances, heartbeats, and data fetching, leaving the developer with a clean API that simply returns available data from the assigned partitions.The max.poll.interval.ms configuration is the maximum delay between invocations of poll() when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If poll() is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance in order to reassign the partitions to another member.Because the max.poll.interval.ms defaults to 5 minutes (300000 ms), but the processing takes about 9 to 10 minutes to finish we should at least double this value to solve the consumer issue.Further reading: Consumer Configurations.

**Detailed explanation of each option:**

1. ❌ **A. Increase session.timeout.ms to 20000.**  
   **Incorrect**.

2. ❌ **B. Decrease session.timeout.ms to 20000.**  
   **Incorrect**.

3. ✅ **C. Increase max.poll.interval.ms to 600000.**  
   **Correct**.

4. ❌ **D. Decrease max.poll.interval.ms to 600000.**  
   **Incorrect**.

</details>

## Question 22 (Kafka Consumers):
You want to increase the parallelism of message processing in a Kafka consumer. What configuration should you adjust?

- A. Consumer group size
- B. Replication factor
- C. Producer acknowledgment setting
- D. Topic retention period

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The configuration you should adjust to increase the parallelism of message processing in a Kafka consumer is the “Consumer group size.“ Explanation: The consumer group size determines the number of consumers that can work in parallel to process messages from a Kafka topic. Each consumer in a consumer group processes a subset of the partitions in the topic. By increasing the consumer group size, you can enhance parallelism, allowing more consumers to work concurrently and process messages from different partitions simultaneously. This can lead to improved throughput and reduced processing time for handling a larger volume of messages. Adjusting the consumer group size is a key factor in scaling the processing capacity of a Kafka consumer.

**Detailed explanation of each option:**

1. ✅ **A. Consumer group size**  
   **Correct**.

2. ❌ **B. Replication factor**  
   **Incorrect**.

3. ❌ **C. Producer acknowledgment setting**  
   **Incorrect**.

4. ❌ **D. Topic retention period**  
   **Incorrect**.

</details>

## Question 23 (Kafka Setup and Operations):
Which broker property needs to be used to specify that a broker belongs to a particular rack?(Choose one)

- A. broker.rack
- B. availability.zone
- C. availability.rack
- D. broker.zone

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The rack awareness feature spreads replicas of the same partition across different racks. This extends the guarantees Kafka provides for broker-failure to cover rack-failure, limiting the risk of data loss should all the brokers on a rack fail at once. The feature can also be applied to other broker groupings such as availability zones in EC2 (Amazon Web Services concept). You can specify that a broker belongs to a particular rack by adding a property to the broker config: broker.rack=my-rack-id Further reading: Kafka Racks.

**Detailed explanation of each option:**

1. ✅ **A. broker.rack**  
   **Correct**.

2. ❌ **B. availability.zone**  
   **Incorrect**.

3. ❌ **C. availability.rack**  
   **Incorrect**.

4. ❌ **D. broker.zone**  
   **Incorrect**.

</details>

## Question 24 (Programming & Serialization):
A Kafka consumer is encountering compatibility issues with a new Avro schema version. What action can you take using Confluent Schema Registry to resolve this issue without impacting the producer?

- A. Update the producer to use the latest schema
- B. Enable schema migration for the producer
- C. Adjust schema compatibility settings for the consumer
- D. Disable schema validation for the consumer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Adjust schema compatibility settings for the consumer Confluent Schema Registry allows you to control schema compatibility at the subject level. By adjusting compatibility settings (for example, BACKWARD, FORWARD, or FULL), you can ensure that existing consumers can continue to read data produced with newer Avro schema versions without requiring any changes to the producer. This resolves consumer compatibility issues while leaving producers unaffected. Incorrect: Option A. Update the producer to use the latest schema This directly impacts the producer and violates the requirement to resolve the issue without affecting it. The problem is on the consumer side, not the producer. Option B. Enable schema migration for the producer Schema migration involves producer-side changes and does not address consumer compatibility issues independently. It would still require modifying producer behavior. Option D. Disable schema validation for the consumer Disabling schema validation bypasses important safety checks and is not a recommended or standard approach in Confluent Schema Registry. It can lead to runtime errors and data integrity issues rather than properly resolving compatibility.

**Detailed explanation of each option:**

1. ❌ **A. Update the producer to use the latest schema**  
   **Incorrect**.

2. ❌ **B. Enable schema migration for the producer**  
   **Incorrect**.

3. ✅ **C. Adjust schema compatibility settings for the consumer**  
   **Correct**.

4. ❌ **D. Disable schema validation for the consumer**  
   **Incorrect**.

</details>

## Question 25 (Kafka Setup and Operations):
A company developed a sales producer application in their development environment without having any broker to client communication issues. The next step was to deploy the application into the cloud to scale globally in different regions worldwide. After copying the application into the cloud, the producer is able to connect to Kafka but unable to produce to the same Kafka topic because of an authorization issue. What‘s the likely issue?(Choose one)

- A. ACLs are configured for specific host IPs only.
- B. RBAC is not enabled by default for cloud deployments.
- C. Kafka topics cannot be copied into cloud environments and therefore it does not exist.
- D. Producer and Consumer operate in different regions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Access Control Lists (ACLs) provide important authorization controls for your enterprise‘s Kafka cluster data. The following command can be used to set the required ACLs to allow a specific user “Bob“ to read and write to the topic “test-topic“ from host “test-host“: bin/kafka-acls.sh –authorizer-properties zookeeper.connect=localhost:2181 –add –allow-principal User:Bob –allow-host test-host –operation read –operation write –topic test-topic This means, that the access to the topic test-topic is only allowed for the specified host. If you move the application to another host, the ACLs need to be updated. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ✅ **A. ACLs are configured for specific host IPs only.**  
   **Correct**.

2. ❌ **B. RBAC is not enabled by default for cloud deployments.**  
   **Incorrect**.

3. ❌ **C. Kafka topics cannot be copied into cloud environments and therefore it does not exist.**  
   **Incorrect**.

4. ❌ **D. Producer and Consumer operate in different regions.**  
   **Incorrect**.

</details>

## Question 26 (Kafka Setup and Operations):
In a Kafka cluster, what is the purpose of the security.protocol configuration setting?

- A. Enabling SSL/TLS encryption
- B. Configuring ACLs
- C. Authenticating consumers
- D. Controlling producer acknowledgment

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The purpose of the “security.protocol“ configuration setting in a Kafka cluster is: Enabling SSL/TLS encryption. Explanation: The “security.protocol“ configuration setting in Kafka is used to specify the security protocol used for communication between clients (producers and consumers) and brokers. Setting it to a value such as “SSL“ or “SASL_SSL“ enables SSL/TLS encryption for securing the data in transit between clients and brokers. This encryption helps protect sensitive information and ensures the confidentiality and integrity of the data being exchanged in a Kafka cluster.

**Detailed explanation of each option:**

1. ✅ **A. Enabling SSL/TLS encryption**  
   **Correct**.

2. ❌ **B. Configuring ACLs**  
   **Incorrect**.

3. ❌ **C. Authenticating consumers**  
   **Incorrect**.

4. ❌ **D. Controlling producer acknowledgment**  
   **Incorrect**.

</details>

## Question 27 (Kafka Consumers):
What‘s one of the main tasks of the consumer group leader? (Choose one)

- A. The group leader is one of the consumers in the consumer group and is responsible for sending requests to join the group.
- B. The group leader is one of the consumers in the consumer group and is responsible for storing all the consumer offsets to Kafka.
- C. The group leader is one of the consumers in the consumer group and is responsible for assigning a subset of topic partitions to each consumer.
- D. The group leader is one of the consumers in the consumer group and receives heartbeats from all consumers to trigger a rebalance, if one of the consumers isn‘t alive.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Applications that need to read data from Kafka use a KafkaConsumer to subscribe to Kafka topics and receive messages from these topics. Consumers read data in consumer groups. A consumer group is a set of consumers which cooperate to consume data from some topics and each consumer within a group reads messages from exclusive partitions. A consumer group basically represents an application.When a consumer wants to join a group, it sends a JoinGroup request to the group coordinator (one of the brokers). The first consumer to join the group becomes the group leader (one of the consumers in the consumer group). The leader receives a list of all consumers in the group from the group coordinator (this will include all consumers that sent a heartbeat recently and which are therefore considered alive) and is responsible for assigning a subset of partitions to each consumer. It uses an implementation of PartitionAssignor to decide which partitions should be handled by which consumer.Further reading: Consumer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. The group leader is one of the consumers in the consumer group and is responsible for sending requests to join the group.**  
   **Incorrect**.

2. ❌ **B. The group leader is one of the consumers in the consumer group and is responsible for storing all the consumer offsets to Kafka.**  
   **Incorrect**.

3. ✅ **C. The group leader is one of the consumers in the consumer group and is responsible for assigning a subset of topic partitions to each consumer.**  
   **Correct**.

4. ❌ **D. The group leader is one of the consumers in the consumer group and receives heartbeats from all consumers to trigger a rebalance, if one of the consumers isn‘t alive.**  
   **Incorrect**.

</details>

## Question 28 (Stream Processing):
Which approach should be used when transforming data from one Kafka topic to another one?(Choose one)

- A. Use ksqlDB.
- B. Use Kafka Connect Sink.
- C. Use Kafka Streams.
- D. Use a Consumer to consume from one topic and a Producer to produce to another topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Streams is a client library for building streaming applications and microservices, where the input and output data are stored in Kafka clusters.Kafka‘s cluster architecture makes Kafka Streams fault-tolerant, highly-scalable, and especially elastic solution. Kafka Streams utilizes exactly-once processing (Kafka topic -> Kafka topic) semantics, connects directly to Kafka, and does not require any separate processing cluster.Kafka‘s Streams library is built on top of the Kafka producer and consumer clients, but it is significantly more powerful and also more expressive than the plain clients. Also it is much simpler and quicker to write a real-world application start to finish with Kafka Streams than with the plain consumer.Further reading: Kafka Streams.

**Detailed explanation of each option:**

1. ❌ **A. Use ksqlDB.**  
   **Incorrect**.

2. ❌ **B. Use Kafka Connect Sink.**  
   **Incorrect**.

3. ✅ **C. Use Kafka Streams.**  
   **Correct**.

4. ❌ **D. Use a Consumer to consume from one topic and a Producer to produce to another topic.**  
   **Incorrect**.

</details>

## Question 29 (Kafka Producers):
Which properties must be set when producing messages to Kafka by creating a ProducerRecord?(Choose two)

- A. Partition
- B. Value
- C. Topic
- D. Key

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

In Kafka, producers create and write messages to topic partitions. We start producing messages to Kafka by creating a ProducerRecord, which must include the topic we want to send the record to and a value. Optionally, we can also specify a key and / or partition.Once we send the ProducerRecord, the first thing the producer will do is serialize the key and value objects to ByteArrays so they can be sent over the network.Further reading: Producer Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Partition**  
   **Incorrect**.

2. ✅ **B. Value**  
   **Correct**.

3. ✅ **C. Topic**  
   **Correct**.

4. ❌ **D. Key**  
   **Incorrect**.

</details>

## Question 30 (Kafka Setup and Operations):
A company created a production topic named prod_topic. The retention period for prod_topic should be 10 days. How could you accomplish this in the most efficient way?(Choose one)

- A. Set the topic configuration retention.days=10.
- B. Set the topic configuration retention.ms=864000000.
- C. Set the broker configuration retention.days=10.
- D. Set the broker configuration retention.ms=864000000.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The property retention.ms can be configured at topic level while creating topics or by altering topics. It shouldn‘t be set at the broker level (log.retention.ms) as this would impact all the topics in the cluster, not just the one we are interested in. The retention.ms configuration controls the maximum time in milliseconds we will retain a log before we will discard old log segments to free up space if we are using the “delete“ retention policy. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied. The default value is 604800000 (7 days).

**Detailed explanation of each option:**

1. ❌ **A. Set the topic configuration retention.days=10.**  
   **Incorrect**.

2. ✅ **B. Set the topic configuration retention.ms=864000000.**  
   **Correct**.

3. ❌ **C. Set the broker configuration retention.days=10.**  
   **Incorrect**.

4. ❌ **D. Set the broker configuration retention.ms=864000000.**  
   **Incorrect**.

</details>

## Question 31 (Kafka Consumers):
What happens if two consumers have the same group id and subscribe to the same topic?(Choose one)

- A. Each consumer will be assigned a subset of the partitions in the topic.
- B. Each consumer will be assigned one of the partitions in the topic.
- C. One consumer will be assigned all of the partitions in the topic and one consumer will be idle.
- D. Each consumer will be assigned all of the partitions in the topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The group.id is a unique string that identifies the consumer group a consumer belongs to. This property is required if the consumer uses either the group management functionality by using subscribe(topic) or the Kafka-based offset management strategy.The basic idea is that if two consumers have the same group id and subscribe to the same topic, each will be assigned a subset of the partitions in the topic and will therefore only read a subset of the messages individually (but all the messages will be read by the group as a whole). If you need a consumer to see, on its own, every single message in the topics it is subscribed to – it will need a unique group.id.Further reading: Consumer Groups.

**Detailed explanation of each option:**

1. ✅ **A. Each consumer will be assigned a subset of the partitions in the topic.**  
   **Correct**.

2. ❌ **B. Each consumer will be assigned one of the partitions in the topic.**  
   **Incorrect**.

3. ❌ **C. One consumer will be assigned all of the partitions in the topic and one consumer will be idle.**  
   **Incorrect**.

4. ❌ **D. Each consumer will be assigned all of the partitions in the topic.**  
   **Incorrect**.

</details>

## Question 32 (Stream Processing):
What‘s the most appropriate way of modeling a retail store‘s data in Kafka Streams? (Choose one)

- A. Sales of products as stream, orders placed for new products as stream, shipments of products that arrive as stream, customer as table.
- B. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.
- C. Sales of products as table, orders placed for new products as table, shipments of products that arrive as table, customer as stream.
- D. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. Sales of products as stream, orders placed for new products as stream, shipments of products that arrive as stream, customer as table Correct because in Kafka Streams, events that occur over time (sales, orders, shipments) are best modeled as streams. Customer data, however, is relatively static and represents the latest state of each customer, so it is best modeled as a table. This aligns with the stream-table duality principle in Kafka Streams: streams represent sequences of events, while tables represent current state. Incorrect Option B. Sales as stream, orders as table, shipments as stream, customer as table Incorrect because orders are also events that occur over time, not static state. Modeling them as a table would lose event granularity. Option C. Sales as table, orders as table, shipments as table, customer as stream Incorrect because sales, orders, and shipments are dynamic event-driven data, not static state. Customers should be modeled as a table, not a stream, since they represent current state. Option D. Sales as stream, orders as table, shipments as stream, customer as table Incorrect because, again, orders are events and should be modeled as a stream, not a table.

**Detailed explanation of each option:**

1. ✅ **A. Sales of products as stream, orders placed for new products as stream, shipments of products that arrive as stream, customer as table.**  
   **Correct**.

2. ❌ **B. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.**  
   **Incorrect**.

3. ❌ **C. Sales of products as table, orders placed for new products as table, shipments of products that arrive as table, customer as stream.**  
   **Incorrect**.

4. ❌ **D. Sales of products as stream, orders placed for new products as table, shipments of products that arrive as stream, customer as table.**  
   **Incorrect**.

</details>

## Question 33 (Programming & Serialization):
Which curl command can be used to fetch a schema by globally unique ID 1?(Choose one)

- A. curl -X GET http://localhost:9092/ids/1
- B. curl -X GET http://localhost:8081/ids/1
- C. curl -X GET http://localhost:9092/schemas/ids/1
- D. curl -X GET http://localhost:8081/schemas/ids/1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The best way to test the Schema Registry API is to use CURL (command line tool and library for transferring data with URLs) commands. First you need to start Schema Registry and its dependent services ZooKeeper and Kafka. To fetch a schema by globally unique ID 1 you can use the following command: curl -X GET http://localhost:8081/schemas/ids/1 Further reading: API Usage Examples.

**Detailed explanation of each option:**

1. ❌ **A. curl -X GET http://localhost:9092/ids/1**  
   **Incorrect**.

2. ❌ **B. curl -X GET http://localhost:8081/ids/1**  
   **Incorrect**.

3. ❌ **C. curl -X GET http://localhost:9092/schemas/ids/1**  
   **Incorrect**.

4. ✅ **D. curl -X GET http://localhost:8081/schemas/ids/1**  
   **Correct**.

</details>

## Question 34 (Kafka Producers):
Consider the following producer example: ProducerRecord<String, String> record = new ProducerRecord<>(“topic“, “key“, “value“); try { producer.send(record).get(); } catch (Exception e) { e.printStackTrace(); } What‘s the purpose of the .get() method? (Choose two)

- A. Using Future.get() tells Kafka to send the message asynchronously.
- B. Using Future.get() waits for a replay from Kafka before continuing.
- C. Using Future.get() will return a RecordMetadata object if there was an error.
- D. Using Future.get() will throw an exception if the record is not send successfully to Kafka.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Option B. Using Future.get() waits for a reply from Kafka before continuing. Correct because .get() blocks the current thread until the send operation completes. This ensures the producer waits for Kafka to acknowledge the message before moving forward. Option D. Using Future.get() will throw an exception if the record is not sent successfully to Kafka. Correct because .get() propagates exceptions such as ExecutionException or InterruptedException if the send fails. This allows the developer to handle delivery errors explicitly. Incorrect Option A. Using Future.get() tells Kafka to send the message asynchronously. Incorrect because the send() method itself is asynchronous. Calling .get() makes it synchronous by blocking until completion, so this statement is misleading. Option C. Using Future.get() will return a RecordMetadata object if there was an error. Incorrect because RecordMetadata is returned on successful sends, not on errors. If there is an error, .get() throws an exception instead of returning metadata.

**Detailed explanation of each option:**

1. ❌ **A. Using Future.get() tells Kafka to send the message asynchronously.**  
   **Incorrect**.

2. ✅ **B. Using Future.get() waits for a replay from Kafka before continuing.**  
   **Correct**.

3. ❌ **C. Using Future.get() will return a RecordMetadata object if there was an error.**  
   **Incorrect**.

4. ✅ **D. Using Future.get() will throw an exception if the record is not send successfully to Kafka.**  
   **Correct**.

</details>

## 🚫 Question 35 (Kafka Ecosystem):
In a scenario where you want to transform a timestamp field in a stream of events from a Kafka topic to a different time zone in KSQL, what KSQL function should you use?

- A. CHANGETIMEZONE
- B. ADJUSTTIMEZONE
- C. CONVERTTIMEZONE
- D. TIMETRANSFORM

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. CONVERTTIMEZONE KSQL provides the CONVERTTIMEZONE function to transform a timestamp from one time zone to another. This function is specifically designed for time zone conversion in streams and tables, making it the correct choice when adjusting event timestamps to a different time zone. Incorrect: Option A. CHANGETIMEZONE There is no CHANGETIMEZONE function available in KSQL. This option is not a valid KSQL function. Option B. ADJUSTTIMEZONE KSQL does not include an ADJUSTTIMEZONE function. Time zone transformations are not performed using this function name. Option D. TIMETRANSFORM TIMETRANSFORM is not a valid KSQL function for handling timestamps or time zone conversions.

**Detailed explanation of each option:**

1. ❌ **A. CHANGETIMEZONE**  
   **Incorrect**.

2. ❌ **B. ADJUSTTIMEZONE**  
   **Incorrect**.

3. ✅ **C. CONVERTTIMEZONE**  
   **Correct**.

4. ❌ **D. TIMETRANSFORM**  
   **Incorrect**.

</details>

## Question 36 (Programming & Serialization):
In a Kafka ecosystem, you are using Confluent Schema Registry to manage Avro schemas, and a new schema version is introduced with a non-breaking change. What should you consider when configuring schema compatibility settings to ensure smooth adoption by consumers?

- A. Enable backward compatibility
- B. Enable forward compatibility
- C. Disable compatibility checks
- D. Enforce strict schema rules

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

When configuring schema compatibility settings in Confluent Schema Registry for a new Avro schema version with a non-breaking change, you should consider: Enable backward compatibility. Explanation: Enabling backward compatibility ensures that the new schema version is compatible with existing consumers using the older version. Since it‘s a non-breaking change, backward compatibility allows consumers with the old schema to successfully process messages with the new schema. Backward compatibility means that new fields or optional changes can be added to the schema without breaking existing consumers. Consumers using the old schema can seamlessly consume messages produced with the new schema. By choosing backward compatibility, you promote a smooth adoption process, allowing consumers to adopt the new schema gradually without disruptions. This approach is particularly suitable for non-breaking changes where the goal is to maintain compatibility with existing consumers while introducing incremental improvements to the schema.

**Detailed explanation of each option:**

1. ✅ **A. Enable backward compatibility**  
   **Correct**.

2. ❌ **B. Enable forward compatibility**  
   **Incorrect**.

3. ❌ **C. Disable compatibility checks**  
   **Incorrect**.

4. ❌ **D. Enforce strict schema rules**  
   **Incorrect**.

</details>

## Question 37 (Kafka Setup and Operations):
What tool can be used together with Kafka to mirror a source Kafka cluster into a target Kafka cluster?(Choose one)

- A. Kafka Connect
- B. Schema Registry
- C. Streams API
- D. MirrorMaker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

With MirrorMaker, Kafka administrators can replicate topics, topic configurations, consumer groups, and ACLs from one or more source Kafka clusters to one or more target Kafka clusters, i. e., across cluster environments. Multi-datacenter deployments enable use-cases such as: – Active -> Active geo-localized deployments: allows users to access a near-by data center to optimize their architecture for low latency and high performance. Replication can be done in both sides and data can be produced and consumed in every cluster. – Active-> Passive disaster recover (DR) deployments: in an event of a partial or complete datacenter disaster, allow failing over applications to use Confluent Platform in a different datacenter. – Active -> Passive centralized analytics: Aggregate data from multiple Apache Kafka clusters into one location for organization-wide analytics. No producers will be used at the replicated cluster, it‘s just for consuming data for analytic purposes. – Aggregation (e. g., from many clusters to one): A->K, B->K, C->K. – Fan-out (e. g., from one to many clusters): K->A, K->B, K->C. – Forwarding: A->B, B->C, C->D. The tool uses a Kafka consumer to consume messages from the source cluster, and re-publishes those messages to the local (target) cluster using an embedded Kafka producer. Further reading: Cluster Replication Flows.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect**  
   **Incorrect**.

2. ❌ **B. Schema Registry**  
   **Incorrect**.

3. ❌ **C. Streams API**  
   **Incorrect**.

4. ✅ **D. MirrorMaker**  
   **Correct**.

</details>

## Question 38 (Programming & Serialization):
In a scenario where Avro schemas for Kafka messages are frequently evolving, how can Confluent Schema Registry assist in maintaining order and compatibility?

- A. Enforce strict schema rules
- B. Use schema validation
- C. Implement schema migration
- D. Define and manage compatibility settings

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In a scenario where Avro schemas for Kafka messages are frequently evolving, Confluent Schema Registry can assist in maintaining order and compatibility by: Defining and managing compatibility settings. Explanation: Confluent Schema Registry allows you to define compatibility settings that control how schemas can evolve over time. By configuring compatibility settings appropriately, you can ensure that changes to schemas are made in a way that maintains compatibility with existing producers and consumers. The compatibility settings include: Backward Compatibility: Ensures that new schema versions are backward compatible with the previous versions, allowing consumers using the old schema to successfully process messages with the new schema. Forward Compatibility: Ensures that new schema versions are forward compatible, allowing consumers using the new schema to successfully process messages with the old schema. Full Compatibility: Enforces both backward and forward compatibility, ensuring a high level of flexibility for schema evolution. None (No Compatibility): Allows any schema changes without enforcing compatibility. This setting should be used cautiously as it may lead to issues with message processing if not managed carefully. By defining and managing compatibility settings, you can control the evolution of Avro schemas, allowing for changes while ensuring that consumers and producers can operate smoothly despite frequent schema updates. This helps maintain order and compatibility in a dynamic schema evolution environment.

**Detailed explanation of each option:**

1. ❌ **A. Enforce strict schema rules**  
   **Incorrect**.

2. ❌ **B. Use schema validation**  
   **Incorrect**.

3. ❌ **C. Implement schema migration**  
   **Incorrect**.

4. ✅ **D. Define and manage compatibility settings**  
   **Correct**.

</details>

## Question 39 (Kafka Consumers):
Which of the following options is a consumer fetch metric?(Choose one)

- A. compression-rate-avg
- B. batch-size-max
- C. request-latency-avg
- D. bytes-consumed-rate

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The only consumer fetch metric is the bytes-consumed-rate. It‘s the average number of bytes consumed per second. All other metrics are producer metrics: – batch-size-max: The max number of bytes sent per partition per-request. – compression-rate-avg: The average compression rate of record batches, defined as the average ratio of the compressed batch size over the uncompressed size. – request-latency-avg: The average request latency in ms.

**Detailed explanation of each option:**

1. ❌ **A. compression-rate-avg**  
   **Incorrect**.

2. ❌ **B. batch-size-max**  
   **Incorrect**.

3. ❌ **C. request-latency-avg**  
   **Incorrect**.

4. ✅ **D. bytes-consumed-rate**  
   **Correct**.

</details>

## Question 40 (Kafka Connect):
When employing a JDBC source connector to transfer data from a table to a Kafka topic, and the connector is configured with max.tasks = 2 on a cluster with 3 workers, how many tasks will be initiated?

- A. 2
- B. 6
- C. 3
- D. 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Option D. 1 Correct because the JDBC source connector creates one task per table by default. Even though max.tasks is set to 2, if only one table is being ingested, only one task will be initiated. The number of workers (3 in this case) does not increase the number of tasks; workers only provide capacity to run tasks. Incorrect Option A. 2 Incorrect because while max.tasks=2 sets the upper limit, the connector will not start 2 tasks unless there are multiple tables or partitions to split across tasks. With a single table, only 1 task is created. Option B. 6 Incorrect because tasks are not multiplied by the number of workers. max.tasks defines the maximum tasks across the connector, not per worker. Option C. 3 Incorrect because the number of workers does not dictate the number of tasks. Tasks are assigned to workers, but the connector itself determines how many tasks to create.

**Detailed explanation of each option:**

1. ❌ **A. 2**  
   **Incorrect**.

2. ❌ **B. 6**  
   **Incorrect**.

3. ❌ **C. 3**  
   **Incorrect**.

4. ✅ **D. 1**  
   **Correct**.

</details>

## Question 41 (Kafka Internals):
Which Kafka broker is responsible for partition leader election?(Choose one)

- A. Partition leader
- B. Controller
- C. In-sync replica
- D. Zookeeper node

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In a Kafka cluster, one (and only one) of the brokers serves as the controller, which is responsible for managing the states of partitions and replicas and for performing administrative tasks like reassigning partitions. The election of that broker happens thanks to Zookeeper. Kafka Controller registers handlers to be notified about changes in Zookeeper and propagate them across brokers in a Kafka cluster. Further reading: Controller Internals.

**Detailed explanation of each option:**

1. ❌ **A. Partition leader**  
   **Incorrect**.

2. ✅ **B. Controller**  
   **Correct**.

3. ❌ **C. In-sync replica**  
   **Incorrect**.

4. ❌ **D. Zookeeper node**  
   **Incorrect**.

</details>

## Question 42 (Kafka Setup and Operations):
What holds true for Kafka brokers and clients starting from version 0.10.2 and later?

- A. Clients and brokers must have the exact same version to be able to communicate
- B. A newer client can‘t talk to a newer broker, but an older client can talk to a newer broker
- C. A newer client can talk to a newer broker, and an older client can talk to a newer broker
- D. A newer client can talk to a newer broker, but an older client cannot talk to a newer broker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

From Kafka version 0.10.2 onwards, the true statement about Kafka brokers and clients is:A newer client can talk to a newer broker, and an older client can talk to a newer brokerKafka maintains backward compatibility, which means that clients from older versions can communicate with newer brokers. This compatibility is an important feature of Kafka, as it allows for incremental upgrades of the system without requiring simultaneous updates of all clients and brokers.Also, newer clients are typically able to communicate with older brokers (within certain limits of version differences), but this is generally less of a concern than backward compatibility. However, it‘s important to note that using newer client features might not be possible if the broker is too old to support those features.The need for clients and brokers to have the exact same version to communicate is not a requirement in Kafka, as Kafka is designed to support communication between different versions within the same major release series.

**Detailed explanation of each option:**

1. ❌ **A. Clients and brokers must have the exact same version to be able to communicate**  
   **Incorrect**.

2. ❌ **B. A newer client can‘t talk to a newer broker, but an older client can talk to a newer broker**  
   **Incorrect**.

3. ✅ **C. A newer client can talk to a newer broker, and an older client can talk to a newer broker**  
   **Correct**.

4. ❌ **D. A newer client can talk to a newer broker, but an older client cannot talk to a newer broker**  
   **Incorrect**.

</details>

## Question 43 (Kafka Consumers):
Which offset commit strategy should you use for a consumer log application, if it‘s ok if messages will be lost?(Choose one)

- A. Auto-commit
- B. At-most once
- C. At-least once
- D. Exactly once

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

At-most once guarantee means the message will be processed exactly once, or not at all.For a consumer application at-most once processing means the consumer group receives a batch of messages from Kafka, transforms these and writes the results to a database. The consumer application has enable.auto.commit set to false and is programmed to commit their offsets back to Kafka prior to writing to the database. If the consumer fails after saving the offsets back to Kafka but before writing the data to the database, it will skip these records next time it runs and data will be lost.Usually perfectly fine for log applications, where it‘s ok if some log messages will be lost.Further reading: Offset Management.

**Detailed explanation of each option:**

1. ❌ **A. Auto-commit**  
   **Incorrect**.

2. ✅ **B. At-most once**  
   **Correct**.

3. ❌ **C. At-least once**  
   **Incorrect**.

4. ❌ **D. Exactly once**  
   **Incorrect**.

</details>

## Question 44 (Kafka Consumers):
Which of the following options is a producer sender metric?(Choose one)

- A. records-lag-max
- B. batch-size-avg
- C. bytes-consumed-rate
- D. commit-latency-avg

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The only producer sender metric is the batch-size-avg. It‘s the average number of bytes sent per partition per-request. All other metrics are consumer metrics: – commit-latency-avg: The average time taken for a commit request. – bytes-consumed-rate: The average number of bytes consumed per second. – records-lag-max: The maximum lag in terms of number of records for any partition in this window.

**Detailed explanation of each option:**

1. ❌ **A. records-lag-max**  
   **Incorrect**.

2. ✅ **B. batch-size-avg**  
   **Correct**.

3. ❌ **C. bytes-consumed-rate**  
   **Incorrect**.

4. ❌ **D. commit-latency-avg**  
   **Incorrect**.

</details>

## Question 45 (Kafka Consumers):
In a scenario where you have a consumer group consisting of 12 consumers, and a consumer is abruptly terminated by the process management system without a graceful shutdown, causing rebalances to take up to 10 seconds, but the business requirement is to reduce this rebalance time to 3 seconds, what two actions should be considered?

- A. Decrease heartbeat.interval.ms
- B. Increase heartbeat.interval.ms
- C. Decrease session.timeout.ms
- D. increase max.poll.interval.ms
- E. decrease max.poll.interval.ms
- F. Increase session.timeout.ms

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

To achieve a rebalance time of 3 seconds when a consumer in a group of 12 consumers is killed abruptly, you should:1. Decrease session.timeout.ms2. Decrease heartbeat.interval.msExplanation:1. Decrease session.timeout.ms: This setting controls the maximum time a consumer can be idle before the broker treats it as dead and triggers a rebalance. By reducing session.timeout.ms, you shorten the time the Kafka broker waits after a consumer stops sending heartbeats before it triggers a rebalance. Lowering this timeout can help achieve faster detection of consumer failures and thus quicker rebalances.2. Decrease heartbeat.interval.ms: This is the interval at which the consumer sends heartbeat messages to the Kafka broker to signal its liveness. Decreasing this value means the consumer will send heartbeats more frequently, allowing the broker to detect a failed consumer more quickly when the heartbeats stop.The other options would not help in achieving a quicker rebalance:Increase heartbeat.interval.ms: This would make heartbeats less frequent, potentially delaying the detection of a consumer failure.Increase max.poll.interval.ms: This setting determines the maximum amount of time a consumer can take between poll calls before being considered dead. Increasing it would not help in reducing the rebalance time.Decrease max.poll.interval.ms: While decreasing this value can lead to quicker detection of consumer failures due to long processing times, it is not directly related to the scenario described where the consumer is killed abruptly.Increase session.timeout.ms: Increasing this would actually delay the rebalance process, as the broker would wait longer before determining that a consumer is unresponsive and initiating a rebalance.

**Detailed explanation of each option:**

1. ✅ **A. Decrease heartbeat.interval.ms**  
   **Correct**.

2. ❌ **B. Increase heartbeat.interval.ms**  
   **Incorrect**.

3. ✅ **C. Decrease session.timeout.ms**  
   **Correct**.

4. ❌ **D. increase max.poll.interval.ms**  
   **Incorrect**.

5. ❌ **E. decrease max.poll.interval.ms**  
   **Incorrect**.

6. ❌ **F. Increase session.timeout.ms**  
   **Incorrect**.

</details>

## Question 46 (Kafka Setup and Operations):
What functionality of Kafka becomes unavailable when an SSL endpoint is activated?

- A. Exactly-once delivery
- B. Cross-cluster mirroring
- C. Support for Avro format
- D. Zero copy

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

If you enable an SSL endpoint in Kafka, the feature that will be affected is:Zero copyExactly-once delivery: This feature won‘t be affected by enabling SSL. Kafka‘s exactly-once semantics are designed to work with various configurations, including secure SSL connections.Cross-cluster mirroring: Enabling SSL does not impact the ability to perform cross-cluster mirroring (like with MirrorMaker). These operations can still be conducted securely over SSL.Support for Avro format: SSL encryption of data in transit does not affect the data format. Kafka can still support Avro and other serialization/deserialization formats regardless of whether SSL is enabled.Zero copy: Enabling SSL affects the “zero copy“ optimization. Zero copy is a performance optimization technique used by Kafka to transfer data directly between the kernel and the network socket, avoiding extra copy operations to user space. When SSL is enabled, data must be encrypted before it is sent over the network, which requires moving data to user space for encryption, thereby negating the zero copy optimization. This can lead to increased CPU usage and lower throughput compared to non-SSL traffic.

**Detailed explanation of each option:**

1. ❌ **A. Exactly-once delivery**  
   **Incorrect**.

2. ❌ **B. Cross-cluster mirroring**  
   **Incorrect**.

3. ❌ **C. Support for Avro format**  
   **Incorrect**.

4. ✅ **D. Zero copy**  
   **Correct**.

</details>

## 🚫 Question 47 (Kafka Setup and Operations):
In a production environment running in PLAINTEXT mode on a machine with 256 GB of RAM, what is the appropriate heap size for a broker?

- A. 512 MB
- B. 16 GB
- C. 4 GB
- D. 128 GB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

For a Kafka broker in a production setup on a machine with 256 GB of RAM, especially when operating in PLAINTEXT mode, an appropriate heap size would be 4 GB.Given Kafka‘s reliance on the OS page cache for performance, it is advantageous to allocate more memory to the page cache and keep the heap size relatively small.4 GB is a sensible starting point for the heap size in a Kafka setup like this. It should be sufficient for most Kafka operational needs, especially in PLAINTEXT mode, where SSL encryption is not a factor.Allocating a heap size of 4 GB leaves a substantial amount of the system‘s RAM available for the OS page cache, which Kafka will effectively utilize for its disk I/O operations.The heap size can be adjusted if specific performance issues are observed or if additional features like SSL encryption are enabled, which may require slightly more heap space. However, for PLAINTEXT mode, 4 GB should be a good balance.

**Detailed explanation of each option:**

1. ❌ **A. 512 MB**  
   **Incorrect**.

2. ❌ **B. 16 GB**  
   **Incorrect**.

3. ✅ **C. 4 GB**  
   **Correct**.

4. ❌ **D. 128 GB**  
   **Incorrect**.

</details>

## Question 48 (Kafka Setup and Operations):
Which command line script can be used to manage Kafka ACLs?(Choose one)

- A. bin/acls.sh
- B. bin/kafka-security.sh
- C. bin/kafka-acls.sh
- D. bin/kafka-authorization.sh

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Authorization allows you to define the actions they are permitted to take once connected to the Kafka cluster. Apache Kafka ships with an out-of-box authorization mechanism to establish ACL configurations to protect specific Kafka resources. Kafka ACLs are stored within ZooKeeper and are managed with the kafka-acls.sh command line script. Further reading: Authorization Concepts.

**Detailed explanation of each option:**

1. ❌ **A. bin/acls.sh**  
   **Incorrect**.

2. ❌ **B. bin/kafka-security.sh**  
   **Incorrect**.

3. ✅ **C. bin/kafka-acls.sh**  
   **Correct**.

4. ❌ **D. bin/kafka-authorization.sh**  
   **Incorrect**.

</details>

## Question 49 (Kafka Connect):
In a Kafka Connect setup, what is the purpose of the Dead Letter Queue (DLQ)?

- A. Storing failed Avro schemas.
- B. Storing records with delivery errors.
- C. Managing task parallelism.
- D. Storing offsets for connector tasks.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In a Kafka Connect setup, the purpose of the Dead Letter Queue (DLQ) is: Storing records with delivery errors. Explanation: The Dead Letter Queue (DLQ) in Kafka Connect is a mechanism to store records that encounter errors during processing or delivery. When a record fails to be processed by a connector or encounters an issue during delivery to the target system, it is typically moved to the Dead Letter Queue. The Dead Letter Queue allows for the isolation and handling of records that cannot be successfully processed, helping operators and developers to identify and address problematic records without affecting the overall data flow. This mechanism is crucial for managing data quality and addressing issues with specific records without disrupting the entire data pipeline. The other options: Storing failed Avro schemas: This is not the primary purpose of the Dead Letter Queue. Schemas are typically managed separately, and failed Avro schemas may not be directly related to DLQ. Managing task parallelism: Task parallelism is typically managed by adjusting the tasks.max configuration, and it‘s not the primary purpose of the Dead Letter Queue. Storing offsets for connector tasks: Offsets are usually managed by Kafka Connect for tracking the progress of connectors, and they are not directly related to the Dead Letter Queue.

**Detailed explanation of each option:**

1. ❌ **A. Storing failed Avro schemas.**  
   **Incorrect**.

2. ✅ **B. Storing records with delivery errors.**  
   **Correct**.

3. ❌ **C. Managing task parallelism.**  
   **Incorrect**.

4. ❌ **D. Storing offsets for connector tasks.**  
   **Incorrect**.

</details>

## Question 50 (Stream Processing):
A Kafka Streams application is processing a topic, and you need to forward specific records to a different topic based on a condition. What Kafka Streams operation should you use for this task?

- A. forward
- B. map
- C. branch
- D. filter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

To forward specific records to a different topic based on a condition in a Kafka Streams application, you should use the branch operation. Explanation: The branch operation in Kafka Streams is used to create multiple branches (or substreams) from a source stream based on specified predicates (conditions). Each branch represents a subset of records that match a particular condition. Example usage: “KStream[] branches = stream.branch( /* your conditions/predicates */ ); “ In this example, you define multiple branches based on conditions, and each branch will contain records that satisfy the corresponding condition. After branching, you can further process each branch separately and perform specific operations based on the conditions. For forwarding records to different topics based on conditions, you can use the branches and apply to operation or further transformations to achieve the desired output.

**Detailed explanation of each option:**

1. ❌ **A. forward**  
   **Incorrect**.

2. ❌ **B. map**  
   **Incorrect**.

3. ✅ **C. branch**  
   **Correct**.

4. ❌ **D. filter**  
   **Incorrect**.

</details>

## 🚫 Question 51 (Kafka Ecosystem):
Which ksqlDB queries read or write data to Kafka?(Choose three)

- A. CREATE STREAM AS SELECT
- B. CREATE TABLE AS SELECT
- C. COUNT
- D. EXPLAIN

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

ksqlDB allows you to query, read, write, and process data in Kafka in real-time and at scale using intuitive SQL-like syntax. – SHOW STREAMS and EXPLAIN query statements run against the ksqlDB server that the ksqlDB client is connected to. They don‘t communicate directly with Kafka. – Persistent queries based on CREATE STREAM AS SELECT and CREATE TABLE AS SELECT read and write to Kafka topics. – Non-persistent queries based on SELECT that are stateless only read from Kafka topics. – Non-persistent queries that are stateful read and write to Kafka, for example, COUNT and JOIN. Further reading: Confluent ksqlDB.

**Detailed explanation of each option:**

1. ✅ **A. CREATE STREAM AS SELECT**  
   **Correct**.

2. ✅ **B. CREATE TABLE AS SELECT**  
   **Correct**.

3. ✅ **C. COUNT**  
   **Correct**.

4. ❌ **D. EXPLAIN**  
   **Incorrect**.

</details>

## 🚫 Question 52 (Kafka Ecosystem):
Which of the following options can be used to interact with the ksqlDB servers through a REST API in the interactive deployment mode?(Choose three)

- A. Favorite REST client
- B. Confluent Control Center
- C. ksqlDB CLI
- D. Kafka Streams API

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

ksqlDB provides two deployment options: – Headless ksqlDB deployment: The simplest deployment mode for ksqlDB is the headless mode, also called application mode. In the headless mode, you write all of your queries in a SQL file, and then start ksqlDB server instances with this file as an argument. Each server instance will read the given SQL file, compile the ksqlDB statements into Kafka Streams applications and start execution of the generated applications. Headless ksqlDB is recommended for production deployments. – Interactive ksqlDB deployment: The other option for running ksqlDB is interactive mode, in which you interact with the ksqlDB servers through a REST API either directly via your favorite REST clients, through ksqlDB CLI or through Confluent Control Center. Further reading: ksqlDB Deployment.

**Detailed explanation of each option:**

1. ✅ **A. Favorite REST client**  
   **Correct**.

2. ✅ **B. Confluent Control Center**  
   **Correct**.

3. ✅ **C. ksqlDB CLI**  
   **Correct**.

4. ❌ **D. Kafka Streams API**  
   **Incorrect**.

</details>

## Question 53 (Kafka Consumers):
A company uses a production consumer application with a large number of consumers. Even for lower activity hours of the day the consumers are using a lot of CPU when fetching messages. Increasing which consumer property is a good choice to possibly reduce the load on both the consumer and the broker?(Choose one)

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

## Question 54 (Kafka Consumers):
In a consumer group application, what internal consumer mechanism can be used to detect a data processing issue?(Choose one)

- A. Offset thread
- B. Heartbeat thread
- C. Poll thread
- D. Push thread

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Consumers in a group talk to a consumer group coordinator. To detect consumers that have processing issues or are down, there is a poll and a heartbeat mechanism: – Heartbeat thread: Heartbeats are sent periodically to the broker. If no heartbeat is sent during that period, the consumer is considered dead. – Poll thread: This is particularly relevant for Big Data frameworks like Spark in case the processing takes a lot of time. This mechanism detects data processing issues.

**Detailed explanation of each option:**

1. ❌ **A. Offset thread**  
   **Incorrect**.

2. ❌ **B. Heartbeat thread**  
   **Incorrect**.

3. ✅ **C. Poll thread**  
   **Correct**.

4. ❌ **D. Push thread**  
   **Incorrect**.

</details>

## Question 55 (Kafka Core Concepts):
Which of the following options are true about topics in Kafka?(Choose two)

- A. You can have as many topics as you want.
- B. A topic is identified by its unique id.
- C. Topics are always multi-producer and multi-subscriber.
- D. The number of topics is limited to 500.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

In Kafka, events are organized and durably stored in topics. – Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. – Topics have no quota and you can create as many topics as you want. – A topic is identified by its name (not ID) and topics are split into partitions.

**Detailed explanation of each option:**

1. ✅ **A. You can have as many topics as you want.**  
   **Correct**.

2. ❌ **B. A topic is identified by its unique id.**  
   **Incorrect**.

3. ✅ **C. Topics are always multi-producer and multi-subscriber.**  
   **Correct**.

4. ❌ **D. The number of topics is limited to 500.**  
   **Incorrect**.

</details>

## Question 56 (Kafka Consumers):
If a consumer successfully processes record #11 but fails to process record #10, what action should be taken to ensure at least once processing of each record?

- A. Do not commit until successfully processing the record #10
- B. Commit offsets at 10
- C. Commit offsets at 11

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To guarantee at least once processing in this scenario, you should choose the following course of action:Do not commit until successfully processing the record #10Explanation:In at least once processing semantics, each message is guaranteed to be processed at least once, which might result in duplicates but ensures no data loss. Therefore, the offset of a message should only be committed after it has been successfully processed.If the consumer fails to process record #10 but succeeds with record #11, it should not commit the offset for record #11. If it does, record #10, which failed to process, will be skipped when the consumer restarts, as the consumer will resume processing from the next record after the last committed offset.By not committing the offset until record #10 is successfully processed, you ensure that upon a restart or recovery, the consumer will retry processing from record #10, thereby adhering to the at least once processing guarantee.

**Detailed explanation of each option:**

1. ✅ **A. Do not commit until successfully processing the record #10**  
   **Correct**.

2. ❌ **B. Commit offsets at 10**  
   **Incorrect**.

3. ❌ **C. Commit offsets at 11**  
   **Incorrect**.

</details>
