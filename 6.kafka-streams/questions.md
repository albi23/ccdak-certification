> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1:
In a Kafka cluster, two topics, `TopicA` and `TopicB`, are configured to be co-partitioned. This means they have an identical number of partitions, and messages in corresponding partitions are related to each other. Given the following configurations for these topics:

- `TopicA` has 6 partitions.
- `TopicB` is configured with the same number of partitions as `TopicA`.
- Both topics are consumed by a single consumer group with the `max.poll.records` configuration set to 500.

Assuming that the consumer processes messages from both topics in a manner that maintains their relationship, what is a critical consideration for ensuring data consistency across these co-partitioned topics?

1. Ensuring both topics have the same `replication.factor` to prevent data loss.
2. Using a custom partitioner that assigns messages to the same partition number in both topics based on key.
3. Configuring `TopicB` with a higher number of partitions than `TopicA` to ensure scalability.
4. Increasing `max.poll.records` to a higher value to ensure more messages are processed in each poll.

Choose the correct answer.

<details>
<summary>Response:</summary> 

The correct answer is **2. Using a custom partitioner that assigns messages to the same partition number in both topics based on key.**

**Explanation:**
Co-partitioning requires the same number of partitions AND the same partitioning strategy (same key type/serialization and the same partitioner), so that records with the same key land in the same partition number in both topics. The replication factor, `max.poll.records` and a different partition count do not affect co-partitioning.

</details>

## Question 2:
For a streaming application processing data from two co-partitioned topics, `TopicX` and `TopicY`, which configuration ensures that the stream processing application maintains message ordering and correlation between these topics?

1. Configuring both topics with `log.compaction=true` to ensure message deduplication.
2. Ensuring that both topics are consumed by the application in separate threads.
3. Assigning a unique consumer group for each topic to maximize parallel processing.
4. Ensuring both topics use the same key for related messages and are consumed by the same consumer group.

Choose the correct answer.

<details>
<summary>Response:</summary> 

The correct answer is **4. Ensuring both topics use the same key for related messages and are consumed by the same consumer group.**

</details>

## Question 3:
In a Kafka Streams application that enriches user clickstream data by joining it with user profile information, what should be the characteristics of the topic storing user profiles for optimal join operations?

```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> clicks = builder.stream("clickstream-topic");
KTable<String, String> profiles = builder.table("user-profiles-topic");
KStream<String, String> enrichedClicks = clicks.join(profiles,
    (click, profile) -> click + " enriched with " + profile);
enrichedClicks.to("enriched-clickstream-topic");
builder.build();
```

Choose the best topic configuration for `user-profiles-topic`.

1. compression.type = snappy
2. cleanup.policy = delete
3. cleanup.policy = compact

<details>
<summary>Response:</summary> 

The correct answer is **3. cleanup.policy = compact.**

**Explanation:**
The `user-profiles-topic`, being used as a `KTable`, represents a changelog of user profile information. Using a `cleanup.policy` of `compact` ensures that the topic retains only the latest state of each user profile, which is essential for performing accurate and efficient joins with the clickstream data.

</details>

## Question 4:
When developing a Kafka Streams application that aggregates transaction amounts by user ID from a financial transactions topic, which key-serde configuration ensures optimal processing and state store management?

```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, BigDecimal> transactions = builder.stream("transactions-topic",
    Consumed.with(Serdes.String(), Serdes.BigDecimal()));
KTable<String, BigDecimal> aggregatedTransactions = transactions
    .groupByKey()
    .reduce(BigDecimal::add, Materialized.as("aggregated-transactions-store"));
aggregatedTransactions.toStream().to("aggregated-transactions-topic");
builder.build();
```

Select the correct Serde configuration for both the input topic and the state store.

1. Key Serde = Serdes.String(), Value Serde = Serdes.BigDecimal()
2. Key Serde = Serdes.Long(), Value Serde = Serdes.Double()
3. Key Serde = Serdes.String(), Value Serde = Serdes.String()

<details>
<summary>Response:</summary> 

The correct answer is **1. Key Serde = Serdes.String(), Value Serde = Serdes.BigDecimal().**

**Explanation:**
The application processes financial transactions where the key is presumably a user ID (as a String) and the value is a transaction amount (as a BigDecimal). Using `Serdes.String()` for the key and `Serdes.BigDecimal()` for the value ensures that the data is correctly serialized/deserialized for both Kafka topic interaction and state store management, facilitating efficient and accurate aggregations.

