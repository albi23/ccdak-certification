> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 1 (Stream Processing):
In ksqlDB, which of the following statements correctly describes how to create a persistent streaming aggregation that maintains a running count of events per key, and what is a critical requirement for the underlying Kafka topic storing this aggregation?

- A. Use a STREAM with a WINDOWED aggregation, the underlying Kafka topic must have infinite retention to avoid losing state data.
- B. Use a TABLE with a GROUP BY and COUNT() aggregation, the underlying Kafka topic must be compacted to retain only the latest state per key.
- C. Use a TABLE with a GROUP BY and SUM() aggregation, the underlying Kafka topic must be configured with delete retention to handle tombstone records.
- D. Use a STREAM with a GROUP BY and COUNT() aggregation, the underlying Kafka topic must be configured as a log-compacted topic to store aggregation state.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In ksqlDB, stateful, persistent aggregations are represented as TABLEs, which maintain the current state per key, such as counts or sums. These TABLEs rely on compacted Kafka topics to store changelog data efficiently, retaining only the latest update per key and enabling fault-tolerant state recovery. STREAMs represent immutable event sequences and do not maintain persistent aggregation state themselves. Windowed aggregations on STREAMs produce new STREAM outputs but do not maintain persistent state tables. Although deletion retention settings can affect topic cleanup, the primary requirement for aggregation state topics is log compaction to ensure optimal storage and state recovery. Understanding these distinctions is essential for designing robust stream processing applications with ksqlDB.

Source: (unverified) - ksqlDB is explicitly out of CCDAK scope (blueprint "Out of Scope"), not verified against ksqlDB docs.

**Detailed explanation of each option:**

1. ❌ **A. Use a STREAM with a WINDOWED aggregation, the underlying Kafka topic must have infinite retention to avoid losing state data.**  
   **Incorrect**. While windowed aggregations are possible on STREAMs, these produce STREAM outputs representing aggregated windows, not persistent state tables. Infinite retention is not a requirement, retention depends on window size and cleanup policies.

2. ✅ **B. Use a TABLE with a GROUP BY and COUNT() aggregation, the underlying Kafka topic must be compacted to retain only the latest state per key.**  
   **Correct**. Persistent aggregations in ksqlDB are represented as TABLEs, which store the latest aggregation results per key. The underlying Kafka changelog topic is typically compacted to ensure only the latest state per key is retained, optimizing storage and recovery.

3. ❌ **C. Use a TABLE with a GROUP BY and SUM() aggregation, the underlying Kafka topic must be configured with delete retention to handle tombstone records.**  
   **Incorrect**. Although TABLEs with SUM() aggregations are valid, the critical requirement for persistent aggregation topics is compaction, not delete retention. Delete retention relates to cleanup of tombstone records but is secondary to topic compaction for state management.

4. ❌ **D. Use a STREAM with a GROUP BY and COUNT() aggregation, the underlying Kafka topic must be configured as a log-compacted topic to store aggregation state.**  
   **Incorrect**. STREAMs represent append-only event sequences and do not maintain stateful aggregations. Aggregations must be stored in TABLEs, not STREAMs. Also, while compacted topics are used for TABLEs, STREAMs usually are not compacted for aggregation state.

</details>

## Question 2 (Kafka Internals): [-]
Which of the following statements accurately describe how Kafka handles request processing within a broker?

- A. Kafka processes all client requests synchronously on a single thread to maintain ordering guarantees.
- B. Request handlers in Kafka brokers use a thread pool to process network requests asynchronously, enabling parallel handling of produce and fetch requests.
- C. The Kafka broker relies on a request queue per partition to ensure that requests affecting the same partition are processed in order.
- D. Kafka uses a selector thread to handle network I/O multiplexing, decoupling it from request processing logic to improve scalability.
- E. Fetch requests from consumers are prioritized over produce requests to reduce consumer lag in Kafka brokers.
- F. Kafka brokers immediately commit the data to disk upon receiving a produce request before sending a response to the producer.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Per the book: for each listener port an acceptor thread hands connections to processor (network) threads, which put requests on ONE shared request queue (and send responses from a response queue), I/O (request handler) threads from a pool pick requests up. There is NO per-partition request queue, so C is false (per-partition order comes from the append-only log on the partition leader and, for producers, from sequence numbers/in-flight limits). Fetch is not prioritized over produce, and produce data need not be fsynced before the response (durability comes from replication). Original text follows.

Kafka brokers handle client requests by leveraging asynchronous processing with a thread pool of request handlers to optimize throughput and reduce latency. Partition-level request queues ensure that produce and fetch requests for the same partition maintain strict ordering guarantees. Selector threads handle network I/O multiplexing, decoupling connection management from processing to improve scalability. Contrary to some misconceptions, Kafka does not process requests synchronously on a single thread, nor does it prioritize fetch over produce requests. Also, data commit behavior depends on configuration and is not always immediate upon receiving a produce request. Understanding these internal request processing mechanisms is critical for developers to optimize Kafka client and broker interactions effectively.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Request Processing" (pp. 142-143, Fig. 6-1)

**Detailed explanation of each option:**

1. ❌ **A. Kafka processes all client requests synchronously on a single thread to maintain ordering guarantees.**  
   **Incorrect**. Kafka uses multiple I/O threads to handle requests concurrently for better throughput, ordering guarantees are managed at the partition level rather than by single-threaded request processing.

2. ✅ **B. Request handlers in Kafka brokers use a thread pool to process network requests asynchronously, enabling parallel handling of produce and fetch requests.**  
   **Correct**. Kafka employs network I/O threads along with request handler threads in a thread pool to process requests asynchronously, improving throughput and low latency.

3. ❌ **C. The Kafka broker relies on a request queue per partition to ensure that requests affecting the same partition are processed in order.**  
   **Incorrect**. Brokers use a single shared request queue, there are no per-partition request queues (book Ch. 6, p. 143).

4. ✅ **D. Kafka uses a selector thread to handle network I/O multiplexing, decoupling it from request processing logic to improve scalability.**  
   **Correct**. Kafka uses selector threads for network I/O multiplexing, which separates connection handling from request processing threads, enhancing scalability and resource utilization.

5. ❌ **E. Fetch requests from consumers are prioritized over produce requests to reduce consumer lag in Kafka brokers.**  
   **Incorrect**. Kafka does not prioritize fetch requests over produce requests, both are processed fairly to maintain overall system balance.

6. ❌ **F. Kafka brokers immediately commit the data to disk upon receiving a produce request before sending a response to the producer.**  
   **Incorrect**. Kafka replicates and appends data to a log segment, but depending on configuration, the response may be sent before data is fully flushed to disk (e.g., when acks=1 or acks=0).

</details>

## Question 3 (Kafka Consumers):
In the context of the Kafka consumer poll loop, which of the following statements accurately describe best practices or behaviors essential for correct and efficient consumer operation in a Confluent Certified Developer for Apache Kafka environment?

- A. Calling poll() less frequently than the configured max.poll.interval.ms can cause the consumer to be considered dead and trigger a rebalance.
- B. Committing offsets should only be done after processing records returned from poll(), either synchronously or asynchronously.
- C. It is acceptable to call poll() once and then process records asynchronously without further poll calls for an extended period.
- D. The poll() method returns immediately with records even if no new data is available, so it is safe to call it in a tight loop without a timeout.
- E. The poll() method must be called frequently enough (within max.poll.interval.ms) to avoid the consumer being removed from the group and triggering a rebalance.
- F. The poll loop should handle rebalances by implementing a ConsumerRebalanceListener to commit offsets and manage partition assignments gracefully.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, B, E, F

**Explanation:**

The Kafka consumer poll loop is central to maintaining consumer liveness and ensuring efficient processing. Calling poll() frequently enough prevents session timeouts and group rebalances by continuously sending heartbeats. Offsets should be committed only after successfully processing records to maintain data integrity. Implementing a ConsumerRebalanceListener is critical for managing partition ownership changes gracefully during rebalances, ensuring no messages are lost or processed twice. Additionally, adhering to the max.poll.interval.ms timeout ensures the consumer is not considered dead due to extended processing delays. Misunderstanding these concepts can lead to frequent rebalances, message duplication, or data loss, which are critical considerations for any developer preparing for the Confluent Certified Developer for Apache Kafka exam.

 answer A, B, E, F confirmed. Option E reworded to refer to max.poll.interval.ms (not session timeouts), which is what poll() frequency governs.

Source: https://kafka.apache.org/42/configuration/consumer-configs/ (max.poll.interval.ms, session.timeout.ms, heartbeat.interval.ms)

**Detailed explanation of each option:**

1. ✅ **A. Calling poll() less frequently than the configured max.poll.interval.ms can cause the consumer to be considered dead and trigger a rebalance.**  
   **Correct**. max.poll.interval.ms defines the max delay between poll calls, exceeding it causes the broker to consider the consumer unresponsive.

2. ✅ **B. Committing offsets should only be done after processing records returned from poll(), either synchronously or asynchronously.**  
   **Correct**. Offsets must be committed after processing to ensure at-least-once delivery semantics and avoid data loss.

3. ❌ **C. It is acceptable to call poll() once and then process records asynchronously without further poll calls for an extended period.**  
   **Incorrect**. Delaying poll() beyond max.poll.interval.ms gets the consumer evicted from the group, triggering a rebalance and potential message duplication.

4. ❌ **D. The poll() method returns immediately with records even if no new data is available, so it is safe to call it in a tight loop without a timeout.**  
   **Incorrect**. poll() blocks up to the specified timeout if no data is available, so the timeout parameter controls wait time and resource usage.

5. ✅ **E. The poll() method must be called frequently enough (within max.poll.interval.ms) to avoid the consumer being removed from the group and triggering a rebalance.**  
   **Correct**. Heartbeats/session.timeout.ms are handled separately, what poll() frequency controls is max.poll.interval.ms: "If poll() is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance".

6. ✅ **F. The poll loop should handle rebalances by implementing a ConsumerRebalanceListener to commit offsets and manage partition assignments gracefully.**  
   **Correct**. Handling rebalances properly prevents message duplication and ensures correct offset management during partition ownership changes.

</details>

## Question 4 (Kafka Ecosystem):
Which Kafka API provides the ability to perform exactly-once stream processing with stateful computations in a fault-tolerant manner?

- A. Consumer API
- B. Producer API
- C. Admin API
- D. Kafka Streams API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The Kafka Streams API is a client library built on top of Kafka's Producer and Consumer APIs, designed for building real-time, fault-tolerant, and stateful stream processing applications. It supports exactly-once semantics, allowing developers to perform accurate computations without data duplication or loss. While the Producer and Consumer APIs provide basic message publishing and consumption, they lack built-in stream processing capabilities. The Admin API is focused on Kafka cluster management rather than data processing. Understanding the distinct roles of each API is critical for developers aiming to build robust Kafka applications with the Confluent Certified Developer certification.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Stream Processing, exactly-once), https://kafka.apache.org/documentation/streams/core-concepts (processing.guarantee=exactly_once_v2)

**Detailed explanation of each option:**

1. ❌ **A. Consumer API**  
   **Incorrect**. The Consumer API is designed for reading records from Kafka topics but does not inherently provide stateful processing or exactly-once guarantees.

2. ❌ **B. Producer API**  
   **Incorrect**. The Producer API is used to publish records to Kafka topics but does not provide stream processing or stateful computation capabilities.

3. ❌ **C. Admin API**  
   **Incorrect**. The Admin API is used for managing Kafka resources such as topics and configurations, and does not handle stream processing.

4. ✅ **D. Kafka Streams API**  
   **Correct**. The Kafka Streams API supports stateful stream processing with fault tolerance and exactly-once semantics, enabling complex transformations and aggregations.

</details>

## Question 5 (Kafka Internals):
In Apache Kafka, during the leader election process for partition leadership, which statement best describes the role of the controller and how leader election is coordinated?

- A. Each broker independently elects partition leaders by exchanging leader epoch information with other brokers without centralized coordination.
- B. The controller node uses ZooKeeper to monitor broker heartbeats and elects a new leader by updating the topic partition metadata directly in ZooKeeper.
- C. The controller is a special broker elected via ZooKeeper which coordinates leader election by assigning partition leaders and updating the controller epoch to ensure consistency across brokers.
- D. Leader election is triggered by the Kafka producer when it detects a broker failure, instructing brokers to elect a new leader for the affected partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Apache Kafka, the controller is a designated broker elected via ZooKeeper (in pre-KRaft architectures) responsible for cluster-wide administrative operations, including partition leader election. The controller maintains a controller epoch to guarantee leadership consistency, preventing split-brain scenarios. When a broker fails or becomes unresponsive, the controller detects this and triggers leader election by selecting new leaders for affected partitions. This centralized coordination ensures all brokers have a consistent view of partition leadership. Misconceptions include the idea that producers or brokers independently elect leaders, which would risk state inconsistencies. Understanding the controller's role and interaction with ZooKeeper is critical for managing Kafka clusters and troubleshooting leader election issues.

NOTE: C describes the ZooKeeper-era design (book 2nd ed.). In Kafka 4.x (KRaft only, ZooKeeper removed) the controller is the active leader of the Raft controller quorum and metadata lives in the __cluster_metadata log - C is still the only acceptable option. Option B's explanation above is muddled: in ZK mode the controller DID write leader/ISR state to ZooKeeper, B is wrong mainly because the "controller uses ZK heartbeats" is replaced in modern versions and C is more precise.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "The Controller" (pp. ~139-141), https://kafka.apache.org/documentation/#kraft

**Detailed explanation of each option:**

1. ❌ **A. Each broker independently elects partition leaders by exchanging leader epoch information with other brokers without centralized coordination.**  
   **Incorrect**. Leader election is centralized through the controller to ensure consistent assignment of partition leaders. Brokers do not independently elect leaders, which would risk inconsistent leadership and data loss.

2. ❌ **B. The controller node uses ZooKeeper to monitor broker heartbeats and elects a new leader by updating the topic partition metadata directly in ZooKeeper.**  
   **Incorrect**. This is partially correct, as the controller interacts with ZooKeeper to monitor broker states and coordinate leader election. However, the controller does not update partition metadata directly in ZooKeeper but writes it to the Kafka internal __cluster_metadata topic (in KRaft mode) or uses ZooKeeper ephemeral nodes in older modes.

3. ✅ **C. The controller is a special broker elected via ZooKeeper which coordinates leader election by assigning partition leaders and updating the controller epoch to ensure consistency across brokers.**  
   **Correct**. The controller broker is elected through ZooKeeper, and it coordinates leader election by assigning partition leaders. It also manages the controller epoch, a monotonically increasing number that ensures all brokers have a consistent view of the current controller, preventing split-brain scenarios.

4. ❌ **D. Leader election is triggered by the Kafka producer when it detects a broker failure, instructing brokers to elect a new leader for the affected partitions.**  
   **Incorrect**. Producers do not trigger leader election. Leader election is managed by the controller broker internally, usually triggered by broker failure detection or session expiration in ZooKeeper.

</details>

## Question 6 (Kafka Producers):
In the context of Kafka Producers, which configuration property primarily controls the acknowledgment behavior and ensures message durability before the producer considers a send successful?

- A. acks
- B. linger.ms
- C. batch.size
- D. compression.type

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The 'acks' configuration is critical in Kafka producer behavior as it defines how many broker acknowledgments are required before a produce request is considered successful. Setting 'acks=all' ensures that the message is committed by all in-sync replicas, maximizing durability and fault tolerance. Other configurations like 'batch.size' and 'linger.ms' optimize performance and throughput but do not influence acknowledgment guarantees. Compression settings affect data size but have no bearing on message durability. Understanding 'acks' is essential for developers aiming to balance performance and reliability in Kafka producer applications, a key concept validated in the Confluent Certified Developer for Apache Kafka exam. (Note: with acks=all, actual durability also depends on topic/broker min.insync.replicas, acks=all is the default since Kafka 3.0.)

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "acks" (pp. ~52-54), https://kafka.apache.org/documentation/#producerconfigs_acks

**Detailed explanation of each option:**

1. ✅ **A. acks**  
   **Correct**. The 'acks' configuration determines the number of acknowledgments the producer requires the leader to receive before considering a request complete. Setting 'acks' to 'all' ensures that all in-sync replicas have acknowledged the record, providing the highest durability.

2. ❌ **B. linger.ms**  
   **Incorrect**. 'linger.ms' sets the delay time to wait for more records before sending a batch, optimizing throughput, but it does not affect acknowledgment semantics or message durability.

3. ❌ **C. batch.size**  
   **Incorrect**. 'batch.size' controls the maximum size of a batch of records sent to a partition, affecting throughput and latency but not acknowledgment behavior or durability guarantees.

4. ❌ **D. compression.type**  
   **Incorrect**. 'compression.type' defines the compression algorithm (e.g., gzip, snappy) used for message payloads to reduce network bandwidth, but it does not impact acknowledgment or durability.

</details>

## Question 7 (Kafka Setup and Operations):
In a Kafka broker configuration, which setting primarily controls the maximum size of a single log segment file before it is rolled over to a new segment?

- A. log.segment.bytes
- B. log.segment.ms
- C. log.retention.hours
- D. log.retention.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The 'log.segment.bytes' configuration parameter in Kafka brokers determines the maximum size in bytes of a single log segment file. When a segment reaches this size, Kafka closes it and starts writing to a new segment file. This is crucial for managing disk I/O performance and log compaction efficiency. Other related settings like 'log.retention.bytes' control total partition log size, and 'log.retention.hours' and 'log.segment.ms' manage retention time and segment rollover based on time, respectively. Understanding these distinctions is vital for tuning Kafka brokers to ensure efficient storage management and predictable log behavior in production environments.

NOTE: there is no broker config named log.segment.ms - the time-based roll setting is log.roll.ms / log.roll.hours (topic-level: segment.ms). log.retention.hours is time-based retention (default 168 h). Option B is therefore a non-existent config, which is still wrong for this question, A remains correct.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 / Ch. 6 "Segment size" (log.segment.bytes, default 1 GB), https://kafka.apache.org/documentation/#brokerconfigs_log.segment.bytes

**Detailed explanation of each option:**

1. ✅ **A. log.segment.bytes**  
   **Correct**. This setting defines the maximum size of a log segment file in bytes. Once this size is reached, the broker rolls over to a new segment.

2. ❌ **B. log.segment.ms**  
   **Incorrect**. log.segment.ms does not exist as a broker config, the time-based roll is log.roll.ms/log.roll.hours (topic segment.ms), and it is time-based, not size-based.

3. ❌ **C. log.retention.hours**  
   **Incorrect**. This setting controls the duration for which log segments are retained before deletion, not their size.

4. ❌ **D. log.retention.bytes**  
   **Incorrect**. This sets the total size of all log segments to retain per partition, not the individual segment size.

</details>

## Question 8 (Reliable Data Delivery):
In the context of ensuring reliable data delivery with Kafka consumers, which configuration or practice is most effective to prevent message loss during consumer failures?

- A. Increase 'max.poll.records' to the highest possible value to process more messages per poll for better throughput
- B. Set 'enable.auto.commit' to true and rely on Kafka's automatic offset commits
- C. Use manual offset commits after processing each message to ensure offsets are only committed upon successful processing
- D. Disable 'auto.offset.reset' to 'earliest' so the consumer always starts from the beginning of the topic on restart

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Reliable data delivery in Kafka consumers hinges on careful offset management. Manual offset commits after successful processing ensure that offsets are only updated once messages are fully handled, preventing data loss during consumer crashes. Automatic offset commits commit offsets at intervals regardless of processing status, which can cause message loss if a consumer fails mid-processing. Increasing 'max.poll.records' can boost throughput but may increase the risk window for failure before committing offsets. The 'auto.offset.reset' setting controls behavior only when no committed offset exists and doesn't safeguard against premature commits. Therefore, manual offset management is critical for guaranteed reliable message processing in Confluent Certified Developer scenarios.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Commits and Offsets" (pp. ~77-84) and Ch. 7 "Consumers" reliability (at-least-once, commit after processing), https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit

**Detailed explanation of each option:**

1. ❌ **A. Increase 'max.poll.records' to the highest possible value to process more messages per poll for better throughput**  
   **Incorrect**. Although increasing 'max.poll.records' improves throughput, it can delay offset commits and increase failure impact, potentially risking message reprocessing or loss.

2. ❌ **B. Set 'enable.auto.commit' to true and rely on Kafka's automatic offset commits**  
   **Incorrect**. While automatic offset commits simplify offset management, they can commit offsets before message processing completes, risking message loss if the consumer crashes.

3. ✅ **C. Use manual offset commits after processing each message to ensure offsets are only committed upon successful processing**  
   **Correct**. Manually committing offsets after processing guarantees that only successfully processed messages are marked as consumed, preventing data loss during failures.

