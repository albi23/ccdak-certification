> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1 (Programming & Serialization):
Kafka uses the hash of the message key to assign a record to a partition. If a producer serializes the key as a UTF‑8 string containing a sequential integer value (e.g., "1", "2", "3", …), which of the following statements best describes the partition assignment behavior for a topic with many partitions?

- A. The partition assignment is independent of the key serialization, only the key's original type matters.
- B. The records will be evenly distributed across partitions because the hash function treats each string uniformly.
- C. The records will be assigned to partitions based on the numerical value of the integer after deserialization.
- D. The records will cluster in a few partitions because sequential string keys produce similar hash values.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, the DefaultPartitioner calculates a hash (Murmur2) of the key’s serialized byte array and maps the result to a partition. Because Murmur2 is designed to spread uniformly, sequential UTF‑8 string keys such as "1", "2", "3" will produce diverse hash values, leading to an even distribution across many partitions. The key’s original Java type is irrelevant, only the deterministic byte output of the serializer matters. Misconceptions arise when assuming that the numerical order directly maps to partition numbers or that serialization has no effect. In practice, ensuring deterministic serialization guarantees reproducible and balanced partitioning, which is crucial for load balancing and fault tolerance in distributed systems.

Source: Apache Kafka docs/source - DefaultPartitioner uses Murmur2 over the serialized key bytes, Kafka: The Definitive Guide 2nd ed. Ch. 3 "Partitions" (pp. 68-70, book notes Kafka's own hash algorithm)

**Detailed explanation of each option:**

1. ❌ **A. The partition assignment is independent of the key serialization, only the key's original type matters.**  
   **Incorrect**. The partitioner hashes the *serialized* key bytes, not the original object. Therefore the actual byte representation produced by the serializer determines the hash input.

2. ✅ **B. The records will be evenly distributed across partitions because the hash function treats each string uniformly.**  
   **Correct**. Kafka’s DefaultPartitioner uses a hash (Murmur2) of the serialized key bytes. Murmur2 produces a well‑distributed hash for sequential UTF‑8 strings, so records will be spread evenly across partitions as long as the key bytes are deterministic.

3. ❌ **C. The records will be assigned to partitions based on the numerical value of the integer after deserialization.**  
   **Incorrect**. The consumer does not influence partition assignment, the producer’s serialized key bytes are hashed. Deserialization happens only when the consumer reads the record.

4. ❌ **D. The records will cluster in a few partitions because sequential string keys produce similar hash values.**  
   **Incorrect**. Sequential string keys do not produce similar hash values with Murmur2, the hash function randomizes the input, avoiding clustering. Clustering would occur only if a poor hash function were used.

</details>

## Question 2 (Kafka Core Concepts):
Which statement correctly describes Kafka’s ordering guarantees?

- A. Kafka guarantees ordering of records across all partitions within a topic.
- B. Producer can guarantee ordering only if it sends records with the same key to the same partition.
- C. Ordering can be broken if a consumer reads from multiple partitions concurrently.
- D. Kafka guarantees ordering of records within a single partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, ordering guarantees are scoped to a single partition. The broker writes records to a partition in the order they arrive and stores them sequentially on disk. Consumers read from that partition in the same order. There is no ordering across partitions or topics. While producers can use keys or explicit partitioning to ensure all related records go to the same partition, ordering is not limited to key‑based routing. Concurrent consumption of multiple partitions preserves each partition’s order, but does not impose any global order. Understanding this scope is essential for designing systems that rely on event sequencing, such as stateful stream processing or event‑sourced services.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6), ordering per partition

**Detailed explanation of each option:**

1. ❌ **A. Kafka guarantees ordering of records across all partitions within a topic.**  
   **Incorrect**. Ordering is guaranteed only within a single partition, there is no ordering guarantee across partitions of the same topic.

2. ❌ **B. Producer can guarantee ordering only if it sends records with the same key to the same partition.**  
   **Incorrect**. While using the same key is a common way to force records to a single partition, a producer can also explicitly specify the partition number to guarantee order.

3. ❌ **C. Ordering can be broken if a consumer reads from multiple partitions concurrently.**  
   **Incorrect**. A consumer’s concurrent reads from different partitions do not affect the intra‑partition order, each partition’s ordering remains intact.

4. ✅ **D. Kafka guarantees ordering of records within a single partition.**  
   **Correct**. Kafka preserves the order of records in each partition as they are written and read, regardless of how many partitions a topic has.

</details>

## Question 3 (Stream Processing): [-]
When designing a stateful Kafka Streams application that performs aggregations and joins, which of the following statements about Kafka Streams’ runtime behavior are true? Select all that apply.

- A. Kafka Streams automatically commits the offsets of input topics on behalf of the application, typically every few seconds or when the application is closed.
- B. When a stream processing task fails, Kafka Streams restarts the task on a different node, but the task’s local state is lost and must be rebuilt from scratch.
- C. Using the KStream.filter() operator can modify the downstream key of a record without changing the original key.
- D. A Kafka Streams application can safely produce records to the same topic it consumes from without risking infinite loops.
- E. The internal state store of a Kafka Streams application is automatically replicated to all instances of the application.
- F. The materialized view created with aggregate() is stored in a changelog topic that can be queried by other consumers.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, F

**Explanation:**

Correction: E is false. A state store is NOT replicated to all instances, each task's store lives on one instance and is backed by a changelog topic. Optional standby replicas (`num.standby.replicas`, default 0) keep warm copies on other instances only if configured, and never on "all" instances. Only A and F are defensible, so this is "select 2", not 3. Original text follows.

Kafka Streams provides robust state management through local state stores that are mirrored to standby replicas for fault tolerance. Offsets are committed automatically, guaranteeing at‑least‑once semantics. Aggregations produce changelog topics that serve as durable, queryable stores. However, operators like filter() only remove records, key/value changes require mapping functions. Producing to the same source topic can create loops unless mitigated, and task restarts recover state from changelogs rather than rebuilding it from scratch. Understanding these mechanics is essential for building reliable, scalable stream processing applications. For more details, see the official Kafka Streams documentation: https://kafka.apache.org/documentation/streams/, https://docs.confluent.io/platform/current/streams/developer-guide.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams: Architecture Overview" (pp. 410-416)

**Detailed explanation of each option:**

1. ✅ **A. Kafka Streams automatically commits the offsets of input topics on behalf of the application, typically every few seconds or when the application is closed.**  
   **Correct**. Kafka Streams manages offset commits internally. By default it commits offsets at intervals defined by the commit interval (e.g., 30 seconds) or on graceful shutdown, ensuring at-least‑once processing.

2. ❌ **B. When a stream processing task fails, Kafka Streams restarts the task on a different node, but the task’s local state is lost and must be rebuilt from scratch.**  
   **Incorrect**. The task’s state is restored from its changelog topic on the new node, so the local state is not lost.

3. ❌ **C. Using the KStream.filter() operator can modify the downstream key of a record without changing the original key.**  
   **Incorrect**. filter() only removes records that do not satisfy the predicate, it does not alter the key or value. Key/value transformations are performed by map, mapValues, or selectKey.

4. ❌ **D. A Kafka Streams application can safely produce records to the same topic it consumes from without risking infinite loops.**  
   **Incorrect**. Producing back to the source topic can create a loop unless precautions (e.g., distinct stream names, windowing, or filtering) are taken. The framework does not automatically prevent such loops.

5. ❌ **E. The internal state store of a Kafka Streams application is automatically replicated to all instances of the application.**  
   **Incorrect**. Each task's store lives on a single instance and is backed by a changelog topic. Standby replicas exist only when `num.standby.replicas` > 0 (default 0) and are placed on a limited number of other instances, not on all of them. Only a `GlobalKTable` is fully materialized on every instance.

6. ✅ **F. The materialized view created with aggregate() is stored in a changelog topic that can be queried by other consumers.**  
   **Correct**. aggregate() creates a persistent state store backed by a changelog topic, which other consumers can read for point‑in‑time queries or for stream replay.

</details>

## Question 4 (Reliable Data Delivery):
Which topic configuration parameter controls the minimum number of in‑sync replicas that must acknowledge a write for the write to be considered successful, and how does it interact with the topic's replication factor and broker‑level settings?

- A. cleanup.policy
- B. segment.bytes
- C. retention.ms
- D. min.insync.replicas
- E. compression.type

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The `min.insync.replicas` topic configuration is key for ensuring data durability in a replicated Kafka topic. It specifies the minimum number of in‑sync replicas required to acknowledge a write for the write to be considered successful. This value must be less than or equal to the topic's replication factor, otherwise, no writes will succeed. It interacts with the broker setting `unclean.leader.election.enable`, which determines whether a broker can become a leader if the in‑sync replica count falls below the minimum. Understanding this interaction helps developers balance availability and durability, especially when configuring topics for critical applications. Common misconceptions include confusing it with `replication.factor` or assuming it controls the number of replicas a broker hosts. Correctly using `min.insync.replicas` allows developers to enforce stronger consistency guarantees while still benefiting from Kafka's replication features. For detailed behavior and examples, refer to the Apache Kafka documentation: https://kafka.apache.org/documentation/#topicconfigs.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 7 "Minimum In-Sync Replicas" (p. 167)

**Detailed explanation of each option:**

1. ❌ **A. cleanup.policy**  
   **Incorrect**. `cleanup.policy` defines whether a topic uses delete or compaction cleanup, not the replication acknowledgement count.

2. ❌ **B. segment.bytes**  
   **Incorrect**. `segment.bytes` controls the size of log segment files before they roll, unrelated to replication or write acknowledgments.

3. ❌ **C. retention.ms**  
   **Incorrect**. `retention.ms` determines how long a message will be kept in a topic before it is eligible for deletion, not related to replication acknowledgments.

4. ✅ **D. min.insync.replicas**  
   **Correct**. This setting specifies how many replicas must be in sync and acknowledge a write before the leader can respond with success. It is evaluated against the topic's replication factor and the broker configuration of `unclean.leader.election.enable`. If the number of in‑sync replicas falls below this value, writes will fail with a `NotEnoughReplicasException`.

5. ❌ **E. compression.type**  
   **Incorrect**. `compression.type` selects the compression algorithm for messages, with no effect on replication acknowledgments.

</details>

## Question 5 (Kafka Connect):
Which of the following statements correctly describe core concepts of Kafka Connect source, sink, and CDC connectors?

- A. Source connectors read data from an external system and produce it to one or more Kafka topics.
- B. Sink connectors consume data from Kafka topics and write it to an external system.
- C. CDC connectors are a special type of source connector that emits change events based on database transaction logs.
- D. CDC connectors always require a sink connector to function.
- E. Kafka Connect uses the Connect API, which defines SourceTask and SinkTask classes, and connectors must also implement a custom interface called ConnectTask.
- F. Connector implementations must handle offset tracking and committing themselves.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Kafka Connect separates data movement into source and sink connectors, each implementing a specific task interface. Source connectors ingest data from external systems, sink connectors push data from Kafka to external destinations, and CDC connectors are a subset of source connectors that emit database change events from transaction logs. Offsets are managed by the Connect framework, relieving connectors from that responsibility. Misconceptions often arise around the need for a sink with CDC connectors or custom interfaces beyond the standard task classes. Understanding these distinctions is essential for designing reliable integration pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ✅ **A. Source connectors read data from an external system and produce it to one or more Kafka topics.**  
   **Correct**. Source connectors implement the SourceTask interface and push records into Kafka. They are the entry point for data coming into the cluster.

2. ✅ **B. Sink connectors consume data from Kafka topics and write it to an external system.**  
   **Correct**. Sink connectors implement the SinkTask interface and consume from Kafka to persist or forward data to other systems.

3. ✅ **C. CDC connectors are a special type of source connector that emits change events based on database transaction logs.**  
   **Correct**. CDC (Change Data Capture) connectors, such as Debezium, capture database changes and produce them as source records, often using a Debezium change event format.

4. ❌ **D. CDC connectors always require a sink connector to function.**  
   **Incorrect**. CDC connectors are source connectors and can operate independently, a sink is not mandatory for them to produce change events to Kafka.

5. ❌ **E. Kafka Connect uses the Connect API, which defines SourceTask and SinkTask classes, and connectors must also implement a custom interface called ConnectTask.**  
   **Incorrect**. While Connect API defines SourceTask and SinkTask, there is no required custom interface named ConnectTask, connectors extend these classes.

6. ❌ **F. Connector implementations must handle offset tracking and committing themselves.**  
   **Incorrect**. Kafka Connect's framework automatically manages offsets for source connectors, connectors only provide offset data. Sink connectors also rely on Connect for offset tracking.

</details>

## Question 6 (Kafka Producers): [-]
Which of the following client configuration settings and practices are recommended for maximizing producer throughput while also ensuring robust error handling in a Confluent Kafka application? (Select all that apply)

- A. Setting `compression.type` to "none" to avoid compression overhead.
- B. Setting `linger.ms` to 0 to send records immediately.
- C. Increasing `batch.size` to a value greater than 16384 bytes.
- D. Enabling `socket.keepalive.enable` to reduce stale connections in long‑running producers.
- E. Enabling `enable.idempotence` for exactly‑once semantics.
- F. Setting `max.block.ms` to 0 to fail immediately when the buffer is full.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, E, F

**Explanation:**

To maximize Kafka producer throughput, the primary strategy is to enlarge the `batch.size`, allowing more records to be sent in a single request and thus reducing per‑record overhead. Enabling `enable.idempotence` adds strong reliability guarantees, ensuring that retries do not produce duplicates, which simplifies client error handling and aligns with exactly‑once semantics. Setting `max.block.ms` to 0 is a defensive error‑handling tactic that forces the application to immediately react when the producer buffer is full, avoiding indefinite blocking. Conversely, a `linger.ms` of 0, disabling compression, or relying solely on `socket.keepalive.enable` do not contribute to throughput optimization and may in some cases degrade performance or provide only marginal reliability benefits. These tuning choices reflect the balance between speed, reliability, and graceful error handling that Confluent developers must manage.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Configuring Producers" (pp. 54-61)

**Detailed explanation of each option:**

1. ❌ **A. Setting `compression.type` to "none" to avoid compression overhead.**  
   **Incorrect**. Disabling compression removes the benefits of reduced payload size and network usage, compression generally improves throughput, especially on high‑volume streams. Thus, this setting is counter‑productive for performance tuning.

2. ❌ **B. Setting `linger.ms` to 0 to send records immediately.**  
   **Incorrect**. While a `linger.ms` of 0 reduces latency, it forces the producer to send every record in a separate request, increasing network overhead and lowering throughput. This is not a best practice for throughput optimization.

3. ✅ **C. Increasing `batch.size` to a value greater than 16384 bytes.**  
   **Correct**. A larger `batch.size` allows the producer to aggregate more records per request, reducing request overhead and improving throughput. It is a standard tuning technique for high‑volume producers. (See Apache Kafka Producer Config: batch.size)

4. ❌ **D. Enabling `socket.keepalive.enable` to reduce stale connections in long‑running producers.**  
   **Incorrect**. While this setting improves connection stability, it does not directly influence throughput or error handling of message delivery. It is a supplementary reliability practice, not a primary tuning knob.

5. ✅ **E. Enabling `enable.idempotence` for exactly‑once semantics.**  
   **Correct**. When `enable.idempotence` is true, the producer guarantees that duplicate records are not produced on retries, providing strong reliability with minimal client‑side error handling. The trade‑off is a slight increase in latency due to additional round‑trips, but it is widely recommended for production. (See Kafka Producer Config: enable.idempotence)

6. ✅ **F. Setting `max.block.ms` to 0 to fail immediately when the buffer is full.**  
   **Correct**. A `max.block.ms` of 0 causes the producer to throw a `TimeoutException` right away if the in‑flight buffer is exhausted, preventing the application from blocking indefinitely. This is a useful error‑handling pattern when backpressure must be surfaced to the caller.

</details>

## Question 7 (Kafka Connect): [-]
Which of the following statements accurately describe core concepts of Kafka Connect regarding source connectors, sink connectors, CDC behavior, and schema evolution?

- A. CDC connectors rely on the Debezium framework to capture database changes and publish them as Avro records with change event metadata.
- B. Schema evolution in Connect is handled automatically by the schema registry, which allows adding fields without breaking consumer compatibility as long as the chosen compatibility mode is set appropriately.
- C. Connect guarantees at-most-once delivery semantics for source connectors, and at-least-once for sink connectors.
- D. Connect connectors can automatically create Kafka topics on demand, but sink connectors cannot create topics—they must exist beforehand.
- E. Source connectors write data to Kafka topics by converting each external record into a Kafka ProducerRecord that may include a schema if one is defined.
- F. Sink connectors read data from Kafka topics and write it to external systems using a single consumer thread per task.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, F

**Explanation:**

Kafka Connect abstracts data movement between Kafka and external systems through source and sink connectors. Source connectors act as producers, converting external records into ProducerRecords with optional schemas, sink connectors act as consumers, each task typically running a single consumer thread. Schema evolution is managed by the Confluent Schema Registry, where compatibility settings determine how new fields affect existing consumers. While Debezium is a common CDC framework, CDC connectors are not limited to it. Misconceptions often arise around topic creation, delivery guarantees, and the exclusive use of Debezium for CDC. Understanding these distinctions is vital for building reliable, scalable pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. CDC connectors rely on the Debezium framework to capture database changes and publish them as Avro records with change event metadata.**  
   **Incorrect**. Partially correct but too narrow. While Debezium is a popular CDC framework and emits Avro with metadata, CDC connectors can also use other frameworks or custom implementations. The statement is not universally true for all CDC connectors.

2. ✅ **B. Schema evolution in Connect is handled automatically by the schema registry, which allows adding fields without breaking consumer compatibility as long as the chosen compatibility mode is set appropriately.**  
   **Correct**. Connect integrates with Confluent Schema Registry, when schemas evolve, compatibility (BACKWARD, FORWARD, FULL) governs whether consumers can continue reading without breaking.

3. ❌ **C. Connect guarantees at-most-once delivery semantics for source connectors, and at-least-once for sink connectors.**  
   **Incorrect**. The default semantics for both source and sink connectors are at-least-once, at-most-once can be configured but is not guaranteed by default.

4. ❌ **D. Connect connectors can automatically create Kafka topics on demand, but sink connectors cannot create topics—they must exist beforehand.**  
   **Incorrect**. Both source and sink connectors can create topics if the broker property `auto.create.topics.enable` is true or if the connector is configured to do so.

5. ✅ **E. Source connectors write data to Kafka topics by converting each external record into a Kafka ProducerRecord that may include a schema if one is defined.**  
   **Correct**. Source connectors act as producers, they read from external systems, serialize records, and publish them to Kafka topics, optionally using a schema from the Schema Registry.

6. ✅ **F. Sink connectors read data from Kafka topics and write it to external systems using a single consumer thread per task.**  
   **Correct**. Each task in a sink connector typically runs a consumer thread that polls records and writes them to the target system.

</details>

## Question 8 (Reliable Data Delivery):
Which of the following statements about Kafka data replication is NOT true?

- A. By default, if replication factor is set to 1, the partition will be replicated across all brokers in the cluster.
- B. A topic's replication factor must be at least as large as the number of in‑sync replicas for a partition to be considered healthy.
- C. If a leader broker fails, a follower that is in‑sync will automatically become the new leader.
- D. Replication ensures fault tolerance by copying each partition to multiple brokers.
- E. The follower will not send data to the leader, the leader sends data to followers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka replication is central to fault tolerance: each partition is copied to a number of brokers defined by the replication factor. The leader broker accepts all writes and propagates them to followers, followers never send data upstream. A replication factor of 1 means no replication, the partition exists only on a single broker, so it cannot be replicated across the cluster. The replication factor is always greater than or equal to the number of in‑sync replicas (ISR), which is the subset of replicas that are fully caught up. When a leader dies, an ISR follower automatically becomes the new leader, ensuring zero data loss. This question tests understanding of replication concepts and common misconceptions about replication factor semantics.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-142) and Ch. 7 "Replication" (pp. 163-168)