`Materialized.as("...")` specifies no serdes, so none are set explicitly: `groupByKey()` without `Grouped` inherits the key/value serdes of the source KStream (here from `Consumed.with(String, BigDecimal)`), and the store and the `to(...)` sink use those inherited serdes (the `default.key.serde`/`default.value.serde` configs apply only when no serde is inherited or given). Hence String/BigDecimal.

Source: Apache Kafka Streams docs, "Data Types and Serialization" (https://kafka.apache.org/documentation/streams/developer-guide/datatypes.html) and `KStream#groupByKey()` javadoc; book ch. 14, pp. 412-413 (Serde per type).

</details>

## Question 5: [x]
In a Kafka Streams application designed to monitor and alert on abnormal application log levels, logs are streamed from a source topic. Each record contains the log level (e.g., ERROR, WARN, INFO) and the log message. The application filters for ERROR level logs and forwards them to an output topic for immediate action. Consider the following Kafka Streams code snippet:

```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> logs = builder.stream("application-logs");
KStream<String, String> errorLogs = logs.filter((key, value) -> value.contains("ERROR"));
errorLogs.to("error-logs-topic");
builder.build();
```

Log records have no meaningful update semantics (every log line must be processed, and keys may repeat or be null). Which setting is the most appropriate for the `application-logs` source topic?

1. cleanup.policy = delete
2. cleanup.policy = compact
3. min.insync.replicas = 2

<details>
<summary>Response:</summary> 

The correct answer is **1. cleanup.policy = delete.**

**Explanation:**
Logs are an event stream: every record must be processed, so the topic should use time/size-based deletion (`cleanup.policy=delete`, the default). `compact` keeps only the latest record per key, silently dropping log events (and fails for null keys), which suits changelog/KTable-style topics only. `min.insync.replicas` only affects producer durability with `acks=all`; it has no effect on this application's processing. (The original wording asked about "performance", but none of the topic settings changes Streams throughput; parallelism comes from the partition count.)

Source: Apache Kafka docs, topic configs `cleanup.policy` (https://kafka.apache.org/documentation/#topicconfigs_cleanup.policy); book ch. 6 (log compaction) and ch. 14, p. 412.

</details>

## Question 6: [x]
For a Kafka Streams application that processes customer orders to calculate real-time metrics such as total orders per hour, considering the following code:

```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, Order> orders = builder.stream("orders-topic",
    Consumed.with(Serdes.String(), new JsonSerde<>(Order.class)));
KTable<Windowed<String>, Long> ordersPerHour = orders
    .groupByKey()
    .windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofHours(1)))
    .count(Materialized.as("orders-per-hour-metrics"));
ordersPerHour.toStream().to("orders-metrics-topic");
builder.build();
```

Which configuration ensures that the state store `orders-per-hour-metrics` is optimally managed for performance and recovery?

1. replication.factor = 3
2. state.store.log.compaction = true
3. commit.interval.ms = 100

<details>
<summary>Response:</summary> 

The correct answer is **1. replication.factor = 3.**

**Explanation:**
Every state store is backed by a changelog topic, which is used to restore the store after a failure or restart. The Kafka Streams `replication.factor` setting controls the replication factor of the internal changelog and repartition topics, so a value of 3 keeps the state recoverable if a broker fails. `state.store.log.compaction` is not a valid configuration (changelog topics are compacted automatically, with delete+compact for windowed stores), and lowering `commit.interval.ms` to 100 only increases commit overhead and does not improve recovery.

</details>

## Question 7 [x]

Is Kafka Streams DSL ANSI SQL compliant?

- A. Yes
- B. No
- C. Partially
- D. It depends on the version

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Kafka Streams DSL, which is used for writing stream processing applications, is not ANSI SQL compliant. It uses a fluent Java API that is inspired by SQL but does not aim for full compliance.

- A is incorrect as Kafka Streams DSL is not designed to be ANSI SQL compliant.
- C and D are incorrect because the non-compliance is not partial or version-dependent. It's a design choice.

</details>

## Question 8

What is the primary language used for writing Kafka Streams applications?

- A. Python
- B. Java
- C. Scala
- D. SQL

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Kafka Streams is a Java library for building real-time, highly scalable, fault-tolerant, distributed applications for stream processing. The primary language for writing Kafka Streams applications is Java.

- A, C, D are incorrect because while Kafka Streams integrates with other JVM languages like Scala, and there are some Python wrappers available, the native and primary language is Java.

</details>

## Question 9

What is the role of RocksDB in Kafka Streams?

- A. It is used for storing output topics.
- B. It is used for storing intermediate processing state.
- C. It is used for storing the Kafka Streams application code.
- D. It is not used in Kafka Streams.

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In Kafka Streams, RocksDB is used as the default local state store for storing intermediate processing state. This state represents the computed results of the stream processing that need to be maintained between processing cycles.

- A is incorrect because output topics are stored in Kafka, not RocksDB.
- C is incorrect as application code is not stored in RocksDB.
- D is incorrect because RocksDB is indeed used in Kafka Streams for state management.

Source: Kafka: The Definitive Guide 2nd Edition, Chapter 14:
Local state is stored in-memory using embedded RocksDB, which also persists the data to disk for quick recovery after restarts.

</details>

## Question 10 [x]

In a Kafka Streams application, where are the processing topology configurations stored?

- A. In a special Kafka topic named `streams-configs`
- B. In Zookeeper under the `/kafka-streams` znode
- C. In the Kafka Streams application code itself
- D. In a separate config file read by the Kafka Streams application

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In a Kafka Streams application, the processing topology (the DAG of processing nodes) is defined in the application code itself using the Kafka Streams DSL or the Processor API.

- A, B are incorrect because Kafka Streams does not use a special topic or Zookeeper for storing topology configurations.
- D is incorrect as the topology is not defined in a separate config file, but rather in the application code.

```

StreamsBuilder builder = new StreamsBuilder();
builder.stream("input-topic")
       .filter((k, v) -> v != null)
       .mapValues(v -> v.toUpperCase())
       .to("output-topic");

Topology topology = builder.build();
```

</details>

## Question 11

You are implementing a Kafka Streams application. The input is a KStream from a topic where the message values are Avro records written with Confluent Schema Registry, and your project has Avro-generated Java classes (specific records) for the schema. What should you set for the `default.value.serde` property in the Streams configuration?

- A. `Serdes.String()`
- B. `Serdes.ByteArray()`
- C. `SpecificAvroSerde` (together with `schema.registry.url`)
- D. `GenericAvroSerde`

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Confluent's Avro serdes (`io.confluent.kafka.streams.serdes.avro.SpecificAvroSerde` / `GenericAvroSerde`) are used with Schema Registry, and they must be given `schema.registry.url` (serde config). `default.value.serde` takes the serde class name (`SpecificAvroSerde.class`). With generated classes, `SpecificAvroSerde` yields typed objects; `GenericAvroSerde` is the choice when there are no generated classes (returns `GenericRecord`).

- A is incorrect: the values are Avro, not String.
- B would only give raw bytes (manual deserialization), not a proper Avro deserialization.
- D works only for `GenericRecord`; with generated classes it is not the best fit.

Source: Confluent docs, "Kafka Streams Data Types and Serialization" (https://docs.confluent.io/platform/current/streams/developer-guide/datatypes.html).

</details>

## Question 12

What is the recommended way to increase the throughput of a Kafka Streams application that does a simple stateless `map` transformation on the input data and is CPU-bound on a single instance?

- A. Increase the number of partitions of the output topic
- B. Enable state store caching
- C. Increase `num.stream.threads` (up to the number of input partitions) or start more application instances
- D. Disable logging

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Kafka Streams parallelism is based on tasks, one per input partition; tasks are the unit of parallelism and are distributed over the threads (`num.stream.threads`) of all application instances. To process faster, add threads, and when the server runs out of resources, start another instance (up to the number of tasks/partitions).

- A is incorrect: output partitions do not determine the number of tasks.
- B is not applicable: caching only affects stateful operations (stores/KTables); `map` is stateless.
- D is incorrect: there is no state/changelog logging in a stateless `map`, and log verbosity is not the throughput limit.

Source: book ch. 14, "Scaling the Topology", pp. 412-413 ("If we want to process faster, add more threads"); Kafka Streams docs, Architecture / Parallelism Model (https://kafka.apache.org/documentation/streams/architecture#streams_architecture_tasks).

</details>

## Question 13

You are running a Kafka Streams application in a Docker container. The application performs a complex join operation and maintains a large state store. Which of the following would provide the greatest performance improvement when restarting the container?

- A. Increase the heap size of the Docker container
- B. Mount a high-performance SSD for the RocksDB directory
- C. Increase the number of replicas for the input topics
- D. Use a more powerful CPU for the Docker host

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In a Kafka Streams application that maintains a large state store (e.g., for a complex join operation), the bottleneck during restarts is often the time taken to restore the state store from the changelog topic. By mounting a high-performance SSD for the RocksDB directory used by Kafka Streams, the state restore process can be significantly speeded up.

- A is less effective because the heap is used for processing, but the state store is stored on disk (in RocksDB) and loaded into off-heap memory.
- C does not directly impact the state restore performance because the changelogs are already replicated.
- D can help with processing speed but does not address the state restore bottleneck.

</details>

## Question 14

You are deploying a Kafka Streams application that joins two high-volume streams. Which of the following is LEAST likely to improve the performance of the application?

- A. Ensuring that the two input streams have the same number of partitions
- B. Increasing the number of standby replicas for the state store
- C. Tuning the `statestore.cache.max.bytes` parameter (formerly `cache.max.bytes.buffering`)
- D. Increasing the `num.stream.threads` parameter

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Increasing the number of standby replicas for the state store in a Kafka Streams application can provide better fault tolerance by allowing faster failover to a replica if a node fails. However, it is unlikely to improve the normal operating performance of the application.

In contrast:

- A can improve performance by allowing the join to be performed more efficiently, with each partition able to be processed independently.
- C can improve performance by allowing more data to be buffered in memory before being flushed to the state store, reducing I/O overhead.
- D can improve performance by allowing more partitions to be processed concurrently, up to the number of partitions of the input topics.

```
┌─────────────────────────────────────────────────────┐
│          CO-PARTITIONING REQUIREMENTS               │
│                                                     │
│  Join Type                  | Co-partitioning       │
│  ─────────────────────────────────────────────────  │
│  KStream-KStream            | ✅ Required           │
│  KTable-KTable (Equi-Join)  | ✅ Required           │
│  KStream-KTable             | ✅ Required           │
│                             |                       │
│  KTable-KTable Foreign-Key  | ❌ Not Required       │
│  KStream-GlobalKTable       | ❌ not Required       │
└─────────────────────────────────────────────────────┘
```
</details>

## Question 15

Which of the following stream processing operations can be considered stateful? (Select all that apply)

- A. Filter: Discarding messages based on a condition
- B. Map: Transforming messages from one format to another
- C. Aggregate: Combining multiple messages into a single result
- D. Join: Combining messages from two different streams based on a common key
- E. Peek: Performing an action on each message without modifying it

<details>
<summary>Response:</summary> 

**Answer:** C, D

**Explanation:**
In stream processing, stateful operations are those that maintain and update a state based on the processed messages. They require the stream processor to keep track of some information over time.

1. Aggregate: Aggregation operations, such as counting, summing, or averaging values, are stateful because they need to maintain a running state of the aggregated result. The state is updated as new messages arrive, and the final result depends on the accumulated state over time.

2. Join: Join operations, especially window-based joins, are stateful because they need to maintain a state of the messages from both streams within a specified time window. The stream processor must store the messages temporarily to match and combine them based on a common key.

The other operations mentioned are generally considered stateless:

- Filter: Filtering messages based on a condition does not require maintaining any state. Each message is evaluated independently against the condition, and the decision to keep or discard the message is made solely based on the current message.

- Map: Transforming messages from one format to another is typically a stateless operation. Each message is processed independently, and the transformation logic is applied to each message without relying on any previous state.

- Peek: Performing an action on each message without modifying it, such as logging or publishing metrics, is usually stateless. The action is performed on each message independently, without maintaining any state across messages.

It's important to note that the specific implementation and requirements of a stream processing application can introduce statefulness to operations that are typically considered stateless. However, in general, aggregation and join operations are inherently stateful, while filtering, mapping, and peeking are often stateless.

</details>

## Question 16

What is the purpose of state stores in Kafka Streams?

- A. To persist the intermediate results and enable fault tolerance
- B. To cache the input messages for faster processing
- C. To store the final output of the stream processing application
- D. To maintain the configuration of the Kafka Streams application

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In Kafka Streams, state stores play a crucial role in persisting the intermediate results and enabling fault tolerance for stateful operations.

When a Kafka Streams application performs stateful operations, such as aggregations or joins, it needs to maintain and update a state based on the processed messages. State stores provide a way to persistently store this state outside of the streaming application's memory.

The purpose of state stores is as follows:

1. Persistence: State stores allow the streaming application to persist the intermediate state to disk. This ensures that the state is not lost if the application fails or needs to be restarted. When the application restarts, it can reload the state from the state stores and resume processing from where it left off.

2. Fault Tolerance: By persisting the state, state stores enable fault tolerance in Kafka Streams applications. If a node in the Kafka Streams cluster fails, another node (or a standby replica) can take over the processing and rebuild the state from the store's changelog topic in Kafka. This ensures that the processing can continue without losing the accumulated state.

3. Queryable State: State stores in Kafka Streams also provide the ability to query the current state of the application. This allows other applications or services to retrieve the latest computed state without needing to process the entire stream again. Queryable state is useful for serving real-time results or building interactive applications.

State stores in Kafka Streams are backed by an embedded key-value store, such as RocksDB, which provides efficient storage and retrieval of state data. Kafka Streams takes care of managing the state stores, including their creation, updates, and fault tolerance, based on the defined topology and configuration.

It's important to note that state stores are not used for caching input messages or storing the final output of the stream processing application. They are specifically designed to persist and manage the intermediate state required for stateful operations.

**Related Area:** Kafka Streams

</details>

## Question 17

How does Kafka Streams handle state recovery in case of a failure?

- A. By replaying all the input messages from the beginning
- B. By restoring the state from a snapshot stored in Kafka
- C. By rebuilding the state from the change log topic
- D. By retrieving the state from an external database

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Kafka Streams provides built-in fault tolerance and state recovery mechanisms to handle failures and ensure the integrity of the processing state. When a failure occurs, Kafka Streams automatically recovers the state using the change log topic.

Here's how state recovery works in Kafka Streams:

1. Change Log Topic: For each state store in a Kafka Streams application, Kafka Streams creates a corresponding change log topic. The change log topic acts as a persistent log of all the state changes that occurred in the state store.

2. State Updates: Whenever the state in a state store is updated as a result of processing messages, Kafka Streams writes the state changes to the change log topic. Each record in the change log topic represents a state update and includes the key, value, and timestamp of the update.

3. Failure Recovery: If a failure occurs and a Kafka Streams application needs to recover its state, it starts by reading the change log topic from the beginning. The application replays the state changes from the change log topic to rebuild the state store. By replaying the state changes in the correct order, the application can restore its state to the latest consistent point before the failure.

4. Resuming Processing: Once the state is recovered from the change log topic, the Kafka Streams application can resume processing from the point where it left off. It continues to read input messages from the source topics and applies the processing logic to update the state and generate output.

By leveraging the change log topic, Kafka Streams ensures that the state can be recovered accurately and efficiently in case of failures. The change log topic acts as a durable and replicated log of state changes, providing a reliable source of truth for state recovery.

It's important to note that Kafka Streams does not rely on replaying all the input messages from the beginning or storing snapshots of the state in Kafka itself. The change log topic is specifically designed to capture and persist the state changes, enabling quick and precise state recovery.

Additionally, Kafka Streams does not rely on external databases for state storage or recovery. The state is managed internally within Kafka Streams using the embedded key-value stores and the change log topics.

</details>

## Question 18

You have a Kafka Streams application that processes messages from an input topic with 6 partitions. The application performs a stateful aggregation using a KTable. How many local state stores will be created by default?

- A. 1
- B. 3
- C. 6
- D. 12

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In a Kafka Streams application, when you perform a stateful operation such as aggregation using a KTable, Kafka Streams creates local state stores to maintain the aggregated state for each partition of the input topic. By default, Kafka Streams creates one local state store per partition.

In this scenario, with an input topic having 6 partitions, the Kafka Streams application will create 6 local state stores by default, one for each partition.

Each local state store is associated with a specific partition and maintains the aggregated state for that partition. When a message is processed from a particular partition, the corresponding local state store is updated accordingly.

Kafka Streams creates one stream task per input partition (more precisely, per partition of the co-partitioned sub-topology), and each task owns its own state store instance. The number of threads (`num.stream.threads`) or application instances only determines how these tasks are distributed; it never changes the number of tasks, and a partition is never processed by more than one task.

It's worth noting that the actual number of local state stores created may be influenced by factors such as state store configuration, stream processing topology, and the specific Kafka Streams version being used.

</details>

## Question 19

What is the main advantage of using Kafka Streams DSL over the Processor API for stream processing?

- A. Kafka Streams DSL provides better performance compared to the Processor API
- B. Kafka Streams DSL offers a higher-level, declarative approach to defining stream processing logic
- C. Kafka Streams DSL supports stateful operations, while the Processor API is limited to stateless operations
- D. Kafka Streams DSL allows for easier integration with external systems compared to the Processor API

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The main advantage of using Kafka Streams DSL (Domain-Specific Language) over the Processor API for stream processing is that it offers a higher-level, declarative approach to defining stream processing logic.

Kafka Streams DSL provides a set of high-level operations and constructs that allow developers to express stream processing logic in a more concise and expressive manner. With the DSL, you can chain together operations like `map`, `filter`, `groupBy`, `aggregate`, and `join` to define the desired stream processing topology. The DSL abstracts away low-level details and provides a more intuitive and readable way to define the processing logic.

On the other hand, the Processor API is a lower-level API that provides more fine-grained control over the stream processing topology. With the Processor API, you need to define individual processor nodes and connect them manually to create the desired processing flow. While this provides more flexibility, it requires more code and can be more complex to implement and maintain compared to the DSL.

Both Kafka Streams DSL and the Processor API offer similar performance characteristics and support stateful operations. They also provide integration capabilities with external systems. The choice between the two depends on the specific requirements of the application and the level of control and customization needed.


</details>

## Question 20

When using Kafka Streams DSL, how can you perform a stateful operation on a KStream?

- A. By using the `map` operation to modify the stream's values
- B. By using the `filter` operation to remove unwanted records from the stream
- C. By using the `groupByKey` operation followed by an aggregation (`count`, `reduce`, `aggregate`)
- D. By using the `mapValues` operation to transform the stream's values

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
To perform a stateful operation on a KStream using Kafka Streams DSL, you first group the stream with `groupByKey` (or `groupBy`), which on its own only prepares the data; the aggregation that follows is what is stateful. The `groupByKey` operation groups the records of a KStream based on their keys, creating a grouped stream called KGroupedStream.

Once you have a KGroupedStream, you can apply stateful operations such as `aggregate`, `reduce`, or `count` to perform aggregations or computations on the grouped records. These stateful operations maintain and update the state for each unique key, allowing you to perform calculations or transformations that depend on the previous state.

For example, to count the occurrences of each key in a KStream, you can use the following code snippet:

```java
KStream<String, String> textLines = ...;
KTable<String, Long> wordCounts = textLines
  .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
  .groupBy((key, word) -> word)
  .count();
```

In this example, the `groupBy` operation groups the stream by the words extracted from the text lines, and the `count` operation counts the occurrences of each word, maintaining the state for each word.

The `map` and `mapValues` operations are used for stateless transformations of the stream's keys and values, respectively. The `filter` operation is used to remove records from the stream based on a predicate, but it does not perform any stateful computation.

</details>

## Question 21

What is the role of the `StateStore` in Kafka Streams?

- A. To store the intermediate results of stream processing operations
- B. To store the configuration properties for Kafka Streams applications
- C. To store the metadata information about the Kafka cluster
- D. To store the consumer offsets for Kafka Streams applications

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In Kafka Streams, the `StateStore` plays a crucial role in storing and managing the state required for stateful stream processing operations. When you perform stateful operations like aggregations, joins, or windowing in Kafka Streams, the intermediate results and the state of the computation need to be stored somewhere. This is where the `StateStore` comes into the picture.

The `StateStore` is an abstraction provided by Kafka Streams that allows you to store and retrieve key-value pairs. It acts as a local database or cache that is accessible by the stream processing application. The `StateStore` is backed by a persistent storage layer, typically using RocksDB or an in-memory store, depending on the configuration.

When you perform stateful operations in Kafka Streams, the intermediate results and the state are automatically stored in the appropriate `StateStore` instances. These `StateStore` instances are managed by Kafka Streams and are fault-tolerant, meaning that they can be automatically restored in case of failures.

The `StateStore` is not used for storing configuration properties, metadata information about the Kafka cluster, or consumer offsets. It is specifically designed to store the intermediate state required for stateful stream processing operations, enabling fault-tolerant and scalable stateful processing in Kafka Streams applications.

</details>

## Question 22

You have an e-commerce application that maintains user information. Which of the following data is best suited to be modeled as a KTable in Kafka Streams?

- A. User clickstream data
- B. User order history
- C. User profile information
- D. User session data

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In the context of an e-commerce application, user profile information is best suited to be modeled as a KTable in Kafka Streams. A KTable represents a changelog stream, where each record represents an update to the value of a key. It is suitable for storing and updating data that has a primary key and can be queried or joined with other streams or tables.

User profile information typically consists of relatively static data associated with each user, such as their name, email address, shipping address, and preferences. This data can be updated over time, but the updates are less frequent compared to other types of data like clickstream or order history.

By modeling user profile information as a KTable, you can efficiently store and retrieve the latest state of each user's profile. The KTable will maintain the most recent value for each user key, allowing you to query and join user profiles with other streams or tables in your application.

On the other hand:
- User clickstream data is better modeled as a KStream, as it represents a continuous flow of user actions and interactions.
- User order history is also better modeled as a KStream, as it represents a series of discrete events over time.
- User session data can be modeled as either a KStream or a windowed KTable, depending on the specific requirements and analysis needs.

</details>

## Question 23

In an IoT application, you have a stream of sensor readings that need to be processed in real-time. Which of the following is the most suitable way to model this data in Kafka Streams?

- A. As a KTable, with each sensor reading as a key-value pair
- B. As a KStream, with each sensor reading as a record
- C. As a GlobalKTable, with each sensor reading as a key-value pair
- D. As a windowed KTable, with each sensor reading as a key-value pair

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In an IoT application that processes sensor readings in real-time, the most suitable way to model the data in Kafka Streams is as a KStream, with each sensor reading as a record.

A KStream represents an unbounded sequence of records, where each record is an independent event. It is suitable for handling continuous, high-volume data streams that require real-time processing. In the case of sensor readings, each reading is a standalone event that needs to be processed as it arrives.

By modeling sensor readings as a KStream, you can perform real-time transformations, aggregations, and analysis on the incoming data. You can apply operations like filtering, mapping, and windowing to process the sensor readings and derive meaningful insights or trigger actions based on the data.

The other options are less suitable for this scenario:
- A KTable is not appropriate because sensor readings are not typically updated or queried by key. Each reading is a new event rather than an update to an existing value.
- A GlobalKTable is fully replicated to every application instance and is meant for relatively small, slowly changing reference data, which is not the case for a continuous stream of sensor readings.
- A windowed KTable is used for aggregating and storing data within a specific time window, but it may not be necessary for real-time processing of individual sensor readings.

Therefore, modeling sensor readings as a KStream provides the most flexibility and efficiency for real-time processing in an IoT application.


</details>

## Question 24

You are building a real-time analytics application that tracks user behavior on a website. Which of the following data is most appropriate to be modeled as a KStream in Kafka Streams?

- A. User demographic information
- B. User navigation events
- C. User purchase history
- D. User authentication data

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In a real-time analytics application that tracks user behavior on a website, user navigation events are most appropriate to be modeled as a KStream in Kafka Streams.

User navigation events represent the actions and interactions of users as they navigate through the website. These events occur continuously and in real-time as users click on links, visit pages, perform searches, and interact with various elements on the website. Each navigation event is a discrete, independent record that needs to be processed and analyzed as it happens.

By modeling user navigation events as a KStream, you can capture and process the events in real-time. You can apply operations like filtering, mapping, and aggregating to analyze user behavior, track user journeys, and derive insights from the navigation data. For example, you can count page views, identify popular paths, or detect anomalies in user behavior.

The other options are less suitable for modeling real-time user behavior:
- User demographic information is relatively static data that is better modeled as a KTable.
- User purchase history represents individual transactions and can be modeled as either a KStream or a KTable, depending on the specific analysis requirements.
- User authentication data is typically static and not directly related to real-time user behavior tracking.

Therefore, modeling user navigation events as a KStream provides the most suitable representation for real-time analysis of user behavior on a website.


</details>