4. ❌ **D. Disable 'auto.offset.reset' to 'earliest' so the consumer always starts from the beginning of the topic on restart**  
   **Incorrect**. Setting 'auto.offset.reset' to 'earliest' only applies when no committed offset exists, it doesn't prevent message loss if offsets are committed prematurely.

</details>

## Question 9 (Kafka Core Concepts): [-]
Which of the following statements about Kafka topics are correct in the context of Confluent Certified Developer for Apache Kafka?

- A. Kafka topics cannot be deleted once created, they persist indefinitely unless the entire cluster is reset.
- B. Kafka topics automatically replicate data across all brokers in the cluster for fault tolerance.
- C. A Kafka topic is a logical channel to which producers publish data and consumers subscribe to consume data.
- D. Each partition within a Kafka topic guarantees message ordering only within that partition.
- E. A topic’s retention period determines how long Kafka retains the messages regardless of whether they have been consumed.
- F. Partitions in a Kafka topic help parallelize data processing and enable scalability of both producers and consumers.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** C, D, E, F

**Explanation:**

Kafka topics are logical streams of data divided into partitions, where ordering is guaranteed only within individual partitions. Producers write data to topics, and consumers read from them, enabling decoupled data pipelines. Replication provides fault tolerance but only to configured replica sets, not necessarily all brokers. Retention policies determine how long messages persist regardless of consumption, facilitating replay and temporal decoupling. Topics can be deleted if broker settings allow, which is important for cluster hygiene. Partitions also facilitate parallelism and scalability by distributing load across multiple brokers and consumers. Understanding these nuances is critical for developing robust Kafka applications and passing the Confluent Certified Developer exam.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 (Topics and Partitions), Ch. 2 (delete.topic.enable defaults to true), Ch. 6 (Replication, Retention), https://kafka.apache.org/documentation/#intro_topics

**Detailed explanation of each option:**

1. ❌ **A. Kafka topics cannot be deleted once created, they persist indefinitely unless the entire cluster is reset.**  
   **Incorrect**. Kafka supports topic deletion if enabled in the broker configuration, topics can be deleted via administrative tools.

2. ❌ **B. Kafka topics automatically replicate data across all brokers in the cluster for fault tolerance.**  
   **Incorrect**. Replication factor is configurable per topic and may not include all brokers, data is replicated to a subset of brokers designated as replicas.

3. ✅ **C. A Kafka topic is a logical channel to which producers publish data and consumers subscribe to consume data.**  
   **Correct**. Topics serve as the fundamental abstraction for data organization in Kafka, enabling decoupling of producers and consumers.

4. ✅ **D. Each partition within a Kafka topic guarantees message ordering only within that partition.**  
   **Correct**. Kafka guarantees order only on a per-partition basis, not across the entire topic.

5. ✅ **E. A topic’s retention period determines how long Kafka retains the messages regardless of whether they have been consumed.**  
   **Correct**. Retention is based on time or size and applies independently of message consumption status.

6. ✅ **F. Partitions in a Kafka topic help parallelize data processing and enable scalability of both producers and consumers.**  
   **Correct**. Partitions enable horizontal scaling by allowing multiple consumers and producers to operate concurrently on different partitions.

</details>

## Question 10 (Kafka Consumers):
In the context of Kafka Consumers, which behavior best describes how consumer groups achieve load balancing and fault tolerance when consuming messages from a topic with multiple partitions?

- A. Consumers within a group share the same offset for all partitions, which guarantees ordered consumption across the entire topic.
- B. A consumer group duplicates messages across consumers to increase throughput and provide message-level fault tolerance.
- C. Partitions are dynamically assigned so that each partition is consumed by exactly one consumer within the group, enabling parallelism and fault tolerance.
- D. Each consumer in the group independently reads all partitions of the topic, ensuring message duplication for fault tolerance.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka consumer groups provide scalability and fault tolerance by dividing topic partitions among consumers, ensuring each partition is consumed by only one consumer at a time. This partition assignment maximizes parallelism and prevents duplicate message processing within the group. Offsets are tracked per partition, preserving message order only within that partition. The misconception that all consumers read all partitions or that offsets are shared among partitions leads to misunderstanding Kafka’s design. Understanding this partition-to-consumer assignment is critical for designing applications that effectively leverage Kafka's consumer group mechanism to achieve load balancing and fault tolerance.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Consumers and Consumer Groups" (pp. ~64-68), https://kafka.apache.org/documentation/#intro_consumers

**Detailed explanation of each option:**

1. ❌ **A. Consumers within a group share the same offset for all partitions, which guarantees ordered consumption across the entire topic.**  
   **Incorrect**. Offsets are tracked per partition, not shared across partitions, so ordered consumption is guaranteed only within a single partition.

2. ❌ **B. A consumer group duplicates messages across consumers to increase throughput and provide message-level fault tolerance.**  
   **Incorrect**. Message duplication within a group is avoided, Kafka’s design ensures each message is processed once per group by exactly one consumer.

3. ✅ **C. Partitions are dynamically assigned so that each partition is consumed by exactly one consumer within the group, enabling parallelism and fault tolerance.**  
   **Correct**. Kafka assigns partitions to consumers in a group such that each partition is consumed by only one consumer, which allows parallel processing and ensures no message duplication within the group.

4. ❌ **D. Each consumer in the group independently reads all partitions of the topic, ensuring message duplication for fault tolerance.**  
   **Incorrect**. Consumers in a group do not all read all partitions, each partition is assigned to only one consumer to avoid duplication.

</details>

## Question 11 (Kafka Connect):
When running Kafka Connect in distributed mode, which configuration property is essential to ensure that multiple workers coordinate properly and share connector and task configurations?

- A. key.converter.schemas.enable
- B. connector.class
- C. bootstrap.servers
- D. offset.flush.interval.ms

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka Connect distributed mode, multiple workers must coordinate to share connector and task configurations. This coordination relies on Kafka topics internally, so specifying 'bootstrap.servers' is essential for workers to connect with the Kafka cluster and join the Connect cluster. Other properties, such as 'key.converter.schemas.enable' or 'offset.flush.interval.ms,' affect message serialization or offset commit behavior but do not influence worker coordination. 'connector.class' is a per-connector setting and not relevant at the worker cluster level. Understanding the role of 'bootstrap.servers' is critical for running Kafka Connect correctly in distributed mode.

NOTE: the property that actually makes workers form one Connect cluster is group.id (same value on all workers, plus config.storage.topic, offset.storage.topic, status.storage.topic). It is not offered here, so C (bootstrap.servers, also required) is the best of the listed options.

Source: https://kafka.apache.org/documentation/#connectconfigs (group.id, config.storage.topic), Kafka: The Definitive Guide 2nd ed. Ch. 9 "Running Connect" (distributed mode)

**Detailed explanation of each option:**

1. ❌ **A. key.converter.schemas.enable**  
   **Incorrect**. : This property controls whether schema information is included when serializing keys and does not affect worker coordination or configuration sharing.

2. ❌ **B. connector.class**  
   **Incorrect**. : This property is specified per connector configuration to identify the connector plugin to run but is not a worker-level setting for coordination.

3. ✅ **C. bootstrap.servers**  
   **Correct**. : This property specifies the Kafka cluster addresses and is required for the Connect workers to communicate with Kafka brokers and coordinate via Kafka topics.

4. ❌ **D. offset.flush.interval.ms**  
   **Incorrect**. : This determines how frequently offsets are committed to Kafka but does not impact worker coordination or connector configuration sharing.

</details>

## Question 12 (Kafka Ecosystem):
In Confluent Schema Registry, which compatibility setting ensures that new schema versions are backward compatible, allowing consumers using the new version of the schema to read data produced with the previous schema?

- A. NONE compatibility
- B. BACKWARD compatibility
- C. FORWARD compatibility
- D. FULL compatibility

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The Confluent Schema Registry supports multiple compatibility modes to manage schema evolution. BACKWARD compatibility ensures consumers using the new schema can read data produced with the previous schema, so consumers are upgraded before producers. FORWARD compatibility is the inverse, ensuring data produced with the new schema can still be read by consumers using the previous schema (producers are upgraded first). FULL compatibility enforces both backward and forward compatibility, providing the strictest guarantees but limiting schema changes. NONE disables compatibility checks, risking runtime serialization errors. Understanding these settings is critical for Confluent Certified Developers to design schemas that evolve safely in production environments and maintain data integrity across distributed Kafka applications.

Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

**Detailed explanation of each option:**

1. ❌ **A. NONE compatibility**  
   **Incorrect**. NONE disables compatibility checks, allowing any schema to be registered regardless of compatibility.

2. ✅ **B. BACKWARD compatibility**  
   **Correct**. BACKWARD compatibility ensures that consumers using the new schema can read data produced with the previous schema version (so consumers are upgraded first, it also allows rewinding consumers to the start of the topic).

3. ❌ **C. FORWARD compatibility**  
   **Incorrect**. FORWARD compatibility ensures that data produced with the new schema can be read by consumers using the previous schema version, which is the opposite direction.

4. ❌ **D. FULL compatibility**  
   **Incorrect**. FULL compatibility requires both backward and forward compatibility, which is stricter than just backward compatibility.

</details>

## Question 13 (Kafka Consumers):
In the context of handling consumer rebalances and errors in Apache Kafka, which of the following strategies best ensures that a Kafka consumer avoids message duplication and data loss during partition reassignments?

- A. Disable offset commits entirely and rely on processing idempotency to handle any duplicate messages caused by rebalances.
- B. Increase the session.timeout.ms to delay the detection of consumer failures, thus reducing the frequency of rebalances and potential errors.
- C. Rely solely on automatic offset commits with a short commit interval to minimize the window of re-processing.
- D. Implement manual offset commits only after message processing is successfully completed and handle rebalances by using a ConsumerRebalanceListener to commit offsets before partitions are revoked.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Handling rebalances carefully is critical to ensuring at-least-once processing guarantees (and minimal duplication) in Kafka consumers. Automatic offset commits risk committing offsets before processing finishes, causing message loss or duplication. The best practice is to disable automatic commits, commit offsets manually only after successful processing, and implement a ConsumerRebalanceListener to commit offsets before partitions are revoked during rebalances. This approach ensures the consumer’s position is saved correctly, avoiding duplicate consumption or data loss. While idempotent processing is important, relying solely on it without proper offset management is insufficient. Adjusting session timeout affects rebalance frequency but does not address offset commit semantics directly. Note: manual commits after processing give at-least-once (not exactly-once) semantics, fully avoiding duplicates also needs idempotent processing or transactions.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Rebalance Listeners" / "Commits and Offsets" (pp. ~77-87), https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit

**Detailed explanation of each option:**

1. ❌ **A. Disable offset commits entirely and rely on processing idempotency to handle any duplicate messages caused by rebalances.**  
   **Incorrect**. While processing idempotency helps, completely disabling offset commits can cause the consumer to reprocess large amounts of data after restarts or rebalances, leading to inefficiency.

2. ❌ **B. Increase the session.timeout.ms to delay the detection of consumer failures, thus reducing the frequency of rebalances and potential errors.**  
   **Incorrect**. Increasing session timeout delays failure detection but does not inherently solve offset commit or duplication issues during rebalances, it may also impact failover responsiveness.

3. ❌ **C. Rely solely on automatic offset commits with a short commit interval to minimize the window of re-processing.**  
   **Incorrect**. Automatic offset commits can lead to message duplication or data loss during rebalances because offsets might be committed before processing is complete or after a rebalance has revoked the partition.

4. ✅ **D. Implement manual offset commits only after message processing is successfully completed and handle rebalances by using a ConsumerRebalanceListener to commit offsets before partitions are revoked.**  
   **Correct**. Manual offset commits after processing give at-least-once semantics (not exactly-once), and using ConsumerRebalanceListener to commit offsets before partition revocation prevents message duplication or loss during rebalances.

</details>

## Question 14 (Kafka Producers):
When constructing a KafkaProducer in Java for a high-throughput, low-latency application, which of the following configurations and practices are recommended to optimize performance and reliability?

- A. Disable batching by setting 'batch.size' to 0 to send records immediately.
- B. Set 'compression.type' to 'none' to minimize CPU overhead during production.
- C. Use 'retries' set to 0 to prevent duplicate messages on failure.
- D. Enable 'enable.idempotence' to true to avoid duplicate record production during retries.
- E. Set 'linger.ms' to a small positive value (e.g., 5-10 ms) to allow batching of records before sending.
- F. Set 'acks' configuration to 'all' to ensure full commit of records across all in-sync replicas.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, E, F

**Explanation:**

For high-throughput, low-latency Kafka producers, configuring 'acks=all' ensures data durability by waiting for acknowledgments from all in-sync replicas. Setting a small 'linger.ms' value enables batching, which improves throughput by reducing the number of requests without significantly increasing latency. Enabling 'enable.idempotence' guarantees exactly-once delivery semantics, preventing duplicates during retries. Disabling batching or retries reduces performance and reliability, while disabling compression increases network usage. Compression typically improves throughput despite CPU cost. Understanding and tuning these configurations are critical for developers aiming to build robust and efficient Kafka producers as required by the Confluent Certified Developer exam. (Since Kafka 3.0 enable.idempotence=true and acks=all are already the defaults, retries defaults to Integer.MAX_VALUE bounded by delivery.timeout.ms, batch.size=0 disables batching.)

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (acks, linger.ms, batch.size, compression.type, idempotent producer), https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ❌ **A. Disable batching by setting 'batch.size' to 0 to send records immediately.**  
   **Incorrect**. Disabling batching reduces throughput and increases network overhead, batching improves throughput by sending multiple records in a single request.

2. ❌ **B. Set 'compression.type' to 'none' to minimize CPU overhead during production.**  
   **Incorrect**. Compression (e.g., 'snappy' or 'lz4') reduces network bandwidth and can improve overall throughput despite some CPU overhead.

3. ❌ **C. Use 'retries' set to 0 to prevent duplicate messages on failure.**  
   **Incorrect**. Setting 'retries' to 0 disables retrying on transient errors, reducing reliability, proper retry configuration with idempotence is preferred.

4. ✅ **D. Enable 'enable.idempotence' to true to avoid duplicate record production during retries.**  
   **Correct**. Idempotence ensures exactly-once delivery semantics for producers, preventing duplicates during retries.

5. ✅ **E. Set 'linger.ms' to a small positive value (e.g., 5-10 ms) to allow batching of records before sending.**  
   **Correct**. 'linger.ms' allows the producer to wait briefly to batch more records, improving throughput without significantly increasing latency.

6. ✅ **F. Set 'acks' configuration to 'all' to ensure full commit of records across all in-sync replicas.**  
   **Correct**. Setting 'acks=all' ensures the producer waits for the full commit to all in-sync replicas, providing highest durability and reliability, which is important for data integrity.

</details>

## Question 15 (Kafka Ecosystem):
In Kafka Connect, which of the following configurations is essential to ensure exactly-once delivery semantics when using a sink connector to write data into an external system?

- A. Setting 'tasks.max' to 1 to avoid parallelism and reduce duplication
- B. Setting the consumer's 'isolation.level' to 'read_committed' (consumer.isolation.level) for the sink connector, together with a sink connector that supports exactly-once writes to the external system
- C. Configuring the connector with 'consumer.auto.offset.reset' set to 'earliest' to reprocess data from the beginning
- D. Using 'offset.flush.interval.ms' set to a very low value to frequently commit offsets

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Exactly-once for Kafka Connect sink connectors depends on the connector supporting it (idempotent/atomic writes, offsets stored with the data) and on the worker's consumer ignoring aborted transactions (consumer.isolation.level=read_committed). Simply adjusting task parallelism, offset commit frequency, or consumer offset reset policies does not guarantee exactly-once semantics, though they impact performance and recovery behavior. Understanding these configurations is critical for developers designing reliable Kafka Connect pipelines that integrate with external systems.

 the original B ("enable transactions via enable.idempotence for the connector") was flawed - Connect has no such sink setting (framework-level exactly-once config exists only for SOURCE connectors). Option B was reworded minimally to what the docs actually say, answer letter B unchanged.

Source: https://kafka.apache.org/42/kafka-connect/user-guide/#exactly-once-support (Exactly-once support / Sink connectors)

**Detailed explanation of each option:**

1. ❌ **A. Setting 'tasks.max' to 1 to avoid parallelism and reduce duplication**  
   **Incorrect**. While limiting tasks can simplify processing, it does not guarantee exactly-once semantics by itself. Exactly-once delivery depends on transactional support and idempotency, not just task count.

2. ✅ **B. Setting the consumer's 'isolation.level' to 'read_committed' (consumer.isolation.level) for the sink connector, together with a sink connector that supports exactly-once writes to the external system**  
   **Correct**. Per the Connect docs: "If a sink connector supports exactly-once semantics, to enable exactly-once at the Connect worker level, you must ensure its consumer group is configured to ignore records in aborted transactions" (consumer.isolation.level=read_committed). The sink connector itself must write idempotently or store offsets together with the data.

3. ❌ **C. Configuring the connector with 'consumer.auto.offset.reset' set to 'earliest' to reprocess data from the beginning**  
   **Incorrect**. This setting controls offset reset behavior on missing offsets but does not influence exactly-once delivery guarantees.

4. ❌ **D. Using 'offset.flush.interval.ms' set to a very low value to frequently commit offsets**  
   **Incorrect**. Although frequent offset commits reduce the window for duplicates on failure, they do not guarantee exactly-once semantics. They mainly help with at-least-once delivery.

</details>

## 🚫 Question 16 (Kafka Setup and Operations):
When setting up a Kafka cluster for production, which of the following configurations or practices are essential to ensure high availability and fault tolerance?

- A. Disable Kafka Controller to eliminate single point of failure
- B. Use unclean leader election to improve availability during broker failures
- C. Set replication factor to at least 3 for critical topics
- D. Enable ZooKeeper ensemble with an odd number of nodes for quorum
- E. Set log segment retention to zero to minimize disk usage
- F. Configure multiple Kafka brokers within the cluster

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, F

**Explanation:**

High availability and fault tolerance in a Kafka cluster depend on deploying multiple brokers and ensuring critical topics have a replication factor of at least three, so data remains available despite broker failures. The Kafka Controller is integral to cluster management and must remain enabled. Unclean leader election risks data loss and should generally be avoided in production. ZooKeeper ensembles require an odd number of nodes to form a reliable quorum, maintaining cluster state consistency. Lastly, setting log retention to zero compromises durability and is not a fault tolerance strategy. Together, these practices create a resilient Kafka cluster suitable for production environments.

NOTE: cluster setup/administration is out of CCDAK scope. D is obsolete: ZooKeeper was removed in Kafka 4.0 (KRaft only), the equivalent is an odd-sized controller quorum (3 or 5). Answer C, D(legacy), F stays valid for ZK-era Kafka, unclean.leader.election.enable defaults to false.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 "Configuring Kafka Clusters" and Ch. 7 "Reliable Data Delivery" (replication factor, unclean leader election), https://kafka.apache.org/documentation/#kraft

**Detailed explanation of each option:**

1. ❌ **A. Disable Kafka Controller to eliminate single point of failure**  
   **Incorrect**. The Kafka Controller is essential for cluster management and electing partition leaders, it cannot be disabled.

2. ❌ **B. Use unclean leader election to improve availability during broker failures**  
   **Incorrect**. Unclean leader election can cause data loss as it allows out-of-sync replicas to become leaders, it is not recommended for production.

3. ✅ **C. Set replication factor to at least 3 for critical topics**  
   **Correct**. A replication factor of 3 ensures that data is replicated to multiple brokers, allowing the cluster to tolerate broker failures without data loss.

4. ✅ **D. Enable ZooKeeper ensemble with an odd number of nodes for quorum**  
   **Correct**. ZooKeeper manages cluster metadata and requires a quorum, typically an odd number of nodes, to maintain availability and consistency.

5. ❌ **E. Set log segment retention to zero to minimize disk usage**  
   **Incorrect**. Setting retention to zero deletes data immediately, which is not suitable for fault tolerance or data durability.

6. ✅ **F. Configure multiple Kafka brokers within the cluster**  
   **Correct**. Multiple brokers distribute partitions and replicas, enabling fault tolerance and load balancing across the cluster.

</details>

## Question 17 (Stream Processing): [-]
In the context of Apache Kafka Streams, when using tumbling time windows for aggregations, which of the following statements is TRUE regarding window boundaries and event-time processing?