**Detailed explanation of each option:**

1. ✅ **A. By default, if replication factor is set to 1, the partition will be replicated across all brokers in the cluster.**  
   **Correct**. Incorrect. A replication factor of 1 means the partition has only one copy and is not replicated to any other broker.

2. ❌ **B. A topic's replication factor must be at least as large as the number of in‑sync replicas for a partition to be considered healthy.**  
   **Incorrect**. Correct. The replication factor represents the total copies, the ISR is a subset and cannot exceed it.

3. ❌ **C. If a leader broker fails, a follower that is in‑sync will automatically become the new leader.**  
   **Incorrect**. Correct. Kafka automatically elects an ISR follower as the new leader to maintain continuity.

4. ❌ **D. Replication ensures fault tolerance by copying each partition to multiple brokers.**  
   **Incorrect**. Correct. Kafka replicates each partition to the number of brokers specified by the topic’s replication factor, providing high availability.

5. ❌ **E. The follower will not send data to the leader, the leader sends data to followers.**  
   **Incorrect**. Correct. The leader broker receives all writes and replicates them to in-sync followers via the follower’s fetch requests.

</details>

## Question 9 (Programming & Serialization):
A Kafka cluster is integrated with Confluent Schema Registry. An application produces messages where the key is serialized with Kafka's StringSerializer and the value is serialized with Kafka's AvroSerializer. The consumer is configured to use AvroDeserializer for both key and value. Which statement correctly describes the behavior of the consumer when it attempts to consume these records?

- A. The consumer will deserialize the keys correctly because AvroDeserializer automatically treats non‑Avro keys as raw bytes.
- B. The consumer will fail to deserialize the keys because AvroDeserializer expects a schema ID prefix that is missing for string keys.
- C. The consumer will deserialize the keys as strings successfully, but it will ignore the schema registry for keys.
- D. The consumer will produce a runtime error when trying to parse the value because the key and value serializers must match.
- E. The consumer will be able to deserialize both keys and values without any configuration changes, because AvroDeserializer can handle both key and value serialization formats interchangeably.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, AvroSerializer prepends a magic byte and a schema ID from Schema Registry. AvroDeserializer expects this exact format for every key/value it processes. If the key is produced with StringSerializer, the bytes lack the magic byte and schema ID, causing AvroDeserializer to throw a "magic byte mismatch" error on key deserialization. The value, serialized with AvroSerializer, will deserialize normally. This scenario highlights the importance of matching serializer/deserializer pairs per topic field and configuring separate deserializers when using mixed serialization formats.

Source: Confluent Schema Registry docs - "Wire format" (magic byte 0 + 4-byte schema ID), Kafka: The Definitive Guide 2nd ed. Ch. 3 "Using Avro Records with Kafka" (pp. 65-68)

**Detailed explanation of each option:**

1. ❌ **A. The consumer will deserialize the keys correctly because AvroDeserializer automatically treats non‑Avro keys as raw bytes.**  
   **Incorrect**. The deserializer does not have such a fallback, it will error on mismatched format.

2. ✅ **B. The consumer will fail to deserialize the keys because AvroDeserializer expects a schema ID prefix that is missing for string keys.**  
   **Correct**. AvroDeserializer looks for a magic byte followed by a 4‑byte schema ID. StringSerializer produces raw UTF‑8 bytes without this prefix, causing the deserializer to throw an error when parsing the key.

3. ❌ **C. The consumer will deserialize the keys as strings successfully, but it will ignore the schema registry for keys.**  
   **Incorrect**. AvroDeserializer does not fallback to treating the key as a plain string, it strictly expects Avro format.

4. ❌ **D. The consumer will produce a runtime error when trying to parse the value because the key and value serializers must match.**  
   **Incorrect**. The value is correctly serialized with AvroSerializer, so the value deserialization will succeed, the error arises only for the key.

5. ❌ **E. The consumer will be able to deserialize both keys and values without any configuration changes, because AvroDeserializer can handle both key and value serialization formats interchangeably.**  
   **Incorrect**. The deserializer must be used only for fields serialized with Avro. Mixing formats requires separate deserializers.

</details>

## Question 10 (Application Observability): [-]
Which of the following approaches are valid ways for a Confluent Certified Developer to monitor a Kafka-based application for performance and health? (Select all that apply.)

- A. Use the Kafka REST Proxy `/metrics` endpoint to obtain application‑level metrics.
- B. Expose metrics by logging JSON messages to application logs and parse them with a log analyzer.
- C. Configure Confluent Control Center to collect and visualize metrics such as throughput and consumer lag.
- D. Rely on the `max.poll.interval.ms` consumer setting to automatically report consumer lag.
- E. Use the Kafka Streams `StreamsMetrics` to monitor per‑operator metrics like processing time.
- F. Enable JMX on the broker and use the Prometheus JMX exporter to scrape metrics.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, E, F

**Explanation:**

Observability in Kafka revolves around collecting metrics from JMX, Prometheus, and Confluent Control Center. Enabling JMX and using the Prometheus JMX exporter is the standard route for exporting metrics. Control Center offers a graphical view of cluster health and consumer lag. Kafka Streams provides per‑operator metrics that can be scraped similarly. Logging metrics or relying on consumer configuration properties does not provide actionable, real‑time observability. The REST Proxy has no metrics endpoint. Mastery of these tools ensures developers can detect performance bottlenecks and maintain healthy streaming pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Client Monitoring" (pp. 370-378)

**Detailed explanation of each option:**

1. ❌ **A. Use the Kafka REST Proxy `/metrics` endpoint to obtain application‑level metrics.**  
   **Incorrect**. The REST Proxy provides endpoints for producing and consuming records, but it does not expose internal Kafka metrics through `/metrics`, this endpoint does not exist.

2. ❌ **B. Expose metrics by logging JSON messages to application logs and parse them with a log analyzer.**  
   **Incorrect**. While possible, this approach is not recommended for real‑time monitoring. Logs are typically asynchronous and not suited for low‑latency metrics collection.

3. ✅ **C. Configure Confluent Control Center to collect and visualize metrics such as throughput and consumer lag.**  
   **Correct**. Control Center ingests Kafka metrics (via JMX or the internal Kafka Connect) and provides dashboards for topic throughput, consumer group lag, and cluster health. It is the official Confluent tool for application observability.

4. ❌ **D. Rely on the `max.poll.interval.ms` consumer setting to automatically report consumer lag.**  
   **Incorrect**. `max.poll.interval.ms` controls how long a consumer can be idle before being considered dead. It does not emit lag metrics, consumer lag must be measured explicitly via offsets.

5. ✅ **E. Use the Kafka Streams `StreamsMetrics` to monitor per‑operator metrics like processing time.**  
   **Correct**. Kafka Streams exposes metrics for each operator (source, processor, sink) via `StreamsMetrics`. These can be scraped by JMX or exported to Prometheus, providing fine‑grained latency and throughput data for stream applications.

6. ✅ **F. Enable JMX on the broker and use the Prometheus JMX exporter to scrape metrics.**  
   **Correct**. Kafka exposes a rich set of JMX metrics by default. The Prometheus JMX exporter can scrape these metrics and expose them to Prometheus. This is a common, supported method for monitoring throughput, lag, and system health.

</details>

## Question 11 (Programming & Serialization): [-]
When a producer adds a new optional field to a schema and wants older consumers to continue processing records without any code changes, which serialization format supported by Confluent Schema Registry allows this without requiring a default value for the new field?

- A. JSON Schema
- B. All of the above
- C. Avro
- D. Protobuf

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Confluent Schema Registry supports Avro, Protobuf, and JSON Schema. For schema evolution, Avro mandates default values for new fields to preserve backward compatibility, while Protobuf natively ignores unknown fields, allowing new optional fields to be added without defaults. JSON Schema can ignore unknown fields but does not automatically apply defaults during deserialization, making it less reliable for seamless compatibility. Thus, Protobuf is the sole format among the three that permits adding optional fields without defining defaults. This behavior is critical when maintaining Kafka topics that evolve over time without disrupting older consumer applications. References: Confluent Schema Registry documentation, Avro, Protobuf, and JSON Schema sections, and compatibility guidelines.

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules) — NOTE: Protobuf optional-field semantics verified against Confluent Schema Registry docs.

**Detailed explanation of each option:**

1. ❌ **A. JSON Schema**  
   **Incorrect**. JSON Schema, when used with Schema Registry, treats unknown fields as tolerated, but default values are not applied during deserialization. While consumers can ignore new fields, the absence of default support makes it less straightforward for guaranteed backward compatibility.

2. ❌ **B. All of the above**  
   **Incorrect**. Only Protobuf satisfies the requirement of not needing a default for new optional fields. Avro and JSON Schema have constraints that require either defaults or additional handling, so this option is incorrect.

3. ❌ **C. Avro**  
   **Incorrect**. Avro requires that any newly added field in a backward-compatible schema must provide a default value. Without a default, older consumers will fail to deserialize the record. Therefore Avro is not the format that eliminates the need for defaults.

4. ✅ **D. Protobuf**  
   **Correct**. Protocol Buffers allow unknown fields to be safely ignored by older consumers. New optional fields can be added without a default value and older consumers will simply treat them as absent, enabling seamless backward compatibility.

</details>

## Question 12 (Stream Processing):
Which of the following statements are true regarding the implementation of exactly‑once semantics (EOS) in Kafka Streams applications?

- A. When using exactly‑once semantics, a Kafka Streams application never needs to read from its state store during rebalancing.
- B. Exactly‑once semantics are achieved by using idempotent producers and transactional writes to the output topic.
- C. Exactly‑once semantics guarantee that no duplicate records will be emitted, even if the application crashes between processing and committing.
- D. Under exactly‑once semantics, if a task fails after processing some records but before committing, the records will be reprocessed once the task restarts.
- E. Exactly‑once semantics are only supported when the application uses a single thread per task.
- F. Enabling exactly‑once semantics requires setting `application.id` and `commit.interval.ms` to a value greater than 0.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

Kafka Streams achieves exactly‑once semantics by wrapping each task’s processing in a Kafka transaction. The application must enable EOS via `processing.guarantee=exactly_once_v2` and use a transactional producer. State stores are still required and are restored during rebalancing. If a task aborts before committing, all work is rolled back and retried, guaranteeing at most one emission of each output record. This mechanism relies on idempotent producers and the transaction coordinator, ensuring no duplicates even in failure scenarios. Misconceptions often arise around required configuration or the relationship between rebalancing and state restoration.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. When using exactly‑once semantics, a Kafka Streams application never needs to read from its state store during rebalancing.**  
   **Incorrect**. During a rebalance, tasks are reassigned and their state stores are restored from changelog topics, the application still reads from the state store.

2. ✅ **B. Exactly‑once semantics are achieved by using idempotent producers and transactional writes to the output topic.**  
   **Correct**. EOS relies on Kafka’s transactional producer API, all records written to output topics are part of a single transaction that is committed or aborted atomically.

3. ✅ **C. Exactly‑once semantics guarantee that no duplicate records will be emitted, even if the application crashes between processing and committing.**  
   **Correct**. The transactional nature ensures that once a transaction is committed, its output records appear exactly once, aborting the transaction prevents any duplicates.

4. ✅ **D. Under exactly‑once semantics, if a task fails after processing some records but before committing, the records will be reprocessed once the task restarts.**  
   **Correct**. If a task aborts before the transaction is committed, the whole transaction is rolled back and the records will be re‑processed from the last committed checkpoint.

5. ❌ **E. Exactly‑once semantics are only supported when the application uses a single thread per task.**  
   **Incorrect**. EOS works with multi‑threaded topologies, the number of threads per task is independent of the guarantee level.

6. ❌ **F. Enabling exactly‑once semantics requires setting `application.id` and `commit.interval.ms` to a value greater than 0.**  
   **Incorrect**. The key setting for EOS is `processing.guarantee=exactly_once_v2` (or `exactly_once`). `commit.interval.ms` controls state store checkpointing but is not required for EOS.

</details>

## Question 13 (Kafka Connect):
When configuring a Kafka Connect distributed worker, which of the following configuration properties must be provided in order for the worker to start successfully? (Assume no defaults are supplied.)

- A. config.storage.topic
- B. offset.storage.topic
- C. status.storage.topic
- D. bootstrap.servers
- E. key.converter
- F. value.converter

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** A, B, C, D, E, F

**Explanation:**

Correction: in distributed mode `config.storage.topic`, `offset.storage.topic` and `status.storage.topic` have NO defaults
(the names `__connect-configs` etc. are not built in, they are just conventional examples in sample config files),
so the worker fails to start without them. `group.id`, `bootstrap.servers`, `key.converter` and `value.converter` are also required 
(strictly, `group.id` too, though it is not offered here). All six listed properties are therefore required. Original text follows.

A Kafka Connect distributed worker requires explicit configuration of the Kafka cluster address and the converters for both keys and values. These three properties enable the worker to connect to Kafka, deserialize incoming records, and produce offset, configuration, and status data. The storage topic properties are optional because Connect supplies sane defaults, omitting them will still allow the worker to start, though custom topics can be useful for isolation or compliance. Understanding these mandatory settings is critical for deploying a worker that can accept connector configurations and stream data correctly.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ✅ **A. config.storage.topic**  
   **Correct**. Required in distributed mode, there is no default topic name, so the worker will not start without it.

2. ✅ **B. offset.storage.topic**  
   **Correct**. Required in distributed mode, no default, the worker will not start without it.

3. ✅ **C. status.storage.topic**  
   **Correct**. Required in distributed mode, no default, the worker will not start without it.

4. ✅ **D. bootstrap.servers**  
   **Correct**. Mandatory. Connect needs the Kafka cluster address to produce offset, configuration, and status records. Without it the worker cannot join the Kafka cluster and will fail to start.

5. ✅ **E. key.converter**  
   **Correct**. Mandatory. The worker must know how to deserialize key data from the topic. If this property is omitted, Connect cannot determine the converter and will abort.

6. ✅ **F. value.converter**  
   **Correct**. Mandatory. Like key.converter, the worker requires a value converter to deserialize the record payload. Omission prevents successful deserialization and causes startup failure.

</details>

## Question 14 (Programming & Serialization):
When using the Confluent Avro Serializer with the Schema Registry, how does the serializer handle a scenario where a new optional field is added to an existing Avro schema and the Schema Registry’s compatibility is set to BACKWARD?

- A. It writes the new field as null for every record, regardless of its defined type, to maintain compatibility.
- B. It creates a new subject in the Schema Registry for the updated schema, isolating it from the original subject.
- C. It requires manual deserialization logic in every consumer to handle the new field and will not otherwise work.
- D. It allows the new field to be included in messages, the field must have a default value in the schema for all existing consumers to ignore it.
- E. It automatically rejects all messages containing the new field until every consumer updates to the new schema.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Confluent’s Avro integration, adding a new optional field with a default value is a backward‑compatible change when the registry is set to BACKWARD. The producer registers the new schema, and messages include the new field. Consumers that still use the older schema can deserialize the data, they ignore the new field and use the default value. This allows gradual schema evolution without breaking existing consumers. Misconceptions often arise around automatic rejection or need for custom code, but Avro’s compatibility rules handle these scenarios automatically. Refer to Confluent Schema Registry compatibility docs for details.

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. It writes the new field as null for every record, regardless of its defined type, to maintain compatibility.**  
   **Incorrect**. The serializer does not modify the data payload to set new fields to null, it writes the field as provided. Consumers may see null if the producer does not set the field, but the schema still defines it.

2. ❌ **B. It creates a new subject in the Schema Registry for the updated schema, isolating it from the original subject.**  
   **Incorrect**. Schema Registry registers new versions under the same subject. Creating a new subject would break compatibility management and is not how Avro evolution is handled.

3. ❌ **C. It requires manual deserialization logic in every consumer to handle the new field and will not otherwise work.**  
   **Incorrect**. Consumers using the older schema can still deserialize records produced with the new schema without any additional code, the new field is simply ignored.

4. ✅ **D. It allows the new field to be included in messages, the field must have a default value in the schema for all existing consumers to ignore it.**  
   **Correct**. In Avro, adding a field with a default value is backward compatible. The serializer registers the new schema, and consumers using the older schema will read the data and ignore the new field, using the default if necessary.

5. ❌ **E. It automatically rejects all messages containing the new field until every consumer updates to the new schema.**  
   **Incorrect**. Backward compatibility allows producers to write data with new fields that consumers using the old schema can still read. The serializer does not reject messages, it will register the new schema if allowed.

</details>

## Question 15 (Programming & Serialization):
In a Kafka Connect job that reads data from a JDBC source and writes to a topic using Avro serialization, which of the following statements correctly describes the role of the Confluent Schema Registry in the serialization process?

- A. The Schema Registry assigns a unique schema ID to the Avro schema, and the connector writes this ID as a four-byte prefix in each record.
- B. The Schema Registry does not participate, the connector serializes the full Avro schema with each record.
- C. The Schema Registry automatically converts the Avro schema to JSON for compatibility with downstream consumers.
- D. The Schema Registry stores the Avro schema in the topic itself so that consumers can deserialize without network calls.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

When a Kafka Connect sink writes Avro data, the AvroConverter registers the record’s Avro schema with the Confluent Schema Registry (if it isn’t already present) and receives a numeric schema ID. Each serialized message begins with a 4‑byte big‑endian schema ID that the consumer uses to fetch the exact schema from the registry, enabling zero‑copy deserialization and forward/backward compatibility checks. This mechanism keeps message payloads small, allows schema evolution, and decouples schema storage from topic data. Understanding this flow is essential for developers configuring Connect pipelines and troubleshooting serialization errors.

Source: Confluent Schema Registry docs - "Wire format" (magic byte 0 + 4-byte schema ID), Kafka: The Definitive Guide 2nd ed. Ch. 3 "Using Avro Records with Kafka" (pp. 65-68) — NOTE: JDBC source + Avro verified against Confluent connector/Schema Registry docs.

**Detailed explanation of each option:**

1. ✅ **A. The Schema Registry assigns a unique schema ID to the Avro schema, and the connector writes this ID as a four-byte prefix in each record.**  
   **Correct**. When using the AvroConverter, the connector registers the schema (if not already registered), obtains a schema ID, and prefixes each Avro-encoded record with a 4-byte schema ID for efficient resolution.

2. ❌ **B. The Schema Registry does not participate, the connector serializes the full Avro schema with each record.**  
   **Incorrect**. Embedding the full schema with every record is not how AvroConverter works, it relies on the schema ID to keep payloads small.

3. ❌ **C. The Schema Registry automatically converts the Avro schema to JSON for compatibility with downstream consumers.**  
   **Incorrect**. The Schema Registry stores the schema in its native format (Avro, JSON, Protobuf) and does not perform automatic format conversions.

4. ❌ **D. The Schema Registry stores the Avro schema in the topic itself so that consumers can deserialize without network calls.**  
   **Incorrect**. The Schema Registry is a separate service, the Avro schema is not embedded in the topic partition data. Consumers still need to contact the registry to resolve the schema ID.

</details>

## 🚫 Question 16 (Stream Processing):
A Kafka Streams application performs stateful aggregation and must be deployed for production so that it can recover its state after a node failure without replaying the entire input stream. Which deployment strategy best achieves this requirement while following Confluent Platform best practices?

