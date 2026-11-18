> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1

Which of the following is stored as a committed-offset record in the Kafka `__consumer_offsets` topic? (Select one)

- A. The latest committed offset for each consumer group, topic and partition
- B. The last produced message for each topic partition
- C. The earliest committed offset for each consumer group
- D. The log-end offset (high watermark) of each topic partition

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
Committed offsets are written to `__consumer_offsets` as records keyed by (group ID, topic, partition) with the committed offset as the value. Because the topic is compacted, only the latest commit per key is retained, so there is no "earliest committed offset" (C).

B: Produced messages are stored in the topic partitions themselves. D: The high watermark / log-end offset is tracked by the partition leader, not in `__consumer_offsets`.

Note: the same internal topic also holds group metadata records (membership/assignment) written by the group coordinator, which is why the question is limited to committed-offset records.

Source: Kafka: The Definitive Guide, 2nd ed., Ch. 4 (Committing Offsets: "commit offset ... to a special `__consumer_offsets` topic"); https://kafka.apache.org/documentation/#impl_offsettracking

</details>

## Question 2

There are two consumers C1 and C2 belonging to the same group G subscribed to topics T1, T2, and T3. Each topic has 4 partitions. Assuming all partitions have data, how many partitions will each consumer be assigned with the Range Assignor?

- A. C1: 6 partitions, C2: 6 partitions
- B. C1: 4 partitions, C2: 8 partitions
- C. C1: all partitions of T1 and T2, C2: all partitions of T3
- D. C1: 1 partition from each topic, C2: 3 partitions from each topic

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
With the Range Assignor, each consumer will be assigned a contiguous range of partitions from each topic. In this case, with 4 partitions per topic and 2 consumers, each consumer will get 2 partitions from each topic, i.e. 6 partitions in total (C1: T1-0,T1-1,T2-0,T2-1,T3-0,T3-1; C2: the remaining ones).

</details>

## Question 3

There are four consumers C1, C2, C3, C4 belonging to the same group G subscribed to two topics T1 and T2. T1 has 3 partitions and T2 has 2 partitions. With the Round Robin Assignor, which consumer(s) will be assigned partition 2 from topic T1?

- A. C1
- B. C2
- C. C3
- D. C4

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
With the Round Robin Assignor, partitions are assigned to consumers sequentially, one by one, going around all the consumers repeatedly. In this case, the assignment will be:

- C1: T1-0, T2-1
- C2: T1-1
- C3: T1-2
- C4: T2-0

So partition 2 from topic T1 will be assigned to consumer C3.

</details>

## Question 4

There are three consumers C1, C2, C3 belonging to the same group G subscribed to a topic T. The topic has 10 partitions. If the Sticky Assignor is used, and C1 leaves the group, how will the partitions be rebalanced?

- A. All partitions will be reassigned evenly among C2 and C3
- B. C2 and C3 will retain their existing partitions, and the partitions from C1 will be reassigned to either C2 or C3
- C. All partitions will be reassigned randomly to C2 and C3
- D. C2 and C3 will retain their existing partitions, and the partitions from C1 will not be reassigned

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The Sticky Assignor aims to minimize partition movement when the group membership changes. When a consumer leaves, it tries to reassign the partitions from the leaving consumer to the remaining consumers, while keeping the existing assignments as sticky as possible.

- A, C are not correct because they involve unnecessary partition movement.
- D is incorrect because the partitions from the leaving consumer will be reassigned, not left unassigned.

</details>

## Question 5

A Kafka Streams application tries to consume from an input topic partition. It receives an 'Offset Out Of Range' error from the broker. How should the application handle this?

- A. Reset the consumer offset to the earliest offset and retry
- B. Reset the consumer offset to the latest offset and retry
- C. Trigger a shutdown of the Streams application
- D. Ignore the error and continue processing other partitions

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
- A. 'Offset Out Of Range' error in Kafka Streams indicates that the application is trying to fetch from an offset that is no longer available in the partition, usually because the data has been deleted due to retention policies. The consumer handles it according to its `auto.offset.reset` policy (Kafka Streams default is `latest`; `none` makes it throw an exception). To avoid losing data, the recommended handling is to reset to the earliest available offset (`auto.offset.reset=earliest`) and retry consuming from there.

- B is not recommended because resetting to the latest offset will skip over the missing data.
- C is too extreme. The error can be handled without shutting down the entire application.
- D will lead to data loss as the partition with the error will be ignored.

</details>

## Question 6

You are designing a Kafka consumer application that will consume messages from a topic. The messages in the topic are in JSON format. Which of the following properties should you set in the consumer configuration?

- A. `key.deserializer=JsonDeserializer`
- B. `value.deserializer=JsonDeserializer`
- C. `key.deserializer=StringDeserializer`
- D. `value.deserializer=StringDeserializer`

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In a Kafka consumer application, you need to specify how to deserialize the message keys and values. Since the messages in the topic are in JSON format, you should set:

- `value.deserializer=JsonDeserializer`: (Apache Kafka core does not ship a JSON deserializer; one is provided by Kafka Connect's `connect-json` module, Confluent serdes or Spring, or you write a custom `Deserializer`.) This tells the consumer to use the `JsonDeserializer` to deserialize the message values from JSON to Java objects.

The other options are not correct:

- A: `key.deserializer=JsonDeserializer` would be correct if the message keys were also in JSON format. However, the question doesn't specify the key format.
- C and D: `StringDeserializer` is not appropriate because the message values are in JSON format, not plain strings.

</details>

## Question 7

A consumer wants to read messages from a specific partition of a topic. Which of the following methods should be used?

- A. `KafkaConsumer.subscribe(String topic, int partition)`
- B. `KafkaConsumer.assign(Collection<TopicPartition> partitions)`
- C. `KafkaConsumer.subscribe(Collection<TopicPartition> partitions)`
- D. `KafkaConsumer.assign(String topic, int partition)`

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
To read messages from a specific partition of a topic, a consumer should use the `assign` method of the `KafkaConsumer` class.

The `assign` method takes a collection of `TopicPartition` objects as a parameter. Each `TopicPartition` represents a specific partition of a topic. By passing a collection of `TopicPartition` objects to `assign`, the consumer is explicitly assigned to those specific partitions.

The other options are incorrect:

- A and D are incorrect because `KafkaConsumer` does not have a method that takes a topic and partition as separate parameters.
- C is incorrect because `subscribe` is used for subscribing to entire topics, not specific partitions. When you subscribe to a topic, Kafka automatically assigns partitions to the consumer.

Using `assign` allows for fine-grained control over which partitions a consumer reads from. It's useful in scenarios where you want to manually balance partitions across consumers or implement a custom partition assignment strategy.

</details>

## Question 8

A consumer uses `assign()` with a `TopicPartition` whose partition does not exist in the cluster. What happens when it calls `poll(Duration)`?

- A. `poll()` throws `UnknownTopicOrPartitionException` immediately and the consumer must be closed
- B. `poll()` returns an empty `ConsumerRecords` (no exception); the consumer only logs metadata warnings and keeps retrying
- C. The consumer creates the partition automatically
- D. The consumer is reassigned to another existing partition

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
`assign()` itself does no validation; the consumer cannot create partitions. `UNKNOWN_TOPIC_OR_PARTITION` is a retriable error: the client refreshes metadata, logs a warning (e.g. "Error while fetching metadata ... UNKNOWN_TOPIC_OR_PARTITION") and `poll()` returns no records until the timeout expires. No exception is thrown to the application (exceptions such as `TopicAuthorizationException` are only for authorization problems). The consumer is not moved to another partition (D). To validate, use `partitionsFor(topic)`.

Source: KafkaConsumer javadoc (https://kafka.apache.org/43/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html, `assign`/`poll`); Kafka protocol error codes (UNKNOWN_TOPIC_OR_PARTITION is retriable).

</details>

## Question 9

Can a consumer dynamically change the partitions it is assigned to without stopping and restarting?

- A. Yes, by calling both `KafkaConsumer.subscribe()` and `KafkaConsumer.assign()` on the same consumer
- B. Yes, by calling `KafkaConsumer.assign()` with a new set of partitions
- C. No, partition assignment can only be changed when the consumer is first started
- D. No, partition assignment is fixed for the entire lifecycle of the consumer

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
A Kafka consumer can dynamically change the partitions it is assigned to without stopping and restarting by calling the `KafkaConsumer.assign()` method with a new set of partitions.

The `assign` method allows a consumer to explicitly specify which partitions it should consume from. By calling `assign` with a different set of partitions, the consumer can dynamically change its assignment.

Here's how it works:

1. The consumer calls `assign` with a new collection of `TopicPartition` objects representing the desired partitions to consume from.
2. Kafka updates the consumer's assignment to the specified partitions.
3. The consumer will stop consuming from its previous assignment and start consuming from the newly assigned partitions.
4. The consumer can continue processing messages from the new partitions without needing to restart.

This dynamic partition assignment is useful in scenarios where you want to implement custom partition load balancing or adjust consumer workload at runtime. Note that manual assignment bypasses consumer group management, so no rebalances happen.

Statement A is incorrect because a consumer cannot mix automatic (`subscribe`) and manual (`assign`) assignment: calling both throws an `IllegalStateException`. (Calling `subscribe()` again with a new set of topics only replaces the subscription; partitions are then assigned automatically by the group protocol.)

Statements C and D are incorrect because partition assignment is not fixed for the entire lifecycle of a consumer. It can be changed dynamically using the `assign` method.

</details>

## Question 10

A consumer is part of a consumer group and is currently processing messages. If the consumer crashes and is restarted, what will happen?

- A. The consumer will resume processing from the last committed offset
- B. The consumer will start processing from the earliest available offset
- C. The consumer will start processing from the latest available offset
- D. The consumer will be assigned a new set of partitions

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
When a consumer in a consumer group crashes and is restarted, it will resume processing from the last committed offset.

In Kafka, each consumer in a consumer group maintains its own offset position for each partition it is assigned to. Periodically, the consumer commits its offsets to Kafka to mark its progress. If a consumer crashes or is shut down, its offsets remain committed in Kafka.

When the consumer is restarted:

1. It will rejoin the consumer group.
2. Kafka will reassign partitions to the consumers in the group, including the restarted consumer.
3. For each assigned partition, the consumer will resume processing from the last committed offset.

This behavior ensures that the consumer does not miss any messages and avoids duplicating message processing.

Statement B is incorrect because the consumer will not start from the earliest available offset unless it is explicitly configured to do so (e.g., by setting `auto.offset.reset=earliest`).

Statement C is incorrect because the consumer will not start from the latest available offset unless it is explicitly configured to do so (e.g., by setting `auto.offset.reset=latest`).

Statement D is incorrect because the consumer will not necessarily be assigned a new set of partitions. Kafka will reassign partitions based on the consumer group's partition assignment strategy, which may or may not result in the same assignments as before.

</details>

## Question 11

What happens when a new consumer joins an existing consumer group?

- A. The new consumer will start consuming from the earliest available offset for all partitions
- B. The new consumer will start consuming from the latest available offset for all partitions
- C. The new consumer will be assigned a subset of partitions and start consuming from the last committed offset for each partition
- D. The new consumer will wait until the next rebalance before starting to consume

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When a new consumer joins an existing consumer group, Kafka will trigger a rebalance of partitions among the consumers in the group, including the new consumer.

During the rebalance:

1. Kafka will assign a subset of the partitions to the new consumer based on the consumer group's partition assignment strategy.
2. For each assigned partition, the new consumer will start consuming from the last committed offset.

This behavior ensures that the new consumer starts processing at the correct position and does not duplicate or miss any messages.

Statement A is incorrect because the new consumer will not start from the earliest available offset unless it is explicitly configured to do so (e.g., by setting `auto.offset.reset=earliest`).

Statement B is incorrect because the new consumer will not start from the latest available offset unless it is explicitly configured to do so (e.g., by setting `auto.offset.reset=latest`).

Statement D is incorrect because the new consumer will not wait until the next rebalance. The joining of a new consumer itself triggers a rebalance, and the consumer starts consuming immediately after the rebalance completes.

</details>

## Question 12

What is the purpose of the `group.id` property in a Kafka consumer configuration?

- A. To specify the ID of the consumer within a consumer group
- B. To specify the ID of the consumer group the consumer belongs to
- C. To specify the ID of the Kafka cluster the consumer connects to
- D. To specify the ID of the partitions the consumer should read from

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The `group.id` property in a Kafka consumer configuration is used to specify the ID of the consumer group the consumer belongs to.

In Kafka, consumers can be organized into consumer groups for scalability and fault tolerance. Consumers within the same group coordinate with each other to distribute the partitions of a topic among themselves. Each consumer in a group is assigned a subset of the partitions to consume from.

The `group.id` serves as a unique identifier for a consumer group. All consumers with the same `group.id` are considered part of the same group and will work together to consume from the topic partitions.

Some key points about `group.id`:

- It is a required property for consumers that participate in a consumer group.
- Consumers with the same `group.id` belong to the same group and will coordinate partition assignments.
- Consumers with different `group.id`s are in separate groups and will each receive all messages from the topic independently.

Statement A is incorrect because the `group.id` identifies the group, not the individual consumer within the group. Kafka assigns each consumer a unique member ID within the group.

Statements C and D are incorrect because the `group.id` is not related to the Kafka cluster or the specific partitions to read from. It is solely used for consumer group coordination.

</details>

## Question 13

What is the default behavior of the auto.offset.reset configuration in Kafka consumers?

- A. It starts consuming from the earliest offset if no committed offset is found
- B. It starts consuming from the latest offset if no committed offset is found
- C. It throws an exception if no committed offset is found
- D. It waits for a committed offset to be available before starting consumption

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In Kafka consumers, the auto.offset.reset configuration determines the behavior when no committed offset is found for a partition. The default value is "latest": if no committed offset exists (e.g. a new consumer group) or the committed offset is out of range, the consumer starts from the end of the partition and only sees messages produced after it starts. Messages produced before that are skipped.

You can explicitly set the auto.offset.reset configuration to one of the following values:

- "earliest": The consumer will start consuming from the earliest available offset in the partition if no committed offset is found. This ensures that the consumer processes all messages from the beginning of the partition.
- "latest" (default): The consumer will start consuming from the latest offset in the partition if no committed offset is found. This means that the consumer will only process new messages that arrive after it starts consuming.
- "none": The consumer throws an exception (`NoOffsetForPartitionException`) if no committed offset is found for the group. This is option C, but it is not the default.

It's important to carefully consider the appropriate value for auto.offset.reset based on your application's requirements. Setting it to "earliest" may result in reprocessing messages, while setting it to "latest" may skip messages that were produced before the consumer started.

If you want more control over the starting offset, you can use the Kafka consumer's seek() method to manually set the offset before starting consumption.

</details>

## Question 14

What happens when a Kafka consumer with enable.auto.commit set to false calls the commitSync() method?

- A. The consumer commits the offsets of the messages it has processed so far
- B. The consumer commits the offsets of the messages it has fetched but not yet processed
- C. The consumer does not commit any offsets and throws an exception
- D. The consumer waits for the next batch of messages to be processed before committing offsets

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
When a Kafka consumer has enable.auto.commit set to false, it means that the consumer is responsible for manually committing the offsets of the messages it has processed. In this case, when the consumer calls the commitSync() method, it explicitly commits the latest offsets returned by the last `poll()` (i.e. the records the application has received and, by convention, finished processing before committing).

Here's what happens when commitSync() is called:

1. The consumer sends a commit request to the Kafka broker, specifying the offsets it wants to commit for each partition it is consuming from.
2. The Kafka broker receives the commit request and updates the committed offsets for the consumer group in its metadata.
3. The broker sends a response back to the consumer indicating whether the commit was successful or not.
4. If the commit is successful, the consumer considers the processed messages as committed and will not receive them again even if it restarts.
5. If the commit fails, the consumer may retry the commit or handle the failure based on its error handling strategy.

It's important to note that commitSync() is a blocking call, meaning that the consumer will wait for the Kafka broker to respond before proceeding with further message processing. This can impact the throughput of the consumer, especially if commits are performed frequently.

An alternative to commitSync() is commitAsync(), which sends the commit request asynchronously and allows the consumer to continue processing messages without waiting for the commit response. However, with commitAsync(), the consumer needs to handle the commit callback to check for any commit failures.

</details>

## Question 15

What is the purpose of the isolation.level configuration in Kafka consumers?

- A. To control the visibility of transactional messages
- B. To specify the maximum number of messages to be read in a single batch
- C. To determine the behavior when a partition is reassigned to another consumer in the group
- D. To set the level of consistency for reading messages from a partition

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The isolation.level configuration in Kafka consumers is used to control the visibility of transactional messages. It determines how the consumer behaves when reading messages that are part of a transaction.

Kafka supports transactional message production and consumption, which allows producers to send messages as part of a transaction and ensures that either all messages in a transaction are successfully written to the partition or none of them are. Consumers, on the other hand, can control the visibility of these transactional messages using the isolation.level configuration.

The isolation.level configuration can be set to one of the following values:

1. "read_uncommitted" (default): With this isolation level, the consumer will read all messages in a partition, including transactional messages that are not yet committed. This means that the consumer may see messages that are part of an ongoing transaction or messages that were part of a transaction that was later aborted.

2. "read_committed": With this isolation level, the consumer will only read messages that are not part of an ongoing transaction and messages that are part of a committed transaction. It will wait until a transaction is committed before making its messages visible to the consumer. This ensures that the consumer only sees messages that are part of successful transactions.

The choice of isolation level depends on the requirements of your application. If your application needs to process messages as soon as they are available and can handle potentially uncommitted or aborted messages, you can use the default "read_uncommitted" isolation level. However, if your application requires strict consistency and needs to see only committed messages, you should set the isolation level to "read_committed".

It's important to note that using "read_committed" isolation level may introduce some latency in message consumption, as the consumer needs to wait for transactions to be committed before processing their messages.

</details>

## Question 16

What happens if you try to call `poll()` on a KafkaConsumer from multiple threads simultaneously?

- A. The consumer will automatically coordinate the threads to process messages in parallel
- B. The consumer will throw a ConcurrentModificationException
- C. The behavior is undefined and may lead to unexpected results or errors
- D. The consumer will process messages sequentially, with each thread taking turns

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In Kafka, the KafkaConsumer is not thread-safe, which means that it should not be accessed concurrently by multiple threads. The consumer detects multi-threaded access and throws a `ConcurrentModificationException` ("KafkaConsumer is not safe for multi-threaded access"). Without this check the consumer's internal state (offset positions, assignments) could become corrupted or inconsistent. The only method safe to call from another thread is `wakeup()`.

The Kafka documentation states that the KafkaConsumer is not thread-safe and should only be used from a single thread. If you need to process messages concurrently, you should create multiple consumer instances, each running in its own thread, and partition the work among them.

Here are a few reasons why calling `poll()` from multiple threads simultaneously can be problematic:

1. The consumer maintains internal state, such as offset positions and partition assignments, which can become inconsistent if accessed concurrently.
2. The consumer may rebalance partitions or update its internal state based on the messages processed, and concurrent access can interfere with these operations.
3. Hence a single consumer instance must be used by one thread at a time.

Therefore, it is important to ensure that a KafkaConsumer instance is only accessed by a single thread at a time. If you need to process messages concurrently, you should create multiple consumer instances and coordinate the work among them.

</details>

## Question 17

Per the KafkaConsumer thread-safety rule, what is the recommended way to consume concurrently within one application?

- A. Create a single KafkaConsumer instance and share it among multiple threads
- B. Create multiple KafkaConsumer instances (same group), each running in its own thread
- C. Share one KafkaConsumer among a thread pool, with every worker thread calling `poll()`
- D. Use a lock or synchronization mechanism to coordinate access to a shared KafkaConsumer instance

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
KafkaConsumer is not thread-safe: "One consumer per thread is the rule." Run each consumer in its own thread (e.g. via an `ExecutorService`, each task owning its own consumer). Options A, C and D all share one consumer between threads, which is unsupported (D is discouraged by the javadoc; concurrent access raises `ConcurrentModificationException`). Note: the javadoc also describes handing records from a single polling thread to a worker pool as an alternative (decoupling consumption and processing), but that is not what C says and it complicates offset management; the primary recommendation is one consumer per thread. Each partition goes to only one consumer in the group, so use at most as many consumers as partitions.

Source: Kafka: The Definitive Guide, 2nd ed., Ch. 4 "Thread Safety"; KafkaConsumer javadoc "Multi-threaded Processing".

</details>

## Question 18

How does Kafka ensure that messages are processed in a balanced way when using multiple consumer instances in a consumer group?

- A. Kafka assigns an equal number of messages to each consumer instance
- B. Kafka assigns each partition to exactly one consumer in the group using the configured partition assignment strategy (e.g. range, round-robin, sticky)
- C. Kafka dynamically adjusts the assignment of partitions based on consumer load
- D. Kafka relies on ZooKeeper to distribute messages evenly among consumer instances

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
When using multiple consumer instances in a consumer group, Kafka ensures that messages are processed in a balanced way by assigning partitions to consumer instances using the configured partition assignment strategy (`partition.assignment.strategy`, e.g. range, round-robin, sticky). This means that each partition is assigned to only one consumer instance within the group at a time, and the assignment is done in a way that distributes the partitions evenly among the available consumer instances.

Here's how Kafka achieves balanced message processing:

1. When a consumer group is created or a new consumer instance joins the group, Kafka initiates a rebalance operation.
2. During the rebalance, Kafka assigns the partitions of the subscribed topics to the consumer instances in the group.
3. The assignment is done by the group leader using the configured assignor (the default is `[RangeAssignor, CooperativeStickyAssignor]`), where each consumer instance is assigned a subset of the partitions.
4. If there are more partitions than consumer instances, some consumer instances may be assigned multiple partitions.
5. If there are more consumer instances than partitions, some consumer instances may not be assigned any partitions and will remain idle.
6. As messages are produced to the partitions, each consumer instance processes the messages from its assigned partitions independently.
7. If a consumer instance fails or leaves the group, Kafka triggers a rebalance to redistribute the partitions among the remaining consumer instances.

By assigning each partition to exactly one consumer instance, Kafka ensures that the workload is evenly distributed among the consumer instances. Each consumer instance is responsible for processing messages from its assigned partitions, allowing for parallel processing and improved throughput.

It's important to note that the actual partition assignment strategy can be customized by implementing a custom `PartitionAssignor` if needed. Kafka does not rebalance based on consumer load (option C), does not assign a number of messages (option A), and consumer groups do not rely on ZooKeeper (option D).

</details>

## Question 19

🚫 What is the primary benefit of Kafka's zero-copy optimization when sending data from brokers to consumers?

- A. It reduces the memory overhead by avoiding data duplication in memory.
- B. It minimizes the latency by eliminating the need for data serialization and deserialization.
- C. It improves the security by encrypting the data during transmission.
- D. It increases the parallelism by leveraging multiple CPU cores for data transfer.

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
Kafka's zero-copy optimization is a key feature that improves performance by avoiding unnecessary data duplication in memory when sending data from brokers to consumers. Zero-copy allows Kafka to transfer data directly from the file system cache to the network socket (via `sendfile`) without copying it into the application's memory space.

Here's how zero-copy optimization benefits Kafka:

1. Reduced memory overhead:
   - In a traditional data transfer process, data is typically copied from the file system to the application's memory buffer, and then from the application's memory buffer to the network buffer.
   - With zero-copy, Kafka eliminates the need for this intermediate data copy in the application's memory space.
   - By avoiding data duplication in memory, Kafka reduces the memory overhead and improves memory utilization.

2. Improved performance:
   - Copying data between memory buffers adds latency and consumes CPU cycles.
   - By leveraging zero-copy, Kafka minimizes the time spent on data copying operations.
   - This results in faster data transfer and improved overall performance of the Kafka cluster.

3. Efficient resource utilization:
   - Zero-copy allows Kafka to make efficient use of system resources, such as memory and CPU.
   - By avoiding unnecessary data copying, Kafka can handle higher throughput and support more clients with the same hardware resources.

While zero-copy does provide some latency benefits by reducing the time spent on data copying, it does not eliminate the need for data serialization and deserialization (option B). Serialization and deserialization are still required to convert data between the application's format and the network format.

Zero-copy applies to the broker-to-consumer fetch path and is not available when TLS encryption is enabled (the data must pass through user space). It is not primarily focused on security (option C) or parallelism (option D). Its main goal is to optimize data transfer efficiency and reduce memory overhead.

</details>

## Question 20

What is the purpose of the `isolation.level` setting in the Kafka consumer configuration?

- A. To specify the maximum number of records to fetch in a single request
- B. To control the visibility of transactional messages
- C. To determine the behavior of the consumer when it encounters an invalid offset
- D. To set the maximum amount of time the consumer will wait for new messages

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The `isolation.level` setting in the Kafka consumer configuration is used to control the visibility of transactional messages. It determines how the consumer behaves when reading messages that are part of a transaction. There are two possible values for `isolation.level`:

1. `read_uncommitted` (default): With this isolation level, the consumer will read all messages, including transactional messages that are not yet committed. It may read messages from aborted transactions.

2. `read_committed`: With this isolation level, the consumer will only read messages that are not part of ongoing transactions and messages that are part of committed transactions. It will wait for transactions to be committed before making the messages visible to the consumer.

The `isolation.level` setting allows you to control the consistency and visibility of transactional messages consumed by the consumer.



</details>

## Question 21

What is the default value of the `isolation.level` setting in the Kafka consumer configuration?

- A. `read_uncommitted`
- B. `read_committed`
- C. `transactional`
- D. `none`

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The default value of the `isolation.level` setting in the Kafka consumer configuration is `read_uncommitted`. This means that by default, the consumer will read all messages, including transactional messages that are not yet committed. It may consume messages from transactions that are later aborted. If you want the consumer to only read committed messages and wait for transactions to be committed before making the messages visible, you need to explicitly set the `isolation.level` to `read_committed`. The `transactional` and `none` options are not valid values for the `isolation.level` setting.


</details>

## Question 22

What happens when a consumer with `isolation.level=read_committed` encounters a message that is part of an ongoing transaction?

- A. The consumer will read the message immediately
- B. The consumer will wait until the transaction is committed before reading the message
- C. The consumer will skip the message and move on to the next one
- D. The consumer will throw an exception and stop consuming

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
When a consumer with `isolation.level=read_committed` encounters a message that is part of an ongoing transaction, the consumer will wait until the transaction is committed before reading the message. The `read_committed` isolation level ensures that the consumer only reads messages that are not part of ongoing transactions and messages that are part of committed transactions. If a message belongs to a transaction that is still in progress, the consumer will wait until the transaction is committed before making the message visible to the consumer. This behavior guarantees that the consumer only sees messages that are part of successful transactions and prevents the consumer from consuming messages that may later be rolled back if the transaction is aborted.


</details>

## Question 23

What is the purpose of the `max.poll.records` setting in the Kafka consumer configuration?

- A. To specify the maximum number of records to return in a single poll
- B. To control the maximum amount of data the consumer can receive per second
- C. To set the maximum number of partitions the consumer can subscribe to
- D. To determine the maximum number of consumers allowed in a consumer group

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `max.poll.records` setting in the Kafka consumer configuration is used to specify the maximum number of records to return in a single poll. When the consumer calls the `poll()` method to fetch records from Kafka, it will retrieve at most `max.poll.records` records. This setting allows you to control the maximum number of records that the consumer will process in each iteration. By default, `max.poll.records` is set to 500. Adjusting this value can help balance the trade-off between latency and throughput. Setting a higher value can increase throughput by allowing the consumer to process more records in each poll, but it may also increase latency if the processing of each batch takes longer.

</details>

## Question 24

How does the `max.poll.interval.ms` setting affect the behavior of a Kafka consumer?

- A. It specifies the maximum amount of time the consumer can wait before polling for new records
- B. It sets the maximum interval between two consecutive polls before the consumer is considered dead
- C. It determines the maximum time allowed for message processing before committing offsets
- D. It controls the maximum number of records the consumer can poll in a single request

<details>
<summary>Response:</summary> 

**Answer:** B


**Explanation:**
The `max.poll.interval.ms` setting in the Kafka consumer configuration specifies the maximum interval between two consecutive polls before the consumer is considered dead. If the consumer does not call the `poll()` method within this interval, the consumer will be marked as failed and removed from the consumer group. This setting is used to detect and handle consumer failures. By default, `max.poll.interval.ms` is set to 5 minutes (300000 milliseconds). If a consumer takes longer than this interval to process a batch of records, it needs to call `poll()` again within the specified interval to avoid being considered dead. Setting an appropriate value for `max.poll.interval.ms` ensures that consumers are actively participating in the consumer group and helps detect and recover from consumer failures.

</details>

## Question 25

What happens when a Kafka consumer is marked as dead due to exceeding the `max.poll.interval.ms` interval?

- A. The consumer is automatically rebalanced, and its partitions are reassigned to other consumers in the group
- B. The consumer receives an exception and must manually rejoin the consumer group
- C. The consumer's offset commits are rolled back, and it starts consuming from the beginning of the assigned partitions
- D. The consumer is permanently removed from the consumer group and cannot rejoin

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
When a Kafka consumer is marked as dead due to exceeding the `max.poll.interval.ms` interval, the consumer is automatically rebalanced, and its partitions are reassigned to other consumers in the consumer group. The Kafka consumer group coordinator detects that the consumer has failed to poll within the specified interval and triggers a rebalance operation. During the rebalance, the partitions assigned to the dead consumer are revoked and redistributed among the remaining active consumers in the group. This ensures that the workload is evenly distributed and that the consumer group continues to make progress. The dead consumer is removed from the group, and it automatically rejoins the group on its next `poll()` call and receives new partition assignments (offset commits made after being kicked out fail with `CommitFailedException`).

</details>

## Question 26

What triggers a partition rebalance in a Kafka consumer group?

- A. Adding a new topic to the Kafka cluster
- B. Changing the replication factor of a topic
- C. Adding a new consumer to the consumer group
- D. Modifying the consumer group ID

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
A partition rebalance in a Kafka consumer group is triggered when there is a change in the group membership. Specifically, adding a new consumer to the consumer group will trigger a rebalance. During a rebalance, Kafka reassigns the partitions to the consumers in the group to ensure an even distribution of work. This allows the new consumer to start consuming messages from the assigned partitions. Other events, such as removing a consumer from the group or a consumer voluntarily leaving the group, will also trigger a rebalance. However, adding a new topic to the cluster, changing the replication factor of a topic, or modifying the consumer group ID do not directly trigger a rebalance.

</details>

## Question 27

What happens to the partition assignments during a consumer group rebalance?

- A. Partitions are evenly distributed among the remaining consumers
- B. Partitions are assigned to the consumers based on the consumer group ID
- C. Partitions are randomly assigned to the consumers
- D. Partitions are assigned to the consumers based on the topic name

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
During a consumer group rebalance, Kafka reassigns the partitions to the consumers in the group to ensure an even distribution of work. The partitions are evenly distributed among the remaining active consumers in the group. Kafka uses a partition assignment strategy, such as the range or round-robin strategy, to determine which consumer gets assigned which partitions. The assignment strategy aims to balance the workload and ensure that each consumer receives a fair share of the partitions. The partition assignments are not based on factors like the consumer group ID or the topic name, but rather on the number of active consumers and the available partitions.



</details>

## Question 28

How can you minimize the impact of consumer group rebalances in a Kafka application?

- A. Increase the session timeout value for consumers
- B. Reduce the number of partitions for the consumed topics
- C. Implement a custom partition assignment strategy
- D. Use static group membership for consumers

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
To minimize the impact of consumer group rebalances in a Kafka application, you can use static group membership for consumers. Static group membership allows you to assign a unique identifier to each consumer in the group using the `group.instance.id` configuration. By providing a stable identifier, consumers can maintain their partition assignments across restarts and rebalances. When a consumer with a static group membership rejoins the group after a restart, it will be assigned the same partitions it had before, reducing the need for a full rebalance. This helps in preserving consumer state and avoiding unnecessary partition migrations. Increasing the session timeout value or reducing the number of partitions may help in certain scenarios but does not directly minimize the impact of rebalances. Implementing a custom partition assignment strategy can provide more control over the assignment process but requires additional development effort.



</details>

## Question 29

When a Kafka consumer wants to read data from a specific partition, what information does it need to provide to the Kafka broker?

- A. The topic name and the consumer group ID
- B. The topic name and the offset to start reading from
- C. The topic name, partition number, and offset to start reading from
- D. The topic name, partition number, and consumer group ID

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When a Kafka consumer wants to read data from a specific partition, it needs to provide the following information to the Kafka broker:
- The topic name: The consumer must specify the name of the topic from which it wants to read data.
- The partition number: The consumer must specify the specific partition number within the topic from which it wants to read data.
- The offset to start reading from: The consumer can optionally specify the offset from which it wants to start reading data within the partition. If no offset is provided, the consumer will start reading from the latest offset or the earliest offset, depending on the `auto.offset.reset` configuration.

The consumer group ID is not required when reading from a specific partition, as partition assignment is handled automatically by the Kafka consumer group coordination protocol. The consumer can choose to read from any partition it wants, regardless of its consumer group.



</details>

## Question 30

How does a Kafka consumer determine which broker to connect to when reading data from a specific partition?

- A. The consumer connects to any available broker and requests the leader for the specific partition
- B. The consumer connects to the Zookeeper ensemble to determine the leader for the specific partition
- C. The consumer uses a round-robin algorithm to select a broker to connect to
- D. The consumer connects to all brokers in the cluster simultaneously

<details>
<summary>Response:</summary> 

**Answer:** A


**Explanation:**
When a Kafka consumer wants to read data from a specific partition, it needs to connect to the broker that is currently acting as the leader for that partition. To determine which broker is the leader, the consumer follows these steps:
1. The consumer connects to any available broker in the Kafka cluster.
2. The consumer sends a metadata request to the connected broker, specifying the topic and partition it wants to read from.
3. The broker responds with the metadata information, including the current leader broker for the specific partition.
4. The consumer establishes a connection to the leader broker for the partition.
5. The consumer starts reading data from the leader broker for the specific partition.

Consumers never connect to ZooKeeper (or the KRaft controllers) directly to determine the leader broker. The Kafka brokers themselves maintain the leadership information and can provide it to the consumers upon request. The consumer also does not use a round-robin algorithm or connect to all brokers simultaneously, as it only needs to connect to the leader broker for the specific partition.


</details>

## Question 31

A consumer that uses `assign()` for a partition that does not exist in an existing topic calls `poll()`. Which statement is correct?

- A. The broker automatically creates the partition and starts serving data
- B. `poll()` returns no records (empty result) without throwing; the client retries metadata refresh and logs warnings
- C. `poll()` throws an exception telling that the partition does not exist
- D. The consumer is assigned a different, existing partition to read from

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Same behaviour as Question 8: the unknown partition yields the retriable `UNKNOWN_TOPIC_OR_PARTITION` error inside the client; it is handled internally (metadata refresh + warning log) and `poll()` simply returns empty. Brokers never create partitions on fetch, and the consumer is never silently reassigned. Use `partitionsFor()` to check which partitions exist.

Source: KafkaConsumer javadoc (https://kafka.apache.org/43/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html).

</details>

## Question 32

When a Kafka consumer commits offsets, what information is included in the commit request?

- A. The consumer group ID and the last processed offset for each partition
- B. The consumer group ID and the next offset to be processed for each partition
- C. The consumer ID and the last processed offset for each partition
- D. The consumer ID and the next offset to be processed for each partition

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
When a Kafka consumer commits offsets, it sends a commit request to the Kafka broker. The commit request includes the following information:
- The consumer group ID: The consumer group to which the consumer belongs. Offsets are committed at the consumer group level.
- The next offset to be processed for each partition: The committed offset is the offset of the next message the application will read, i.e. the last processed offset + 1. This offset represents the position from which consumption resumes after a restart or rebalance.

The commit request does not include the consumer ID, as offsets are not committed at the individual consumer level, but rather at the consumer group level. All consumers within the same consumer group collaborate and share the responsibility of consuming and committing offsets.

Options A and C are incorrect because the committed offset is not the last processed offset but the next one (last processed + 1). Committing it acknowledges that all messages before that offset have been processed.



</details>

## Question 33

What happens if a Kafka consumer commits an offset for a partition and then crashes before processing the next message?

- A. The consumer will resume processing from the last committed offset when it restarts
- B. The consumer will resume processing from the next message after the last committed offset when it restarts
- C. The consumer will start processing from the beginning of the partition when it restarts
- D. The consumer will be assigned a different partition to process when it restarts

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
If a Kafka consumer commits an offset for a partition and then crashes before processing the next message, the following will happen when the consumer restarts:

The consumer will resume processing from the last committed offset when it restarts. When the consumer starts up again, it will check the last committed offset for each partition it was consuming from. It will then begin processing messages starting at the committed offset, which already points to the next unprocessed message (last processed offset + 1).

This behavior ensures that the consumer does not miss any messages and avoids duplicate processing. By committing offsets, the consumer acknowledges that it has successfully processed messages up to a certain point. When it restarts, it picks up from where it left off based on the last committed offset.

Option B is incorrect: the committed offset itself is the position of the next message to read, so starting one message after it would skip a message. It also will not start processing from the beginning of the partition, as that would lead to duplicate processing of already consumed messages.

The consumer will not be assigned a different partition to process when it restarts. Partition assignment is handled by the consumer group protocol and remains stable across consumer restarts, unless there are changes in the consumer group membership or partition allocation.



</details>

## Question 34

What is the purpose of the `enable.auto.commit` configuration property in Kafka consumers?

- A. To automatically commit offsets at a fixed interval
- B. To automatically commit offsets after each message is processed
- C. To enable or disable automatic offset commits
- D. To specify the maximum number of offsets to commit in a single request

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
The `enable.auto.commit` configuration property in Kafka consumers is used to enable or disable automatic offset commits. When set to `true` (which is the default value), the consumer will automatically commit offsets at a regular interval specified by the `auto.commit.interval.ms` configuration property.

When automatic offset commits are enabled, the consumer periodically commits the offsets of the messages it has processed without the need for explicit offset management by the application. This helps in ensuring that the consumer's progress is persisted and allows for easier recovery in case of failures.

However, if `enable.auto.commit` is set to `false`, the consumer will not automatically commit offsets, and the application will be responsible for manually committing offsets using the `commitSync()` or `commitAsync()` methods provided by the Kafka consumer API. This gives the application more control over when and how offsets are committed, allowing for custom offset management strategies.

The `enable.auto.commit` configuration property does not control the interval at which offsets are committed (option A) or the number of offsets to commit in a single request (option D). It also does not automatically commit offsets after each message is processed (option B), as that would be inefficient and impact performance.



</details>

## Question 35

In a topic with a replication factor of 3 and `min.insync.replicas` set to 2, what happens when a consumer sends a read request to a partition with only one in-sync replica?

- A. The consumer receives the requested data from the in-sync replica
- B. The consumer request fails with a `NotEnoughReplicasException`
- C. The consumer receives an empty response
- D. The consumer request remains pending until another replica becomes in-sync

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
When a topic has a replication factor of 3 and `min.insync.replicas` is set to 2, it means that producers using `acks=all` need at least 2 in-sync replicas (including the leader) to write successfully. Consumers read only from the leader (up to the high watermark) and are not affected.

In the scenario where a consumer sends a read request to a partition that has only one in-sync replica, the consumer will still receive the requested data from that in-sync replica. The `min.insync.replicas` setting does not directly affect read operations; it primarily impacts write availability.

As long as there is a leader (an in-sync replica) available, consumer read requests can be served successfully. The consumer does not need to wait for additional replicas to become in-sync or for the `min.insync.replicas` requirement to be met.

The consumer request will not fail with a `NotEnoughReplicasException`, receive an empty response, or remain pending. The in-sync replica will provide the requested data to the consumer.

</details>