- A. In event-time processing, late-arriving events can be assigned to a window if they arrive before the window retention period expires.
- B. The window's start and end timestamps are inclusive, meaning events with timestamps equal to the window's end time are included in that window.
- C. Tumbling windows require a fixed-size hop interval smaller than the window size to function correctly.
- D. Tumbling windows can overlap, allowing an event to belong to multiple windows simultaneously.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Tumbling windows in Kafka Streams define fixed, non-overlapping time intervals where each event belongs to exactly one window. The window start time is inclusive, while the end time is exclusive, so events at the boundary belong to the subsequent window. Event-time processing manages out-of-order and late-arriving events by maintaining a retention period (or grace period), during which late events can still update aggregates for their windows. This feature is essential for accurate stream processing in real-world scenarios where event arrival can be delayed. Misunderstandings often arise around window boundaries and late event handling, knowing these details is critical for implementing correct time-windowed aggregations in Kafka Streams. Precisely: a late record is accepted into its window as long as stream-time has not passed window end + grace period, window store retention must be >= window size + grace. So A is true as an approximation (the grace period, not retention, is the actual cut-off).

Source: https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#windowing , https://kafka.apache.org/documentation/streams/core-concepts#streams_time , Kafka: The Definitive Guide 2nd ed. Ch. 14 (Windowed joins/aggregations)

**Detailed explanation of each option:**

1. ✅ **A. In event-time processing, late-arriving events can be assigned to a window if they arrive before the window retention period expires.**  
   **Correct**. Kafka Streams allows late-arriving events to update windowed aggregates as long as they arrive within the configured grace period (the window store retention must be at least window size + grace), once the grace period expires the record is dropped.

2. ❌ **B. The window's start and end timestamps are inclusive, meaning events with timestamps equal to the window's end time are included in that window.**  
   **Incorrect**. The window's start time is inclusive, but the end time is exclusive, events with timestamps equal to the window's end fall into the next window.

3. ❌ **C. Tumbling windows require a fixed-size hop interval smaller than the window size to function correctly.**  
   **Incorrect**. Fixed-size hop intervals are used in hopping windows, not tumbling windows, which have no overlap and no hops.

4. ❌ **D. Tumbling windows can overlap, allowing an event to belong to multiple windows simultaneously.**  
   **Incorrect**. Tumbling windows are fixed-size, non-overlapping time intervals, so each event belongs to exactly one window.

</details>

## Question 18 (Reliable Data Delivery):
In Apache Kafka, which of the following statements about replication and its impact on reliable data delivery are CORRECT? Select all that apply.

- A. If all replicas become offline except the leader, Kafka continues to accept writes without any impact on durability guarantees.
- B. Kafka’s replication mechanism ensures data is stored on geographically distributed brokers by default to maximize disaster recovery capabilities.
- C. Kafka replicates data across brokers to ensure availability and durability even if some brokers fail.
- D. Replication lag occurs when follower replicas fall behind the leader, which can affect the visibility of committed records to consumers.
- E. The min.insync.replicas configuration dictates the minimum number of replicas that must acknowledge a write for it to be considered successful when acks=all is set.
- F. The leader broker for a partition synchronously replicates data to all followers before acknowledging a producer's write request.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, E

**Explanation:**

Kafka replication is fundamental to reliable data delivery, providing fault tolerance by maintaining multiple copies of partition data across brokers. The leader asynchronously replicates to followers, but with acks=all and min.insync.replicas configured, Kafka ensures a specified number of replicas have the data before acknowledging writes, preventing data loss. Writes are rejected if the number of in-sync replicas falls below the configured threshold, preserving durability guarantees. Replication lag is an important factor affecting failover speed and data visibility to consumers. However, Kafka’s replication is cluster-local and doesn’t automatically provide geographic disaster recovery without additional tools. Understanding these nuances is critical for Confluent Certified Developers to design robust, reliable Kafka systems. (Correction: followers PULL data via fetch requests, with acks=all the leader waits for all in-sync replicas, not all followers, and only records replicated to all ISR are "committed" and visible to consumers.)

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (high watermark, committed records) and Ch. 7 "Reliable Data Delivery" (pp. ~193-200), https://kafka.apache.org/documentation/#design_replicatedlog

**Detailed explanation of each option:**

1. ❌ **A. If all replicas become offline except the leader, Kafka continues to accept writes without any impact on durability guarantees.**  
   **Incorrect**. If the number of in-sync replicas falls below min.insync.replicas when acks=all is used, the leader will reject writes to prevent data loss.

2. ❌ **B. Kafka’s replication mechanism ensures data is stored on geographically distributed brokers by default to maximize disaster recovery capabilities.**  
   **Incorrect**. Kafka replication is per cluster and does not inherently replicate data across geographically distributed clusters, cross-region replication requires additional setup like MirrorMaker.

3. ✅ **C. Kafka replicates data across brokers to ensure availability and durability even if some brokers fail.**  
   **Correct**. Kafka uses replication to store multiple copies of partitions on different brokers, which provides fault tolerance and durability.

4. ✅ **D. Replication lag occurs when follower replicas fall behind the leader, which can affect the visibility of committed records to consumers.**  
   **Correct**. Followers may lag due to network or resource constraints, which can delay failover and impact consumers relying on committed data.

5. ✅ **E. The min.insync.replicas configuration dictates the minimum number of replicas that must acknowledge a write for it to be considered successful when acks=all is set.**  
   **Correct**. This setting ensures that the data is replicated to a minimum number of brokers before the write is acknowledged, increasing data reliability.

6. ❌ **F. The leader broker for a partition synchronously replicates data to all followers before acknowledging a producer's write request.**  
   **Incorrect**. The leader does not wait for ALL followers: with acks=all it waits for the in-sync replicas (at least min.insync.replicas), with acks=1 it acknowledges after the local write. Out-of-sync followers never block writes.

</details>

## Question 19 (Stream Processing):
In the Kafka Streams architecture, which component is primarily responsible for maintaining the local state store and handling fault tolerance through changelog topics?

- A. The Stream Task, which processes partitions of input topics, manages local state stores, and commits changelog updates for fault tolerance.
- B. The Kafka Consumer, which consumes from input topics and also manages local state and fault tolerance internally.
- C. The Kafka Producer, which writes processed records to output topics and manages local state logging.
- D. The Stream Thread, which coordinates between Stream Tasks but does not maintain local state or manage changelog commits directly.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams architecture is designed around Stream Tasks, which are the core processing units assigned to specific partitions of input topics. Each Stream Task maintains a local state store to enable stateful processing and writes changes to a changelog topic for fault tolerance, allowing state recovery upon failure. While Kafka Producers and Consumers handle data ingress and egress, they do not manage state stores or fault tolerance. Stream Threads execute Stream Tasks but act as coordinators rather than state managers. Understanding this division of responsibilities is critical for the Confluent Certified Developer, as it impacts application design, scaling, and fault tolerance strategies.

Source: https://kafka.apache.org/documentation/streams/architecture (stream tasks, threading, local state stores and changelog topics), Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" / "Scaling the Topology"

**Detailed explanation of each option:**

1. ✅ **A. The Stream Task, which processes partitions of input topics, manages local state stores, and commits changelog updates for fault tolerance.**  
   **Correct**. In Kafka Streams, each Stream Task processes a subset of topic partitions, maintains local state stores, and commits updates to changelog topics to ensure fault tolerance and state recovery.

2. ❌ **B. The Kafka Consumer, which consumes from input topics and also manages local state and fault tolerance internally.**  
   **Incorrect**. While Kafka Consumer reads data from topics, it does not manage local state stores or fault tolerance, these responsibilities are handled at the Stream Task level.

3. ❌ **C. The Kafka Producer, which writes processed records to output topics and manages local state logging.**  
   **Incorrect**. The Kafka Producer is responsible for sending records to Kafka topics but does not manage local state stores or handle fault tolerance mechanisms like changelog topics.

4. ❌ **D. The Stream Thread, which coordinates between Stream Tasks but does not maintain local state or manage changelog commits directly.**  
   **Incorrect**. Stream Threads run multiple Stream Tasks and manage their lifecycle but do not directly maintain local state stores or handle changelog commits, those are task-level responsibilities.

</details>

## Question 20 (Kafka Producers):
In the context of Kafka producer reliability and error handling, which configuration or approach most effectively prevents message loss due to transient broker failures while ensuring message ordering within a partition?

- A. Configuring 'acks=all' with 'enable.idempotence=true' and using a single producer instance per partition
- B. Setting 'acks=0' to minimize latency and relying on the producer retries to handle failures
- C. Using 'batch.size' and 'linger.ms' to buffer messages and reduce network calls, thereby improving reliability
- D. Setting 'retries=0' to avoid duplicate records and relying on manual error handling for failed sends

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Ensuring producer reliability in Kafka requires careful configuration of acknowledgments, retries, and idempotence. 'acks=all' guarantees that a message is fully committed to all in-sync replicas before the producer considers it sent, reducing message loss risk. Enabling idempotence prevents duplicate records when retries occur, critical during transient failures. Using a single producer instance per partition preserves message order. Other configurations like 'acks=0' or disabling retries may improve latency but risk data loss or duplicates. Batch and linger settings optimize throughput but do not guarantee reliability or ordering. Thus, the combination of 'acks=all', 'enable.idempotence=true', and proper producer partitioning is the recommended approach for reliable, ordered message delivery in Kafka producers. Note: a "single producer per partition" is not required - an idempotent producer keeps per-partition order even with retries (max.in.flight.requests.per.connection <= 5), also pair acks=all with min.insync.replicas >= 2 for real durability. A is still clearly the best option.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 ("Ordering Guarantees", idempotent producer, pp. ~63-64), https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence

**Detailed explanation of each option:**

1. ✅ **A. Configuring 'acks=all' with 'enable.idempotence=true' and using a single producer instance per partition**  
   **Correct**. 'acks=all' ensures the leader waits for all in-sync replicas to acknowledge the record, and 'enable.idempotence=true' prevents duplicate records on retries. Using a single producer per partition guarantees ordering and prevents message loss during transient failures.

2. ❌ **B. Setting 'acks=0' to minimize latency and relying on the producer retries to handle failures**  
   **Incorrect**. 'acks=0' means the producer does not wait for any acknowledgment from the broker, increasing throughput but risking message loss. This setting does not guarantee delivery or ordering during transient failures.

3. ❌ **C. Using 'batch.size' and 'linger.ms' to buffer messages and reduce network calls, thereby improving reliability**  
   **Incorrect**. 'batch.size' and 'linger.ms' improve throughput and reduce network overhead but do not directly affect reliability or error handling related to message loss or ordering guarantees.

4. ❌ **D. Setting 'retries=0' to avoid duplicate records and relying on manual error handling for failed sends**  
   **Incorrect**. Setting 'retries=0' disables automatic retries, increasing risk of message loss when transient errors occur. Manual error handling is error-prone and generally less reliable than the built-in retry mechanism combined with idempotence.

</details>

## Question 21 (Kafka Setup and Operations):
Which of the following statements accurately describe the role and characteristics of ZooKeeper in a (legacy, ZooKeeper-based) Apache Kafka cluster setup?

- A. ZooKeeper directly manages consumer group offsets in Kafka.
- B. ZooKeeper is responsible for storing Kafka topic configuration and retention policies.
- C. ZooKeeper tracks the status of Kafka brokers to detect failures and trigger leader re-election.
- D. ZooKeeper manages Kafka broker metadata including leader election for partitions.
- E. ZooKeeper stores the actual Kafka messages and serves them to consumers.
- F. ZooKeeper stores the partition data replicas and serves fetch requests from followers.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

ZooKeeper plays a critical role in traditional Kafka deployments by managing cluster metadata such as broker registrations, topic configurations, and leader election for partitions. It monitors broker health and triggers failover procedures. However, it does not store or serve Kafka message data nor manage consumer offsets, which are stored in Kafka topics. Note that KRaft mode (early access in 2.8, production-ready in 3.3) replaces ZooKeeper, and ZooKeeper support was removed entirely in Kafka 4.0, The original option F ("Kafka can operate without ZooKeeper...") was a true statement that did not describe ZooKeeper's role, making the question ambiguous, re-verified and F was reworded to an unambiguously false statement. Answer B, C, D confirmed. The topic is legacy/administration material and outside the CCDAK scope.

Source: https://kafka.apache.org/42/getting-started/zk2kraft/ , https://kafka.apache.org/42/operations/kraft/ , book ch. 6 pp. 135-137

**Detailed explanation of each option:**

1. ❌ **A. ZooKeeper directly manages consumer group offsets in Kafka.**  
   **Incorrect**. Consumer offsets are stored in Kafka’s internal __consumer_offsets topic, not ZooKeeper.

2. ✅ **B. ZooKeeper is responsible for storing Kafka topic configuration and retention policies.**  
   **Correct**. ZooKeeper stores topic configurations, ACLs, and retention policies in older Kafka versions prior to KRaft.

3. ✅ **C. ZooKeeper tracks the status of Kafka brokers to detect failures and trigger leader re-election.**  
   **Correct**. ZooKeeper monitors broker health and coordinates failover by triggering leader re-election when a broker fails.

4. ✅ **D. ZooKeeper manages Kafka broker metadata including leader election for partitions.**  
   **Correct**. ZooKeeper is responsible for managing metadata such as broker registrations and performing leader election for Kafka partitions.

5. ❌ **E. ZooKeeper stores the actual Kafka messages and serves them to consumers.**  
   **Incorrect**. Kafka brokers store and serve messages, ZooKeeper does not store message data.

6. ❌ **F. ZooKeeper stores the partition data replicas and serves fetch requests from followers.**  
   **Incorrect**. Replicas are stored and served by brokers, ZooKeeper holds only metadata.

</details>

## Question 22 (Kafka Connect):
In Kafka Connect, which of the following statements accurately describe the behavior and configuration of distributed mode compared to standalone mode?

- A. Connector plugins must be manually installed on each worker node in distributed mode to ensure consistent execution.
- B. In distributed mode, connector and task configurations are stored in Kafka topics to provide centralized configuration management.
- C. Kafka Connect’s distributed mode requires manual intervention to rebalance tasks when a worker node fails.
- D. Standalone mode supports automatic failover of connectors between worker nodes without data loss.
- E. Distributed mode allows connectors to be automatically balanced and fault-tolerant across multiple worker nodes.
- F. Standalone mode is recommended for production environments requiring high availability and scalability.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

Kafka Connect’s distributed mode enables fault tolerance and scalability by running multiple worker nodes that coordinate via Kafka topics storing connector configurations and statuses. This allows automatic task balancing and recovery without manual intervention. In contrast, standalone mode runs a single process without failover capabilities, making it unsuitable for production environments requiring high availability. Moreover, to ensure connectors function correctly across all workers in distributed mode, connector plugins must be manually deployed on each node. Common misconceptions include expecting standalone mode to support failover or distributed mode to require manual rebalancing. Understanding these distinctions is critical for designing robust Kafka Connect deployments in production.

Source: Kafka: The Definitive Guide 2nd ed., ch. 9 "Running Connect" (standalone vs distributed mode, plugin.path on every worker, config/offset/status topics), https://kafka.apache.org/documentation/#connect_running

**Detailed explanation of each option:**

1. ✅ **A. Connector plugins must be manually installed on each worker node in distributed mode to ensure consistent execution.**  
   **Correct**. Plugins need to be available on every worker to run connectors properly in distributed mode.

2. ✅ **B. In distributed mode, connector and task configurations are stored in Kafka topics to provide centralized configuration management.**  
   **Correct**. Distributed mode uses Kafka topics to store configs and status, enabling coordination and recovery.

3. ❌ **C. Kafka Connect’s distributed mode requires manual intervention to rebalance tasks when a worker node fails.**  
   **Incorrect**. Task rebalancing in distributed mode occurs automatically upon worker failure.

4. ❌ **D. Standalone mode supports automatic failover of connectors between worker nodes without data loss.**  
   **Incorrect**. Standalone mode runs on a single process and does not support failover or scaling.

5. ✅ **E. Distributed mode allows connectors to be automatically balanced and fault-tolerant across multiple worker nodes.**  
   **Correct**. Distributed mode supports scaling and fault tolerance by coordinating multiple worker instances to share connector tasks.

6. ❌ **F. Standalone mode is recommended for production environments requiring high availability and scalability.**  
   **Incorrect**. Standalone mode is typically used for development or testing, not for production with high availability needs.

</details>

## Question 23 (Kafka Ecosystem):
Which of the following statements accurately describe key features and behaviors of Kafka Connect in the context of building scalable and fault-tolerant data pipelines?

- A. Kafka Connect can run in distributed mode, allowing connectors and tasks to be dynamically assigned across a cluster of workers.
- B. Kafka Connect leverages the Kafka consumer group protocol internally to coordinate task distribution in distributed mode.
- C. Kafka Connect supports exactly-once delivery semantics out-of-the-box for all connectors.
- D. Connector configurations must be hardcoded in worker properties files and cannot be updated dynamically at runtime.
- E. Kafka Connect does not support transformation of records during data flow, transformations must be done externally.
- F. Source connectors ingest data into Kafka topics, while sink connectors export data from Kafka topics to external systems.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, F

**Explanation:**

Kafka Connect is designed to simplify integration between Kafka and external systems via source and sink connectors. It supports running in distributed mode, which provides scalability and fault tolerance by coordinating worker nodes through Kafka's own consumer group protocol. This coordination allows dynamic task assignment and rebalancing. Source connectors bring data into Kafka topics, while sink connectors export data out, reflecting the core design paradigm. Connector configurations are managed dynamically through the REST API, not hardcoded in worker properties. Additionally, Kafka Connect supports Single Message Transforms (SMTs) for simple record alterations inline, contrary to the misconception that transformations require external processing. Exactly-once semantics depend on connector and system capabilities and are not guaranteed universally, highlighting the importance of understanding delivery guarantees in pipelines. (Since Kafka 3.3, KIP-618 adds opt-in exactly-once support for source connectors via exactly.once.source.support, but only for connectors that support it - never for all connectors out of the box.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 9 (Connect architecture, converters/SMTs, REST API), https://kafka.apache.org/documentation/#connect_exactlyonce

**Detailed explanation of each option:**

1. ✅ **A. Kafka Connect can run in distributed mode, allowing connectors and tasks to be dynamically assigned across a cluster of workers.**  
   **Correct**. Distributed mode enables scalability and fault tolerance by distributing connector tasks across multiple worker nodes with automatic rebalancing.

2. ✅ **B. Kafka Connect leverages the Kafka consumer group protocol internally to coordinate task distribution in distributed mode.**  
   **Correct**. Kafka Connect uses Kafka’s group coordination protocol to manage worker group membership and partition assignment for connector tasks.

3. ❌ **C. Kafka Connect supports exactly-once delivery semantics out-of-the-box for all connectors.**  
   **Incorrect**. While Kafka Connect supports at-least-once delivery semantics by default, exactly-once semantics depend on the connector implementation and the idempotency of the sink system, it is not guaranteed universally out-of-the-box.

4. ❌ **D. Connector configurations must be hardcoded in worker properties files and cannot be updated dynamically at runtime.**  
   **Incorrect**. Connector configurations are managed independently from worker properties and can be created, updated, or deleted dynamically via the REST API without restarting the workers.

5. ❌ **E. Kafka Connect does not support transformation of records during data flow, transformations must be done externally.**  
   **Incorrect**. Kafka Connect supports Single Message Transforms (SMTs) which allow lightweight, in-flight transformations on records as they move through connectors.

6. ✅ **F. Source connectors ingest data into Kafka topics, while sink connectors export data from Kafka topics to external systems.**  
   **Correct**. This is a fundamental concept in Kafka Connect where source connectors import data to Kafka, and sink connectors export data out of Kafka.

</details>

## 🚫 Question 24 (Kafka Setup and Operations):
Which of the following practices are critical to ensure reliable and efficient production deployments of Kafka clusters in a Confluent Certified Developer environment?

- A. Setting producer acks to 0 to maximize throughput and reduce latency
- B. Enabling SSL encryption and SASL authentication to secure data in transit and control cluster access
- C. Disabling topic-level log compaction to improve write throughput in production
- D. Monitoring consumer lag and configuring appropriate retention policies to balance storage and data availability
- E. Configuring log segment size to a very small value to minimize data loss during broker crashes
- F. Setting appropriate replication factor and min.insync.replicas to guarantee data durability and availability

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

In production Kafka deployments, ensuring data durability and availability requires correctly setting replication factors and min.insync.replicas to handle broker failures without data loss. Monitoring consumer lag and retention policies are essential for balancing storage constraints and data availability, preventing backlog issues. Security is a critical aspect, enabling SSL and SASL protects data in transit and restricts access to authorized users. Conversely, disabling log compaction or setting acks=0 undermines data guarantees and reliability. Similarly, overly small log segment sizes can negatively impact performance. These practices align with Confluent's recommended production best practices for robust and secure Kafka clusters. (Note: this is a generic "production best practices" question about deploying/operating clusters - largely outside the exam scope, the answer B, D, F is consistent with the sources.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 8 "Reliable Data Delivery" (replication, min.insync.replicas, acks), ch. 11 "Securing Kafka", https://kafka.apache.org/documentation/#security