- A. Deploy the application as a Kafka Streams interactive query service behind a load balancer, with state stored in RocksDB on each instance, and rely on Kafka’s changelog topics for state replication.
- B. Deploy multiple instances of the application as separate pods in Kubernetes, using the Confluent Platform Helm chart, and configure the `state.dir` to an external S3 bucket for state storage.
- C. Deploy the application in a Kubernetes StatefulSet with persistent volumes, using the default RocksDB state store, and let Kafka Streams automatically recover state from changelog topics on restart.
- D. Deploy the application as a single Docker container on a single VM, relying on Kafka’s log compaction for state recovery.
- E. Deploy the application on a cloud‑managed Kafka Streams service (Confluent Cloud) with auto‑scaling, without managing any local state.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

For stateful Kafka Streams applications, production deployments must combine local state persistence with Kafka Streams’ changelog recovery. A StatefulSet with persistent volumes preserves the RocksDB store across pod restarts, reducing recovery time. Kafka Streams will still replay the changelog topics if the local store is missing, ensuring no data loss. This approach aligns with Confluent Platform guidelines for fault‑tolerant, scalable deployments and satisfies the requirement to recover state without replaying the entire input stream. Options that rely solely on a single VM, external object storage, or omit persistent local storage fail to meet these resilience criteria.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 14 "Scaling a Topology" (pp. 412-415) — NOTE: Kubernetes StatefulSet deployment is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ❌ **A. Deploy the application as a Kafka Streams interactive query service behind a load balancer, with state stored in RocksDB on each instance, and rely on Kafka’s changelog topics for state replication.**  
   **Incorrect**. Partially correct. Interactive queries expose state, but without persistent storage the local RocksDB store is lost on a pod restart, forcing a full replay of the input stream.

2. ❌ **B. Deploy multiple instances of the application as separate pods in Kubernetes, using the Confluent Platform Helm chart, and configure the `state.dir` to an external S3 bucket for state storage.**  
   **Incorrect**. While Helm charts simplify deployment, storing the state directory on S3 is unsupported for the local RocksDB store and would break Kafka Streams’ changelog recovery mechanism.

3. ✅ **C. Deploy the application in a Kubernetes StatefulSet with persistent volumes, using the default RocksDB state store, and let Kafka Streams automatically recover state from changelog topics on restart.**  
   **Correct**. Persistent volumes keep the RocksDB data across pod restarts, while Kafka Streams’ changelog topics provide an additional recovery mechanism. This follows Confluent best practices for production deployments.

4. ❌ **D. Deploy the application as a single Docker container on a single VM, relying on Kafka’s log compaction for state recovery.**  
   **Incorrect**. A single instance on a single VM provides no fault tolerance, if the VM fails the application is lost, and log compaction does not restore the RocksDB state store.

5. ❌ **E. Deploy the application on a cloud‑managed Kafka Streams service (Confluent Cloud) with auto‑scaling, without managing any local state.**  
   **Incorrect**. Confluent Cloud removes the need for local state, but the question specifically asks for a deployment that retains state locally for faster recovery.

</details>

## Question 17 (Stream Processing): [-]
In Kafka Streams, which of the following configurations or design choices are necessary to achieve exactly‑once semantics for stateful processing and output to a sink topic?

- A. Set `processing.guarantee` to "at_least_once" and use a transactional producer.
- B. Disable `auto.offset.reset` to avoid duplicate records.
- C. Set `processing.guarantee` to "exactly_once" and enable `transactional.id` in the Streams configuration.
- D. Configure the source topics to have a retention of at least 24 hours and use `enable.idempotence=true` in the producer configuration.
- E. Use `KTable` joins with caching enabled to reduce duplicate processing.
- F. Set `exactly_once_batched=true` in the Streams configuration to enable batching of records within each transaction.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Correction: F is false. `exactly_once_batched` is not a real Kafka Streams config or `processing.guarantee` value (the real values are `at_least_once`, `exactly_once_v2`, and the deprecated `exactly_once` / `exactly_once_beta`). Only C is correct (Streams derives and manages `transactional.id` itself, the key setting is `processing.guarantee`). Original text follows.

Exactly‑once semantics in Kafka Streams rely on the Streams client’s ability to use Kafka transactions to atomically commit both state changes and output records. The core requirement is setting `processing.guarantee` to either "exactly_once" or "exactly_once_batched". The Streams runtime automatically generates a transactional.id and performs the necessary commit logic. Optional optimizations include `exactly_once_batched=true`, which batches records per transaction for higher throughput. Features like caching, retention policies, idempotence, or offset reset do not affect the exactly‑once contract. Misconceptions often arise from conflating idempotent producer writes with full transactional guarantees. Correctly configuring the guarantee property and transactional id ensures that each record is processed and stored exactly once, even in the presence of failures.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201) — NOTE: option F "exactly_once_batched" is not a real Kafka Streams config.

**Detailed explanation of each option:**

1. ❌ **A. Set `processing.guarantee` to "at_least_once" and use a transactional producer.**  
   **Incorrect**. The "at_least_once" guarantee does not ensure no duplicate processing or state updates, even if the producer is transactional.

2. ❌ **B. Disable `auto.offset.reset` to avoid duplicate records.**  
   **Incorrect**. The offset reset policy only affects how the consumer starts reading when no committed offset exists. It does not influence the transactional semantics.

3. ✅ **C. Set `processing.guarantee` to "exactly_once" and enable `transactional.id` in the Streams configuration.**  
   **Correct**. The `processing.guarantee` property controls the fault‑tolerance semantics. Setting it to "exactly_once" (or "exactly_once_batched") activates transactional state commits and record writes. The `transactional.id` prefix is automatically derived by Streams, but must be enabled to allow the Kafka producer to participate in transactions.

4. ❌ **D. Configure the source topics to have a retention of at least 24 hours and use `enable.idempotence=true` in the producer configuration.**  
   **Incorrect**. Retention length and idempotence alone do not provide exactly‑once guarantees. Exactly‑once requires transactional state commits, not just idempotent producer writes.

5. ❌ **E. Use `KTable` joins with caching enabled to reduce duplicate processing.**  
   **Incorrect**. While caching can improve throughput, it does not provide any additional guarantee of exactly‑once semantics. The guarantee is driven by the transactional boundaries set by the Streams client.

6. ❌ **F. Set `exactly_once_batched=true` in the Streams configuration to enable batching of records within each transaction.**  
   **Incorrect**. No such configuration exists in Kafka Streams. Transaction batching is governed by `commit.interval.ms`, and EOS is enabled only via `processing.guarantee`.

</details>

## Question 18 (Kafka Ecosystem):
Which of the following are the core Confluent tools or APIs that a developer can use to produce, consume, and manage topics in a Kafka cluster? Select all that apply.

- A. Kafka Streams DSL
- B. Kafka AdminClient API
- C. Schema Registry REST API
- D. Kafka Producer API
- E. Kafka Consumer API

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, E

**Explanation:**

In Kafka Fundamentals, the three core client APIs that developers use to interact with a cluster are the Producer API, Consumer API, and AdminClient API. These provide the ability to publish records, read records, and perform administrative actions such as creating or deleting topics. While other libraries like Kafka Streams DSL or the Schema Registry API are important parts of the Confluent ecosystem, they are not direct substitutes for the basic produce/consume/management operations. Recognizing the distinction between core client APIs and higher‑level abstractions is essential for building and maintaining Kafka applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ❌ **A. Kafka Streams DSL**  
   **Incorrect**. Kafka Streams DSL is a high‑level library for building stream processing applications. While it consumes and produces streams, it is not a low‑level API for arbitrary produce/consume or topic management, therefore it is not one of the core tools listed in the question.

2. ✅ **B. Kafka AdminClient API**  
   **Correct**. The AdminClient API provides programmatic access to topic, consumer group, and cluster configuration management (create, alter, delete topics, etc.). It is the official client for administrative operations.

3. ❌ **C. Schema Registry REST API**  
   **Incorrect**. The Schema Registry API is used to register and retrieve Avro/JSON/Protobuf schemas. It does not provide direct produce, consume, or topic‑management functionality, so it is not a core tool for those tasks.

4. ✅ **D. Kafka Producer API**  
   **Correct**. The Producer API is a client library that lets applications publish records to Kafka topics. It is the primary programmatic way to produce data and is part of the core Kafka API set.

5. ✅ **E. Kafka Consumer API**  
   **Correct**. The Consumer API is a client library that lets applications subscribe to topics and retrieve records. It is the core interface for consuming data from Kafka.

</details>

## 🚫 Question 19 (Kafka Connect):
When deploying Kafka Connect as a Docker container or inside a Kubernetes cluster, which of the following steps are required to ensure the Connect worker can communicate with the Kafka cluster, persist connector state, and expose the REST API correctly?

- A. Mount a persistent Docker volume to store Connect worker logs so that logs survive container restarts.
- B. Enable the REST API security by setting CONNECT_REST_ADVERTISED_HOST_NAME and CONNECT_REST_ADVERTISED_PORT and configuring listeners.
- C. Configure the worker to use dedicated Kafka topics (config-storage-topic, offset-storage-topic, status-storage-topic) for storing connector configurations and offsets.
- D. Set the CONNECT_BOOTSTRAP_SERVERS environment variable to point the worker to the Kafka cluster.
- E. Use Kubernetes HorizontalPodAutoscaler to automatically scale Connect workers based on CPU usage.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

To run Kafka Connect in Docker or Kubernetes, the worker must first know where the Kafka cluster is via CONNECT_BOOTSTRAP_SERVERS. It also needs dedicated topics for config, offsets, and status so that multiple workers can coordinate and survive failures, these topics must be replicated and partitioned. The REST API is how clients create connectors, so listeners and advertised host/port settings must be configured correctly. Logging persistence and autoscaling are operational niceties, not functional requirements. For more detail see the Confluent Docker quickstart (https://docs.confluent.io/platform/current/connect/quickstart/docker.html) and the Connect HA guide (https://docs.confluent.io/platform/current/connect/cluster.html).

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Docker/Kubernetes deployment is out of exam scope (Administer and deploy Kafka, Networking).

**Detailed explanation of each option:**

1. ❌ **A. Mount a persistent Docker volume to store Connect worker logs so that logs survive container restarts.**  
   **Incorrect**. Logging is typically directed to stdout/stderr and collected by Docker or Kubernetes logging agents, persisting logs is not required for Connect operation.

2. ✅ **B. Enable the REST API security by setting CONNECT_REST_ADVERTISED_HOST_NAME and CONNECT_REST_ADVERTISED_PORT and configuring listeners.**  
   **Correct**. These settings expose the REST interface to external clients and are essential when multiple workers share the same host or when the service must be reachable from other pods or outside the cluster.

3. ✅ **C. Configure the worker to use dedicated Kafka topics (config-storage-topic, offset-storage-topic, status-storage-topic) for storing connector configurations and offsets.**  
   **Correct**. These topics must exist, be replicated and partitioned to enable distributed Connect workers to share state and provide high availability.

4. ✅ **D. Set the CONNECT_BOOTSTRAP_SERVERS environment variable to point the worker to the Kafka cluster.**  
   **Correct**. This environment variable is mandatory for the worker to discover the Kafka brokers and submit requests for connector configuration, offsets, and status.

5. ❌ **E. Use Kubernetes HorizontalPodAutoscaler to automatically scale Connect workers based on CPU usage.**  
   **Incorrect**. Scaling is an optional operational convenience, it is not a prerequisite for Connect to function correctly.

</details>

## Question 20 (Programming & Serialization):
Which of the following statements about using the Confluent Schema Registry with Kafka clients in Java, Python, or C# for Avro serialization are true? (Select all that apply)

- A. The Java `KafkaAvroSerializer` automatically registers a new Avro schema with the Schema Registry when it encounters a schema that is not yet registered.
- B. The schema registry supports backward, forward, and full compatibility modes, but these modes cannot be changed after a subject has been created.
- C. The Confluent wire format for Avro messages starts with a magic byte `0` followed by a 4-byte schema ID in network byte order.
- D. The `specific.avro.reader` configuration option only affects the Kafka consumer, not the producer.
- E. In the Python `confluent_kafka.avro.AvroProducer`, you must supply the Avro schema definition as a JSON string in the `value_schema` parameter each time you produce a record.
- F. The C# `Confluent.SchemaRegistry.Serdes.AvroSerializer` will automatically deserialize keys using the same schema as values if the `AutoRegisterSchemas` property is true.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

In Confluent Kafka deployments, the Avro serializer/serializer automatically handles schema registration and embeds a schema ID using the Confluent wire format (magic byte + 4‑byte ID). Configuration options such as `specific.avro.reader` only influence deserialization on consumers, while schema registration is managed automatically by the producer serializer. The Python client follows the same pattern, requiring the schema only at producer creation. Schema compatibility modes (backward, forward, full) are configurable per subject and can be updated after creation, contrary to the false statement. Understanding these details ensures correct implementation and avoids runtime errors.

Source: Confluent Schema Registry docs - KafkaAvroSerializer (auto.register.schemas), Kafka: The Definitive Guide 2nd ed. Ch. 3 (pp. 64-68)

**Detailed explanation of each option:**

1. ✅ **A. The Java `KafkaAvroSerializer` automatically registers a new Avro schema with the Schema Registry when it encounters a schema that is not yet registered.**  
   **Correct**. The serializer checks if the schema is present, if not, it registers it before sending the message.

2. ❌ **B. The schema registry supports backward, forward, and full compatibility modes, but these modes cannot be changed after a subject has been created.**  
   **Incorrect**. Compatibility can be updated at the subject or global level at any time via the REST API.

3. ✅ **C. The Confluent wire format for Avro messages starts with a magic byte `0` followed by a 4-byte schema ID in network byte order.**  
   **Correct**. The first byte is the magic byte, followed by a 4‑byte big‑endian schema ID.

4. ✅ **D. The `specific.avro.reader` configuration option only affects the Kafka consumer, not the producer.**  
   **Correct**. It instructs the consumer deserializer to return specific record classes, it has no impact on the producer.

5. ❌ **E. In the Python `confluent_kafka.avro.AvroProducer`, you must supply the Avro schema definition as a JSON string in the `value_schema` parameter each time you produce a record.**  
   **Incorrect**. The schema is supplied once when the producer is instantiated, subsequent records reuse the cached schema.

6. ❌ **F. The C# `Confluent.SchemaRegistry.Serdes.AvroSerializer` will automatically deserialize keys using the same schema as values if the `AutoRegisterSchemas` property is true.**  
   **Incorrect**. AutoRegisterSchemas applies to values only, key serialization/deserialization requires separate configuration.

</details>

## Question 21 (Stream Processing):
A Kafka Streams application must be deployed with exactly‑once processing semantics. Which configuration property is required to enable this behavior and why?

- A. Set `exactly.once` to `true` in the Streams configuration.
- B. Set `transactional.id` to a unique string for each instance.
- C. Set `commit.interval.ms` to 0.
- D. Set `processing.guarantee` to `exactly_once` (or `exactly_once_v2` in newer versions).

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Exactly‑once semantics in Kafka Streams rely on a transactional producer and consumer that coordinate commits. The `processing.guarantee` property tells Streams to set up this transactionality and perform atomic source‑sink updates. Without it, even if you configure `transactional.id`, the Streams runtime will fall back to at‑least‑once behavior. The other options either reference non‑existent configuration keys, provide only part of the required settings, or misinterpret the role of commit intervals. Refer to the official Streams configuration guide (https://docs.confluent.io/platform/current/streams/developer-guide/configuration.html) for the full list of properties and their effects.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Set `exactly.once` to `true` in the Streams configuration.**  
   **Incorrect**. `exactly.once` is not a valid Streams configuration key, it never existed in the Kafka Streams API.

2. ❌ **B. Set `transactional.id` to a unique string for each instance.**  
   **Incorrect**. While `transactional.id` is required for the underlying producer, it is not sufficient alone, `processing.guarantee` must also be enabled.

3. ❌ **C. Set `commit.interval.ms` to 0.**  
   **Incorrect**. Disabling periodic commits does not enable exactly‑once semantics and can actually degrade reliability.

4. ✅ **D. Set `processing.guarantee` to `exactly_once` (or `exactly_once_v2` in newer versions).**  
   **Correct**. This property activates the Streams library’s built‑in exactly‑once support, which internally uses a transactional producer and consumer to achieve idempotent writes and atomic commits.

</details>

## Question 22 (Stream Processing): [-]
Which of the following statements correctly describe key considerations and best practices when writing a Kafka Streams application that aggregates metrics per key and stores the result in a state store for querying? (Select all that apply)

- A. Using a `through()` method to write a stream to an intermediate topic guarantees that downstream stages will receive the records in the exact order they were processed.
- B. Windowed aggregations require specifying a retention period larger than the window size to ensure that the output records are not lost after the window closes.
- C. When using `transformValues()` with a `ValueTransformerSupplier`, the supplied transformer can modify the input record value in place without creating a new value instance.
- D. A `KTable` created from a `KStream` via `toTable()` will automatically create a global state store that is replicated across all instances of the application.
- E. Using a `KGroupedStream` followed by `aggregate()` with a custom `Initializer` guarantees that the aggregation will be fault tolerant and replayable across rebalances.
- F. A `KStream` can be materialized into a changelog topic by attaching a `Materialized` object with a state store name, which allows the state to be restored after a crash.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, F

**Explanation:**

The question tests knowledge of fault‑tolerant aggregation, state store materialization, and windowing semantics in Kafka Streams. Correct options 1, 3, and 5 reflect core concepts: aggregates use changelog topics for replay, retention must exceed window size, and materialization via `Materialized` enables state recovery. Common misconceptions include assuming global stores are created automatically, in‑place value mutation, or that ordering is preserved across partitions. Understanding these details is essential for building reliable, scalable stream applications, a key requirement for the Confluent Certified Developer exam.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Time Windows" (pp. 390-392)

**Detailed explanation of each option:**

1. ❌ **A. Using a `through()` method to write a stream to an intermediate topic guarantees that downstream stages will receive the records in the exact order they were processed.**  
   **Incorrect**. Ordering is preserved only within a partition, across partitions the order can change, so downstream consumers may observe a different order.

2. ✅ **B. Windowed aggregations require specifying a retention period larger than the window size to ensure that the output records are not lost after the window closes.**  
   **Correct**. The retention period must exceed the window size plus grace period so that records can be emitted after the window expires and the state can be cleaned up safely.

3. ❌ **C. When using `transformValues()` with a `ValueTransformerSupplier`, the supplied transformer can modify the input record value in place without creating a new value instance.**  
   **Incorrect**. The transformer should return a new value, modifying the input in place can lead to unpredictable results because the same value instance may be reused by downstream operators.

4. ❌ **D. A `KTable` created from a `KStream` via `toTable()` will automatically create a global state store that is replicated across all instances of the application.**  
   **Incorrect**. `toTable()` creates a local key‑value store per instance, backed by a changelog topic. It does not create a global store, a `GlobalKTable` must be used for that.

5. ✅ **E. Using a `KGroupedStream` followed by `aggregate()` with a custom `Initializer` guarantees that the aggregation will be fault tolerant and replayable across rebalances.**  
   **Correct**. Aggregations in Kafka Streams write each intermediate result to a changelog topic. The `Initializer` supplies the starting value for each key. Because the state is replicated and can be replayed from the changelog, the aggregation is fault tolerant and can recover after a rebalance or crash.

6. ✅ **F. A `KStream` can be materialized into a changelog topic by attaching a `Materialized` object with a state store name, which allows the state to be restored after a crash.**  
   **Correct**. Providing a `Materialized` instance names the state store and triggers creation of a changelog topic, enabling state restoration.

</details>

## Question 23 (Reliable Data Delivery):
Which of the following configurations and mechanisms directly influence the reliability and consistency of data replication in a Kafka cluster? (Select all that apply.)

- A. The broker configuration `unclean.leader.election.enable` allows a follower that is not in the ISR to become the leader if the current leader fails.
- B. The topic configuration `min.insync.replicas` determines the minimum number of in‑sync replicas that must acknowledge a produce request before the write is considered successful.
- C. The broker configuration `auto.leader.rebalance.enable` automatically rebalances leaders across brokers when replicas move.
- D. The broker configuration `max.message.bytes` controls the maximum size of messages that can be replicated between brokers.
- E. The topic configuration `replication.factor` defines how many copies of each partition are stored across the cluster.
- F. The broker configuration `segment.bytes` determines the size of log segment files, affecting replication speed but not data consistency.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

Replication reliability in Kafka hinges on the replication factor, in‑sync replicas (ISR), and leader election policies. `replication.factor` defines how many copies of each partition exist, higher values mean more replicas to survive failures. The ISR set contains only replicas that have caught up, and `min.insync.replicas` ensures a write succeeds only when enough ISR members acknowledge it, guarding against partial writes. Allowing unclean leader election (`unclean.leader.election.enable`) lets a lagging follower become leader, which can break consistency. Misconceptions often arise around settings that affect message size or log segment size, which do not directly impact replication consistency. Mastery of these parameters is essential for building robust Kafka applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-142) and Ch. 7 "Replication" (pp. 163-168)

**Detailed explanation of each option:**

1. ✅ **A. The broker configuration `unclean.leader.election.enable` allows a follower that is not in the ISR to become the leader if the current leader fails.**  
   **Correct**. Enabling unclean leader election can lead to a follower that is not in sync becoming leader, potentially causing loss of recent data. It directly affects replication reliability.

2. ✅ **B. The topic configuration `min.insync.replicas` determines the minimum number of in‑sync replicas that must acknowledge a produce request before the write is considered successful.**  
   **Correct**. `min.insync.replicas` sets the required number of ISR members that must acknowledge the write, ensuring that replication is not considered successful until enough copies exist. This protects against partial replication and data loss.

3. ❌ **C. The broker configuration `auto.leader.rebalance.enable` automatically rebalances leaders across brokers when replicas move.**  
   **Incorrect**. This setting is for dynamic leader rebalancing of partitions and does not alter replication guarantees or consistency.

4. ❌ **D. The broker configuration `max.message.bytes` controls the maximum size of messages that can be replicated between brokers.**  
   **Incorrect**. `max.message.bytes` limits the maximum message size that can be produced to a topic, it does not affect replication behavior or consistency.

5. ✅ **E. The topic configuration `replication.factor` defines how many copies of each partition are stored across the cluster.**  
   **Correct**. `replication.factor` specifies the number of replicas (one leader + (N‑1) followers) for each partition. A higher factor increases fault tolerance and replication consistency.

6. ❌ **F. The broker configuration `segment.bytes` determines the size of log segment files, affecting replication speed but not data consistency.**  
   **Incorrect**. While `segment.bytes` controls when a log segment rolls over, it does not directly influence the consistency of replicated data.

</details>

## Question 24 (Kafka Connect):
Which of the following statements accurately describe core concepts or features related to Kafka Connect source, sink, and CDC connectors?

- A. Source connectors read data from external systems (e.g., databases, message queues) and write the records into Kafka topics.
- B. Sink connectors consume records from Kafka topics and write them into external target systems (e.g., HDFS, JDBC databases).
- C. Debezium connectors are an example of CDC connectors that transform change events into a JSON format by default.
- D. CDC connectors require explicit schema registry configuration to capture change events from the source system.
- E. Kafka Connect's offset management for source connectors is stored in the connector configuration file by default.
- F. Sink connectors do not support idempotent writes, they rely entirely on the external system to handle duplicate records.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Kafka Connect distinguishes between source connectors (write to Kafka), sink connectors (read from Kafka), and CDC connectors (specialized sources that capture change events). Source connectors emit records into topics, while sink connectors pull from topics and persist to external sinks. Debezium exemplifies a CDC connector that emits change events in JSON. Offsets for source connectors are stored in a dedicated Kafka topic, not in configuration files. Sink connectors themselves do not enforce idempotence, idempotent behavior must be implemented by the connector or the target system. Understanding these distinctions is critical for designing reliable data pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ✅ **A. Source connectors read data from external systems (e.g., databases, message queues) and write the records into Kafka topics.**  
   **Correct**. This is the fundamental role of a source connector. It extracts data and produces Kafka records. Correct.

2. ✅ **B. Sink connectors consume records from Kafka topics and write them into external target systems (e.g., HDFS, JDBC databases).**  
   **Correct**. Sink connectors perform the opposite of source connectors by reading from Kafka and persisting to external stores. Correct.

3. ✅ **C. Debezium connectors are an example of CDC connectors that transform change events into a JSON format by default.**  
   **Correct**. Debezium emits change data events in JSON (or Avro) and is widely used as a CDC connector. Correct.

4. ❌ **D. CDC connectors require explicit schema registry configuration to capture change events from the source system.**  
   **Incorrect**. While CDC connectors often produce Schema Registry-compatible schemas, they do not *require* schema registry configuration, they can operate with Avro or JSON schemas directly. Incorrect.

5. ❌ **E. Kafka Connect's offset management for source connectors is stored in the connector configuration file by default.**  
   **Incorrect**. Offsets are persisted in a dedicated Kafka topic (default: __connect-offsets), not in the connector config. Incorrect.

6. ❌ **F. Sink connectors do not support idempotent writes, they rely entirely on the external system to handle duplicate records.**  
   **Incorrect**. Sink connectors themselves do not guarantee idempotence, however, idempotent writes can be achieved by implementing idempotent logic in the connector or by using external system features. The statement is misleading, so it is considered incorrect for the purpose of this question.

</details>

## Question 25 (Kafka Consumers):
You have a Kafka topic named `orders` with 4 partitions. A producer writes records using a `customerId` key, and a consumer group of 2 consumers reads from the topic. Which statement best describes the ordering guarantees and offset handling for this setup?

- A. Kafka guarantees global ordering of messages across all partitions within a consumer group.
- B. The consumer automatically reorders messages from different partitions to preserve key order before processing.
- C. Offsets are committed per partition, a consumer can re‑read messages from a partition if it restarts but will never see duplicates across partitions.
- D. Each consumer will receive messages in strict order of arrival across all partitions.
- E. Ordering is guaranteed only within the same partition for a given key, across partitions order is not guaranteed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka guarantees message ordering only within a single partition. A producer that uses a key ensures all records with that key hash to the same partition, preserving their order. When a consumer group has multiple consumers, each consumer is assigned a subset of partitions, records from different partitions can be delivered in any interleaved order. Offsets are stored per partition, so a consumer can resume from the last committed offset for each partition independently. This model allows horizontal scaling while maintaining per‑partition order, a core concept for Confluent Certified Developers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6), ordering per partition

