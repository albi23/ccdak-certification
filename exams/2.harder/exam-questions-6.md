> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1 (Kafka Fundamentals):
Which of the following statements about Kafka compression is FALSE?

- A. Using GZIP compression can increase latency but reduces the amount of data sent over the network compared to no compression.
- B. The `max.request.size` broker setting limits the size of compressed batches that a producer can send, but does not affect the size of uncompressed records within the batch.
- C. The `compression.type` configuration on the producer applies to each batch of records that the producer sends to a partition, the broker does not override it.
- D. A compressed batch will always be smaller than an uncompressed batch of the same records, regardless of the compression codec.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Kafka allows producers to specify a compression codec (gzip, snappy, lz4, zstd, none) via the compression.type property. The codec compresses the entire batch of records before it is sent to the broker, so the broker stores the compressed data exactly as received. `max.request.size` is a PRODUCER setting (not a broker one), the broker-side limit is `message.max.bytes` / topic `max.message.bytes` (applied to the compressed batch), so statement B is false. GZIP offers the highest compression ratio but incurs higher CPU and latency, lighter codecs trade off compression ratio for speed. However, compression is not guaranteed to reduce size for every batch – very small or already‑compressed data can lead to larger payloads, so the statement that a compressed batch is always smaller is false. The original question has two false statements (B and D), so both are the answer.

Verified (answer confirmed). ProducerConfig source: MAX_REQUEST_SIZE_DOC says it is "effectively a cap on the maximum uncompressed record batch size.
Note that the server has its own cap on the record batch size (after compression if compression is enabled)", COMPRESSION_TYPE_DOC:
"Compression is of full batches of data". So B is false twice over (producer not broker setting, it caps the uncompressed batch).
Source: https://raw.githubusercontent.com/apache/kafka/trunk/clients/src/main/java/org/apache/kafka/clients/producer/ProducerConfig.java

**Detailed explanation of each option:**

1. ❌ **A. Using GZIP compression can increase latency but reduces the amount of data sent over the network compared to no compression.**  
   **Incorrect (the statement is true)**. GZIP provides higher compression ratios at the cost of CPU and latency. It generally reduces payload size, especially for large, repetitive data, but may increase latency due to encoding/decoding overhead.

2. ✅ **B. The `max.request.size` broker setting limits the size of compressed batches that a producer can send, but does not affect the size of uncompressed records within the batch.**  
   **Correct (this statement is FALSE)**. max.request.size is a producer-side setting, not a broker setting, the producer also checks it against the record size at send time. The broker limit is message.max.bytes / max.message.bytes.

3. ❌ **C. The `compression.type` configuration on the producer applies to each batch of records that the producer sends to a partition, the broker does not override it.**  
   **Incorrect (true with the default broker/topic compression.type=producer)**. The producer’s compression.type (e.g., gzip, snappy, lz4, zstd) determines the codec used for each batch sent. The broker stores the compressed data as sent, it does not change the codec or decompress the batch.

4. ✅ **D. A compressed batch will always be smaller than an uncompressed batch of the same records, regardless of the compression codec.**  
   **Correct (this statement is FALSE)**. Compression may add overhead and sometimes produce a larger payload if the data is already compressed, highly random, or too small. Some codecs (e.g., lz4, snappy) may produce larger batches for very small records.

</details>

## Question 2 (Application Development):
In Kafka, the key of a record is hashed to determine the target partition. Which of the following statements about key hashing and partitioning are **true**?

- A. The hash calculation is deterministic, the same key will always map to the same partition within a single cluster.
- B. You can override the default partitioning logic by providing a custom implementation of org.apache.kafka.clients.producer.Partitioner.
- C. When a key is null, the partitioner selects a partition using a round‑robin strategy(or sticky in newer versions of Kafka).
- D. The partitioner applies the hash to the key's string representation before computing the hash.
- E. The default Kafka partitioner uses Murmur2 hashing on the key bytes to select a partition.
- F. Changing the hashing algorithm on the producer side automatically changes the partitioning behavior on the broker without any broker configuration.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C, E

**Explanation:**

Kafka uses the key’s byte array to compute a hash (Murmur2 by default) which is then modded by the partition count. This deterministic mapping ensures that identical keys always go to the same partition as long as the topic’s partition count remains unchanged. Null keys bypass hashing and are spread across partitions (sticky batching since Kafka 2.4, not strict round-robin). Custom partitioning can be achieved by implementing the Partitioner interface and setting the 'partitioner.class' config, only the producer handles hashing, so no broker config changes are required. Understanding these nuances is essential for developers who need predictable ordering or load distribution across partitions.

Source: book ch. 3 "Partitions" (PDF p. 97-99: murmur2 hash of key bytes, null key = sticky/random, custom Partitioner), https://kafka.apache.org/documentation/#producerconfigs_partitioner.class

**Detailed explanation of each option:**

1. ✅ **A. The hash calculation is deterministic, the same key will always map to the same partition within a single cluster.**  
   **Correct**. Given the same key bytes and the same cluster metadata, the hash will always produce the same partition number.

2. ✅ **B. You can override the default partitioning logic by providing a custom implementation of org.apache.kafka.clients.producer.Partitioner.**  
   **Correct**. Implementing this interface and configuring 'partitioner.class' allows custom hashing or routing logic.

3. ✅ **C. When a key is null, the partitioner selects a partition using a round‑robin strategy.**  
   **Correct**. If the key is null, the partitioner picks a partition without hashing, since Kafka 2.4 it is a "sticky" strategy (fills a batch for one partition before switching), not plain round‑robin.

4. ❌ **D. The partitioner applies the hash to the key's string representation before computing the hash.**  
   **Incorrect**. The hash is applied directly to the raw key bytes, not to a string conversion.

5. ✅ **E. The default Kafka partitioner uses Murmur2 hashing on the key bytes to select a partition.**  
   **Correct**. Kafka’s DefaultPartitioner computes a Murmur2 hash of the key’s raw byte array and then takes the modulo with the number of partitions.

6. ❌ **F. Changing the hashing algorithm on the producer side automatically changes the partitioning behavior on the broker without any broker configuration.**  
   **Incorrect**. Partitioning is performed by the producer, brokers do not rehash keys. Only producer configuration is needed.

</details>

## Question 3 (Observability & Testing):
Which of the following are valid ways to monitor an application that produces or consumes data from a Kafka cluster?.

- A. Expose the application’s JMX metrics and scrape them with Prometheus, then visualize in Grafana
- B. Rely solely on application logs (e.g., Log4j) to determine performance and errors
- C. Use the Confluent Control Center dashboards to view consumer lag and topic throughput
- D. Query the Kafka Streams state store via interactive queries to check the state of application data
- E. Rely only on OpenTelemetry distributed tracing (collecting no Kafka client metrics at all) to track consumer lag and topic throughput
- F. Use the Kafka Connect REST API to monitor producer latency

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

Monitoring a Kafka‑based application requires collecting metrics, visualizing performance, and inspecting state. JMX metrics exposed by Kafka and Kafka Streams can be scraped by Prometheus and visualized with Grafana, giving real‑time throughput and lag data. Confluent Control Center offers built‑in dashboards that expose similar metrics in a user‑friendly interface. Kafka Streams interactive queries let developers probe the state store to confirm correctness and detect anomalies. Relying only on logs or the Connect REST API does not provide the granular, continuous metrics needed for robust observability, and OpenTelemetry, while valuable for tracing, is complementary rather than a primary monitoring tool. These three approaches collectively cover metric collection, visualization, and state inspection, aligning with best practices for Observability & Testing in Confluent Certified Developer exams. Note: OpenTelemetry is a legitimate tool in general (KIP-714 even uses the OpenTelemetry metrics format for client telemetry), so option E was reworded to say 'only tracing, no Kafka metrics', which makes it unambiguously wrong. Control Center is Confluent-platform specific.

Source (verified): https://kafka.apache.org/42/operations/monitoring/ (JMX metrics), https://cwiki.apache.org/confluence/display/KAFKA/KIP-714%3A+Client+metrics+and+observability

**Detailed explanation of each option:**

1. ✅ **A. Expose the application’s JMX metrics and scrape them with Prometheus, then visualize in Grafana**  
   **Correct**. Kafka and Kafka Streams expose JMX metrics that Prometheus can scrape. These metrics include record throughput, lag, and latency, which are essential for observability.

2. ❌ **B. Rely solely on application logs (e.g., Log4j) to determine performance and errors**  
   **Incorrect**. While logs help debugging, they don’t provide the real‑time metrics or visibility required for proper observability.

3. ✅ **C. Use the Confluent Control Center dashboards to view consumer lag and topic throughput**  
   **Correct**. Control Center provides real‑time visualizations of topic metrics, consumer group lag, and producer latency. It’s a built‑in monitoring solution for Confluent Platform users.

4. ✅ **D. Query the Kafka Streams state store via interactive queries to check the state of application data**  
   **Correct**. Interactive queries expose the current state of a Streams application, allowing developers to monitor the contents and health of state stores.

5. ❌ **E. Rely only on OpenTelemetry distributed tracing (collecting no Kafka client metrics at all) to track consumer lag and topic throughput**  
   **Incorrect**. Tracing alone does not give consumer lag or topic throughput, OpenTelemetry is complementary to metrics, not a replacement.

6. ❌ **F. Use the Kafka Connect REST API to monitor producer latency**  
   **Incorrect**. The Connect REST API provides connector status and metrics but not producer latency for non‑Connector applications.

</details>

## Question 4 (Kafka Fundamentals):
A topic in a Kafka cluster is configured with the following settings: 
```
cleanup.policy=delete 
retention.ms=86400000 (1 day) 
segment.bytes=1073741824 (1 GB)
```
Which statement best describes how the broker handles message deletion for this topic? 

- A. Messages older than 1 day are retained until the current segment is closed, after which they are deleted.
- B. The broker will keep all messages indefinitely because `cleanup.policy=delete` is overridden by `retention.ms`.
- C. The broker will delete messages only after the current segment is full (1 GB) and older than 1 day.
- D. The broker will delete all messages older than 1 day regardless of segment size.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka implements data retention by segmenting topic logs into files. The `cleanup.policy=delete` flag tells the broker to remove entire segments when they become older than `retention.ms`. The broker only deletes closed segments, an open segment can exceed the retention time but remains until it is closed (triggered by `segment.bytes` or `segment.ms`). Thus, data older than the retention period is removed only after the segment that contains it is closed. This behavior ensures efficient log management while preventing the deletion of in‑flight data. Note: a segment is rolled by `segment.bytes` OR `segment.ms` (default 7 days), and the segment age is based on the largest timestamp in it.

Source: book ch. 6 "Retention of Messages" / active segment (PDF p. 182, 188), https://kafka.apache.org/documentation/#topicconfigs_retention.ms

**Detailed explanation of each option:**

1. ✅ **A. Messages older than 1 day are retained until the current segment is closed, after which they are deleted.**  
   **Correct**. Kafka deletes segments only after they are closed. An open segment can become older than the retention period but cannot be deleted until it is closed (when it reaches `segment.bytes`). Once closed and older than `retention.ms`, the segment is removed.

2. ❌ **B. The broker will keep all messages indefinitely because `cleanup.policy=delete` is overridden by `retention.ms`.**  
   **Incorrect**. The `retention.ms` setting dictates how long data is kept, it does not override the delete cleanup policy. Messages are still deleted after the retention period.

3. ❌ **C. The broker will delete messages only after the current segment is full (1 GB) and older than 1 day.**  
   **Incorrect**. Retention time applies to closed segments, however, the broker can delete segments older than the retention period regardless of whether the current open segment has reached the size limit. Thus, this statement incorrectly links size and time together.

4. ❌ **D. The broker will delete all messages older than 1 day regardless of segment size.**  
   **Incorrect**. While the net effect is that old data is removed, deletion is performed at the segment level. Kafka cannot delete individual messages, it deletes entire log segments that are older than the configured retention. Therefore the statement is imprecise, making it an incorrect answer.

</details>

## Question 5 (Deployment & Ops):
During a production deployment of a Kafka cluster, a team wants to guarantee that all records related to a specific customer are processed in the order they are produced. Which statement about message keying is correct?

- A. If no key is provided, Kafka automatically orders records based on the event timestamp.
- B. Records with the same key can be sent to different partitions if the topic has more partitions than the number of unique keys.
- C. A key can be any Java object, the producer will serialize it using the default key serializer without configuration.
- D. Using the customer ID as the record key ensures that all records with that key are routed to the same partition, preserving order within that partition.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka, message keying is the mechanism that links records to a specific partition. When a key is present, the default producer partitioner hashes it to a partition index, guaranteeing that all records with the same key land in the same partition and thus are processed in order. Without a key, records are spread across partitions (sticky batching since 2.4), and ordering is only preserved across the entire topic if it has a single partition (the per-key guarantee also holds only while the partition count does not change). Misconceptions often arise around timestamps or assuming keys can be arbitrary objects, in practice, the key must be serializable by the configured key serializer. This behavior is critical in deployment scenarios where ordering or affinity per entity is required, such as per‑customer or per‑session processing.

Source: book ch. 3 "Partitions" (PDF p. 97), https://kafka.apache.org/documentation/#intro_concepts_and_terms

**Detailed explanation of each option:**

1. ❌ **A. If no key is provided, Kafka automatically orders records based on the event timestamp.**  
   **Incorrect**. Without a key, the partitioner spreads records across partitions (sticky, not by timestamp). Ordering is not guaranteed and timestamps are not used for partitioning.

2. ❌ **B. Records with the same key can be sent to different partitions if the topic has more partitions than the number of unique keys.**  
   **Incorrect**. The partitioner deterministically maps a key to a single partition, even with many partitions, the same key will never end up in multiple partitions. Only if the key is null will round‑robin distribution occur.

3. ❌ **C. A key can be any Java object, the producer will serialize it using the default key serializer without configuration.**  
   **Incorrect**. The key must be a type supported by the configured key serializer (e.g., String, byte[], Avro). Using an unsupported type will cause a serialization error unless a custom serializer is configured.

4. ✅ **D. Using the customer ID as the record key ensures that all records with that key are routed to the same partition, preserving order within that partition.**  
   **Correct**. Kafka’s default partitioner hashes the key, records with the same key always map to the same partition, and ordering is guaranteed per partition. This is the primary method for maintaining ordering for a subset of data in a distributed topic.

</details>

## Question 6 (Streams Development):
In a Kafka Streams application, you need to compute the cumulative sum of an integer value for each key in a KTable and persist the result in a RocksDB local state store named "sum-store". Which code snippet correctly achieves this using the `aggregate` method? (Note: `aggregate` is defined on KGroupedStream/KGroupedTable, not directly on KTable – treat `inputTable` as the grouped stream/table, for KGroupedTable an additional subtractor is required.)

- A. ```KTable<String, Integer> aggregated = inputTable.aggregate( Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") .withKeySerde(Serdes.String()) .withValueSerde(Serdes.Integer()), () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue ), ```
- B. ```KTable<String, Integer> aggregated = inputTable.reduce( (v1, v2) -> v1 + v2, Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") ), ```
- C. ```KTable<String, Integer> aggregated = inputTable.aggregate( () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue, Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") .withKeySerde(Serdes.String()) .withValueSerde(Serdes.Integer()) ), ```
- D. ```KTable<String, Integer> aggregated = inputTable.aggregate( () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue ), ```

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The `aggregate` operation in Kafka Streams requires an initializer, an aggregator, and a `Materialized` instance that can name the state store and define serdes. The correct signature is `aggregate(Initializer, Aggregator, Materialized<…>)`. Option C supplies these arguments in the correct order and names the RocksDB store "sum-store", satisfying all requirements. Options A, B and D either use the wrong parameter order, a different aggregation method (reduce), or omit the store name.
FLAG: question wording is imprecise (KTable has no aggregate method, it is KGroupedStream.aggregate).

Source: https://kafka.apache.org/43/documentation/streams/developer-guide/dsl-api.html#aggregating

**Detailed explanation of each option:**

1. ❌ **A. ``` KTable<String, Integer> aggregated = inputTable.aggregate( Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") .withKeySerde(Serdes.String()) .withValueSerde(Serdes.Integer()), () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue ), ```**  
   **Incorrect**. The parameters are passed in the wrong order, the compiler will raise an error because `Materialized` cannot be the first argument to `aggregate`.

2. ❌ **B. ``` KTable<String, Integer> aggregated = inputTable.reduce( (v1, v2) -> v1 + v2, Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") ), ```**  
   **Incorrect**. This uses `reduce` instead of `aggregate`. While it would compute a per‑key sum, the question explicitly asks for the `aggregate` method, so this snippet is not the correct answer.

3. ✅ **C. ``` KTable<String, Integer> aggregated = inputTable.aggregate( () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue, Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>>as("sum-store") .withKeySerde(Serdes.String()) .withValueSerde(Serdes.Integer()) ), ```**  
   **Correct**. This code provides the initializer, aggregator, and a correctly ordered `Materialized` instance that names the state store "sum-store" and specifies the required serdes. It matches the signature `aggregate(Initializer<VR>, Aggregator<? super K, ? super V, VR>, Materialized<…>)` and is therefore correct.

4. ❌ **D. ``` KTable<String, Integer> aggregated = inputTable.aggregate( () -> 0, (aggKey, newValue, aggValue) -> aggValue + newValue ), ```**  
   **Incorrect**. This snippet omits the `Materialized` parameter, so the state store gets an auto-generated internal name (e.g. KSTREAM-AGGREGATE-STATE-STORE-0000000001) and the default serdes from the config. It does not satisfy the requirement to name the store "sum-store".

</details>

## Question 7 (Kafka Connect):
When deploying a Kafka Connect connector in a distributed cluster, which of the following configuration properties directly influence how many connector tasks can run concurrently for that connector instance?

- A. `key.converter`
- B. `offset.flush.interval.ms`
- C. `worker.threads`
- D. `connector.class`
- E. `tasks.max`
- F. `max.poll.records`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

In a distributed Kafka Connect cluster, task parallelism is governed by the connector’s own tasks.max property, which caps the number of tasks that the connector can spawn
(the connector may create fewer, e.g. a sink is limited by the topic partition count). `worker.threads` is NOT a Kafka Connect configuration (it does not exist, each task runs in its own thread).
While consumer‑side properties such as max.poll.records or offset.flush.interval.ms control batch processing and commit frequency, they do not change the number of tasks. Similarly,
metadata properties like connector.class and key.converter are required for the connector’s operation but do not influence concurrency. Understanding these distinctions is essential
for tuning connector performance and resource utilization in production deployments.

Source: https://kafka.apache.org/documentation/#connectconfigs_tasks.max (connector config), book ch. 9 (PDF p. 280, tasks.max), https://kafka.apache.org/documentation/#connectconfigs for the worker configs

**Detailed explanation of each option:**

1. ❌ **A. key.converter**  
   **Incorrect**. Determines how key data is serialized/deserialized. It has no effect on task scaling. Incorrect.

2. ❌ **B. offset.flush.interval.ms**  
   **Incorrect**. Controls how often offsets are committed to the backing store. It has no impact on task parallelism. Incorrect.

3. ❌ **C. worker.threads**  
   **Incorrect**. No such Kafka Connect worker property exists, each task is executed in its own thread. Incorrect.

4. ❌ **D. connector.class**  
   **Incorrect**. Specifies the Java class that implements the connector. It does not affect task concurrency. Incorrect.

5. ✅ **E. tasks.max**  
   **Correct**. This connector‑specific setting defines the maximum number of parallel tasks the connector may create. It is the primary knob for scaling a connector instance. Correct.

6. ❌ **F. max.poll.records**  
   **Incorrect**. This consumer‑level setting limits how many records are returned in a single poll. It affects batch size, not the number of tasks. Incorrect.

</details>

## Question 8 (Kafka Fundamentals):
In Apache Kafka, what is the primary responsibility of a broker that hosts the leader replica of a partition?

- A. It handles all read requests for the partition, but writes are forwarded to follower replicas.
- B. It coordinates consumer group state and ensures balanced assignment.
- C. It handles writes but serves reads only when the replica is configured as a follower.
- D. It serves reads from all replicas, but only the leader writes are committed to ZooKeeper.
- E. It handles all read and write requests for the partition, follower replicas only replicate the log and serve reads when the broker is in read‑only mode.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

In Kafka, each partition has a single leader replica that handles every read and write operation. Followers replicate the leader’s log, by default they do not serve clients (only since Kafka 2.4 / KIP-392 can consumers optionally fetch from the closest follower via client.rack and replica.selector.class – producers always write to the leader).
FLAG: the wording of option E ("read‑only mode") is inaccurate, but it is the only option correctly stating that the leader handles reads and writes.
The leader is responsible for guaranteeing ordering and durability of messages within its partition. Understanding this leader/follower model is essential for tuning replication factor, handling broker failures, and ensuring data consistency. A common misconception is that followers can serve reads or that writes are forwarded, in reality, all client traffic is routed to the leader. Refer to Kafka’s replication documentation for detailed mechanics.

Source: book ch. 7 "Replication" (PDF p. 355: all produce and consume requests go to the leader) and ch. 3 client.rack (PDF p. 112, fetch from closest replica), https://kafka.apache.org/documentation/#replication

**Detailed explanation of each option:**

1. ❌ **A. It handles all read requests for the partition, but writes are forwarded to follower replicas.**  
   **Incorrect**. The leader does not forward writes, it processes all writes. Followers only replicate data from the leader.

2. ❌ **B. It coordinates consumer group state and ensures balanced assignment.**  
   **Incorrect**. Consumer group coordination is handled by the group coordinator broker, not the leader replica of a partition.

3. ❌ **C. It handles writes but serves reads only when the replica is configured as a follower.**  
   **Incorrect**. Reads are served by the leader, not by the follower configuration. By default followers do not serve reads (exception: follower fetching, KIP-392).

4. ❌ **D. It serves reads from all replicas, but only the leader writes are committed to ZooKeeper.**  
   **Incorrect**. Log data is never stored in ZooKeeper (and Kafka 4.x runs on KRaft without ZooKeeper). Reads are served by the leader, not all replicas.

5. ✅ **E. It handles all read and write requests for the partition, follower replicas only replicate the log and serve reads when the broker is in read‑only mode.**  
   **Correct**. The leader processes all reads and writes. Followers replicate the leader’s log and, by default, do not serve reads unless specifically configured for read‑only operations.

</details>

## Question 9 (Application Development):
When using the Kafka Producer API to set custom headers, which statement accurately reflects the size and ordering constraints defined by the Kafka broker?