**Detailed explanation of each option:**

1. ❌ **A. Setting producer acks to 0 to maximize throughput and reduce latency**  
   **Incorrect**. Setting acks=0 sacrifices message durability and guarantees, risking data loss in production scenarios.

2. ✅ **B. Enabling SSL encryption and SASL authentication to secure data in transit and control cluster access**  
   **Correct**. Security configurations are vital in production to protect data confidentiality and ensure authorized access.

3. ❌ **C. Disabling topic-level log compaction to improve write throughput in production**  
   **Incorrect**. Disabling log compaction may increase storage usage and is not recommended if compacted topics are needed for state management.

4. ✅ **D. Monitoring consumer lag and configuring appropriate retention policies to balance storage and data availability**  
   **Correct**. Monitoring consumer lag helps detect slow consumers, while retention policies control storage usage without losing critical data.

5. ❌ **E. Configuring log segment size to a very small value to minimize data loss during broker crashes**  
   **Incorrect**. Very small log segments increase overhead and can degrade performance, tuning size balances recovery time and throughput.

6. ✅ **F. Setting appropriate replication factor and min.insync.replicas to guarantee data durability and availability**  
   **Correct**. Proper replication and min.insync.replicas settings ensure fault tolerance and prevent data loss during broker failures.

</details>

## Question 25 (Reliable Data Delivery):
In the context of broker configuration for ensuring reliable data delivery in Apache Kafka, which broker setting primarily controls the minimum number of ISR (in-sync replicas) that must acknowledge a write for the broker to consider a write successful?

- A. log.flush.interval.messages
- B. replica.lag.time.max.ms
- C. unclean.leader.election.enable
- D. min.insync.replicas

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The 'min.insync.replicas' broker configuration is critical for ensuring reliable data delivery because it specifies the minimum number of in-sync replicas that must acknowledge a write for it to be considered successful. This setting works in conjunction with the producer's 'acks' setting to guarantee durability and consistency. If the number of in-sync replicas falls below this threshold, the broker will reject writes to prevent data loss. Other options like 'unclean.leader.election.enable' relate to leader election policies and data loss risk during failover but do not directly control write acknowledgment. 'replica.lag.time.max.ms' affects ISR membership but not write success criteria, and 'log.flush.interval.messages' influences flushing frequency rather than replica acknowledgments. Understanding these distinctions is vital for Confluent Certified Developers to configure Kafka brokers for reliable data delivery effectively. Note that min.insync.replicas exists both as a broker default and as a topic-level override, and it is enforced only for producers using acks=all (with acks=0/1 it has no effect), if fewer replicas are in sync, the broker rejects the write with NotEnoughReplicas.

Source: Kafka: The Definitive Guide 2nd ed., ch. 8 "Reliable Data Delivery" - "Minimum In-Sync Replicas", https://kafka.apache.org/documentation/#brokerconfigs_min.insync.replicas

**Detailed explanation of each option:**

1. ❌ **A. log.flush.interval.messages**  
   **Incorrect**. This controls how often the broker flushes messages to disk based on the number of messages, it influences durability but not the minimum ISR acknowledgment count.

2. ❌ **B. replica.lag.time.max.ms**  
   **Incorrect**. This setting determines the maximum time a replica can lag behind the leader before being considered out of the ISR but does not control acknowledgment thresholds.

3. ❌ **C. unclean.leader.election.enable**  
   **Incorrect**. This setting controls whether a broker can become leader if it is not in the ISR, it impacts data durability during leader failover but does not directly control acknowledgment requirements for writes.

4. ✅ **D. min.insync.replicas**  
   **Correct**. This broker-level configuration defines the minimum number of replicas that must acknowledge a write for the broker to consider it successful, directly affecting the reliability of data delivery.

</details>

## Question 26 (Stream Processing):
Which of the following concepts/patterns are commonly associated with Kafka Streams applications to ensure scalability, fault tolerance, and maintainability in stream processing pipelines?

- A. Processor Topology Pattern
- B. Model View Controller (MVC)
- C. Lambda Architecture
- D. Circuit Breaker
- E. KTable as a Materialized View
- F. Event Sourcing

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, E, F

**Explanation:**

In Kafka Streams development, design patterns like Event Sourcing, Processor Topology, and KTables as materialized views are essential to build scalable and fault-tolerant stream processing applications. Event Sourcing ensures the state can be reconstructed from event logs, which Kafka inherently supports. Processor Topology defines the flow of data through processors and state stores, promoting modular design. KTables provide efficient state management via materialized views, enabling fast access to aggregated or enriched data. Patterns like Lambda Architecture and Circuit Breaker, while useful in broader system design, are not specific to Kafka Streams. MVC is unrelated to stream processing. Understanding these patterns helps developers design robust, maintainable Kafka Streams pipelines.

 the Streams core-concepts page defines "processor topology" (a graph of stream processors) and the stream-table duality (basis of KTable as a materialized view / state stores), it does not mention "event sourcing" explicitly (state rebuilt from the changelog topic is the closest idea). Stem softened to "concepts/patterns commonly associated with", answer A, E, F kept as best of the options (B, C, D are clearly not Streams patterns). Event Sourcing remains weakly verified.

Source: https://kafka.apache.org/42/streams/core-concepts/ (processor topology, stream-table duality)

**Detailed explanation of each option:**

1. ✅ **A. Processor Topology Pattern**  
   **Correct**. Defining a processor topology in Kafka Streams allows developers to build reusable and modular stream processing logic, enhancing maintainability and scalability.

2. ❌ **B. Model View Controller (MVC)**  
   **Incorrect**. MVC is an architectural pattern mainly used in UI development and is not directly applicable to Kafka Streams design.

3. ❌ **C. Lambda Architecture**  
   **Incorrect**. Lambda Architecture involves a batch layer combined with a streaming speed layer, which is a system architecture rather than a Kafka Streams design pattern.

4. ❌ **D. Circuit Breaker**  
   **Incorrect**. Circuit Breaker is typically used to handle fault tolerance in service-to-service communication, but it is not a core design pattern specifically for Kafka Streams processing.

5. ✅ **E. KTable as a Materialized View**  
   **Correct**. Using KTables to maintain materialized views enables efficient stateful processing and fast lookups, which is a key design pattern in Kafka Streams.

6. ✅ **F. Event Sourcing**  
   **Correct**. Event Sourcing is a pattern where state changes are logged as a sequence of events, which Kafka Streams can leverage to rebuild state stores and provide fault tolerance.

</details>

## Question 27 (Kafka Core Concepts):
Which of the following statements about events in Apache Kafka are true and relevant for a Confluent Certified Developer for Apache Kafka?

- A. The event timestamp in Kafka represents the event creation time and can be used for event-time processing.
- B. Each event in Kafka must contain a unique key to ensure ordering within a partition.
- C. Events in Kafka are immutable records that once written cannot be changed or deleted.
- D. Kafka events can be updated in place by producers to correct erroneous data before consumers read them.
- E. Events in Kafka may contain both key and value, where the key is optional but important for partitioning and message semantics.
- F. Kafka enforces strict schema validation on events at the broker level to ensure data compatibility.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, E

**Explanation:**

In Kafka, events are immutable append-only records, ensuring data consistency and enabling replayability. The timestamp associated with an event can represent the time of occurrence, crucial for event-time processing use cases. While keys are optional, they play a vital role in routing events to partitions and enabling features like log compaction. Kafka does not allow in-place updates of events, requiring new messages for corrections. Schema validation is handled outside the broker, commonly via Confluent Schema Registry, making Kafka flexible yet requiring developers to enforce data contracts. Understanding these properties is essential for designing robust, scalable Kafka-based event-driven applications. Precision notes: Kafka events are immutable, but they are not kept forever - they are removed by retention (or compaction), so "cannot be deleted" in C should be read as "cannot be modified", and the timestamp is CreateTime by default (set by the producer) but can be LogAppendTime depending on message.timestamp.type.

Source: Kafka: The Definitive Guide 2nd ed., ch. 1 "Messages and Batches" / ch. 3 (record key, timestamp), https://kafka.apache.org/documentation/#topicconfigs_message.timestamp.type

**Detailed explanation of each option:**

1. ✅ **A. The event timestamp in Kafka represents the event creation time and can be used for event-time processing.**  
   **Correct**. Kafka supports event timestamps that can reflect the creation or ingestion time, enabling event-time semantics.

2. ❌ **B. Each event in Kafka must contain a unique key to ensure ordering within a partition.**  
   **Incorrect**. While keys are used to determine the partition for ordering, uniqueness of the key is not required, multiple events can share the same key.

3. ✅ **C. Events in Kafka are immutable records that once written cannot be changed or deleted.**  
   **Correct**. Kafka events are immutable, this immutability guarantees consistency and allows Kafka to be an append-only log.

4. ❌ **D. Kafka events can be updated in place by producers to correct erroneous data before consumers read them.**  
   **Incorrect**. Due to immutability, events cannot be updated in place, corrections require producing new events.

5. ✅ **E. Events in Kafka may contain both key and value, where the key is optional but important for partitioning and message semantics.**  
   **Correct**. Keys are optional but commonly used to control partition assignment and enable message semantics like compaction.

6. ❌ **F. Kafka enforces strict schema validation on events at the broker level to ensure data compatibility.**  
   **Incorrect**. Schema validation is not enforced by Kafka brokers but typically handled via external schema registries and client-side serialization.

</details>

## Question 28 (Kafka Ecosystem):
In the context of Confluent Schema Registry, which of the following best describes the compatibility setting 'BACKWARD' for Avro schemas?

- A. New schema can read data produced with the previous schema, but old schema cannot read data produced with the new schema.
- B. New schema must be identical to the previous schema to maintain compatibility.
- C. New schema can read data produced with the previous schema, ensuring consumers using the new schema can process old data.
- D. New schema is completely independent and does not need to consider previous schemas for compatibility.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The 'BACKWARD' compatibility mode in Confluent Schema Registry ensures that consumers using the new schema can correctly deserialize data produced with the previous schema version. This is critical for seamless schema evolution in Kafka applications, as it guarantees that schema updates do not break existing consumers. Common misconceptions include confusing 'BACKWARD' with 'FORWARD' compatibility or assuming schemas must remain identical to be compatible. Understanding these compatibility modes is essential for developers to safely evolve data schemas while maintaining data integrity and application stability in the Kafka ecosystem. BACKWARD is also the default compatibility level in Schema Registry (BACKWARD_TRANSITIVE checks against all previous versions, not only the latest). Option A is not the best answer because BACKWARD does not require that the old schema be unable to read new data.

Source: Confluent docs, Schema Evolution and Compatibility: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

**Detailed explanation of each option:**

1. ❌ **A. New schema can read data produced with the previous schema, but old schema cannot read data produced with the new schema.**  
   **Incorrect** (as the best answer). The first half ("new schema can read data produced with the previous schema") is exactly what BACKWARD guarantees, however, the added claim that the old schema cannot read new data is not a property of BACKWARD (it is simply not guaranteed - FULL compatibility allows both). C states the BACKWARD guarantee without that extra claim, so C is the better answer. FORWARD would be the reverse direction (old schema can read data written with the new schema).

2. ❌ **B. New schema must be identical to the previous schema to maintain compatibility.**  
   **Incorrect**. Identical schema means no evolution, compatibility settings like BACKWARD allow certain changes without breaking consumers.

3. ✅ **C. New schema can read data produced with the previous schema, ensuring consumers using the new schema can process old data.**  
   **Correct**. Backward compatibility means the new schema can deserialize data written with the previous schema, allowing consumers to read older data.

4. ❌ **D. New schema is completely independent and does not need to consider previous schemas for compatibility.**  
   **Incorrect**. Schema Registry enforces compatibility settings to ensure schema evolution does not break consumers or producers.

</details>

## Question 29 (Reliable Data Delivery):
Which of the following configurations and design choices in Apache Kafka help ensure exactly-once delivery semantics (EOS) for a Kafka producer-consumer pipeline?

- A. Use Kafka transactions by invoking 'initTransactions()', 'beginTransaction()', and 'commitTransaction()' in the producer
- B. Use 'acks=all' to require full ISR acknowledgment before considering a write successful
- C. Enable idempotent producer by setting 'enable.idempotence=true'
- D. Set 'enable.auto.commit=true' on the consumer to automatically commit offsets after processing
- E. Disable producer retries to avoid duplicate message production
- F. Configure 'acks=0' to reduce latency and improve throughput in high-volume pipelines

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Achieving exactly-once semantics in Kafka requires a combination of enabling the idempotent producer, ensuring full acknowledgment from all in-sync replicas ('acks=all'), and using Kafka transactions to atomically write and commit messages across partitions or topics. Idempotence prevents duplicate messages on retries, while full acknowledgments avoid data loss due to broker failures. Transactions ensure atomicity and consistency of the data pipeline. Misconfigurations such as disabling retries, relying on auto offset commits, or using low acknowledgment levels undermine reliability guarantees, leading to potential message loss or duplication. Understanding and properly configuring these features is crucial for developers seeking to build fault-tolerant, reliable Kafka applications aligned with Confluent's best practices.

Source: Kafka: The Definitive Guide 2nd ed., ch. 8 (idempotent producer) and ch. 8 "Exactly-Once Semantics" (transactions), https://kafka.apache.org/documentation/#semantics

**Detailed explanation of each option:**

1. ✅ **A. Use Kafka transactions by invoking 'initTransactions()', 'beginTransaction()', and 'commitTransaction()' in the producer**  
   **Correct**. Kafka transactions allow atomic writes across multiple partitions or topics, enabling exactly-once semantics in multi-topic or multi-partition writes.

2. ✅ **B. Use 'acks=all' to require full ISR acknowledgment before considering a write successful**  
   **Correct**. Setting 'acks=all' guarantees the message is committed to all in-sync replicas, preventing data loss and supporting EOS guarantees.

3. ✅ **C. Enable idempotent producer by setting 'enable.idempotence=true'**  
   **Correct**. Enabling idempotence ensures that retries of the same message do not result in duplicates, which is fundamental for achieving exactly-once delivery.

4. ❌ **D. Set 'enable.auto.commit=true' on the consumer to automatically commit offsets after processing**  
   **Incorrect**. Automatic offset commits may occur before processing completes, risking message loss or duplication, manual offset management within transactions is preferred for EOS.

5. ❌ **E. Disable producer retries to avoid duplicate message production**  
   **Incorrect**. Disabling retries can lead to message loss on transient failures, retries combined with idempotence prevent duplicates while maintaining reliability.

6. ❌ **F. Configure 'acks=0' to reduce latency and improve throughput in high-volume pipelines**  
   **Incorrect**. 'acks=0' does not wait for any broker acknowledgment, which risks data loss and does not support reliable or exactly-once delivery guarantees.

</details>

## Question 30 (Kafka Core Concepts):
In Apache Kafka, which of the following best describes the role of the leader replica in a partition's replication process?

- A. The leader replica periodically checkpoints committed offsets but does not handle replication.
- B. The leader replica only serves read requests while followers handle write requests to balance the load.
- C. The leader replica is responsible for serving all read and write requests for the partition and replicating data to follower replicas.
- D. The leader replica replicates data from followers to keep the cluster in sync.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka's replication mechanism, the leader replica of a partition is the authoritative source of data, handling all client reads and writes. It is responsible for replicating data to follower replicas, which maintain copies but do not serve write requests. This design ensures consistency and fault tolerance. Common misconceptions include the idea that followers can serve writes or that replication occurs bidirectionally. Understanding the leader’s role is essential for designing resilient Kafka applications and troubleshooting replication issues. (Nuance: since Kafka 2.4 / KIP-392 consumers may optionally fetch from follower replicas via replica.selector.class, but writes always go to the leader and C remains the best answer.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Replication" (p. 139), https://kafka.apache.org/documentation/#replication

**Detailed explanation of each option:**

1. ❌ **A. The leader replica periodically checkpoints committed offsets but does not handle replication.**  
   **Incorrect**. While committed offsets are managed, the leader’s primary role includes handling replication to followers.

2. ❌ **B. The leader replica only serves read requests while followers handle write requests to balance the load.**  
   **Incorrect**. Followers do not serve write requests, only the leader handles writes to maintain a single source of truth.

3. ✅ **C. The leader replica is responsible for serving all read and write requests for the partition and replicating data to follower replicas.**  
   **Correct**. The leader handles all client requests and ensures data is replicated to followers, maintaining consistency and availability.

4. ❌ **D. The leader replica replicates data from followers to keep the cluster in sync.**  
   **Incorrect**. Replication is one-way, from leader to followers: followers PULL new records from the leader with fetch requests (the leader never copies data from followers).

</details>

## Question 31 (Reliable Data Delivery):
When validating the reliability of data delivery in Apache Kafka, which of the following configurations or design choices directly contribute to ensuring at-least-once or exactly-once delivery semantics?

- A. Implementing exactly-once semantics using Kafka Streams with transactions enabled
- B. Using a single partition topic to avoid out-of-order message delivery
- C. Enabling producer retries with idempotence set to true
- D. Using a consumer with enable.auto.commit=true and a short auto commit interval
- E. Setting acks=all on the producer configuration
- F. Configuring log.retention.ms to a very low value to free up space quickly

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, E

**Explanation:**

Reliable data delivery in Apache Kafka hinges on configuring the producer and consumer to handle potential failures without data loss or duplication. Enabling producer idempotence with retries and setting acks=all ensures that messages are durably written to all in-sync replicas, which is essential for at-least-once or exactly-once semantics. Kafka Streams uses transactions to provide exactly-once processing guarantees in stream processing pipelines. Conversely, relying on auto offset commits or reducing retention times can jeopardize reliability by risking message loss or duplication. While partitioning affects ordering and throughput, it does not directly guarantee reliability. Understanding these configurations is critical for developers to build robust Kafka applications that meet strict delivery guarantees.

Source: Kafka: The Definitive Guide 2nd ed., ch. 8 "Reliable Data Delivery" (acks, retries, idempotence, exactly-once, consumer commits), https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence

**Detailed explanation of each option:**

1. ✅ **A. Implementing exactly-once semantics using Kafka Streams with transactions enabled**  
   **Correct**. : Kafka Streams leverages Kafka’s transactional APIs to provide end-to-end exactly-once processing, ensuring reliable data delivery in stream processing applications.

2. ❌ **B. Using a single partition topic to avoid out-of-order message delivery**  
   **Incorrect**. : While a single partition preserves order, it limits throughput and does not inherently improve delivery reliability, delivery guarantees depend on other configurations.

3. ✅ **C. Enabling producer retries with idempotence set to true**  
   **Correct**. : Enabling idempotence ensures that even if retries occur, duplicates are avoided, enabling exactly-once delivery semantics on the producer side.

4. ❌ **D. Using a consumer with enable.auto.commit=true and a short auto commit interval**  
   **Incorrect**. : While auto committing offsets simplifies processing, it can cause message loss or duplicates if the consumer crashes before processing, manual offset management is preferred for reliable delivery.

5. ✅ **E. Setting acks=all on the producer configuration**  
   **Correct**. : Using acks=all guarantees that the leader waits for all in-sync replicas to acknowledge the write, enhancing durability and minimizing data loss, which is critical for reliable delivery.

6. ❌ **F. Configuring log.retention.ms to a very low value to free up space quickly**  
   **Incorrect**. : Setting low retention times risks deleting messages before consumers have processed them, which can lead to data loss and unreliability.

</details>

## Question 32 (Kafka Core Concepts):
Which producer configuration setting in Apache Kafka ensures that a message is considered successfully written only after it has been replicated to all in-sync replicas, thereby maximizing data durability?