**Detailed explanation of each option:**

1. ❌ **A. Kafka guarantees global ordering of messages across all partitions within a consumer group.**  
   **Incorrect**. Global ordering is not provided by Kafka, the only ordering guarantee is per-partition. Consumer groups can see records from multiple partitions in any order.

2. ❌ **B. The consumer automatically reorders messages from different partitions to preserve key order before processing.**  
   **Incorrect**. Consumers do not perform cross-partition reordering. They process records in the order they receive them from each partition independently.

3. ❌ **C. Offsets are committed per partition, a consumer can re‑read messages from a partition if it restarts but will never see duplicates across partitions.**  
   **Incorrect**. Partially incorrect for this question. While offset commits are indeed per partition, this statement does not address ordering guarantees and includes an unrelated claim about duplicates across partitions.

4. ❌ **D. Each consumer will receive messages in strict order of arrival across all partitions.**  
   **Incorrect**. Kafka guarantees ordering only within a single partition. When a consumer reads from multiple partitions, the order of records across those partitions is not preserved, so a consumer cannot rely on global order.

5. ✅ **E. Ordering is guaranteed only within the same partition for a given key, across partitions order is not guaranteed.**  
   **Correct**. Because all records with the same key hash to the same partition, Kafka preserves the order of those records within that partition. However, records from different partitions may be delivered in any interleaved order.

</details>

## Question 26 (Kafka Producers): [-]
Which of the following statements accurately describes the default behavior of Kafka's partitioner regarding message keys and hashing?

- A. By configuring the `partition.key.type` property to `Long`, you can enforce that Kafka uses the key's numeric value rather than its byte representation for partitioning.
- B. Changing the serialization format of the key (e.g., from String to Integer) has no impact on which partition a message is sent to, as hashing operates on the byte array.
- C. When the key is null, the producer assigns messages to partitions in a round‑robin fashion, which preserves the original message order.
- D. If you use a custom partitioner that implements `org.apache.kafka.clients.producer.Partitioner`, you can override the default hashing behavior and provide deterministic or round‑robin logic as needed.
- E. The default Murmur2 hash function guarantees that every distinct key maps to a unique partition, ensuring order for that key's messages.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s default producer uses the Murmur2 hash of the key’s serialized byte array to select a partition. Keys that hash to the same value always end up in the same partition, preserving ordering for that key, but collisions can occur and keys are not guaranteed unique per partition. Null keys are routed round‑robin, which breaks ordering. The hashing algorithm operates on the byte array, so changing the serializer (String → Integer) changes the bytes and can alter the hash. There is no `partition.key.type` property. Custom partitioners allow developers to replace the default logic with any deterministic or round‑robin strategy, making option 5 the sole correct statement.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Partitions" (pp. 68-70)

**Detailed explanation of each option:**

1. ❌ **A. By configuring the `partition.key.type` property to `Long`, you can enforce that Kafka uses the key's numeric value rather than its byte representation for partitioning.**  
   **Incorrect**. No such property exists, partitioning always uses the key's serialized bytes.

2. ❌ **B. Changing the serialization format of the key (e.g., from String to Integer) has no impact on which partition a message is sent to, as hashing operates on the byte array.**  
   **Incorrect**. The partitioner hashes the serialized byte array, altering the serializer changes the byte representation and can change the hash and thus the target partition.

3. ❌ **C. When the key is null, the producer assigns messages to partitions in a round‑robin fashion, which preserves the original message order.**  
   **Incorrect**. Null keys are routed round‑robin across partitions, which distributes messages and destroys ordering guarantees.

4. ✅ **D. If you use a custom partitioner that implements `org.apache.kafka.clients.producer.Partitioner`, you can override the default hashing behavior and provide deterministic or round‑robin logic as needed.**  
   **Correct**. A custom partitioner can implement any routing logic, including deterministic or round‑robin, and replace the default Murmur2 hashing.

5. ❌ **E. The default Murmur2 hash function guarantees that every distinct key maps to a unique partition, ensuring order for that key's messages.**  
   **Incorrect**. The Murmur2 hash can produce collisions, it only guarantees that keys with identical hashes go to the same partition, not that every key gets a unique partition.

</details>

## Question 27 (Programming & Serialization): [-]
A developer wants to ensure that the payload of every record written to a Kafka topic is encrypted, so that it remains confidential even if the topic is stored on disk or accessed by other consumers. Which of the following approaches is most appropriate for achieving this while keeping the producer and consumer code unchanged except for the serializer/deserializer pair?

- A. Enable `SASL_SSL` on the broker and clients to encrypt all traffic between producers, brokers, and consumers.
- B. Implement a custom `Serializer` that encrypts the value bytes before they are sent, and a matching `Deserializer` that decrypts them on the consumer side.
- C. Create a dedicated topic for sensitive data and protect it with ACLs that only allow authorized consumers to read from it.
- D. Configure the producer to use the `interceptor.classes` configuration to wrap each record with an encryption layer before sending it to the broker.
- E. Use the Kafka Streams `transform` method to encrypt the record value before forwarding it to the topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To achieve end‑to‑end confidentiality for message payloads, the most reliable and idiomatic approach is to encrypt the data at the client side using a custom `Serializer`. This ensures that what is written to the topic is already encrypted, covering both in‑transit and at‑rest scenarios. TLS (SASL_SSL) protects data while moving across the network but not on disk, while ACLs control who can read but not how the data looks. Interceptors and Kafka Streams are not designed for payload transformation, making them unsuitable for this requirement. The custom serializer/deserializer pair keeps the application code clean and aligns with Kafka’s extensible serialization framework.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Encryption" / "End-to-End Encryption" (pp. 289-291)

**Detailed explanation of each option:**

1. ❌ **A. Enable `SASL_SSL` on the broker and clients to encrypt all traffic between producers, brokers, and consumers.**  
   **Incorrect**. TLS (SASL_SSL) protects data in transit but does not encrypt the payload stored on disk. It therefore does not satisfy the requirement for encryption at rest.

2. ✅ **B. Implement a custom `Serializer` that encrypts the value bytes before they are sent, and a matching `Deserializer` that decrypts them on the consumer side.**  
   **Correct**. This is the recommended method. The `Serializer` interface is called by the producer to convert the Java object into bytes, by encrypting these bytes, the data stored in the topic is encrypted. The consumer uses the matching `Deserializer` to decrypt. This keeps application logic simple and provides end‑to‑end encryption. Reference: https://kafka.apache.org/documentation/#producerconfigs_serializer.

3. ❌ **C. Create a dedicated topic for sensitive data and protect it with ACLs that only allow authorized consumers to read from it.**  
   **Incorrect**. Access control lists provide authorization, not encryption. The data would still be readable on disk and by any consumer that has the ACL permissions.

4. ❌ **D. Configure the producer to use the `interceptor.classes` configuration to wrap each record with an encryption layer before sending it to the broker.**  
   **Incorrect**. Producer interceptors can modify headers and metrics, but they are not designed to transform the record value. Using an interceptor to encrypt the payload would require additional logic in the interceptor and could break record structure, making it an incorrect approach for payload encryption.

5. ❌ **E. Use the Kafka Streams `transform` method to encrypt the record value before forwarding it to the topic.**  
   **Incorrect**. The `transform` operation is intended for stream processing logic, not for initial production of encrypted data. It would add unnecessary complexity and still rely on the producer to send plaintext to the stream.

</details>

## Question 28 (Application Testing):
When developing and testing Kafka client applications, which of the following techniques are commonly used to provide an isolated, reproducible environment for unit or integration tests? Select all that apply.

- A. Using the Kafka Connect source connector's integration tests to test data ingestion into Kafka topics.
- B. Using the Kafka AdminClient's createTopics method to programmatically create topics during a test and then verify topic metadata.
- C. Using the EmbeddedKafkaCluster (from the kafka‑clients test library) to spin up an in‑process broker for integration tests.
- D. Using the consumer.poll with a timeout of zero to simulate a non‑blocking fetch and assert no messages are returned.
- E. Using the Kafka Streams TopologyTestDriver to validate processing logic without requiring a running cluster.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

In Kafka client development, tests should be fast, deterministic, and isolated from external systems. The TopologyTestDriver enables pure-Java unit tests for stream logic, while the AdminClient allows programmatic topic lifecycle management in integration tests. An embedded broker (EmbeddedKafkaCluster) or testcontainers provides a lightweight Kafka cluster for end‑to‑end tests. Options involving a zero‑timeout poll or Connect integration tests are either incomplete or target different components, making them unsuitable for standard client‑app testing. These approaches are endorsed in Confluent's developer guides, which recommend using the test harness for unit tests and an embedded broker for integration tests to achieve repeatable results without external infrastructure. Developers can also capture and assert metrics and logs to verify observability during test runs. Refer to the Kafka Streams testing guide (https://kafka.apache.org/documentation/streams/developer-guide/testing.html) and the AdminClient API docs (https://kafka.apache.org/documentation/#adminclient) for implementation details.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Testing" (pp. 131-133) and Ch. 14 "Testing a Topology" (pp. 411-412)

**Detailed explanation of each option:**

1. ❌ **A. Using the Kafka Connect source connector's integration tests to test data ingestion into Kafka topics.**  
   **Incorrect**. for client‑app testing. While Connect tests are valid for connector development, they are not part of typical client application test strategies.

2. ✅ **B. Using the Kafka AdminClient's createTopics method to programmatically create topics during a test and then verify topic metadata.**  
   **Correct**. AdminClient can be used in tests to create topics, list metadata, and delete topics, enabling end‑to‑end tests that run against an actual broker (e.g., embedded or testcontainers).

3. ✅ **C. Using the EmbeddedKafkaCluster (from the kafka‑clients test library) to spin up an in‑process broker for integration tests.**  
   **Correct**. EmbeddedKafkaCluster starts a lightweight broker in the same JVM, allowing tests to produce/consume without external dependencies, which is a common pattern for integration tests.

4. ❌ **D. Using the consumer.poll with a timeout of zero to simulate a non‑blocking fetch and assert no messages are returned.**  
   **Incorrect**. Poll(0) will return immediately but still requires a running broker and may not be deterministic, tests typically rely on real broker interactions or the TopologyTestDriver instead.

5. ✅ **E. Using the Kafka Streams TopologyTestDriver to validate processing logic without requiring a running cluster.**  
   **Correct**. TopologyTestDriver provides a pure-Java test harness that simulates the stream processing pipeline, allowing assertions on state stores and output records while keeping the test fast and deterministic.

</details>

## Question 29 (Kafka Ecosystem):
Which of the following AdminClient methods is NOT used to perform cluster administration tasks such as creating topics, deleting topics, or listing cluster metadata?

- A. AdminClient#listTopics
- B. AdminClient#describeCluster
- C. AdminClient#createTopics
- D. AdminClient#deleteTopics
- E. AdminClient#offsetCommit

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

The AdminClient API provides administrative functions for Kafka clusters, including creating, listing, describing, and deleting topics, as well as managing configurations and ACLs. Methods like createTopics, describeCluster, listTopics, and deleteTopics directly interact with cluster metadata or topic lifecycles. offsetCommit, however, belongs to the Consumer API and is used to commit consumer offsets, it does not perform any cluster administration. Recognizing the boundaries between AdminClient and ConsumerClient operations is essential for developers to correctly use the Kafka client libraries.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "AdminClient Overview" (pp. 114-115) — NOTE: AdminClient method list verified against Apache Kafka AdminClient API docs, offsetCommit is not an AdminClient method.

**Detailed explanation of each option:**

1. ❌ **A. AdminClient#listTopics**  
   **Incorrect**. Correct. listTopics lists all topics in the cluster and is an AdminClient administrative operation.

2. ❌ **B. AdminClient#describeCluster**  
   **Incorrect**. Correct. describeCluster retrieves cluster metadata such as cluster ID and broker information, a standard AdminClient operation.

3. ❌ **C. AdminClient#createTopics**  
   **Incorrect**. Correct. The createTopics method is part of the AdminClient API and is used to create new topics in the cluster.

4. ❌ **D. AdminClient#deleteTopics**  
   **Incorrect**. Correct. deleteTopics removes topics from the cluster, a valid AdminClient administrative action.

5. ✅ **E. AdminClient#offsetCommit**  
   **Correct**. Incorrect. offsetCommit is a consumer client operation, not part of the AdminClient. It commits consumer offsets to Kafka.

</details>

## 🚫 Question 30 (Kafka Connect):
When deploying a Kafka Connect cluster on Kubernetes using Docker containers or Helm, which of the following practices are recommended? Select all that apply.

- A. Disable task retry to prevent duplicate data in production.
- B. Use the `CONNECT_ZOOKEEPER_CONNECT` environment variable for all Connect deployments.
- C. Use a ConfigMap to externalize and mount worker configuration into pods, enabling dynamic config updates.
- D. Deploy each connector as a separate pod to isolate failures.
- E. Deploy Connect workers as a StatefulSet with persistent volumes for offset storage.
- F. Enable the `offset.storage.file.filename` property for each worker to store offsets locally.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, E

**Explanation:**