- A. Header keys must be no longer than 256 bytes, header values no longer than 4 KB, and the order of headers is preserved as they are added.
- B. Header keys are strings and values are byte arrays, there is no per-header size limit, only the total record batch size limit (`message.max.bytes` / `max.message.bytes`) applies.
- C. The combined size of all headers and the record payload cannot exceed the broker's `max.message.bytes` setting, and header ordering is not guaranteed.
- D. Each header can be up to 1 MB in size, and headers are sorted alphabetically before transmission.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Record headers are an ordered collection of key/value pairs (keys are Strings, values are byte[], duplicate keys are allowed). Kafka defines NO header-specific size limits (the 256 B / 4 KB figures in option A do not exist in Kafka), headers only count toward the overall record batch size limit (`message.max.bytes` on the broker / `max.message.bytes` on the topic, `max.request.size` on the producer). Header order IS preserved. Verified: the Headers Javadoc says "A mutable ordered collection of Header objects ... The order of headers is preserved in the order they were added" and documents no size limits. 


Source: https://kafka.apache.org/42/javadoc/org/apache/kafka/common/header/Headers.html

**Detailed explanation of each option:**

1. ❌ **A. Header keys must be no longer than 256 bytes, header values no longer than 4 KB, and the order of headers is preserved as they are added.**  
   **Incorrect**. Kafka documents no such 256 B / 4 KB header limits, only the total record/batch size limits apply (the ordering part is true).

2. ✅ **B. Header keys are strings and values are byte arrays, there is no per-header size limit, only the total record batch size limit (`message.max.bytes` / `max.message.bytes`) applies.**  
   **Correct**. There is no per-header limit, only the total record size limit, header keys are strings and values are byte arrays.

3. ❌ **C. The combined size of all headers and the record payload cannot exceed the broker's `max.message.bytes` setting, and header ordering is not guaranteed.**  
   **Incorrect**. The size part is right, but Kafka guarantees that the order in which headers are added to a `ProducerRecord` is preserved when sent to the broker. Header ordering is therefore deterministic, not arbitrary.

4. ❌ **D. Each header can be up to 1 MB in size, and headers are sorted alphabetically before transmission.**  
   **Incorrect**. Kafka defines no per-header size limit (neither 1 MB nor 4 KB, only the total record/batch limit applies), and it does not sort headers alphabetically—order is maintained.

</details>

## Question 10 (Kafka Fundamentals):
Which of the following statements correctly describe the capabilities of the Kafka Admin API (AdminClient) in Apache Kafka 3.x?(Note: in Kafka 4.0 `alterConfigs` was removed – use `incrementalAlterConfigs`.)

- A. The AdminClient can create topics with arbitrary partition counts and replication factors using the createTopics method.
- B. The AdminClient supports altering topic configurations at runtime without requiring a broker restart using the alterConfigs method.
- C. The AdminClient provides a GetClusterInfo request that retrieves the current broker cluster ID.
- D. The Admin API can produce records to topics as part of administrative operations.
- E. The Admin API can delete consumer group offsets via the deleteConsumerGroupOffsets method.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

The AdminClient is Kafka’s programmatic interface for cluster metadata and configuration tasks. It can create topics (createTopics), modify topic, broker, and consumer group configurations (alterConfigs), and delete consumer group offsets (deleteConsumerGroupOffsets). It does not provide a dedicated GetClusterInfo request, cluster information (including the cluster ID) is obtained via describeCluster(). Note: `alterConfigs` is deprecated since 2.3 and removed in Kafka 4.0 in favor of `incrementalAlterConfigs`. Additionally, producing records is outside the scope of the Admin API and is performed with the Producer API. Understanding these distinctions is essential for developers designing management or automation tools around Kafka clusters.

Source: book ch. 5 "Kafka Administration" / AdminClient (PDF p. 103 ff.), https://kafka.apache.org/43/javadoc/org/apache/kafka/clients/admin/Admin.html

**Detailed explanation of each option:**

1. ✅ **A. The AdminClient can create topics with arbitrary partition counts and replication factors using the createTopics method.**  
   **Correct**. The AdminClient’s createTopics API allows specifying the number of partitions and the replication factor per topic at creation time. See https://kafka.apache.org/documentation.html#admin_createTopics.

2. ✅ **B. The AdminClient supports altering topic configurations at runtime without requiring a broker restart using the alterConfigs method.**  
   **Correct**. The alterConfigs API (deprecated, in 4.x use incrementalAlterConfigs) enables updating configuration properties for topics, consumer groups, and brokers on the fly. Refer to https://kafka.apache.org/documentation.html#admin_alterConfigs.

3. ❌ **C. The AdminClient provides a GetClusterInfo request that retrieves the current broker cluster ID.**  
   **Incorrect**. While AdminClient can describe the cluster with describeCluster, there is no GetClusterInfo request, cluster ID is exposed through DescribeClusterResult.clusterId().

4. ❌ **D. The Admin API can produce records to topics as part of administrative operations.**  
   **Incorrect**. Record production is handled by the Producer API, not by the AdminClient, which is dedicated to metadata and configuration management.

5. ✅ **E. The Admin API can delete consumer group offsets via the deleteConsumerGroupOffsets method.**  
   **Correct**. AdminClient provides deleteConsumerGroupOffsets to remove specific offsets for a consumer group, allowing group re‑initialization. Documentation: https://kafka.apache.org/documentation.html#admin_deleteConsumerGroupOffsets.

</details>

## Question 11 (Kafka Connect):
You are configuring a Kafka Connect worker to connect to a Confluent Platform cluster that requires SASL/PLAIN authentication over TLS. Which of the following worker properties must be set (directly or via the worker properties file) to establish a secure connection?

- A. Add `security.protocol=SASL_SSL` to the worker properties.
- B. Set `sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="user" password="pass",` in the worker properties.
- C. Configure `ssl.truststore.location` and `ssl.truststore.password` in the worker properties.
- D. Set `bootstrap.servers` to `ssl://kafka-broker:9093`.
- E. Provide `sasl.mechanism=PLAIN` in the worker properties.
- F. Add `producer.security.protocol=PLAINTEXT` to the connector configuration.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

A Kafka Connect worker connects to a Kafka cluster via the bootstrap servers and applies a single security protocol for both consumer and producer clients. For a SASL/PLAIN over TLS cluster, the worker must specify `security.protocol=SASL_SSL`, the `sasl.mechanism=PLAIN`, and provide the JAAS login configuration. These three properties enable the TLS handshake and SASL authentication. Optional truststore settings are only needed when the broker’s certificate isn’t in the default truststore. Note: the worker-level settings secure only the worker’s own clients (internal topics/admin), the producers/consumers of connectors need the same settings with the `producer.`/`consumer.`/`admin.` prefixes (or connector-level `producer.override.*`/`consumer.override.*`). Specifying `ssl://` in `bootstrap.servers` is unnecessary, and setting a plaintext protocol would expose traffic. Understanding which properties belong to the worker versus connector configuration prevents misconfigurations that cause connection failures.

Source: https://docs.confluent.io/platform/current/connect/security.html, https://kafka.apache.org/documentation/#security_sasl_plain, book ch. 11 (PDF p. 304)

**Detailed explanation of each option:**

1. ✅ **A. Add `security.protocol=SASL_SSL` to the worker properties.**  
   **Correct**. This property tells the worker to use TLS for transport and SASL for authentication, which is mandatory for a SASL/PLAIN over TLS cluster.

2. ✅ **B. Set `sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="user" password="pass",` in the worker properties.**  
   **Correct**. This JAAS configuration supplies the credentials for SASL/PLAIN authentication and is mandatory for the worker to authenticate.

3. ❌ **C. Configure `ssl.truststore.location` and `ssl.truststore.password` in the worker properties.**  
   **Incorrect**. While useful when the broker uses a self‑signed or private CA certificate, these properties are optional if the broker's certificate is already trusted by the Java default truststore.

4. ❌ **D. Set `bootstrap.servers` to `ssl://kafka-broker:9093`.**  
   **Incorrect**. bootstrap.servers takes plain host:port pairs (a URL scheme like `ssl://` is not valid there), the security protocol dictates TLS usage.

5. ✅ **E. Provide `sasl.mechanism=PLAIN` in the worker properties.**  
   **Correct**. The SASL mechanism must match the broker's configuration, for SASL/PLAIN authentication this property is required.

6. ❌ **F. Add `producer.security.protocol=PLAINTEXT` to the connector configuration.**  
   **Incorrect**. Connector configurations are separate from the worker and must mirror the worker's security settings, using PLAINTEXT would break the secure connection.

</details>

## Question 12 (Streams Development):
Which of the following options are effective techniques for tuning performance and scaling a Kafka Streams application?

- A. Disable the use of changelog topics for state stores to reduce network traffic.
- B. Configure the RocksDB compression property to snappy to improve write throughput.
- C. Reduce the window size in windowed joins to lower latency and memory usage.
- D. Increase the number of stream threads (default 1) to match the number of partitions for parallel processing.
- E. Use the materialized-as clause to create multiple state stores for a single topology to improve query performance.
- F. Increase the record cache size (`statestore.cache.max.bytes`) to reduce writes to the state store and downstream traffic.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

Documented tuning/scaling levers for Kafka Streams: increase `num.stream.threads` (config name, default 1) up to the number of tasks/partitions and/or add instances, enlarge the record cache (`statestore.cache.max.bytes`, formerly `cache.max.bytes.buffering`, default 10 MB) which reduces writes to RocksDB and downstream/changelog traffic, tune RocksDB via a `rocksdb.config.setter`. Disabling changelogs sacrifices fault tolerance, shrinking join windows changes the application semantics, creating multiple stores per topology is not a recognized query-performance technique. Verified live: `statestore.cache.max.bytes` (default 10485760, `cache.max.bytes.buffering` deprecated), `num.stream.threads` (default 1), `rocksdb.config.setter` exist, the record cache reduces output records. Option F was reworded (the original 'very large value' was dubious), the original key was B, D, E but E has no documentation support.
Still unverified: that RocksDB compression=snappy is a documented throughput tuning (B), docs only show rocksdb.config.setter for RocksDB tuning.

Source: https://kafka.apache.org/42/streams/developer-guide/memory-mgmt/ , https://kafka.apache.org/42/streams/developer-guide/config-streams/

**Detailed explanation of each option:**

1. ❌ **A. Disable the use of changelog topics for state stores to reduce network traffic.**  
   **Incorrect**. Changelog topics are essential for fault‑tolerance and state recovery. Disabling them would make the state store unreplicated, leading to data loss after a crash or rebalance, and is not a recommended tuning option.

2. ✅ **B. Configure the RocksDB compression property to snappy to improve write throughput.**  
   **Correct**. Using a lightweight compression algorithm such as snappy reduces CPU usage during writes while still compressing data, which can lower disk I/O and improve overall throughput, especially on high‑throughput workloads.

3. ❌ **C. Reduce the window size in windowed joins to lower latency and memory usage.**  
   **Incorrect**. Shorter windows reduce the amount of state kept per key, which can lower memory consumption and increase responsiveness. However, it can also increase the number of windows that need to be processed, potentially raising overhead, the effect depends on the application semantics.

4. ✅ **D. Increase the number of stream threads (default 1) to match the number of partitions for parallel processing.**  
   **Correct**. Kafka Streams runs tasks (one per input partition of a subtopology) on stream threads, the config is `num.stream.threads`, setting it equal to or slightly higher than the number of topic partitions allows each thread to process a subset of the data in parallel, improving throughput. However, it should not exceed the number of available CPU cores to avoid context‑switch overhead.

5. ❌ **E. Use the materialized-as clause to create multiple state stores for a single topology to improve query performance.**  
   **Incorrect (unsupported by docs, changed from the original key)**. Defining separate state stores allows the application to keep different key/value sets in distinct RocksDB instances, which can reduce contention and enable more efficient compaction. This technique is beneficial when the application needs to expose multiple queryable state tables.

6. ✅ **F. Increase the record cache size (`statestore.cache.max.bytes`) to reduce writes to the state store and downstream traffic.**  
   **Correct (with a caveat)**. A larger cache can reduce writes to the underlying RocksDB, but it also consumes more heap. An excessively large cache can trigger frequent garbage collection pauses and may lead to out‑of‑memory errors. The recommended approach is to use a moderate cache (e.g., 10–15% of available RAM) and tune based on the workload.

</details>

## Question 13 (Application Development):
What is the primary purpose of the Confluent Schema Registry when using Avro SerDes in a Kafka producer/consumer application?

- A. To store and manage Avro schemas, enabling schema evolution and backward/forward compatibility checks.
- B. To provide a graphical UI for monitoring Kafka cluster performance.
- C. To automatically convert JSON payloads to Protobuf format during serialization.
- D. To handle message routing based on partition keys without requiring a custom partitioner.
- E. To encrypt message payloads to ensure data confidentiality during transit.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Confluent Schema Registry’s core function is to act as a central repository for Avro (and other) schemas, assigning each a unique ID that is prefixed to the serialized data. During production, the serializer fetches the schema ID and writes the data according to the schema, during consumption, the deserializer uses the ID to retrieve the correct schema and decode the payload. This mechanism allows safe schema evolution—backward, forward, or full compatibility checks—so that older consumers can read newer data and vice‑versa. Misconceptions often arise because the Registry is sometimes mistakenly thought to provide encryption, UI, or data transformation, but its role is strictly schema management and compatibility enforcement.

Source: book ch. 3 "Serializers/Avro/Schema Registry" (PDF p. 94), https://docs.confluent.io/platform/current/schema-registry/index.html (supports Avro, Protobuf and JSON Schema)

**Detailed explanation of each option:**

1. ✅ **A. To store and manage Avro schemas, enabling schema evolution and backward/forward compatibility checks.**  
   **Correct**. The Schema Registry centralizes Avro schema definitions, assigns unique IDs, and enforces compatibility rules (backward, forward, full) during serialization and deserialization, ensuring that producers and consumers agree on data structure.

2. ❌ **B. To provide a graphical UI for monitoring Kafka cluster performance.**  
   **Incorrect**. While Confluent Control Center offers monitoring, the Schema Registry is focused on schema storage, not performance dashboards.

3. ❌ **C. To automatically convert JSON payloads to Protobuf format during serialization.**  
   **Incorrect**. The Registry is schema-agnostic and does not transform data formats, it simply stores schemas. Format conversion is handled by the application or dedicated connectors.

4. ❌ **D. To handle message routing based on partition keys without requiring a custom partitioner.**  
   **Incorrect**. Partitioning logic is handled by Kafka’s partitioner. The Schema Registry does not influence routing.

5. ❌ **E. To encrypt message payloads to ensure data confidentiality during transit.**  
   **Incorrect**. The Schema Registry does not perform encryption, it only manages schemas. Kafka’s TLS or SASL mechanisms handle security.

</details>

## Question 14 (Observability & Testing):
You are developing a Kafka Streams application that reads records from the topic `orders`, performs a transformation, and writes the results to the topic `orders-transformed`. During unit testing you want to validate the transformation logic without starting a real Kafka broker or cluster. Which utility from the Kafka Streams library should you use to provide the input and capture the output of the topology in memory?

- A. EmbeddedKafkaBroker
- B. MockProcessor
- C. EmbeddedKafkaCluster
- D. KafkaTestClient
- E. TopologyTestDriver

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Unit testing of Kafka Streams should be performed with the `TopologyTestDriver`. It executes the entire stream topology in a lightweight, in‑memory environment, allowing developers to push input records and read output records directly, without any external broker dependencies. This speeds up test cycles and isolates the logic from network or broker failures. Alternatives like `EmbeddedKafkaCluster` or `EmbeddedKafkaBroker` are suited for integration testing, while `MockProcessor` is too granular and requires a surrounding driver. The other options are either non‑existent or not intended for this purpose. Using the correct driver ensures accurate, fast, and deterministic tests of stream logic.

Source: book ch. 14 (PDF p. 441: TopologyTestDriver is the main testing tool), https://kafka.apache.org/43/documentation/streams/developer-guide/testing.html

**Detailed explanation of each option:**

1. ❌ **A. EmbeddedKafkaBroker**  
   **Incorrect**. EmbeddedKafkaBroker is used with the Spring Kafka test framework to spin up a broker for integration tests. It is not part of the Kafka Streams API and does not provide the in‑memory topology execution needed for unit tests.

2. ❌ **B. MockProcessor**  
   **Incorrect**. MockProcessorContext/MockProcessor-style helpers test individual processors in isolation (the old MockProcessorContext is deprecated), they do not run a whole topology. It does not provide the end‑to‑end topology execution needed for unit tests of the full stream.

3. ❌ **C. EmbeddedKafkaCluster**  
   **Incorrect**. EmbeddedKafkaCluster starts an actual Kafka broker and cluster in memory. It is useful for integration tests that involve real network I/O, but it is heavier and unnecessary for pure unit tests of stream logic.

4. ❌ **D. KafkaTestClient**  
   **Incorrect**. KafkaTestClient is not an official class in the Kafka Streams library, it is a fictitious placeholder. Using it would result in a compile‑time error.

5. ✅ **E. TopologyTestDriver**  
   **Correct**. TopologyTestDriver is the official in‑memory test harness for Kafka Streams. It allows you to feed records into the topology and read the produced records directly, without any network or broker overhead. This is the recommended approach for unit‑level validation of stream processing logic.

</details>

## 🚫 Question 15 (Deployment & Ops):
When deploying a Kafka Streams application on Kubernetes with the Confluent Operator, which action ensures that the operator automatically injects the correct bootstrap server configuration into the Streams pod?

- A. Provide the name of the `KafkaCluster` custom resource in the `KafkaStreams` spec, the operator uses this to resolve and inject the bootstrap servers.
- B. Deploy a headless Kubernetes Service for each Streams task, the operator will use the service DNS to discover the broker addresses.
- C. Create a ConfigMap named `kafka-config` containing a key `kafka.bootstrap.servers`, the operator automatically mounts this ConfigMap into the pod.
- D. Add a `bootstrap.servers` entry to the Streams application's `application.yml` file, the operator will read this file and set the environment variable.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Deploying Kafka Streams with the Confluent Operator requires specifying the Kafka cluster to use. The operator reads the `kafkaCluster` field in the `KafkaStreams` custom resource, queries the referenced `KafkaCluster` CR for broker endpoints, and injects the resulting `KAFKA_BOOTSTRAP_SERVERS` environment variable into the pod. This eliminates the need for manual configuration files or secrets. The other options either rely on manual file edits, services, or ConfigMaps that the operator does not process automatically, leading to misconfiguration or failures to connect to the cluster.
FLAG: out of CCDAK scope (Kubernetes/operator deployment), and the premise looks fabricated – Confluent for Kubernetes (CFK) has no `KafkaStreams` or `KafkaCluster` custom resources (its CRs are Kafka, Connect, SchemaRegistry, KafkaTopic, etc.), Streams apps are plain client apps whose bootstrap.servers is set via their own config.

Verified live: the CFK component list contains Kafka, KRaft, Schema Registry, ksqlDB, Connect, Control Center, Flink, REST Proxy, Replicator, KafkaTopic, ClusterLink etc., there is NO `KafkaStreams` or `KafkaCluster` CRD, so the question premise is fabricated
Source: https://docs.confluent.io/operator/current/co-manage-overview.html

**Detailed explanation of each option:**

1. ✅ **A. Provide the name of the `KafkaCluster` custom resource in the `KafkaStreams` spec, the operator uses this to resolve and inject the bootstrap servers.**  
   **Correct**. The operator looks for the `kafkaCluster` field in the `KafkaStreams` custom resource, queries the referenced KafkaCluster, and automatically sets the `KAFKA_BOOTSTRAP_SERVERS` env var in the pod.

2. ❌ **B. Deploy a headless Kubernetes Service for each Streams task, the operator will use the service DNS to discover the broker addresses.**  
   **Incorrect**. While services expose pods, the operator relies on the KafkaCluster reference, not on task services, to obtain broker addresses.

3. ❌ **C. Create a ConfigMap named `kafka-config` containing a key `kafka.bootstrap.servers`, the operator automatically mounts this ConfigMap into the pod.**  
   **Incorrect**. The operator does not automatically mount arbitrary ConfigMaps. Bootstrap servers must be provided via the KafkaCluster reference.

4. ❌ **D. Add a `bootstrap.servers` entry to the Streams application's `application.yml` file, the operator will read this file and set the environment variable.**  
   **Incorrect**. The Confluent Operator does not parse application configuration files, it injects settings via environment variables or secrets. Adding the entry alone will not be honored by the operator.

</details>

## Question 16 (Deployment & Ops):
Which of the following statements correctly describes Kafka's native support for encrypting message payloads on the wire and at rest?

- A. Kafka encrypts only the headers but not the payload when using SASL/SSL.
- B. Kafka natively encrypts message payloads using AES‑256 when TLS is enabled.
- C. Kafka automatically encrypts messages using the broker's file system encryption settings.
- D. Kafka can encrypt message payloads at rest using the built‑in "data‑at‑rest‑encryption" feature in Confluent Platform 7.x.
- E. Kafka does not provide native message payload encryption, encryption must be handled by clients or external tools.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka provides transport‑layer encryption (TLS) and authentication (SASL) to secure data in transit. For data at rest, Confluent Platform relies on storage‑level encryption or external tools, it does not natively encrypt the payload itself. Many developers mistakenly believe TLS protects the payload or that Kafka includes a built‑in at‑rest encryption feature. Understanding this distinction is critical for designing secure Kafka deployments and for selecting appropriate encryption strategies for both transit and storage.

Source: book ch. 11 "Securing Kafka" – Encryption / data at rest / end-to-end encryption (PDF p. 318), https://kafka.apache.org/documentation/#security_ssl

**Detailed explanation of each option:**

1. ❌ **A. Kafka encrypts only the headers but not the payload when using SASL/SSL.**  
   **Incorrect**. SASL/SSL encrypts the entire communication channel, including headers and payload. Kafka does not selectively encrypt headers only.

2. ❌ **B. Kafka natively encrypts message payloads using AES‑256 when TLS is enabled.**  
   **Incorrect**. TLS encrypts the entire transport channel between client and broker, not just the payload. Kafka does not apply AES‑256 to individual records, encryption is applied at the TCP layer.

3. ❌ **C. Kafka automatically encrypts messages using the broker's file system encryption settings.**  
   **Incorrect**. File system encryption is independent of Kafka, Kafka will write data to disk as received. The broker does not automatically apply encryption.

4. ❌ **D. Kafka can encrypt message payloads at rest using the built‑in "data‑at‑rest‑encryption" feature in Confluent Platform 7.x.**  
   **Incorrect**. Confluent Platform does not ship a built‑in per‑topic encryption feature for stored records. Encryption at rest must be provided by the storage system (e.g., LUKS, file system encryption) or external tooling.