- A. "acks=all"
- B. "acks=0"
- C. "retries=0"
- D. "linger.ms=100"

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The 'acks' configuration in Kafka producers dictates the durability and reliability of message delivery. Setting 'acks=all' ensures that the leader broker waits for all in-sync replicas to acknowledge the message before considering it successfully written, providing the highest level of durability and minimizing data loss risks. In contrast, 'acks=0' offers no acknowledgment, risking message loss, and 'acks=1' waits only for the leader, which is less durable. Other configurations like 'retries' and 'linger.ms' affect retry behavior and batching efficiency but do not directly influence acknowledgment and replication guarantees. Understanding and correctly configuring 'acks' is critical for developers aiming to meet strict data durability requirements in production Kafka deployments. Precisely: the leader waits for the replicas that are currently in the ISR (not literally all assigned replicas), and the write is rejected if the ISR is smaller than min.insync.replicas. (Since Kafka 3.0 acks=all is the default together with enable.idempotence=true.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 "Acknowledgments (acks)" and ch. 8, https://kafka.apache.org/documentation/#producerconfigs_acks

**Detailed explanation of each option:**

1. ✅ **A. "acks=all"**  
   **Correct**. Setting acks=all (or acks=-1) ensures the leader waits for all in-sync replicas to acknowledge the write, maximizing durability.

2. ❌ **B. "acks=0"**  
   **Incorrect**. Setting acks=0 means the producer does not wait for any acknowledgment from the broker, risking message loss.

3. ❌ **C. "retries=0"**  
   **Incorrect**. Retries control the number of resend attempts on failure but do not affect acknowledgment behavior or durability guarantees.

4. ❌ **D. "linger.ms=100"**  
   **Incorrect**. linger.ms controls batching delay and throughput but does not impact acknowledgment or replication guarantees.

</details>

## 🚫 Question 33 (Kafka Internals):
In the context of Kafka's request processing pipeline within the broker, which of the following statements accurately describe key aspects of how incoming client requests are handled to ensure efficiency and correctness?

- A. Partition leaders apply received produce requests directly to the local log and replicate asynchronously to followers.
- B. Request processing includes metrics collection and request throttling to manage load and ensure broker stability.
- C. Kafka uses a request queue per topic partition to serialize request processing and maintain strict ordering.
- D. Network (processor) threads place incoming requests on a request queue, from which I/O (request handler) threads pick them up and process them, with responses going through a response queue.
- E. Requests are processed synchronously in a single thread per broker to guarantee order and reduce complexity.
- F. Fetch requests are served exclusively by the Kafka controller to ensure consistency across replicas.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

Kafka's request processing pipeline involves multiple components working in concert to handle client requests efficiently and correctly. Network threads queue incoming requests and I/O (request handler) threads process them. Leaders apply produce requests to their local logs and replicate asynchronously to followers for durability. Fetch requests are served by leaders, not the controller, which manages cluster state. Kafka does not serialize requests per partition through explicit queues but relies on the partition log's inherent ordering. Additionally, the broker collects detailed metrics and enforces throttling policies to maintain stability under load. Understanding these internals is critical for developers optimizing Kafka client interactions and troubleshooting performance issues.

option D reworded, because the original ("forward the requests to the partition leaders") was wrong - clients must send produce/fetch directly to the leader and get a "Not a Leader" error otherwise. The reworded D matches the book (network threads -> request queue -> I/O threads -> response queue). Answer A, B, D confirmed.

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Request Processing" (pp. 143-145)

**Detailed explanation of each option:**

1. ✅ **A. Partition leaders apply received produce requests directly to the local log and replicate asynchronously to followers.**  
   **Correct**. The partition leader writes produce requests to its local log and asynchronously replicates the data to follower replicas to maintain consistency.

2. ✅ **B. Request processing includes metrics collection and request throttling to manage load and ensure broker stability.**  
   **Correct**. Kafka brokers collect metrics during request processing and apply throttling policies (e.g., quota enforcement) to prevent overload and ensure stable operation.

3. ❌ **C. Kafka uses a request queue per topic partition to serialize request processing and maintain strict ordering.**  
   **Incorrect**. Kafka does not maintain a request queue per partition at the broker level for processing. Instead, request handler threads process requests and the ordering is maintained by the partition leader’s log.

4. ✅ **D. Network (processor) threads place incoming requests on a request queue, from which I/O (request handler) threads pick them up and process them, with responses going through a response queue.**  
   **Correct**. This is the broker request pipeline described in the book (ch. 6), clients send produce/fetch requests directly to the partition leader, the broker does not forward them.

5. ❌ **E. Requests are processed synchronously in a single thread per broker to guarantee order and reduce complexity.**  
   **Incorrect**. Kafka uses multiple I/O threads and request handler threads to process requests concurrently, improving throughput. Synchronous single-thread processing would severely limit scalability.

6. ❌ **F. Fetch requests are served exclusively by the Kafka controller to ensure consistency across replicas.**  
   **Incorrect**. Fetch requests are served by partition leaders, not the controller. The controller manages cluster metadata and leader election, not direct client fetch processing.

</details>

## 🚫 Question 34 (Kafka Connect):
When configuring the JDBC Source Connector in Kafka Connect, which of the following statements about its behavior and configuration are true?

- A. The JDBC Source Connector automatically creates the source tables in the database if they do not exist.
- B. The connector can only read from a single table per task without any support for custom queries.
- C. The "mode" configuration can be set to "bulk" for full table reloads or "incrementing"/"timestamp+incrementing" for incremental loading.
- D. The connector uses a timestamp column or incrementing column to track offsets for incremental data loading.
- E. The connector requires Schema Registry and cannot be used with the JSON converter.
- F. Setting "batch.max.rows" controls the maximum number of rows fetched per poll from the database.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, F

**Explanation:**

The JDBC Source Connector supports incremental loading by leveraging timestamp and/or incrementing columns to track new or updated rows, which is critical for efficient data ingestion without duplication.
Configuration options like "batch.max.rows" influence query size and performance.
The "mode" parameter dictates whether data is loaded in bulk or incrementally.
Contrary to some misconceptions, the connector supports custom SQL queries, allowing flexible data extraction beyond single tables.
It does not automatically create target tables in the sink database, nor does it inherently register schemas with Schema Registry.
Understanding these nuances is vital for correctly configuring and optimizing JDBC connectors in Kafka Connect environments.
 C, D, F confirmed (modes bulk/incrementing/timestamp/timestamp+incrementing, batch.max.rows, query).
Options A and E were ambiguous in the original (A talked about the Sink connector, and E could be read as true because the config page lists auto.register.schemas), so they were reworded minimally to be unambiguously false. The JDBC connector is a system-specific connector, outside the exam scope.

Source: https://docs.confluent.io/kafka-connectors/jdbc/current/source-connector/source_config_options.html

**Detailed explanation of each option:**

1. ❌ **A. The JDBC Source Connector automatically creates the source tables in the database if they do not exist.**  
   **Incorrect**. A source connector only reads from existing tables/queries, it never creates them.

2. ❌ **B. The connector can only read from a single table per task without any support for custom queries.**  
   **Incorrect**. The connector supports custom queries via the "query" configuration, allowing reading from multiple tables or complex joins, not just a single table.

3. ✅ **C. The "mode" configuration can be set to "bulk" for full table reloads or "incrementing"/"timestamp+incrementing" for incremental loading.**  
   **Correct**. The "mode" parameter controls how the connector tracks and loads data: "bulk" reloads all data, while "incrementing" and "timestamp+incrementing" enable incremental updates.

4. ✅ **D. The connector uses a timestamp column or incrementing column to track offsets for incremental data loading.**  
   **Correct**. The JDBC Source Connector relies on timestamp or incrementing columns to identify new or updated rows since the last poll, which is essential for incremental loading.

5. ❌ **E. The connector requires Schema Registry and cannot be used with the JSON converter.**  
   **Incorrect**. The connector builds a Connect schema from the table, registering it in Schema Registry is done by the configured converter (e.g. AvroConverter) and is optional - JsonConverter works too.

6. ✅ **F. Setting "batch.max.rows" controls the maximum number of rows fetched per poll from the database.**  
   **Correct**. This configuration parameter limits how many rows the connector retrieves in each query execution, helping control memory usage and throughput.

</details>

## 🚫 Question 35 (Kafka Setup and Operations):
Which of the following statements accurately describe the role and characteristics of ZooKeeper in Apache Kafka cluster setup and operations?

- A. ZooKeeper stores the actual Kafka message data to ensure durability.
- B. ZooKeeper manages Kafka broker metadata, including leader election for partitions.
- C. ZooKeeper maintains configuration information for Kafka topics and brokers.
- D. ZooKeeper is responsible for replicating partition data across brokers.
- E. Kafka can operate natively without ZooKeeper in all versions since it is optional.
- F. ZooKeeper ensures synchronization and coordination between Kafka brokers.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

ZooKeeper plays a critical role in traditional Apache Kafka clusters by managing metadata, orchestrating leader elections for partition leaders, and maintaining configuration data necessary for cluster coordination. It does not store actual message data nor handle replication directly, those responsibilities lie with Kafka brokers. ZooKeeper ensures synchronization between brokers, which is vital for consistent cluster operations. Although Kafka is evolving to reduce ZooKeeper dependency with KRaft mode, Confluent Certified Developer certification primarily covers ZooKeeper-based setups, making its understanding essential. Common misconceptions include assuming ZooKeeper stores message data or replicates partitions, which it does not. (Today ZooKeeper is legacy: KRaft is production-ready since 3.3 and ZooKeeper was removed in Kafka 4.0, E is false because ZooKeeper was required in all versions before KRaft. Outside the exam scope.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Cluster Membership" (p. 135), https://kafka.apache.org/documentation/#zk_depr

**Detailed explanation of each option:**

1. ❌ **A. ZooKeeper stores the actual Kafka message data to ensure durability.**  
   **Incorrect**. Kafka message data is stored on brokers' local disks, ZooKeeper does not store message data but only metadata.

2. ✅ **B. ZooKeeper manages Kafka broker metadata, including leader election for partitions.**  
   **Correct**. ZooKeeper is responsible for managing broker metadata and conducting leader elections for Kafka partitions to ensure high availability.

3. ✅ **C. ZooKeeper maintains configuration information for Kafka topics and brokers.**  
   **Correct**. ZooKeeper holds configuration details such as topic configurations, broker registrations, and access control lists.

4. ❌ **D. ZooKeeper is responsible for replicating partition data across brokers.**  
   **Incorrect**. Partition replication is handled by Kafka brokers themselves, not ZooKeeper.

5. ❌ **E. Kafka can operate natively without ZooKeeper in all versions since it is optional.**  
   **Incorrect**. While newer Kafka versions support KRaft mode to remove ZooKeeper dependency, in the context of Confluent Certified Developer (which currently focuses on ZooKeeper-based setups), ZooKeeper is essential.

6. ✅ **F. ZooKeeper ensures synchronization and coordination between Kafka brokers.**  
   **Correct**. ZooKeeper provides synchronization mechanisms and coordination services, enabling brokers to work together consistently.

</details>

## 🚫 Question 36 (Kafka Internals):
In the context of Kafka's ZooKeeper-based (pre-KRaft) cluster membership protocol, which of the following statements accurately describe how Kafka brokers maintain and update cluster membership information?

- A. The controller broker is responsible for monitoring the membership state and triggering rebalances when brokers join or leave the cluster.
- B. When a broker fails, the cluster membership information remains until a manual cleanup is performed to remove the dead broker from the cluster metadata.
- C. Kafka's cluster membership protocol ensures that all brokers have a consistent view of live brokers by using session timeouts and heartbeat mechanisms.
- D. Kafka brokers maintain membership state by persisting broker session information directly in Kafka topics dedicated to cluster metadata.
- E. Kafka brokers use a gossip protocol to exchange membership information among themselves without relying on ZooKeeper.
- F. Kafka brokers use ZooKeeper ephemeral nodes to track live broker membership, which are automatically removed when a broker fails or disconnects.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

Kafka's cluster membership relies on ephemeral nodes in ZooKeeper (or session management in KRaft) to indicate live brokers, which are automatically removed upon broker failure or disconnection. The controller broker monitors these membership changes and triggers necessary metadata updates and partition reassignments to maintain cluster consistency. Heartbeat mechanisms ensure timely detection of dead brokers, enabling the cluster to maintain an accurate and consistent membership view without manual intervention. Misconceptions include assuming gossip protocols or manual cleanup processes are involved, which Kafka does not use for membership management.

Re-verified: stem now explicitly says ZooKeeper-based (pre-KRaft), which makes D unambiguously false. In KRaft mode (KIP-631) brokers send BrokerRegistration/heartbeat requests to the controller quorum (broker.session.timeout.ms = lease length, default 9000) and RegisterBrokerRecord is stored in the __cluster_metadata topic, so D would be true there. Original note: broker-internals question (outside the exam scope), written for the ZooKeeper era. Per the book, brokers register ephemeral znodes under /brokers/ids and the controller/other brokers watch them (F, C correct), the controller then reacts by electing new partition leaders (A uses "rebalances", which is loosely worded - consumer-group rebalances are done by the group coordinator). In KRaft mode (default since 3.3, only option in 4.x) brokers register with the controller quorum and send heartbeats (broker.session.timeout.ms), and registrations are records in the __cluster_metadata topic, so D would be arguably true in KRaft, marked answer A, C, F left unchanged.

Source: https://cwiki.apache.org/confluence/display/KAFKA/KIP-631%3A+The+Quorum-based+Kafka+Controller , https://kafka.apache.org/42/configuration/broker-configs/ (broker.session.timeout.ms) , book ch. 6 pp. 135-137

**Detailed explanation of each option:**

1. ✅ **A. The controller broker is responsible for monitoring the membership state and triggering rebalances when brokers join or leave the cluster.**  
   **Correct**. The controller monitors broker membership changes and initiates partition leadership reassignments and metadata updates accordingly.

2. ❌ **B. When a broker fails, the cluster membership information remains until a manual cleanup is performed to remove the dead broker from the cluster metadata.**  
   **Incorrect**. Ephemeral nodes in ZooKeeper or session timeouts in KRaft ensure automatic removal of failed brokers from cluster membership.

3. ✅ **C. Kafka's cluster membership protocol ensures that all brokers have a consistent view of live brokers by using session timeouts and heartbeat mechanisms.**  
   **Correct**. Heartbeats with ZooKeeper or KRaft sessions allow brokers and the controller to detect failed brokers and maintain consistent membership state.

4. ❌ **D. Kafka brokers maintain membership state by persisting broker session information directly in Kafka topics dedicated to cluster metadata.**  
   **Incorrect**. Brokers do not store membership session info in Kafka topics, this information is managed via ZooKeeper ephemeral nodes or KRaft metadata quorum.

5. ❌ **E. Kafka brokers use a gossip protocol to exchange membership information among themselves without relying on ZooKeeper.**  
   **Incorrect**. Kafka does not use a gossip protocol for cluster membership, instead, it relies on ZooKeeper (pre-KRaft) or KRaft metadata quorum depending on the mode.

6. ✅ **F. Kafka brokers use ZooKeeper ephemeral nodes to track live broker membership, which are automatically removed when a broker fails or disconnects.**  
   **Correct**. Kafka brokers register ephemeral nodes in ZooKeeper to indicate live membership, which get deleted if the broker session expires, enabling failure detection.

</details>

## Question 37 (Kafka Consumers):
In Apache Kafka, which of the following strategies best ensures consumer reliability and precise offset management to avoid duplicate processing or data loss when using the KafkaConsumer API?

- A. Enable 'enable.auto.commit' and rely on Kafka’s automatic offset commits at regular intervals.
- B. Disable offset commits entirely and rely on external storage to track message processing state for reliability.
- C. Manually commit offsets synchronously only after processing each batch of records to ensure at-least-once delivery semantics.
- D. Commit offsets asynchronously immediately after fetching records to maximize consumer throughput.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Manual synchronous offset commits after successful message processing provide the most reliable offset management in Kafka consumers. This approach ensures offsets only advance when processing completes, preventing data loss or duplicate processing common with automatic commits or premature asynchronous commits. Automatic commits, while convenient, commit offsets at fixed intervals regardless of processing status, which can cause inconsistencies especially during failures. Relying on external offset storage adds complexity and is rarely needed unless implementing advanced exactly-once semantics beyond Kafka's built-in capabilities. Understanding these offset management strategies is critical for developers seeking to build reliable Kafka consumers aligned with best practices in the Confluent Certified Developer for Apache Kafka exam.

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 "Commits and Offsets" - "Synchronous Commit" (at-least-once, commit after processing the batch), https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit

**Detailed explanation of each option:**

1. ❌ **A. Enable 'enable.auto.commit' and rely on Kafka’s automatic offset commits at regular intervals.**  
   **Incorrect**. While automatic offset commits simplify offset management, they can lead to duplicate processing or data loss because offsets may be committed before or after message processing, reducing reliability.

2. ❌ **B. Disable offset commits entirely and rely on external storage to track message processing state for reliability.**  
   **Incorrect**. Disabling offset commits requires implementing custom offset tracking, which adds complexity and is not typically necessary for standard reliability use cases with KafkaConsumer.

3. ✅ **C. Manually commit offsets synchronously only after processing each batch of records to ensure at-least-once delivery semantics.**  
   **Correct**. This is the recommended approach for precise offset management and consumer reliability. Committing offsets manually after processing guarantees offsets reflect processed messages, minimizing duplicate or lost data.

4. ❌ **D. Commit offsets asynchronously immediately after fetching records to maximize consumer throughput.**  
   **Incorrect**. Committing offsets asynchronously right after fetching messages risks acknowledging unprocessed messages, which can cause data loss if the consumer crashes before processing completes.

</details>

## Question 38 (Kafka Consumers): [-]
When creating a Kafka consumer in a Confluent platform environment, which of the following configurations and practices are essential to ensure correct and efficient consumption of messages?

- A. Using 'auto.commit.interval.ms' to set the frequency of automatic offset commits when 'enable.auto.commit' is true
- B. Specifying 'key.deserializer' and 'value.deserializer' to correctly deserialize records fetched from Kafka
- C. Setting 'max.poll.records' to 1 to minimize memory usage and improve throughput
- D. Disabling 'enable.auto.commit' and manually committing offsets to have precise control over message processing
- E. Using 'auto.offset.reset' set to 'latest' to start consuming from the earliest available message in the topic
- F. Setting the 'group.id' configuration to enable consumer group coordination and offset management

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, B, D, F

**Explanation:**

Creating an efficient Kafka consumer involves configuring key parameters that affect message processing, offset management, and deserialization. Setting 'group.id' is fundamental for consumer group coordination and offset tracking. Disabling 'enable.auto.commit' grants the developer control over when offsets are committed, improving reliability. Correct deserializers must be specified to interpret Kafka messages properly. The 'auto.commit.interval.ms' setting only applies if automatic commits are enabled and influences commit frequency. Misconfigurations such as setting 'auto.offset.reset' to 'latest' when trying to consume from the beginning, or setting 'max.poll.records' too low, can lead to inefficient or incorrect consumption patterns. Understanding these configurations is critical for passing the Confluent Certified Developer exam and for building robust consumer applications in production. (Precision: key.deserializer and value.deserializer are mandatory, group.id is required when using subscribe()/offset commits, but not when using assign() without commits. max.poll.records=1 would reduce, not improve, throughput.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 "Configuring Consumers" (pp. 87-93), https://kafka.apache.org/documentation/#consumerconfigs

**Detailed explanation of each option:**

1. ✅ **A. Using 'auto.commit.interval.ms' to set the frequency of automatic offset commits when 'enable.auto.commit' is true**  
   **Correct**. This setting controls how often offsets are committed automatically, impacting the balance between throughput and potential message reprocessing.

2. ✅ **B. Specifying 'key.deserializer' and 'value.deserializer' to correctly deserialize records fetched from Kafka**  
   **Correct**. Proper deserializers must be configured to convert byte arrays into usable key and value objects in the application.

3. ❌ **C. Setting 'max.poll.records' to 1 to minimize memory usage and improve throughput**  
   **Incorrect**. While setting 'max.poll.records' to 1 reduces memory usage, it negatively impacts throughput by fetching one record at a time, which is typically inefficient.

4. ✅ **D. Disabling 'enable.auto.commit' and manually committing offsets to have precise control over message processing**  
   **Correct**. Disabling automatic commits allows the application to commit offsets only after processing messages successfully, improving reliability.

5. ❌ **E. Using 'auto.offset.reset' set to 'latest' to start consuming from the earliest available message in the topic**  
   **Incorrect**. Setting 'auto.offset.reset' to 'latest' causes the consumer to start from the end of the topic, not the earliest message. To consume from the beginning, it should be set to 'earliest'.

6. ✅ **F. Setting the 'group.id' configuration to enable consumer group coordination and offset management**  
   **Correct**. The 'group.id' uniquely identifies the consumer group and is required for Kafka to manage offset commits and load balancing among consumers.

</details>

## Question 39 (Stream Processing):
In the context of stateful stream processing with Kafka Streams, which of the following statements about state stores and their management are true?

- A. State stores can be either persistent (RocksDB) or in-memory, and the choice affects fault tolerance and performance trade-offs.
- B. State stores in Kafka Streams are immutable after initialization, and any updates require rebuilding the entire state store.
- C. State stores are backed by Kafka topics called changelogs that ensure fault-tolerance by capturing all state changes.
- D. Interactive queries allow querying the local state stores of Kafka Streams instances, enabling real-time state access without external databases.
- E. Kafka Streams automatically replicates state stores across multiple instances to provide high availability.
- F. Windowed aggregations rely on in-memory state stores only and do not use changelog topics for durability.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

Stateful operations in Kafka Streams rely heavily on state stores to maintain intermediate computation results such as aggregations or joins. These state stores are backed by Kafka changelog topics, ensuring fault tolerance by persisting state changes and enabling recovery. Developers can choose between persistent stores like RocksDB for durability or in-memory stores for faster reads with less durability. Kafka Streams does not replicate state stores across instances by default (num.standby.replicas defaults to 0), it achieves fault tolerance through changelog topics, and standby replicas are an opt-in feature that speed up failover. Interactive queries expose local state stores to external clients, enabling real-time querying without additional databases. Common misconceptions include thinking state stores are immutable or windowed aggregations lack durability, which are incorrect as state stores are mutable and by default backed by changelogs (changelog logging can be disabled per store with withLoggingDisabled(), but windowed stores log by default).

Source: Kafka Streams docs - state stores, fault tolerance, standby replicas: https://kafka.apache.org/documentation/streams/architecture#streams_architecture_state , interactive queries: https://kafka.apache.org/documentation/streams/developer-guide/interactive-queries.html , book ch. 14 "Kafka Streams: By Example" (local state, p. 393)

**Detailed explanation of each option:**

1. ✅ **A. State stores can be either persistent (RocksDB) or in-memory, and the choice affects fault tolerance and performance trade-offs.**  
   **Correct**. RocksDB is commonly used for persistent state stores providing durability, while in-memory stores offer faster access but no durability.

2. ❌ **B. State stores in Kafka Streams are immutable after initialization, and any updates require rebuilding the entire state store.**  
   **Incorrect**. State stores are mutable and continuously updated as new records are processed, rebuilding is not necessary for every update.

3. ✅ **C. State stores are backed by Kafka topics called changelogs that ensure fault-tolerance by capturing all state changes.**  
   **Correct**. Kafka Streams uses changelog topics to persist state store updates, enabling fault-tolerance and state recovery on failure.

4. ✅ **D. Interactive queries allow querying the local state stores of Kafka Streams instances, enabling real-time state access without external databases.**  
   **Correct**. Interactive queries provide direct access to local state stores, allowing real-time querying of stateful data.

5. ❌ **E. Kafka Streams automatically replicates state stores across multiple instances to provide high availability.**  
   **Incorrect**. Kafka Streams achieves fault tolerance by persisting state changes to changelog topics, but it does not automatically replicate state stores across instances, only one instance owns a partition and its state. High availability through standby replicas must be enabled explicitly with num.standby.replicas (default 0).

6. ❌ **F. Windowed aggregations rely on in-memory state stores only and do not use changelog topics for durability.**  
   **Incorrect**. Windowed aggregations use state stores that are backed by changelog topics to provide durability and fault tolerance.

</details>

## Question 40 (Kafka Connect):
When running Kafka Connect in distributed mode, which of the following statements about connector management and fault tolerance are true?

- A. Connectors can be dynamically added or removed without restarting the Connect cluster.
- B. Connector configurations are stored in Kafka topics to enable fault tolerance and cluster coordination.
- C. Each connector instance runs exclusively on a single worker and cannot be rebalanced across workers.
- D. Restarting an individual worker node will cause all connectors to restart cluster-wide.
- E. Distributed mode provides automatic failover by reassigning tasks from failed workers to active ones.
- F. Kafka Connect workers maintain state only in local files and do not rely on Kafka for cluster state.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

Kafka Connect in distributed mode leverages Kafka internal topics to store connector configurations and offsets, enabling fault tolerance and state synchronization across workers. Connectors and their tasks can be dynamically added, removed, or rebalanced without restarting the entire cluster, supporting smooth operational flexibility. Automatic failover is provided by task reassignment when worker nodes fail, ensuring high availability. Common misconceptions include believing that connectors run exclusively on one worker without rebalancing or that state is stored locally, which applies only to standalone mode. Understanding these mechanisms is essential for effectively managing scalable and resilient Kafka Connect deployments. (Distributed mode stores configs, offsets and status in the config.storage.topic, offset.storage.topic and status.storage.topic, since Kafka 2.3 incremental cooperative rebalancing means a worker restart does not stop all connectors cluster-wide.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 9 "Kafka Connect" (running Connect, distributed mode), https://kafka.apache.org/documentation/#connect_running

**Detailed explanation of each option:**

1. ✅ **A. Connectors can be dynamically added or removed without restarting the Connect cluster.**  
   **Correct**. In distributed mode, Kafka Connect supports dynamic management of connectors via the REST API without requiring restarts.

2. ✅ **B. Connector configurations are stored in Kafka topics to enable fault tolerance and cluster coordination.**  
   **Correct**. Distributed mode stores connector configs and offsets in internal Kafka topics to provide fault tolerance and enable worker coordination.

3. ❌ **C. Each connector instance runs exclusively on a single worker and cannot be rebalanced across workers.**  
   **Incorrect**. Connectors’ tasks are distributed and can be rebalanced across workers to ensure high availability.

4. ❌ **D. Restarting an individual worker node will cause all connectors to restart cluster-wide.**  
   **Incorrect**. Restarting a worker only affects tasks assigned to that worker, the cluster continues running other tasks without interruption.

5. ✅ **E. Distributed mode provides automatic failover by reassigning tasks from failed workers to active ones.**  
   **Correct**. When a worker fails, tasks it ran are automatically reassigned to other active workers to maintain connector availability.

6. ❌ **F. Kafka Connect workers maintain state only in local files and do not rely on Kafka for cluster state.**  
   **Incorrect**. Distributed mode relies on Kafka internal topics for state management rather than local files.

</details>

## 🚫 Question 41 (Kafka Ecosystem):
In ksqlDB, which of the following statements correctly describes how the STREAM and TABLE abstractions differ in terms of data processing and state management?

- A. Both STREAM and TABLE abstractions in ksqlDB are stateless, with state being managed externally by Kafka brokers.
- B. TABLEs in ksqlDB can only be created from existing STREAMs, but STREAMs cannot be created from TABLEs.
- C. A STREAM is an unbounded sequence of immutable events, and a TABLE represents the latest state derived from those events, maintaining state internally.
- D. A STREAM represents a changelog of an evolving state while a TABLE is an unbounded sequence of immutable events.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

This question tests understanding of the fundamental abstractions in ksqlDB. STREAMs represent an unbounded, append-only sequence of immutable events, ideal for event-driven processing. TABLEs, conversely, represent evolving state, maintaining the latest value for each key, supported by internal state stores. Misunderstanding these concepts can lead to incorrect data modeling and query design. While STREAMs are stateless event sequences, TABLEs are stateful and enable complex stateful operations like aggregations and joins. Also, STREAMs and TABLEs can be transformed into one another, reflecting the flexibility of ksqlDB's abstractions in building real-time data pipelines and applications within the Kafka ecosystem.

Source: ksqlDB concepts (STREAM vs TABLE), https://docs.confluent.io/platform/current/ksqldb/concepts/ - zagadnienie ksqlDB poza zakresem CCDAK, odpowiedź C poprawna (opcja B: wyjaśnienie z "EMIT CHANGES" jest nieścisłe - EMIT CHANGES to push query, nie sposób tworzenia STREAM z TABLE).

**Detailed explanation of each option:**

1. ❌ **A. Both STREAM and TABLE abstractions in ksqlDB are stateless, with state being managed externally by Kafka brokers.**  
   **Incorrect**. TABLEs in ksqlDB are stateful abstractions that maintain local state stores, enabling stateful operations, STREAMs are stateless in terms of event processing but represent continuous data.

2. ❌ **B. TABLEs in ksqlDB can only be created from existing STREAMs, but STREAMs cannot be created from TABLEs.**  
   **Incorrect**. TABLEs can be created directly on a Kafka topic (CREATE TABLE ... WITH (KAFKA_TOPIC=...)) or derived from STREAMs/TABLEs via CREATE TABLE AS SELECT, so "only from existing STREAMs" is false. (EMIT CHANGES only makes a query a push query, it is not how a STREAM is created from a TABLE.)

3. ✅ **C. A STREAM is an unbounded sequence of immutable events, and a TABLE represents the latest state derived from those events, maintaining state internally.**  
   **Correct**. In ksqlDB, a STREAM models an append-only sequence of events, while a TABLE represents a stateful abstraction that reflects the latest values keyed by a unique identifier, maintained internally as state stores.

4. ❌ **D. A STREAM represents a changelog of an evolving state while a TABLE is an unbounded sequence of immutable events.**  
   **Incorrect**. This reverses the definitions. A TABLE represents a changelog of an evolving state, whereas a STREAM is an unbounded sequence of immutable events.

</details>

## Question 42 (Kafka Internals): [-]
In Apache Kafka's cluster membership protocol, which of the following statements accurately describe how brokers maintain membership and handle cluster changes?

- A. When a broker fails to send heartbeats within the session timeout, it is immediately removed from the cluster membership and its partitions are reassigned.
- B. Brokers use the Kafka Controller to manage membership changes and propagate metadata updates to all brokers.
- C. ZooKeeper is used to track the live brokers and their session states in older Kafka versions prior to KIP-500.
- D. The Controller triggers partition leader elections when brokers join or leave the cluster to maintain availability and balance.
- E. The cluster membership information is stored persistently on each broker's local disk to survive broker restarts.
- F. Kafka brokers use a gossip protocol among themselves to exchange membership information and detect failures.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

Kafka cluster membership management involves coordination primarily by the Kafka Controller, which tracks live brokers and propagates metadata changes. Prior to KIP-500, ZooKeeper stores broker session states and helps detect live brokers through ephemeral nodes. When brokers fail to heartbeat within the session timeout, the Controller marks them as dead and triggers partition leader elections to maintain availability. Membership data is not stored locally on brokers but managed centrally to ensure consistency. Kafka does not employ gossip protocols for membership, instead, it uses a centralized approach for coordination and fault detection. Understanding this mechanism is crucial for developers to troubleshoot broker failures and cluster rebalancing effectively. Note: in Kafka 4.x ZooKeeper is removed, brokers register with and send heartbeats to the KRaft controller quorum. Option A is wrong because the controller elects new leaders for the affected partitions (replicas are not reassigned), and option E is wrong because membership is kept in ZooKeeper/KRaft metadata (a broker only keeps its ID in meta.properties).

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Cluster Membership" and "The Controller" (pp. 135-137), https://kafka.apache.org/43/operations/kraft/

**Detailed explanation of each option:**

1. ❌ **A. When a broker fails to send heartbeats within the session timeout, it is immediately removed from the cluster membership and its partitions are reassigned.**  
   **Incorrect**. The broker is marked as dead only after session timeout expiration, but partitions reassignment depends on the Controller's logic and may not be immediate.

2. ✅ **B. Brokers use the Kafka Controller to manage membership changes and propagate metadata updates to all brokers.**  
   **Correct**. The Kafka Controller is responsible for cluster metadata management, including membership changes and leader elections, and propagates updates to brokers.

3. ✅ **C. ZooKeeper is used to track the live brokers and their session states in older Kafka versions prior to KIP-500.**  
   **Correct**. Before the KIP-500 transition, Kafka brokers rely on ZooKeeper to maintain cluster membership and detect live brokers via ephemeral nodes.

4. ✅ **D. The Controller triggers partition leader elections when brokers join or leave the cluster to maintain availability and balance.**  
   **Correct**. The Controller initiates leader elections to adjust partition leadership in response to membership changes to maintain cluster availability.

5. ❌ **E. The cluster membership information is stored persistently on each broker's local disk to survive broker restarts.**  
   **Incorrect**. Membership state is maintained in ZooKeeper or the Kafka Raft quorum (post-KIP-500), not locally on individual brokers.

6. ❌ **F. Kafka brokers use a gossip protocol among themselves to exchange membership information and detect failures.**  
   **Incorrect**. Kafka brokers do not use a gossip protocol, instead, membership is managed centrally by the Controller and ZooKeeper (pre-KIP-500) or the Quorum Controller (post-KIP-500).

</details>

## Question 43 (Kafka Core Concepts):
In Apache Kafka, which of the following best describes the role of a broker in the context of message storage and delivery?

- A. A broker is responsible for schema validation and transformation of messages before storage.
- B. A broker acts as a client that produces data to Kafka topics and consumes data from topics.
- C. A broker manages the coordination and synchronization of consumer group offsets across different topics.
- D. A broker is a Kafka server responsible for receiving messages from producers, storing them on disk, and serving them to consumers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka architecture, brokers are the fundamental servers that receive data from producers, store it durably on disk, and serve it to consumers upon request. They manage topic partitions and ensure data availability and durability. While brokers do not act as clients themselves, nor do they perform schema validation or directly manage consumer offsets, they play a crucial role in message storage and delivery. Understanding the broker's responsibilities helps developers optimize Kafka deployments and troubleshoot message flow issues effectively.

Source: Kafka: The Definitive Guide 2nd ed., ch. 1 "Brokers and Clusters", ch. 6 (group coordinator is a broker role). Note: option C is only loosely wrong - a broker acting as group coordinator does store group offsets in __consumer_offsets, D is still the best, most general answer.

**Detailed explanation of each option:**

1. ❌ **A. A broker is responsible for schema validation and transformation of messages before storage.**  
   **Incorrect**. Schema validation and transformation are usually handled by external components like Schema Registry or Kafka Streams, not brokers.

2. ❌ **B. A broker acts as a client that produces data to Kafka topics and consumes data from topics.**  
   **Incorrect**. Brokers are servers that store and manage data, not clients that produce or consume messages.

3. ❌ **C. A broker manages the coordination and synchronization of consumer group offsets across different topics.**  
   **Incorrect**. Committed offsets are stored in the internal __consumer_offsets topic and the group coordinator (itself a broker, not the controller) manages group membership, this is a secondary role, not the broker's defining one, so D remains the best answer.

4. ✅ **D. A broker is a Kafka server responsible for receiving messages from producers, storing them on disk, and serving them to consumers.**  
   **Correct**. Brokers handle message reception, persistent storage, and delivery, making them central to Kafka's messaging system.

</details>

## Question 44 (Kafka Internals):
In Apache Kafka's physical storage architecture, which component is primarily responsible for ensuring efficient sequential disk writes and enabling high-throughput data ingestion?

- A. The index files
- B. Log compaction
- C. The segment file
- D. The append-only log structure

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s physical storage relies on an append-only log structure, which is fundamental to its performance model. This design enables efficient sequential disk writes by always appending new records to the end of log segments, reducing random disk I/O. Segment files store the actual data, while index files provide fast offset-based lookup.  Understanding this append-only log design is crucial for developers to optimize Kafka's throughput and storage behavior, especially when tuning segment sizes and retention policies. Re-verified: option B was originally "The commit log", a synonym of D, making the question ambiguous, it was reworded to "Log compaction" (clearly wrong). Answer D confirmed.

Source: https://kafka.apache.org/42/design/design/ (Persistence: "a persistent queue could be built on simple reads and appends to files", sequential disk access)

**Detailed explanation of each option:**

1. ❌ **A. The index files**  
   **Incorrect**. Index files map message offsets to physical positions in segment files to enable quick lookups, but they do not facilitate sequential writes.

2. ❌ **B. Log compaction**  
   **Incorrect**. Log compaction is a retention/cleanup mechanism that removes older records per key, it does not enable sequential writes.

3. ❌ **C. The segment file**  
   **Incorrect**. Segment files store the actual data on disk but do not directly enable efficient sequential writes, they are the result of those writes.

4. ✅ **D. The append-only log structure**  
   **Correct**. Kafka’s storage is based on an append-only log which allows efficient sequential writes, minimizing disk seek times and maximizing throughput.

</details>

## Question 45 (Kafka Setup and Operations):
When deploying Apache Kafka clusters in a cloud environment using Confluent Cloud, which practice is most critical to ensure high availability and minimal data loss?

- A. Configure Kafka brokers across multiple availability zones with replication factor of at least 3 for critical topics.
- B. Disable topic replication and rely solely on producer retries to handle failures in cloud setups.
- C. Deploy all Kafka brokers in a single availability zone to reduce inter-zone network latency.
- D. Use ephemeral storage for Kafka logs to improve performance in cloud deployments.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In cloud deployments, ensuring high availability and data durability requires distributing Kafka brokers across multiple availability zones to protect against zone failures. A replication factor of at least 3 for critical topics enables Kafka to maintain replicas even if one or two brokers fail, minimizing data loss. While low latency is desirable, concentrating all brokers in one zone risks total cluster downtime if that zone fails. Disabling replication or relying on producer retries undermines Kafka's inherent fault tolerance. Using ephemeral storage compromises data persistence, so persistent, durable storage is essential. This approach aligns with best practices for Kafka operations in the cloud, ensuring resilience and reliability. (Outside CCDAK scope: deploying/administering clusters.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 2 (Kafka in the cloud, p. ~35: ephemeral storage risk) and ch. 7 (rack/AZ awareness), https://docs.confluent.io/cloud/current/clusters/cluster-types.html

**Detailed explanation of each option:**

1. ✅ **A. Configure Kafka brokers across multiple availability zones with replication factor of at least 3 for critical topics.**  
   **Correct**. Spreading brokers across AZs and using a replication factor ≥3 ensures fault tolerance and data durability in cloud environments.

2. ❌ **B. Disable topic replication and rely solely on producer retries to handle failures in cloud setups.**  
   **Incorrect**. Disabling replication risks data loss on broker failure, producer retries do not replace replication for durability.

3. ❌ **C. Deploy all Kafka brokers in a single availability zone to reduce inter-zone network latency.**  
   **Incorrect**. While this minimizes latency, it creates a single point of failure, risking cluster availability if that zone goes down.

4. ❌ **D. Use ephemeral storage for Kafka logs to improve performance in cloud deployments.**  
   **Incorrect**. Ephemeral storage is often lost if the broker restarts or migrates, risking data loss, persistent storage is recommended.

</details>

## Question 46 (Kafka Connect):
When configuring a Kafka Connect source connector for a high-throughput data pipeline, which of the following settings and practices help ensure optimal performance and fault tolerance?

- A. Utilize the "transforms" configuration to preprocess and filter records before they are sent to Kafka, reducing unnecessary data ingestion
- B. Avoid using schema registry integration to reduce connector complexity and improve performance
- C. Disable "errors.tolerance" to fail fast on any data issue, ensuring data quality without retries or dead-letter queues
- D. Increase the "tasks.max" configuration to enable parallelism and leverage multiple connector tasks for better throughput
- E. Set "offset.flush.timeout.ms" to a very high value to reduce the frequency of offset commits and minimize overhead
- F. Configure "producer.batch.size" and "producer.linger.ms" to tune batching behavior, optimizing throughput and latency trade-offs

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

Optimizing Kafka Connect source connectors requires balancing throughput, fault tolerance, and data quality. Increasing "tasks.max" enables parallelism, improving ingestion speed. Using SMTs via "transforms" helps filter or modify data early, reducing unnecessary load. Tuning producer batching parameters like "producer.batch.size" and "producer.linger.ms" directly impacts performance by controlling record batching and send frequency. Conversely, setting offset flush timeouts too high risks data loss, and disabling error tolerance reduces fault tolerance by stopping the connector on recoverable errors. Avoiding schema registry integration sacrifices schema management benefits, critical for data governance. These optimizations reflect best practices expected of a Confluent Certified Developer for Apache Kafka working with Kafka Connect. Note: "offset.flush.timeout.ms" is the maximum time to wait for the offset flush to complete, how often offsets are committed is controlled by "offset.flush.interval.ms". Also, errors.tolerance (default "none") for source connectors only covers errors in converters/transformations.

Source: https://kafka.apache.org/43/configuration/kafka-connect-configs/ , https://docs.confluent.io/platform/current/connect/userguide.html , Kafka: The Definitive Guide 2nd ed., ch. 9

**Detailed explanation of each option:**

1. ✅ **A. Utilize the "transforms" configuration to preprocess and filter records before they are sent to Kafka, reducing unnecessary data ingestion**  
   **Correct**. Applying Single Message Transformations (SMTs) via "transforms" helps reduce downstream processing load and improves pipeline efficiency.

2. ❌ **B. Avoid using schema registry integration to reduce connector complexity and improve performance**  
   **Incorrect**. Schema Registry integration ensures data compatibility and governance, and while it adds some overhead, it is critical for maintaining data quality.

3. ❌ **C. Disable "errors.tolerance" to fail fast on any data issue, ensuring data quality without retries or dead-letter queues**  
   **Incorrect**. Disabling error tolerance can cause the connector to stop on recoverable errors, reducing fault tolerance and availability.

4. ✅ **D. Increase the "tasks.max" configuration to enable parallelism and leverage multiple connector tasks for better throughput**  
   **Correct**. Increasing "tasks.max" allows multiple task instances to run in parallel, improving throughput by dividing the data ingestion workload.

5. ❌ **E. Set "offset.flush.timeout.ms" to a very high value to reduce the frequency of offset commits and minimize overhead**  
   **Incorrect**. `offset.flush.timeout.ms` is only the maximum time allowed for an offset flush to complete (default 5000 ms), the commit frequency is set by `offset.flush.interval.ms`. A very high timeout does not reduce commit overhead and only delays detection of a stuck flush.

6. ✅ **F. Configure "producer.batch.size" and "producer.linger.ms" to tune batching behavior, optimizing throughput and latency trade-offs**  
   **Correct**. These producer parameters control how records are batched before sending to Kafka, impacting throughput and latency.

</details>

## Question 47 (Kafka Producers):
When configuring serializers in a Kafka producer for a Confluent platform application, which of the following statements about serializers are correct?

- A. Using JsonSerializer automatically enforces schema validation against the Schema Registry before serialization.
- B. The StringSerializer converts a String into a byte array using UTF-8 encoding and is suitable for simple text data.
- C. The AvroSerializer requires schema registry configuration to serialize objects using Avro schemas, enabling schema evolution support.
- D. KafkaProducer requires both key.serializer and value.serializer properties to be set for proper serialization of message keys and values.
- E. Custom serializers must implement the org.apache.kafka.common.serialization.Serializer interface to be compatible with KafkaProducer.
- F. The ByteArraySerializer converts complex Java objects directly into byte arrays without additional configuration or schema requirements.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, C, D, E

**Explanation:**

In Kafka producers, serializers convert Java objects to byte arrays for transmission. StringSerializer is suitable for simple text, encoding strings as UTF-8. AvroSerializer integrates tightly with Confluent Schema Registry to manage Avro schemas and enable schema evolution. KafkaProducer requires both key.serializer and value.serializer to be explicitly set for correct operation. Custom serializers must implement the Serializer interface to be compatible. ByteArraySerializer does not serialize complex objects but rather passes byte arrays through. JsonSerializer serializes objects to JSON but does not enforce schema validation against Schema Registry by default, which can be a common misconception. Understanding these distinctions is critical for producing data correctly in Confluent Kafka environments. (The Confluent class is KafkaAvroSerializer, key.serializer/value.serializer have no defaults - alternatively serializer instances can be passed to the KafkaProducer constructor.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 "Serializers", https://kafka.apache.org/43/configuration/producer-configs/ , https://docs.confluent.io/platform/current/schema-registry/fundamentals/serdes-develop/

**Detailed explanation of each option:**

1. ❌ **A. Using JsonSerializer automatically enforces schema validation against the Schema Registry before serialization.**  
   **Incorrect**. JsonSerializer serializes Java objects to JSON format but does not enforce schema validation via Schema Registry by default, that functionality requires additional configuration or use of specific Confluent serializers.

2. ✅ **B. The StringSerializer converts a String into a byte array using UTF-8 encoding and is suitable for simple text data.**  
   **Correct**. StringSerializer is commonly used for serializing String keys or values by encoding them in UTF-8, which is standard and widely supported.

3. ✅ **C. The AvroSerializer requires schema registry configuration to serialize objects using Avro schemas, enabling schema evolution support.**  
   **Correct**. AvroSerializer depends on the Confluent Schema Registry to manage schemas and supports schema evolution, making it essential for Avro serialization in Confluent Kafka clients.

4. ✅ **D. KafkaProducer requires both key.serializer and value.serializer properties to be set for proper serialization of message keys and values.**  
   **Correct**. KafkaProducer mandates setting both key.serializer and value.serializer properties to correctly serialize keys and values before sending messages to Kafka topics.

5. ✅ **E. Custom serializers must implement the org.apache.kafka.common.serialization.Serializer interface to be compatible with KafkaProducer.**  
   **Correct**. To integrate custom serialization logic, the serializer must implement Kafka's Serializer interface to ensure compatibility and proper behavior within KafkaProducer.

6. ❌ **F. The ByteArraySerializer converts complex Java objects directly into byte arrays without additional configuration or schema requirements.**  
   **Incorrect**. ByteArraySerializer simply passes through byte arrays, it does not convert complex Java objects. Complex objects require explicit serialization to byte arrays before using ByteArraySerializer.

</details>

## Question 48 (Kafka Producers):
When configuring a Kafka producer for a high-throughput, low-latency application, which producer configuration property is most critical to tune in order to maximize batching efficiency without significantly increasing latency?

- A. linger.ms
- B. batch.size
- C. acks
- D. retries

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The 'linger.ms' configuration is key to tuning Kafka producer performance for high-throughput and low-latency applications. It defines the maximum time the producer will wait to fill up a batch before sending it to the broker. A higher 'linger.ms' allows more messages to accumulate, improving compression and throughput, but can increase latency. Conversely, a lower 'linger.ms' reduces latency but decreases batching efficiency. While 'batch.size' controls batch capacity, it does not govern the delay before sending. 'acks' and 'retries' impact message durability and reliability, but not batching or latency directly. Proper tuning of 'linger.ms' is essential for balancing throughput and latency in production scenarios.  answer A confirmed. batch.size also matters, but linger.ms is the knob that trades wait time for batching, docs: "The default changed from 0 to 5 in Apache Kafka 4.0 as the efficiency gains from larger batches typically result in similar or lower producer latency despite the increased linger."

Source: https://kafka.apache.org/42/configuration/producer-configs/ (linger.ms)

**Detailed explanation of each option:**

1. ✅ **A. linger.ms**  
   **Correct**. 'linger.ms' sets the maximum time the producer will wait to accumulate messages into a batch before sending. Increasing this value improves batching efficiency and throughput but can add latency, so tuning it balances throughput and latency.

2. ❌ **B. batch.size**  
   **Incorrect**. 'batch.size' sets the maximum size of a batch in bytes. While important for batching, it does not control the timing aspect that affects latency, 'linger.ms' controls how long to wait before sending a batch.

3. ❌ **C. acks**  
   **Incorrect**. 'acks' controls the durability guarantees of a message by specifying how many brokers must acknowledge the write. While important for reliability, it does not directly affect batching efficiency or latency.

4. ❌ **D. retries**  
   **Incorrect**. 'retries' configures how many times the producer will attempt to resend failed messages. It affects reliability but not batching behavior or latency directly.

</details>

## Question 49 (Kafka Core Concepts):
In Apache Kafka, when a producer sends a message without specifying a key, how does Kafka determine the partition to which the message is assigned?

- A. Kafka waits for the producer to specify a partition explicitly before assigning the message.
- B. Kafka uses a round-robin algorithm to distribute messages evenly across all partitions.
- C. Kafka defaults all messages without keys to the first partition of the topic.
- D. Kafka hashes the null key and assigns messages based on the hash result.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, partitioning is critical for load balancing and message ordering. When a producer does not specify a key, the default partitioner applies a round-robin algorithm to assign messages evenly across all partitions. This ensures balanced throughput and avoids bottlenecks. Assigning all keyless messages to a single partition would cause uneven load and potential performance degradation. Hashing is only used when a key is present, ensuring messages with the same key go to the same partition to preserve order. Producers can override this behavior by specifying a partition explicitly, but Kafka does not wait for that, it uses the default strategy automatically. Understanding this mechanism is essential for designing efficient Kafka producers and ensuring predictable message distribution. Precision: since Kafka 2.4 (KIP-480) keyless records use the "sticky" behaviour - the producer fills a batch for one partition, then switches to another - so the distribution is even over time but not strictly per-record round-robin. B remains the best of the options.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 "Partitions" (p. 68-69)

**Detailed explanation of each option:**

1. ❌ **A. Kafka waits for the producer to specify a partition explicitly before assigning the message.**  
   **Incorrect**. Kafka automatically assigns partitions using a partitioner if the producer does not specify one.

2. ✅ **B. Kafka uses a round-robin algorithm to distribute messages evenly across all partitions.**  
   **Correct**. When no key is provided, the default partitioner in Kafka assigns messages to partitions in a round-robin fashion to ensure even load distribution.

3. ❌ **C. Kafka defaults all messages without keys to the first partition of the topic.**  
   **Incorrect**. Assigning all keyless messages to the first partition would cause data skew and is not the default behavior.

4. ❌ **D. Kafka hashes the null key and assigns messages based on the hash result.**  
   **Incorrect**. Kafka does not hash null keys, hashing is only applied when a key is provided.

</details>

## Question 50 (Kafka Producers):
When sending a message using a Kafka producer in a Confluent Kafka environment, which of the following configurations or actions directly affect message delivery semantics and ordering guarantees?

- A. Enabling idempotence in the producer disables retries to avoid duplicate message delivery.
- B. Setting the 'acks' configuration to 'all' ensures that the leader broker waits for all in-sync replicas to acknowledge the message before considering it sent.
- C. Using a key-based partitioner (such as the default one, which hashes the key) sends messages with the same key to the same partition, preserving message ordering per key.
- D. Setting 'linger.ms' to a high value reduces latency by sending messages immediately without batching.
- E. Calling the producer's send() method synchronously using get() blocks the calling thread until the broker acknowledges the message, providing synchronous delivery confirmation.
- F. Configuring 'max.in.flight.requests.per.connection' to a value greater than 5 improves message ordering guarantees under retries.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

In Kafka producers, the 'acks' setting controls durability and delivery guarantees by defining how many broker acknowledgments are required. Setting it to 'all' provides the strongest guarantee. Consistent partitioning, either through default or custom partitioners, ensures ordering of messages with the same key by routing them to the same partition. Calling send() synchronously using get() forces the producer to wait for acknowledgment before proceeding, providing delivery confirmation at the cost of throughput. Idempotence enables safe retries rather than disabling them, while 'linger.ms' controls batching delay (higher values increase latency). Lastly, 'max.in.flight.requests.per.connection' affects ordering during retries, where higher values can introduce out-of-order messages. Understanding these configurations is essential to correctly implement desired delivery semantics and ordering in Confluent Certified Developer applications.  option C originally said "custom partitioner guarantees", which was false in general (a custom partitioner can route arbitrarily), so it was reworded to a key-based (default) partitioner, answer B, C, E confirmed, with idempotence enabled (default since 3.0) ordering is preserved for max.in.flight.requests.per.connection <= 5, and a value above 5 is rejected.

Source: https://kafka.apache.org/42/configuration/producer-configs/ (partitioner.class, enable.idempotence, acks)

**Detailed explanation of each option:**

1. ❌ **A. Enabling idempotence in the producer disables retries to avoid duplicate message delivery.**  
   **Incorrect**. Enabling idempotence actually allows safe retries to avoid duplicates, it does not disable retries.

2. ✅ **B. Setting the 'acks' configuration to 'all' ensures that the leader broker waits for all in-sync replicas to acknowledge the message before considering it sent.**  
   **Correct**. Setting 'acks' to 'all' provides the strongest delivery guarantee by waiting for all in-sync replicas, reducing the chance of message loss.

3. ✅ **C. Using a key-based partitioner (such as the default one, which hashes the key) sends messages with the same key to the same partition, preserving message ordering per key.**  
   **Correct**. Docs: "If no partition is specified but a key is present, choose a partition based on a hash of the key." Ordering per key holds as long as the partition count does not change.

4. ❌ **D. Setting 'linger.ms' to a high value reduces latency by sending messages immediately without batching.**  
   **Incorrect**. A high 'linger.ms' value increases batching delay to improve throughput but increases latency.

5. ✅ **E. Calling the producer's send() method synchronously using get() blocks the calling thread until the broker acknowledges the message, providing synchronous delivery confirmation.**  
   **Correct**. Using get() on the Future returned by send() blocks until the message is acknowledged, enabling synchronous confirmation.

6. ❌ **F. Configuring 'max.in.flight.requests.per.connection' to a value greater than 5 improves message ordering guarantees under retries.**  
   **Incorrect**. Increasing 'max.in.flight.requests.per.connection' beyond 5 can lead to out-of-order messages during retries, harming ordering guarantees.

</details>

## Question 51 (Kafka Producers):
When producing messages to Kafka, which of the following statements about how partitions are selected and managed by Kafka producers are true?

- A. Using a key in the producer record improves message ordering guarantees by ensuring ordering within the selected partition.
- B. The number of partitions cannot be changed after a topic is created without data loss, so the producer must handle partition count changes dynamically.
- C. Custom partitioners can be implemented by the developer to control partition selection beyond the default hashing.
- D. If no key is provided, the producer always sends messages to partition 0 by default.
- E. If a message key is provided, the producer uses a hash of the key to determine the partition, ensuring all messages with the same key go to the same partition.
- F. Kafka producers always ensure messages are evenly distributed across all partitions regardless of keys or custom partitioners to balance load.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, E

**Explanation:**

Kafka producers determine partition assignment primarily through the message key. When a key is provided, Kafka computes a hash of the key to consistently route messages to the same partition, preserving order for that key. If no key is provided, the producer uses a default partitioner that distributes messages evenly, often in a round-robin or sticky manner. Developers can implement custom partitioners to control partition selection logic beyond default hashing, allowing tailored distribution strategies. While the number of partitions can be increased dynamically without data loss, producers must be aware of partition count changes to avoid errors (adding partitions changes the key-to-partition mapping, and partitions can never be decreased). Understanding these mechanisms is crucial for optimizing message ordering guarantees and load distribution in Kafka producer implementations.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 "Partitions" (pp. 68-70), ch. 2 "Choosing Partitions", https://kafka.apache.org/43/design/design/#theproducer

**Detailed explanation of each option:**

1. ✅ **A. Using a key in the producer record improves message ordering guarantees by ensuring ordering within the selected partition.**  
   **Correct**. Keys ensure that all messages with the same key are routed to the same partition, preserving order for those keys.

2. ❌ **B. The number of partitions cannot be changed after a topic is created without data loss, so the producer must handle partition count changes dynamically.**  
   **Incorrect**. Kafka allows increasing the number of partitions in a topic dynamically without data loss, however, producers may need to be aware of the new partition count.

3. ✅ **C. Custom partitioners can be implemented by the developer to control partition selection beyond the default hashing.**  
   **Correct**. Kafka allows custom partitioners to be implemented, enabling advanced partitioning strategies based on message content or other criteria.

4. ❌ **D. If no key is provided, the producer always sends messages to partition 0 by default.**  
   **Incorrect**. When no key is provided, the producer uses a partitioner that usually distributes messages in a round-robin or sticky manner across all available partitions, rather than sending all to partition 0.

5. ✅ **E. If a message key is provided, the producer uses a hash of the key to determine the partition, ensuring all messages with the same key go to the same partition.**  
   **Correct**. Kafka producers hash the serialized key to select the partition, which guarantees message ordering per key within a partition.

6. ❌ **F. Kafka producers always ensure messages are evenly distributed across all partitions regardless of keys or custom partitioners to balance load.**  
   **Incorrect**. Producers distribute messages based on keys or partitioner logic, if keys are used, distribution may be skewed, and custom partitioners may purposely imbalance to meet application requirements.

</details>

## 🚫 Question 52 (Kafka Connect):
Which of the following statements about the JDBC Source Connector in Kafka Connect are true? Select all that apply.

- A. The connector can perform bulk loading only and does not support incremental updates or change data capture (CDC).
- B. The `table.whitelist` configuration allows the connector to limit which tables to poll from the database.
- C. The `query` configuration can be used to specify a custom SQL query instead of polling entire tables.
- D. The connector supports incremental queries using a timestamp or numeric column to avoid reading the entire table on each poll.
- E. The connector requires the Kafka Connect cluster to run in distributed mode to connect to JDBC sources.
- F. Setting the `auto.create` configuration to true allows the connector to automatically create Kafka topics if they do not exist.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

The JDBC Source Connector in Kafka Connect supports incremental loading using timestamp or numeric columns to efficiently capture new or updated data (D), allows limiting tables with `table.whitelist` (B, newer versions also `table.include.list`) and specifying a custom SQL query via `query` (C). Contrary to some misconceptions, `auto.create` is not a source option (F is incorrect), the connector supports more than bulk loading - incremental modes, though not log-based CDC (A is incorrect), and it can run in both standalone and distributed modes (E is incorrect). Understanding these capabilities is critical for configuring efficient and reliable data pipelines with Kafka Connect.

Source: https://docs.confluent.io/kafka-connectors/jdbc/current/source-connector/source_config_options.html , https://docs.confluent.io/kafka-connectors/jdbc/current/sink-connector/sink_config_options.html

**Detailed explanation of each option:**

1. ❌ **A. The connector can perform bulk loading only and does not support incremental updates or change data capture (CDC).**  
   **Incorrect**. While the connector supports bulk loading (`mode=bulk`), it also supports incremental modes (`incrementing`, `timestamp`, `timestamp+incrementing`). It is query-polling based, not true log-based CDC (that needs e.g. Debezium).

2. ✅ **B. The `table.whitelist` configuration allows the connector to limit which tables to poll from the database.**  
   **Correct**. Using `table.whitelist` restricts the connector to only poll specified tables, which is useful for filtering relevant data sources.

3. ✅ **C. The `query` configuration can be used to specify a custom SQL query instead of polling entire tables.**  
   **Correct**. The `query` option lets users define a custom SQL query for the connector to execute, which can be used for complex data retrieval scenarios.

4. ✅ **D. The connector supports incremental queries using a timestamp or numeric column to avoid reading the entire table on each poll.**  
   **Correct**. The JDBC Source Connector can perform incremental queries by specifying the `mode` as `incrementing` or `timestamp+incrementing`, using a column to track new or updated rows.

5. ❌ **E. The connector requires the Kafka Connect cluster to run in distributed mode to connect to JDBC sources.**  
   **Incorrect**. The JDBC Source Connector can run in either standalone or distributed mode, the choice depends on deployment needs, not connector capabilities.

6. ❌ **F. Setting the `auto.create` configuration to true allows the connector to automatically create Kafka topics if they do not exist.**  
   **Incorrect**. `auto.create` belongs to the JDBC *Sink* connector (creates the destination database table), it is not a source option and does not create Kafka topics (topic creation is governed by broker `auto.create.topics.enable` or Connect's topic.creation.* settings).

</details>

## Question 53 (Reliable Data Delivery):
Which configuration settings and practices should a Confluent Certified Developer apply to ensure reliable and efficient data delivery when using Kafka producers in a high-throughput, fault-tolerant environment?

- A. Set acks=all to ensure the leader and all in-sync replicas acknowledge the record before considering it committed.
- B. Increase linger.ms to buffer records before sending, improving throughput but potentially increasing latency.
- C. Set retries=0 to avoid duplicate messages by not retrying failed sends.
- D. Enable idempotence by setting enable.idempotence=true to prevent duplicate records during retries.
- E. Use compression.type=none to avoid additional processing overhead and ensure faster message delivery.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

To ensure reliable data delivery using Kafka producers, a developer should configure acks=all to wait for all in-sync replicas, which prevents data loss during broker failures. Enabling idempotence prevents duplicate records from being produced during retries, ensuring exactly-once delivery semantics. Adjusting linger.ms helps batch messages, improving throughput without sacrificing reliability, though it may increase latency. Setting retries=0 is detrimental to reliability as it disables retrying transient failures, increasing data loss risk. While compression reduces network load and can enhance throughput and reliability, setting compression.type=none sacrifices these benefits, making it an unfavorable choice in most reliability-focused scenarios. These configurations together balance throughput, latency, and fault tolerance in production Kafka use cases. Caveats: idempotence gives no duplicates per partition within a producer session (not end-to-end exactly-once), acks=all is only as durable as min.insync.replicas,  A, B, D confirmed. B (linger.ms) is about throughput, not reliability, so the stem was changed to "reliable and efficient" to make B legitimately correct, C (retries=0 contradicts idempotence, which requires retries > 0 and acks=all) and E are wrong. Docs: "When set to 'true', the producer will ensure that exactly one copy of each message is written in the stream."

Source: https://kafka.apache.org/42/configuration/producer-configs/ (enable.idempotence, linger.ms)

**Detailed explanation of each option:**

1. ✅ **A. Set acks=all to ensure the leader and all in-sync replicas acknowledge the record before considering it committed.**  
   **Correct**. Setting acks=all ensures the highest durability by waiting for all in-sync replicas to acknowledge, reducing the risk of data loss.

2. ✅ **B. Increase linger.ms to buffer records before sending, improving throughput but potentially increasing latency.**  
   **Correct**. Increasing linger.ms batches records to improve throughput, which can be balanced against latency requirements.

3. ❌ **C. Set retries=0 to avoid duplicate messages by not retrying failed sends.**  
   **Incorrect**. Setting retries=0 can lead to data loss during transient failures, retries should be enabled alongside idempotence.

4. ✅ **D. Enable idempotence by setting enable.idempotence=true to prevent duplicate records during retries.**  
   **Correct**. Enabling idempotence guarantees exactly-once delivery semantics from the producer side, preventing duplicates on retries.

5. ❌ **E. Use compression.type=none to avoid additional processing overhead and ensure faster message delivery.**  
   **Incorrect**. While no compression reduces CPU overhead, it increases network usage, compression helps throughput and can improve reliability under load.

</details>

## Question 54 (Kafka Core Concepts):
Which of the following statements about Kafka consumers and their behavior in a consumer group are TRUE?

- A. When a new consumer joins a group, a rebalance occurs that redistributes partitions among all consumers in the group.
- B. Each partition in a topic can be consumed by multiple consumers within the same consumer group simultaneously.
- C. Kafka consumers automatically handle offset resets by discarding messages if offsets are out of range.
- D. Kafka consumers track their read progress using offsets, which can be committed either automatically or manually.
- E. The consumer poll() method must be called frequently to avoid session timeouts and trigger rebalances.
- F. Consumer groups allow multiple consumers to read the same message independently without any coordination.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, E

**Explanation:**

Kafka consumers in a consumer group coordinate to ensure each partition is consumed by only one consumer instance, maintaining message order and avoiding duplicates. Offsets track consumption progress and can be committed automatically or manually based on application needs, which impacts fault tolerance and exactly-once semantics. When consumers join or leave a group, Kafka triggers a rebalance to redistribute partitions fairly. Frequent calls to poll() are essential to send heartbeats and avoid session timeouts that cause unnecessary rebalances. Misunderstandings often arise regarding partition sharing within groups and offset reset behaviors, knowing these details is critical for designing robust Kafka consumer applications. Correction: heartbeats are sent by a separate background thread (since KIP-62), so poll() does not send them, poll() must be called within max.poll.interval.ms, otherwise the consumer is removed from the group and a rebalance is triggered. (Option E's "session timeouts" wording is therefore loose, but it is still the best third answer, F describes multiple consumer *groups*, not one group.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (pp. 83-90: heartbeat thread, max.poll.interval.ms, rebalance), https://kafka.apache.org/43/configuration/consumer-configs/

**Detailed explanation of each option:**

1. ✅ **A. When a new consumer joins a group, a rebalance occurs that redistributes partitions among all consumers in the group.**  
   **Correct**. Adding or removing consumers triggers a rebalance in which Kafka reassigns partitions to consumers to evenly distribute the load.

2. ❌ **B. Each partition in a topic can be consumed by multiple consumers within the same consumer group simultaneously.**  
   **Incorrect**. Within a single consumer group, each partition is assigned to only one consumer at a time to guarantee message order and avoid duplicate processing.

3. ❌ **C. Kafka consumers automatically handle offset resets by discarding messages if offsets are out of range.**  
   **Incorrect**. Offset resets depend on the 'auto.offset.reset' configuration and may cause consumers to start reading from earliest or latest offsets, but they do not simply discard messages automatically.

4. ✅ **D. Kafka consumers track their read progress using offsets, which can be committed either automatically or manually.**  
   **Correct**. Consumers maintain offsets for each partition they consume, and offset commits can be configured to happen automatically or manually, affecting fault tolerance and processing guarantees.

5. ✅ **E. The consumer poll() method must be called frequently to avoid session timeouts and trigger rebalances.**  
   **Correct**. Regular calls to poll() (within max.poll.interval.ms) keep the consumer a live member of the group, heartbeats themselves are sent by a background thread (session.timeout.ms / heartbeat.interval.ms).

6. ❌ **F. Consumer groups allow multiple consumers to read the same message independently without any coordination.**  
   **Incorrect**. Consumer groups coordinate partition assignments so that each message is processed by only one consumer instance in the group, avoiding duplicate consumption.

</details>

## Question 55 (Kafka Consumers):
When implementing a standalone Kafka consumer using the KafkaConsumer API in a Confluent Kafka environment, which configuration or practice is essential to ensure the consumer does not lose messages and resumes from the last processed position after a restart (at-least-once processing)?

- A. Set 'enable.auto.commit' to true and rely on automatic offset commits.
- B. Disable 'enable.auto.commit' and manually commit offsets synchronously after processing each record batch.
- C. Set 'isolation.level' to 'read_uncommitted' to consume all messages including uncommitted transactions.
- D. Use 'auto.offset.reset' set to 'earliest' to always reprocess from the beginning on restart.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To get reliable at-least-once processing in a standalone Kafka consumer, it is essential to disable automatic offset commits and instead commit offsets manually only after messages have been successfully processed. This prevents the consumer from committing offsets prematurely, which can cause duplicates if the consumer crashes before processing completes. Using 'auto.offset.reset=earliest' does not guarantee exactly-once semantics, as it only controls where to start if no committed offset exists. Similarly, enabling 'enable.auto.commit' risks committing offsets before processing finishes. Finally, 'isolation.level' set to 'read_uncommitted' can expose uncommitted data, which is undesirable for exactly-once guarantees. Therefore, manual synchronous commits after processing are key for reliable standalone consumers. Re-verified: the original wording ("exactly once") was flawed - committing after processing gives at-least-once (a crash between processing and commit still produces duplicates), true exactly-once needs transactions (read_committed + sendOffsetsToTransaction) or storing results atomically with offsets (Kafka design doc, "Message Delivery Semantics"). The stem was reworded to at-least-once, answer B confirmed.

Source: https://kafka.apache.org/42/design/design/#message-delivery-semantics

**Detailed explanation of each option:**

1. ❌ **A. Set 'enable.auto.commit' to true and rely on automatic offset commits.**  
   **Incorrect**. 'enable.auto.commit' set to true causes offsets to be committed periodically in the background, which can lead to duplicate processing if the consumer crashes before the commit happens. Therefore, this does not guarantee exactly-once processing.

2. ✅ **B. Disable 'enable.auto.commit' and manually commit offsets synchronously after processing each record batch.**  
   **Correct**. Disabling automatic commits and committing offsets manually after processing ensures that offsets are only committed after successful processing, avoiding message loss on restart (at-least-once, duplicates remain possible).

3. ❌ **C. Set 'isolation.level' to 'read_uncommitted' to consume all messages including uncommitted transactions.**  
   **Incorrect**. 'isolation.level' set to 'read_uncommitted' allows reading uncommitted transactional messages, which can cause duplicates or inconsistent data. For exactly-once processing, 'read_committed' is preferred.

4. ❌ **D. Use 'auto.offset.reset' set to 'earliest' to always reprocess from the beginning on restart.**  
   **Incorrect**. 'auto.offset.reset' set to 'earliest' only applies when there are no committed offsets. It causes the consumer to start at the earliest offset, which can lead to reprocessing messages unnecessarily and does not ensure exactly-once processing.

</details>

## Question 56 (Stream Processing):
In the context of achieving Exactly-Once Semantics (EOS) in Kafka Streams applications, which of the following statements accurately describe the mechanisms or configurations that ensure EOS? Select THREE.

- A. Configuring 'processing.guarantee' to 'exactly_once' or 'exactly_once_beta' in Kafka Streams (in Kafka 4.x the valid value is 'exactly_once_v2').
- B. Setting the consumer isolation level to 'read_uncommitted' to maximize throughput.
- C. Relying solely on producer retries without transactions to handle message duplication.
- D. Enabling idempotent producers to prevent duplicate message writes to Kafka topics.
- E. Disabling Kafka Streams' internal state store changelog topics to reduce overhead.
- F. Using transactions to atomically commit both the processed output records and the consumer offsets.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

Exactly-Once Semantics in Kafka Streams is achieved through a combination of idempotent producers, transactional writes, and appropriate configuration settings. Enabling idempotent producers prevents duplicate messages during retries, while transactions ensure atomic commits of both output records and consumer offsets, avoiding partial processing. The 'processing.guarantee' config activates these features. Disabling changelog topics or setting isolation level to 'read_uncommitted' compromises fault tolerance or allows reading uncommitted data, violating EOS. Relying only on retries without transactions cannot ensure EOS because offsets and outputs might not be committed atomically. Therefore, the correct mechanisms involve idempotency, transactions, and Kafka Streams EOS configurations. Note: 'exactly_once' and 'exactly_once_beta' were deprecated in 3.0 and removed in 4.0, valid values are now at_least_once and exactly_once_v2 (the question text is dated, intent of A is still correct). The question originally said "Select TWO" but three answers are correct.

Source: https://kafka.apache.org/43/configuration/kafka-streams-configs/#streamsconfigs_processing.guarantee , Kafka: The Definitive Guide 2nd ed., ch. 14 (Kafka Streams exactly-once, p. ~392) and ch. 8 (transactions)

**Detailed explanation of each option:**

1. ✅ **A. Configuring 'processing.guarantee' to 'exactly_once' or 'exactly_once_beta' in Kafka Streams.**  
   **Correct**. This configuration enables EOS by activating internal mechanisms like idempotent producers and transactions.

2. ❌ **B. Setting the consumer isolation level to 'read_uncommitted' to maximize throughput.**  
   **Incorrect**. 'read_uncommitted' allows reading uncommitted data, which risks duplicates and violates EOS guarantees.

3. ❌ **C. Relying solely on producer retries without transactions to handle message duplication.**  
   **Incorrect**. Producer retries alone cannot guarantee EOS without transactions to atomically commit offsets and outputs.

4. ✅ **D. Enabling idempotent producers to prevent duplicate message writes to Kafka topics.**  
   **Correct**. Idempotent producers ensure that retries do not result in duplicate messages, which is fundamental to EOS.

5. ❌ **E. Disabling Kafka Streams' internal state store changelog topics to reduce overhead.**  
   **Incorrect**. Disabling changelog topics removes the fault-tolerance guarantees and breaks EOS by losing state recovery capability.

6. ✅ **F. Using transactions to atomically commit both the processed output records and the consumer offsets.**  
   **Correct**. Kafka transactions enable atomic writes of output data and offset commits, ensuring EOS.

</details>

## Question 57 (Kafka Ecosystem):
In Kafka Streams, which of the following statements correctly describes how state stores are managed and utilized to ensure fault tolerance and exactly-once processing semantics?

- A. State stores are kept only in-memory and rely on upstream Kafka topics for recovery, thus they do not require changelog topics.
- B. State stores are backed by local persistent storage and continuously backed up to a Kafka changelog topic to enable fault-tolerant recovery and exactly-once semantics.
- C. State stores do not participate in Kafka's transaction protocol and thus cannot support exactly-once semantics.
- D. State stores are replicated across multiple Kafka Streams instances by default to ensure high availability without needing changelog topics.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka Streams manages state stores by persisting them locally and continuously backing them up to Kafka changelog topics. This design allows fast local access during processing and enables fault-tolerant recovery by restoring state from changelog topics after failures. The changelog topics also participate in Kafka's transactional protocol, which allows Kafka Streams to offer exactly-once processing semantics. Common misconceptions include thinking state stores are purely in-memory or replicated across instances, but Kafka Streams relies on changelog topics for durability and recovery instead. Understanding this mechanism is critical for developing fault-tolerant stream processing applications with Kafka Streams. (Changelog topics are enabled by default, num.standby.replicas defaults to 0, so stores are not replicated across instances by default.)

Source: https://kafka.apache.org/43/documentation/streams/architecture/#streams_architecture_recovery , Kafka: The Definitive Guide 2nd ed., ch. 14 "Local state"/"Fault tolerance"

**Detailed explanation of each option:**

1. ❌ **A. State stores are kept only in-memory and rely on upstream Kafka topics for recovery, thus they do not require changelog topics.**  
   **Incorrect**. State stores in Kafka Streams are backed by persistent local storage and changelog topics to enable fault tolerance and recovery.

2. ✅ **B. State stores are backed by local persistent storage and continuously backed up to a Kafka changelog topic to enable fault-tolerant recovery and exactly-once semantics.**  
   **Correct**. Kafka Streams uses local persistent state stores and updates a changelog topic so state can be restored after failures, supporting fault tolerance and exactly-once processing.

3. ❌ **C. State stores do not participate in Kafka's transaction protocol and thus cannot support exactly-once semantics.**  
   **Incorrect**. State stores integrate with Kafka's transaction protocol via changelog topics to achieve exactly-once semantics.

4. ❌ **D. State stores are replicated across multiple Kafka Streams instances by default to ensure high availability without needing changelog topics.**  
   **Incorrect**. Kafka Streams does not replicate state stores across instances, instead, it uses changelog topics to restore state.

</details>

## Question 58 (Kafka Setup and Operations):
When selecting hardware for a Kafka broker in a high-throughput production environment, which factor is the most critical to ensure optimal broker performance and data durability?

- A. Selecting network cards with the highest possible bandwidth, such as 100 Gbps, regardless of cluster size
- B. Choosing the highest number of CPU cores regardless of clock speed
- C. Maximizing RAM above 1 TB to cache all Kafka messages in memory
- D. Using SSD storage instead of HDD to reduce disk latency and improve I/O throughput

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka broker hardware selection, SSD storage is the most critical factor due to Kafka’s heavy reliance on disk I/O for log segment writes and reads. SSDs drastically reduce latency and increase throughput compared to traditional HDDs, enhancing overall broker performance and durability. While CPU cores and RAM are important, their benefits have diminishing returns beyond certain thresholds. Over-provisioning RAM to cache all data is unrealistic since Kafka is designed for disk-based storage with OS page caching. Network bandwidth should be balanced according to the cluster’s actual data transfer needs rather than over-specification. Understanding these trade-offs is essential for optimizing Kafka deployments in production environments. (Outside CCDAK scope: hardware sizing/administration. Per the book, disk throughput is the main factor for producer performance and memory/page cache for consumer performance, SSD vs HDD is the best option here.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 2 "Selecting Hardware" (Disk Throughput, Disk Capacity, Memory, Networking, CPU)

**Detailed explanation of each option:**

1. ❌ **A. Selecting network cards with the highest possible bandwidth, such as 100 Gbps, regardless of cluster size**  
   **Incorrect**. : High bandwidth network cards can be beneficial but are not always cost-effective or necessary depending on cluster scale and workload. Network throughput should match actual data flow requirements.

2. ❌ **B. Choosing the highest number of CPU cores regardless of clock speed**  
   **Incorrect**. : While CPU cores are important for handling multiple partitions and threads, clock speed and core efficiency also matter. Simply having the most cores without sufficient clock speed or balanced resources may not yield the best performance.

3. ❌ **C. Maximizing RAM above 1 TB to cache all Kafka messages in memory**  
   **Incorrect**. : While having sufficient RAM (e.g., 64GB-256GB) improves caching and page cache efficiency, caching all messages in RAM is impractical and unnecessary since Kafka relies on disk storage for durability.

4. ✅ **D. Using SSD storage instead of HDD to reduce disk latency and improve I/O throughput**  
   **Correct**. : SSDs provide significantly lower latency and higher I/O operations per second compared to HDDs, directly improving Kafka’s log write and read performance, which is critical for high-throughput scenarios.

</details>

## Question 59 (Kafka Internals):
Which of the following statements accurately describe how log compaction works in Apache Kafka and its implications for topic data retention?

- A. Compacted topics are suitable for use cases requiring a changelog of all data changes over time without data loss.
- B. Log compaction guarantees that the latest record for each key is retained, regardless of the record's age.
- C. The compaction process runs continuously in the background and does not block producers or consumers.
- D. Log compaction can run concurrently with standard time or size-based retention policies on the same topic.
- E. During compaction, Kafka guarantees that all intermediate updates for a key are retained in the log.
- F. Compacted topics delete messages only based on their age, similar to log retention by time.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

Log compaction in Kafka ensures that the latest value for each key is preserved, making it ideal for topics representing state or snapshots. It differs fundamentally from time- or size-based retention, which removes data solely based on age or log size. Compaction runs as an asynchronous background process and can coexist with other retention policies, allowing flexibility in managing topic data. However, compaction does not retain all historical updates for a key, so it is unsuitable for use cases requiring a complete changelog of all changes. Understanding these nuances is critical for developers designing Kafka topics to meet specific data retention and recovery requirements. (B holds for cleanup.policy=compact, tombstones are removed after delete.retention.ms, and with cleanup.policy=compact,delete records older than retention are deleted too. The active segment is not compacted.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Compaction"/"How Compaction Works"/"Deleted Events", https://kafka.apache.org/43/configuration/topic-configs/#topicconfigs_cleanup.policy

**Detailed explanation of each option:**

1. ❌ **A. Compacted topics are suitable for use cases requiring a changelog of all data changes over time without data loss.**  
   **Incorrect**. Since compaction discards older versions of a key, it is not ideal for changelog use cases that need a full history of changes.

2. ✅ **B. Log compaction guarantees that the latest record for each key is retained, regardless of the record's age.**  
   **Correct**. Log compaction ensures that at least the most recent value for each key is kept in the log, providing a snapshot of the latest state.

3. ✅ **C. The compaction process runs continuously in the background and does not block producers or consumers.**  
   **Correct**. Compaction is an asynchronous background process that does not interfere with producers or consumers, ensuring minimal impact on performance.

4. ✅ **D. Log compaction can run concurrently with standard time or size-based retention policies on the same topic.**  
   **Correct**. Kafka allows both compaction and time/size retention to coexist, compaction preserves latest key updates, while retention deletes old data beyond configured thresholds.

5. ❌ **E. During compaction, Kafka guarantees that all intermediate updates for a key are retained in the log.**  
   **Incorrect**. Compaction removes intermediate updates, keeping only the latest value per key, so intermediate states are typically discarded.

6. ❌ **F. Compacted topics delete messages only based on their age, similar to log retention by time.**  
   **Incorrect**. Unlike time-based retention, compaction removes older duplicates of keys but does not delete records solely based on age.

</details>

## Question 60 (Kafka Consumers):
Which of the following statements about commits and offsets in Kafka consumers are correct? Select all that apply.

- A. Offsets are stored only in ZooKeeper and never in Kafka topics.
- B. Each consumer in a group keeps its own private committed offsets locally, invisible to the other members of the group.
- C. A consumer can commit offsets synchronously or asynchronously, with synchronous commits providing stronger delivery guarantees at the cost of higher latency.
- D. Offsets can be committed automatically by enabling `enable.auto.commit`, which commits at periodic intervals defined by `auto.commit.interval.ms`.
- E. Kafka automatically commits offsets when a message is received by the consumer's poll method.
- F. When using manual offset commits, failing to commit offsets after processing can cause message reprocessing after consumer restart.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, F

**Explanation:**

In Kafka consumer offset management, enabling `enable.auto.commit` allows automatic periodic commits, but manual commits provide finer control. Synchronous commits offer stronger guarantees at the cost of blocking, whereas asynchronous commits are faster but less reliable. Offsets have been stored in Kafka's internal __consumer_offsets topic since Kafka 0.9, replacing ZooKeeper storage. Manual offset commits require careful management to avoid duplicate processing after consumer restarts. Offsets track progress per consumer group and partition, not shared among consumers directly. Kafka does not commit offsets upon polling messages, ensuring that only processed messages are committed. Understanding these nuances is essential for developing robust Kafka consumer applications. (Re-verified: option B was originally "offsets are shared among all consumers ... coordinate", which was ambiguous (loosely true), so it was reworded to an unambiguously false statement, C, D, F confirmed. With auto-commit, poll() commits the previous poll's offsets once auto.commit.interval.ms has elapsed - not on every poll.)

Source: https://kafka.apache.org/42/configuration/consumer-configs/ (enable.auto.commit, auto.commit.interval.ms) , https://kafka.apache.org/42/design/design/#consumer-position

**Detailed explanation of each option:**

1. ❌ **A. Offsets are stored only in ZooKeeper and never in Kafka topics.**  
   **Incorrect**. Since Kafka 0.9, offsets are stored in an internal Kafka topic (__consumer_offsets), not in ZooKeeper, which improves scalability and reliability.

2. ❌ **B. Each consumer in a group keeps its own private committed offsets locally, invisible to the other members of the group.**  
   **Incorrect**. Committed offsets are stored on the broker (in __consumer_offsets) per group, topic and partition, so after a rebalance the new partition owner resumes from them.

3. ✅ **C. A consumer can commit offsets synchronously or asynchronously, with synchronous commits providing stronger delivery guarantees at the cost of higher latency.**  
   **Correct**. Synchronous commits block until the broker acknowledges the commit, ensuring the offset is stored before proceeding, which enhances delivery guarantees but may introduce latency.

4. ✅ **D. Offsets can be committed automatically by enabling `enable.auto.commit`, which commits at periodic intervals defined by `auto.commit.interval.ms`.**  
   **Correct**. Enabling `enable.auto.commit` allows Kafka consumers to commit offsets automatically at intervals specified by `auto.commit.interval.ms`, simplifying offset management but potentially risking duplicate processing.

5. ❌ **E. Kafka automatically commits offsets when a message is received by the consumer's poll method.**  
   **Incorrect**. Kafka does not commit offsets simply upon polling messages. Offsets are committed either automatically based on configuration or manually by the consumer after processing.

6. ✅ **F. When using manual offset commits, failing to commit offsets after processing can cause message reprocessing after consumer restart.**  
   **Correct**. Without committing processed offsets, the consumer will reset to the last committed offset on restart, causing messages to be reprocessed, which may or may not be desirable.

</details>