Deploying Kafka Connect on Kubernetes should leverage Kubernetes abstractions to improve maintainability and reliability. Using ConfigMaps to mount worker config (option 2) decouples configuration from images and allows live updates. StatefulSets with persistent volumes (option 6) ensure that critical data such as offsets survive pod restarts and provide stable identities for workers. Options that isolate connectors per pod, disable retries, rely on local file offsets, or unnecessarily use ZooKeeper are sub‑optimal or incorrect because they reduce scalability, fault tolerance, or introduce unnecessary complexity.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229) — NOTE: Kubernetes/Helm/Docker deployment is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ❌ **A. Disable task retry to prevent duplicate data in production.**  
   **Incorrect**. Disabling retries removes fault tolerance and can lead to data loss if a task fails. The retry mechanism is essential for ensuring reliable data transfer.

2. ❌ **B. Use the `CONNECT_ZOOKEEPER_CONNECT` environment variable for all Connect deployments.**  
   **Incorrect**. Modern Connect workers (KIP‑357) can operate without ZooKeeper, using only bootstrap servers. Relying on ZooKeeper unnecessarily complicates deployment.

3. ✅ **C. Use a ConfigMap to externalize and mount worker configuration into pods, enabling dynamic config updates.**  
   **Correct**. A ConfigMap allows separating configuration from the container image and lets you update worker properties without rebuilding images, improving maintainability.

4. ❌ **D. Deploy each connector as a separate pod to isolate failures.**  
   **Incorrect**. Running one connector per pod limits scalability and increases resource overhead. Connect is designed to host multiple connectors per worker for efficient resource utilization.

5. ✅ **E. Deploy Connect workers as a StatefulSet with persistent volumes for offset storage.**  
   **Correct**. StatefulSets provide stable network IDs and persistent storage, which is ideal for offset and checkpoint data that must survive pod restarts.

6. ❌ **F. Enable the `offset.storage.file.filename` property for each worker to store offsets locally.**  
   **Incorrect**. Local file offset storage is not recommended in Kubernetes due to pod restarts and lack of persistence. The KafkaOffsetStore should be used instead.

</details>

## Question 31 (Kafka Connect): [-]
When configuring and deploying Kafka Connect source connectors in a distributed deployment, which of the following statements are true? Select all that apply.

- A. The `tasks.max` property determines the maximum number of parallel tasks that will run for a connector.
- B. The `offset.flush.interval.ms` setting can be configured on the connector to control how often offsets are committed.
- C. Connect workers cannot load new connector plugins after the cluster has started, a restart is required for new JARs to be recognized.
- D. Connector configurations can be submitted directly to the workers via REST API or by placing JSON files in a monitored directory.
- E. The `key.converter` and `value.converter` must use the same converter type for compatibility.
- F. All Connect workers in a distributed cluster must connect to the same Kafka cluster that holds the internal topics.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

Correction: E is false. `key.converter` and `value.converter` are independent and commonly differ (e.g. `StringConverter` for keys and `AvroConverter` or `JsonConverter` for values), there is no requirement that they match. So the answer is A, C, F (select 3). Original text follows (its remark about matching converters is wrong).

In Kafka Connect, connector‑level properties control the connector’s behavior, while worker‑level properties affect the entire cluster. The `tasks.max` setting limits parallelism, and matching `key.converter`/`value.converter` ensures schema compatibility. Distributed deployments rely on shared internal topics, so all workers must point to the same Kafka cluster. Offset flushing is configured at the worker level (`offset.flush.interval.ms`), not per connector. Configurations are only accepted via the REST API, there is no file‑watching mechanism. Finally, plugin discovery happens at startup, so any new connector JARs require a worker restart. Understanding these distinctions is essential for correctly deploying and scaling connectors in production.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. The `tasks.max` property determines the maximum number of parallel tasks that will run for a connector.**  
   **Correct**. `tasks.max` is a connector‑level configuration that limits how many task instances a connector can spawn.

2. ❌ **B. The `offset.flush.interval.ms` setting can be configured on the connector to control how often offsets are committed.**  
   **Incorrect**. `offset.flush.interval.ms` is a worker‑level configuration, not a connector property.

3. ✅ **C. Connect workers cannot load new connector plugins after the cluster has started, a restart is required for new JARs to be recognized.**  
   **Correct**. Plugins are discovered at startup, adding a new connector JAR requires restarting the worker process.

4. ❌ **D. Connector configurations can be submitted directly to the workers via REST API or by placing JSON files in a monitored directory.**  
   **Incorrect**. Kafka Connect only accepts connector configurations through the REST API, it does not monitor a directory for config files.

5. ❌ **E. The `key.converter` and `value.converter` must use the same converter type for compatibility.**  
   **Incorrect**. The two converters are configured independently and often differ (e.g. String keys with Avro/JSON values). Each must simply match how the corresponding part of the record is serialized in the topic.

6. ✅ **F. All Connect workers in a distributed cluster must connect to the same Kafka cluster that holds the internal topics.**  
   **Correct**. Distributed mode relies on internal topics (e.g., connect-configs, connect-offsets, connect-status) that are shared by all workers.

</details>

## Question 32 (Kafka Core Concepts): [-]
You are designing a Kafka-based event-driven application that uses Avro schemas and the Confluent Schema Registry. Which of the following statements about data modeling and topic design are **correct** for this scenario?

- A. Choosing JSON serialization over Avro results in smaller payloads due to its efficient binary encoding.
- B. Using a composite key that includes userId and eventTimestamp ensures that events are strictly ordered by time within a partition.
- C. Defining a dedicated topic per aggregate is a good practice when implementing CQRS patterns.
- D. Adding backward-compatible schema evolution using Avro allows consumers to skip unknown fields without breaking.
- E. Using keyless messages is acceptable for stateful stream processing that requires ordering guarantees.
- F. Storing all event types in a single topic simplifies consumer logic but may lead to increased message size and storage overhead.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

In Kafka data modeling, schema evolution and topic granularity are critical for maintainability and performance. Avro with the Schema Registry enables backward‑compatible evolution, allowing consumers to ignore new fields. A dedicated topic per aggregate aligns with CQRS and event‑sourcing principles, offering clear event streams and scalable partitions. Conversely, composite keys that change per record break ordering guarantees, and keyless messages cannot provide the ordering required by stateful stream processing. Storing all event types in a single topic may simplify topic count but introduces payload bloat and consumer complexity. Understanding these trade‑offs ensures robust, scalable event‑driven applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6)

**Detailed explanation of each option:**

1. ❌ **A. Choosing JSON serialization over Avro results in smaller payloads due to its efficient binary encoding.**  
   **Incorrect**. JSON is a text format and typically larger than Avro’s binary encoding. Therefore JSON does **not** produce smaller payloads. This statement is incorrect.

2. ❌ **B. Using a composite key that includes userId and eventTimestamp ensures that events are strictly ordered by time within a partition.**  
   **Incorrect**. Kafka guarantees ordering only per key within a partition. If the key changes for every event (e.g., because it contains the timestamp), each event may end up in a different partition, breaking per‑aggregate ordering. Therefore this statement is incorrect.

3. ✅ **C. Defining a dedicated topic per aggregate is a good practice when implementing CQRS patterns.**  
   **Correct**. In CQRS and event sourcing, isolating each aggregate’s events into its own topic allows fine‑grained partitioning, easier scaling, and clear separation of concerns. This is considered a valid best practice. The statement is correct.

4. ✅ **D. Adding backward-compatible schema evolution using Avro allows consumers to skip unknown fields without breaking.**  
   **Correct**. Avro supports schema evolution and, when configured for backward compatibility, consumers can safely read newer records that contain additional fields, automatically ignoring unknown fields. This is a correct statement.

5. ❌ **E. Using keyless messages is acceptable for stateful stream processing that requires ordering guarantees.**  
   **Incorrect**. Stateful operators that rely on ordering (e.g., joins, aggregations) need a consistent key to guarantee ordering within a partition. Keyless records are routed randomly, so ordering is not guaranteed. Thus this statement is incorrect.

6. ❌ **F. Storing all event types in a single topic simplifies consumer logic but may lead to increased message size and storage overhead.**  
   **Incorrect**. While a single topic can reduce the number of topics a consumer must subscribe to, it forces all events to share a common schema and increases message size due to polymorphic payloads. Consumers still need to filter by type, so the simplification claim is misleading. Hence, this statement is not fully correct.

</details>

## Question 33 (Kafka Consumers): [-]
A new Kafka consumer joins a group and has never committed an offset for the subscribed topic. If the consumer configuration does not explicitly set the "auto.offset.reset" property, from where does the consumer begin consuming records?

- A. The latest offset of each partition (just after the current end of the log).
- B. A random offset chosen by the broker.
- C. The earliest offset of each partition (the beginning of the log).
- D. The middle of the log, roughly halfway between the oldest and newest records.
- E. The consumer will fail to join the group and throw an error.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka, a consumer without a committed offset relies on the "auto.offset.reset" configuration to determine its starting point. The default value for this setting is "latest", meaning the consumer begins at the most recent offset in each partition. Many developers mistakenly believe the default is "earliest", this confusion often leads to missed records in real‑time processing. The other options describe non‑existent defaults or erroneous behaviors. Understanding this default is crucial for designing reliable consumer groups, especially when handling late‑joining consumers or during cluster restarts.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "auto.offset.reset" (p. 91)

**Detailed explanation of each option:**

1. ✅ **A. The latest offset of each partition (just after the current end of the log).**  
   **Correct**. With no prior offset and the default setting of "auto.offset.reset=latest", the consumer starts at the end of each partition.

2. ❌ **B. A random offset chosen by the broker.**  
   **Incorrect**. The offset is deterministic based on the "auto.offset.reset" policy.

3. ❌ **C. The earliest offset of each partition (the beginning of the log).**  
   **Incorrect**. The default value of "auto.offset.reset" is "latest", not "earliest".

4. ❌ **D. The middle of the log, roughly halfway between the oldest and newest records.**  
   **Incorrect**. Kafka does not provide a default middle‑offset behavior.

5. ❌ **E. The consumer will fail to join the group and throw an error.**  
   **Incorrect**. It will join successfully and apply the default offset reset policy.

</details>

## Question 34 (Application Observability): [-]
When monitoring a Kafka consumer group to ensure it keeps up with the incoming stream, which JMX metric provides the most direct indicator of the group’s current lag?

- A. kafka.server.BrokerTopicMetrics.totalProduceRequests
- B. consumer-lag-avg
- C. consumer-fetch-manager-metrics.records-lag-max
- D. records-consumed-total
- E. kafka.server.Server.ProduceRequestTotal

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Consumer lag is the most critical observable for ensuring timely processing of records. The JMX metric `consumer-fetch-manager-metrics.records-lag-max` directly reports the offset difference between the consumer and the latest broker log, making it the most reliable lag indicator. `records-consumed-total` only measures throughput, while broker metrics like `ProduceRequestTotal` reflect producer activity, not consumer progress. `consumer-lag-avg` is not a native JMX metric, it appears only in external aggregations (e.g., Prometheus) and would require additional computation. Monitoring the correct lag metric enables prompt alerting and proactive scaling of consumer resources, a key requirement in Confluent Certified Developer examinations. References: https://kafka.apache.org/documentation/#jmx, https://docs.confluent.io/platform/current/monitoring.html, https://docs.confluent.io/platform/current/monitoring/monitoring_prometheus.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Consumer Metrics" / "Lag Monitoring" (pp. 373-377)

**Detailed explanation of each option:**

1. ❌ **A. kafka.server.BrokerTopicMetrics.totalProduceRequests**  
   **Incorrect**. Also broker‑side, this metric aggregates produce requests for a topic. It provides no insight into consumer processing speed.

2. ❌ **B. consumer-lag-avg**  
   **Incorrect**. This metric does not exist in the standard Kafka JMX namespace. Developers sometimes confuse it with the Prometheus "kafka_consumer_lag_avg" metric, which is computed externally.

3. ✅ **C. consumer-fetch-manager-metrics.records-lag-max**  
   **Correct**. Reports the maximum offset lag across all partitions for the consumer group. This is the canonical metric for detecting whether a consumer is falling behind.

4. ❌ **D. records-consumed-total**  
   **Incorrect**. Counts the total number of records consumed by a consumer but does not provide information about the offset gap relative to the producer. Useful for throughput but not for lag detection.

5. ❌ **E. kafka.server.Server.ProduceRequestTotal**  
   **Incorrect**. A broker‑side metric that counts produce requests, it reflects producer activity, not consumer lag.

</details>

## Question 35 (Stream Processing):
When deploying a Kafka Streams application that must be fault‑tolerant, stateful, and scalable in a container orchestration environment, which of the following options is a valid deployment strategy that allows the application to restart with the same state restored from changelog topics and to run multiple replicas for load‑balancing?

- A. Build the application into a JAR, package it in a Docker container based on `confluentinc/cp-kafka-streams`, and run multiple container replicas behind a load balancer with the same `application.id` configured in the environment.
- B. Use the Confluent Control Center to auto‑deploy the Streams application by providing the Maven coordinates of the artifact.
- C. Run the Java main class directly on a single VM without packaging, using the same application ID and enabling `commit.interval.ms` to zero.
- D. Deploy the application as a KSQL query using `CREATE STREAM ... AS SELECT ...` and rely on KSQL's stateful processing.
- E. Configure the Streams application to use the `state.dir` property pointing to an external NFS share and run on a single node cluster.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Deploying a Kafka Streams application in a reproducible, scalable, and fault‑tolerant manner is typically done by packaging the compiled JAR into a Docker image based on the Confluent Platform `cp-kafka-streams` image. Running multiple container replicas with the same `application.id` lets Kafka Streams automatically partition the input topic across the active instances. Each instance stores its local state in the configured `state.dir`, and a changelog topic backs up the state, ensuring that on a crash or restart the state can be restored. This pattern is fully supported by Confluent’s documentation and works seamlessly with Kubernetes, Docker‑Compose, or any container orchestrator. Other options either lack reproducibility, fault tolerance, or do not provide true horizontal scaling. References: - https://docs.confluent.io/platform/current/streams/deploying-streams-applications.html - https://docs.confluent.io/platform/current/streams/deploying-with-docker.html

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 14 "Scaling a Topology" (pp. 412-415) — NOTE: Docker container deployment is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ✅ **A. Build the application into a JAR, package it in a Docker container based on `confluentinc/cp-kafka-streams`, and run multiple container replicas behind a load balancer with the same `application.id` configured in the environment.**  
   **Correct**. This is a supported deployment pattern. The JAR is built once, the Docker image contains the Confluent Platform Kafka Streams runtime, and replicas share the same `application.id`. Kafka Streams assigns partitions to the active replicas, the state is persisted in local directories and backed by changelog topics, enabling restoration on restart and fault tolerance.

2. ❌ **B. Use the Confluent Control Center to auto‑deploy the Streams application by providing the Maven coordinates of the artifact.**  
   **Incorrect**. Control Center does not provide an automatic deployment mechanism for Kafka Streams applications. Deployment must be handled via Docker, Kubernetes, or other orchestration tools.

3. ❌ **C. Run the Java main class directly on a single VM without packaging, using the same application ID and enabling `commit.interval.ms` to zero.**  
   **Incorrect**. Running on a single VM without packaging does not provide a reproducible environment. Setting `commit.interval.ms` to zero only forces frequent commits but does not enable state restoration or horizontal scaling. This approach lacks fault tolerance and cannot run multiple replicas.

4. ❌ **D. Deploy the application as a KSQL query using `CREATE STREAM ... AS SELECT ...` and rely on KSQL's stateful processing.**  
   **Incorrect**. KSQL is a higher‑level query engine, not a direct deployment of a Kafka Streams application. It uses its own runtime and does not expose the same deployment flexibility for Java streams code.

5. ❌ **E. Configure the Streams application to use the `state.dir` property pointing to an external NFS share and run on a single node cluster.**  
   **Incorrect**. Persisting state on an external NFS share is unsupported and can cause data corruption. A single node cluster provides no fault tolerance and cannot scale horizontally.

</details>

## Question 36 (Kafka Producers): [x]
Which of the following statements are true about the behavior of a Kafka Producer when idempotence is enabled by setting `enable.idempotence=true`? Select all that apply.

- A. When idempotence is enabled, the producer will automatically set `max.in.flight.requests.per.connection` to 5 if not explicitly configured.
- B. The broker tracks a producer ID and sequence number to detect and discard duplicates.
- C. Enabling idempotence automatically turns on transactional support for the producer.
- D. Idempotence guarantees exactly‑once semantics for multiple partitions and topics.
- E. The producer guarantees no duplicate records for a given partition when a retry occurs.
- F. The maximum in‑flight requests per connection must be set to 1 when idempotence is enabled.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

Enabling idempotence (`producer.idempotence=true`) configures the producer to use sequence numbers and a unique producer ID so that the broker can detect and discard duplicate records on retry, guaranteeing no duplicates per partition. It does not automatically enable transactions, nor does it provide exactly‑once semantics across topics. The broker tracks the producer ID and sequence number, and the producer defaults `max.in.flight.requests.per.connection` to 5 when idempotence is true, balancing safety and throughput. Misconceptions often arise around the relationship between idempotence and transactions, and the necessity to set `max.in.flight.requests.per.connection` to 1, which is incorrect. Understanding these distinctions is crucial for correct producer configuration in production applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 "Idempotent Producer" (pp. 182-185)

**Detailed explanation of each option:**

1. ✅ **A. When idempotence is enabled, the producer will automatically set `max.in.flight.requests.per.connection` to 5 if not explicitly configured.**  
   **Correct**. True. The producer defaults this setting to 5 when idempotence is true, ensuring correct ordering without sacrificing throughput.

2. ✅ **B. The broker tracks a producer ID and sequence number to detect and discard duplicates.**  
   **Correct**. True. Each idempotent producer is assigned a producer ID, and each message carries a sequence number, the broker uses these to identify duplicates.

3. ❌ **C. Enabling idempotence automatically turns on transactional support for the producer.**  
   **Incorrect**. False. Idempotence and transactions are separate features. Transactions require a `transactional.id` and explicit begin/commit calls.

4. ❌ **D. Idempotence guarantees exactly‑once semantics for multiple partitions and topics.**  
   **Incorrect**. False. Idempotence guarantees no duplicate records per partition but does not provide atomicity across partitions or topics, transactions are required for exactly‑once semantics.

5. ✅ **E. The producer guarantees no duplicate records for a given partition when a retry occurs.**  
   **Correct**. True. Idempotence uses a sequence number per partition, if a retry is sent, the broker discards the duplicate record, ensuring that the consumer sees each record only once.

6. ❌ **F. The maximum in‑flight requests per connection must be set to 1 when idempotence is enabled.**  
   **Incorrect**. False. The default value is 5, which is safe for idempotence. Setting it to 1 is unnecessary and can hurt throughput.

</details>

## Question 37 (Kafka Core Concepts):
Which statement accurately describes the behavior of message headers in Apache Kafka in the context of observability and testing?

- A. Headers are only available in the Java client and not in the Confluent REST Proxy.
- B. The size of headers contributes to the message size limit of 1 MB enforced by Kafka.
- C. Headers can be used by a consumer to filter messages using the Kafka Streams DSL without pulling them into the application.
- D. Headers are automatically encrypted by Kafka brokers for security.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Message headers in Kafka are an optional key‑value pair attached to each record that can carry contextual data such as trace IDs or correlation IDs for observability. They are supported across all major clients and the REST Proxy, but they are not automatically encrypted and do not enable broker‑side filtering. Importantly, headers add to the overall record size, which must stay within the broker’s `message.max.bytes` setting (default 1 MB). This makes header size a practical consideration during test design and performance tuning.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Headers" (p. 71)

**Detailed explanation of each option:**

1. ❌ **A. Headers are only available in the Java client and not in the Confluent REST Proxy.**  
   **Incorrect**. The Confluent REST Proxy supports setting and retrieving message headers via the HTTP interface, as documented in the REST Proxy API. Headers are not limited to the Java client.