5. ✅ **E. Kafka does not provide native message payload encryption, encryption must be handled by clients or external tools.**  
   **Correct**. Kafka’s core platform offers TLS/SASL for transport security and supports encryption at rest via storage‑level mechanisms, but it does not encrypt the payload data itself.

</details>

## Question 17 (Kafka Connect):
In a Kafka Connect distributed cluster, which configuration property determines the number of replicas of the internal Kafka topic that stores connector configurations, and what is the impact of setting it to 1 in a three‑broker cluster?

- A. `config.storage.replication.factor` – it sets how many replicas the config topic has, setting it to 1 means the topic will be stored on a single broker and can be lost if that broker fails.
- B. `config.storage.replication.factor` – but if set to 1, it will cause the connector to fail on startup because Connect requires a replication factor of at least 3.
- C. `config.storage.replication.factor` – but it only applies to standalone mode and has no effect in distributed mode.
- D. `offset.storage.replication.factor` – it defines replication of the offsets topic, setting it to 1 would affect offset durability, not config storage.
- E. `status.storage.replication.factor` – it controls replication of the status topic, setting it to 1 only affects the status topic, not connector configs.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In a distributed Connect cluster, the internal topics—config, status, and offset—must have a replication factor that matches the desired fault tolerance. The property config.storage.replication.factor controls how many replicas of the connector configuration topic are maintained. Setting it to 1 means the topic resides on a single broker, if that broker fails, the topic becomes unavailable and connectors may stop functioning until the broker recovers. This is useful for test environments but not recommended for production. The other options reference either the wrong internal topic or misunderstand the mode in which the property applies. Note: default is 3, it applies to distributed mode (config topic, single partition).

Source: https://kafka.apache.org/documentation/#connectconfigs_config.storage.replication.factor, book ch. 9 (PDF p. 258, Connect internal topics)

**Detailed explanation of each option:**

1. ✅ **A. config.storage.replication.factor – it sets how many replicas the config topic has, setting it to 1 means the topic will be stored on a single broker and can be lost if that broker fails.**  
   **Correct**. This property controls replication of the config topic, a replication factor of 1 reduces fault tolerance.

2. ❌ **B. config.storage.replication.factor – but if set to 1, it will cause the connector to fail on startup because Connect requires a replication factor of at least 3.**  
   **Incorrect**. Connect accepts a replication factor of 1, the topic will be available but with no redundancy.

3. ❌ **C. config.storage.replication.factor – but it only applies to standalone mode and has no effect in distributed mode.**  
   **Incorrect**. The property is valid and used in distributed mode.

4. ❌ **D. offset.storage.replication.factor – it defines replication of the offsets topic, setting it to 1 would affect offset durability, not config storage.**  
   **Incorrect**. This property is unrelated to connector configuration.

5. ❌ **E. status.storage.replication.factor – it controls replication of the status topic, setting it to 1 only affects the status topic, not connector configs.**  
   **Incorrect**. This property applies to the status topic, not the config topic.

</details>

## Question 18 (Application Development):
A production application uses a Kafka producer to send 1 million messages per second to a cluster with 5 brokers and topics configured with 3 replicas.
Which of the following client configuration settings should you tune to maximize throughput while still ensuring message durability and reliability?

- A. `compression.type=gzip`
- B. `max.in.flight.requests.per.connection=5`
- C. `min.insync.replicas=2`
- D. `acks=all`
- E. `linger.ms=0`
- F. `batch.size=1048576 (1 MB)`

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

For high‑throughput Kafka producers that still need durability, the key tuning knobs are batch.size, acks, and compression.type. A larger batch.size lets the producer send more records per request, reducing the per‑record overhead. Setting acks to all guarantees that all replicas acknowledge the write, ensuring durability. Compression reduces the size of each request, improving effective throughput on network‑bound workloads. Options like linger.ms=0 hurt batching (a bigger batch.size only helps together with linger.ms > 0), and min.insync.replicas is a broker/topic setting, not a client one. max.in.flight.requests.per.connection=5 is the default and is safe for ordering with idempotence (default enabled since 3.0).

Source: book ch. 3 (PDF p. 89-90: max.in.flight, idempotence, batch.size, linger.ms, compression.type), https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ✅ **A. compression.type=gzip**  
   **Correct**. Enabling gzip compression reduces the payload size, leading to fewer bytes sent over the network. This can improve throughput, especially on bandwidth‑constrained links, at the cost of additional CPU usage.

2. ❌ **B. max.in.flight.requests.per.connection=5**  
   **Incorrect**. 5 is already the default, with enable.idempotence=true (default since Kafka 3.0) ordering is preserved for up to 5 in-flight requests, so it is not a tuning change.

3. ❌ **C. min.insync.replicas=2**  
   **Incorrect**. This is a broker/topic configuration, not a client (producer) setting, it works with acks=all to require at least two in-sync replicas. The question asks for client settings.

4. ✅ **D. acks=all**  
   **Correct**. Configuring acks to all guarantees that a record is considered written only after all in‑sync replicas have acknowledged it, providing the strongest durability guarantee without affecting throughput directly.

5. ❌ **E. linger.ms=0**  
   **Incorrect**. Setting linger.ms to 0 disables batching, forcing the producer to send records immediately. This reduces latency but also limits throughput because each record is sent in its own network request.

6. ✅ **F. batch.size=1048576**  
   **Correct**. Increasing batch.size to 1 MB allows the producer to accumulate more records before sending them in a single request, which significantly boosts throughput. This is a common tuning knob for high‑volume producers.

</details>

## Question 19 (Observability & Testing):
Which of the following Kafka client or application metrics are available by default in the Java client libraries (Producer and Consumer) and can be used to monitor application health and performance?

- A. producer-completion-rate – the number of record sends completed per second.
- B. consumer-rebalance-rate – the number of consumer rebalances occurring per second.
- C. producer-latency-avg – the average time in milliseconds for a producer request to be acknowledged by the broker.
- D. bytes-consumed-total – the total number of bytes read by a consumer.
- E. request-queue-size – the number of queued requests in the producer's network thread.
- F. records-pushed-total – the total number of records forwarded by a Kafka Streams application.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s Java clients publish metrics via JMX. Of the listed names only `bytes-consumed-total` (consumer fetch metrics) exists. The producer has `request-latency-avg` (not `producer-latency-avg`) and `record-send-rate` (not `producer-completion-rate`), the consumer has `rebalance-rate-per-hour` (not `consumer-rebalance-rate`), `request-queue-size` is a broker metric (RequestQueueSize), not a producer one, `records-pushed-total` is not a Streams metric.

Verified live (answer D confirmed): the page lists request-latency-avg, record-send-rate, bytes-consumed-total, rebalance-rate-per-hour, rebalance-latency-avg, broker RequestQueueSize, it does not list producer-latency-avg, producer-completion-rate, consumer-rebalance-rate.
Source: https://kafka.apache.org/42/operations/monitoring/ . Understanding which metrics are standard allows developers to instrument and alert on critical application behavior without custom instrumentation.

**Detailed explanation of each option:**

1. ❌ **A. producer-completion-rate – the number of record sends completed per second.**  
   **Incorrect**. While there is a `record-send-rate` metric, `producer-completion-rate` is not part of the default metric set.

2. ❌ **B. consumer-rebalance-rate – the number of consumer rebalances occurring per second.**  
   **Incorrect**. The Kafka client does not expose a metric named consumer‑rebalance‑rate. The consumer exposes `rebalance-rate-per-hour`, `rebalance-total` and `rebalance-latency-avg` instead.

3. ❌ **C. producer-latency-avg – the average time in milliseconds for a producer request to be acknowledged by the broker.**  
   **Incorrect**. No such metric, the real one is `request-latency-avg`.

4. ✅ **D. bytes-consumed-total – the total number of bytes read by a consumer.**  
   **Correct**. This is a standard consumer metric that helps gauge throughput and detect bottlenecks in the consumer.

5. ❌ **E. request-queue-size – the number of queued requests in the producer's network thread.**  
   **Incorrect**. `RequestQueueSize` is a broker metric, not a producer client metric.

6. ❌ **F. records-pushed-total – the total number of records forwarded by a Kafka Streams application.**  
   **Incorrect**. `records-pushed-total` is not a Kafka Streams metric (Streams has e.g. `process-rate`, `process-total`, `forward` related and `record-e2e-latency` metrics).

</details>

## 🚫 Question 20 (Deployment & Ops):
You are deploying a Kafka consumer application in a production Kubernetes cluster. Which deployment strategy offers the best combination of fault tolerance, automatic scaling, and clean runtime configuration management for the client, while also supporting dynamic schema evolution with Avro?