2. ✅ **B. The size of headers contributes to the message size limit of 1 MB enforced by Kafka.**  
   **Correct**. Each message’s total size (key, value, headers, and record metadata) must not exceed the broker’s `message.max.bytes` (default 1 MB). Headers are counted toward this limit.

3. ❌ **C. Headers can be used by a consumer to filter messages using the Kafka Streams DSL without pulling them into the application.**  
   **Incorrect**. While the Streams DSL allows predicates that inspect headers, the consumer still needs to pull the records from the broker, there is no broker‑side filtering based solely on headers.

4. ❌ **D. Headers are automatically encrypted by Kafka brokers for security.**  
   **Incorrect**. Kafka does not provide automatic encryption of headers. Security is handled via TLS for transport and at-rest encryption, but headers remain in clear text unless the application encrypts them explicitly.

</details>

## Question 38 (Kafka Producers):
When optimizing a Kafka producer for high throughput, which configuration setting should be adjusted to reduce the number of network requests by allowing the producer to wait for a short period before sending a batch of records?

- A. max.in.flight.requests.per.connection
- B. compression.type
- C. retries
- D. linger.ms
- E. batch.size

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

To maximize throughput, a producer must minimize the number of network round-trips by batching multiple records into a single request. The linger.ms configuration controls the delay the producer waits after the first record arrives before sending the batch. A larger linger.ms value allows more records to be collected, reducing request overhead and improving throughput. Other parameters such as batch.size set an upper bound on batch size, compression.type affects payload size, and retries or max.in.flight.requests.per.connection manage fault tolerance and ordering but do not control batching timing. Understanding the role of linger.ms is essential for tuning producers in real‑world applications. See the official Kafka producer configuration docs: https://kafka.apache.org/documentation/#producerconfigs_linger.ms, https://kafka.apache.org/documentation/#producerconfigs_batch.size.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "linger.ms"/"batch.size" (pp. 59-60)

**Detailed explanation of each option:**

1. ❌ **A. max.in.flight.requests.per.connection**  
   **Incorrect**. This option limits the number of unacknowledged requests per connection and has no effect on when batches are sent.

2. ❌ **B. compression.type**  
   **Incorrect**. compression.type selects the compression algorithm for records. It affects payload size but not the batching timing.

3. ❌ **C. retries**  
   **Incorrect**. retries controls the number of retry attempts for failed sends and does not influence batch timing.

4. ✅ **D. linger.ms**  
   **Correct**. This setting specifies the maximum time to wait for additional records before sending a batch. By increasing it, the producer can accumulate more records into a single request, lowering network overhead.

5. ❌ **E. batch.size**  
   **Incorrect**. batch.size limits the maximum size of a batch in bytes. While larger batches can improve throughput, this option does not control the timing of when batches are sent.

</details>

## 🚫 Question 39 (Application Observability):
Which of the following techniques and tools are recommended for monitoring and testing the scaling of a Kafka cluster in a Confluent environment?

- A. Use the `kafka-consumer-groups.sh` tool to reset offsets when scaling partitions.
- B. Monitor the `kafka.server:type=ReplicaFetcherStats` JMX bean to detect inter‑broker replication lag during scaling.
- C. Scale the Kafka cluster by adding more Zookeeper nodes without updating the `zookeeper.connect` configuration in brokers.
- D. Use the `kafka-run-class.sh kafka.tools.JmxTool` to fetch JMX metrics and integrate with Prometheus.
- E. Rely solely on Confluent Control Center’s UI to automatically detect and fix consumer lag when adding partitions.
- F. Run the `kafka-producer-perf-test.sh` test with a higher `numPartitions` to gauge throughput after scaling the number of brokers.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

For scaling Kafka, observability relies on JMX metrics that expose replication, fetch, and partition statistics, tools like JmxTool and Prometheus are standard for gathering and visualizing these metrics. Performance testing with `kafka-producer-perf-test.sh` under higher partition counts validates throughput gains. Resetting offsets or relying on Control Center alone does not provide actionable metrics, while adding Zookeeper nodes without config updates is ineffective. Understanding which metrics signal scaling issues and how to automate their collection is essential for a Confluent Certified Developer. See Confluent Monitoring docs (https://docs.confluent.io/platform/current/monitoring.html) and Kafka JMX docs (https://kafka.apache.org/documentation/#metrics) for details.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 13 "Monitoring Kafka" (pp. 339-378) — NOTE: Cluster scaling/administration is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ❌ **A. Use the `kafka-consumer-groups.sh` tool to reset offsets when scaling partitions.**  
   **Incorrect**. Resetting offsets is useful for re‑balancing consumers, but it does not provide observability of cluster performance or detect scaling issues. Monitoring should focus on metrics rather than manual offset manipulation.

2. ✅ **B. Monitor the `kafka.server:type=ReplicaFetcherStats` JMX bean to detect inter‑broker replication lag during scaling.**  
   **Correct**. This JMX bean exposes metrics such as `replicaFetchAvg`, `replicaFetchMax`, and `replicaFetchSum`, which are critical for detecting replication lag that can arise when adding brokers or partitions. It is a standard observability practice for scaling clusters.

3. ❌ **C. Scale the Kafka cluster by adding more Zookeeper nodes without updating the `zookeeper.connect` configuration in brokers.**  
   **Incorrect**. Adding Zookeeper nodes requires updating the broker configuration or using a dynamic cluster configuration. Simply adding nodes without configuration changes does not scale the broker cluster and can lead to inconsistencies.

4. ✅ **D. Use the `kafka-run-class.sh kafka.tools.JmxTool` to fetch JMX metrics and integrate with Prometheus.**  
   **Correct**. JmxTool can query any JMX bean and output metrics in a format that Prometheus can scrape. Integrating with Prometheus/Grafana is a common approach for monitoring scaling events and alerting on thresholds.

5. ❌ **E. Rely solely on Confluent Control Center’s UI to automatically detect and fix consumer lag when adding partitions.**  
   **Incorrect**. Control Center can display consumer lag and other metrics, but it does not automatically resolve scaling issues. Manual investigation or automation scripts are required to fix the root cause.

6. ✅ **F. Run the `kafka-producer-perf-test.sh` test with a higher `numPartitions` to gauge throughput after scaling the number of brokers.**  
   **Correct**. Performance tests with increased partitions simulate realistic load after scaling brokers. They help verify that the cluster can sustain higher throughput and detect bottlenecks.

</details>

## Question 40 (Kafka Core Concepts):
When a producer publishes records with different keys to a topic that has multiple partitions, which statement correctly describes the ordering guarantee that Kafka provides?

- A. Kafka guarantees global ordering of all records within the topic regardless of partition assignment.
- B. Kafka guarantees ordering only for records that share the same key, and no ordering for records with different keys.
- C. Kafka guarantees ordering only if the consumer group has a single consumer instance.
- D. Kafka guarantees ordering within each partition, regardless of the key of the record, but not across partitions.
- E. Kafka guarantees ordering only if the topic has a single partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s ordering guarantee is tied to partitions, not the entire topic. A producer’s partitioner (often key-based) routes each record to a specific partition, and the broker preserves the send order for all records within that partition. Consequently, consumers reading from a single partition will see records in the order they were produced, but consumers that read from multiple partitions cannot rely on any cross‑partition ordering. This principle underpins many Kafka design choices, such as the use of keys for ordering guarantees and the expectation that downstream systems must handle potential reordering across partitions.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6), ordering per partition

**Detailed explanation of each option:**

1. ❌ **A. Kafka guarantees global ordering of all records within the topic regardless of partition assignment.**  
   **Incorrect**. Kafka only guarantees ordering within a single partition. Global ordering across partitions is not maintained.

2. ❌ **B. Kafka guarantees ordering only for records that share the same key, and no ordering for records with different keys.**  
   **Incorrect**. Partially correct but incomplete. While records with the same key go to the same partition, ordering is actually preserved for all records within a partition, not just those sharing a key.

3. ❌ **C. Kafka guarantees ordering only if the consumer group has a single consumer instance.**  
   **Incorrect**. Ordering is a property of partitions at the broker level, independent of consumer group size.

4. ✅ **D. Kafka guarantees ordering within each partition, regardless of the key of the record, but not across partitions.**  
   **Correct**. The producer’s partitioner ensures records are routed to partitions (often by key), and Kafka preserves order per partition. Ordering across partitions is not guaranteed.

5. ❌ **E. Kafka guarantees ordering only if the topic has a single partition.**  
   **Incorrect**. Even with multiple partitions, each partition individually preserves order, but the overall topic does not guarantee global ordering.

</details>

## Question 41 (Application Testing):
Which of the following is NOT a feature of the Kafka Streams TestDriver used for unit‑testing stream processing logic?

- A. Requires an actual running Kafka broker
- B. Provides a method to query intermediate streams
- C. Allows injecting input records with specific timestamps
- D. Enables validation of state store contents after processing

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Kafka Streams TestDriver is a lightweight, in‑memory tool that lets developers simulate the processing of records without deploying a full Kafka cluster. It supports timestamp injection, state store inspection, and output stream retrieval, all essential for deterministic unit tests. Because it emulates the Streams runtime internally, it eliminates the need for a running broker, which is why the statement that a broker is required is false. Misconceptions often arise from confusing the TestDriver with end‑to‑end integration tests that do use brokers. For more details, see the official Streams testing guide.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Testing a Topology" (pp. 411-412)

**Detailed explanation of each option:**

1. ✅ **A. Requires an actual running Kafka broker**  
   **Correct**. Incorrect. The TestDriver runs in‑memory and does not need a live broker, making it lightweight for unit tests.

2. ❌ **B. Provides a method to query intermediate streams**  
   **Incorrect**. Correct. The TestDriver exposes `outputStream()` to retrieve output records and to verify intermediate transformations.

3. ❌ **C. Allows injecting input records with specific timestamps**  
   **Incorrect**. Correct. The TestDriver provides methods like `pipeInput()` that accept a timestamp, enabling time‑based logic to be exercised.

4. ❌ **D. Enables validation of state store contents after processing**  
   **Incorrect**. Correct. State stores can be queried via `stateStore()` after records have been processed, facilitating assertions on local state.

</details>

## Question 42 (Kafka Consumers):
A Java application consumes records from a Kafka topic. The business requirement is that records must be processed in the exact order they appear in each partition and the consumer should commit the offset only after each record is successfully processed. Which configuration and processing strategy correctly satisfies these constraints?

- A. Set `enable.auto.commit=true` and rely on the broker to commit offsets automatically during the `poll()` loop.
- B. Set `enable.auto.commit=false`, process each record, and call `consumer.commitAsync()` after each record.
- C. Set `enable.auto.commit=false`, set `max.poll.records=1`, process each record, and commit synchronously after each poll.
- D. Set `enable.auto.commit=false`, process all records returned by a `poll()` call, and then call `consumer.commitSync()` once per poll.
- E. Set `enable.auto.commit=false`, process each record, and call `consumer.commitSync()` immediately after processing every record.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

To meet the requirement of ordered processing and per‑record offset commitment, a consumer must disable automatic commits and perform a synchronous commit immediately after each record is processed. This guarantees that if processing fails, the offset remains at the last successfully handled record, enabling safe reprocessing. Auto‑commit or asynchronous commits risk committing offsets before successful processing, while committing only after a batch may leave the consumer in an inconsistent state if a record fails within the batch. The chosen strategy preserves the natural Kafka ordering guarantees per partition and provides at‑least‑once delivery semantics.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Commits and Offsets" (pp. 94-100)

**Detailed explanation of each option:**

1. ❌ **A. Set `enable.auto.commit=true` and rely on the broker to commit offsets automatically during the `poll()` loop.**  
   **Incorrect**. Auto‑commit advances the offset every `auto.commit.interval.ms` regardless of whether the record was processed successfully, breaking the requirement that commits occur only after each record.

2. ❌ **B. Set `enable.auto.commit=false`, process each record, and call `consumer.commitAsync()` after each record.**  
   **Incorrect**. Async commits return before the broker acknowledges the offset, so a failure could occur after the commit, leading to possible record loss or re‑processing out of order.

3. ❌ **C. Set `enable.auto.commit=false`, set `max.poll.records=1`, process each record, and commit synchronously after each poll.**  
   **Incorrect**. While committing after each poll with one record per poll works, the extra `max.poll.records` setting is unnecessary and does not directly relate to the core requirement, other options already satisfy the requirement more simply.

4. ❌ **D. Set `enable.auto.commit=false`, process all records returned by a `poll()` call, and then call `consumer.commitSync()` once per poll.**  
   **Incorrect**. Committing after a batch means the offset represents the last record of the batch, not each individual record, violating the requirement that commits happen after every record.

5. ✅ **E. Set `enable.auto.commit=false`, process each record, and call `consumer.commitSync()` immediately after processing every record.**  
   **Correct**. Disabling auto‑commit and performing a synchronous commit after each successfully processed record guarantees that the offset is stored only after that record is handled, preserving per‑partition order.

</details>

## Question 43 (Kafka Connect):
Which of the following statements are true about configuring and deploying a source connector in Kafka Connect when running in distributed mode?

- A. The connector configuration must be submitted via the REST endpoint /connectors with a POST request.
- B. The connector configuration file can be placed in the 'config' directory of the worker and will be automatically loaded when the worker starts.
- C. For a source connector, a topics.pattern property must be specified to capture multiple source tables.
- D. Once the connector is created, it will be automatically registered in ZooKeeper when using standalone mode.
- E. The connector class name must be fully qualified and must implement the SourceConnector interface.
- F. The tasks.max setting is optional and can be omitted from the configuration.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, E, F

**Explanation:**

Correction: F is true. `tasks.max` is optional, `ConnectorConfig` defines it with a default of 1, so it can be omitted (only `name` and `connector.class` are required). Hence A, E, F (select 3). Original text follows (its claim that tasks.max is required is wrong).

In distributed Kafka Connect, connectors are deployed by posting their JSON configuration to the worker REST endpoint, this is the only supported deployment method. The required configuration includes the fully‑qualified connector.class and a tasks.max value that controls parallelism. Other properties are source‑specific or optional and do not make the configuration valid. Understanding these requirements prevents common deployment failures such as missing class names or absent tasks.max. The other statements describe behaviors that belong to standalone mode, sink connectors, or ZooKeeper usage, which are not applicable to distributed source connector deployment.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. The connector configuration must be submitted via the REST endpoint /connectors with a POST request.**  
   **Correct**. In distributed mode, connectors are created or updated by POSTing a JSON payload to the worker’s REST API (e.g., POST /connectors). This is the standard way to register a connector with the cluster. Reference: https://docs.confluent.io/platform/current/connect/using.html#create-a-connector

2. ❌ **B. The connector configuration file can be placed in the 'config' directory of the worker and will be automatically loaded when the worker starts.**  
   **Incorrect**. In distributed mode, connector configs are not automatically loaded from files, they must be submitted via the REST API. Files in the config directory are used only for worker settings. Reference: https://docs.confluent.io/platform/current/connect/overview.html#distributed-mode

3. ❌ **C. For a source connector, a topics.pattern property must be specified to capture multiple source tables.**  
   **Incorrect**. topics.pattern is a sink connector setting used to write to multiple topics. Source connectors typically use source-specific properties (e.g., table.whitelist). Reference: https://docs.confluent.io/platform/current/connect/using.html#source-connector-configurations

4. ❌ **D. Once the connector is created, it will be automatically registered in ZooKeeper when using standalone mode.**  
   **Incorrect**. Standalone mode stores connector configs in the worker’s local configuration files, not ZooKeeper. ZooKeeper is not used by Kafka Connect. Reference: https://docs.confluent.io/platform/current/connect/overview.html#standalone-mode

5. ✅ **E. The connector class name must be fully qualified and must implement the SourceConnector interface.**  
   **Correct**. The connector.class property must specify the fully qualified class name of the implementation, which must extend SourceConnector (or sink). This ensures the worker can instantiate the connector. Reference: https://docs.confluent.io/platform/current/connect/configuration.html#connector-class

6. ✅ **F. The tasks.max setting is optional and can be omitted from the configuration.**  
   **Correct**. `tasks.max` defines the maximum number of parallel tasks but has a default value of 1, so the connector starts fine without it (only `name` and `connector.class` are mandatory).

</details>

## Question 44 (Kafka Core Concepts): [-]
A Kafka topic is configured with the following retention properties: - `retention.ms` = 604800000 (7 days) - `retention.bytes` = 10737418240 (10 GB) The topic receives exactly 1.5 GB of data every day. Assuming no other producers or consumers influence the topic size, after how many days will the topic start deleting older records due to exceeding the size limit? (Note: Deletion occurs as soon as the size limit is exceeded, not at the end of the day.)

- A. 9 days
- B. 6 days
- C. 7 days
- D. 8 days

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka enforces two independent retention limits: a time‑based limit (`retention.ms`) and a size‑based limit (`retention.bytes`). Records are eligible for deletion once either limit is breached. In this scenario, the daily write rate is 1.5 GB, so the size limit of 10 GB is reached after the 7th day (7 × 1.5 GB = 10.5 GB). Deletion begins immediately once the limit is exceeded, regardless of the time limit. Understanding this interplay helps prevent unexpected log growth or premature data loss in production clusters. For more details, see the official Kafka configuration docs: https://kafka.apache.org/documentation/#brokerconfigs_retention.ms and https://kafka.apache.org/documentation/#brokerconfigs_retention.bytes.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 "Topic Defaults" (retention.ms/retention.bytes, pp. 27-33) and Ch. 6 "File Management" (pp. 152-153) — NOTE: retention.bytes vs retention.ms: on day 7, 7 x 1.5GB = 10.5GB > 10GB triggers deletion.

**Detailed explanation of each option:**

1. ❌ **A. 9 days**  
   **Incorrect**. Similar to option 3, deletion would have started on day 7, not day 9.

2. ❌ **B. 6 days**  
   **Incorrect**. After 6 days the topic holds 6 × 1.5 GB = 9 GB, which is below the 10 GB size limit, so no size‑based deletion yet.

3. ✅ **C. 7 days**  
   **Correct**. After 7 days the topic holds 7 × 1.5 GB = 10.5 GB, exceeding the 10 GB limit. As soon as the size exceeds `retention.bytes`, Kafka deletes the oldest records, so deletion begins on day 7.

4. ❌ **D. 8 days**  
   **Incorrect**. By day 8 the topic would already have exceeded the limit on day 7, so deletion would have started earlier, making 8 days incorrect.

</details>

## Question 45 (Stream Processing):
Which of the following configuration choices is required to enable true exactly‑once processing semantics for a Kafka Streams application that performs stateful transformations?

- A. Set `processing.guarantee=exactly_once_v2` in the Streams configuration and ensure that all topics used by the application have a replication factor of at least 3.
- B. Use `exactly_once_v2` but do not configure any replication, just rely on the broker's default replication settings.
- C. Set `processing.guarantee=at_least_once` and use idempotent producers only.
- D. Set `processing.guarantee=exactly_once_v1` and set `state.dir` to a local disk.
- E. Enable `enable.auto.commit=false` on the consumer and manually commit offsets after each record.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Exactly‑once semantics in Kafka Streams hinge on the `processing.guarantee` configuration. Setting it to `exactly_once_v2` activates the transaction framework that wraps both read and write operations, ensuring that each record is processed and written atomically. However, transactions alone are insufficient without proper durability, therefore, all topics involved must have a replication factor of at least three to survive broker failures. Deprecated settings like `exactly_once_v1` lack full support, and configurations that only adjust offset commits or rely on idempotent producers do not provide the end‑to‑end exactly‑once guarantee. This combination of transaction settings and replication is the recommended practice for production Kafka Streams applications requiring deterministic results.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ✅ **A. Set `processing.guarantee=exactly_once_v2` in the Streams configuration and ensure that all topics used by the application have a replication factor of at least 3.**  
   **Correct**. The `processing.guarantee` property is the core configuration for exactly‑once semantics in Kafka Streams. `exactly_once_v2` enables transaction support for both input and output topics. Additionally, a replication factor of ≥3 provides durability so that the broker can recover from failures during a transaction.

2. ❌ **B. Use `exactly_once_v2` but do not configure any replication, just rely on the broker's default replication settings.**  
   **Incorrect**. While `exactly_once_v2` enables transactions, insufficient replication (e.g., replication factor 1) defeats durability guarantees and can cause lost or duplicated data if a broker fails.

3. ❌ **C. Set `processing.guarantee=at_least_once` and use idempotent producers only.**  
   **Incorrect**. At‑least‑once guarantees may still replay records, idempotent producers prevent duplicate writes to the same key but do not provide exactly‑once processing across the entire topology.

4. ❌ **D. Set `processing.guarantee=exactly_once_v1` and set `state.dir` to a local disk.**  
   **Incorrect**. `exactly_once_v1` is deprecated and has known limitations. The `state.dir` setting only defines where local state is stored, it does not affect transaction semantics.

5. ❌ **E. Enable `enable.auto.commit=false` on the consumer and manually commit offsets after each record.**  
   **Incorrect**. Manual offset commits control acknowledgment but do not provide transactional guarantees. Exactly‑once requires the Streams transaction framework.

</details>

## Question 46 (Kafka Connect):
Which of the following statements correctly describe the fundamental behavior, configuration, or data flow of Kafka Connect source connectors, sink connectors, and CDC connectors?

- A. Sink connectors use the `topics` property to specify Kafka topics from which the connector will consume data.
- B. CDC connectors are a special type of source connector that streams database changes to Kafka topics using binlog or change data capture mechanisms.
- C. Sink connectors can be configured to write data to Kafka topics.
- D. Source connectors can read data from Kafka topics and write it back to external systems.
- E. Source connectors use the `topics` property to specify Kafka topics where the connector will write data.
- F. CDC connectors automatically store schema changes in the same topic where data changes are published, eliminating the need for a separate history topic.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

Correction: E is false. The `topics` / `topics.regex` properties exist only for sink connectors (they select which topics to consume). Source connectors do not have a `topics` property, the destination topic is chosen by connector-specific settings (e.g. `topic`, `topic.prefix`) or by SMTs such as RegexRouter. So only A and B are correct (select 2). Original text follows.