- A. Deploy the consumer as a StatefulSet with a persistent volume per replica and a separate ConfigMap for each replica containing unique group.id values to avoid consumer group collisions.
- B. Deploy the consumer as a Deployment with multiple replicas, using a ConfigMap for static configuration and mounting a shared PVC for log retention, with a Horizontal Pod Autoscaler based on CPU usage.
- C. Run the consumer in a Docker Compose file locally with docker-compose.override.yml for environment variables, and rely on the Kafka broker's default topic configuration.
- D. Deploy the consumer as a single pod with its own ConfigMap containing bootstrap servers and topic configuration, and use the Kafka client auto‑create topics feature.
- E. Package the consumer into a Docker image, push it to a container registry, and deploy it with Helm charts that reference a ConfigMap for the bootstrap servers and use init containers to fetch the latest Avro schema from the Schema Registry.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Deploying Kafka clients in Kubernetes is most effective when using immutable container images and declarative Helm charts, as described in Confluent’s Kubernetes Helm documentation (https://docs.confluent.io/platform/current/installation/kubernetes/helm-deployment.html). A ConfigMap centralizes runtime settings like bootstrap servers and client properties, ensuring consistency across replicas and simplifying updates. Init containers can pre‑fetch Avro schemas from the Schema Registry, reducing runtime latency and guaranteeing that consumers have the latest schema definitions (https://docs.confluent.io/platform/current/schema-registry/index.html). This pattern supports horizontal scaling via Deployment replicas, built‑in health checks, and automatic recovery from pod failures, meeting the exam’s requirements for fault tolerance, scalability, and configuration management.
FLAG: out of CCDAK scope (Kubernetes/Helm deployment), also E's init container for fetching schemas is unnecessary because Avro deserializers fetch schemas by ID from the Schema Registry at runtime (and cache them), and E does not mention autoscaling, so the question is weak.

Source: not verifiable (out of scope, 🚫), Schema Registry client behaviour (deserializer fetches schema by ID at runtime) is standard. Related CFK doc checked: https://docs.confluent.io/operator/current/co-manage-overview.html (no client-app CRDs).

**Detailed explanation of each option:**

1. ❌ **A. Deploy the consumer as a StatefulSet with a persistent volume per replica and a separate ConfigMap for each replica containing unique group.id values to avoid consumer group collisions.**  
   **Incorrect**. StatefulSets are intended for stateful workloads that require stable network identities. Kafka consumers are stateless, a StatefulSet adds unnecessary complexity and overhead. Unique group.id values per replica are also unnecessary and can fragment the consumer group.

2. ❌ **B. Deploy the consumer as a Deployment with multiple replicas, using a ConfigMap for static configuration and mounting a shared PVC for log retention, with a Horizontal Pod Autoscaler based on CPU usage.**  
   **Incorrect**. This approach improves scaling and high availability. However, it introduces a shared persistent volume that is unnecessary for stateless consumers and can become a bottleneck. It also does not address schema evolution or dynamic configuration of the Schema Registry.

3. ❌ **C. Run the consumer in a Docker Compose file locally with docker-compose.override.yml for environment variables, and rely on the Kafka broker's default topic configuration.**  
   **Incorrect**. Docker Compose is suitable for local development only. It lacks built‑in orchestration, scaling, or high‑availability features required in production Kubernetes deployments, and it ignores best practices for configuration management.

4. ❌ **D. Deploy the consumer as a single pod with its own ConfigMap containing bootstrap servers and topic configuration, and use the Kafka client auto‑create topics feature.**  
   **Incorrect**. Deploying a single pod eliminates load balancing concerns but provides no high‑availability or scaling. Auto‑creating topics at runtime is risky in production and can lead to inconsistent topic settings. Therefore, this approach is inadequate for fault tolerance or scaling.

5. ✅ **E. Package the consumer into a Docker image, push it to a container registry, and deploy it with Helm charts that reference a ConfigMap for the bootstrap servers and use init containers to fetch the latest Avro schema from the Schema Registry.**  
   **Correct**. This strategy follows Confluent’s recommended best practices for Kubernetes: immutable container images, declarative Helm charts, centralized configuration via ConfigMaps, and init containers for pre‑deployment tasks such as schema retrieval. It supports horizontal scaling, high availability, and dynamic schema evolution.

</details>

## Question 21 (Kafka Connect):
You are deploying a JDBC Sink connector that writes to a PostgreSQL database. The target table has a primary key on 'id'. During load, duplicate records cause a primary key violation and the connector stops. You want the connector to skip duplicate records and continue processing. Which configuration setting(s) should you apply?

- A. Set `errors.tolerance=all` and configure a dead letter queue with `errors.deadletterqueue.topic.name=dlq`.
- B. Set `auto.create=true` and `auto.evolve=true` to allow the connector to create and evolve tables automatically.
- C. Set `max.retries=10` and `retry.backoff.ms=1000` to retry on failures.
- D. Set `batch.size=500` and `max.poll.records=500` to adjust batching behavior.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka Connect, records that violate constraints in a sink cause the connector to fail. The `errors.tolerance` configuration controls this behavior: `none` (default) stops on the first error, while `all` allows the connector to skip the offending record and continue processing. To log the skipped records, a dead letter queue can be set with `errors.deadletterqueue.topic.name`. The other options configure table auto-creation/evolution, retry behavior, or batching and do not address key‑violation errors.
CAVEAT (flawed question): `errors.tolerance` covers only errors in the Connect framework stages (converters, SMTs, key/value deserialization), an SQLException thrown by the JDBC sink's `put()` is not skipped by it, so the connector would still fail. The idiomatic fix for duplicate primary keys is `insert.mode=upsert` with `pk.mode`/`pk.fields`. Since it is not offered, A is only the best available option. For detailed guidance see the official docs: https://docs.confluent.io/platform/current/connectors/connect-jdbc-sink.html and https://docs.confluent.io/platform/current/connectors/connect-connector-config.html.  
Source: https://docs.confluent.io/kafka-connectors/jdbc/current/sink-connector/sink_config_options.html (insert.mode, pk.mode, max.retries, retry.backoff.ms, auto.create, auto.evolve) , https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/ (error handling does not cover put() to the external system)

**Detailed explanation of each option:**

1. ✅ **A. Set `errors.tolerance=all` and configure a dead letter queue with `errors.deadletterqueue.topic.name=dlq`.**  
   **Correct**. Setting `errors.tolerance=all` tells Connect to continue after an error, while the DLQ configuration captures failed records for later inspection.

2. ❌ **B. Set `auto.create=true` and `auto.evolve=true` to allow the connector to create and evolve tables automatically.**  
   **Incorrect**. These are JDBC sink connector properties (create/alter the target table), not Debezium and not error-handling settings. They do not affect duplicate key violations.

3. ❌ **C. Set `max.retries=10` and `retry.backoff.ms=1000` to retry on failures.**  
   **Incorrect**. `max.retries` and `retry.backoff.ms` are real JDBC sink settings, but they apply to transient errors like network timeouts, not to persistent key constraint violations. The connector will still stop after retries are exhausted.

4. ❌ **D. Set `batch.size=500` and `max.poll.records=500` to adjust batching behavior.**  
   **Incorrect**. `batch.size` is a JDBC sink setting, `max.poll.records` is a consumer setting (set in Connect via `consumer.override.`). Neither alters error handling for duplicate keys.

</details>

## Question 22 (Deployment & Ops):
When deploying a Kafka Streams application in a Docker/Kubernetes environment, which of the following practices are 
essential to ensure reliable state management, proper initialization, and seamless scaling?

- A. Set the Streams application to use the changelog topics for state store restoration automatically.
- B. Expose Kafka bootstrap servers through a NodePort service for external access.
- C. Configure the Streams application to use exactly‑once semantics by setting application.id and enable.idempotence.
- D. Use a Kubernetes StatefulSet with Persistent Volume Claims to preserve local state across pod restarts.
- E. Run the Streams application as a single replica pod to reduce resource usage.
- F. Run an init container that creates required Kafka topics and verifies connectivity before the Streams pod starts.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

Deploying Kafka Streams on Docker/Kubernetes requires more than just container images, it demands reliable state persistence, correct initialization, and built‑in scalability. A StatefulSet with Persistent Volume Claims guarantees that local state survives pod rescheduling. An init container that pre‑creates topics ensures the application starts only when its dependencies are ready, preventing runtime failures. Relying on Kafka’s changelog topics for state store restoration allows the Streams app to rebuild state efficiently after a crash or scaling event. These practices are aligned with Confluent’s deployment guidance and are critical for production reliability. References: - Confluent Docs – Deploying Streams in Kubernetes: https://docs.confluent.io/platform/current/streams/deployment.html - Kubernetes StatefulSets: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ - Kafka Streams – State Store and Changelog Topics: https://docs.confluent.io/platform/current/streams/developer-guide/streams-state.html  
Source: https://kafka.apache.org/43/documentation/streams/developer-guide/running-app/ (state restoration from changelog, standby replicas, scaling) , https://kafka.apache.org/43/documentation/streams/architecture/ (state, changelog topics). Note: K8s-specific items (StatefulSet, init container) are deployment practices, not Kafka docs.

**Detailed explanation of each option:**

1. ✅ **A. Set the Streams application to use the changelog topics for state store restoration automatically.**  
   **Correct**. Streams automatically writes state to changelog topics. Configuring this ensures that on restart, the state store can be rebuilt efficiently from Kafka, reducing recovery time.

2. ❌ **B. Expose Kafka bootstrap servers through a NodePort service for external access.**  
   **Incorrect**. Exposing internal Kafka brokers via NodePort is insecure and unnecessary, clients should use a dedicated Kafka service within the cluster or a managed Kafka service.

3. ❌ **C. Configure the Streams application to use exactly‑once semantics by setting application.id and enable.idempotence.**  
   **Incorrect**. Exactly‑once in Kafka Streams is enabled with `processing.guarantee=exactly_once_v2`, `application.id` is unrelated to it and `enable.idempotence` is configured by Streams itself. It is an application setting, not a deployment practice.

4. ✅ **D. Use a Kubernetes StatefulSet with Persistent Volume Claims to preserve local state across pod restarts.**  
   **Correct**. A StatefulSet provides stable network identity and persistent storage for the Streams state store. Without it, local state would be lost on pod rescheduling, leading to unnecessary state restoration overhead.

5. ❌ **E. Run the Streams application as a single replica pod to reduce resource usage.**  
   **Incorrect**. While reducing resources is desirable, a single replica limits fault tolerance and scalability. Deploying multiple replicas improves availability and throughput.

6. ✅ **F. Run an init container that creates required Kafka topics and verifies connectivity before the Streams pod starts.**  
   **Correct**. Using an init container guarantees that the application does not start until its topics exist and connectivity is confirmed, avoiding runtime errors and ensuring idempotent startup.

</details>

## Question 23 (Streams Development):
Which of the following statements correctly describe how Kafka Streams ensures state consistency and fault tolerance in a distributed environment?

- A. The internal changelog topics for state stores use the same replication factor as the source topic.
- B. All stateful operators must be explicitly configured with a Replication Factor > 1 to survive node failures.
- C. The offset commit for stateful operators is handled automatically by the Streams framework.
- D. State stores are automatically sharded across tasks based on the input topic partition assignment.
- E. When a task fails, its state is recovered from the latest snapshot of the local file system.
- F. Kafka Streams stores state in a local RocksDB instance and replicates it to other nodes via internal changelog topics.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, F

**Explanation:**

In a distributed Kafka Streams application, stateful operators maintain local RocksDB stores whose changes are published to internal changelog topics. These topics are replicated across the cluster, providing fault tolerance. Each task handles one partition of each input topic, which naturally partitions the state store. Recovery is achieved by replaying the changelog, not by restoring local snapshots. The replication factor is set per topic, not per operator, and the Streams framework automatically commits offsets after state updates, guaranteeing consistency across restarts. Understanding these mechanisms is essential for designing reliable stream processing applications.  
Source: https://kafka.apache.org/43/documentation/streams/architecture/ (tasks, local state stores, fault tolerance via changelog topics) , https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams/

**Detailed explanation of each option:**

1. ❌ **A. The internal changelog topics for state stores use the same replication factor as the source topic.**  
   **Incorrect**. Changelog topics get the replication factor from the Streams `replication.factor` config (not from the source topic).

2. ❌ **B. All stateful operators must be explicitly configured with a Replication Factor > 1 to survive node failures.**  
   **Incorrect**. Replication factor is a topic-level setting, the framework automatically creates changelog topics with a configurable replication factor, but operators themselves are not individually configured for replication.

3. ✅ **C. The offset commit for stateful operators is handled automatically by the Streams framework.**  
   **Correct**. The framework commits offsets after a batch of records has been processed and the state has been checkpointed, ensuring that processing resumes from a consistent point after a failure.

4. ✅ **D. State stores are automatically sharded across tasks based on the input topic partition assignment.**  
   **Correct**. Each task is responsible for a single partition of every input topic, its local state store is partitioned accordingly. This design enables parallel processing and deterministic state partitioning.

5. ❌ **E. When a task fails, its state is recovered from the latest snapshot of the local file system.**  
   **Incorrect**. Recovery is performed by replaying the internal changelog topic, not by restoring a local file system snapshot.

6. ✅ **F. Kafka Streams stores state in a local RocksDB instance and replicates it to other nodes via internal changelog topics.**  
   **Correct**. The framework writes all stateful operator data to a local RocksDB store and publishes each change to a corresponding changelog topic. Replication of these topics provides durability and allows a new task to rebuild the state from the changelog when needed.

</details>

## Question 24 (Kafka Connect):
In Kafka Connect’s distributed deployment, which configuration parameter controls the maximum number of parallel tasks that a single connector instance can spawn to read or write data?

- A. `num.tasks`
- B. `tasks.max`
- C. `connector.max.tasks`
- D. `max.tasks`
- E. `worker.tasks.max`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The `tasks.max` configuration is a core part of Kafka Connect’s scalability model. It defines the upper bound of task instances a connector may create (default 1, the connector may create fewer), allowing the connector to leverage parallelism across the worker cluster. Setting it too low can become a bottleneck, setting it too high may oversubscribe resources. Understanding `tasks.max` is essential for developers designing source or sink connectors that need to handle high-throughput or high-volume data flows. The other options are either non‑existent or incorrectly named, which would result in default behavior or ignored configurations. For more detail, see the Connect configuration reference: https://docs.confluent.io/platform/current/connect/references/configuration.html  
Source: https://kafka.apache.org/43/documentation/#connectconfigs (tasks.max: "Maximum number of tasks to use for this connector") , book Ch. 9 (Kafka Connect)

**Detailed explanation of each option:**

1. ❌ **A. num.tasks**  
   **Incorrect**. The correct property is `tasks.max`. `num.tasks` is not a recognized Connect configuration and would be ignored.

2. ✅ **B. tasks.max**  
   **Correct**. `tasks.max` is the official connector property that limits how many task instances can run for that connector type across the worker cluster. It directly influences parallelism and load distribution.

3. ❌ **C. connector.max.tasks**  
   **Incorrect**. This property is not part of the Connect configuration namespace and would be ignored by the framework, leading to default behavior.

4. ❌ **D. max.tasks**  
   **Incorrect**. While it might seem plausible, the framework looks for `tasks.max`, using `max.tasks` has no effect and would be treated as an unrecognized configuration.

5. ❌ **E. worker.tasks.max**  
   **Incorrect**. There is no `worker.tasks.max` property in the documented Connect worker configuration.

</details>

## Question 25 (Streams Development):
When scaling a Kafka Streams application across multiple instances, which of the following actions can directly improve overall throughput?

- A. Increase the number of partitions on the input topic.
- B. Enable/enlarge the Kafka Streams record cache by setting `statestore.cache.max.bytes` to a higher value.
- C. Set `retention.ms` to a larger value on the input topic so records stay longer, allowing the application to consume them later.
- D. Increase the `num.stream.threads` configuration to create more processing threads per instance.
- E. Use a GlobalKTable for all joins to reduce data movement across instances.
- F. Set `state.cleanup.delay.ms` to a very low value to keep state stores small.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

In Kafka Streams, throughput and latency are mainly governed by parallelism and efficient state access. Increasing `num.stream.threads` and input topic partitions raise parallelism within and across instances. Enabling the record cache compacts repeated updates for the same key, reducing state store writes and downstream records (higher throughput, note that emission is delayed until commit.interval.ms/cache pressure, so it does not reduce latency). Settings such as retention, GlobalKTable usage, or aggressive cleanup primarily affect durability or memory, not throughput, and can even hurt performance if misused. Mastery of these knobs is essential for scaling Stream topologies to meet high‑throughput demands.  
Verified live: record cache reduces output records (docs example 15 -> 8), config `statestore.cache.max.bytes` with deprecated `cache.max.bytes.buffering`. The stem was narrowed to 'throughput' (cache does not lower latency).
Source: https://kafka.apache.org/42/streams/developer-guide/memory-mgmt/ , https://kafka.apache.org/42/streams/developer-guide/config-streams/

**Detailed explanation of each option:**

1. ✅ **A. Increase the number of partitions on the input topic.**  
   **Correct**. More partitions provide greater parallelism across instances and threads, allowing Kafka Streams to scale horizontally and process records concurrently, which boosts throughput (number of tasks = number of input partitions, caveat: adding partitions to an existing keyed topic changes the key-to-partition mapping).

2. ✅ **B. Enable/enlarge the Kafka Streams record cache by setting `statestore.cache.max.bytes` to a higher value.**  
   **Correct**. The record cache compacts successive updates for the same key before they are written to the state store and forwarded downstream, which reduces RocksDB writes and downstream traffic and so increases throughput (it does not lower latency: output is held until `commit.interval.ms` or cache pressure). Note: `cache.max.bytes.buffering` is deprecated since 3.4 (KIP-770) in favor of `statestore.cache.max.bytes`, weakest of the three marked answers.

3. ❌ **C. Set `retention.ms` to a larger value on the input topic so records stay longer, allowing the application to consume them later.**  
   **Incorrect**. While longer retention preserves data, it does not affect per‑record processing speed or parallelism. This setting is irrelevant for throughput tuning.

4. ✅ **D. Increase the `num.stream.threads` configuration to create more processing threads per instance.**  
   **Correct**. Increasing `num.stream.threads` allows a single JVM to process multiple streams in parallel, thereby improving CPU utilization and overall throughput. It is a common tuning knob for scaling within a single instance.

5. ❌ **E. Use a GlobalKTable for all joins to reduce data movement across instances.**  
   **Incorrect**. GlobalKTables replicate the entire table on every instance, which eliminates shuffling for lookups but can increase memory usage and does not improve throughput for large datasets.

6. ❌ **F. Set `state.cleanup.delay.ms` to a very low value to keep state stores small.**  
   **Incorrect**. Shortening the cleanup delay may reduce disk space but forces frequent compaction and garbage collection, which can actually degrade performance rather than improve it.

</details>

## Question 26 (Deployment & Ops):
In a Confluent Platform deployment, which of the following statements accurately describe how schema evolution is handled by the Schema Registry to ensure seamless producer‑consumer compatibility?

- A. Defining a JSON schema with a `default` value for new fields allows producers to omit the field without breaking consumers.
- B. Changing the logical type of a field (e.g., from `int32` to `int64`) is allowed under `FULL` compatibility but not under `BACKWARD`.
- C. Using the `latest compatible` endpoint of Schema Registry to retrieve the most compatible schema for a given subject.
- D. Deploying Schema Registry with `compatibility` set to `FORWARD` at the cluster level guarantees that consumers can read data written with newer schema.
- E. Enabling `auto.register.schemas=false` in the producer config prevents schema evolution issues.
- F. Setting `schema.registry.schema.compatibility.level=BACKWARD` ensures that a newly registered schema can read data written with the older schema.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** D, F 

**Explanation:**

Schema evolution in Confluent Kafka relies on compatibility levels defined per subject or cluster. Backward compatibility guarantees that new schemas can read data produced with older ones, while forward compatibility ensures older consumers can read data produced with newer schemas. Full compatibility requires both. There is no `latest compatible` endpoint: compatibility is tested with `POST /compatibility/subjects/{subject}/versions/{version}` and the default level is set via `PUT /config`. Defaults in Avro, not JSON Schema, support optional fields during evolution. Configuring compatibility at the cluster level applies a consistent rule across subjects, but the flag `auto.register.schemas=false` only stops automatic registration and does not influence compatibility semantics.  
Verified live: the API reference has POST /compatibility/subjects/{subject}/versions/{version}, POST /compatibility/subjects/{subject}/versions, GET/PUT /config, GET /subjects/{subject}/versions/latest and no 'latest compatible' endpoint (C false). Still unverified: JSON Schema default semantics (A).
Source: https://docs.confluent.io/platform/current/schema-registry/develop/api.html

**Detailed explanation of each option:**

1. ❌ **A. Defining a JSON schema with a `default` value for new fields allows producers to omit the field without breaking consumers.**  
   **Incorrect**. While default values are supported in Avro schemas, JSON Schema defaults are not used by Kafka consumers. Consumers rely on Avro default values or schema evolution rules, not JSON Schema defaults.

2. ❌ **B. Changing the logical type of a field (e.g., from `int32` to `int64`) is allowed under `FULL` compatibility but not under `BACKWARD`.**  
   **Incorrect**. Avro promotion int -> long is allowed under BACKWARD (a new reader schema with `long` can read old `int` data) but not under FORWARD, hence not under FULL, the statement has it reversed.

3. ❌ **C. Using the `latest compatible` endpoint of Schema Registry to retrieve the most compatible schema for a given subject.**  
   **Incorrect**. No such endpoint exists. The Schema Registry API offers `POST /compatibility/subjects/{subject}/versions/{version}` to TEST whether a schema is compatible with a given/latest version, it does not return a 'most compatible' schema.

4. ✅ **D. Deploying Schema Registry with `compatibility` set to `FORWARD` at the cluster level guarantees that consumers can read data written with newer schema.**  
   **Correct**. Forward compatibility ensures that older consumers can deserialize data written with newer schemas, setting it at the cluster level applies this rule globally to all subjects.

5. ❌ **E. Enabling `auto.register.schemas=false` in the producer config prevents schema evolution issues.**  
   **Incorrect**. This flag simply disables automatic schema registration, it does not affect compatibility checks and can actually increase the risk of mismatched schemas if the client does not register the correct schema.

6. ✅ **F. Setting `schema.registry.schema.compatibility.level=BACKWARD` ensures that a newly registered schema can read data written with the older schema.**  
   **Correct**. Backward compatibility means the new schema can read data written with the previous schema(s). Note: the real server property name is `schema.compatibility.level` (env var `SCHEMA_REGISTRY_SCHEMA_COMPATIBILITY_LEVEL`), not `schema.registry.schema.compatibility.level`.

</details>

## Question 27 (Kafka Connect):
Which of the following statements accurately describe core responsibilities and behaviors of Kafka Connect workers and connectors in a distributed deployment?

- A. In distributed mode, Connect workers store connector configurations, source offsets, and connector/task status in three dedicated internal Kafka topics (`config.storage.topic`, `offset.storage.topic`, `status.storage.topic`), allowing any worker to recover state after a failure.
- B. Connect workers support exactly‑once semantics by default without any configuration changes.
- C. The Connect worker automatically commits offsets to Kafka only after all tasks for a connector have completed.
- D. Sink connectors are responsible for serializing data into Kafka format before sending to the target system.
- E. Connectors can be scaled horizontally by adding more workers to the cluster, each worker will automatically pick up tasks based on the cluster metadata.
- F. Connectors are defined by type (source or sink) and are responsible for creating one or more tasks that perform the actual data transfer.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, E, F

**Explanation:**

Kafka Connect’s core design separates the orchestration of data pipelines into workers, connectors, and tasks. Workers host tasks and handle assignment and state persistence via internal topics. Connectors merely provide the logic for source or sink operations, they do not manage offsets or commit behavior, which is task‑level. In distributed mode, configuration and offsets are stored in `__connect-configs` and `__connect-offsets`, allowing any worker to recover. Horizontal scaling is achieved by adding workers that automatically receive task assignments. Misconceptions often arise around offset handling, exactly‑once semantics, and the responsibilities of source versus sink connectors. Understanding these distinctions is essential for building robust, scalable Connect deployments.  
Source: https://kafka.apache.org/43/documentation/#connect_running , DistributedConfig (exactly.once.source.support default disabled) , book Ch. 9 (Kafka Connect)

**Detailed explanation of each option:**

1. ✅ **A. In distributed mode, Connect workers store connector configurations, source offsets, and connector/task status in three dedicated internal Kafka topics.**  
   **Correct**. 

2. ❌ **B. Connect workers support exactly‑once semantics by default without any configuration changes.**  
   **Incorrect**. Exactly‑once for source connectors exists since Kafka 3.3 (KIP-618) but is opt-in: `exactly.once.source.support` defaults to `disabled`. Sink delivery guarantees depend on the connector.

3. ❌ **C. The Connect worker automatically commits offsets to Kafka only after all tasks for a connector have completed.**  
   **Incorrect**. Offsets are committed per task based on the task’s configured commit interval or when the task is shut down, the worker does not wait for all tasks of a connector to finish.

4. ❌ **D. Sink connectors are responsible for serializing data into Kafka format before sending to the target system.**  
   **Incorrect**. Sink connectors consume from Kafka and deserialize records using converters, source connectors serialize data before publishing.

5. ✅ **E. Connectors can be scaled horizontally by adding more workers to the cluster, each worker will automatically pick up tasks based on the cluster metadata.**  
   **Correct**. In distributed mode workers join the Connect group via Kafka's group coordination protocol (no ZooKeeper involved) and tasks are rebalanced across available workers, enabling horizontal scaling.

6. ✅ **F. Connectors are defined by type (source or sink) and are responsible for creating one or more tasks that perform the actual data transfer.**  
   **Correct**. In Kafka Connect each connector declares whether it is a source or sink and the framework splits the work into tasks, the connector provides the task implementation, while the worker runs the tasks.

</details>

## 🚫 Question 28 (Deployment & Ops):
When deploying a Confluent Platform cluster with TLS encryption for both inter‑broker and client communication, which configuration file is primarily responsible for specifying the key store and trust store locations and their passwords?

- A. zookeeper.cfg
- B. kafka-broker-config.yaml
- C. server.properties
- D. broker-config.yml
- E. client.properties

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

TLS for Kafka brokers is configured through properties in server.properties, such as ssl.keystore.location, ssl.truststore.location, and their passwords. These settings enable secure inter-broker and client traffic. While client.properties holds equivalent SSL settings for producers and consumers, it does not affect broker configuration. Confluent Platform’s broker configuration does not use broker-config.yml or kafka-broker-config.yaml for TLS, those files are either nonexistent or are just alternative representations that still reference server.properties. Zookeeper’s configuration is unrelated to broker TLS. Understanding the exact file that governs broker TLS is essential for secure deployment and troubleshooting of encrypted Kafka clusters. For detailed reference, see Apache Kafka SSL docs (https://kafka.apache.org/documentation/#security_ssl) and Confluent’s security guide (https://docs.confluent.io/platform/current/security.html).  
Source: https://kafka.apache.org/43/documentation/#security_ssl (broker ssl.* settings in server.properties). Out of CCDAK scope: configuring/deploying brokers.

**Detailed explanation of each option:**

1. ❌ **A. zookeeper.cfg**  
   **Incorrect**. Zookeeper configuration files are unrelated to Kafka broker TLS settings, they control ZooKeeper node properties.

2. ❌ **B. kafka-broker-config.yaml**  
   **Incorrect**. While Confluent may expose broker settings via YAML for certain tooling, TLS configuration is still read from server.properties by the Kafka broker process.

3. ✅ **C. server.properties**  
   **Correct**. The Kafka broker configuration file server.properties contains SSL properties such as ssl.keystore.location, ssl.keystore.password, ssl.truststore.location, and ssl.truststore.password, which are used to configure TLS for broker communication.

4. ❌ **D. broker-config.yml**  
   **Incorrect**. Confluent Platform does not use a broker-config.yml file for TLS settings, broker properties are defined in server.properties.

5. ❌ **E. client.properties**  
   **Incorrect**. client.properties is used for client applications and contains SSL settings for the client side, but it is not the primary file for broker TLS configuration.

</details>

## Question 29 (Deployment & Ops):
When deploying Kafka clients in a Confluent Platform cluster, which of the following actions are required to ensure secure and reliable operation?

- A. Configure the `security.protocol` property to match the cluster's authentication mechanism (e.g., SASL_SSL or SSL) and supply the appropriate credentials.
- B. Provide a comma‑separated list of broker host:port pairs in the `bootstrap.servers` configuration so the client can discover the cluster topology.
- C. Set the `client.id` property to a unique value per client instance to aid in metrics and tracing.
- D. Use the same consumer `group.id` for all consumers, even when they consume from different partitions of the same topic.
- E. Exclude the `key.serializer` and `value.serializer` properties from the producer configuration because they are optional.
- F. Rely on the default Kafka broker port 9092 for all environments, ignoring any firewall or network ACLs that may block traffic.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Deploying Kafka clients requires proper bootstrap discovery, secure communication, and identification. The bootstrap.servers list lets the client learn the broker topology, security.protocol and its related settings enforce authentication and encryption, and client.id provides a unique traceable identifier for monitoring and debugging. Omitting serializers breaks producer functionality, ignoring network constraints leads to connection failures, and misusing consumer group ids can corrupt load balancing. Mastering these basics ensures reliable, secure, and observable client deployments in Confluent Platform.  
Source: https://kafka.apache.org/43/configuration/producer-configs/ (bootstrap.servers, key/value.serializer required, client.id optional) , https://kafka.apache.org/43/configuration/consumer-configs/ , book Ch. 3-4

**Detailed explanation of each option:**

1. ✅ **A. Configure the security.protocol property to match the cluster's authentication mechanism (e.g., SASL_SSL or SSL) and supply the appropriate credentials.**  
   **Correct**. In a secured Confluent cluster you must set security.protocol and related settings (ssl.truststore, sasl.jaas.config, etc.) to authenticate and encrypt traffic. Failure to do so results in connection refusals. Refer to Confluent security guide (https://docs.confluent.io/platform/current/kafka/security.html).

2. ✅ **B. Provide a comma‑separated list of broker host:port pairs in the bootstrap.servers configuration so the client can discover the cluster topology.**  
   **Correct**. The bootstrap.servers property is mandatory, it allows the client to obtain the full cluster metadata. Without it, the client cannot connect to any broker. See Confluent docs on client configuration (https://docs.confluent.io/platform/current/kafka/clients.html).

3. ✅ **C. Set the client.id property to a unique value per client instance to aid in metrics and tracing.**  
   **Correct**. `client.id` is optional (not strictly required) but strongly recommended: it appears in broker logs, quotas and metrics, which helps monitoring and tracing.

4. ❌ **D. Use the same consumer group.id for all consumers, even when they consume from different partitions of the same topic.**  
   **Incorrect**. Consumers sharing one `group.id` split the topic's partitions among themselves (the normal way to scale one application), but unrelated applications that each need all the data must use distinct `group.id` values. The option is ambiguous, it is not a required practice.

5. ❌ **E. Exclude the key.serializer and value.serializer properties from the producer configuration because they are optional.**  
   **Incorrect**. key.serializer and value.serializer are required for all producers, they define how the record keys and values are converted to bytes. Omitting them causes configuration errors. (Reference: Confluent producer config docs)

6. ❌ **F. Rely on the default Kafka broker port 9092 for all environments, ignoring any firewall or network ACLs that may block traffic.**  
   **Incorrect**. Network configuration is environment‑specific. You must verify that client traffic to broker ports is allowed by firewalls and ACLs, otherwise the client will fail to connect. (See Confluent deployment networking guide)

</details>

## Question 30 (Deployment & Ops):
In a production Confluent Kafka deployment, which of the following statements about message keying and partitioning are true?

- A. When using key‑based routing, the offset of a record is globally unique across the topic, regardless of key.
- B. If multiple producers send the same key concurrently, the broker will merge those records into a single message.
- C. A non‑null key guarantees that all records with the same key will be routed to the same partition, preserving order for those keys.
- D. Message keys are always serialized as strings any other data type will cause a runtime exception.
- E. A custom partitioner that includes the key in its hash function can be configured via the `partitioner.class` setting in producer properties.
- F. If a producer sends records with null keys, the broker will always assign them to partition 0.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, E

**Explanation:**

Kafka guarantees ordering only within a single partition. By providing a non‑null key, the producer’s hash function directs all messages with that key to the same partition, preserving order for that key. Custom partitioners, set via 'partitioner.class', allow more sophisticated routing logic, including key‑based decisions. Null keys are load‑balanced across partitions by default, not sent to a single one. Keys can be any serializable type, the serializer dictates the format. Offsets are per‑partition, not globally unique, and Kafka does not merge records from different producers even if the key is identical. Understanding these nuances is essential for reliable message routing in production deployments.  
Source: book Ch. 3 (Partitions, p. 98 of PDF: null keys and sticky partitioner) , https://kafka.apache.org/43/configuration/producer-configs/#producerconfigs_partitioner.class

**Detailed explanation of each option:**

1. ❌ **A. When using key‑based routing, the offset of a record is globally unique across the topic, regardless of key.**  
   **Incorrect**. Offsets are partition‑level unique identifiers. Even if multiple keys exist, each partition maintains its own sequence of offsets.

2. ❌ **B. If multiple producers send the same key concurrently, the broker will merge those records into a single message.**  
   **Incorrect**. Kafka stores each record separately, concurrent writes with the same key result in distinct records, each with its own offset within the partition.

3. ✅ **C. A non‑null key guarantees that all records with the same key will be routed to the same partition, preserving order for those keys.**  
   **Correct**. Kafka’s default partitioner hashes the key (murmur2) so identical keys go to the same partition, preserving their order, as long as the topic's partition count does not change.

4. ❌ **D. Message keys are always serialized as strings, any other data type will cause a runtime exception.**  
   **Incorrect**. Keys can be any serializable type, the serializer chosen (StringSerializer, IntegerSerializer, AvroSerializer, etc.) determines how the key is encoded. Using a different type is valid as long as the serializer matches.

5. ✅ **E. A custom partitioner that includes the key in its hash function can be configured via the 'partitioner.class' setting in producer properties.**  
   **Correct**. Producers can specify a custom partitioner (a class implementing the `Partitioner` interface) through `partitioner.class`, allowing tailored key‑based routing logic.

6. ❌ **F. If a producer sends records with null keys, the broker will always assign them to partition 0.**  
   **Incorrect**. Partitioning is done by the producer, not the broker. Records with null keys are spread across partitions (sticky partitioning since 2.4: a batch is filled for one partition, then another is chosen, older versions used round‑robin), never always partition 0.

</details>

## Question 31 (Kafka Connect):
Which of the following statements accurately describe core concepts of Kafka Connect?

- A. Kafka Connect guarantees exactly-once delivery semantics by default for all connectors.
- B. Connectors can be configured to use incremental source offsets for incremental data capture.
- C. Connectors are implemented as either source or sink connectors.
- D. Connectors are always deployed as separate processes independent of the Connect workers.
- E. Connectors are stateless components and rely entirely on Kafka topics for state.
- F. Connectors can leverage the Confluent Schema Registry for data validation and schema evolution.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

Kafka Connect is a framework that simplifies data ingestion and extraction between Kafka and external systems. The core concepts include the distinction between source and sink connectors, the ability to use a Schema Registry for schema validation, and the support for incremental offsets to enable fault‑tolerant, resume‑able data capture. Connectors are not standalone processes, they execute within Connect workers and maintain internal state such as offsets. Exactly‑once semantics are not guaranteed out of the box, they require specific configuration and connector support. Understanding these fundamentals is essential for designing robust pipelines and for passing the Confluent Certified Developer exam.  
Source: https://kafka.apache.org/43/documentation/#connect (connectors, tasks, workers, converters, offsets) , book Ch. 9. Note: options B and E are loosely worded but B, C, F remain the best answers.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect guarantees exactly-once delivery semantics by default for all connectors.**  
   **Incorrect**. Exactly-once semantics are optional and depend on the connector implementation and configuration, they are not guaranteed by default.

2. ✅ **B. Connectors can be configured to use incremental source offsets for incremental data capture.**  
   **Correct**. Source connectors support incremental offset strategies (e.g., incremental snapshots, incremental change data capture) to resume from the last processed record.

3. ✅ **C. Connectors are implemented as either source or sink connectors.**  
   **Correct**. Kafka Connect defines two connector types: source connectors pull data from external systems into Kafka, and sink connectors write data from Kafka to external systems.

4. ❌ **D. Connectors are always deployed as separate processes independent of the Connect workers.**  
   **Incorrect**. Connectors run inside Kafka Connect workers, workers can be standalone or distributed. Deploying connectors as separate processes is not required.

5. ❌ **E. Connectors are stateless components and rely entirely on Kafka topics for state.**  
   **Incorrect**. Connectors maintain state such as offsets, task progress, and error handling. Offsets are stored in internal topics or external storage, not via statelessness.

6. ✅ **F. Connectors can leverage the Confluent Schema Registry for data validation and schema evolution.**  
   **Correct**. Many connectors support Schema Registry integration, allowing them to produce or consume Avro, JSON Schema, or Protobuf messages with schema validation.

</details>

## Question 32 (Observability & Testing):
You are troubleshooting a lagging consumer group named `order-processor` on the topic `orders`.
Which of the following Kafka CLI commands are valid for retrieving consumer group lag information, topic metadata, or both?

- A. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor --json
- B. kafka-topics --bootstrap-server localhost:9092 --describe --topic orders
- C. kafka-cluster --bootstrap-server localhost:9092 --describe
- D. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor
- E. kafka-consumer-groups --bootstrap-server localhost:9092 --group order-processor

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

In Kafka observability, consumer lag is a primary metric for diagnosing throughput issues. The kafka-consumer-groups tool, when used with the --describe flag, reports per‑partition committed and log offsets, allowing calculation of lag. kafka-consumer-groups has no --json option. The kafka-topics command with --describe provides topic metadata—partition layout, replicas, and ISR—which is essential for understanding replication lag or partition misconfiguration. Commands missing the --describe flag or referencing non‑existent tools do not yield the required data. Knowing which CLI commands deliver which pieces of information is critical for efficient troubleshooting.  
Source: book Ch. 12 (Consumer Groups, --describe output, p. 342 of PDF) , Kafka source ConsumerGroupCommandOptions (no --json) and ClusterTool

**Detailed explanation of each option:**

1. ❌ **A. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor --json**  
   **Incorrect**. `kafka-consumer-groups.sh` has no `--json` option (unrecognized option error), the `--describe` output is plain text only.

2. ✅ **B. kafka-topics --bootstrap-server localhost:9092 --describe --topic orders**  
   **Correct**. This command shows the topic configuration, partition count, leader, replicas, and ISR information. While it does not show lag directly, it provides metadata useful for troubleshooting.

3. ❌ **C. kafka-cluster --bootstrap-server localhost:9092 --describe**  
   **Incorrect**. A `kafka-cluster` tool exists (subcommands such as cluster-id, unregister, list-endpoints) but it has no `--describe` and gives no lag or topic metadata.

4. ✅ **D. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor**  
   **Correct**. The --describe flag lists the consumer group offsets, committed offsets, and the resulting lag for each partition. This is the standard way to view consumer lag.

5. ❌ **E. kafka-consumer-groups --bootstrap-server localhost:9092 --group order-processor**  
   **Incorrect**. Without an action option (--describe, --list, --reset-offsets, ...) the tool fails with an error and prints no group details.

</details>

## Question 33 (Application Development):
Which single producer configuration setting is **required** to enable transactional messaging and prevent duplicate record delivery when the producer restarts or experiences transient failures?

- A. `max.in.flight.requests.per.connection=5`
- B. `enable.idempotence=true`
- C. `acks=all`
- D. `linger.ms=5`
- E. `transactional.id="my-transaction"`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

To use Kafka’s transactional producer API, the producer must be initialized with a unique transactional.id. This
identifier ties all subsequent transaction operations (init, begin, commit, abort) to the same logical transaction
context. While enable.idempotence=true provides duplicate protection for non‑transactional sends, it is not sufficient
for transactions. Acks=all, max.in.flight.requests.per.connection, and linger.ms affect reliability, ordering, and
batching, but do not enable transaction boundaries. The transactional.id is the sole required configuration for
transactional messaging, ensuring atomic writes and exactly‑once semantics across multiple topics and partitions.  
Source: book Ch. 8 (Transactions, 'Transactional IDs and Fencing', p. 218 of PDF) , https://kafka.apache.org/43/configuration/producer-configs/#producerconfigs_transactional.id. 

**Detailed explanation of each option:**

1. ❌ **A. max.in.flight.requests.per.connection=5**  
   **Incorrect**. This controls how many unacknowledged requests may be in flight per connection. Idempotence/transactions allow up to 5 (the default), it is not what enables transactions.

2. ❌ **B. enable.idempotence=true**  
   **Incorrect**. This guarantees idempotent writes (no duplicates on retries), but it is not enough to start a transaction, which requires a unique `transactional.id` (setting it enables idempotence implicitly).

3. ❌ **C. acks=all**  
   **Incorrect**. While acks=all ensures that the leader acknowledges the write, providing stronger durability, it is not required for enabling transactions. The transaction API works with any acks setting as long as the producer has a transactional.id.

4. ❌ **D. linger.ms=5**  
   **Incorrect**. This delays sending batches to increase throughput. It has no impact on transactional support or duplicate prevention.

5. ✅ **E. transactional.id="my-transaction"**  
   **Correct**. A unique transactional.id is mandatory for the Producer to participate in a transaction. Without it, the producer cannot call initTransactions(), beginTransaction(), sendOffsetsToTransaction(), etc., and transaction boundaries cannot be established.

</details>

## Question 34 (Kafka Fundamentals):
Which of the following statements accurately describes the role of the `min.insync.replicas` configuration in Kafka data replication?

- A. The `min.insync.replicas` setting determines the minimum number of replicas that must acknowledge a write before the producer receives an acknowledgment.
- B. A topic can have a replication factor larger than the number of brokers in the cluster.
- C. Data is replicated synchronously from leader to all replicas regardless of network latency.
- D. If a follower becomes leader due to a leader failure, the new leader starts serving messages only after the broker has rejoined the cluster.
- E. The replication factor defines the number of copies of each partition that are maintained across brokers to provide fault tolerance and determines how many brokers must be online for a partition to be considered available.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka’s replication ensures durability and high availability by maintaining multiple copies of each partition. The replication factor specifies how many replicas exist but does not itself enforce availability guarantees, instead, the `min.insync.replicas` setting dictates how many replicas must be in sync to accept writes, combined with the producer's 'acks' setting. This mechanism protects against data loss during broker failures. Understanding the interplay between replication factor, `min.insync.replicas`, and producer acknowledgments is essential for configuring fault‑tolerant topics. The other statements either misrepresent the replication process or describe conditions that are not required for a follower to assume leadership.  
Source: book Ch. 6 (Reliable Data Delivery: replication, min.insync.replicas, p. 196 of PDF) , https://kafka.apache.org/43/configuration/topic-configs/#topicconfigs_min.insync.replicas

**Detailed explanation of each option:**

1. ✅ **A. The `min.insync.replicas` setting determines the minimum number of replicas that must acknowledge a write before the producer receives an acknowledgment.**  
   **Correct**. With `acks=all`, the leader rejects the write (NotEnoughReplicas) unless at least `min.insync.replicas` replicas (including the leader) are in sync, so a write is acknowledged only after that many replicas have it. It has no effect with acks=0/1.

2. ❌ **B. A topic can have a replication factor larger than the number of brokers in the cluster.**  
   **Incorrect**. The replication factor cannot exceed the total number of brokers in the cluster, otherwise Kafka will not be able to create all replicas.

3. ❌ **C. Data is replicated synchronously from leader to all replicas regardless of network latency.**  
   **Incorrect**. Followers pull data from the leader asynchronously, when the producer gets its ack is controlled by `acks` and `min.insync.replicas`, not by network latency.

4. ❌ **D. If a follower becomes leader due to a leader failure, the new leader starts serving messages only after the broker has rejoined the cluster.**  
   **Incorrect**. When a leader fails, any follower that has caught up with the latest offset can immediately become the new leader and start serving messages, rejoining the cluster is not required for it to take over.

5. ❌ **E. The replication factor defines the number of copies of each partition that are maintained across brokers to provide fault tolerance and determines how many brokers must be online for a partition to be considered available.**  
   **Incorrect**. While the replication factor indicates how many replicas exist, it does not dictate the minimum number of replicas that must be online for the partition to remain available. That behavior is governed by `min.insync.replicas`.

</details>

## Question 35 (Kafka Fundamentals):
Which of the following statements about Kafka data retention are true? (Select all that apply)

- A. A broker‑wide default for `retention.ms` can be overridden by a per‑topic configuration, and the change takes effect only after a broker restart.
- B. Configuring `retention.bytes` to 0 indicates unlimited data retention.
- C. Setting `segment.ms` to a very high value delays segment rollover, which can increase the time before old segments are eligible for deletion by retention policies.
- D. Setting `retention.ms` to -1 on a topic disables all automatic data deletion, effectively retaining data indefinitely.
- E. If both `retention.ms` and `retention.bytes` are configured on a topic, Kafka deletes a segment when either the age or size threshold is met, whichever condition is satisfied first triggers deletion.
- F. When `cleanup.policy` is set to `compact`, the log compaction process removes older duplicate records for the same key, and the topic will never delete older segments regardless of `retention.ms`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, E

**Explanation:**

Kafka’s retention mechanisms combine time‑based and size‑based policies to control log growth. The `retention.ms` property sets the maximum age for segments, while `retention.bytes` limits the total log size, setting either to -1 disables that constraint. Log compaction (`cleanup.policy`=compact) removes duplicate key records but does not exempt segments from the configured retention thresholds. `segment.ms` governs segment rollover frequency, larger values mean fewer, bigger segments and can postpone deletions. Topic‑level configurations override broker defaults immediately, eliminating the need for broker restarts. Understanding these interactions is essential for ensuring data availability and efficient storage usage.  
Source: book Ch. 2 (Configuring Retention by Size and Time, p. 60 of PDF: deletion when either criterion is met) , https://kafka.apache.org/43/configuration/topic-configs/ (`retention.ms`, `retention.bytes`, `segment.ms`, `cleanup.policy`)

**Detailed explanation of each option:**

1. ❌ **A. A broker‑wide default for `retention.ms` can be overridden by a per‑topic configuration, and the change takes effect only after a broker restart.**  
   **Incorrect**. Topic overrides take effect immediately without needing a broker restart.

2. ❌ **B. Configuring `retention.bytes` to 0 indicates unlimited data retention.**  
   **Incorrect**. `retention.bytes` limits the total size of a log. A value of -1 disables size‑based retention, 0 would keep no data, as it limits the log to 0 bytes.

3. ✅ **C. Setting `segment.ms` to a very high value delays segment rollover, which can increase the time before old segments are eligible for deletion by retention policies.**  
   **Correct**. `segment.ms` controls how often a new segment is rolled. Retention deletes only closed segments (the active segment is never deleted), and a segment is eligible only when its newest record is older than `retention.ms`, a very high `segment.ms` therefore delays deletion.

4. ✅ **D. Setting `retention.ms` to -1 on a topic disables all automatic data deletion, effectively retaining data indefinitely.**  
   **Correct**. In Kafka, `retention.ms` controls the maximum age of log segments. A value of -1 disables time‑based retention, meaning segments will not be deleted by age.

5. ✅ **E. If both `retention.ms` and `retention.bytes` are configured on a topic, Kafka deletes a segment when either the age or size threshold is met, whichever condition is satisfied first triggers deletion.**  
   **Correct**. Kafka evaluates both constraints, deletion occurs as soon as one of them is exceeded.

6. ❌ **F. When `cleanup.policy` is set to `compact`, the log compaction process removes older duplicate records for the same key, and the topic will never delete older segments regardless of `retention.ms`.**  
   **Incorrect**. While compaction removes duplicate keys, `retention.ms` (or `retention.bytes`) can still delete whole segments. The statement overstates compaction’s effect.

</details>

## Question 36 (Kafka Fundamentals):
Which of the following mechanisms can be configured to provide transport‑level encryption for client‑to‑broker communication in Apache Kafka?

- A. OAuth 2.0 (SASL/OAUTHBEARER)
- B. SASL/PLAIN authentication
- C. Mutual TLS (client certificates) with `ssl.client.auth=required`
- D. Kerberos GSSAPI (SASL/KRB5)
- E. Access Control Lists (ACLs)
- F. SSL/TLS enabled by setting `ssl.enabled.protocols` and related cipher suites

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, F

**Explanation:**

Kafka offers several security layers. Transport‑level encryption is achieved only with TLS/SSL, configuring `ssl.enabled.protocols` activates this. Mutual TLS extends SSL by requiring client certificates (`ssl.client.auth=required`) and still provides encryption. SASL mechanisms (PLAIN, GSSAPI, OAUTHBEARER) provide authentication but rely on an existing encrypted channel, they do not encrypt traffic by themselves. ACLs and OAuth are higher‑level authorization and token‑based authentication services that do not impact transport encryption. Understanding which features secure the wire is essential for designing compliant Kafka clusters.  
Source: https://kafka.apache.org/43/documentation/#security_overview and #security_ssl , book Ch. 11 (Securing Kafka)

**Detailed explanation of each option:**

1. ❌ **A. OAuth 2.0 (SASL/OAUTHBEARER)**  
   **Incorrect**. OAuth 2.0 supplies authentication tokens, but does not encrypt traffic unless used over SSL/TLS.

2. ❌ **B. SASL/PLAIN authentication**  
   **Incorrect**. SASL/PLAIN provides only authentication (username/password) and does not encrypt traffic, it must be used over an already‑encrypted transport.

3. ✅ **C. Mutual TLS (client certificates) with `ssl.client.auth=required`**  
   **Correct**. Mutual TLS authenticates both sides with certificates while simultaneously encrypting the channel.

4. ❌ **D. Kerberos GSSAPI (SASL/KRB5)**  
   **Incorrect**. GSSAPI provides mutual authentication, but Kafka relies on SSL/TLS for encryption, Kerberos alone does not encrypt the channel.

5. ❌ **E. Access Control Lists (ACLs)**  
   **Incorrect**. ACLs enforce authorization once a connection is established, they do not provide encryption.

6. ✅ **F. SSL/TLS enabled by setting `ssl.enabled.protocols` and related cipher suites**  
   **Correct**. SSL/TLS encrypts the entire TCP connection between client and broker, protecting payloads and headers.

</details>

## Question 37 (Observability & Testing):
In a Kafka Streams application that uses the default metrics reporter, which of the following application‑level metrics are automatically emitted and exposed via JMX? (Select all that apply)

- A. max-thread-idle-time – the maximum idle time of any Streams worker thread
- B. record-processing-latency-avg – the average time between record consumption and forwarding
- C. bytes-consumed-rate – the rate of bytes consumed per second by the Streams consumer
- D. stream-task-lag – the number of records waiting in a task’s input queue
- E. jvm-heap-used – the amount of heap memory currently used by the JVM
- F. records-consumed-rate – the rate at which the Streams consumer pulls records from Kafka

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, F

**Explanation:**

A Kafka Streams instance exposes, via JMX/KafkaStreams#metrics(), its own Streams metrics (thread, task, processor, state-store, record-cache level) plus the metrics of its embedded producer, consumer and admin clients. `bytes-consumed-rate` and `records-consumed-rate` are consumer fetch metrics of the embedded consumer and are therefore exposed. The names `record-processing-latency-avg`, `stream-task-lag` and `max-thread-idle-time` do not exist (the closest real Streams metrics are `process-latency-avg`, `process-rate`, `record-e2e-latency-avg`, consumer lag is `records-lag-max`), and JVM metrics are not Streams metrics.  
Verified live (answer C, F confirmed): the page says "A Kafka Streams instance contains all the producer and consumer metrics as well as additional metrics specific to Streams", lists bytes-consumed-rate and records-consumed-rate under consumer-fetch-manager-metrics, and thread-level metrics commit/poll/process/punctuate-latency-*, no stream-task-lag, max-thread-idle-time or record-processing-latency-avg.
Source: https://kafka.apache.org/42/operations/monitoring/

**Detailed explanation of each option:**

1. ❌ **A. max-thread-idle-time – the maximum idle time of any Streams worker thread**  
   **Incorrect**. Streams does not expose a metric with this name, thread‑pool metrics are not reported by default.

2. ❌ **B. record-processing-latency-avg – the average time between record consumption and forwarding**  
   **Incorrect**. No Streams metric has this name, the closest real ones are `process-latency-avg`/`process-latency-max` (task/thread level).

3. ✅ **C. bytes-consumed-rate – the rate of bytes consumed per second by the Streams consumer**  
   **Correct**. An embedded consumer metric (consumer-fetch-manager-metrics) that Streams exposes through its metrics registry.

4. ❌ **D. stream-task-lag – the number of records waiting in a task’s input queue**  
   **Incorrect**. No Streams metric named `stream-task-lag` exists, lag is visible through the consumer metric `records-lag-max`/`records-lag`.

5. ❌ **E. jvm-heap-used – the amount of heap memory currently used by the JVM**  
   **Incorrect**. This is a JVM JMX metric, not a Kafka Streams application metric.

6. ✅ **F. records-consumed-rate – the rate at which the Streams consumer pulls records from Kafka**  
   **Correct**. An embedded consumer metric (consumer-fetch-manager-metrics, `records-consumed-rate`) exposed by the Streams client together with its own Streams metrics.

</details>

## Question 38 (Kafka Connect):
Which of the following statements accurately describe how Kafka Connect operates in Distributed mode?

- A. Connect Distributed mode supports exactly‑once semantics by default for source connectors.
- B. Connect Distributed mode stores connector offsets in the internal topic configured via `offset.storage.topic`
- C. Connect Distributed mode requires that the Kafka cluster be a Confluent Platform cluster, not plain Apache Kafka.
- D. Connect Distributed mode uses the "__consumer_offsets" internal topic to store connector status.
- E. Changing a connector's configuration requires stopping the worker, editing the config file, and restarting the worker.
- F. Each worker in a Connect Distributed cluster can host multiple connector tasks, and tasks are automatically balanced across workers.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, F

**Explanation:**

In Distributed mode, source offsets are persisted in a dedicated Kafka topic (`offset.storage.topic`, often named connect-offsets), connector/task configs in `config.storage.topic` and status in `status.storage.topic`, so workers share state and can recover from failures.
Workers can run any number of tasks and the framework rebalances tasks across workers. Connect runs on plain Apache Kafka. Config changes are made via the REST API, no worker restart needed. Exactly‑once for source connectors exists since Kafka 3.3 (KIP-618) but is opt-in (`exactly.once.source.support`, default disabled).  
Source: https://kafka.apache.org/43/documentation/#connectconfigs (offset.storage.topic, config.storage.topic, status.storage.topic, exactly.once.source.support) , book Ch. 9

**Detailed explanation of each option:**

1. ❌ **A. Connect Distributed mode supports exactly‑once semantics by default for source connectors.**  
   **Incorrect**. Exactly‑once support for source connectors (KIP-618, Kafka 3.3+) is opt-in: `exactly.once.source.support` defaults to `disabled`.

2. ✅ **B. Connect Distributed mode stores connector offsets in a special Kafka topic named "__connect-offsets".**  
   **Correct**. Source connector offsets are stored in the internal topic configured via `offset.storage.topic` (commonly named connect-offsets/`__connect-offsets`), status is stored in a separate topic (`status.storage.topic`).

3. ❌ **C. Connect Distributed mode requires that the Kafka cluster be a Confluent Platform cluster, not plain Apache Kafka.**  
   **Incorrect**. Kafka Connect can run on any standard Apache Kafka cluster, Confluent Platform adds additional features but is not a prerequisite.

4. ❌ **D. Connect Distributed mode uses the "__consumer_offsets" internal topic to store connector status.**  
   **Incorrect**. `__consumer_offsets` stores consumer group offsets (including those of sink tasks). Connector status is stored in the topic set by `status.storage.topic`.

5. ❌ **E. Changing a connector's configuration requires stopping the worker, editing the config file, and restarting the worker.**  
   **Incorrect**. Connector configurations can be updated dynamically via the Connect REST API without restarting workers.

6. ✅ **F. Each worker in a Connect Distributed cluster can host multiple connector tasks, and tasks are automatically balanced across workers.**  
   **Correct**. Workers spawn tasks based on connector configuration and the Connect framework distributes them evenly to achieve load balancing.

</details>

## Question 39 (Streams Development):
Which of the following statements about Kafka Streams application writing are true?

- A. A KTable aggregation (`groupBy(...).aggregate/count`) is a changelog‑enabled stateful transformation, and `groupBy` on a KTable always causes data re-partitioning.
- B. GlobalKTable is materialized per instance and does not produce changelog topics.
- C. Each source node reads from a topic partition assignment is round‑robin.
- D. Suppress operator cannot be used on aggregations that emit intermediate results.
- E. A state store can be defined with any arbitrary name but must be the same across all instances to allow recovery.
- F. A KStream-foreach always writes to a sink topic automatically.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

In Kafka Streams, stateful operators such as KTable joins maintain a local state store and write a changelog topic to enable fault tolerance. When keys differ across join partners, Streams automatically inserts a repartition topic to align keys. GlobalKTable, unlike a normal KTable, is replicated on every instance and therefore has no changelog. The foreach operator is a terminal operation that performs side‑effects but does not produce records. Suppress is intended to hide intermediate aggregation results, making it useful for windowed aggregations. Finally, store names must be consistent across instances to enable proper state recovery from changelog topics. These concepts are essential for designing robust, fault‑tolerant stream processing applications.

Source: book ch. 14 "Kafka Streams" (DSL, GlobalKTable, state stores), https://kafka.apache.org/42/streams/developer-guide/dsl-api/ (groupBy causes re-partitioning, GlobalKTable has no changelog), https://docs.confluent.io/current/streams/developer-guide.html

**Detailed explanation of each option:**

1. ✅ **A. A KTable aggregation (`groupBy(...).aggregate/count`) is a changelog‑enabled stateful transformation, and `groupBy` on a KTable always causes data re-partitioning.**  
   **Correct**. DSL docs: "groupBy always causes data re-partitioning", aggregations use a changelog-backed store. (The original wording about KTable joins was wrong: KTable-KTable joins need co-partitioned inputs and Streams does not repartition for them, foreign-key joins handle co-partitioning internally. The option was reworded.)

2. ✅ **B. GlobalKTable is materialized per instance and does not produce changelog topics.**  
   **Correct**. True. GlobalKTable keeps a full copy of the source topic on every instance, it is not partitioned and therefore does not emit a changelog topic. It is refreshed by reading the source topic fully during startup or on change events.

3. ❌ **C. Each source node reads from a topic, partition assignment is round‑robin.**  
   **Incorrect**. False. Kafka Streams assigns topic partitions to stream tasks based on the group coordinator’s assignment algorithm, not a round‑robin strategy. Each task owns a subset of partitions, which can be imbalanced depending on the cluster configuration.

4. ❌ **D. Suppress operator cannot be used on aggregations that emit intermediate results.**  
   **Incorrect**. False. Suppress can be applied to aggregations (e.g., windowed aggregations) to suppress intermediate updates until the window closes, allowing downstream operators to receive only the final result.

5. ✅ **E. A state store can be defined with any arbitrary name but must be the same across all instances to allow recovery.**  
   **Correct**. True. The store name is used to locate the store’s backing changelog topic. All instances must use the same name for a given logical store so that state can be recovered from the changelog during restarts.

6. ❌ **F. A KStream-foreach always writes to a sink topic automatically.**  
   **Incorrect**. False. The foreach operator performs an action for each record (e.g., logging or external call) but does not emit to a Kafka topic. To write to a topic, the stream must be sent to a sink node with to().

</details>

## Question 40 (Kafka Connect):
A Confluent cluster is configured to use TLS encryption and SASL (`security.protocol=SASL_SSL`) with the PLAIN mechanism for client authentication.
A Kafka Connect worker must be configured to communicate with this cluster. Which single configuration property is mandatory on the worker to provide the 
JAAS credentials that the PLAIN mechanism requires?

- A. `sasl.mechanism`
- B. `sasl.jaas.config`
- C. `ssl.truststore.location`
- D. `security.protocol`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In a secured Kafka Connect environment, the worker uses the same client configuration as any Kafka client. When the cluster requires SASL authentication (here SASL_SSL, i.e. SASL over TLS), the worker must supply JAAS credentials through the `sasl.jaas.config` property, which contains the username and password. Although other properties such as `security.protocol`, `sasl.mechanism`, and TLS truststore settings are necessary for connectivity, only `sasl.jaas.config` directly provides the authentication information that the PLAIN mechanism consumes. 
Note: SASL_PLAINTEXT means no TLS. With TLS the protocol is SASL_SSL. The worker's own `sasl.jaas.config` covers its group/config/offset/status clients, while task clients need the `producer.`/`consumer.`/`admin.` prefixed variants. Misconfiguring this property results in authentication failures, whereas omitting transport or TLS settings would cause network or handshake errors. This distinction is critical for developers building production-grade Connect workers.  
Source: https://kafka.apache.org/43/documentation/#security_sasl_plain , https://docs.confluent.io/platform/current/connect/security.html

**Detailed explanation of each option:**

1. ❌ **A. `sasl.mechanism`**  
   **Incorrect**. This property specifies the SASL mechanism (e.g., PLAIN) but, by itself, does not provide the username/password required for authentication.

2. ✅ **B. `sasl.jaas.config`**  
   **Correct**. This property supplies the JAAS configuration string that contains the username and password for SASL/PLAIN. Without it the worker cannot authenticate to the broker.

3. ❌ **C. `ssl.truststore.location`**  
   **Incorrect**. This property points to the truststore for TLS verification, but it does not carry the JAAS credentials needed for SASL/PLAIN.

4. ❌ **D. `security.protocol`**  
   **Incorrect**. While this property (here SASL_SSL) must be set, it only specifies the transport protocol and does not provide authentication credentials.

</details>

## Question 41 (Streams Development):
Which of the following mechanisms does Kafka Streams provide to ensure fault tolerance and consistency of stateful stream processing applications in a distributed environment?

- A. Automatic repartitioning of streams based on key changes to balance load
- B. State store restoration from changelog topics upon restart
- C. Kafka Streams tasks are distributed via the consumer group protocol, allowing load balancing and rebalancing
- D. Exactly-once semantics via idempotent producers
- E. Global tables are replicated across all instances for consistent state
- F. RocksDB checkpointing to allow recovery from crashes

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

Kafka Streams guarantees fault tolerance for stateful processing through three intertwined mechanisms: (1) every local state store has a corresponding changelog topic, enabling state restoration on restart or reassignment, (2) RocksDB checkpoints provide an additional local recovery point, and (3) tasks are distributed as consumer‑group members, so the protocol automatically rebalances tasks when a node fails. These features together ensure that, even after a crash, the application can resume with its exact state and correct results. EOS, while useful for eliminating duplicate writes, does not recover state, and GlobalKTables or repartitioning are for data sharing and load balancing rather than fault tolerance. Note: the RocksDB "checkpoint" is a local `.checkpoint` file holding the changelog offsets up to which the store is already persisted on disk, so after a clean restart only the missing tail of the changelog has to be replayed (it is an optimization on top of the changelog, not a replacement for it).

Source: Kafka Streams architecture/fault tolerance - https://kafka.apache.org/documentation/streams/architecture (sections "Fault Tolerance", "State"), Kafka: The Definitive Guide 2nd ed., ch. 14 (Stream Processing - local state, rebalancing, changelog).

**Detailed explanation of each option:**

1. ❌ **A. Automatic repartitioning of streams based on key changes to balance load**  
   **Incorrect**. Streams may create a repartition topic when the key changes to enable shuffling. Repartitioning improves load balancing but does not directly provide fault tolerance or state recovery.

2. ✅ **B. State store restoration from changelog topics upon restart**  
   **Correct**. Kafka Streams backs every local state store with a changelog topic. When an instance restarts or a task is reassigned, the store is rebuilt by replaying the changelog, ensuring exact recovery of state. This is a core fault‑tolerance feature of Streams.

3. ✅ **C. Kafka Streams tasks are distributed via the consumer group protocol, allowing load balancing and rebalancing**  
   **Correct**. Each Streams task behaves as a member of a consumer group. When a task fails or a node leaves, the group protocol reassigns tasks to other members, ensuring continuous processing. This dynamic rebalancing is a key fault‑tolerance feature.

4. ❌ **D. Exactly-once semantics via idempotent producers**  
   **Incorrect**. Exactly-once semantics (EOS) is a property of Kafka producers and consumers that guarantees no duplicate records are written to a topic. While Streams can enable EOS for its output topics, EOS itself does not restore or preserve stateful local stores on failure. Thus, it is not a dedicated fault‑tolerance mechanism for stateful stream processing.

5. ❌ **E. Global tables are replicated across all instances for consistent state**  
   **Incorrect**. A GlobalKTable loads the entire topic into every instance, providing a read‑only, consistent view. However, this is not a fault‑tolerance mechanism for stateful processing, it is a design choice for read‑only data sharing.

6. ✅ **F. RocksDB checkpointing to allow recovery from crashes**  
   **Correct**. State stores backed by RocksDB are checkpointed to disk. On failure, the store can be restored from the checkpoint and the changelog, providing durable state. This is a built‑in fault‑tolerance feature.

</details>

## Question 42 (Streams Development):
In a Kafka Streams application that aggregates data using a KTable, which configuration and practice combination is required to achieve **exactly‑once** output semantics across all stateful operations?

- A. Increase the replication factor of the input topics to 3.
- B. Set `processing.guarantee=exactly_once_v2`, enable the idempotent producer, and use a `commit.interval.ms` that is not too large, so that state stores and output records are committed atomically.
- C. Assign a unique `application.id` and rely on the default Kafka Streams settings.
- D. Repartition the stream before aggregation and disable the internal caching (`cache.max.bytes.buffering=0`).
- E. Use a global KTable and store the aggregation in a compacted topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Exactly‑once output in Kafka Streams is achieved by enabling transactional support via `processing.guarantee=exactly_once_v2`. This setting turns on the idempotent producer and uses the Kafka Transactions API to atomically commit state store updates and outgoing records. The idempotent producer is a prerequisite for the transaction. A suitable `commit.interval.ms` ensures that the transaction boundaries align with the logical processing windows. Merely setting a unique `application.id`, repartitioning, changing replication factors, or using a global KTable does not provide the atomicity required for exactly‑once semantics. These options affect isolation or throughput but not the transactional guarantees. (Note: `cache.max.bytes.buffering` is deprecated in favour of `statestore.cache.max.bytes`, under EOS the default `commit.interval.ms` is 100 ms instead of 30 s.)

Source: https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (processing.guarantee), Kafka: The Definitive Guide 2nd ed., ch. 8 (Exactly Once Semantics) and ch. 14.

**Detailed explanation of each option:**

1. ❌ **A. Increase the replication factor of the input topics to 3.**  
   **Incorrect**. Higher replication provides fault tolerance but does not affect the output semantics of a Kafka Streams application. Exactly‑once semantics require transactional support, not replication.

2. ✅ **B. Set `processing.guarantee=exactly_once_v2`, enable the idempotent producer, and use a `commit.interval.ms` that is not too large, so that state stores and output records are committed atomically.**  
   **Correct**. This is the correct combination. The `exactly_once_v2` guarantee turns on the Kafka Streams transactional producer, the idempotent producer, and ensures that both state store updates and output records are written as a single transaction. A reasonable `commit.interval.ms` (or 0 for immediate commits) guarantees the transaction boundaries align with state changes.

3. ❌ **C. Assign a unique `application.id` and rely on the default Kafka Streams settings.**  
   **Incorrect**. A unique application id isolates the instance but does not enable exactly‑once semantics, the default `processing.guarantee` is `at_least_once`.

4. ❌ **D. Repartition the stream before aggregation and disable the internal caching (`cache.max.bytes.buffering=0`).**  
   **Incorrect**. Repartitioning or disabling caching improves throughput but does not provide exactly‑once guarantees. The semantics are still at‑least‑once unless the guarantee is explicitly set.

5. ❌ **E. Use a global KTable and store the aggregation in a compacted topic.**  
   **Incorrect**. A global KTable can materialize state but does not enforce exactly‑once semantics by itself. The guarantee must be configured at the Streams application level.

</details>

## Question 43 (Streams Development):
In a Kafka Streams application, which of the following statements correctly describe best practices or guarantees related to application configuration and deployment?

- A. Setting `commit.interval.ms` to a very low value ensures that the application state is always up-to-date in case of a crash.
- B. Enabling `processing.guarantee` to `exactly_once_v2` guarantees that each record is processed exactly once even in the presence of failures.
- C. Setting `application.id` to a unique value for each instance is required to avoid duplicate consumer group metadata.
- D. Using the `state.dir` configuration to a local file system directory ensures fault tolerance across restarts.
- E. Registering a GlobalKTable via `builder.globalTable()` ensures that each instance of the Streams application receives the full table materialized locally for efficient join operations.
- F. Registering a state store with the `Stores.keyValueStoreBuilder` automatically creates a changelog topic that is replicated based on `replication.factor`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, F

**Explanation:**

Kafka Streams relies on a combination of configuration properties and API choices to achieve fault tolerance and exactly‑once semantics. Setting `processing.guarantee` to an exactly-once mode activates Kafka transactions, which guarantees that each input record is processed and output is written atomically (option B, note that in current Kafka the value is `exactly_once_v2` - the old `exactly_once` value was deprecated and removed in 4.0, so the option is correct conceptually but its wording is dated). State stores created with a `Stores.keyValueStoreBuilder` and added to the topology have logging enabled by default, so a changelog topic is created automatically. GlobalKTables replicate the full reference data to every instance, allowing fast local joins (option E). Misconceptions often arise around `application.id` (it must be shared among instances), `state.dir` (local persistence alone does not provide fault tolerance), or `commit.interval.ms` (a low value trades performance for latency but does not ensure state is always current). Understanding these concepts is essential for designing resilient Streams applications.

Source: https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html,
https://kafka.apache.org/documentation/streams/developer-guide/processor-api.html (state store logging),
https://kafka.apache.org/documentation/streams/architecture, Kafka: The Definitive Guide 2nd ed. ch. 14 "Kafka Streams".

**Detailed explanation of each option:**

1. ❌ **A. Setting `commit.interval.ms` to a very low value ensures that the application state is always up-to-date in case of a crash.**  
   **Incorrect**. `commit.interval.ms` controls how often the application commits offsets and state. A very low value increases latency and CPU overhead, it does not guarantee the state is always up-to-date, as state updates may still be in the changelog but not yet committed.

2. ✅ **B. Enabling `processing.guarantee` to `exactly_once_v2` guarantees that each record is processed exactly once even in the presence of failures.**  
   **Correct**. Setting `processing.guarantee` to an exactly-once mode (today `exactly_once_v2`, plain `exactly_once` was removed in Kafka 4.0) enables transactional processing, ensuring each input record is processed once and output records are written atomically. It requires Kafka to be configured with transactions and a transactional producer.

3. ❌ **C. Setting `application.id` to a unique value for each instance is required to avoid duplicate consumer group metadata.**  
   **Incorrect**. `application.id` identifies a logical Streams application and is shared by all instances that should participate in the same processing group. Using a unique ID for each instance defeats load balancing and rebalancing, it is not a requirement for avoiding duplicate metadata.

4. ❌ **D. Using the `state.dir` configuration to a local file system directory ensures fault tolerance across restarts.**  
   **Incorrect**. `state.dir` specifies where local state stores are materialized. While it persists state locally, fault tolerance relies on Kafka changelog topics that are replicated across the cluster. A local directory alone does not provide fault tolerance.

5. ✅ **E. Registering a GlobalKTable via `builder.globalTable()` ensures that each instance of the Streams application receives the full table materialized locally for efficient join operations.**  
   **Correct**. A GlobalKTable is replicated to every Streams instance. Each instance has a local copy of the full table, enabling efficient joins without needing a repartitioned topic. This is a correct statement.

6. ✅ **F. Registering a state store with the `Stores.keyValueStoreBuilder` automatically creates a changelog topic that is replicated based on `replication.factor`.**  
   **Correct**. When a state store is registered, Streams creates a corresponding changelog topic (logging is enabled by default) whose replication factor is set by the Streams config `replication.factor` (in recent versions -1 = broker default). This ensures state changes are replicated for fault tolerance.

</details>

## Question 44 (Application Development):
Which of the following serialization formats is NOT supported by Confluent Schema Registry for automatic schema compatibility checks?

- A. JSON Schema
- B. XML Schema
- C. MessagePack
- D. Protocol Buffers (Protobuf)
- E. Avro

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

Confluent Schema Registry focuses on three primary wire formats: Avro, Protocol Buffers, and JSON Schema. These formats are registered in the registry, and the registry automatically performs compatibility checks (backward, forward, full) when new schemas are added. XML Schema and MessagePack are not among the supported formats, developers would need custom serializers and would lose the automatic compatibility feature. Understanding which formats the registry supports is critical for designing robust, schema‑driven Kafka applications.

Verified live (answer B, C confirmed): "Schema Registry supports Protocol Buffers and JSON Schema along with Avro, the original default format", each with own compatibility rules.
Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/index.html

**Detailed explanation of each option:**

1. ❌ **A. JSON Schema**  
   **Incorrect**. Supported. Schema Registry can register JSON Schema definitions and validate compatibility automatically.

2. ✅ **B. XML Schema**  
   **Correct**. Not supported. Schema Registry does not provide native support for XML Schema, nor does it automatically track or validate XML schemas.

3. ✅ **C. MessagePack**  
   **Correct**. Not supported. While MessagePack can be used with Kafka, it requires a custom serde, the registry does not provide native compatibility checks.

4. ❌ **D. Protocol Buffers (Protobuf)**  
   **Incorrect**. Supported. Schema Registry offers a Protobuf serde that tracks schema IDs and enforces compatibility rules.

5. ❌ **E. Avro**  
   **Incorrect**. Supported. Schema Registry provides native support for Avro, including automatic compatibility evaluation (backward, forward, full).

</details>

## Question 45 (Deployment & Ops):
In a production Kafka environment that uses Avro serialization and Confluent Schema Registry, which of the following statements correctly describe valid schema evolution practices that will not cause a compatibility error when a new schema version is registered?

- A. Setting the schema registry compatibility level to `FORWARD` ensures that older producers cannot produce messages that older consumers can read.
- B. Setting the schema registry compatibility level to `BACKWARD` allows producers with a new schema to write records that older consumers (using the old schema) can still read.
- C. Removing an existing field breaks backward compatibility, but the operation will succeed if the compatibility level is set to `NONE`.
- D. Changing the type of an existing field from `int` to `long` is considered compatible by Confluent Schema Registry.
- E. Adding a new optional field that includes a default value preserves backward compatibility.
- F. The `--auto-register` flag in the schema registry UI automatically registers new fields as required when a schema is updated.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, E

**Explanation:**

Schema evolution in Confluent Kafka relies on compatibility settings that determine whether a new schema version can coexist with older ones. BACKWARD (the default) means consumers using the NEW schema can read data written with the OLD schema (so you may delete fields and add optional fields with defaults, upgrade consumers first). FORWARD means consumers using the OLD schema can read data written with the NEW schema (you may add fields and delete optional fields, upgrade producers first). So option B is wrong - it describes FORWARD, not BACKWARD. Optional fields with defaults (E), widening numeric types such as int to long (D, Avro type promotion) and disabling compatibility checks (NONE, any change, e.g. removing a field, is accepted) are valid. Caveat on C: the premise "removing a field breaks backward compatibility" is inaccurate (removing a field is actually BACKWARD-compatible, it breaks FORWARD compatibility unless the field had a default), but the conclusion (succeeds under NONE) is true, and it is the best third choice.

Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html (compatibility types table, Avro), Kafka: The Definitive Guide 2nd ed., ch. 3 (Schema Registry, schema evolution).

**Detailed explanation of each option:**

1. ❌ **A. Setting the schema registry compatibility level to "FORWARD" ensures that older producers cannot produce messages that older consumers can read.**  
   **Incorrect**. FORWARD means data written with the new schema can be read by consumers using the previous schema. It does not stop older producers' messages from being readable by older consumers.

2. ❌ **B. Setting the schema registry compatibility level to "BACKWARD" allows producers with a new schema to write records that older consumers (using the old schema) can still read.**  
   **Incorrect**. That is FORWARD compatibility. BACKWARD means consumers with the NEW schema can read data written with the OLD schema.

3. ✅ **C. Removing an existing field breaks backward compatibility, but the operation will succeed if the compatibility level is set to "NONE".**  
   **Correct** (with a caveat). With compatibility level NONE the registry does not enforce any compatibility checks, so field removal is accepted. The first half of the sentence is imprecise: removing a field is BACKWARD-compatible (breaks FORWARD unless it had a default).

4. ✅ **D. Changing the type of an existing field from "int" to "long" is considered compatible by Confluent Schema Registry.**  
   **Correct**. In Avro, widening an integer type to a long is a safe upcast, and Schema Registry marks it as compatible.

5. ✅ **E. Adding a new optional field that includes a default value preserves backward compatibility.**  
   **Correct**. New fields with default values are considered optional for readers using older schemas, so backward compatibility is maintained.

6. ❌ **F. The "--auto-register" flag in the schema registry UI automatically registers new fields as required when a schema is updated.**  
   **Incorrect**. There is no such flag in a "schema registry UI", automatic registration is the serializer setting `auto.register.schemas` (default true) and it never changes field requirement semantics.

</details>

## Question 46 (Observability & Testing):
A Kafka consumer application is intermittently throwing a `SerializationException` while processing records from a topic that uses Avro serialization. Which action will most effectively allow you to identify the problematic record(s) and keep the consumer running without downtime?

- A. Increase the `fetch.max.bytes` configuration so that the consumer retrieves larger batches, hoping that a full record will avoid partial deserialization failures.
- B. Switch the consumer group ID to a new one so that the consumer starts from the earliest offset, hoping that cached deserializer state is cleared.
- C. Reduce the `max.poll.interval.ms` to force a rebalance more often, hoping that a new leader will deserialize correctly.
- D. Configure the consumer to use a Dead‑Letter Queue strategy with `ErrorHandlingDeserializer` so that failed records are routed to a separate topic while the consumer continues.
- E. Add a custom `DeserializationExceptionHandler` that logs the error and rethrows it, causing the consumer to pause on the problematic record.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When a consumer encounters a `SerializationException`, the root cause is usually a corrupt or incompatible record. The most effective way to troubleshoot while keeping the application running is to use a Dead‑Letter Queue (DLT) with an `ErrorHandlingDeserializer`. This approach logs the failure, skips the problematic record, and routes it to a separate topic for later analysis, thereby preventing downtime. Other options either change network or consumer settings that have no effect on deserialization or cause the consumer to pause. The DLT strategy is the standard practice recommended by Confluent for observability and testing of Kafka applications. Caveat: `ErrorHandlingDeserializer` is a Spring for Apache Kafka class (the plain Apache Kafka consumer has no built-in DLQ, the Kafka Streams `DeserializationExceptionHandler` / Connect `errors.tolerance` + `errors.deadletterqueue.*` are the native equivalents), so D is only the best of the offered options.

Verified live (D confirmed as best option): Spring docs - ErrorHandlingDeserializer returns null plus a DeserializationException header with the raw bytes, the record is not passed to the listener, and DeadLetterPublishingRecoverer can publish it. It is a Spring class, not plain Apache Kafka.
Source: https://docs.spring.io/spring-kafka/reference/kafka/serdes.html

**Detailed explanation of each option:**

1. ❌ **A. Increase the `fetch.max.bytes` configuration so that the consumer retrieves larger batches, hoping that a full record will avoid partial deserialization failures.**  
   **Incorrect**. Increasing fetch size does not affect whether a record can be deserialized. If the record itself is corrupted or does not match the schema, a larger fetch will still result in a `SerializationException`. This setting only influences network bandwidth and batch size, not deserialization.

2. ❌ **B. Switch the consumer group ID to a new one so that the consumer starts from the earliest offset, hoping that cached deserializer state is cleared.**  
   **Incorrect**. Changing the group ID merely resets the offsets, it does not remove the underlying deserialization problem. The consumer will still attempt to deserialize the same malformed records and continue to fail.

3. ❌ **C. Reduce the `max.poll.interval.ms` to force a rebalance more often, hoping that a new leader will deserialize correctly.**  
   **Incorrect**. Lowering the poll interval triggers frequent rebalances but does not influence record deserialization. The same corrupt record will be fetched again and will still fail to deserialize.

4. ✅ **D. Configure the consumer to use a Dead‑Letter Queue strategy with `ErrorHandlingDeserializer` so that failed records are routed to a separate topic while the consumer continues.**  
   **Correct**. The `ErrorHandlingDeserializer` captures the failing record, logs the error, and passes a placeholder to the user code, allowing the consumer to skip the bad record. The original record is sent to a DLT topic, enabling developers to inspect it later. This is the recommended approach for troubleshooting deserialization errors without service interruption.

5. ❌ **E. Add a custom `DeserializationExceptionHandler` that logs the error and rethrows it, causing the consumer to pause on the problematic record.**  
   **Incorrect**. Rethrowing the exception will pause the consumer and halt processing. While it logs the error, it does not provide a mechanism to isolate or recover the bad record, nor does it allow the consumer to continue processing valid records.

</details>

## Question 47 (Application Development):
In a Kafka Streams application, what is the default behavior when a record fails deserialization during processing?

- A. A StreamsException is thrown, causing the stream thread to halt and the application to stop until restarted.
- B. The offending record is discarded, and the stream thread pauses for 30 seconds before resuming.
- C. The offending record is routed to a dead‑letter topic automatically.
- D. The offending record is skipped, and the stream continues processing subsequent records.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

When a record cannot be deserialized in Kafka Streams, the default exception handler (`LogAndFailExceptionHandler`, configured through `deserialization.exception.handler`, formerly `default.deserialization.exception.handler`) logs the error and fails, so a `StreamsException` ends the stream thread (and the application client if no other threads remain) until it is restarted or a custom handler is set. Skipping requires `LogAndContinueExceptionHandler`, since Kafka 3.8 a custom handler can also return a dead-letter-queue record list (KIP-1034), but that is not the default. Understanding the default behavior is critical for designing robust stream applications and for deciding whether to implement custom error handling.

Source: https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (deserialization.exception.handler), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html (Handling Exceptions). Verified in source: ConfigDef .define("deserialization.exception.handler", Type.CLASS, LogAndFailExceptionHandler.class.getName(), ...), the old default.deserialization.exception.handler is deprecated since 4.0.
Source: https://raw.githubusercontent.com/apache/kafka/trunk/streams/src/main/java/org/apache/kafka/streams/StreamsConfig.java

**Detailed explanation of each option:**

1. ✅ **A. A StreamsException is thrown, causing the stream thread to halt and the application to stop until restarted.**  
   **Correct**. The default handler `LogAndFailExceptionHandler` logs the error and throws a `StreamsException`, which stops the stream thread (the application stops once all threads are dead unless a `StreamsUncaughtExceptionHandler` replaces the thread). This is the default behavior.

2. ❌ **B. The offending record is discarded, and the stream thread pauses for 30 seconds before resuming.**  
   **Incorrect**. This describes a custom retry strategy. The default handler does not pause the thread, it terminates the thread immediately.

3. ❌ **C. The offending record is routed to a dead‑letter topic automatically.**  
   **Incorrect**. Kafka Streams does not provide automatic dead‑letter routing for deserialization errors unless explicitly configured.

4. ❌ **D. The offending record is skipped, and the stream continues processing subsequent records.**  
   **Incorrect**. This is the behavior of the user‑supplied `LogAndContinueExceptionHandler`, not the default.

</details>

## Question 48 (Kafka Fundamentals):
Which of the following best describes how Apache Kafka ensures data durability and high availability through replication?

- A. The offset information is replicated with the data so that a consumer can resume from the last committed offset after a broker crash.
- B. Replication is performed by the producer sending the same message to every consumer group so that each consumer receives an identical copy of the data.
- C. Replication is controlled by the broker’s log cleaner which removes duplicate log segments to keep data consistent across replicas.
- D. The replication factor specifies the number of replica copies per partition. Each replica resides on a distinct broker, the broker elected as the partition leader handles all reads and writes, while followers fetch data from the leader. If the leader fails, a follower is promoted to leader automatically, maintaining availability.
- E. Each partition’s log is mirrored to every other partition within the same topic to balance load and improve throughput.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka achieves durability and high availability by replicating each partition’s log across multiple brokers. The replication factor determines how many copies exist. One broker is elected as the partition leader, and all producers and consumers talk to this leader. The other brokers hold follower replicas that continually pull data from the leader. If the leader broker fails, one of the followers is automatically promoted to leader, ensuring zero downtime. This design guarantees that data is not lost and remains accessible even in the face of broker failures. Understanding this replication workflow is essential for designing fault‑tolerant Kafka clusters. (Precision: the leader must be chosen from the in-sync replicas, consumers can also fetch from followers since KIP-392, but by default reads go to the leader.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 7 (Reliable Data Delivery - Replication) and ch. 6 (Kafka Internals - Replication), https://kafka.apache.org/documentation/#replication

**Detailed explanation of each option:**

1. ❌ **A. The offset information is replicated with the data so that a consumer can resume from the last committed offset after a broker crash.**  
   **Incorrect**. Offsets are stored in a separate __consumer_offsets topic, not part of the partition replication.

2. ❌ **B. Replication is performed by the producer sending the same message to every consumer group so that each consumer receives an identical copy of the data.**  
   **Incorrect**. Replication is a broker‑level feature, not performed by producers or consumers.

3. ❌ **C. Replication is controlled by the broker’s log cleaner which removes duplicate log segments to keep data consistent across replicas.**  
   **Incorrect**. Log cleaning removes idle data, it does not provide replication.

4. ✅ **D. The replication factor specifies the number of replica copies per partition. Each replica resides on a distinct broker, the broker elected as the partition leader handles all reads and writes, while followers fetch data from the leader. If the leader fails, a follower is promoted to leader automatically, maintaining availability.**  
   **Correct**. This is the core replication mechanism: replication factor, separate brokers, leader election, and failover.

5. ❌ **E. Each partition’s log is mirrored to every other partition within the same topic to balance load and improve throughput.**  
   **Incorrect**. Partitions are independent, replication does not involve mirroring across partitions.

</details>

## Question 49 (Observability & Testing):
As a Confluent Certified Developer, you are required to expose your Kafka Streams application metrics so that a Prometheus monitoring stack can collect them. Which of the following approaches is the most standard and recommended way to achieve this in a Confluent Platform deployment?

- A. Configure the Kafka Streams application to expose JMX metrics and use the Prometheus JMX exporter to scrape them.
- B. Use the Confluent Control Center REST API to poll application metrics at runtime.
- C. Write metrics to a dedicated Kafka topic and set up a Prometheus Kafka consumer to consume them.
- D. Add a custom Micrometer registry to the Streams application and configure Prometheus to scrape it.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Confluent Platform recommends exposing Kafka Streams metrics via Java Management Extensions (JMX) and then using the Prometheus JMX exporter to scrape them. This approach leverages the built‑in JMX reporter that Streams automatically publishes, while Prometheus can consume those metrics without extra instrumentation. Alternatives such as Micrometer or Control Center REST polling are either non‑standard or not designed for Prometheus scraping, and writing to a Kafka topic adds unnecessary overhead. Using the JMX path aligns with the official Confluent documentation and ensures metrics are available for real‑time monitoring, alerting, and troubleshooting.

Source: https://kafka.apache.org/documentation/#monitoring and https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (Streams metrics are exposed via JMX), Kafka: The Definitive Guide 2nd ed., ch. 13 (Monitoring Kafka, JMX). Verified live: Confluent says Streams reports metrics through JMX (https://docs.confluent.io/platform/current/streams/monitoring.html) and points to confluentinc/jmx-monitoring-stacks (Prometheus + Grafana) for exporting JMX (https://docs.confluent.io/platform/current/kafka/monitoring.html). The pages do not literally name 'Prometheus JMX exporter', so A is the best option, not word-for-word documented.

**Detailed explanation of each option:**

1. ✅ **A. Configure the Kafka Streams application to expose JMX metrics and use the Prometheus JMX exporter to scrape them.**  
   **Correct**. Kafka Streams ships with a JMX metrics reporter. Prometheus can scrape these metrics via the official Prometheus JMX exporter, which is the supported, well‑documented path for Prometheus integration.

2. ❌ **B. Use the Confluent Control Center REST API to poll application metrics at runtime.**  
   **Incorrect**. Control Center can provide metrics dashboards, but it does not expose metrics via a Prometheus scrape endpoint, it is intended for visualization, not direct Prometheus integration.

3. ❌ **C. Write metrics to a dedicated Kafka topic and set up a Prometheus Kafka consumer to consume them.**  
   **Incorrect**. This is a custom solution that introduces additional latency and complexity, the Confluent Platform provides a native JMX exporter path that is far simpler and more reliable.

4. ❌ **D. Add a custom Micrometer registry to the Streams application and configure Prometheus to scrape it.**  
   **Incorrect**. While Micrometer can expose metrics, it is not the default or recommended mechanism in the Confluent Platform for Kafka Streams, and requires additional libraries and configuration that are not part of the core SDK.

</details>

## Question 50 (Observability & Testing):
You have deployed a Kafka consumer application that is now reporting high lag across several partitions. Which of the following actions are effective first‑step troubleshooting techniques to isolate the root cause?

- A. Analyze the consumer’s thread pool size and `max.poll.interval.ms` to ensure it is not timing out and losing offsets.
- B. Use `kafka-consumer-groups.sh --describe` to view current lag for each partition.
- C. Verify that the consumer group’s `auto.offset.reset` is set to `earliest` to ensure it reads from the beginning of the partition.
- D. Enable and monitor the `consumer-fetch-manager-metrics` JMX bean for `fetcher.max.poll.records` and `fetcher.avg.bytes.per.sec`.
- E. Increase the consumer’s `fetch.min.bytes` setting to reduce the number of fetch requests.
- F. Check the size of the `__consumer_offsets` topic to determine if offset commits are being throttled.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

Effective lag troubleshooting starts with quantifying the problem using `kafka-consumer-groups.sh --describe`, which shows the exact number of messages behind each partition. Once lag is confirmed, inspect consumer configuration for timing issues: a too‑small `max.poll.interval.ms` causes frequent rebalances that reset offsets, while an undersized thread pool can delay poll calls. Adjusting these settings restores a steady consumer pace. JMX fetch metrics and `fetch.min.bytes` can provide context on throughput, but they are secondary to lag measurement and configuration tuning. These practices align with Confluent’s guidance on monitoring consumer lag and tuning consumer performance. Note: `consumer-fetch-manager-metrics` does expose lag (`records-lag-max`, per-partition `records-lag`), but the metric names in option D (`fetcher.max.poll.records`, `fetcher.avg.bytes.per.sec`) do not exist, which makes D wrong. Option A is only loosely worded (the consumer has no thread pool, the point is that slow processing between `poll()` calls exceeding `max.poll.interval.ms` triggers rebalances).

Source: https://kafka.apache.org/documentation/#consumer_monitoring and #basic_ops_consumer_group, Kafka: The Definitive Guide 2nd ed., ch. 13 (Consumer lag monitoring, Burrow) and ch. 4.

**Detailed explanation of each option:**

1. ✅ **A. Analyze the consumer’s thread pool size and `max.poll.interval.ms` to ensure it is not timing out and losing offsets.**  
   **Correct**. A too‑low `max.poll.interval.ms` can trigger rebalances, causing offsets to be re‑consumed and increasing lag. Adjusting thread pool and interval settings can mitigate this.

2. ✅ **B. Use `kafka-consumer-groups.sh --describe` to view current lag for each partition.**  
   **Correct**. This command directly reports lag per partition, making it a core diagnostic step for understanding consumer performance issues.

3. ❌ **C. Verify that the consumer group’s `auto.offset.reset` is set to `earliest` to ensure it reads from the beginning of the partition.**  
   **Incorrect**. `auto.offset.reset` only matters when a group has no committed offset. Changing it does not affect an already‑running consumer’s lag.

4. ❌ **D. Enable and monitor the `consumer-fetch-manager-metrics` JMX bean for `fetcher.max.poll.records` and `fetcher.avg.bytes.per.sec`.**  
   **Incorrect**. The metrics named here (`fetcher.max.poll.records`, `fetcher.avg.bytes.per.sec`) do not exist. The bean `kafka.consumer:type=consumer-fetch-manager-metrics` does expose lag via `records-lag-max` and fetch throughput via `bytes-consumed-rate`, but the option names the wrong attributes.

5. ❌ **E. Increase the consumer’s `fetch.min.bytes` setting to reduce the number of fetch requests.**  
   **Incorrect**. Raising `fetch.min.bytes` can reduce request frequency but may increase latency, it does not directly address lag and can actually worsen it if the consumer blocks waiting for more data.

6. ❌ **F. Check the size of the `__consumer_offsets` topic to determine if offset commits are being throttled.**  
   **Incorrect**. Offset commits are typically lightweight, the size of `__consumer_offsets` rarely causes significant lag. This check is rarely useful for lag diagnosis.

</details>

## Question 51 (Application Development):
An application uses the Kafka Producer and Consumer APIs to implement a data pipeline. Which of the following statements correctly describe how to achieve at‑most‑once, at‑least‑once, and exactly‑once processing semantics in such a setup?

- A. Kafka Streams' `commit.interval.ms` config automatically commits offsets to the broker, ensuring at‑least‑once processing semantics.
- B. Configure the producer with `enable.idempotence=true` and `acks=all`. This alone provides at‑least‑once delivery.
- C. Set `max.in.flight.requests.per.connection=1` along with `enable.idempotence=true` to prevent duplicate records.
- D. Use a transactional producer (`transactional.id` set) and wrap each batch of sends in `beginTransaction()` / `commitTransaction()`, while the consumer commits offsets manually inside the same transaction. This guarantees exactly‑once semantics.
- E. Using a consumer with `enable.auto.commit=true` and processing records in the polling loop without committing offsets explicitly guarantees exactly‑once semantics.
- F. Set `enable.auto.commit=false` and call `consumer.commitSync()` after each record is processed. This guarantees at‑most‑once semantics.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

Processing semantics in Kafka revolve around how producers and consumers handle duplicates and data loss. Exactly‑once semantics require atomicity between producing records and committing offsets, achievable with transactional producers and `sendOffsetsToTransaction` (consumers downstream use `isolation.level=read_committed`). At‑least‑once is what you get when offsets are committed AFTER processing (Streams `commit.interval.ms` default), and on the producer side `acks=all` with retries (adding `enable.idempotence=true` even removes the duplicates). At‑most‑once is the opposite: commit offsets BEFORE processing, so records can be lost but never re-processed. Hence F is wrong: committing with `commitSync()` after each processed record is still at-least-once (a crash between processing and commit causes re-processing), the original answer key was wrong here. B is right per the book: acks=all + sufficient delivery.timeout.ms guarantees at-least-once delivery to Kafka (idempotence additionally prevents duplicates). C is not a way to prevent duplicates - idempotence already does that and allows up to 5 in-flight requests while preserving order. E is wrong: auto-commit gives at-least-once at best (or loss if the commit happens before processing finishes), never exactly-once.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 (enable.idempotence, acks, max.in.flight), ch. 4 (Commits and Offsets - commit after processing), ch. 8 (Exactly Once Semantics), https://kafka.apache.org/documentation/#semantics

**Detailed explanation of each option:**

1. ✅ **A. Kafka Streams' `commit.interval.ms` config automatically commits offsets to the broker, ensuring at‑least‑once processing semantics.**  
   **Correct**. In Kafka Streams, `commit.interval.ms` controls how frequently the library commits processed offsets. If a failure occurs, the same records will be re‑processed, which satisfies the at‑least‑once guarantee.

2. ✅ **B. Configure the producer with `enable.idempotence=true` and `acks=all`. This alone provides at‑least‑once delivery.**  
   **Correct**. The statement is about producer-to-broker delivery: `acks=all` plus retries guarantees each record is written at least once (the book, ch. 3), and idempotence additionally removes the duplicates retries could cause (so it is actually stronger than at-least-once per partition within a producer session). Consumer offset handling is a separate concern.

3. ❌ **C. Set `max.in.flight.requests.per.connection=1` along with `enable.idempotence=true` to prevent duplicate records.**  
   **Incorrect**. Idempotence by itself already prevents duplicate writes from retries (and keeps ordering with up to 5 in-flight requests), so limiting in-flight requests to 1 is not what prevents duplicates, and it says nothing about processing semantics.

4. ✅ **D. Use a transactional producer (`transactional.id` set) and wrap each batch of sends in `beginTransaction()` / `commitTransaction()`, while the consumer commits offsets manually inside the same transaction. This guarantees exactly‑once semantics.**  
   **Correct**. Transactional producers allow a single, atomic write that includes both producing records and committing consumer offsets. When the transaction is committed, the broker guarantees that either all records and the corresponding offsets are visible or none are, providing true exactly‑once processing.

5. ❌ **E. Using a consumer with `enable.auto.commit=true` and processing records in the polling loop without committing offsets explicitly guarantees exactly‑once semantics.**  
   **Incorrect**. Auto‑commit commits the offsets returned by the previous `poll()` periodically, independent of whether processing finished, so a crash can cause re‑processing (duplicates) or, if processing was still in progress, loss. It never gives exactly‑once.

6. ❌ **F. Set `enable.auto.commit=false` and call `consumer.commitSync()` after each record is processed. This guarantees at‑most‑once semantics.**  
   **Incorrect**. Committing AFTER processing means a crash between processing and commit leads to re‑processing of that record on restart: that is at‑least‑once. At‑most‑once requires committing BEFORE processing.

</details>

## Question 52 (Application Development):
A Kafka consumer is configured with `enable.auto.commit=false` and the application manually commits offsets after processing each batch. If the application crashes before committing the offsets for a batch, what will happen when it restarts?

- A. It will re-read the messages from the beginning of the topic.
- B. It will skip the messages that were processed before the crash.
- C. It will read messages from the last committed offset plus the uncommitted batch again.
- D. It will start from the last committed offset.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When `enable.auto.commit` is disabled, the consumer only records offsets after an explicit commit. If the application crashes before committing the current batch, the broker’s stored offset (in `__consumer_offsets`) remains at the last successful commit. On restart the consumer resumes from that last committed offset, which means the batch that was processed but not committed is read (and processed) again, i.e. at‑least‑once semantics with possible duplicates. D states exactly this. C is worded confusingly ("last committed offset plus the uncommitted batch again") - the uncommitted batch lies after the last committed offset, so it is the same data, not an additional re-read, D is the precise statement. (Ambiguous question: C and D describe the same behaviour, D is cleaner.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (Commits and Offsets, Committing the Current Offset - "Re-processing"), https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit

**Detailed explanation of each option:**

1. ❌ **A. It will re-read the messages from the beginning of the topic.**  
   **Incorrect**. Restarting does not reset the offset to the topic beginning unless a special reset policy is applied. The consumer continues from the last committed position.

2. ❌ **B. It will skip the messages that were processed before the crash.**  
   **Incorrect**. Skipping would violate at-least-once delivery. Without committing, the consumer has no record that it processed those messages, so they will be re-read.

3. ❌ **C. It will read messages from the last committed offset plus the uncommitted batch again.**  
   **Incorrect** (imprecise). The uncommitted batch is already part of "everything after the last committed offset", so this is a confusing way to say the same as D, it also wrongly implies a separate re-read on top of the committed position. (The batch is re-processed, so duplicates are possible.)

4. ✅ **D. It will start from the last committed offset.**  
   **Correct**. The consumer resumes from the last committed offset, since the crashed batch was never committed, its records are delivered again.

</details>

## Question 53 (Kafka Fundamentals):
Which of the following statements correctly describe fundamental properties of Apache Kafka’s log‑based architecture that enable its scalability and fault tolerance?

- A. Kafka’s log compaction feature keeps only the latest value for each key, ensuring compact storage.
- B. ZooKeeper is responsible for replicating partition data across brokers.
- C. Replication of partitions across brokers guarantees durability and high availability.
- D. All Kafka messages are stored entirely in memory for maximum throughput.
- E. Kafka uses immutable, append‑only logs so that writes do not overwrite existing data, reducing write contention.
- F. Kafka partitions a topic into multiple logs, allowing parallel processing across many brokers.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, E, F

**Explanation:**

Kafka’s core design relies on immutable, append‑only logs that minimize write contention and enable sequential disk I/O. Topics are divided into partitions, each a separate log that can be distributed across brokers for parallelism. Replication of each partition across multiple brokers provides durability and high availability, the leader replica processes client requests while followers sync asynchronously. Memory is used for caching and index storage, not for holding all messages. Optional features such as log compaction and ZooKeeper’s role in metadata management are important but not fundamental to scalability or fault tolerance. Understanding these basics is critical for building robust, high‑throughput Kafka applications. Note: statement A is also factually true (compaction keeps the latest value per key) - it is just not a fundamental scalability/fault-tolerance property, so it is the "distractor" here, ZooKeeper/KRaft handle metadata, not data replication.

Source: Kafka: The Definitive Guide 2nd ed., ch. 1-2 (Publish/Subscribe, Partitions, Replication), ch. 6 (Kafka Internals - Replication, Physical Storage, Compaction), https://kafka.apache.org/documentation/#design

**Detailed explanation of each option:**

1. ❌ **A. Kafka’s log compaction feature keeps only the latest value for each key, ensuring compact storage.**  
   **Incorrect**. While log compaction is a valuable feature, it is an optional configuration and not a fundamental property required for scalability or fault tolerance.

2. ❌ **B. ZooKeeper is responsible for replicating partition data across brokers.**  
   **Incorrect**. ZooKeeper (or the newer KRaft mode) manages cluster metadata and leader election, but the actual data replication happens using Kafka’s own protocol between brokers.

3. ✅ **C. Replication of partitions across brokers guarantees durability and high availability.**  
   **Correct**. Replicas are maintained on separate brokers, the leader replica handles traffic, while followers sync asynchronously, providing fault tolerance.

4. ❌ **D. All Kafka messages are stored entirely in memory for maximum throughput.**  
   **Incorrect**. Kafka persists messages to disk (often with configurable log retention) to ensure durability, memory is used only for caching headers and indexes.

5. ✅ **E. Kafka uses immutable, append‑only logs so that writes do not overwrite existing data, reducing write contention.**  
   **Correct**. The immutable log design allows producers to append quickly and enables efficient sequential disk writes, which is a core scalability feature.

6. ✅ **F. Kafka partitions a topic into multiple logs, allowing parallel processing across many brokers.**  
   **Correct**. Partitioning is the primary mechanism for horizontal scaling, each partition can be handled by a different broker, enabling concurrent reads and writes.

</details>

## Question 54 (Streams Development):
Which of the following actions are effective for tuning performance and scaling a Kafka Streams application?

- A. Increase the value of `num.stream.threads` beyond the number of physical cores to fully utilize CPU resources.
- B. Distribute the input topic across many partitions so that each stream instance can process them in parallel.
- C. Use the `process` API to manually split the stream state across multiple RocksDB instances for better cache locality.
- D. Use the `state.dir` property to point to a local SSD for RocksDB state stores.
- E. Enable `compression.type` to `gzip` on all topics to reduce serialization overhead.
- F. Reduce `cache.max.bytes.buffering` to zero to avoid memory consumption.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

For Kafka Streams performance tuning, scaling is achieved by maximizing parallelism and minimizing I/O bottlenecks. Distributing input data across many partitions (option 3) lets each stream instance consume concurrently, scaling horizontally. Locating RocksDB state on fast local SSDs (option 6) reduces disk latency, which is critical for stateful operators. In contrast, over‑provisioning threads (option 1) causes CPU thrashing, manual state splitting via `process` (option 2) is unsupported, excessive compression (option 4) can increase CPU cost, and disabling the cache (option 5) forces costly disk reads. Proper configuration of these parameters yields significant throughput gains while avoiding common misconceptions about resource allocation. Details: the number of tasks (= max partitions of the input topics) is the upper bound of parallelism, so threads/instances beyond that stay idle, `num.stream.threads` can be raised above 1 (default) but "one thread per core" is only a rule of thumb. `cache.max.bytes.buffering` is deprecated in favour of `statestore.cache.max.bytes`, the cache reduces downstream updates and store writes, so zeroing it generally lowers throughput.

Source: https://kafka.apache.org/documentation/streams/architecture (Parallelism Model) and https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html, Kafka: The Definitive Guide 2nd ed., ch. 14 (Scaling the Topology).

**Detailed explanation of each option:**

1. ❌ **A. Increase the value of `num.stream.threads` beyond the number of physical cores to fully utilize CPU resources.**  
   **Incorrect**. Kafka Streams runs one thread per core for optimal CPU utilization. Setting `num.stream.threads` higher than available cores causes context switching and can degrade performance, not improve it.

2. ✅ **B. Distribute the input topic across many partitions so that each stream instance can process them in parallel.**  
   **Correct**. Increasing topic partitions allows multiple stream instances (or threads) to consume in parallel, improving throughput and scaling out horizontally. This is a primary scaling strategy for Kafka Streams.

3. ❌ **C. Use the `process` API to manually split the stream state across multiple RocksDB instances for better cache locality.**  
   **Incorrect**. While the `process` API allows custom processing, it does not provide a mechanism to split a single state store into multiple RocksDB instances, RocksDB is managed internally by Streams. This approach is not supported for performance tuning.

4. ✅ **D. Use the `state.dir` property to point to a local SSD for RocksDB state stores.**  
   **Correct**. RocksDB state stores are stored on disk, locating them on fast SSDs (or NVMe) improves read/write latency and overall application throughput, especially for stateful operations.

5. ❌ **E. Enable `compression.type` to `gzip` on all topics to reduce serialization overhead.**  
   **Incorrect**. Compression can reduce network I/O but increases CPU load for encoding/decoding. While it may help in bandwidth‑constrained environments, it is not a guaranteed performance win and can actually hurt throughput in CPU‑bound workloads.

6. ❌ **F. Reduce `cache.max.bytes.buffering` to zero to avoid memory consumption.**  
   **Incorrect**. Setting the in‑memory cache to zero eliminates the buffering that prevents repeated state lookups, leading to many disk reads and dramatically lower throughput. Keeping a reasonable cache size is essential for performance.

</details>

## Question 55 (Kafka Connect):
You need to configure a Kafka Connect worker to communicate with a Confluent Cluster that uses TLS encryption and SASL/SCRAM-SHA-512 authentication. Which configuration set is sufficient to enable the worker to authenticate and establish a secure connection?

- A. Add `sasl.mechanism=GSSAPI` and `sasl.jaas.config` for Kerberos to the worker’s properties file.
- B. Add `security.protocol=SSL` and `sasl.mechanism=PLAIN` to the worker’s properties file.
- C. Add only `sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="connect" password="password",` to the worker’s properties file.
- D. Add only `ssl.truststore.location` and `ssl.truststore.password` to the worker’s properties file.
- E. Add `security.protocol=SASL_SSL` and `sasl.mechanism=SCRAM-SHA-512` to the worker’s properties file.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

To connect a Kafka Connect worker to a secured Confluent cluster, you must enable both encryption and authentication. The `security.protocol` property selects the protocol stack, `SASL_SSL` combines TLS encryption with SASL authentication. The `sasl.mechanism` property must match the mechanism used by the cluster (e.g., `SCRAM-SHA-512`). Additionally, a `sasl.jaas.config` entry is required for credentials, but the question focuses on the protocol and mechanism configuration. Without specifying these, the worker cannot negotiate the secure channel, leading to connection failures. Caveats: strictly, a working setup also needs `sasl.jaas.config` (credentials) and a truststore (unless the CA is in the JVM default), and the connectors' internal clients need the same settings with the `producer.`/`consumer.`/`admin.` prefixes, E is still the only option that is correct as far as it goes (the others are wrong protocol/mechanism or incomplete).

Source: https://docs.confluent.io/platform/current/connect/security.html (Kafka Connect security - worker config), https://kafka.apache.org/documentation/#security_sasl_scram, Kafka: The Definitive Guide 2nd ed., ch. 11 (Securing Kafka - SASL/SCRAM, TLS) and ch. 9 (Connect).

**Detailed explanation of each option:**

1. ❌ **A. Add `sasl.mechanism=GSSAPI` and `sasl.jaas.config` for Kerberos to the worker’s properties file.**  
   **Incorrect**. GSSAPI/Kerberos is not the authentication mechanism configured on the cluster, using it would cause authentication failure.

2. ❌ **B. Add `security.protocol=SSL` and `sasl.mechanism=PLAIN` to the worker’s properties file.**  
   **Incorrect**. `SSL` alone does not enable SASL, and `PLAIN` is a different authentication mechanism that requires a different JAAS configuration.

3. ❌ **C. Add only `sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="connect" password="password",` to the worker’s properties file.**  
   **Incorrect**. Without `security.protocol` and `sasl.mechanism`, the worker does not know to use SASL or TLS, so authentication will fail.

4. ❌ **D. Add only `ssl.truststore.location` and `ssl.truststore.password` to the worker’s properties file.**  
   **Incorrect**. These properties enable TLS encryption but do not provide any authentication mechanism, so the cluster will reject the connection.

5. ✅ **E. Add `security.protocol=SASL_SSL` and `sasl.mechanism=SCRAM-SHA-512` to the worker’s properties file.**  
   **Correct**. The worker must specify both the transport protocol (`SASL_SSL` combines encryption and SASL) and the authentication mechanism (`SCRAM-SHA-512`). These settings, together with the required JAAS config, allow the worker to authenticate and communicate securely with the cluster.
```
security.protocol=SASL_SSL
sasl.mechanism=SCRAM-SHA-512
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
  username="connect" password="secret",
ssl.truststore.location=/path/to/truststore.jks
ssl.truststore.password=changeit
```
</details>

## Question 56 (Observability & Testing):
When unit‑testing or integration‑testing a Kafka client application that produces and consumes messages, which of the following practices help ensure accurate, reliable, and deterministic tests?

- A. Hardcode timestamps in test records to avoid flaky tests caused by clock drift.
- B. Run integration tests against the production cluster to guarantee realism.
- C. Use an embedded Kafka broker (e.g., EmbeddedKafka) to simulate a cluster within the test JVM.
- D. Disable idempotence and transaction support during tests to reduce complexity.
- E. Employ MockProducer and MockConsumer to validate serialization and record handling without network overhead.
- F. Skip testing consumer offset commits because the client library handles them automatically.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, E

**Explanation:**

Testing Kafka client applications requires a blend of lightweight mocks and realistic embedded environments. MockProducer/MockConsumer validate serialization logic quickly, while an embedded broker preserves full Kafka semantics for integration tests. Deterministic timestamps prevent flaky tests caused by clock drift, and offset commit verification ensures correct consumption semantics. Avoiding production clusters keeps tests isolated, and disabling idempotence or transactions can hide real‑world bugs. Together, these practices provide reliable, repeatable, and meaningful tests that align with Confluent’s Observability & Testing guidelines. (Caveats: EmbeddedKafka is a Spring Kafka test utility - Apache Kafka's own options are MockProducer/MockConsumer, TopologyTestDriver for Streams, or Testcontainers, an embedded broker is a real broker using temp dirs, not "fully in-memory". Option A is the weakest of the three, but the other candidates are clearly wrong.)

Source: https://kafka.apache.org/documentation/streams/developer-guide/testing.html (TopologyTestDriver, test utils), MockProducer/MockConsumer javadoc in kafka-clients, https://docs.spring.io/spring-kafka/reference/testing.html (EmbeddedKafka).

**Detailed explanation of each option:**

1. ✅ **A. Hardcode timestamps in test records to avoid flaky tests caused by clock drift.**  
   **Correct**. Deterministic timestamps eliminate variability that can affect tests relying on time‑based logic, ensuring reproducibility. However, test logic that depends on dynamic timestamps should still be exercised with real clock values.

2. ❌ **B. Run integration tests against the production cluster to guarantee realism.**  
   **Incorrect**. Tests should be isolated, repeatable, and not affect live data. Using production can lead to flakiness, data corruption, and security risks. It violates best practices for test isolation.

3. ✅ **C. Use an embedded Kafka broker (e.g., EmbeddedKafka) to simulate a cluster within the test JVM.**  
   **Correct**. An embedded broker provides a real Kafka environment, preserving partitioning, ordering, and network semantics while remaining fully in‑memory. It allows end‑to‑end testing without external dependencies. Reference: https://github.com/spring-projects/spring-kafka/blob/master/src/test/java/org/springframework/kafka/embedded/EmbeddedKafkaBroker.java

4. ❌ **D. Disable idempotence and transaction support during tests to reduce complexity.**  
   **Incorrect**. Disabling these features when the production application uses them masks bugs related to duplicate detection or exactly‑once semantics. Tests must mirror production configuration.

5. ✅ **E. Employ MockProducer and MockConsumer to validate serialization and record handling without network overhead.**  
   **Correct**. These mock classes allow unit‑level validation of record creation, headers, and serialization logic, yielding fast, deterministic tests. Reference: https://github.com/apache/kafka/blob/master/clients/src/main/java/org/apache/kafka/clients/producer/MockProducer.java

6. ❌ **F. Skip testing consumer offset commits because the client library handles them automatically.**  
   **Incorrect**. Offset management is critical for at‑least‑once or exactly‑once processing. Tests must verify that offsets are committed correctly, especially in the presence of failures or rebalances.

</details>

## Question 57 (Kafka Fundamentals):
A topic `orders` has 2 partitions (0 and 1) and a 24‑hour retention period. A consumer group `order-processor` consumes from both partitions and commits offsets after each batch. The group stops for 2 days (longer than the retention period) and then restarts with auto.offset.reset set to `earliest`. Which statement correctly describes the starting offsets for each partition when the group resumes?

- A. The consumer will receive an error and need to manually reset the offsets because the committed offsets are no longer valid.
- B. The consumer will start from the latest offsets in each partition because `auto.offset.reset=earliest` is overridden by the fact that offsets were lost.
- C. The consumer will start from the earliest available offset in each partition (which could be greater than 0), because the committed offsets are considered out‑of‑range.
- D. The consumer will start reading from offset 0 on both partitions, because the committed offsets were lost during the downtime.
- E. The consumer will start from the last committed offsets before shutdown, even though the data at those offsets may have been deleted by retention.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When a consumer group resumes after a pause that exceeds the topic’s retention, any committed offsets that point to deleted records become out‑of‑range. Kafka then applies the auto.offset.reset configuration to determine where to seek. With auto.offset.reset set to "earliest", the consumer starts at the first available offset in each partition, which may be greater than 0 if earlier data was purged. This behavior ensures continuity of consumption without manual intervention and prevents accidental duplicate reads of already‑deleted data. Understanding the interplay between retention, committed offsets, and auto.offset.reset is essential for designing reliable consumer applications in Kafka. Detail: the committed offsets themselves survive because the group's offsets are retained for `offsets.retention.minutes` (default 7 days, counted from when the group became empty), which is longer than the 2-day pause, if the pause had exceeded that, the offsets would be deleted and `auto.offset.reset` would apply as well (same outcome here). If all data was deleted, "earliest" equals the log end offset, not necessarily 0.

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (auto.offset.reset, committed offsets) and ch. 3 (offsets.retention.minutes), https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset, https://kafka.apache.org/documentation/#brokerconfigs_offsets.retention.minutes

**Detailed explanation of each option:**

1. ❌ **A. The consumer will receive an error and need to manually reset the offsets because the committed offsets are no longer valid.**  
   **Incorrect**. Kafka clients handle out‑of‑range offsets internally by applying the auto.offset.reset policy. The consumer will not throw a hard error requiring manual intervention.

2. ❌ **B. The consumer will start from the latest offsets in each partition because auto.offset.reset="earliest" is overridden by the fact that offsets were lost.**  
   **Incorrect**. The auto.offset.reset value is honored only when the offset is out of range, it is not overridden by the fact that offsets were lost. Therefore the consumer will not default to the latest unless the policy is set to "latest".

3. ✅ **C. The consumer will start from the earliest available offset in each partition (which could be greater than 0), because the committed offsets are considered out‑of‑range.**  
   **Correct**. When the committed offset is out of range, Kafka seeks to the offset defined by auto.offset.reset. With "earliest", the consumer begins at the first retained message in each partition.

4. ❌ **D. The consumer will start reading from offset 0 on both partitions, because the committed offsets were lost during the downtime.**  
   **Incorrect**. Committed offsets are stored in the broker, they are not lost during downtime. Even if the data has been deleted, the offsets still exist, but the broker will treat them as out‑of‑range and will not reset to 0 automatically.

5. ❌ **E. The consumer will start from the last committed offsets before shutdown, even though the data at those offsets may have been deleted by retention.**  
   **Incorrect**. If the broker’s log has removed all messages up to those offsets, the committed offsets become out‑of‑range. Kafka does not automatically seek to them, instead it applies the auto.offset.reset policy.

</details>

## Question 58 (Observability & Testing):
You are debugging a Confluent Kafka cluster and need to display the current lag for the consumer group `analytics-group` across all partitions of its subscribed topics. Which CLI command will correctly return this information when the cluster is reachable at `localhost:9092`?

- A. kafka-consumer-groups.sh --describe --group analytics-group --bootstrap-server localhost:9092
- B. kafka-configs.sh --describe --entity-type consumer-groups --entity-name analytics-group --bootstrap-server localhost:9092
- C. kafka-console-consumer.sh --group analytics-group --bootstrap-server localhost:9092 --topic my-topic
- D. kafka-run-class org.apache.kafka.clients.admin.ConsumerGroupCommand --describe --group analytics-group --bootstrap-server localhost:9092
- E. kafka-consumer-groups.sh --describe --group analytics-group --zookeeper localhost:2181

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In modern Kafka deployments, consumer group metadata and lag are queried via the `kafka-consumer-groups.sh` script using the `--describe` flag. This tool prints each subscribed partition’s current offset, log end offset, and the lag (difference). The `--zookeeper` flag is deprecated, and other commands either consume data or fetch configuration, not lag. Knowing the correct CLI is essential for debugging consumer performance and ensuring timely message processing. (Option D is wrong mainly because that class path does not exist as written - the tool class lives in `org.apache.kafka.tools.consumer.group.ConsumerGroupCommand` and the script is `kafka-run-class.sh`, E uses `--zookeeper`, which was removed.)

Source: https://kafka.apache.org/documentation/#basic_ops_consumer_group, Kafka: The Definitive Guide 2nd ed., ch. 12 (Administering Kafka - Consumer Groups, kafka-consumer-groups.sh).

**Detailed explanation of each option:**

1. ✅ **A. kafka-consumer-groups.sh --describe --group analytics-group --bootstrap-server localhost:9092**  
   **Correct**. This is the standard Kafka consumer‑group CLI. The `--describe` option prints each partition’s current offset, log end offset, and the calculated lag. The `--bootstrap-server` flag points the tool to the Kafka broker. This command directly returns the lag information you need.

2. ❌ **B. kafka-configs.sh --describe --entity-type consumer-groups --entity-name analytics-group --bootstrap-server localhost:9092**  
   **Incorrect**. This command retrieves configuration entries for a consumer group, not its offset or lag information. It does not provide the desired lag metrics.

3. ❌ **C. kafka-console-consumer.sh --group analytics-group --bootstrap-server localhost:9092 --topic my-topic**  
   **Incorrect**. This command starts a console consumer that reads messages from `my-topic`. It does not query or display consumer‑group lag metrics. It is unrelated to the requested information.

4. ❌ **D. kafka-run-class org.apache.kafka.clients.admin.ConsumerGroupCommand --describe --group analytics-group --bootstrap-server localhost:9092**  
   **Incorrect**. While `kafka-run-class` can execute the `ConsumerGroupCommand` class, this is not the official consumer‑group CLI used for observability. The exam expects the dedicated `kafka-consumer-groups.sh` script, making this answer incorrect.

5. ❌ **E. kafka-consumer-groups.sh --describe --group analytics-group --zookeeper localhost:2181**  
   **Incorrect**. Consumer group metadata is no longer stored in ZooKeeper in Kafka 2.x+. The `--zookeeper` option is deprecated for consumer‑group commands and will not provide accurate lag information. This command is therefore incorrect.

</details>

## Question 59 (Application Development):
A producer is using the default configuration to send records up to 4 MB each. The application needs to keep round‑trip latency low while ensuring the producer does not fail with a record‑size error. Which producer configuration should be adjusted and how?

- A. Set `linger.ms` to 200 ms to allow more records to accumulate.
- B. Set `acks` to "all" to ensure durability.
- C. Increase `max.request.size` to at least 4 MB.
- D. Reduce `buffer.memory` to 1 MB to force the producer to flush faster.
- E. Increase the `batch.size` property to 4 MB.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The producer-side limit on the size of a request (and therefore of the largest record) is `max.request.size` (default 1 MiB), so it must be raised above the largest record (4 MB). `batch.size` (default 16 KiB) is only a soft target for batch accumulation: a record larger than `batch.size` is simply sent in its own batch, so raising it is unnecessary (and wastes memory). Caveat: the broker (`message.max.bytes`) or topic (`max.message.bytes`) limit, default about 1 MB, must also be raised, otherwise the broker returns `RecordTooLargeException`, the question only asks about the producer. Increasing `linger.ms` would worsen latency, and changing `buffer.memory` or `acks` does not address the size constraint. Proper tuning balances these settings to achieve high throughput with acceptable latency. Refer to the official Kafka Producer configuration docs for detailed limits and default values.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 (max.request.size, p. 60: "caps both the size of the largest message... the broker has its own limit message.max.bytes"), https://kafka.apache.org/documentation/#producerconfigs_max.request.size

**Detailed explanation of each option:**

1. ❌ **A. Set `linger.ms` to 200 ms to allow more records to accumulate.**  
   **Incorrect**. Increasing `linger.ms` delays the send to collect more records, which actually increases latency, not decreases it. It also does not address the 4 MB record size limitation.

2. ❌ **B. Set `acks` to "all" to ensure durability.**  
   **Incorrect**. While `acks=all` increases reliability, it also increases round‑trip latency and does not affect the ability to send 4 MB records. The problem is about record size, not durability.

3. ✅ **C. Increase `max.request.size` to at least 4 MB.**  
   **Correct**. `max.request.size` is the maximum size of a request that can be sent to the broker. Setting it to ≥ the largest record size (plus a small margin) prevents size‑related errors and allows the producer to send large records efficiently.

4. ❌ **D. Reduce `buffer.memory` to 1 MB to force the producer to flush faster.**  
   **Incorrect**. A smaller buffer would cause the producer to block or back‑off, increasing latency and potentially dropping records. It does not solve the large record size issue.

5. ❌ **E. Increase the `batch.size` property to 4 MB.**  
   **Incorrect**. The `batch.size` setting controls how many bytes the producer buffers per request before sending. While a larger batch can improve throughput, the default 16 KiB does not prevent a 4 MB record from being sent. However, `batch.size` is limited by `max.request.size`, setting it alone is insufficient and may waste memory.

</details>

## Question 60 (Streams Development):
Which of the following statements correctly describe how Kafka Streams ensures fault tolerance, state durability, and data consistency for stateful operators?

- A. Kafka Streams writes its local state store to an external database for durability.
- B. Global tables are replicated to all instances to provide read-only access to a global view of the data.
- C. Each state store is mirrored by a changelog topic that replicates state to other cluster nodes.
- D. Repartition topics are created automatically to support joins and aggregations across keys.
- E. Kafka Streams uses exactly-once semantics (EOS) to prevent duplicate records when reprocessing after a failure.
- F. The default retention period for changelog topics is 7 days, after which old state is discarded.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

Kafka Streams guarantees fault tolerance for stateful operators by persisting each local state store to a replicated changelog topic. This replication ensures that if an instance fails, another can recover the exact state from the topic. Exactly‑once semantics (EOS) further guarantees that state updates and output records are written atomically, preventing duplicates during replay. Global tables replicate the entire table to every instance, providing a consistent read‑only view without repartitioning. Common misconceptions include assuming an external DB is required or that retention of changelog topics is limited, in reality, changelog topics for non-windowed stores are log-compacted (`cleanup.policy=compact`, latest value per key kept indefinitely), while changelogs of windowed stores use `compact,delete` with retention = window retention + 1 day (not 7 days), and they rely on Kafka’s replication. Option D (repartition topics) is a true statement but concerns re-keying, not fault tolerance/durability, hence not selected. These mechanisms together provide robust consistency and durability for stream processing applications.

Source: https://kafka.apache.org/documentation/streams/architecture and https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (state store changelog configs), Kafka: The Definitive Guide 2nd ed., ch. 14 (local state, rebalancing, exactly-once in Streams).

**Detailed explanation of each option:**

1. ❌ **A. Kafka Streams writes its local state store to an external database for durability.**  
   **Incorrect**. Kafka Streams relies on its own changelog topics to replicate the local state, it does not persist state to an external database.

2. ✅ **B. Global tables are replicated to all instances to provide read-only access to a global view of the data.**  
   **Correct**. A GlobalKTable materializes a copy of the KTable on every instance, enabling local lookups and consistency without a repartition.

3. ✅ **C. Each state store is mirrored by a changelog topic that replicates state to other cluster nodes.**  
   **Correct**. State stores are backed by changelog topics that are replicated across the Kafka cluster, providing durability and fault tolerance.

4. ❌ **D. Repartition topics are created automatically to support joins and aggregations across keys.**  
   **Incorrect**. for this context. While repartition topics are indeed used for re‑keying streams, the statement does not describe fault tolerance or state durability mechanisms.

5. ✅ **E. Kafka Streams uses exactly-once semantics (EOS) to prevent duplicate records when reprocessing after a failure.**  
   **Correct**. EOS guarantees that state changes and output records are written atomically and idempotently, ensuring consistency after a failure.

6. ❌ **F. The default retention period for changelog topics is 7 days, after which old state is discarded.**  
   **Incorrect**. Changelog topics are log-compacted rather than time-retained (windowed stores: retention = window retention + 1 day), so there is no 7-day default after which state is discarded.

</details>