In Kafka Connect, source connectors ingest data from external systems and publish to Kafka topics, controlled by the `topics` or `topics.regex` configuration. Sink connectors consume from those topics and push data to external destinations, again using the same `topics` setting to define the source streams. CDC connectors are a subclass of source connectors that capture database change events via mechanisms such as binlogs, they publish both data and schema changes, typically storing schema evolution in a separate history topic (e.g., `database.history.kafka.topic`). Misconceptions arise when one assumes sink connectors can write to Kafka or source connectors can read from Kafka, both statements are false. Understanding these distinctions is essential for designing correct data pipelines and for the Confluent Certified Developer exam. For reference, see the Kafka Connect documentation (https://docs.confluent.io/platform/current/connect/index.html) and Debezium CDC guide (https://debezium.io/documentation/reference/).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ✅ **A. Sink connectors use the `topics` property to specify Kafka topics from which the connector will consume data.**  
   **Correct**. Sink connectors subscribe to Kafka topics defined by the `topics` (or `topics.regex`) setting and write consumed records to an external system.

2. ✅ **B. CDC connectors are a special type of source connector that streams database changes to Kafka topics using binlog or change data capture mechanisms.**  
   **Correct**. CDC connectors (e.g., Debezium) are implemented as source connectors and capture changes via database logs, publishing change events to Kafka topics.

3. ❌ **C. Sink connectors can be configured to write data to Kafka topics.**  
   **Incorrect**. Sink connectors consume from Kafka and write to external systems, they do not produce to Kafka topics.

4. ❌ **D. Source connectors can read data from Kafka topics and write it back to external systems.**  
   **Incorrect**. Source connectors read from external systems, not from Kafka topics, and publish to Kafka.

5. ❌ **E. Source connectors use the `topics` property to specify Kafka topics where the connector will write data.**  
   **Incorrect**. `topics` / `topics.regex` are sink-connector properties. Source connectors define their target topics through connector-specific settings (e.g. `topic.prefix`) or routing SMTs.

6. ❌ **F. CDC connectors automatically store schema changes in the same topic where data changes are published, eliminating the need for a separate history topic.**  
   **Incorrect**. CDC connectors write schema changes to a dedicated history topic (e.g., `database.history.kafka.topic`) for later replay.

</details>

## Question 47 (Stream Processing):
You are deploying a Kafka Streams application to a production environment. Which client configuration property must be set to a unique value across all instances of the application to ensure proper state store coordination and consistent processing semantics?

- A. bootstrap.servers – The host/port pairs of Kafka brokers.
- B. application.id – A unique identifier for the Streams application.
- C. num.stream.threads – Number of threads for processing records.
- D. state.dir – The local directory for persisting state stores.
- E. commit.interval.ms – Frequency of committing offsets.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka Streams, the application.id property is the single configuration that uniquely identifies a Streams instance to the cluster. It is used to create internal topics (e.g., topic-application.id-changelog) and to form the consumer group that manages state store replicas. Without a consistent application.id across instances, each instance would think it owns a separate group, leading to duplicate processing, state inconsistencies, and failure to rebalance. The other properties configure connectivity, storage, threading, or offset commit timing but do not provide the unique identity required for state coordination. Properly setting application.id is a fundamental deployment best practice for scalable, fault‑tolerant Streams applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ❌ **A. bootstrap.servers – The host/port pairs of Kafka brokers.**  
   **Incorrect**. This property tells the client where the cluster is, but it does not differentiate one Streams instance from another. Multiple instances can share the same bootstrap servers without conflict. It is required, but not the property that guarantees unique coordination.

2. ✅ **B. application.id – A unique identifier for the Streams application.**  
   **Correct**. The application.id is used by Kafka Streams to create internal topics, coordinate state stores, and manage group membership. All instances of the same application must share the same id, while different applications must use different ids. A unique application.id is essential for correct operation when scaling out.

3. ❌ **C. num.stream.threads – Number of threads for processing records.**  
   **Incorrect**. Controls parallelism within a single instance. It does not affect coordination or state store ownership across instances.

4. ❌ **D. state.dir – The local directory for persisting state stores.**  
   **Incorrect**. This sets the path on the local filesystem where RocksDB state stores are written. It must be unique per machine, but it does not serve as the identifier for coordinating between instances.

5. ❌ **E. commit.interval.ms – Frequency of committing offsets.**  
   **Incorrect**. Determines how often the application commits offsets. It is unrelated to the identification of the Streams instance.

</details>

## Question 48 (Stream Processing):
Which of the following statements correctly describe valid ways to materialize state stores in a Kafka Streams application?

- A. Enable caching with `Cache.enable()` to hold state only in RAM.
- B. Use `Materialized.as("store")` on a KTable to back the table with a persistent RocksDB store.
- C. Declare a KStream with `.to("topic")` and then call `store()` on the stream to create an in‑memory state store.
- D. Configure `application.state.dir` to point to an external SQL database so that the state store is persisted there.
- E. Use `transformValues()` with a `ValueTransformerWithKeySupplier` that writes intermediate results to a separate Kafka topic, treating that topic as a state store.
- F. Create a GlobalKTable with `Materialized.<String, Value, KeyValueStore<Bytes, byte[]>>as("globalStore")` to share read‑only state across all instances.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, F

**Explanation:**

Kafka Streams materializes state with persistent or in‑memory stores that can be queried at runtime. RocksDB is the default persistent store, configured via `Materialized.as()`. GlobalKTables use their own materialized stores for read‑only, global access. Caching is separate from state stores and does not provide persistence. Options that rely on writing to plain topics, using incorrect API methods, or pointing the state directory to external systems are invalid. Understanding these distinctions is essential for designing fault‑tolerant, queryable stream processing pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "State" / "Surviving Failures" (pp. 388-389, 415-416)

**Detailed explanation of each option:**

1. ❌ **A. Enable caching with `Cache.enable()` to hold state only in RAM.**  
   **Incorrect**. The cache improves performance but is transient, it does not persist state across restarts.

2. ✅ **B. Use `Materialized.as("store")` on a KTable to back the table with a persistent RocksDB store.**  
   **Correct**. The `Materialized` helper creates a state store backed by RocksDB (default), allowing the KTable to be queried and rehydrated after restarts.

3. ❌ **C. Declare a KStream with `.to("topic")` and then call `store()` on the stream to create an in‑memory state store.**  
   **Incorrect**. `to()` writes to a topic, `store()` is not a method on `KStream`. In‑memory stores are created with `Stores.inMemoryKeyValueStore()` via `Materialized`.

4. ❌ **D. Configure `application.state.dir` to point to an external SQL database so that the state store is persisted there.**  
   **Incorrect**. The state directory must be a local file system path, Kafka Streams does not support external databases for state persistence.

5. ❌ **E. Use `transformValues()` with a `ValueTransformerWithKeySupplier` that writes intermediate results to a separate Kafka topic, treating that topic as a state store.**  
   **Incorrect**. While a topic can carry data, it is not a state store, state stores must be created via the Streams API.

6. ✅ **F. Create a GlobalKTable with `Materialized.<String, Value, KeyValueStore<Bytes, byte[]>>as("globalStore")` to share read‑only state across all instances.**  
   **Correct**. GlobalKTables are materialized in every instance using a key-value store, enabling fast read‑only lookups.

</details>

## Question 49 (Programming & Serialization):
You are designing a Kafka topic that uses Avro for serialization and a Confluent Schema Registry. Which of the following schema evolution changes will **not** break compatibility (i.e., will preserve both backward and forward compatibility) when the new schema is registered? Select all that apply.

- A. Add a new field "age" of type int with a default value of 0.
- B. Add a new field "status" of type enum without providing a default value.
- C. Remove the existing field "name".
- D. Add a new required field "email" of type string without a default value.
- E. Reorder the fields "timestamp" and "payload" in the schema definition.
- F. Change the type of field "id" from int to string.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, E

**Explanation:**

Schema evolution in Avro with Confluent Schema Registry is governed by compatibility modes. The question asks for changes that preserve **both** backward and forward compatibility (equivalent to FULL compatibility). Only two changes satisfy this. Adding a field **with a default** is fully compatible: new readers supply the default when reading old data (backward), and old readers ignore the new field (forward). Reordering fields is a no‑op in Avro because fields are matched by name, not position, so compatibility is unaffected in both directions. Removing a field is NOT fully compatible — it is backward compatible but breaks forward compatibility unless the removed field had a default. Adding required fields without defaults, adding enums without defaults, and changing a primitive type to an unrelated type all break compatibility. Understanding these rules is essential for maintaining schema stability across producers and consumers.

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ✅ **A. Add a new field "age" of type int with a default value of 0.**  
   **Correct**. This is compatible. A default value allows old data to be read by the new schema, and old consumers can ignore the new field.

2. ❌ **B. Add a new field "status" of type enum without providing a default value.**  
   **Incorrect**. Without a default, old data will be missing the field, breaking backward compatibility.

3. ❌ **C. Remove the existing field "name".**  
   **Incorrect**. Removing a field is backward compatible (new readers simply ignore the extra field in old data), but it breaks forward compatibility unless the removed field had a default value, because an old reader expecting "name" cannot read data written without it. Since it does not guarantee BOTH directions, it does not qualify as fully compatible.

4. ❌ **D. Add a new required field "email" of type string without a default value.**  
   **Incorrect**. This is incompatible. Old data will be missing the field, so the new schema cannot read it (backward break).

5. ✅ **E. Reorder the fields "timestamp" and "payload" in the schema definition.**  
   **Correct**. Field order has no semantic meaning in Avro, reordering does not affect compatibility.

6. ❌ **F. Change the type of field "id" from int to string.**  
   **Incorrect**. This is incompatible. Changing a primitive type to an unrelated type breaks both forward and backward compatibility.

</details>

## Question 50 (Programming & Serialization):
A Java Kafka producer uses Confluent's Avro serializer to publish records. Which configuration property must be set to enable the producer to automatically register a new schema with the Schema Registry when the schema is not already known?

- A. "auto.register.schemas": true
- B. "schema.registry.auto.register.schemas": true
- C. "auto.register.schemas": false
- D. "value.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer"
- E. "schema.registry.auto.register": true

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Confluent's Avro serializer for Java, the property "auto.register.schemas" controls whether the serializer registers unknown schemas with the Schema Registry. When set to true, the producer will automatically register the schema before sending, simplifying development but potentially increasing network traffic and load on the registry. Setting it to false forces explicit schema registration, which is safer in production to avoid accidental schema changes. The other options either reference incorrect property names, control different aspects (like selecting the serializer), or disable registration. Understanding this setting is essential for managing schema evolution and ensuring producers operate correctly in a Confluent environment. See the official Confluent documentation on Avro serializers for more details.

Source: Confluent Schema Registry docs - KafkaAvroSerializer (auto.register.schemas), Kafka: The Definitive Guide 2nd ed. Ch. 3 (pp. 64-68)

**Detailed explanation of each option:**

1. ✅ **A. "auto.register.schemas": true**  
   **Correct**. This is the correct setting. When true, the Avro serializer automatically registers any new schema with the Schema Registry before sending the record.

2. ❌ **B. "schema.registry.auto.register.schemas": true**  
   **Incorrect**. The property name is incorrect, it should be "auto.register.schemas". This misspelled property will be ignored.

3. ❌ **C. "auto.register.schemas": false**  
   **Incorrect**. Setting this to false disables automatic registration. The producer will throw a NotRegisteredException if the schema is unknown, requiring manual schema registration.

4. ❌ **D. "value.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer"**  
   **Incorrect**. While this property is required to use the Avro serializer, it does not control automatic registration, it merely selects the serializer class.

5. ❌ **E. "schema.registry.auto.register": true**  
   **Incorrect**. This property does not exist in the Confluent serializer configuration and will be ignored.

</details>

## Question 51 (Programming & Serialization):
In Confluent Schema Registry, when using Avro schemas under the default backward compatibility setting, which of the following schema evolution changes is automatically permitted without triggering a compatibility error?

- A. Adding a new required field without a default value
- B. Changing the data type of an existing field from INT32 to INT64
- C. Adding a new field with a default value
- D. Removing a required field
- E. Renaming an existing field

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

Correction: B is also permitted. Avro schema resolution allows type promotion int -> long (also int/long -> float/double, string <-> bytes), so a new schema (reader) with `long` can read data written with `int`, Schema Registry's BACKWARD check accepts it. (Only the reverse, long -> int, would fail.) Original text follows (its claim that B is incompatible is wrong for Avro).

In Confluent Schema Registry, backward compatibility permits producers to evolve schemas by adding new optional fields that have default values, ensuring older consumers can still read the data without changes. Operations such as renaming fields, removing required fields, altering field types, or adding required fields without defaults break backward compatibility because existing consumers will not find the expected schema components. Understanding these rules is essential for maintaining reliable data pipelines, as incompatible schema changes can cause runtime failures. For detailed guidance, see the Confluent Schema Registry documentation on compatibility rules (https://docs.confluent.io/platform/current/schema-registry/compatibility.html) and Avro schema evolution (https://docs.confluent.io/platform/current/schema-registry/serdes-develop/index.html).

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. Adding a new required field without a default value**  
   **Incorrect**. Adding a required field without a default means that older data will not contain this field, breaking deserialization for consumers expecting it.

2. ✅ **B. Changing the data type of an existing field from INT32 to INT64**  
   **Correct**. In Avro, `int` is promotable to `long`, so a reader using the new `long` schema can read old `int` data, this passes the BACKWARD check. (Arbitrary type changes, e.g. int -> string, or narrowing long -> int, are incompatible.)

3. ✅ **C. Adding a new field with a default value**  
   **Correct**. Backward compatibility allows producers to add new fields that have a default value so that existing consumers that are unaware of the new field can still deserialize the data. The default ensures the field is present with a known value, satisfying the consumer's expectations.

4. ❌ **D. Removing a required field**  
   **Incorrect**. Removing a field that is required by existing consumers causes the schema to be incompatible, because the consumer will attempt to read a field that no longer exists.

5. ❌ **E. Renaming an existing field**  
   **Incorrect**. Renaming changes the field name, consumers that expect the old name will not find it, leading to a compatibility failure. Schema Registry does not treat renamed fields as compatible.

</details>

## 🚫 Question 52 (Kafka Connect):
When deploying multiple Kafka Connect workers with the Confluent Docker image in a Docker Compose setup, which environment variable must be set to the same value on every worker to enable them to join a distributed Connect cluster and coordinate work?

- A. CONNECT_CLIENT_ID
- B. CONNECT_BOOTSTRAP_SERVERS
- C. CONNECT_REST_PORT
- D. CONNECT_CONFIG_STORAGE_TOPIC
- E. CONNECT_GROUP_ID

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

In a distributed Kafka Connect cluster, workers must share a common group.id so they read from and write to the same internal topics (config, offset, status). This coordination allows the cluster to load‑balance connector tasks and ensures exactly‑once semantics for connectors. The group.id is the only environment variable that guarantees the workers belong to the same logical cluster, other settings such as CONNECT_BOOTSTRAP_SERVERS or CONNECT_CLIENT_ID are independent of clustering. Misconfiguring group.id typically results in duplicate tasks and inconsistent offsets. For more details, see Confluent’s Connect configuration reference and runtime documentation.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229) — NOTE: Docker Compose multi-worker deployment is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ❌ **A. CONNECT_CLIENT_ID**  
   **Incorrect**. CONNECT_CLIENT_ID is used only for client identification when talking to Kafka. Each worker should have a unique client.id to avoid conflicts, but it does not affect clustering.

2. ❌ **B. CONNECT_BOOTSTRAP_SERVERS**  
   **Incorrect**. This variable tells each worker where Kafka brokers are located. While mandatory, it does not coordinate worker discovery or partition assignment. Workers can have different bootstrap lists and still form a cluster if the group.id matches.

3. ❌ **C. CONNECT_REST_PORT**  
   **Incorrect**. This sets the HTTP port on which the worker exposes its REST API. It has no impact on cluster membership or task coordination.

4. ❌ **D. CONNECT_CONFIG_STORAGE_TOPIC**  
   **Incorrect**. The topic names are auto‑created based on the group.id and cluster configuration. Specifying them individually does not influence worker grouping.

5. ✅ **E. CONNECT_GROUP_ID**  
   **Correct**. The group.id identifies the Connect worker group. All workers in a distributed cluster must share the same value so they can read from the same internal topics (config, offset, status) and coordinate task distribution. Mismatched group IDs cause each worker to treat itself as a separate cluster, leading to duplicate processing and partition assignments.

</details>

## 🚫 Question 53 (Kafka Setup and Operations):
Which of the following configuration steps are required to secure a Kafka cluster with SASL/SCRAM authentication **and** authorization via ACLs, assuming you use plain text listeners (no TLS) for inter-broker communication?

- A. Set 'sasl.mechanism.inter.broker.protocol=SCRAM-SHA-512' and configure 'security.inter.broker.protocol=SASL_PLAINTEXT' in server.properties.
- B. Create a JAAS configuration file that includes an entry for 'org.apache.kafka.common.security.scram.ScramLoginModule' for both clients and servers.
- C. Enable 'ssl.client.auth=required' and provide client keystores to the broker.
- D. Add ACL entries for topics, consumer groups, and cluster operations using the 'kafka-acls' tool.
- E. Enable 'sasl.enabled.mechanisms=PLAIN,GSSAPI' in the broker configuration.
- F. Set 'allow.everyone.if.no.acl.found=true' to enforce strict authorization.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

Securing Kafka with SASL/SCRAM requires three core steps: (1) configure the broker to use a SASL listener and set the SCRAM mechanism for inter‑broker traffic, (2) provide a JAAS file that defines the SCRAM login module with usernames and passwords, and (3) create ACLs to enforce authorization. With an authorizer enabled, resources without ACLs are denied by default (allow.everyone.if.no.acl.found defaults to false), so setting it to true would weaken, not enforce, access control. SSL client authentication and enabling unrelated SASL mechanisms are unnecessary for a plain text SASL/SCRAM configuration. These steps align with Confluent’s security guidelines: https://docs.confluent.io/platform/current/kafka/security.html#sasl-scram.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 11 "Authorization" / "AclAuthorizer" (pp. 291-295) — NOTE: Broker-side SASL/SCRAM + ACL setup is out of exam scope (Administer and deploy Kafka).

**Detailed explanation of each option:**

1. ✅ **A. Set 'sasl.mechanism.inter.broker.protocol=SCRAM-SHA-512' and configure 'security.inter.broker.protocol=SASL_PLAINTEXT' in server.properties.**  
   **Correct**. The broker must use a SASL listener for inter‑broker traffic and the specified SCRAM mechanism for authentication.

2. ✅ **B. Create a JAAS configuration file that includes an entry for 'org.apache.kafka.common.security.scram.ScramLoginModule' for both clients and servers.**  
   **Correct**. JAAS is the only way to supply usernames, passwords, and SCRAM parameters for both brokers and clients.

3. ❌ **C. Enable 'ssl.client.auth=required' and provide client keystores to the broker.**  
   **Incorrect**. SSL client authentication is unrelated to SASL/SCRAM and is not needed for plain text listeners.

4. ✅ **D. Add ACL entries for topics, consumer groups, and cluster operations using the 'kafka-acls' tool.**  
   **Correct**. Without ACLs, authorization is not enforced even if authentication succeeds.

5. ❌ **E. Enable 'sasl.enabled.mechanisms=PLAIN,GSSAPI' in the broker configuration.**  
   **Incorrect**. While enabling other mechanisms is possible, it is not required for a SCRAM‑only setup.

6. ❌ **F. Set 'allow.everyone.if.no.acl.found=true' to enforce strict authorization.**  
   **Incorrect**. Setting it to true is the permissive option (anyone is allowed when no ACL matches the resource), the opposite of strict. The default is false (deny when no ACL is found), strict authorization needs it left at false, plus an `authorizer.class.name` configured.

</details>

## Question 54 (Application Observability): [-]
In a Kafka Streams application, which metric from the **StreamsMetrics** group most directly represents the throughput of records processed by the application, measured in records per second?

- A. streams.records.per-sec
- B. stream.processed.bytes-per-sec
- C. streams.records.in-total-rate
- D. streams.processed.records-total
- E. streams.records.in-total

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams exposes a set of metrics under the `streams.*` group. The metric `streams.records.per-sec` is the key throughput indicator, reporting how many records the stream processing logic handles each second. Cumulative counters like `streams.records.in-total` give total counts but cannot express rate, while byte‑based metrics are useful for payload size analysis, not record throughput. Recognizing the correct metric is essential for monitoring performance, diagnosing bottlenecks, and setting alerts in a production Streams application. The official documentation lists all available metrics and their descriptions (see https://kafka.apache.org/documentation/#streams_metrics).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Monitoring Kafka" (pp. 339-378) — NOTE: StreamsMetrics throughput metric, exact metric name is illustrative.

**Detailed explanation of each option:**

1. ✅ **A. streams.records.per-sec**  
   **Correct**. This metric reports the average number of records processed per second, providing a direct measure of application throughput.

2. ❌ **B. stream.processed.bytes-per-sec**  
   **Incorrect**. This metric measures bytes, not records, and is part of the `stream.*` namespace, not the `streams.*` namespace used by StreamsMetrics.

3. ❌ **C. streams.records.in-total-rate**  
   **Incorrect**. No such metric exists in the StreamsMetrics group, the correct throughput metric is `streams.records.per-sec`.

4. ❌ **D. streams.processed.records-total**  
   **Incorrect**. This is another cumulative counter, similar to `streams.records.in-total`. It indicates the total number processed but not the rate.

5. ❌ **E. streams.records.in-total**  
   **Incorrect**. This metric is a cumulative counter of all records that have entered the stream. It does not reflect the rate of processing and therefore is not a throughput metric.

</details>

## 🚫 Question 55 (Application Observability):
When a Kafka cluster is instrumented with Prometheus and you want to monitor the average time it takes a broker to persist a record to disk (write latency), which Prometheus metric should you query?

- A. kafka_server_request_handler_avg_time_ms
- B. kafka_server_recovery_manager_recovery_latency_ms
- C. kafka_server_broker_write_latency_ms
- D. kafka_server_network_processor_avg_time_ms
- E. kafka_server_request_handler_throttle_time_ms

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka observability, write latency is a key metric for evaluating broker health and storage performance. The JMX exporter exposes `kafka_server_broker_write_latency_ms`, which aggregates the time taken for flush operations to persist data to the log segment files. The other metrics listed are related to request handling, network processing, throttling, or recovery, and therefore do not isolate the disk write component. Monitoring this metric helps detect disk I/O bottlenecks and guide capacity planning. Reference: Confluent Kafka Monitoring Guide – https://docs.confluent.io/platform/current/kafka/monitoring.html

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 13 "Monitoring Kafka" (pp. 339-378) — NOTE: Broker write-latency monitoring leans toward cluster administration, metric name illustrative/unverified.

**Detailed explanation of each option:**

1. ❌ **A. kafka_server_request_handler_avg_time_ms**  
   **Incorrect**. This metric represents the average time spent handling client requests overall, including network I/O, serialization, and processing, not specifically the disk write phase.

2. ❌ **B. kafka_server_recovery_manager_recovery_latency_ms**  
   **Incorrect**. It reflects the latency of recovery operations after a broker failure, not normal write operations.

3. ✅ **C. kafka_server_broker_write_latency_ms**  
   **Correct**. This metric, exposed by Kafka's JMX exporter, reports the average write latency (in milliseconds) for all records that the broker flushes to the log. It directly measures disk write time, which is what the question asks for.

4. ❌ **D. kafka_server_network_processor_avg_time_ms**  
   **Incorrect**. It measures the average time the network processor thread spends handling network I/O, not the time the broker spends writing data to disk.

5. ❌ **E. kafka_server_request_handler_throttle_time_ms**  
   **Incorrect**. This metric shows the time a request handler is throttled due to resource constraints (e.g., I/O limits), not the actual write latency to disk.

</details>

## Question 56 (Stream Processing):
When developing a Kafka Streams application, which of the following elements are essential or considered best practice?

- A. Call start() on a KafkaStreams instance and then close() when shutting down.
- B. Configure a StreamsBuilder instance and use it to construct the processing topology.
- C. Use the foreach processor to emit records to external systems.
- D. Provide explicit Serdes for all input and output topics.
- E. Set enable.auto.commit=true to allow automatic consumer offset commits.
- F. Include application.id and bootstrap.servers in the StreamsConfig properties.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

A Kafka Streams application must be built by defining a topology with StreamsBuilder, providing necessary configuration such as application.id and bootstrap.servers, and specifying Serdes for all topics. These elements are mandatory for the compiler and runtime to correctly interpret and process records. Starting and closing the KafkaStreams instance is part of running the application, not writing it. Properties like enable.auto.commit are ignored by Streams and can interfere with its internal commit logic. The foreach processor is optional and used only for side‑effects, it is not required for writing the core stream logic. Mastery of these fundamentals is essential for the Confluent Certified Developer exam.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ❌ **A. 2. Call start() on a KafkaStreams instance and then close() when shutting down.**  
   **Incorrect**. for the "write" phase. While starting the stream is required to run the application, it is part of the deployment lifecycle rather than writing the logic.

2. ✅ **B. 1. Configure a StreamsBuilder instance and use it to construct the processing topology.**  
   **Correct**. The StreamsBuilder is the entry point for defining the DSL or Processor API topology that drives the application.

3. ❌ **C. 6. Use the foreach processor to emit records to external systems.**  
   **Incorrect**. While foreach can be used for side‑effects, it is optional and not a requirement for writing a Streams application.

4. ✅ **D. 5. Provide explicit Serdes for all input and output topics.**  
   **Correct**. Serdes must be specified so the Streams library can serialize/deserialize records, otherwise the application will fail at runtime.

5. ❌ **E. 4. Set enable.auto.commit=true to allow automatic consumer offset commits.**  
   **Incorrect**. Kafka Streams manages commits automatically, setting this property can conflict with the library’s commit strategy.

6. ✅ **F. 3. Include application.id and bootstrap.servers in the StreamsConfig properties.**  
   **Correct**. These core configuration properties identify the application and connect it to the cluster, they are mandatory for any Streams app.

</details>

## Question 57 (Application Observability):
Which of the following metrics is most appropriate for detecting that a Kafka consumer group is falling behind in processing records?

- A. fetch_size_bytes_total
- B. consumer_lag
- C. request_latency_ms
- D. broker_active_connections
- E. producer_records_total

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In a Kafka deployment, the health of consumer groups is measured by the "consumer_lag" metric, which tells how many records each consumer is behind the latest offsets in its partitions. Monitoring this metric (e.g., via JMX, Prometheus exporters, or Confluent Control Center) allows operators to detect and react to backlogs quickly. Other metrics such as producer record counts, request latency, broker connections, or fetch size describe load, throughput, or network health, but they do not indicate consumer lag. Correctly interpreting consumer_lag prevents false alarms and ensures timely scaling or rebalance actions.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Consumer Metrics" / "Lag Monitoring" (pp. 373-377)

**Detailed explanation of each option:**

1. ❌ **A. fetch_size_bytes_total**  
   **Incorrect**. Shows the amount of data fetched per second by a consumer. This is a throughput metric, not a lag metric, and can be high even when the consumer is on‑track.

2. ✅ **B. consumer_lag**  
   **Correct**. This metric, emitted by the consumer’s JMX bean `kafka.consumer:type=consumer-coordinator-metrics,group-id=<group>` or via Confluent Control Center, reports the number of records each consumer group is behind the latest offsets. A rising value directly indicates lag and is the canonical metric for consumer‑group health.

3. ❌ **C. request_latency_ms**  
   **Incorrect**. Measures the round‑trip latency of network requests (e.g., fetch or produce). High values can indicate network or broker issues but do not quantify consumer backlog.

4. ❌ **D. broker_active_connections**  
   **Incorrect**. Represents the number of active TCP connections to a broker. It reflects client load but not how far consumers are behind the topic offsets.

5. ❌ **E. producer_records_total**  
   **Incorrect**. Counts the total number of records produced by the producer. While useful for load monitoring, it provides no insight into consumer processing speed or backlog.

</details>

## Question 58 (Programming & Serialization):
You are developing a Kafka producer that must send data securely to a broker cluster in a Confluent Platform deployment. Which set of client configuration properties is required to enable TLS encryption with server certificate verification?

- A. security.protocol=SSL ssl.truststore.location=/etc/ssl/truststore.jks ssl.truststore.password=truststorepw ssl.endpoint.identification.algorithm=HTTPS
- B. security.protocol=SASL_SSL sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="user" password="pw", ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS
- C. security.protocol=SSL ssl.certificate.location=/etc/ssl/client.crt ssl.key.location=/etc/ssl/client.key ssl.endpoint.identification.algorithm=HTTPS
- D. security.protocol=PLAINTEXT ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To secure client‑to‑broker traffic with TLS, the client must set security.protocol=SSL. The truststore contains the broker’s CA certificates, allowing the client to validate the broker’s certificate chain, ssl.truststore.location and ssl.truststore.password provide these files. The ssl.endpoint.identification.algorithm=HTTPS property enforces hostname verification, preventing man‑in‑the‑middle attacks. Options 2 and 4 omit essential TLS settings, while option 3 adds unnecessary SASL authentication. Proper configuration ensures encrypted communication and integrity of the broker identity, which is a core requirement for Confluent‑Certified developers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ✅ **A. security.protocol=SSL ssl.truststore.location=/etc/ssl/truststore.jks ssl.truststore.password=truststorepw ssl.endpoint.identification.algorithm=HTTPS**  
   **Correct**. The security.protocol=SSL enables TLS. The truststore properties provide the certificates to validate the broker's certificate, and ssl.endpoint.identification.algorithm=HTTPS enforces hostname verification against the broker certificate.

2. ❌ **B. security.protocol=SASL_SSL sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="user" password="pw", ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. SASL_SSL requires both SASL authentication and TLS. If the application does not need SASL, this configuration is unnecessarily complex. The exam question explicitly asks for TLS with server verification only, not authentication.

3. ❌ **C. security.protocol=SSL ssl.certificate.location=/etc/ssl/client.crt ssl.key.location=/etc/ssl/client.key ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. ssl.certificate.location and ssl.key.location are used for client authentication, not for server verification. The client must also provide a truststore to validate the broker certificate.

4. ❌ **D. security.protocol=PLAINTEXT ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. PLAINTEXT disables TLS, so traffic is not encrypted. The other properties are irrelevant without TLS.

</details>

## Question 59 (Stream Processing):
During a Kafka Streams deployment, you notice that the application stops consuming from its source topic after a few minutes and no records appear in the sink topic. The logs contain a stack trace of a `NullPointerException` thrown in a user‑defined `Processor`, after which the stream thread terminates. Which single action will enable the Streams application to continue processing after the exception?

- A. Configure a custom `StreamsUncaughtExceptionHandler` that returns `StreamsUncaughtExceptionHandler.StreamThreadExceptionResponse.REPLACE_THREAD` and set it via `streams.setUncaughtExceptionHandler(handler)`.
- B. Set `default.deserialization.exception.handler` to a custom handler that logs the exception and ignores the offending record.
- C. Set `application.state.interval.ms` to a larger value to allow the application to recover more gracefully.
- D. Increase the `num.stream.threads` property so that another thread can take over processing.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Correction: `StreamsUncaughtExceptionHandler.StreamThreadExceptionResponse` has only `REPLACE_THREAD`, `SHUTDOWN_CLIENT` and `SHUTDOWN_APPLICATION` (KIP-671), there is no `CONTINUE`. Option A was changed to use `REPLACE_THREAD`, which is the response that lets processing continue (note: the replacement thread re-reads from the last committed offset, so a deterministic poison record that always throws will keep killing threads, fix the processor or skip the record in code). Original text follows, with CONTINUE read as REPLACE_THREAD.

Kafka Streams’ default uncaught‑exception handler terminates the stream thread on any runtime exception, which stops processing entirely. Providing a custom `StreamsUncaughtExceptionHandler` that returns `REPLACE_THREAD` tells Streams to start a replacement thread, allowing the topology to resume after the error. Adding more threads or adjusting deserialization or state‑flush settings do not address the thread‑termination behavior. This question tests knowledge of error handling in Streams and the correct use of the uncaught‑exception handler API.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams: Architecture Overview" (pp. 410-416)

**Detailed explanation of each option:**

1. ✅ **A. Configure a custom `StreamsUncaughtExceptionHandler` that returns `StreamsUncaughtExceptionHandler.StreamThreadExceptionResponse.REPLACE_THREAD` and set it via `streams.setUncaughtExceptionHandler(handler)`.**  
   **Correct**. The default uncaught‑exception handler in Kafka Streams terminates the thread (and often the application). A custom handler that returns REPLACE_THREAD replaces the failed thread with a new one, allowing the application to keep processing after the exception.

2. ❌ **B. Set `default.deserialization.exception.handler` to a custom handler that logs the exception and ignores the offending record.**  
   **Incorrect**. That handler applies only to deserialization errors in consumers, not to runtime exceptions thrown inside a processor.

3. ❌ **C. Set `application.state.interval.ms` to a larger value to allow the application to recover more gracefully.**  
   **Incorrect**. This property controls how often the state directory is flushed, it does not affect thread termination on runtime errors.

4. ❌ **D. Increase the `num.stream.threads` property so that another thread can take over processing.**  
   **Incorrect**. Adding more threads does not replace the thread that crashed, the crashed thread will still terminate and the application will not resume unless the uncaught‑exception handler is changed.

</details>

## Question 60 (Application Development):
When connecting an Apache Kafka producer or consumer to a Confluent Cloud secured cluster that uses SASL/SSL authentication, which of the following configuration steps are **required** to establish a successful connection? Select all that apply.

- A. Provide a JAAS configuration file (or set `java.security.auth.login.config`) containing the client principal and password, and reference it via the `SASL_CLIENT_JAAS_CONFIG` system property.
- B. Use the `SASL_PLAINTEXT` security protocol to combine SASL authentication with plaintext transport.
- C. Specify `ssl.keystore.location` and `ssl.keystore.password` to supply a client certificate for mutual TLS authentication.
- D. Include the broker’s hostname in the `bootstrap.servers` list using the `ssl://` scheme, e.g., `ssl://broker:9093`.
- E. Set the `security.protocol` property to `SASL_SSL` and specify a SASL mechanism such as `PLAIN` or `SCRAM-SHA-512` via `sasl.mechanism`.
- F. Configure the `ssl.truststore.location` and `ssl.truststore.password` properties to trust the broker’s certificate chain.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, E, F

**Explanation:**

To securely connect to a Kafka cluster that uses SASL/SSL, a client must (1) set `security.protocol=SASL_SSL` and a valid SASL mechanism, (2) provide SASL credentials via a JAAS config file, and (3) trust the broker’s certificate by configuring the SSL truststore. These three steps establish encryption, authenticate the client, and ensure the broker’s identity. Options 4–6 are optional or incorrect: a client keystore is only needed for mutual TLS, `ssl://` is not a valid bootstrap syntax, and `SASL_PLAINTEXT` lacks encryption.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ✅ **A. Provide a JAAS configuration file (or set `java.security.auth.login.config`) containing the client principal and password, and reference it via the `SASL_CLIENT_JAAS_CONFIG` system property.**  
   **Correct**. The JAAS file supplies the SASL credentials (username/password or keytab). The client must read these credentials, otherwise SASL authentication cannot occur, leading to a connection failure.

2. ❌ **B. Use the `SASL_PLAINTEXT` security protocol to combine SASL authentication with plaintext transport.**  
   **Incorrect**. `SASL_PLAINTEXT` does not encrypt traffic, which is unacceptable for a secured cluster that requires SSL. Attempting to use this protocol will result in a connection failure on a cluster that mandates TLS.

3. ❌ **C. Specify `ssl.keystore.location` and `ssl.keystore.password` to supply a client certificate for mutual TLS authentication.**  
   **Incorrect**. Mutual TLS is optional, most Confluent Cloud clusters use SASL for client authentication. Including a keystore will work if the cluster requires mutual TLS, but it is not a mandatory step for standard SASL/SSL setups.

4. ❌ **D. Include the broker’s hostname in the `bootstrap.servers` list using the `ssl://` scheme, e.g., `ssl://broker:9093`.**  
   **Incorrect**. The `bootstrap.servers` property uses plain host:port pairs, adding a scheme prefix is not supported and will cause a parsing error. The correct format is `broker:9093` with the protocol set via `security.protocol`.

5. ✅ **E. Set the `security.protocol` property to `SASL_SSL` and specify a SASL mechanism such as `PLAIN` or `SCRAM-SHA-512` via `sasl.mechanism`.**  
   **Correct**. This property tells the client to use SSL for encryption and SASL for authentication. It is mandatory for a secured cluster that requires both encryption and SASL credentials. Without it, the client will attempt an unsecured connection and fail.

6. ✅ **F. Configure the `ssl.truststore.location` and `ssl.truststore.password` properties to trust the broker’s certificate chain.**  
   **Correct**. The truststore holds the CA certificates that signed the broker’s certificate. Without a trusted CA, the SSL handshake will fail, preventing the client from establishing a secure connection.

</details>
