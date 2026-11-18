> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1 (Kafka Setup and Operations):
Which statements about consumer lag as a performance/observability/definition signal are correct?

- A. Lag of zero always means the system is unhealthy.
- B. Consumer lag is the difference between a partition's log-end offset and the consumer group's committed (or current) offset.
- C. Lag can be inspected with `kafka-consumer-groups --describe` and is also exposed as the client metric `records-lag-max`.
- D. Lag can only ever be measured in seconds, never in number of records.
- E. Steadily growing lag indicates consumers are falling behind producers and may need to scale out or speed up processing.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, C

**Explanation:**

Consumer lag measures how far behind a consumer group is: for each partition it is the log-end (latest) offset minus the group's committed/current offset — i.e. the number of records produced but not yet consumed. Lag that grows steadily over time is a classic warning that consumers cannot keep up with the produce rate, pointing to a need for more consumers (up to the partition count), faster processing, or more partitions. You can observe lag operationally with `kafka-consumer-groups --describe` (CURRENT-OFFSET, LOG-END-OFFSET, LAG columns) and programmatically via the consumer client metric `records-lag-max`. Statement A is false — zero or low, stable lag is the *healthy* state. Statement D is false — lag is fundamentally a count of records (a record offset difference), though some tooling also estimates a time-based lag, it is not "only in seconds."

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 & Ch. 13 (Consumer lag, monitoring), `LAST_MINUTE_REVIEW.md` (records-lag-max), https://kafka.apache.org/documentation/#monitoring

**Detailed explanation of each option:**

1. ❌ **A. Zero lag means unhealthy.**  
   **Incorrect**. Low/zero stable lag is healthy.

2. ✅ **B. Lag = log-end offset − committed/current offset.**  
   **Correct**. The definition of lag.

3. ✅ **C. Visible via `kafka-consumer-groups` and `records-lag-max`.**  
   **Correct**. Both operational and client-metric views.

4. ❌ **D. Lag only in seconds.**  
   **Incorrect**. Lag is primarily a record count.

5. ✅ **E. Growing lag = consumers falling behind.**  
   **Correct**. Signals a need to scale/speed up.

</details>

## Question 2 (Kafka Setup and Operations):
Which statements about running and operating a Kafka cluster are correct for modern Kafka (4.x)?

- A. Increasing the number of partitions for an existing topic is impossible.
- B. Controller responsibilities (metadata management, leader election) are handled by KRaft controller nodes.
- C. Kafka 4.x runs in KRaft mode, ZooKeeper has been removed.
- D. `min.insync.replicas` together with `acks=all` controls how many replicas must acknowledge a write for it to succeed.
- E. The replication factor of a topic can never be changed after the topic is created.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, B, D

**Explanation:**

Modern Kafka (4.x) runs exclusively in KRaft mode, and ZooKeeper has been removed, cluster metadata and controller duties such as leader election are managed by dedicated KRaft controller nodes. Durability is tuned by combining `acks=all` on the producer with the topic/broker `min.insync.replicas` setting, which defines how many in-sync replicas must acknowledge a write. Topic replication factor can in fact be changed after creation using partition reassignment tooling, and partitions can be increased for an existing topic (though not decreased), so the statements claiming these are impossible are incorrect.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 (Reliability: acks, min.insync.replicas) and Ch. 7 (Administering), KRaft per Kafka 4.x release notes, https://kafka.apache.org/documentation/#kraft

**Detailed explanation of each option:**

1. ❌ **A. Increasing the number of partitions for an existing topic is impossible.**  
   **Incorrect**. Partitions can be increased (but not decreased).

2. ✅ **B. Controller responsibilities (metadata management, leader election) are handled by KRaft controller nodes.**  
   **Correct**. KRaft controllers own metadata and leader election.

3. ✅ **C. Kafka 4.x runs in KRaft mode, ZooKeeper has been removed.**  
   **Correct**. ZooKeeper was removed in Kafka 4.0, KRaft is the only mode.

4. ✅ **D. `min.insync.replicas` together with `acks=all` controls how many replicas must acknowledge a write for it to succeed.**  
   **Correct**. These together define durability guarantees.

5. ❌ **E. The replication factor of a topic can never be changed after the topic is created.**  
   **Incorrect**. Replication factor can be changed via partition reassignment.

</details>

## Question 3 (Kafka Setup and Operations):
Which statements about horizontally and vertically scaling a Kafka deployment are correct?

- A. A consumer group's effective parallelism can exceed the number of partitions if you add enough consumers.
- B. Horizontal scaling adds more brokers to the cluster so partitions and load can be spread across more machines.
- C. Increasing a topic's partition count raises the achievable consumer parallelism for a consumer group.
- D. Adding brokers automatically moves existing partition replicas onto the new brokers with no reassignment step.
- E. Vertical scaling means giving existing brokers more CPU, memory, or faster/larger disks.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

Scaling Kafka comes in two directions. Horizontal scaling adds broker nodes so partitions, storage, and client load can be distributed across more machines — the primary way Kafka grows. Because a partition is consumed by at most one consumer per group, increasing a topic's partition count raises the ceiling on consumer-group parallelism (more partitions → more consumers can work in parallel). Vertical scaling means strengthening existing brokers with more CPU, RAM, or faster/larger disks. Statement D is false: adding brokers does **not** automatically rebalance existing partitions onto them — you must run a partition reassignment (`kafka-reassign-partitions`) to move replicas to the new brokers. Statement A is false because consumer parallelism is capped by the partition count, extra consumers beyond that number sit idle.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 & Ch. 12 (Sizing, scaling, reassignment), https://kafka.apache.org/documentation/#hwandos

**Detailed explanation of each option:**

1. ❌ **A. Parallelism can exceed partition count.**  
   **Incorrect**. Extra consumers beyond partitions are idle.

2. ✅ **B. Horizontal scaling adds brokers to spread load.**  
   **Correct**. Scale-out by adding nodes.

3. ✅ **C. More partitions raise consumer-group parallelism.**  
   **Correct**. Parallelism ceiling is the partition count.

4. ❌ **D. New brokers auto-rebalance existing partitions.**  
   **Incorrect**. Reassignment is a manual/admin step.

5. ✅ **E. Vertical scaling = more CPU/RAM/disk per broker.**  
   **Correct**. Scale-up of existing nodes.

</details>

## Question 4 (Kafka Connect):
Which statements about using the Kafka Connect REST interface are correct?

- A. `POST /connectors` with a JSON body creates a new connector, `PUT /connectors/{name}/config` creates or updates one.
- B. `DELETE /connectors/{name}` removes a connector, and `POST /connectors/{name}/restart` restarts it.
- C. `GET /connectors/{name}/status` returns the connector's and tasks' state (RUNNING, FAILED, PAUSED) for monitoring.
- D. `GET /connectors` lists the connectors currently running on the Connect cluster.
- E. The REST interface is read-only and cannot be used to create or delete connectors.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, A, C, B

**Explanation:**

Kafka Connect is managed almost entirely through its REST API, which is the standard interface for both operations and automation. `GET /connectors` lists the active connectors. `POST /connectors` (with `{ "name": ..., "config": {...} }`) creates a connector, while `PUT /connectors/{name}/config` is the idempotent create-or-update call often used in CI/CD. `GET /connectors/{name}/status` reports the state of the connector and each task — RUNNING, PAUSED, FAILED (with trace) — which is how you monitor and detect failed tasks. Lifecycle operations include `DELETE /connectors/{name}` to remove a connector and `POST /connectors/{name}/restart` (plus task-level `restart`) to recover failed tasks, along with `pause`/`resume`. Statement E is simply wrong — the REST interface is fully read/write and is the primary way to create, configure, and delete connectors.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Connect REST API), https://kafka.apache.org/documentation/#connect_rest

**Detailed explanation of each option:**

1. ✅ **A. `POST /connectors` creates, `PUT .../config` creates/updates.**  
   **Correct**. Both creation paths.

2. ✅ **B. `DELETE` removes, `POST .../restart` restarts.**  
   **Correct**. Lifecycle operations.

3. ✅ **C. `GET .../status` returns connector/task state.**  
   **Correct**. Used for monitoring.

4. ✅ **D. `GET /connectors` lists connectors.**  
   **Correct**. Standard listing endpoint.

5. ❌ **E. REST interface is read-only.**  
   **Incorrect**. It is the main read/write management API.

</details>

## Question 5 (Kafka Connect):
Which statements about Connect scalability and offsets are correct?

- A. A sink connector's consumption progress is tracked using Kafka consumer group offsets, like any other consumer.
- B. Source connector offsets are stored in an internal Connect offsets topic so a restarted connector resumes where it left off.
- C. The only way to scale Connect is to vertically scale a single worker, it cannot run distributed.
- D. Scaling out is achieved by increasing `tasks.max` so the connector's work is split across more tasks (up to the number of input partitions for a sink).
- E. Adding more worker nodes to a distributed Connect cluster lets tasks be spread across more machines.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, E, A, B

**Explanation:**

Kafka Connect scales both ways. Within a connector, raising `tasks.max` divides the work into more tasks, for a sink connector, useful parallelism is bounded by the number of partitions in the input topics (a partition is consumed by one task). Across the cluster, adding worker nodes in distributed mode lets the framework rebalance connectors and tasks onto more machines — horizontal scaling. Offset handling differs by connector direction: a **sink** connector is effectively a consumer group, so its progress is tracked via normal Kafka consumer offsets in `__consumer_offsets`, a **source** connector has no upstream Kafka offsets, so Connect persists its source offsets (positions in the external system) in an internal Connect offsets topic, allowing a restarted source connector to resume. Statement C is false — Connect's signature strength is distributed mode, not single-worker-only.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Connect — scaling, offsets, distributed mode), https://kafka.apache.org/documentation/#connect_running

**Detailed explanation of each option:**

1. ✅ **A. Sink progress tracked via consumer offsets.**  
   **Correct**. A sink is a consumer group under the hood.

2. ✅ **B. Source offsets in the internal Connect offsets topic.**  
   **Correct**. Enables source connectors to resume.

3. ❌ **C. Connect can only vertically scale a single worker.**  
   **Incorrect**. Distributed mode is the standard way to scale out.

4. ✅ **D. Increase `tasks.max` to split work (bounded by partitions for sinks).**  
   **Correct**. Primary intra-connector scaling lever.

5. ✅ **E. Add workers to spread tasks across machines.**  
   **Correct**. Horizontal scaling in distributed mode.

</details>

## Question 6 (Kafka Internals):
Which statements about log compaction configuration and behavior are correct?

- A. Compaction guarantees that duplicate keys are removed instantly on every produce.
- B. Compaction operates on the inactive (already-rolled) segments, not the active segment being written.
- C. `cleanup.policy=compact,delete` applies both compaction and time/size-based retention.
- D. A topic uses compaction when `cleanup.policy` includes `compact`.
- E. A null value does not delete a key under compaction, it is retained forever as a normal record.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, C, B

**Explanation:**

Compaction is enabled when `cleanup.policy` contains `compact`. You can combine policies with `cleanup.policy=compact,delete`, which applies both key-based compaction and traditional time/size-based retention, useful for changelogs that should also age out. The log cleaner works on closed (inactive) segments, it does not compact the active segment currently receiving writes, so recently produced duplicate keys are not removed instantly—compaction happens asynchronously in the background. A null value is a tombstone that marks a key for deletion, not a normally retained record, so the statement claiming null values are retained forever is wrong.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Cleaning the Log", https://kafka.apache.org/documentation/#design_compaction

**Detailed explanation of each option:**

1. ❌ **A. Compaction guarantees that duplicate keys are removed instantly on every produce.**  
   **Incorrect**. Compaction is asynchronous and works on inactive segments.

2. ✅ **B. Compaction operates on the inactive (already-rolled) segments, not the active segment being written.**  
   **Correct**. The log cleaner processes closed segments only.

3. ✅ **C. `cleanup.policy=compact,delete` applies both compaction and time/size-based retention.**  
   **Correct**. Both policies can be combined on one topic.

4. ✅ **D. A topic uses compaction when `cleanup.policy` includes `compact`.**  
   **Correct**. The `compact` policy enables log compaction.

5. ❌ **E. A null value does not delete a key under compaction, it is retained forever as a normal record.**  
   **Incorrect**. A null value is a tombstone that deletes the key.

</details>

## Question 7 (Kafka Setup and Operations):
Which statements about commonly-identified Kafka producer configurations are correct?

- A. `enable.idempotence=true` prevents duplicate records from producer retries by using producer IDs and sequence numbers.
- B. Increasing `acks` from `1` to `all` reduces durability because fewer replicas confirm the write.
- C. `linger.ms` and `batch.size` tune batching: larger values improve throughput at the cost of some latency.
- D. `acks=all` with a suitable `min.insync.replicas` maximizes durability by requiring all in-sync replicas to acknowledge.
- E. `compression.type` (e.g. `snappy`, `lz4`, `zstd`) reduces network and storage usage at some CPU cost.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, A, C, E

**Explanation:**

These are the producer knobs most commonly tested. `acks=all` requires every in-sync replica to acknowledge a write, combined with `min.insync.replicas` (which enforces a minimum ISR count or the produce fails), it gives the strongest durability. `enable.idempotence=true` makes the producer deduplicate retried records using a producer ID plus per-partition sequence numbers, preventing duplicates from retries (and it's the foundation for exactly-once). `linger.ms` (how long to wait to fill a batch) and `batch.size` (max batch bytes) control batching — larger values boost throughput and compression efficiency while adding a little latency. `compression.type` (`gzip`, `snappy`, `lz4`, `zstd`) trades CPU for smaller payloads on the network and on disk. Statement B inverts reality: going from `acks=1` to `acks=all` *increases* durability because more replicas must confirm the write before it's acknowledged.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 & Ch. 7 (Producer configuration, reliability), https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ✅ **A. `enable.idempotence=true` dedups retries.**  
   **Correct**. Producer ID + sequence numbers.

2. ❌ **B. `acks=all` reduces durability.**  
   **Incorrect**. It increases durability.

3. ✅ **C. `linger.ms`/`batch.size` trade latency for throughput.**  
   **Correct**. The batching knobs.

4. ✅ **D. `acks=all` + `min.insync.replicas` maximizes durability.**  
   **Correct**. Strongest write-durability setting.

5. ✅ **E. `compression.type` saves network/disk at CPU cost.**  
   **Correct**. Standard compression trade-off.

</details>

## Question 8 (Kafka Core Concepts):
Which statements correctly describe the Kafka resource hierarchy and how it is referenced for configuration and authorization?

- A. A topic is composed of one or more partitions, and each partition is an ordered, immutable append-only log.
- B. Each partition is replicated across brokers, one replica is the leader and the others are followers.
- C. ACLs can be defined on resource types such as Topic, Group, Cluster, and TransactionalId.
- D. A consumer group is a cluster-wide resource identified by its `group.id`.
- E. Partitions can be decreased as easily as they can be increased.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, B, C, D

**Explanation:**

Kafka's resource hierarchy nests as cluster → topics → partitions → records. A topic is a logical stream divided into one or more partitions, and each partition is an ordered, immutable, append-only log with its own offsets. Each partition is replicated across brokers for fault tolerance, exactly one replica acts as the leader (handling reads and writes) while the others are followers that replicate it. This hierarchy is also the basis for authorization: ACLs are defined per resource type — Topic, Group (consumer groups, identified by `group.id`), Cluster, TransactionalId, and more — with operations like Read, Write, and Describe. The one false statement is E: partition count can be *increased* but never decreased, which is a key "modifying topics" caveat (and increasing partitions can change key-to-partition mapping for future records).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 & Ch. 11 (Topics/partitions, Authorization resources), https://kafka.apache.org/documentation/#security_authz

**Detailed explanation of each option:**

1. ✅ **A. Topic → partitions, partition is an append-only log.**  
   **Correct**. Core topic/partition structure.

2. ✅ **B. Partitions replicated, one leader, others followers.**  
   **Correct**. Leader/follower replication model.

3. ✅ **C. ACLs on Topic, Group, Cluster, TransactionalId.**  
   **Correct**. These are real authorizable resource types.

4. ✅ **D. Consumer group identified by `group.id`.**  
   **Correct**. Groups are a first-class resource.

5. ❌ **E. Partitions can be decreased as easily as increased.**  
   **Incorrect**. Partition count can only be increased, never reduced.

</details>

## Question 9 (Programming & Serialization):
A team needs to be able to upgrade producers and consumers in any order without coordination. Which Schema Registry compatibility mode should they choose, and what does it permit?

- A. `NONE`, because it performs no checks and therefore guarantees compatibility.
- B. `FULL`, which is both backward and forward compatible and permits only adding or removing fields that have default values.
- C. `FORWARD`, which alone lets you upgrade in any order.
- D. `BACKWARD`, which alone lets you upgrade in any order.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

`FULL` compatibility enforces both BACKWARD and FORWARD guarantees simultaneously, so data remains readable regardless of whether the producer or consumer is upgraded first. Because it must satisfy both directions, the only safe structural changes are adding or removing fields that have default values. `BACKWARD` alone requires upgrading consumers first, and `FORWARD` alone requires upgrading producers first, so neither permits arbitrary upgrade order. `NONE` disables checks entirely, which removes protection rather than guaranteeing compatibility, making it unsafe for uncoordinated upgrades.

Source: `9.schema-registry/schema-registry-summary.md` (Schema Compatibility: FULL, upgrade order), Kafka: The Definitive Guide 2nd ed. Ch. 3

**Detailed explanation of each option:**

1. ❌ **A. `NONE`, because it performs no checks and therefore guarantees compatibility.**  
   **Incorrect**. NONE disables checks, removing protection rather than guaranteeing compatibility.

2. ✅ **B. `FULL`, which is both backward and forward compatible and permits only adding or removing fields that have default values.**  
   **Correct**. FULL allows upgrades in any order and restricts changes to add/remove fields with defaults.

3. ❌ **C. `FORWARD`, which alone lets you upgrade in any order.**  
   **Incorrect**. FORWARD requires upgrading producers first.

4. ❌ **D. `BACKWARD`, which alone lets you upgrade in any order.**  
   **Incorrect**. BACKWARD requires upgrading consumers first.

</details>

## Question 10 (Kafka Setup and Operations):
Which statements about the `kafka-transactions` (`kafka-transactions.sh`) CLI tool are correct?

- A. `kafka-transactions describe --transactional-id my-txn-id` shows the state of a specific transactional producer's transaction.
- B. Transactions are a client-side concern that no broker-side tooling can inspect.
- C. It is the tool used to enable idempotence on a producer.
- D. `kafka-transactions --list` lists the current transactions known to the cluster.
- E. It can `--find-hanging` and `--abort` a hanging/long-running transaction that is blocking consumers reading with `read_committed`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, A, E

**Explanation:**

`kafka-transactions` is an administrative tool for inspecting and repairing Kafka's transaction state. `--list` enumerates the transactions/transactional IDs tracked by the cluster, and `describe --transactional-id <id>` reports the current state (producer id/epoch, status, timeouts) of a given transactional producer. Its most operationally important capability is `--find-hanging` to locate hanging transactions and `--abort` to forcibly abort one — critical because a stuck open transaction blocks the last-stable-offset and prevents `read_committed` consumers from advancing past it. Statement C is false: idempotence is enabled by the producer config `enable.idempotence=true`, not by this CLI. Statement B is false: transactions are coordinated by the broker-side transaction coordinator and persisted in the internal `__transaction_state` topic, so broker-side tools like `kafka-transactions` can absolutely inspect and manage them.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 (Transactions), KIP-664 (`kafka-transactions` tool), https://kafka.apache.org/documentation/#transactions

**Detailed explanation of each option:**

1. ✅ **A. `describe --transactional-id` shows a transaction's state.**  
   **Correct**. Per-transaction inspection.

2. ❌ **B. No broker-side tool can inspect transactions.**  
   **Incorrect**. The coordinator/`__transaction_state` make them inspectable.

3. ❌ **C. Enables idempotence on a producer.**  
   **Incorrect**. That is `enable.idempotence=true`, a producer config.

4. ✅ **D. `--list` lists current transactions.**  
   **Correct**. Enumerates transactional IDs/transactions.

5. ✅ **E. `--find-hanging` / `--abort` clears hanging transactions.**  
   **Correct**. Unblocks `read_committed` consumers.

</details>

## Question 11 (Kafka Producers):
Which statements correctly describe how Kafka record headers are structured, encoded, and allowed to be used?

- A. Setting a header automatically changes the record's partition assignment.
- B. Each header is a key that is a string plus a value that is a raw `byte[]` (which may be null), the application is responsible for encoding/decoding the value bytes.
- C. A record may have zero, one, or many headers, and duplicate header keys are allowed (headers are an ordered list, not a map).
- D. Header values must be UTF-8 strings, Kafka rejects any non-string header value.
- E. Headers are part of the record and are preserved as the record is replicated and retained, and they are available to consumers, interceptors, and Connect SMTs.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

A Kafka header is a simple pair: a **string key** and a **`byte[]` value**. Kafka does not interpret the value — it is opaque bytes (and may even be null), so encoding and decoding (e.g. UTF-8 text, a number, JSON) is entirely the application's responsibility. Headers are represented as an **ordered list**, not a map, so a record can carry zero, one, or many headers and the **same key may appear more than once** (useful for multi-valued metadata), `Headers.lastHeader(key)` returns the last one for a key while `headers(key)` iterates all of them. Headers are a genuine part of the record: they are stored inline, replicated, and retained with the message, and they are readable by consumers, producer/consumer interceptors, and Kafka Connect Single Message Transforms. Statement D is false because values are arbitrary bytes, not required to be UTF-8 strings. Statement A is false because partitioning is driven by the key/partitioner, not by headers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (Headers), `org.apache.kafka.common.header.Header`/`Headers`, https://kafka.apache.org/documentation/#recordheader

**Detailed explanation of each option:**

1. ❌ **A. Setting a header changes the partition.**  
   **Incorrect**. Partitioning depends on the key/partitioner, not headers.

2. ✅ **B. String key + `byte[]` value (possibly null), app encodes/decodes.**  
   **Correct**. Kafka treats the value as opaque bytes.

3. ✅ **C. Zero/one/many headers, duplicate keys allowed (ordered list).**  
   **Correct**. Headers are a list, so keys can repeat.

4. ❌ **D. Values must be UTF-8 strings.**  
   **Incorrect**. Values are arbitrary bytes, any encoding is the app's choice.

5. ✅ **E. Preserved through replication/retention, available to consumers, interceptors, SMTs.**  
   **Correct**. Headers travel with the record end to end.

</details>

## Question 12 (Kafka Setup and Operations):
Which statements correctly describe common Kafka errors and how clients handle them?

- A. `TimeoutException` can occur when a producer cannot get acknowledgment within `delivery.timeout.ms` or metadata within `max.block.ms`.
- B. `NotLeaderForPartitionException`/`NotLeaderOrFollowerException` is typically transient, the client refreshes metadata and retries against the new leader.
- C. A `SerializationException` is a retriable error that Kafka will automatically keep retrying until it succeeds.
- D. `RecordTooLargeException` occurs when a record exceeds `max.request.size` (producer) or the broker's `message.max.bytes`.
- E. Retriable errors are retried automatically up to `retries`/`delivery.timeout.ms`, while non-retriable errors (e.g. serialization errors) fail fast.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, D, A, E

**Explanation:**

Kafka clients distinguish *retriable* from *non-retriable* errors. Leadership errors like `NotLeaderForPartitionException` (newer `NotLeaderOrFollowerException`) are transient — they happen during leader elections/reassignments, and the client simply refreshes metadata and retries against the new leader. `RecordTooLargeException` is raised when a record exceeds the producer's `max.request.size` or the broker's `message.max.bytes` (topic `max.message.bytes`), so the fix is configuration/record size, not retrying blindly. `TimeoutException` surfaces when the producer can't obtain acknowledgment within `delivery.timeout.ms` or can't fetch metadata/allocate buffer within `max.block.ms`. The idempotent producer and its retry machinery automatically retry retriable errors up to the configured `retries`/`delivery.timeout.ms`. Statement C is false: a `SerializationException` is *non-retriable* — retrying the same unserializable record will always fail, so it fails fast and should be handled (e.g. routed to a DLQ) rather than retried.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 & Ch. 7 (Producer errors, reliability), https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ✅ **A. `TimeoutException` from `delivery.timeout.ms`/`max.block.ms`.**  
   **Correct**. Common timeout causes.

2. ✅ **B. Leader errors are transient, refresh metadata and retry.**  
   **Correct**. Retriable leadership change.

3. ❌ **C. `SerializationException` is retriable and auto-retried.**  
   **Incorrect**. It is non-retriable and fails fast.

4. ✅ **D. `RecordTooLargeException` from size limits.**  
   **Correct**. `max.request.size`/`message.max.bytes`.

5. ✅ **E. Retriable retried automatically, non-retriable fail fast.**  
   **Correct**. The core error taxonomy.

</details>

## Question 13 (Programming & Serialization):
Which statements about common data/serialization formats used with Kafka are correct?

- A. Plain JSON (without a schema) is human-readable but carries no enforced schema and is less compact than Avro.
- B. Avro, Protobuf, and JSON Schema are the formats natively supported by Confluent Schema Registry.
- C. The `StringSerializer` and `ByteArraySerializer` are built-in Kafka serializers that require no Schema Registry.
- D. Avro stores data compactly in binary and relies on a separate schema, it is well suited to schema evolution.
- E. Avro messages produced with `KafkaAvroSerializer` embed the full schema text in every record payload.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, D, A, C

**Explanation:**

Confluent Schema Registry natively supports three serialization formats: Avro, Protobuf, and JSON Schema. Avro encodes data compactly in binary and keeps the schema separate from the data, which — combined with its default values and resolution rules — makes it a strong fit for schema evolution. Plain JSON is human-readable and flexible but has no enforced schema and is more verbose (larger payloads) than Avro's binary encoding. Kafka also ships simple built-in serializers such as `StringSerializer`, `ByteArraySerializer`, `IntegerSerializer`, and `LongSerializer` that work without any Schema Registry. Statement E is false: `KafkaAvroSerializer` does *not* embed the full schema in each record — it registers the schema once and writes only a compact schema **ID** (a magic byte plus a 4-byte ID) in front of the Avro-encoded payload, which is exactly what keeps messages small.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (Serializers), Confluent Schema Registry docs, `9.schema-registry/schema-registry-summary.md`

**Detailed explanation of each option:**

1. ✅ **A. Plain JSON: readable, unenforced schema, less compact.**  
   **Correct**. Trade-offs of schemaless JSON.

2. ✅ **B. Avro, Protobuf, JSON Schema supported by Schema Registry.**  
   **Correct**. These are the three registry formats.

3. ✅ **C. `StringSerializer`/`ByteArraySerializer` need no registry.**  
   **Correct**. Built-in simple serializers.

4. ✅ **D. Avro is compact binary with a separate schema, good for evolution.**  
   **Correct**. A defining property of Avro.

5. ❌ **E. Avro records embed full schema text each time.**  
   **Incorrect**. They carry only a 4-byte schema ID, not the schema text.

</details>

## Question 14 (Kafka Producers):
Arrange the following steps a transactional Kafka producer performs to atomically produce records and commit consumer offsets, in the correct order.

- A. `beginTransaction()` to start a new transaction
- B. `sendOffsetsToTransaction()` to include the consumed input offsets in the transaction
- C. `initTransactions()` to initialize the transactional producer (register the `transactional.id`)
- D. `send()` the output records
- E. `commitTransaction()` to atomically commit the records and offsets

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** C, A, D, B, E

**Explanation:**

A transactional producer must first call `initTransactions()` once at startup, this registers its configured `transactional.id` with the transaction coordinator and fences off any previous producer instance using the same id. For each consume-process-produce cycle it then calls `beginTransaction()`, sends the output records with `send()`, and—when implementing exactly-once across a consume-then-produce flow—calls `sendOffsetsToTransaction()` to include the input topic offsets in the same transaction. Finally, `commitTransaction()` atomically commits both the produced records and the consumer offsets, so either everything becomes visible or nothing does. This ordering is what gives Kafka Streams and read-process-write apps their exactly-once guarantee.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 (Transactions, exactly-once), https://kafka.apache.org/documentation/#transactions

**Detailed explanation of each option:**

- **C. `initTransactions()`** — Step 1: one-time initialization that registers the `transactional.id` and fences prior instances.
- **A. `beginTransaction()`** — Step 2: opens a new transaction for this cycle.
- **D. `send()` the output records** — Step 3: produces the records as part of the open transaction.
- **B. `sendOffsetsToTransaction()`** — Step 4: adds the consumed input offsets to the same transaction (for consume-process-produce EOS).
- **E. `commitTransaction()`** — Step 5: atomically commits both records and offsets, making them visible together.

</details>

## Question 15 (Programming & Serialization):
With the default `TopicNameStrategy`, how is the subject name derived for the value schema of a topic named `orders`, and what does this imply?

- A. The subject is `orders-value`, which means all messages in the topic's value must conform to that subject's schema (and its compatible evolutions).
- B. The subject is `orders` with no suffix, shared between key and value.
- C. The subject is the fully-qualified record name, allowing many topics to share one subject.
- D. The subject is randomly generated per message.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The default subject naming strategy is `TopicNameStrategy`, which names the subject as the topic name suffixed with `-key` or `-value`. For the value schema of topic `orders`, the subject is `orders-value`. This implies that all message values in the topic must conform to the schema registered under that subject (and to its compatible evolutions), so a topic effectively carries a single value schema lineage. `RecordNameStrategy` (fully-qualified record name) and `TopicRecordNameStrategy` (topic plus record name) are alternatives used when a topic must carry multiple record types or when a schema is shared across topics.

Source: `9.schema-registry/schema-registry-summary.md` (Subject Naming Strategies), Confluent Schema Registry docs

**Detailed explanation of each option:**

1. ✅ **A. The subject is `orders-value`, which means all messages in the topic's value must conform to that subject's schema (and its compatible evolutions).**  
   **Correct**. TopicNameStrategy yields `<topic>-value` and binds the topic to one value schema lineage.

2. ❌ **B. The subject is `orders` with no suffix, shared between key and value.**  
   **Incorrect**. The default adds `-key` or `-value` suffixes.

3. ❌ **C. The subject is the fully-qualified record name, allowing many topics to share one subject.**  
   **Incorrect**. That describes `RecordNameStrategy`, not the default.

4. ❌ **D. The subject is randomly generated per message.**  
   **Incorrect**. Subjects are deterministic, not random.

</details>

## Question 16 (Stream Processing):
When monitoring a Kafka Streams application, which metric most directly tells you whether the application is falling behind the input topics it consumes?

- A. `ActiveControllerCount` of the brokers.
- B. The consumer lag of the application's underlying consumer (for example, `records-lag-max`), since Kafka Streams consumes from Kafka with embedded consumers.
- C. The output topic's replication factor.
- D. The Schema Registry's compatibility-check count.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A Kafka Streams application reads from its input topics using embedded Kafka consumers, so the most direct signal that it is falling behind is the consumer lag of those embedded consumers, surfaced through standard consumer metrics such as `records-lag-max`. Growing lag means records are being produced faster than the topology can process them. Kafka Streams also exposes its own metrics (such as process and commit rates), but lag is the clearest "keeping up" indicator. The broker `ActiveControllerCount`, Schema Registry activity, and output-topic replication factor do not measure processing backlog.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 and Ch. 14 (Kafka Streams metrics, consumer lag), https://kafka.apache.org/documentation/#kafka_streams_monitoring

**Detailed explanation of each option:**

1. ❌ **A. `ActiveControllerCount` of the brokers.**  
   **Incorrect**. This is a controller-health metric, unrelated to processing backlog.

2. ✅ **B. The consumer lag of the application's underlying consumer (for example, `records-lag-max`), since Kafka Streams consumes from Kafka with embedded consumers.**  
   **Correct**. Lag on the embedded consumer directly shows whether the app is keeping up.

3. ❌ **C. The output topic's replication factor.**  
   **Incorrect**. A static durability setting, not a lag indicator.

4. ❌ **D. The Schema Registry's compatibility-check count.**  
   **Incorrect**. This does not reflect stream processing progress.

</details>

## Question 17 (Stream Processing):
A tumbling window of 1 minute is applied to a `count()` aggregation. How are records assigned to windows, and how many windows will contain a given record?

- A. Each record is assigned to every open window, so counts are duplicated across windows.
- B. Each record is assigned to exactly one 1-minute window based on its timestamp, producing non-overlapping per-minute counts.
- C. Records are assigned by partition number, not timestamp.
- D. Each record spans two adjacent windows to smooth the count.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A tumbling window partitions the time axis into contiguous, equal, non-overlapping intervals. With a 1-minute tumbling window, a record is placed into exactly one window determined by its event timestamp, so you get one independent count per minute with no double counting. This is distinct from hopping windows, where overlap can place a record in multiple windows. Window assignment is driven by record timestamps (event time by default), not by partition number, and a record does not span adjacent tumbling windows.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Tumbling windows), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#windowing

**Detailed explanation of each option:**

1. ❌ **A. Each record is assigned to every open window, so counts are duplicated across windows.**  
   **Incorrect**. That would describe overlapping (hopping) windows, not tumbling.

2. ✅ **B. Each record is assigned to exactly one 1-minute window based on its timestamp, producing non-overlapping per-minute counts.**  
   **Correct**. Tumbling windows are non-overlapping, so each record maps to one window.

3. ❌ **C. Records are assigned by partition number, not timestamp.**  
   **Incorrect**. Windowing is based on record timestamps, not partitions.

4. ❌ **D. Each record spans two adjacent windows to smooth the count.**  
   **Incorrect**. Tumbling windows do not overlap, so records do not span two of them.

</details>

## Question 18 (Stream Processing):
Which statements correctly describe state stores in Kafka Streams?

- A. A changelog topic that backs a state store is configured with log compaction.
- B. Disabling the changelog ("logging") for a store removes its fault-tolerance guarantee.
- C. Interactive Queries allow read access to the values stored in local state stores.
- D. State stores can only be key-value stores, windowed and session stores are not supported.
- E. Standby replicas can keep shadow copies of state stores to speed up failover.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, E, C, B

**Explanation:**

State stores in Kafka Streams are durable and queryable. Their changelog topics use log compaction so the latest value per key is retained, enabling a complete restore of current state. Standby replicas maintain warm copies of state from the changelog so that failover to another instance is fast rather than requiring a full replay. Interactive Queries expose the local state stores for read-only lookups directly from the application, avoiding a round trip to an external datastore. Kafka Streams supports several store types including key-value, windowed, and session stores. If you explicitly disable logging for a store, Kafka Streams no longer writes a changelog, so the store loses its fault-tolerance and cannot be restored after failure.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Local State, Standby replicas, Interactive Queries), https://kafka.apache.org/documentation/streams/developer-guide/

**Detailed explanation of each option:**

1. ✅ **A. A changelog topic that backs a state store is configured with log compaction.**  
   **Correct**. Compaction retains the latest value per key for full state restoration.

2. ✅ **B. Disabling the changelog ("logging") for a store removes its fault-tolerance guarantee.**  
   **Correct**. Without a changelog, the store cannot be restored after failure.

3. ✅ **C. Interactive Queries allow read access to the values stored in local state stores.**  
   **Correct**. Interactive Queries expose read-only access to local state.

4. ❌ **D. State stores can only be key-value stores, windowed and session stores are not supported.**  
   **Incorrect**. Key-value, windowed, and session stores are all supported.

5. ✅ **E. Standby replicas can keep shadow copies of state stores to speed up failover.**  
   **Correct**. `num.standby.replicas` keeps warm copies to minimize recovery time.

</details>

## Question 19 (Stream Processing):
Which statements correctly describe the window types available in the Kafka Streams DSL?

- A. Hopping windows are fixed-size but can overlap because the advance (hop) is smaller than the window size, so a record can fall into multiple windows.
- B. Session windows group records by periods of activity separated by an inactivity gap and have a dynamic, data-driven size.
- C. Sliding windows (for joins/aggregations) define windows based on the time difference between record timestamps.
- D. Tumbling windows are fixed-size, non-overlapping, and gap-less, each record belongs to exactly one window.
- E. Tumbling windows always overlap by half their size.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, A, B, C

**Explanation:**

Kafka Streams provides several window types for time-based aggregations and joins. Tumbling windows are a special case of hopping windows where the advance equals the window size, so they are fixed-size, non-overlapping, and gap-less, and each record maps to exactly one window. Hopping windows are fixed-size but advance by a smaller hop, causing overlap so a single record can belong to multiple windows. Session windows are dynamic: they group records into sessions separated by a configurable inactivity gap, so their size depends on the data. Sliding windows define membership by the timestamp difference between records, which is particularly useful for windowed joins. The claim that tumbling windows always overlap is false by definition.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Windowing: Tumbling, Hopping, Session, Sliding), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#windowing

**Detailed explanation of each option:**

1. ✅ **A. Hopping windows are fixed-size but can overlap because the advance (hop) is smaller than the window size, so a record can fall into multiple windows.**  
   **Correct**. A hop smaller than the size produces overlapping windows.

2. ✅ **B. Session windows group records by periods of activity separated by an inactivity gap and have a dynamic, data-driven size.**  
   **Correct**. Session windows are defined by an inactivity gap and vary in size.

3. ✅ **C. Sliding windows (for joins/aggregations) define windows based on the time difference between record timestamps.**  
   **Correct**. Sliding windows use timestamp differences between records.

4. ✅ **D. Tumbling windows are fixed-size, non-overlapping, and gap-less, each record belongs to exactly one window.**  
   **Correct**. Tumbling windows partition time into contiguous, non-overlapping intervals.

5. ❌ **E. Tumbling windows always overlap by half their size.**  
   **Incorrect**. Tumbling windows never overlap, this describes a hopping window.

</details>

## Question 20 (Stream Processing):
Which statements correctly describe Kafka Streams?

- A. Kafka Streams runs as a normal application/library against a Kafka cluster — it does not require a separate processing cluster.
- B. Kafka Streams is a library for building stream-processing topologies with built-in state, windowing, and joins, whereas the plain consumer/producer APIs give you raw read/write primitives you must orchestrate yourself.
- C. Kafka Streams manages local state stores (backed by changelog topics) and offset commits for you, with plain clients you handle state and commits manually.
- D. Kafka Streams can only move data unchanged from one topic to another and cannot perform aggregations or joins.
- E. Kafka Streams provides exactly-once processing via a single config (`processing.guarantee=exactly_once_v2`), which is harder to assemble by hand with plain clients.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, C, A, E

**Explanation:**

Kafka Streams is a higher-level library built on top of the producer and consumer clients. It lets you declare a processing topology with rich operations — stateful aggregations, windowing, and stream/table joins — and handles the heavy lifting: local state stores backed by fault-tolerant changelog topics, offset management, and task distribution/rebalancing across instances. With the plain consumer/producer APIs you get only raw primitives (poll, process, send, commit) and must build state handling, windowing, and commit logic yourself. Streams also runs as an ordinary JVM application/library using Kafka as its backbone — no separate processing cluster is needed — and it offers exactly-once processing through a single setting (`processing.guarantee=exactly_once_v2`), which would be substantially more work to replicate with raw clients. Statement D is false: performing aggregations, joins, and windowing is precisely what Streams adds beyond simple passthrough.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Stream Processing — why Kafka Streams), https://kafka.apache.org/documentation/streams/

**Detailed explanation of each option:**

1. ✅ **A. Streams runs as a library, no separate cluster.**  
   **Correct**. It is an application-embedded library.

2. ✅ **B. Streams = topologies with state/windowing/joins vs raw primitives.**  
   **Correct**. The fundamental distinction.

3. ✅ **C. Streams manages state stores and offsets for you.**  
   **Correct**. Plain clients require manual handling.

4. ❌ **D. Streams can only passthrough, no aggregations/joins.**  
   **Incorrect**. Aggregations and joins are core Streams features.

5. ✅ **E. EOS via one config setting.**  
   **Correct**. `exactly_once_v2` is built in.

</details>

## Question 21 (Kafka Internals):
In a KRaft-based Kafka cluster, the active controller fails. Arrange the following steps of the controller election and recovery, in the correct order.

- A. The new active controller replays the metadata log to rebuild the latest cluster state in memory
- B. The new controller begins serving metadata and handling broker/partition changes for the cluster
- D. A new leader is elected for the metadata (`__cluster_metadata`) partition via the Raft protocol
- C. Controller nodes in the quorum detect the leader is gone (missed heartbeats / election timeout)

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** C, D, A, B

**Explanation:**

In KRaft mode (the only mode in Kafka 4.x — ZooKeeper was removed in 4.0), cluster metadata lives in an internal replicated log,
the `__cluster_metadata` topic, managed by a quorum of controller nodes using the Raft consensus protocol. 
When the active controller (the Raft leader) fails, the remaining controllers in the quorum detect its absence through missed heartbeats 
and an election timeout, then run a Raft leader election to choose a new leader for the metadata partition. A candidate can only win if its
log is at least as up to date as a majority of the quorum, which guarantees no committed metadata is lost. The winner becomes the new active controller, 
it replays the metadata log up to the latest committed offset to rebuild the current cluster state in memory, and then starts serving metadata requests and processing
broker and partition changes. Because the metadata is already a replicated log, failover is fast — there is no external coordination service 
to reconcile with. Note a KRaft quorum tolerates failures only while a majority of controllers remain available.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 (Kafka Internals — Cluster Membership, The Controller), KIP-500 / KRaft, https://kafka.apache.org/documentation/#kraft

**Detailed explanation of each option:**

- **D. New metadata-partition leader elected via Raft** — Step 2: a candidate with an up-to-date log wins a majority vote.
- **B. New controller serves metadata and handles changes** — Step 4: it becomes active and resumes cluster management.
- **C. Controllers detect the leader is gone** — Step 1: missed heartbeats trigger an election timeout in the quorum.
- **A. New controller replays the metadata log** — Step 3: rebuilds the latest cluster state in memory from the committed log.

</details>

## Question 22 (Kafka Setup and Operations):
Which client configuration properties are required to connect a Kafka client to a cluster using SASL/SCRAM over an encrypted channel?

- A. `security.protocol=SASL_SSL`
- B. `sasl.jaas.config` with the SCRAM login module and credentials
- C. `ssl.endpoint.identification.algorithm=none` is mandatory for SCRAM
- D. `sasl.mechanism=SCRAM-SHA-256` (or `SCRAM-SHA-512`)
- E. `compression.type=gzip`

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, B

**Explanation:**

To authenticate a client with SASL/SCRAM over TLS, you set `security.protocol=SASL_SSL` so that authentication uses SASL and the connection is encrypted with TLS. You select the SCRAM mechanism via `sasl.mechanism` (SCRAM-SHA-256 or SCRAM-SHA-512), and you provide the credentials through `sasl.jaas.config` using the SCRAM login module. Disabling hostname verification (`ssl.endpoint.identification.algorithm=none`) is not required and is generally discouraged for security. Compression settings like `compression.type` are unrelated to authentication and encryption.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Securing Kafka: SASL/SCRAM, TLS), https://kafka.apache.org/documentation/#security_sasl_scram

**Detailed explanation of each option:**

1. ✅ **A. `security.protocol=SASL_SSL`**  
   **Correct**. Selects SASL authentication over a TLS-encrypted channel.

2. ✅ **B. `sasl.jaas.config` with the SCRAM login module and credentials**  
   **Correct**. Provides the login module and username/password.

3. ❌ **C. `ssl.endpoint.identification.algorithm=none` is mandatory for SCRAM.**  
   **Incorrect**. It is not required and disabling hostname verification weakens security.

4. ✅ **D. `sasl.mechanism=SCRAM-SHA-256` (or `SCRAM-SHA-512`)**  
   **Correct**. Chooses the SCRAM mechanism for authentication.

5. ❌ **E. `compression.type=gzip`**  
   **Incorrect**. Compression is unrelated to security configuration.

</details>

## Question 23 (Stream Processing):
A Kafka Streams topology performs a windowed count aggregation. Where is the intermediate count for each key and window kept while the window is open?

- A. In ZooKeeper, which tracks per-window counters.
- B. In the consumer offset topic for the application.
- C. Only in the output topic, re-read on every record.
- D. In a windowed state store local to the stream task, backed by a changelog topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Windowed aggregations such as counts require maintaining a running value per key and per window until the window closes (and through its grace period). Kafka Streams keeps these intermediate results in a windowed state store local to the task, typically RocksDB-backed, with a compacted changelog topic for fault tolerance. Results are emitted downstream as the aggregate updates. ZooKeeper plays no role in application state, the offsets topic tracks only consumer positions, and re-reading the output topic for every record would be incorrect and inefficient.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Windowed operations and state stores), https://kafka.apache.org/documentation/streams/

**Detailed explanation of each option:**

1. ❌ **A. In ZooKeeper, which tracks per-window counters.**  
   **Incorrect**. ZooKeeper does not store application aggregation state.

2. ❌ **B. In the consumer offset topic for the application.**  
   **Incorrect**. The offsets topic tracks consumer positions, not aggregation values.

3. ❌ **C. Only in the output topic, re-read on every record.**  
   **Incorrect**. The running state is kept in a local store, not reconstructed from the output topic each time.

4. ✅ **D. In a windowed state store local to the stream task, backed by a changelog topic.**  
   **Correct**. Windowed aggregations use a local windowed store with a changelog for recovery.

</details>

## Question 24 (Kafka Connect):
What is a Single Message Transform (SMT) in Kafka Connect, and where is it applied?

- A. A broker-side plugin that rewrites records already stored in the log.
- B. A lightweight transformation configured on a connector that modifies or filters each record as it passes between the connector and Kafka, without needing a separate stream processor.
- C. A Schema Registry feature that converts Avro to Protobuf automatically.
- D. A consumer-group setting that reorders records before delivery.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A Single Message Transform (SMT) is a simple, per-record transformation you configure directly on a Kafka Connect source or sink connector. SMTs operate on one record at a time as it flows between the connector and Kafka: for a source connector, after the task produces a record and before it is written to Kafka, for a sink connector, after reading from Kafka and before writing to the external system. Common SMTs include renaming or masking fields, inserting a static field, routing to a different topic, extracting a field as the key, or adding/extracting headers. SMTs run inside the Connect worker—they are not broker-side, not a consumer setting, and not a Schema Registry conversion feature. For anything beyond simple per-record edits, you use Kafka Streams or ksqlDB instead.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Kafka Connect, Transformations), https://kafka.apache.org/documentation/#connect_transforms

**Detailed explanation of each option:**

1. ❌ **A. A broker-side plugin that rewrites records already stored in the log.**  
   **Incorrect**. SMTs run in Connect workers, not on the broker, and do not rewrite stored data.

2. ✅ **B. A lightweight transformation configured on a connector that modifies or filters each record as it passes between the connector and Kafka, without needing a separate stream processor.**  
   **Correct**. SMTs are per-record transforms configured on the connector, running in the Connect worker.

3. ❌ **C. A Schema Registry feature that converts Avro to Protobuf automatically.**  
   **Incorrect**. Format conversion is handled by converters, not SMTs.

4. ❌ **D. A consumer-group setting that reorders records before delivery.**  
   **Incorrect**. SMTs are a Connect feature, not a consumer-group setting, and do not reorder records.

</details>

## Question 25 (Kafka Connect):
A new worker joins an existing distributed Kafka Connect cluster. Arrange the following steps of the resulting rebalance, in the correct order.

- A. Connectors and tasks are redistributed across all available workers
- B. The new worker joins the Connect group
- C. Each worker resumes its assigned tasks from the offsets stored in the internal offsets topic
- D. The group coordinator triggers a rebalance of the Connect group

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** B, D, A, C

**Explanation:**

Distributed Kafka Connect workers form a group that is coordinated through Kafka's group-membership protocol, much like a consumer group. When a new worker joins (or an existing one leaves or fails), it joins the Connect group and the group coordinator triggers a rebalance. During the rebalance the set of running connectors and their tasks is redistributed so the load is spread across all available workers. Each worker then (re)starts the tasks it was assigned, resuming from the offsets persisted in the internal Connect offsets topic rather than from scratch — this is what makes distributed Connect fault-tolerant and horizontally scalable. The config and status for connectors live in internal topics, so no external coordination service is required.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Kafka Connect — Running Connect in distributed mode), https://kafka.apache.org/documentation/#connect

**Detailed explanation of each option:**

- **B. New worker joins the Connect group** — Step 1: membership change triggers the protocol.
- **D. Coordinator triggers a rebalance** — Step 2: the group re-evaluates assignments.
- **A. Connectors and tasks redistributed** — Step 3: work is spread across workers.
- **C. Workers resume tasks from stored offsets** — Step 4: tasks pick up where they left off.

</details>

## Question 26 (Kafka Consumers):
A consumer needs to read a tracing identifier that the producer attached to each record without affecting the record's key or value. Where does it find this, and what should it expect?

- A. Only by parsing the value payload, since Kafka does not support per-record metadata.
- B. In the record's headers, accessible via `ConsumerRecord.headers()`, where each header is a string key with a byte-array value.
- C. From the consumer group coordinator, which stores per-record headers.
- D. In the record key, which always contains header metadata.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Record headers are exposed on the consumer side through `ConsumerRecord.headers()`. Each header has a string key and a byte-array value, so the consumer reads the tracing identifier by looking up the appropriate header key and decoding its bytes—without touching the record's key or value. This is exactly the intended use of headers: carrying cross-cutting metadata like trace/correlation IDs separately from the business data. The key is not a container for header metadata, Kafka does support per-record metadata (so you need not encode it into the value), and the group coordinator tracks offsets and membership, not per-record headers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 and Ch. 4 (Headers, ConsumerRecord), https://kafka.apache.org/documentation/#recordheader

**Detailed explanation of each option:**

1. ❌ **A. Only by parsing the value payload, since Kafka does not support per-record metadata.**  
   **Incorrect**. Kafka supports headers, so metadata need not be embedded in the value.

2. ✅ **B. In the record's headers, accessible via `ConsumerRecord.headers()`, where each header is a string key with a byte-array value.**  
   **Correct**. Consumers read headers via `ConsumerRecord.headers()`.

3. ❌ **C. From the consumer group coordinator, which stores per-record headers.**  
   **Incorrect**. The coordinator manages offsets and membership, not per-record headers.

4. ❌ **D. In the record key, which always contains header metadata.**  
   **Incorrect**. The key does not hold header metadata.

</details>

## Question 27 (Stream Processing):
Which statements about session windows in Kafka Streams are correct?

- A. Session windows are well suited to modeling bursts of user activity separated by idle periods.
- B. A late record arriving within the inactivity gap can cause two existing sessions to be merged into one.
- C. A session window closes when no new records arrive for a key within the configured inactivity gap.
- D. Session windows have a fixed, uniform size defined up front.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, B, A

**Explanation:**

Session windows are dynamic, data-driven windows defined by an inactivity gap rather than a fixed size. A session for a key continues as long as records keep arriving within the gap, once the gap elapses with no new records, the session is considered closed. Because sessions grow with activity, a record arriving in the gap between two previously separate sessions can bridge them, causing the two sessions to merge into a single larger session. This makes session windows a natural fit for modeling user activity that comes in bursts separated by idle time. The claim that they have a fixed uniform size is incorrect—that describes tumbling or hopping windows.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Session windows), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#session-windows

**Detailed explanation of each option:**

1. ✅ **A. Session windows are well suited to modeling bursts of user activity separated by idle periods.**  
   **Correct**. They naturally capture activity bursts separated by idle time.

2. ✅ **B. A late record arriving within the inactivity gap can cause two existing sessions to be merged into one.**  
   **Correct**. Bridging records merge adjacent sessions.

3. ✅ **C. A session window closes when no new records arrive for a key within the configured inactivity gap.**  
   **Correct**. The inactivity gap defines when a session ends.

4. ❌ **D. Session windows have a fixed, uniform size defined up front.**  
   **Incorrect**. Session windows are dynamic in size, driven by activity.

</details>

## Question 28 (Kafka Producers):
How does Kafka's default producer partitioner decide the target partition for a record in modern Kafka clients?

- A. It always sends every record to partition 0 unless a partition is specified explicitly.
- B. It always assigns partitions in strict round-robin regardless of the key.
- C. If the key is null it throws an exception, because a key is mandatory.
- D. If a key is present, the partition is `hash(key) % numPartitions` (consistent per key), if the key is null, the sticky partitioner batches records to one partition until the batch is sent, then may switch.
- E. It routes by record timestamp, placing newer records in higher-numbered partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The default partitioner behaves in two modes. When a record has a key, Kafka computes a hash of the key (murmur2) and maps it to a partition deterministically, so all records with the same key land in the same partition — this is what preserves per-key ordering and enables key-based locality. When the key is null, modern clients use the *sticky* partitioner: rather than round-robining every single record (which fragments batches), it sticks to one partition and fills a batch, then switches to another partition for the next batch. This improves batching and throughput while still spreading load across partitions over time. You can always override routing by specifying an explicit partition or supplying a custom partitioner.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (Partitions and the default partitioner), KIP-480 Sticky Partitioner, https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ❌ **A. Always partition 0.**  
   **Incorrect**. That is not how the default partitioner works.

2. ❌ **B. Always strict round-robin.**  
   **Incorrect**. Keyed records are hashed, null-key records use sticky batching, not per-record round-robin.

3. ❌ **C. Null key throws.**  
   **Incorrect**. A null key is valid and handled by the sticky partitioner.

4. ✅ **D. Keyed = hash(key) % partitions, null key = sticky partitioner batching per partition.**  
   **Correct**. This is the current default-partitioner behavior.

5. ❌ **E. Routes by timestamp.**  
   **Incorrect**. Timestamps do not determine the partition.

</details>

## Question 29 (Programming & Serialization):
Which statements correctly describe the compatibility types available in Confluent Schema Registry?

- A. The `*_TRANSITIVE` variants check a new schema against **all** previously registered versions, not just the most recent one.
- B. `FULL` requires both backward and forward compatibility, so only adding or removing fields that have default values is allowed.
- C. The available modes are `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`, `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, and `NONE`.
- D. `NONE` enforces the strictest possible checks, rejecting any schema change.
- E. `BACKWARD` (the default) lets a consumer with the new schema read data written with the previous schema, it checks only against the latest registered version.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** C, E, A, B

**Explanation:**

Confluent Schema Registry supports seven compatibility settings, configurable globally or per subject: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`, `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, and `NONE`. `BACKWARD` is the default and means a consumer using the new schema can read data produced with the prior schema (so you upgrade consumers first), allowed changes include adding fields with defaults, removing fields, and type widening. `FORWARD` means data produced with the new schema can be read by consumers using the prior schema (upgrade producers first). `FULL` requires both directions at once, which restricts safe changes to adding or removing fields that have default values. The key distinction of the `*_TRANSITIVE` variants is scope: non-transitive modes validate a new schema only against the **latest** version, while transitive modes validate it against **all** previous versions in the subject's history. Statement D is false — `NONE` is the opposite of strict: it disables compatibility checking entirely, so any change is accepted (and no safety is guaranteed).

Source: `9.schema-registry/schema-registry-summary.md` (compatibility modes, transitive variants), Confluent Schema Registry docs, https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

**Detailed explanation of each option:**

1. ✅ **A. `*_TRANSITIVE` checks against all previous versions.**  
   **Correct**. Transitive = full version history.

2. ✅ **B. `FULL` = backward + forward, add/remove fields with defaults only.**  
   **Correct**. Both-direction constraint.

3. ✅ **C. Seven modes incl. the three `*_TRANSITIVE` and `NONE`.**  
   **Correct**. That is the full set of compatibility types.

4. ❌ **D. `NONE` is the strictest, rejecting all changes.**  
   **Incorrect**. `NONE` disables checks, it is the least strict.

5. ✅ **E. `BACKWARD` is default, checks only the latest version.**  
   **Correct**. New reader reads old data, non-transitive scope.

</details>

## Question 30 (Stream Processing):
What distinguishes the Kafka Streams DSL from the Processor API?

- A. The DSL is a producer-only API with no consuming capability.
- B. The DSL and the Processor API are completely separate libraries that cannot be combined in one application.
- C. The Processor API cannot access state stores, only the DSL can.
- D. Only the Processor API can run on Kafka, the DSL requires an external cluster.
- E. The DSL offers high-level declarative operators (`map`, `filter`, `groupByKey`, `join`, windowing) while the Processor API gives low-level, imperative control over processors, state stores, and the topology.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka Streams exposes two levels of abstraction. The DSL is high-level and declarative: you compose transformations with ready-made operators such as `map`, `filter`, `flatMap`, `groupByKey`, `aggregate`, `join`, and the windowing operators, and Kafka Streams builds the underlying topology for you. The Processor API is low-level and imperative: you implement `Processor`/`Transformer` nodes, wire the topology explicitly, and interact directly with state stores and the record context — giving maximum control for custom logic that the DSL does not express cleanly. They are not mutually exclusive: you can drop into the Processor API from within a DSL topology using operators like `process`/`transform`, mixing both. Both access state stores, both run on Kafka, and both consume and produce — so the only correct description is E.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Kafka Streams — DSL and Processor API), https://kafka.apache.org/documentation/streams/developer-guide/

**Detailed explanation of each option:**

1. ❌ **A. DSL is producer-only.**  
   **Incorrect**. Streams both consumes and produces.

2. ❌ **B. They cannot be combined.**  
   **Incorrect**. You can mix them (e.g. `transform`/`process`).

3. ❌ **C. Processor API cannot access state stores.**  
   **Incorrect**. The Processor API has full, direct state-store access.

4. ❌ **D. DSL needs an external cluster.**  
   **Incorrect**. Both run as a normal Kafka client library.

5. ✅ **E. DSL = high-level declarative operators, Processor API = low-level imperative control.**  
   **Correct**. This is the defining difference.

</details>

## Question 31 (Stream Processing):
Which statements about joins and co-partitioning in Kafka Streams are correct?

- A. Co-partitioning means both topics must share the same leader broker.
- B. A KStream-GlobalKTable join does not require co-partitioning because the GlobalKTable is fully replicated on every instance.
- C. `selectKey()` or a repartition may be needed before a join if the stream is not keyed on the join key.
- D. For a KStream-KStream or KStream-KTable join, both input topics must be co-partitioned (same number of partitions and the same partitioning for keys).
- E. Joins can be performed on topics with different key types as long as the partition counts match.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, B, C

**Explanation:**

Kafka Streams joins (except those involving a GlobalKTable) require the input topics to be co-partitioned: the same number of partitions and the same key-based partitioning, so that matching keys are handled by the same task. If a stream is not already keyed on the join key, you must re-key it with `selectKey()` (and typically repartition) before joining. A KStream-GlobalKTable join is the exception—because the GlobalKTable is fully materialized on every application instance, the stream side can join against it regardless of its partitioning. Co-partitioning is about partition count and key partitioning, not about sharing a leader broker, and both sides must join on the same key, so differing key types that don't match cannot be joined just because partition counts align.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Co-partitioning, GlobalKTable joins), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#joining

**Detailed explanation of each option:**

1. ❌ **A. Co-partitioning means both topics must share the same leader broker.**  
   **Incorrect**. Co-partitioning is about partition count and key partitioning, not broker leadership.

2. ✅ **B. A KStream-GlobalKTable join does not require co-partitioning because the GlobalKTable is fully replicated on every instance.**  
   **Correct**. The fully materialized GlobalKTable removes the co-partitioning requirement.

3. ✅ **C. `selectKey()` or a repartition may be needed before a join if the stream is not keyed on the join key.**  
   **Correct**. Re-keying/repartitioning aligns the stream on the join key.

4. ✅ **D. For a KStream-KStream or KStream-KTable join, both input topics must be co-partitioned (same number of partitions and the same partitioning for keys).**  
   **Correct**. Co-partitioning ensures matching keys land in the same task.

5. ❌ **E. Joins can be performed on topics with different key types as long as the partition counts match.**  
   **Incorrect**. Both sides must join on the same matching key, not merely equal partition counts.

</details>

## Question 32 (Kafka Consumers):
What is the difference between a consumer's `subscribe()` and `assign()` methods?

- A. `assign()` joins a consumer group while `subscribe()` bypasses group coordination.
- B. `subscribe()` joins a consumer group and lets Kafka automatically assign and rebalance partitions, `assign()` manually pins specific partitions to the consumer with no group management or automatic rebalancing.
- C. They are aliases for the same behavior and can be used interchangeably.
- D. `subscribe()` is for producers and `assign()` is for consumers.
- E. `subscribe()` reads only the latest offset, `assign()` reads from the beginning.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

`subscribe()` opts the consumer into Kafka's group-management protocol: it joins a consumer group (identified by `group.id`), and the group coordinator automatically assigns partitions and triggers rebalances as members join or leave. `assign()`, by contrast, gives the application manual control — you hand the consumer an explicit list of `TopicPartition`s, and Kafka performs no group coordination, no automatic assignment, and no rebalancing for that consumer. Manual `assign()` is useful when you need deterministic ownership of specific partitions (for example, a single-process reader of a known partition), but you forgo automatic failover and load balancing. You cannot mix the two on the same consumer instance.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (subscribe vs assign), https://kafka.apache.org/documentation/#consumerapi

**Detailed explanation of each option:**

1. ❌ **A. `assign()` joins a group.**  
   **Incorrect**. It is the reverse: `subscribe()` joins the group.

2. ✅ **B. `subscribe()` = group + auto-assignment/rebalance, `assign()` = manual partitions, no group management.**  
   **Correct**. This is the exact distinction.

3. ❌ **C. They are interchangeable aliases.**  
   **Incorrect**. They have fundamentally different semantics and can't be mixed.

4. ❌ **D. One is for producers.**  
   **Incorrect**. Both are consumer methods.

5. ❌ **E. One reads latest, the other from the beginning.**  
   **Incorrect**. Starting offset is controlled by `auto.offset.reset`/`seek`, not by subscribe vs assign.

</details>

## Question 33 (Kafka Setup and Operations):
Arrange the following steps that occur when a client establishes a TLS (SSL)-encrypted connection to a Kafka broker, in the correct order.

- A. The client validates the broker's certificate against its configured `ssl.truststore.location`
- B. The client is configured with `security.protocol=SSL` and connects to the broker
- C. The broker presents its certificate during the TLS handshake
- D. An encrypted channel is established and Kafka protocol requests flow over it

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** B, C, A, D

**Explanation:**

To talk to a broker over TLS, the client must first be configured with `security.protocol=SSL` (or `SASL_SSL`) and point at a truststore. When it connects, the TLS handshake begins and the broker presents its certificate. The client then validates that certificate against the CA chain in its `ssl.truststore.location` — this is what prevents man-in-the-middle attacks. Only after the certificate is trusted is the encrypted channel established, after which normal Kafka protocol requests (metadata, produce, fetch) flow over the encrypted connection. If mutual TLS (`ssl.client.auth=required`) is enabled, the client also presents its own certificate from its keystore during the handshake, but the ordering of trust-then-encrypt is the same.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Securing Kafka — Encryption with SSL), https://kafka.apache.org/documentation/#security_ssl

**Detailed explanation of each option:**

- **B. Client configured with `security.protocol=SSL` and connects** — Step 1: without this the connection stays plaintext.
- **C. Broker presents its certificate** — Step 2: happens during the TLS handshake.
- **A. Client validates the certificate against its truststore** — Step 3: establishes that the broker is trusted.
- **D. Encrypted channel established, requests flow** — Step 4: Kafka traffic now travels encrypted.

</details>

## Question 34 (Kafka Setup and Operations):
Which statements about defining topic configurations are correct?

- A. Topic configuration cannot be changed after the topic is created.
- B. `retention.ms` (or `retention.bytes`) controls how long (or how much) data a topic keeps before deletion under the `delete` cleanup policy.
- C. A topic's default configs come from broker defaults but can be overridden per topic at creation or via `kafka-configs`.
- D. `min.insync.replicas` is a topic/broker config that, with `acks=all`, defines how many replicas must be in sync for a write to succeed.
- E. `cleanup.policy=compact` keeps the latest value per key instead of deleting by age, `delete` removes old segments by retention.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, E, D, C

**Explanation:**

Topic configuration governs retention, cleanup, and durability. `retention.ms`/`retention.bytes` set the time/size budget after which old data is eligible for deletion under the default `cleanup.policy=delete`. Setting `cleanup.policy=compact` switches to log compaction, which retains at least the latest value for each key rather than deleting purely by age (you can even combine `compact,delete`). `min.insync.replicas` works with `acks=all`: it is the minimum number of in-sync replicas that must acknowledge, and if the ISR drops below it the produce fails with `NotEnoughReplicas` — a key durability lever set at topic or broker level. Topic configs inherit from broker defaults but are overridable per topic at creation (`--config`) or later with `kafka-configs --alter`. Statement A is false — topic configs are very much mutable at runtime (only partition *decrease* is disallowed).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 (Topic configuration), https://kafka.apache.org/documentation/#topicconfigs

**Detailed explanation of each option:**

1. ❌ **A. Topic config can't change after creation.**  
   **Incorrect**. Most topic configs are dynamically changeable.

2. ✅ **B. `retention.ms`/`retention.bytes` govern deletion.**  
   **Correct**. Time/size retention under `delete`.

3. ✅ **C. Topic configs inherit defaults, overridable per topic.**  
   **Correct**. Set at creation or via `kafka-configs`.

4. ✅ **D. `min.insync.replicas` + `acks=all` defines required ISR.**  
   **Correct**. Durability threshold.

5. ✅ **E. `compact` keeps latest-per-key, `delete` by age.**  
   **Correct**. The two cleanup policies.

</details>

## Question 35 (Stream Processing):
In a Kafka Streams windowed aggregation, what is the role of the grace period (for example, set via `ofSizeAndGrace`)?

- A. It controls the interval at which commit offsets are flushed.
- B. It defines how long after a window's end Kafka Streams will still accept out-of-order (late) records into that window before the window is closed.
- C. It determines the retention of the output topic.
- D. It sets how long the state store keeps the window's result available for interactive queries only.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Because event time can arrive out of order, Kafka Streams lets you configure a grace period for a window. During the grace period—measured from the window's end—late-arriving records whose event timestamps fall within the window are still accepted and update the aggregation. Once the grace period elapses, the window is considered closed and later records for it are dropped. This decouples window boundaries from strict wall-clock arrival and controls the trade-off between result completeness and how long state must be held. It is not about offset flush intervals, output-topic retention, or interactive-query availability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Handling late events, grace period), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#windowing

**Detailed explanation of each option:**

1. ❌ **A. It controls the interval at which commit offsets are flushed.**  
   **Incorrect**. Offset flushing is unrelated to the grace period.

2. ✅ **B. It defines how long after a window's end Kafka Streams will still accept out-of-order (late) records into that window before the window is closed.**  
   **Correct**. The grace period bounds acceptance of late records before closing the window.

3. ❌ **C. It determines the retention of the output topic.**  
   **Incorrect**. Output-topic retention is a separate topic configuration.

4. ❌ **D. It sets how long the state store keeps the window's result available for interactive queries only.**  
   **Incorrect**. That is store retention, not the grace period's purpose.

</details>

## Question 36 (Kafka Setup and Operations):
Which statements about Kafka logging and log4j configuration are correct?

- A. Application/operational logging (log4j) is distinct from Kafka's data logs (the partition commit logs on disk).
- B. Kafka brokers and clients use a logging framework (log4j/Log4j2) configured via a `log4j.properties`/`log4j2.yaml`-style file.
- C. Broker log levels can be changed at runtime via `kafka-configs`/the Admin API without a full restart.
- D. Deleting the log4j configuration file speeds up the broker because it stops writing partition data.
- E. You can raise a specific logger (for example the request or controller logger) to `DEBUG` to troubleshoot without flooding everything.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, A, E, C

**Explanation:**

Kafka uses a standard Java logging framework (historically log4j, now Log4j2) configured through a properties/YAML file, controlling what the brokers and clients emit and where. It is important to distinguish this *application logging* from Kafka's *data logs* — the on-disk partition commit-log segments where records are stored, they are unrelated concepts that merely share the word "log." For troubleshooting you can raise an individual logger (e.g. `kafka.request.logger`, the controller, or a client package) to `DEBUG`/`TRACE` while leaving the rest at `INFO`, avoiding log floods. Modern Kafka also lets you adjust broker log levels dynamically at runtime via `kafka-configs --alter` / the Admin API (`incrementalAlterConfigs` on a broker-logger resource) without restarting. Statement D is nonsense: deleting the log4j config does not stop Kafka from persisting partition data (that is governed by the data logs and retention), and would only harm diagnostics.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Monitoring — logging), https://kafka.apache.org/documentation/#operations

**Detailed explanation of each option:**

1. ✅ **A. Application logging ≠ Kafka data logs.**  
   **Correct**. Two different "logs."

2. ✅ **B. Kafka uses log4j/Log4j2 via a config file.**  
   **Correct**. Standard logging configuration.

3. ✅ **C. Broker log levels changeable at runtime via `kafka-configs`.**  
   **Correct**. Dynamic logger levels, no restart.

4. ❌ **D. Deleting log4j config stops writing partition data.**  
   **Incorrect**. It only affects application logging, not data persistence.

5. ✅ **E. Raise a specific logger to DEBUG for troubleshooting.**  
   **Correct**. Per-logger levels avoid flooding.

</details>

## Question 37 (Stream Processing):
By default, where does a Kafka Streams application store the RocksDB files that back its local state stores, and what controls this location?

- A. In the broker's log directory on each broker.
- B. In a temporary directory that is always deleted on clean shutdown.
- C. Under the directory configured by `state.dir`, in a subdirectory named after the `application.id`.
- D. In ZooKeeper's data directory.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Streams persists local state (RocksDB files) on the application host's local disk under the directory given by the `state.dir` configuration, within a subdirectory named for the `application.id`. Keeping state local to the processing node is what makes stateful operations fast. ZooKeeper and the broker log directories are unrelated to application state. The files are not necessarily deleted on shutdown, retaining them lets an instance restart quickly without a full changelog replay.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Local State), https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (state.dir)

**Detailed explanation of each option:**

1. ❌ **A. In the broker's log directory on each broker.**  
   **Incorrect**. State lives on the application host, not in broker log directories.

2. ❌ **B. In a temporary directory that is always deleted on clean shutdown.**  
   **Incorrect**. State is retained to allow fast restarts.

3. ✅ **C. Under the directory configured by `state.dir`, in a subdirectory named after the `application.id`.**  
   **Correct**. `state.dir` controls the base path, subdirectories are keyed by `application.id`.

4. ❌ **D. In ZooKeeper's data directory.**  
   **Incorrect**. ZooKeeper does not store application state.

</details>

## Question 38 (Stream Processing):
Which of the following are stateful operations in the Kafka Streams DSL that require a state store?

- A. `aggregate()`
- B. `filter()`
- C. `mapValues()`
- D. `join()` of two KStreams within a window
- E. `count()`

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, A, D

**Explanation:**

Stateful DSL operations maintain state across records and therefore require a state store. Aggregations like `count()` and `aggregate()` keep a running result per key. Windowed joins between two KStreams buffer records from each side within the join window in a state store so that matching records can be found. In contrast, `filter()` and `mapValues()` are stateless record-at-a-time transformations that examine or transform a single record without remembering anything, so no state store is needed.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Stateless vs. stateful transformations, joins), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html

**Detailed explanation of each option:**

1. ✅ **A. `aggregate()`**  
   **Correct**. Aggregations accumulate state per key.

2. ❌ **B. `filter()`**  
   **Incorrect**. Filtering is stateless, it evaluates a predicate per record.

3. ❌ **C. `mapValues()`**  
   **Incorrect**. Mapping values is a stateless per-record transformation.

4. ✅ **D. `join()` of two KStreams within a window**  
   **Correct**. Windowed stream-stream joins buffer records in a state store.

5. ✅ **E. `count()`**  
   **Correct**. Counting maintains a running total per key in a state store.

</details>

## Question 39 (Kafka Internals):
A team stores the current account balance per account in a compacted Kafka topic so a consumer can rebuild all current balances by reading the topic from the beginning. Which configuration best supports this use case?

- A. `cleanup.policy=compact`, keyed by account ID, writing a tombstone (null value) when an account is closed.
- B. `cleanup.policy=delete` with a 7-day retention so old records are purged by time.
- C. No key on the records, relying on partition order to find the latest balance.
- D. A very small `segment.bytes` with `cleanup.policy=delete` to force frequent deletion of all data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Rebuilding current state per key from a topic is the canonical log-compaction use case. Setting `cleanup.policy=compact` and keying records by account ID ensures Kafka retains at least the latest balance for each account, so a consumer reading from the beginning reconstructs all current balances. Writing a null-value tombstone when an account is closed removes that key during compaction. Time-based deletion (`cleanup.policy=delete`) would discard history needed to rebuild state, unkeyed records break compaction's per-key semantics, and aggressive deletion would lose the current values entirely.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Cleaning the Log" (use cases for compaction), https://kafka.apache.org/documentation/#compaction

**Detailed explanation of each option:**

1. ✅ **A. `cleanup.policy=compact`, keyed by account ID, writing a tombstone (null value) when an account is closed.**  
   **Correct**. Compaction keyed by account ID retains the latest balance, tombstones remove closed accounts.

2. ❌ **B. `cleanup.policy=delete` with a 7-day retention so old records are purged by time.**  
   **Incorrect**. Time-based deletion would lose state needed to rebuild balances.

3. ❌ **C. No key on the records, relying on partition order to find the latest balance.**  
   **Incorrect**. Compaction requires keys, unkeyed records cannot be compacted per account.

4. ❌ **D. A very small `segment.bytes` with `cleanup.policy=delete` to force frequent deletion of all data.**  
   **Incorrect**. This deletes the very data needed to reconstruct balances.

</details>

## Question 40 (Kafka Core Concepts):
Place the following stages of a produce request's lifecycle inside a Kafka broker into the correct order, from arrival to acknowledgment.

- D. An I/O (request handler) thread picks up the request and validates it
- C. The broker waits for the required in-sync replicas to replicate per the `acks` setting
- B. The leader appends the records to the partition's log (page cache)
- E. The response (acknowledgment) is placed on the response queue and sent back to the client
- A. The network thread receives the request and places it on the request queue

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** A, D, B, C, E

**Explanation:**

A produce request follows a well-defined path through the broker. A network (processor) thread reads the request off the socket and enqueues it on the shared request queue. A request-handler (I/O) thread then dequeues it, validates it (authorization, format, etc.), and the leader appends the records to the partition's log — in practice written to the OS page cache, which is flushed to disk asynchronously. If `acks=all`, the broker holds the request in purgatory until the required in-sync replicas have fetched and replicated the records, with `acks=1` it responds after the leader write, and with `acks=0` the client does not wait. Once the acknowledgment condition is satisfied, the response is placed on the response queue and a network thread sends it back to the producer. Understanding this flow explains why `acks` and ISR directly affect produce latency and durability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 (Kafka Internals — How requests are processed, purgatory), https://kafka.apache.org/documentation/#design

**Detailed explanation of each option:**

- **A. Network thread receives the request, enqueues it** — Step 1: request arrives on the request queue.
- **D. I/O (handler) thread picks it up and validates** — Step 2: dequeued and checked.
- **B. Leader appends records to the log (page cache)** — Step 3: the write happens on the leader.
- **C. Wait for required in-sync replicas per `acks`** — Step 4: durability is enforced via replication.
- **E. Response placed on response queue and returned** — Step 5: the acknowledgment is sent back.

</details>

## Question 41 (Kafka Setup and Operations):
Which statements about the `kafka-configs` (`kafka-configs.sh`) CLI tool are correct?

- A. `kafka-configs` is the tool used to create topics.
- B. `kafka-configs --alter --entity-type topics --entity-name orders --add-config retention.ms=604800000` dynamically sets a topic-level config.
- C. `--delete-config retention.ms` removes a previously set override so the value reverts to the default.
- D. `kafka-configs --describe --entity-type topics --entity-name orders` shows the configuration overrides for a topic.
- E. It can view and alter configs for entity types such as `topics`, `brokers`, `users`, and `clients` (e.g. quotas).

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, B, E, C

**Explanation:**

`kafka-configs` reads and dynamically alters configuration entities without a restart. `--describe --entity-type topics --entity-name <t>` lists a topic's non-default overrides. `--alter --add-config key=value` sets a dynamic config (for example `retention.ms`, `cleanup.policy`, or a broker log level). It operates on multiple entity types — `topics`, `brokers`, `users`, and `clients` — which is how per-user/per-client quotas and per-broker dynamic settings are managed. `--delete-config <key>` removes an override so the entity falls back to the broker/cluster default. Statement A is false: topic creation is done with `kafka-topics --create`, not `kafka-configs` (which only reads/changes configuration of entities that already exist).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Dynamic configuration — kafka-configs), https://kafka.apache.org/documentation/#dynamicbrokerconfigs

**Detailed explanation of each option:**

1. ❌ **A. `kafka-configs` creates topics.**  
   **Incorrect**. Topic creation is `kafka-topics --create`.

2. ✅ **B. `--alter --add-config` sets a dynamic config.**  
   **Correct**. Runtime config change, no restart.

3. ✅ **C. `--delete-config` reverts to default.**  
   **Correct**. Removes the override.

4. ✅ **D. `--describe --entity-type topics` shows overrides.**  
   **Correct**. Views entity configuration.

5. ✅ **E. Works on topics, brokers, users, clients.**  
   **Correct**. Covers quotas and dynamic broker configs too.

</details>

## Question 42 (Kafka Producers):
A team wants all events for the same customer to be processed in order while spreading load across partitions. How should they design their record keys?

- A. Use the customer ID as the record key, so all events for a customer hash to the same partition and keep per-customer order.
- B. Put every customer's events in a separate topic with one partition each.
- C. Use a random UUID per event as the key to maximize even distribution.
- D. Use the current timestamp as the key so events are ordered globally.
- E. Use a null key and rely on ordering being preserved across all partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka guarantees ordering only *within* a partition, and the default partitioner sends all records with the same key to the same partition. So choosing the customer ID as the key makes every event for a given customer land on one partition, preserving the order of that customer's events, while different customers hash across the available partitions to spread load. A random UUID would scatter a single customer's events across partitions and destroy per-customer ordering. A null key gives no ordering guarantee across partitions. A timestamp key provides neither per-entity grouping nor reliable global ordering. Creating a one-partition topic per customer does not scale and defeats partition-based parallelism.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (Keys and partitioning), https://kafka.apache.org/documentation/#intro_topics

**Detailed explanation of each option:**

1. ✅ **A. Customer ID as key.**  
   **Correct**. Same key → same partition → per-customer ordering, with load spread across customers.

2. ❌ **B. One single-partition topic per customer.**  
   **Incorrect**. Unscalable and unnecessary, keying solves the problem.

3. ❌ **C. Random UUID per event.**  
   **Incorrect**. Scatters one customer's events across partitions, breaking order.

4. ❌ **D. Timestamp as key.**  
   **Incorrect**. Does not group a customer's events and gives no global order.

5. ❌ **E. Null key, expecting cross-partition order.**  
   **Incorrect**. Kafka does not order across partitions.

</details>

## Question 43 (Kafka Setup and Operations):
Which statements reflect best practices and constraints when modifying existing Kafka topics?

- A. You can increase a topic's partition count, but you cannot decrease it.
- B. The replication factor of an existing topic is changed by simply editing a number in one command flag with no reassignment needed.
- C. Deleting and recreating a topic is always the safest way to add partitions.
- D. Increasing partitions can change which partition a given key maps to for new records, breaking existing per-key ordering assumptions.
- E. Topic-level configuration overrides (for example `retention.ms`) and  can be changed at runtime with `kafka-configs`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, E

**Explanation:**

Topics can be scaled up in partitions with `kafka-topics --alter`, but Kafka never supports reducing the partition count (doing so would require dropping data and remapping keys). Increasing partitions changes the modulus in `hash(key) % numPartitions`, so new records for an existing key may route to a different partition than before — existing data stays put, but per-key ordering across the change is no longer guaranteed, which is why partition count is best chosen up front. Many topic configs (retention, cleanup policy, etc.) are dynamic and can be overridden per-topic at runtime via `kafka-configs --alter --add-config`. Replication factor is *not* changed by a single flag, it requires a partition reassignment (`kafka-reassign-partitions`) with a JSON plan, so D is false. Deleting and recreating a topic loses data and consumer offsets, so it is not a safe way to add partitions — E is false.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 & Ch. 12 (Managing topics, reassignment), https://kafka.apache.org/documentation/#basic_ops_modify_topic

**Detailed explanation of each option:**

1. ✅ **A. Can increase but not decrease partitions.**  
   **Correct**. Partition count is one-directional.

2. ❌ **B. Replication factor changed by one flag, no reassignment.**  
   **Incorrect**. Changing replication factor requires a partition reassignment — you must generate a reassignment JSON plan and execute it via `kafka-reassign-partitions`.
   There is no single command flag that changes it directly. It’s a multi-step process involving data movement across brokers.

3. ❌ **C. Delete-and-recreate is the safest way to add partitions.**  
   **Incorrect**. Deleting and recreating is not the safest way — it destroys all existing data. 
   The correct approach is `kafka-topics --alter --partitions N`. Recreating is only necessary when you need to decrease partitions (which alter doesn’t support), and even then data loss is accepted as a trade-off.

4. ✅ **D. Increasing partitions can remap keys for new records.**  
   **Correct**. The hash modulus changes.

5. ✅ **E. Topic configs changeable at runtime via `kafka-configs`.**  
   **Correct**. Dynamic per-topic overrides are supported. 
   ```
   kafka-configs --bootstrap-server ... --alter \
      --entity-type topics --entity-name my-topic \
      --add-config retention.ms=86400000
   ```

</details>

## Question 44 (Kafka Consumers):
How do partitions and consumers interact within a single consumer group subscribed to a topic?

- A. Each partition of the topic is assigned to exactly one consumer in the group, and a consumer may own multiple partitions.
- B. Every consumer in the group reads every partition, so each message is processed by all consumers.
- C. The number of consumers can exceed the number of partitions with no idle consumers.
- D. Partitions are shared concurrently by all consumers, each reading half of every partition.
- E. A single partition is always split across two consumers for redundancy.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Within one consumer group, Kafka assigns each partition of a subscribed topic to exactly one consumer instance — this is how the group achieves parallel, non-overlapping consumption. A consumer may be assigned several partitions, but a given partition is never processed by more than one consumer in the same group at a time, which is what preserves per-partition ordering and avoids duplicate processing inside the group. The maximum useful parallelism is therefore the partition count: if you have more consumers than partitions, the extra consumers sit idle with no assignment. When consumers join or leave, a rebalance redistributes partitions across the active members.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (Consumers and Consumer Groups), https://kafka.apache.org/documentation/#intro_consumers

**Detailed explanation of each option:**

1. ✅ **A. Each partition is assigned to exactly one consumer, a consumer may own multiple partitions.**  
   **Correct**. This is the core consumer-group partition-assignment rule.

2. ❌ **B. Every consumer reads every partition.**  
   **Incorrect**. That describes different groups, not members of the same group, within a group partitions are divided.

3. ❌ **C. More consumers than partitions with no idle consumers.**  
   **Incorrect**. Extra consumers beyond the partition count remain idle.

4. ❌ **D. Partitions are shared concurrently by all consumers.**  
   **Incorrect**. A partition is owned by one consumer at a time, it is not split.

5. ❌ **E. A partition is split across two consumers for redundancy.**  
   **Incorrect**. Redundancy comes from replication of partitions, not from sharing a partition between consumers.

</details>

## Question 45 (Stream Processing):
In Kafka Streams, what is required for a KStream-to-KStream (stream-stream) join, and how does it differ from a KStream-to-KTable join?

- A. A stream-stream join is never windowed and matches records globally, a stream-table join must always be windowed.
- B. Neither join uses a state store, they match purely on arrival order.
- C. Both joins require a GlobalKTable and cannot use local state.
- D. A stream-stream join must be windowed, buffering records from both sides within the window in state stores, a stream-table join is not windowed and enriches each stream record with the current table value for its key.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

A KStream-KStream join correlates two event streams, so it must be windowed: Kafka Streams buffers records from each side in state stores and emits a result when records with the same key fall within the configured join window. A KStream-KTable join is different: the table represents the latest value per key (a changelog materialized in a state store), so each arriving stream record is enriched with the table's current value for that key without any window. Both joins require matching keys and co-partitioned input topics. GlobalKTable is an option for KStream-GlobalKTable joins (which avoid co-partitioning requirements) but is not mandatory for ordinary joins, and joins are not based merely on arrival order.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Joins: stream-stream, stream-table), https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#joining

**Detailed explanation of each option:**

1. ❌ **A. A stream-stream join is never windowed and matches records globally, a stream-table join must always be windowed.**  
   **Incorrect**. This is reversed—stream-stream joins require a window, stream-table joins do not.

2. ❌ **B. Neither join uses a state store, they match purely on arrival order.**  
   **Incorrect**. Joins rely on state stores and key matching, not arrival order.

3. ❌ **C. Both joins require a GlobalKTable and cannot use local state.**  
   **Incorrect**. GlobalKTable is optional, ordinary joins use local state stores.

4. ✅ **D. A stream-stream join must be windowed, buffering records from both sides within the window in state stores, a stream-table join is not windowed and enriches each stream record with the current table value for its key.**  
   **Correct**. Stream-stream joins are windowed, stream-table joins are lookups against current table state.

</details>

## Question 46 (Stream Processing):
In a Kafka Streams application, what is the primary purpose of a state store, and how is it made fault tolerant?

- A. A state store writes directly to an external database to guarantee durability.
- B. A state store is an in-memory cache that is lost on restart and cannot be recovered.
- C. A state store persists data only to the local disk and relies on RAID for durability.
- D. A state store holds local state for stateful operations such as aggregations and joins, and it is backed by a changelog topic in Kafka for fault tolerance.
- E. A state store is replicated synchronously to every other instance of the application in real time.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Streams uses state stores to maintain local state required by stateful operations such as aggregations, windowed computations, and joins. By default these are backed by RocksDB on local disk for fast key-value access. To make the state fault tolerant, Kafka Streams logs every update to the store into a compacted changelog topic in Kafka. If an instance fails or a task is reassigned, the new host restores the state store by replaying the changelog topic, so no state is lost. This design keeps processing local and fast while using Kafka itself as the durable, replicated source of truth for recovery.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams: Architecture Overview" (Local State and changelog topics), https://kafka.apache.org/documentation/streams/

**Detailed explanation of each option:**

1. ❌ **A. A state store writes directly to an external database to guarantee durability.**  
   **Incorrect**. The default stores are local (RocksDB) with Kafka changelogs, not external databases.

2. ❌ **B. A state store is an in-memory cache that is lost on restart and cannot be recovered.**  
   **Incorrect**. State is recoverable by replaying the changelog topic, it is not simply lost.

3. ❌ **C. A state store persists data only to the local disk and relies on RAID for durability.**  
   **Incorrect**. Durability comes from the replicated changelog topic in Kafka, not local RAID.

4. ✅ **D. A state store holds local state for stateful operations such as aggregations and joins, and it is backed by a changelog topic in Kafka for fault tolerance.**  
   **Correct**. Local state stores are backed by compacted changelog topics that allow full recovery on failover.

5. ❌ **E. A state store is replicated synchronously to every other instance of the application in real time.**  
   **Incorrect**. Standby replicas update asynchronously from the changelog, there is no synchronous cross-instance replication.

</details>

## Question 47 (Kafka Producers):
To gauge how well a producer is batching records and how much latency batching adds, which producer client metrics are most relevant?

- A. `UnderReplicatedPartitions`
- B. `request-latency-avg` (average time for a produce request to be acknowledged)
- C. `record-send-rate` (records sent per second)
- D. `record-queue-time-avg` (average time records wait in the send buffer)
- E. `batch-size-avg` (average number of bytes per batch)

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** E, D, B, C

**Explanation:**

Producer performance and batching behavior are observed through producer client metrics. `batch-size-avg` shows the average batch size, indicating how effectively records are being grouped. `record-queue-time-avg` measures how long records sit buffered before being sent, which is influenced by `linger.ms` and `batch.size`. `request-latency-avg` captures the time from sending a produce request to receiving its acknowledgment. `record-send-rate` reports throughput in records per second. `UnderReplicatedPartitions`, in contrast, is a broker-side replication-health metric and is not a producer client metric.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Producer metrics), https://kafka.apache.org/documentation/#producer_monitoring

**Detailed explanation of each option:**

1. ❌ **A. `UnderReplicatedPartitions`**  
   **Incorrect**. This is a broker replication metric, not a producer metric.

2. ✅ **B. `request-latency-avg` (average time for a produce request to be acknowledged)**  
   **Correct**. Measures produce request round-trip time.

3. ✅ **C. `record-send-rate` (records sent per second)**  
   **Correct**. Reports producer throughput.

4. ✅ **D. `record-queue-time-avg` (average time records wait in the send buffer)**  
   **Correct**. Shows buffering latency influenced by linger.ms/batch.size.

5. ✅ **E. `batch-size-avg` (average number of bytes per batch)**  
   **Correct**. Reflects how effectively records are batched.

</details>

## Question 48 (Kafka Setup and Operations):
A client must present its own certificate so the broker can verify its identity (mutual TLS). Which broker-side setting enforces that clients authenticate with a certificate?

- A. `ssl.client.auth=none` on the broker.
- B. `ssl.client.auth=required` on the broker's SSL listener.
- C. `enable.auto.commit=false` on the consumer.
- D. `acks=all` on the producer.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Mutual TLS requires the broker to demand and verify a client certificate during the TLS handshake. Setting `ssl.client.auth=required` on the broker forces clients to present a valid certificate, which the broker validates against its truststore, the certificate's principal can then be used for authorization. `ssl.client.auth=none` disables client authentication, so it is the opposite of what is needed. `acks` and `enable.auto.commit` govern delivery and offset-commit behavior and are unrelated to TLS client authentication.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (TLS mutual authentication), https://kafka.apache.org/documentation/#brokerconfigs_ssl.client.auth

**Detailed explanation of each option:**

1. ❌ **A. `ssl.client.auth=none` on the broker.**  
   **Incorrect**. This disables client certificate authentication.

2. ✅ **B. `ssl.client.auth=required` on the broker's SSL listener.**  
   **Correct**. This forces clients to present a certificate for authentication.

3. ❌ **C. `enable.auto.commit=false` on the consumer.**  
   **Incorrect**. This governs offset commits, not TLS client auth.

4. ❌ **D. `acks=all` on the producer.**  
   **Incorrect**. `acks` controls durability of writes, not authentication.

</details>

## Question 49 (Kafka Setup and Operations):
Which statements about the `kafka-acls` (`kafka-acls.sh`) CLI tool are correct?

- A. `kafka-acls --list --topic orders` shows the ACLs currently defined for that topic.
- B. A suitable authorizer (for example the KRaft `StandardAuthorizer`) must be configured on the brokers for ACLs to be enforced.
- C. `kafka-acls --add --allow-principal User:alice --operation Read --topic orders` grants alice Read on the `orders` topic.
- D. ACLs can target resource types such as Topic, Group, Cluster, and TransactionalId, and operations like Read, Write, Create, and Describe.
- E. ACLs set with `kafka-acls` replace TLS/SASL authentication, so no authentication is needed once ACLs exist.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** C, D, A, B

**Explanation:**

`kafka-acls` manages authorization rules. `--add --allow-principal User:<name> --operation <op>` with a resource flag (e.g. `--topic`) grants a permission, `--deny-principal` creates deny rules, and `--remove` deletes them. ACLs apply to resource types including Topic, Group (consumer groups), Cluster, and TransactionalId, with operations such as Read, Write, Create, Delete, Alter, and Describe. `--list` (optionally scoped by resource) shows the ACLs in effect. Crucially, ACLs are only *enforced* if the brokers run an authorizer — in modern KRaft clusters that is the `StandardAuthorizer` (set via `authorizer.class.name`) — otherwise the rules have no effect. Statement E is false and a dangerous misconception: **authorization is separate from authentication**. ACLs decide *what* an already-identified principal may do, they do not authenticate anyone. You still need TLS/SASL to establish *who* the client is, and typically also set how unauthenticated/unmatched requests are treated.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Securing Kafka — Authorization, kafka-acls), https://kafka.apache.org/documentation/#security_authz

**Detailed explanation of each option:**

1. ✅ **A. `--list` shows defined ACLs.**  
   **Correct**. Lists current rules.

2. ✅ **B. An authorizer (e.g. `StandardAuthorizer`) must be configured.**  
   **Correct**. Without it ACLs aren't enforced.

3. ✅ **C. `--add --allow-principal ... --operation Read --topic`.**  
   **Correct**. Grants a topic permission.

4. ✅ **D. Targets Topic/Group/Cluster/TransactionalId, ops Read/Write/etc.**  
   **Correct**. The authorizable resources and operations.

5. ❌ **E. ACLs replace authentication.**  
   **Incorrect**. Authorization ≠ authentication, TLS/SASL is still required.

</details>

## Question 50 (Programming & Serialization):
In Kafka Streams, what does enabling exactly-once semantics (`processing.guarantee=exactly_once_v2`) ensure for a topology that reads, processes, and writes back to Kafka?

- A. It disables state stores to avoid duplicate state.
- B. It only deduplicates records by key in the output topic.
- C. Reads, state-store updates, and writes to output topics are committed atomically using Kafka transactions, so each input record affects the result exactly once even across failures.
- D. It guarantees exactly-once delivery to external systems such as relational databases automatically.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Exactly-once semantics in Kafka Streams rely on Kafka transactions to commit the consumer offsets, the state-store changelog records, and the output-topic writes as a single atomic unit. If a failure occurs, the transaction is aborted and partial effects are not visible, so reprocessing does not produce duplicates in Kafka. This guarantee applies to data that stays within Kafka (input topics, state, output topics). It does not automatically extend exactly-once to arbitrary external systems, which require their own idempotency or transactional integration. State stores remain in use, they participate in the transaction rather than being disabled.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 (Exactly-Once Semantics) and Ch. 14, https://kafka.apache.org/documentation/streams/core-concepts#streams_processing_guarantee

**Detailed explanation of each option:**

1. ❌ **A. It disables state stores to avoid duplicate state.**  
   **Incorrect**. State stores participate in the transaction, they are not disabled.

2. ❌ **B. It only deduplicates records by key in the output topic.**  
   **Incorrect**. The guarantee is atomic commit, not key-based dedup in the output.

3. ✅ **C. Reads, state-store updates, and writes to output topics are committed atomically using Kafka transactions, so each input record affects the result exactly once even across failures.**  
   **Correct**. Kafka transactions tie offsets, changelog, and output writes into one atomic commit.

4. ❌ **D. It guarantees exactly-once delivery to external systems such as relational databases automatically.**  
   **Incorrect**. External systems need their own idempotent or transactional handling.

</details>

## Question 51 (Kafka Setup and Operations):
Which client-side metric is the standard way to measure how far a Kafka consumer is behind the latest records in its partitions?

- A. `BytesInPerSec`
- B. `MessagesInPerSec`
- C. `records-lag-max`
- D. `ActiveControllerCount`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Consumer lag—the difference between the latest offset in a partition and the consumer's current position—is exposed on the consumer client as `records-lag-max`, the maximum lag across the partitions it is reading. Monitoring this tells you whether a consumer is keeping up with production. `BytesInPerSec` and `MessagesInPerSec` are broker throughput metrics (inbound bytes and produced-message rate), and `ActiveControllerCount` is a controller-health metric, none of these measures consumer lag.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Consumer metrics, lag), `LAST_MINUTE_REVIEW.md`, https://kafka.apache.org/documentation/#consumer_monitoring

**Detailed explanation of each option:**

1. ❌ **A. `BytesInPerSec`**  
   **Incorrect**. This is a broker inbound-throughput metric.

2. ❌ **B. `MessagesInPerSec`**  
   **Incorrect**. This is the broker's produced-message rate, not consumer lag.

3. ✅ **C. `records-lag-max`**  
   **Correct**. It reports the maximum consumer lag across assigned partitions.

4. ❌ **D. `ActiveControllerCount`**  
   **Incorrect**. This indicates controller health, not consumer lag.

</details>

## Question 52 (Kafka Setup and Operations):
Arrange the following steps of a SASL/SCRAM authentication flow for a Kafka client, in the correct order.

- A. The client supplies credentials through its JAAS configuration (`sasl.jaas.config`)
- B. The client sets `security.protocol=SASL_SSL`
- C. Authenticated requests are authorized against the broker's ACLs
- D. The client sets `sasl.mechanism=SCRAM-SHA-256`
- E. The broker authenticates the client against the stored SCRAM credentials

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** B, D, A, E, C

**Explanation:**

A SASL/SCRAM client first chooses a secure transport by setting `security.protocol=SASL_SSL` (SASL for authentication, SSL for encryption in transit). It then selects the SASL mechanism with `sasl.mechanism=SCRAM-SHA-256` (or `SCRAM-SHA-512`) and supplies its username and password via `sasl.jaas.config`. During connection setup the broker performs the SCRAM challenge-response exchange and authenticates the client against the SCRAM credentials stored in Kafka (previously created with `kafka-configs`). Authentication only establishes *who* the client is, each subsequent request is then authorized against the broker's ACLs to decide *what* the client may do. Authentication and authorization are distinct, sequential concerns.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Securing Kafka — SASL, Authorization), https://kafka.apache.org/documentation/#security_sasl_scram

**Detailed explanation of each option:**

- **B. Set `security.protocol=SASL_SSL`** — Step 1: selects SASL auth over an encrypted channel.
- **D. Set `sasl.mechanism=SCRAM-SHA-256`** — Step 2: picks the SCRAM mechanism.
- **A. Supply credentials via `sasl.jaas.config`** — Step 3: provides the username/password.
- **E. Broker authenticates against stored SCRAM credentials** — Step 4: verifies identity.
- **C. Requests authorized against ACLs** — Step 5: authorization follows authentication.

</details>

## Question 53 (Kafka Setup and Operations):
Which statements about securing a Kafka cluster are correct?

- A. `security.protocol=PLAINTEXT` encrypts traffic using a shared password.
- B. SASL provides authentication mechanisms such as GSSAPI (Kerberos), PLAIN, and SCRAM.
- C. Enabling TLS encryption automatically authenticates and authorizes all clients without any further configuration.
- D. TLS can be used to encrypt data in transit between clients and brokers and between brokers.
- E. Authorization in Kafka is handled separately from authentication, via an authorizer evaluating ACLs.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, B, E

**Explanation:**

Kafka security has distinct layers. TLS encrypts data in transit on client-broker and inter-broker connections and can optionally provide mutual authentication. SASL supplies pluggable authentication mechanisms, including GSSAPI/Kerberos, PLAIN, and SCRAM. Authentication (who you are) is separate from authorization (what you may do), the latter is enforced by an authorizer that evaluates ACLs. Merely enabling TLS encryption does not by itself authorize clients—authorization still requires ACLs. `PLAINTEXT` means no encryption and no authentication at all, it does not use a shared password to encrypt traffic.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Encryption, Authentication, Authorization), https://kafka.apache.org/documentation/#security

**Detailed explanation of each option:**

1. ❌ **A. `security.protocol=PLAINTEXT` encrypts traffic using a shared password.**  
   **Incorrect**. PLAINTEXT provides neither encryption nor authentication.

2. ✅ **B. SASL provides authentication mechanisms such as GSSAPI (Kerberos), PLAIN, and SCRAM.**  
   **Correct**. These are standard SASL mechanisms supported by Kafka.

3. ❌ **C. Enabling TLS encryption automatically authenticates and authorizes all clients without any further configuration.**  
   **Incorrect**. Encryption alone does not authorize, ACLs are still required.

4. ✅ **D. TLS can be used to encrypt data in transit between clients and brokers and between brokers.**  
   **Correct**. TLS protects client-broker and inter-broker traffic.

5. ✅ **E. Authorization in Kafka is handled separately from authentication, via an authorizer evaluating ACLs.**  
   **Correct**. Authentication and authorization are distinct layers.

</details>

## Question 54 (Kafka Internals):
In a modern KRaft-based Kafka cluster, what is the controller responsible for, and what metadata does it manage and where is that metadata stored?

- A. The controller is responsible for running Kafka Connect tasks and Kafka Streams topologies.
- B. Cluster metadata is kept only in each broker's local memory with no durable, replicated source of truth.
- C. The active controller manages cluster metadata — broker registrations and liveness, topic/partition assignments, leader elections for partitions, and ACL/config changes — and persists this metadata as a replicated event log in the internal `__cluster_metadata` topic, which brokers follow to stay in sync.
- D. The controller stores each topic's record payloads (the actual messages) and serves them to consumers directly.
- E. In KRaft, cluster metadata is stored in ZooKeeper, which the controller updates on every change.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The controller is the component that owns the cluster's **metadata and coordination**, not its message data. The active controller tracks broker registration and liveness (via heartbeats), topic and partition assignments, the ISR, partition leader elections and failover, and administrative changes such as topic creation/deletion, configuration updates, and ACLs. In KRaft mode this metadata is modeled as an ordered, replicated **event log** stored in the internal `__cluster_metadata` topic, managed by the controller quorum using the Raft protocol, the active controller is the Raft leader that writes records to this log, and every broker replays the log to keep an up-to-date in-memory view of the cluster (replacing the old ZooKeeper-based mechanism, which was removed in Kafka 4.0). This design gives a single durable, replicated source of truth and fast failover. The other options are wrong: the controller does not store message payloads (that is the partition logs on brokers — B), metadata is durable and replicated rather than memory-only (C), KRaft specifically eliminates ZooKeeper (D), and Connect/Streams workloads run in their own processes, not in the controller (E).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 (Kafka Internals — The Controller), KIP-500 / KRaft, https://kafka.apache.org/documentation/#kraft

**Detailed explanation of each option:**

1. ❌ **A. Controller runs Connect tasks and Streams topologies.**  
   **Incorrect**. Those run in separate processes, unrelated to the controller.

2. ❌ **B. Metadata only in local memory, no durable source of truth.**  
   **Incorrect**. It is a durable, replicated Raft log, brokers cache it in memory.

3. ✅ **C. Controller manages cluster metadata, persisted in the `__cluster_metadata` log that brokers follow.**  
   **Correct**. This is exactly the controller's role and where KRaft metadata lives.

4. ❌ **D. Controller stores and serves message payloads.**  
   **Incorrect**. Message data lives in the partition logs on brokers, not in the controller.

5. ❌ **E. KRaft stores metadata in ZooKeeper.**  
   **Incorrect**. KRaft removed ZooKeeper, metadata is the `__cluster_metadata` log.

</details>

## Question 55 (Kafka Connect):
Arrange the following steps that occur when a source connector is created and started on a Kafka Connect worker, in the correct order.

- A. Each Task polls the external source and produces records to Kafka topics
- B. The Connector generates a set of task configurations
- C. You submit the connector configuration to the worker's REST API (`POST /connectors`)
- D. The worker commits source offsets to the Connect offsets topic
- E. The worker instantiates the Connector class and starts its Tasks

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** C, E, B, A, D

**Explanation:**

A connector lifecycle begins when you POST its configuration to the Connect REST API. The worker instantiates the configured `Connector` class, which is responsible not for moving data but for dividing the work: it generates one or more task configurations (for example, one per table or per partition range). The worker then starts those `Task` instances, which do the actual data movement — a source task polls the external system (`SourceTask.poll()`) and returns records that Connect produces to the target Kafka topics. As records are delivered, the worker periodically commits the source offsets to the internal Connect offsets topic so the connector can resume from where it left off after a restart or rebalance. The Connector plans the work, the Tasks execute it.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Kafka Connect — Connectors and Tasks), https://kafka.apache.org/documentation/#connect

**Detailed explanation of each option:**

- **C. Submit config to the REST API** — Step 1: registers the connector with the cluster.
- **E. Worker instantiates the Connector and starts Tasks** — Step 2: Connect sets up the runtime objects.
- **B. Connector generates task configurations** — Step 3: the Connector divides the work into tasks.
- **A. Tasks poll the source and produce records** — Step 4: the actual data movement.
- **D. Worker commits source offsets** — Step 5: progress is recorded for fault tolerance.

</details>

## Question 56 (Kafka Consumers):
Which approaches are appropriate for handling errors (including "poison pill" records) when consuming from Kafka?

- A. For deserialization failures, use an error-handling deserializer (e.g. `ErrorHandlingDeserializer`) so a single unparseable record does not block the partition.
- B. Wrap record processing in try/catch so one bad record does not crash the whole consumer.
- C. Apply a retry-with-backoff policy for transient failures before giving up on a record.
- D. Always skip offset commits entirely so failed records are retried forever in a tight loop with no backoff.
- E. Route records that repeatedly fail processing to a dead letter queue (DLQ) topic.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, E, A, C

**Explanation:**

Robust consumers isolate failures so a single bad record cannot take down the application or permanently stall a partition. Wrapping processing in try/catch lets you handle a bad record (log it, divert it) and continue. A dead letter queue — a separate topic where records that exhaust their retries are sent — is the standard pattern for quarantining "poison pill" messages while keeping the main flow moving. Deserialization failures are especially dangerous because they can block a partition before your code runs, an error-handling deserializer catches the parse exception and lets you skip or divert the record instead of crashing. Transient errors (a brief downstream outage) should be retried with backoff before the record is abandoned. Option D is bad practice: never-committing and tight-looping with no backoff creates an infinite hot loop that blocks progress and hammers resources — it is the opposite of good error handling.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 & Ch. 7 (Handling errors, reliability), Confluent error-handling / DLQ patterns

**Detailed explanation of each option:**

1. ✅ **A. Error-handling deserializer for parse failures.**  
   **Correct**. Prevents a poison pill from blocking the partition.

2. ✅ **B. try/catch around processing.**  
   **Correct**. Isolates per-record failures.

3. ✅ **C. Retry-with-backoff for transient failures.**  
   **Correct**. Appropriate for recoverable errors.

4. ❌ **D. Never commit and retry forever with no backoff.**  
   **Incorrect**. Creates an infinite hot loop and blocks progress.

5. ✅ **E. Dead letter queue for repeated failures.**  
   **Correct**. Standard quarantine pattern.

</details>

## Question 57 (Stream Processing):
What is the difference between a KStream and a KTable in Kafka Streams?

- A. A KStream is always backed by a state store, a KTable never is.
- B. A KStream is an unbounded record stream where each record is an independent event, a KTable is a changelog where each record is an update (upsert) to a value keyed by its key.
- C. A KStream retains only the latest value per key, a KTable keeps every event.
- D. There is no functional difference, the names are interchangeable.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

A KStream models an unbounded sequence of independent events, where two records with the same key are both meaningful facts (for example, two purchases by the same customer). A KTable models a changelog stream interpreted as a table: each record is an insert or update for its key, and only the latest value per key is the current state. This table-like view is materialized in a state store. The two abstractions support a stream-table duality central to Kafka Streams, and choosing the right one determines how records with repeated keys are interpreted.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 (Stream-table duality), https://kafka.apache.org/documentation/streams/core-concepts

**Detailed explanation of each option:**

1. ❌ **A. A KStream is always backed by a state store, a KTable never is.**  
   **Incorrect**. KTables are materialized in state stores, plain KStreams are not inherently stateful.

2. ✅ **B. A KStream is an unbounded record stream where each record is an independent event, a KTable is a changelog where each record is an update (upsert) to a value keyed by its key.**  
   **Correct**. This is the core stream-table distinction in Kafka Streams.

3. ❌ **C. A KStream retains only the latest value per key, a KTable keeps every event.**  
   **Incorrect**. This is reversed: the KTable keeps the latest per key.

4. ❌ **D. There is no functional difference, the names are interchangeable.**  
   **Incorrect**. They differ fundamentally in how repeated keys are interpreted.

</details>

## Question 58 (Kafka Consumers):
Which statements about the consumer partition-assignment strategies (assignors) configured via `partition.assignment.strategy` are correct?

- A. `CooperativeStickyAssignor` enables incremental cooperative rebalancing, so consumers need not stop processing all partitions during a rebalance.
- B. `StickyAssignor` aims for a balanced assignment while minimizing partition movement between rebalances.
- C. `RoundRobinAssignor` distributes all subscribed partitions across consumers in round-robin order, typically producing a more even spread.
- D. The assignment strategy is decided and enforced by the brokers, not the consumer clients.
- E. `RangeAssignor` assigns partitions per topic as contiguous ranges to consumers, which can lead to uneven load when topics have few partitions.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** E, C, B, A

**Explanation:**

Kafka lets a consumer group choose how partitions are divided among members via the `partition.assignment.strategy` config, and ships several built-in assignors. `RangeAssignor` (the historical default) works per topic: it lays out each topic's partitions and assigns contiguous ranges to consumers in order — simple, but it can skew load when a topic has few partitions relative to consumers. `RoundRobinAssignor` takes all partitions the group subscribes to and deals them out round-robin, usually giving a more even distribution. `StickyAssignor` balances the assignment while deliberately keeping partitions on the same consumers across rebalances where possible, reducing churn. `CooperativeStickyAssignor` adds **incremental cooperative rebalancing**: instead of every consumer revoking all partitions (the "stop-the-world" eager protocol), only the partitions that must move are revoked, so the rest keep being processed — this is the modern recommended strategy. Statement D is wrong: the assignment is computed by the **group leader (a consumer)** using the configured assignor during the rebalance protocol, the broker's group coordinator orchestrates membership but does not itself decide the partition assignment.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (Consumer groups, partition assignment, rebalancing), https://kafka.apache.org/documentation/#consumerconfigs_partition.assignment.strategy

**Detailed explanation of each option:**

1. ✅ **A. `CooperativeStickyAssignor` — incremental cooperative rebalancing.**  
   **Correct**. Avoids stop-the-world revocation of all partitions.

2. ✅ **B. `StickyAssignor` — balanced while minimizing movement.**  
   **Correct**. Reduces churn between rebalances.

3. ✅ **C. `RoundRobinAssignor` — round-robin across all partitions, more even.**  
   **Correct**. Spreads partitions evenly.

4. ❌ **D. Brokers decide and enforce the strategy.**  
   **Incorrect**. The group leader (a consumer) computes the assignment, the coordinator only manages membership.

5. ✅ **E. `RangeAssignor` — per-topic contiguous ranges, can be uneven.**  
   **Correct**. Range-based per topic.

</details>

## Question 59 (Programming & Serialization):
A topic's subject is set to the default `BACKWARD` compatibility. Which schema changes are allowed under BACKWARD compatibility?

- A. Removing a field.
- B. Adding a new required field without a default value.
- C. Widening a field's type via Avro promotion (for example, int to long).
- D. Adding a new field that has a default value.
- E. Renaming a record without using aliases.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, A, C

**Explanation:**

BACKWARD compatibility (the default) means a consumer using the new schema can read data written with the previous schema. Allowed changes are: adding a field that has a default value (so old data missing the field still deserializes), removing a field (the new reader simply ignores it), and widening a type through Avro's numeric promotion such as int to long. Adding a new required field without a default breaks backward compatibility, because old data has no value for the mandatory field. Renaming a record (or field) without aliases is a breaking change because the reader can no longer match it.

Source: `9.schema-registry/schema-registry-summary.md` (Schema Evolution Support, Schema Compatibility), Kafka: The Definitive Guide 2nd ed. Ch. 3

**Detailed explanation of each option:**

1. ✅ **A. Removing a field.**  
   **Correct**. Under BACKWARD a field can be removed, the new reader ignores it.

2. ❌ **B. Adding a new required field without a default value.**  
   **Incorrect**. This breaks backward compatibility since old data has no value for it.

3. ✅ **C. Widening a field's type via Avro promotion (for example, int to long).**  
   **Correct**. Numeric promotion such as int to long is backward compatible.

4. ✅ **D. Adding a new field that has a default value.**  
   **Correct**. The default lets the new reader handle old data lacking the field.

5. ❌ **E. Renaming a record without using aliases.**  
   **Incorrect**. Renaming without aliases is a breaking change.

</details>

## Question 60 (Kafka Consumers):
Which statements about committing consumer group offsets are correct?

- A. Committed offsets are stored in the internal `__consumer_offsets` topic.
- B. Committing an offset before processing the corresponding records gives at-least-once semantics.
- C. With `enable.auto.commit=true`, offsets are committed automatically on a timer during `poll()`.
- D. `commitSync()` retries on retriable errors and blocks until it succeeds or fails, `commitAsync()` does not retry by default.
- E. A committed offset points to the next record the consumer should read, not the last one it processed.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, C, E, D

**Explanation:**

Consumer offsets are persisted in Kafka's internal compacted `__consumer_offsets` topic, keyed by group/topic/partition. With auto-commit enabled, the client commits the latest polled offsets automatically on an interval (`auto.commit.interval.ms`) during calls to `poll()`. A committed offset is the position of the *next* record to consume (one past the last processed record), which is why resuming starts cleanly after the last committed message. On delivery semantics, committing *after* processing yields at-least-once (a crash before commit reprocesses records), whereas committing *before* processing yields at-most-once (records may be skipped) — so option D is the reverse of the truth. `commitSync()` blocks and retries retriable failures until it succeeds or gives up, `commitAsync()` fires without blocking and does not retry automatically, trading reliability for throughput.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (Committing Offsets, commitSync/commitAsync), https://kafka.apache.org/documentation/#consumerconfigs

**Detailed explanation of each option:**

1. ✅ **A. Offsets stored in `__consumer_offsets`.**  
   **Correct**. The internal topic holds committed offsets - a compacted internal topic, sharded by consumer group hash across its partitions..

2. ❌ **B. Committing before processing = at-least-once.**  
   **Incorrect**. Committing before processing is at-most-once, committing after is at-least-once.

3. ✅ **C. Auto-commit on a timer during `poll()`.**  
   **Correct**. With `enable.auto.commit=true`, the consumer commits the offset returned by the previous poll() call when poll() is invoked again, subject to auto.commit.interval.ms (default 5000ms). The timing is tied to the poll loop, not a background thread.

4. ✅ **D. `commitSync` retries/blocks, `commitAsync` does not retry by default.**  
   **Correct**. This is the key reliability-vs-throughput trade-off between them.

5. ✅ **E. Committed offset = next record to read.**  
   **Correct**. A committed offset of X means “I have processed up to X-1, next read should start at X.” So commitSync(offset + 1) is the correct pattern when committing manually per-record.

</details>

## Question 61 (Kafka Producers):
What are Kafka record headers, and how can a producer use them?

- A. Headers are optional key-value metadata attached to a record (separate from the key and value), which a producer can add via the `ProducerRecord` to carry information such as trace IDs or content type.
- B. Headers are a mandatory part of every record that replaces the key.
- C. Headers are broker-only fields that clients cannot set or read.
- D. Headers are stored in a separate topic and referenced by ID.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka record headers are optional metadata carried alongside each record, independent of the record key and value. Each header is a key (a string) with a byte-array value, and a record may have multiple headers. A producer attaches them when constructing a `ProducerRecord`, which is useful for cross-cutting concerns such as correlation/trace IDs, content type, source system, or routing hints—without polluting the business payload. Headers are not mandatory, do not replace the key, are fully readable and writable by clients, and are stored inline with the record (not in a separate topic). Consumers and interceptors, as well as Connect SMTs, can read and act on them.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 (Headers), https://kafka.apache.org/documentation/#recordheader

**Detailed explanation of each option:**

1. ✅ **A. Headers are optional key-value metadata attached to a record (separate from the key and value), which a producer can add via the `ProducerRecord` to carry information such as trace IDs or content type.**  
   **Correct**. Headers are optional per-record metadata set on the `ProducerRecord`.

2. ❌ **B. Headers are a mandatory part of every record that replaces the key.**  
   **Incorrect**. Headers are optional and do not replace the key.

3. ❌ **C. Headers are broker-only fields that clients cannot set or read.**  
   **Incorrect**. Producers set them and consumers read them.

4. ❌ **D. Headers are stored in a separate topic and referenced by ID.**  
   **Incorrect**. Headers are stored inline with the record.

</details>

## Question 62 (Kafka Setup and Operations):
Which broker-level metrics are important indicators of cluster replication and controller health?

- A. `OfflinePartitionsCount`
- B. `UnderReplicatedPartitions`
- C. `ActiveControllerCount`
- D. `UnderMinIsrPartitionCount`
- E. `records-lag-max`

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, A, C, D

**Explanation:**

Several broker-side metrics signal replication and controller health. `UnderReplicatedPartitions` counts partitions whose in-sync replica set is smaller than the configured replication factor, a key durability warning. `OfflinePartitionsCount` shows partitions with no available leader, meaning they are unavailable. `ActiveControllerCount` should sum to exactly 1 across the cluster—more or fewer indicates a controller problem. `UnderMinIsrPartitionCount` tracks partitions that have fewer in-sync replicas than `min.insync.replicas`, which can block `acks=all` writes. `records-lag-max`, by contrast, is a consumer client metric that measures how far a consumer is behind, not a broker replication/controller metric.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Broker metrics), `LAST_MINUTE_REVIEW.md` (Metrics), https://kafka.apache.org/documentation/#monitoring

**Detailed explanation of each option:**

1. ✅ **A. `OfflinePartitionsCount`**  
   **Correct**. Counts partitions with no leader, i.e., unavailable.

2. ✅ **B. `UnderReplicatedPartitions`**  
   **Correct**. Indicates partitions with fewer in-sync replicas than the replication factor.

3. ✅ **C. `ActiveControllerCount`**  
   **Correct**. Should total exactly 1 across the cluster, otherwise a controller issue exists.

4. ✅ **D. `UnderMinIsrPartitionCount`**  
   **Correct**. Tracks partitions below `min.insync.replicas`, which can block acks=all writes.

5. ❌ **E. `records-lag-max`**  
   **Incorrect**. This is a consumer client metric, not a broker replication/controller metric.

</details>

## Question 63 (Programming & Serialization):
What is the primary role of Confluent Schema Registry in a Kafka system that uses Avro?

- A. It stores and manages schemas centrally, assigns each schema an ID, and enforces compatibility rules so producers and consumers agree on the data format.
- B. It stores the actual message payloads so brokers do not have to.
- C. It compresses Avro messages to reduce their size on the broker.
- D. It replaces the need for producers and consumers to deserialize data.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Schema Registry is a centralized service that stores Avro (as well as JSON Schema and Protobuf) schemas, assigns each registered schema a unique ID, and enforces compatibility rules when new schema versions are registered. Producers send only a small schema ID (plus a magic byte) with each message rather than the full schema, and consumers use that ID to fetch the matching schema for deserialization. This keeps messages compact and guarantees that producers and consumers agree on the structure of the data, enabling safe schema evolution. It does not store message payloads (those stay in Kafka), does not compress data, and does not eliminate deserialization.

Source: `9.schema-registry/schema-registry-summary.md` (Overview, Schema Registry Integration with Kafka), Kafka: The Definitive Guide 2nd ed. Ch. 3 (Serializers, Schema Registry)

**Detailed explanation of each option:**

1. ✅ **A. It stores and manages schemas centrally, assigns each schema an ID, and enforces compatibility rules so producers and consumers agree on the data format.**  
   **Correct**. Centralized schema storage with IDs and compatibility enforcement is the core role.

2. ❌ **B. It stores the actual message payloads so brokers do not have to.**  
   **Incorrect**. Message payloads remain in Kafka, Schema Registry stores only schemas.

3. ❌ **C. It compresses Avro messages to reduce their size on the broker.**  
   **Incorrect**. Size reduction comes from sending a schema ID, not from compression by the registry.

4. ❌ **D. It replaces the need for producers and consumers to deserialize data.**  
   **Incorrect**. Clients still serialize and deserialize, the registry supplies the schema.

</details>

## Question 64 (Kafka Producers):
Which statements about header ordering, duplicates, and size/limit considerations are correct?

- A. There is a dedicated broker setting `max.header.bytes` that caps the total size of a record's headers independently of the message size limit.
- B. Within one record, headers keep the order in which they were added, and `Headers.lastHeader("k")` returns the most recently added header for that key.
- C. Large or numerous headers increase per-record overhead and reduce effective batch/throughput, so keep header metadata small.
- D. Headers are compressed and retained separately from the record value in their own index.
- E. Headers count toward the total record size, so they are subject to the same `max.request.size` (producer) and `message.max.bytes`/`max.message.bytes` (broker/topic) limits as the rest of the record.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, B, C

**Explanation:**

Headers are serialized **inline as part of the record**, so their bytes count toward the overall record size and are governed by the same limits as the key and value: the producer's `max.request.size` and the broker/topic `message.max.bytes` / `max.message.bytes` (a record whose key + value + headers + overhead exceeds the limit is rejected with `RecordTooLargeException`). Because headers are an ordered list, they preserve insertion order, and `lastHeader(key)` returns the last header added for a given key — the expected way to read a logically single-valued header when duplicates might exist. Since headers add per-record overhead, bloating them (many headers or large values) wastes space, inflates each record, and lowers effective batching/throughput, so metadata should be kept small and purposeful. Statement A is false — there is **no** separate `max.header.bytes` broker limit, headers are bounded by the message-size limits, not a dedicated header cap. Statement D is false — headers are part of the record (stored/compressed with it in the log segment), not kept in a separate index.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 & Ch. 6 (Headers, record format, size limits), https://kafka.apache.org/documentation/#brokerconfigs_message.max.bytes

**Detailed explanation of each option:**

1. ❌ **A. A dedicated `max.header.bytes` caps headers.**  
   **Incorrect**. No such separate limit exists, message-size limits apply.

2. ✅ **B. Insertion order preserved, `lastHeader` returns the latest for a key.**  
   **Correct**. Headers are an ordered list with last-wins lookup.

3. ✅ **C. Large/numerous headers raise overhead and cut throughput.**  
   **Correct**. Keep header metadata small.

4. ❌ **D. Headers compressed/retained in a separate index.**  
   **Incorrect**. Headers live inline with the record, not in a separate store.

5. ✅ **E. Headers count toward record size and message-size limits.**  
   **Correct**. They share `max.request.size`/`message.max.bytes`.

</details>

## Question 65 (Programming & Serialization):
Using `KafkaAvroSerializer` with its default settings, what happens when a producer serializes a record whose schema has not yet been registered in Schema Registry?

- A. The broker registers the schema on the producer's behalf.
- B. The serializer silently drops the record.
- C. The full schema text is written into every message alongside the data.
- D. With `auto.register.schemas=true` (the default), the serializer registers the schema, obtains a schema ID, and prepends a magic byte plus the 4-byte ID to the payload.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

By default `auto.register.schemas=true`, so when the `KafkaAvroSerializer` encounters a schema that is not yet registered, it calls the Schema Registry REST API to register it and retrieve the assigned schema ID. The serialized message is then written as a magic byte, the 4-byte schema ID, and the Avro-encoded payload. Consumers read the ID to fetch the correct schema for deserialization. If registration fails (for example, due to an incompatible change), the serializer throws an exception and the record is not produced. The broker is not involved in schema registration, and the full schema text is never embedded in each message—only the compact ID is.

Source: `9.schema-registry/schema-registry-summary.md` (Serializers and Deserializers, auto.register.schemas), Kafka: The Definitive Guide 2nd ed. Ch. 3

**Detailed explanation of each option:**

1. ❌ **A. The broker registers the schema on the producer's behalf.**  
   **Incorrect**. Registration is done by the client serializer, not the broker.

2. ❌ **B. The serializer silently drops the record.**  
   **Incorrect**. It registers the schema or throws on failure, it does not silently drop.

3. ❌ **C. The full schema text is written into every message alongside the data.**  
   **Incorrect**. Only the compact schema ID is written, not the full schema.

4. ✅ **D. With `auto.register.schemas=true` (the default), the serializer registers the schema, obtains a schema ID, and prepends a magic byte plus the 4-byte ID to the payload.**  
   **Correct**. This is the default auto-registration and wire format behavior.

</details>

## Question 66 (Kafka Connect):
Which statements about configuring Kafka Connect connectors and workers are correct?

- A. A connector's `connector.class`, plus its source/sink-specific properties, is submitted as JSON to the Connect REST API.
- B. Converters and the connector class are irrelevant because Connect always sends raw bytes unchanged.
- C. `key.converter` and `value.converter` are worker/connector properties that define how data is (de)serialized (e.g. Avro, JSON, String converters).
- D. `tasks.max` limits the number of tasks a connector may split its work into, which bounds its parallelism.
- E. Sink connectors use `topics` (or `topics.regex`) to declare which Kafka topics they read from.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, C, E, D

**Explanation:**

A connector is configured as JSON specifying its `connector.class` and the properties that class understands (connection URLs, table lists, file paths, topic names, etc.), submitted to the Connect REST API. Converters — `key.converter` and `value.converter` — are a central part of Connect configuration: they translate between Connect's internal data representation and the serialized bytes in Kafka (AvroConverter, JsonConverter, StringConverter, ProtobufConverter), and can be set at the worker level as defaults and overridden per connector. Sink connectors declare their input with `topics` or `topics.regex`. `tasks.max` caps how many tasks a connector divides its work into, which is the primary lever for a connector's parallelism (actual tasks may be fewer if the work can't be split that far). Statement B is wrong — converters are exactly what (de)serialize the data, so they are far from irrelevant.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 (Kafka Connect — configuration, converters, tasks), https://kafka.apache.org/documentation/#connectconfigs

**Detailed explanation of each option:**

1. ✅ **A. `connector.class` + properties submitted as JSON to the REST API.**  
   **Correct**. Standard connector configuration.

2. ❌ **B. Converters/class irrelevant, Connect sends raw bytes.**  
   **Incorrect**. Converters perform the serialization and are essential.

3. ✅ **C. `key.converter`/`value.converter` define (de)serialization.**  
   **Correct**. Converters bridge Connect data and Kafka bytes.

4. ✅ **D. `tasks.max` bounds parallelism.**  
   **Correct**. It caps the number of tasks.

5. ✅ **E. Sink connectors use `topics`/`topics.regex`.**  
   **Correct**. That is how sinks select input topics.

</details>

## Question 67 (Kafka Setup and Operations):
Which statements about the `kafka-producer-perf-test` (`kafka-producer-perf-test.sh`) CLI tool are correct?

- A. It is primarily used to define ACLs for producers.
- B. It is a benchmarking tool that produces a configurable number of records to a topic to measure producer throughput and latency.
- C. There is a corresponding `kafka-consumer-perf-test` tool for benchmarking consumer throughput.
- D. Key options include `--num-records`, `--record-size`, `--throughput` (target records/sec, `-1` for max), and `--producer-props` to pass producer configs like `acks` and `batch.size`.
- E. It reports metrics such as records/sec, MB/sec, and average/percentile latency.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, D, E, C

**Explanation:**

`kafka-producer-perf-test` is a load/benchmark tool: it sends a controlled volume of records to a topic so you can measure and tune producer performance. Common flags are `--topic`, `--num-records`, `--record-size` (payload bytes), `--throughput` (a target rate in records/sec, or `-1` for unthrottled/maximum), and `--producer-props` (to set producer configs such as `acks`, `batch.size`, `linger.ms`, `compression.type`). Its output reports throughput (records/sec and MB/sec) and latency statistics including average and high percentiles (e.g. p95/p99) — ideal for comparing the effect of config changes or hardware. A sibling tool, `kafka-consumer-perf-test`, benchmarks consumer-side throughput. Statement A is false: it has nothing to do with ACLs (that is `kafka-acls`), it only generates producer load.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Performance testing tools), https://kafka.apache.org/documentation/#monitoring

**Detailed explanation of each option:**

1. ❌ **A. Used to define producer ACLs.**  
   **Incorrect**. ACLs are managed by `kafka-acls`.

2. ✅ **B. Benchmarks producer throughput/latency.**  
   **Correct**. A load-generation tool.

3. ✅ **C. `kafka-consumer-perf-test` benchmarks consumers.**  
   **Correct**. The consumer-side counterpart exists.

4. ✅ **D. `--num-records`, `--record-size`, `--throughput`, `--producer-props`.**  
   **Correct**. Its core options.

5. ✅ **E. Reports records/sec, MB/sec, latency percentiles.**  
   **Correct**. Standard benchmark output.

</details>

## Question 68 (Kafka Consumers):
Arrange the following steps of a typical Kafka consumer's lifecycle into the correct order, from startup to committing progress.

- A. `poll()` the broker to fetch a batch of records
- B. Process the records returned by the poll
- C. `subscribe()` to one or more topics
- D. Commit the offsets of the processed records

Arrange the steps in the correct order.

<details>
<summary>Response:</summary>

**Answer:** C, A, B, D

**Explanation:**

A Kafka consumer first `subscribe()`s to the topics it wants to read, this registers it with the group coordinator and triggers partition assignment. It then enters a loop where it calls `poll()` to fetch a batch of records from the assigned partitions, processes those records (your application logic), and finally commits the offsets so that progress is recorded and the consumer can resume from the right place after a restart or rebalance. The poll–process–commit steps repeat continuously, `subscribe()` happens once up front. Committing before processing would risk losing records on failure (at-most-once), so the natural order is subscribe → poll → process → commit.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 (The Poll Loop, Committing Offsets), https://kafka.apache.org/documentation/#consumerapi

**Detailed explanation of each option:**

- **C. `subscribe()` to one or more topics** — Step 1: declares interest in topics and joins the consumer group.
- **A. `poll()` the broker to fetch a batch of records** — Step 2: retrieves the next batch from assigned partitions.
- **B. Process the records returned by the poll** — Step 3: application handles each record.
- **D. Commit the offsets of the processed records** — Step 4: records progress so processing resumes correctly after a restart/rebalance.

</details>

## Question 69 (Kafka Setup and Operations):
Which statements about configuring alerts for a Kafka deployment reflect good practice?

- A. Alert on `UnderReplicatedPartitions > 0` and offline partitions, which indicate replication or availability problems.
- B. The best alerting strategy is to page on every single `INFO` log line to be safe.
- C. Alert on active-controller count not equal to 1 across the cluster, which signals a controller problem.
- D. Alert on growing consumer lag (e.g. `records-lag-max` or `kafka-consumer-groups` lag) so you catch consumers falling behind.
- E. Alert on sustained high request latency and low free disk space on brokers.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, A, C, E

**Explanation:**

Good Kafka alerting focuses on a small set of high-signal health indicators. Consumer lag (via `records-lag-max` or the consumer-groups lag) catches consumers falling behind before it becomes a backlog incident. `UnderReplicatedPartitions > 0` and offline partitions are classic replication/availability alarms — they mean replicas are out of sync or a partition has no leader. The cluster should have exactly one active controller, an active-controller count other than 1 (zero or more than one reported) indicates a controller election problem. Sustained high produce/fetch request latency and low free disk space are strong operational alerts because they precede outages. Statement B is an anti-pattern: paging on every `INFO` line creates alert fatigue and noise, drowning out the actionable signals — alerts should be few, meaningful, and tied to symptoms that require human action.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Monitoring — key metrics and alerting), `LAST_MINUTE_REVIEW.md` (UnderReplicatedPartitions, controller), https://kafka.apache.org/documentation/#monitoring

**Detailed explanation of each option:**

1. ✅ **A. Alert on under-replicated/offline partitions.**  
   **Correct**. Replication/availability risk.

2. ❌ **B. Page on every INFO log line.**  
   **Incorrect**. Causes alert fatigue, alerts must be high-signal.

3. ✅ **C. Alert on active-controller count ≠ 1.**  
   **Correct**. Indicates a controller problem.

4. ✅ **D. Alert on growing consumer lag.**  
   **Correct**. Early warning that consumers lag producers.

5. ✅ **E. Alert on high latency and low disk.**  
   **Correct**. Strong operational early warnings.

</details>

## Question 70 (Kafka Internals):
How does log compaction treat records in a compacted topic, and what is the one record it guarantees to retain per key?

- A. It merges all values for a key into a concatenated record.
- B. It retains at least the latest value for each key, removing older records with the same key, a record with a null value (a tombstone) marks the key for deletion.
- C. It deletes all records older than the retention period regardless of key.
- D. It keeps the first value ever written for each key and discards later updates.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Log compaction guarantees that Kafka retains at least the most recent value for each key within a partition, cleaning up superseded older records with the same key over time. This makes a compacted topic ideal for changelog-style data where you only care about the current state per key (for example, the changelog topics behind Kafka Streams state stores). A record with a null value is a tombstone: it signals deletion of the key and, after a configurable retention period for tombstones, allows the key to be removed entirely. Compaction is distinct from time/size-based deletion, does not keep the oldest value, and never concatenates values.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Cleaning the Log" (Compaction, Tombstones), https://kafka.apache.org/documentation/#compaction

**Detailed explanation of each option:**

1. ❌ **A. It merges all values for a key into a concatenated record.**  
   **Incorrect**. Compaction does not merge values.

2. ✅ **B. It retains at least the latest value for each key, removing older records with the same key, a record with a null value (a tombstone) marks the key for deletion.**  
   **Correct**. Compaction keeps the latest value per key, null-value tombstones delete keys.

3. ❌ **C. It deletes all records older than the retention period regardless of key.**  
   **Incorrect**. That describes time-based deletion, not compaction.

4. ❌ **D. It keeps the first value ever written for each key and discards later updates.**  
   **Incorrect**. Compaction keeps the latest value, not the first.

</details>

## Question 71 (Kafka Setup and Operations):
What does a Kafka ACL (access control list) entry define, and at what level is authorization enforced?

- A. It grants or denies a principal specific operations (such as Read, Write, Describe) on resources (such as a topic or group), enforced by the broker's authorizer.
- B. It encrypts data at rest on the broker's disk.
- C. It controls only ZooKeeper access and has no effect on topic operations.
- D. It defines network routing rules between brokers.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

A Kafka ACL binds a principal (an authenticated identity) to permission to perform operations such as Read, Write, Create, or Describe on a resource like a topic, consumer group, or cluster. The broker's authorizer evaluates these ACLs on each request and allows or denies the action. ACLs are an authorization mechanism and are distinct from encryption (TLS protects data in transit) and from any at-rest encryption. They apply to Kafka operations broadly, not just ZooKeeper, and in KRaft-based clusters authorization is handled by the StandardAuthorizer.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 (Authorization, ACLs), https://kafka.apache.org/documentation/#security_authz

**Detailed explanation of each option:**

1. ✅ **A. It grants or denies a principal specific operations (such as Read, Write, Describe) on resources (such as a topic or group), enforced by the broker's authorizer.**  
   **Correct**. ACLs are principal-operation-resource bindings evaluated by the authorizer.

2. ❌ **B. It encrypts data at rest on the broker's disk.**  
   **Incorrect**. ACLs are about authorization, not encryption.

3. ❌ **C. It controls only ZooKeeper access and has no effect on topic operations.**  
   **Incorrect**. ACLs govern Kafka operations on topics, groups, and the cluster.

4. ❌ **D. It defines network routing rules between brokers.**  
   **Incorrect**. ACLs do not configure network routing.

</details>

## Question 72 (Kafka Setup and Operations):
How are Kafka broker, producer, consumer, and Kafka Streams metrics primarily exposed for monitoring?

- A. Exclusively through ZooKeeper nodes.
- B. Only through the Schema Registry REST API.
- C. Only by parsing the broker's server.log file.
- D. Via JMX (Java Management Extensions), which can be scraped by external monitoring tools.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka components—brokers, producers, consumers, and Kafka Streams applications—expose their metrics through JMX (Java Management Extensions). Monitoring systems connect to these JMX MBeans (or use a JMX exporter) to collect request rates, byte rates, lag, and many other values. While logs are useful for troubleshooting, metrics are not obtained by parsing log files. ZooKeeper is removed in modern (4.x) Kafka and was never the general metrics channel, and Schema Registry's REST API deals with schemas, not Kafka runtime metrics.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 (Monitoring Kafka: JMX), https://kafka.apache.org/documentation/#monitoring

**Detailed explanation of each option:**

1. ❌ **A. Exclusively through ZooKeeper nodes.**  
   **Incorrect**. ZooKeeper is not the metrics channel and is removed in Kafka 4.x.

2. ❌ **B. Only through the Schema Registry REST API.**  
   **Incorrect**. That API serves schemas, not runtime metrics.

3. ❌ **C. Only by parsing the broker's server.log file.**  
   **Incorrect**. Metrics come from JMX, not log parsing.

4. ✅ **D. Via JMX (Java Management Extensions), which can be scraped by external monitoring tools.**  
   **Correct**. JMX is the standard channel for Kafka metrics.

</details>

## Question 73 (Kafka Setup and Operations):
Which statements about the `kafka-topics` (`kafka-topics.sh`) CLI tool are correct?

- A. `kafka-topics --create --topic orders --partitions 6 --replication-factor 3` creates a topic with 6 partitions and a replication factor of 3.
- B. `kafka-topics --alter --topic orders --partitions 12` increases the partition count to 12 (you cannot decrease it).
- C. `kafka-topics --describe --topic orders` shows the partitions, leader, replicas, and in-sync replicas (ISR) for the topic.
- D. In modern Kafka (4.x) the tool connects with `--bootstrap-server`, not `--zookeeper`.
- E. `kafka-topics --alter --replication-factor 5` is the correct way to change an existing topic's replication factor.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, C, B, D

**Explanation:**

`kafka-topics` manages topic lifecycle and metadata. `--create` with `--partitions` and `--replication-factor` provisions a new topic. `--describe` prints each partition's leader, the replica list, and the current ISR, which is the primary way to inspect topic health. `--alter --partitions` can **increase** the partition count (never decrease it — reducing partitions is unsupported). In modern Kafka (KRaft, 4.x) all admin CLIs talk to the cluster through `--bootstrap-server`, the old `--zookeeper` flag is gone because ZooKeeper was removed in 4.0. Statement E is false: replication factor is **not** changed via `kafka-topics --alter`, you must perform a partition reassignment with `kafka-reassign-partitions` using a JSON plan that lists the new replica set.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Administering Kafka — kafka-topics), https://kafka.apache.org/documentation/#basic_ops_add_topic

**Detailed explanation of each option:**

1. ✅ **A. `--create ... --partitions 6 --replication-factor 3`.**  
   **Correct**. Standard topic creation flags.

2. ✅ **B. `--alter --partitions 12` increases (can't decrease).**  
   **Correct**. Partition count is one-directional.

3. ✅ **C. `--describe` shows leader/replicas/ISR.**  
   **Correct**. Primary inspection command.

4. ✅ **D. Uses `--bootstrap-server` in 4.x, not `--zookeeper`.**  
   **Correct**. ZooKeeper flags are removed.

5. ❌ **E. `--alter --replication-factor` changes RF.**  
   **Incorrect**. RF changes require `kafka-reassign-partitions`.

</details>

## Question 74 (Kafka Core Concepts):
Which statements correctly describe Kafka's end-to-end delivery guarantees?

- A. Exactly-once is achieved simply by setting `acks=1` on the producer.
- B. At-most-once means a message may be lost but is never redelivered.
- C. At-least-once means a message is never lost but may be redelivered (duplicates possible).
- D. At-least-once typically results from committing consumer offsets after processing records.
- E. Exactly-once (EOS) in Kafka is achieved with an idempotent producer plus transactions, so records are neither lost nor duplicated.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, C, E, D

**Explanation:**

Kafka supports three delivery semantics. At-most-once trades reliability for simplicity: a record may be lost (for example if offsets are committed before processing) but is never delivered twice. At-least-once never loses a record but may deliver it more than once — this is the default behavior when you commit offsets *after* processing, because a crash before the commit causes reprocessing. Exactly-once semantics (EOS) eliminate both loss and duplication, in Kafka this is built from the idempotent producer (`enable.idempotence=true`, dedup via producer id + sequence numbers) combined with transactions that atomically write records and commit consumer offsets together. Setting `acks=1` only controls leader acknowledgment and does not provide exactly-once — E is false, EOS requires idempotence/transactions, not just an ack level.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 7 & Ch. 8 (Reliable Data Delivery, Exactly-Once Semantics), https://kafka.apache.org/documentation/#semantics

**Detailed explanation of each option:**

1. ❌ **A. Exactly-once via `acks=1`.**  
   **Incorrect**. `acks=1` is just leader-ack, EOS needs idempotence/transactions.

2. ✅ **B. At-most-once: may be lost, never redelivered.**  
   **Correct**. Definition of at-most-once.

3. ✅ **C. At-least-once: never lost, may be duplicated.**  
   **Correct**. Definition of at-least-once.

4. ✅ **D. At-least-once from committing offsets after processing.**  
   **Correct**. Commit-after-process is the standard at-least-once pattern.

5. ✅ **E. EOS = idempotent producer + transactions.**  
   **Correct**. This is how Kafka achieves exactly-once.

</details>

## Question 75 (Kafka Setup and Operations):
Which statements about the `kafka-reassign-partitions` (`kafka-reassign-partitions.sh`) CLI tool are correct?

- A. It moves partition replicas between brokers and is the correct way to change an existing topic's replica assignment (including replication factor).
- B. It deletes a topic's data as part of the reassignment.
- C. It can throttle the replication traffic during a reassignment to limit the impact on the cluster.
- D. It is used to rebalance partitions onto newly added brokers (which are not populated automatically).
- E. It can `--generate` a candidate reassignment plan, `--execute` it from a JSON file, and `--verify` that the reassignment completed.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, E, C, D

**Explanation:**

`kafka-reassign-partitions` changes which brokers hold a partition's replicas. It is the proper mechanism to move replicas and to change an existing topic's **replication factor** (by adding or removing broker IDs in the replica list) — something `kafka-topics --alter` cannot do. Its workflow has three phases: `--generate` proposes a plan (given a topics-to-move file and a target broker list), `--execute` applies a reassignment JSON, and `--verify` checks whether it finished. Because moving replicas copies data across the network, the tool supports a `--throttle` to cap replication bandwidth and protect cluster performance. It is also the standard way to **rebalance partitions onto newly added brokers**, since adding brokers does not automatically relocate existing partitions. Statement B is false: reassignment relocates replicas, it does not delete topic data (deletion is `kafka-topics --delete`).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Reassigning partitions, throttling), https://kafka.apache.org/documentation/#basic_ops_cluster_expansion

**Detailed explanation of each option:**

1. ✅ **A. Moves replicas, changes replication factor.**  
   **Correct**. The tool for replica assignment/RF changes.

2. ❌ **B. Deletes topic data.**  
   **Incorrect**. It relocates replicas, not deletes data.

3. ✅ **C. Can throttle replication traffic.**  
   **Correct**. `--throttle` limits impact.

4. ✅ **D. Rebalances partitions onto new brokers.**  
   **Correct**. New brokers aren't populated automatically.

5. ✅ **E. `--generate`, `--execute`, `--verify` workflow.**  
   **Correct**. The three reassignment phases.

</details>

## Question 76 (Programming & Serialization):
Which statements about serializing and deserializing Kafka messages in application code are correct?

- A. The consumer's deserializer must be compatible with the producer's serializer for the data to be read correctly.
- B. `KafkaAvroSerializer`/`KafkaAvroDeserializer` integrate with Schema Registry to register and fetch schemas automatically.
- C. Kafka brokers deserialize and re-serialize each record, so the client serializers are irrelevant.
- D. The serializer turns an object into the `byte[]` stored in Kafka, the deserializer reconstructs the object from those bytes.
- E. A producer is configured with `key.serializer` and `value.serializer`, a consumer with `key.deserializer` and `value.deserializer`.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** E, D, A, B

**Explanation:**

Serialization is a purely client-side concern in Kafka. A producer declares `key.serializer` and `value.serializer`, the matching consumer declares `key.deserializer` and `value.deserializer`. A serializer converts the application object into the `byte[]` that Kafka stores (Kafka itself only ever sees opaque bytes), and the deserializer reverses that on read. The producer's and consumer's (de)serializers must therefore be compatible — using a `StringSerializer` on the way in and expecting an `IntegerDeserializer` on the way out would fail or corrupt data. For schema-managed formats, `KafkaAvroSerializer`/`KafkaAvroDeserializer` (and the Protobuf/JSON-Schema equivalents) talk to Schema Registry to register the writer schema and fetch it by ID when reading, enabling evolution. Statement C is false — brokers never deserialize record payloads, they store and forward raw bytes, which is exactly why client serializers matter and why they must match.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 & Ch. 4 (Serializers/Deserializers), `9.schema-registry/schema-registry-summary.md`

**Detailed explanation of each option:**

1. ✅ **A. Consumer deserializer must match producer serializer.**  
   **Correct**. Otherwise data can't be read.

2. ✅ **B. Avro (de)serializers integrate with Schema Registry.**  
   **Correct**. Auto register/fetch schemas.

3. ❌ **C. Brokers deserialize/re-serialize records.**  
   **Incorrect**. Brokers handle opaque bytes only.

4. ✅ **D. Serializer → bytes, deserializer → object.**  
   **Correct**. The core round-trip.

5. ✅ **E. Producer has serializers, consumer has deserializers.**  
   **Correct**. The paired client configs.

</details>

## Question 77 (Kafka Setup and Operations):
Match each task to the correct Kafka CLI tool. Which statements are correct?

- A. `kafka-consumer-groups` describes consumer groups and shows per-partition lag, and can reset offsets.
- B. `kafka-topics` creates, lists, describes, and alters topics (including increasing partition count).
- C. `kafka-reassign-partitions` is used to permanently delete a topic's data.
- D. `kafka-console-producer` and `kafka-console-consumer` produce and consume records from the command line for quick testing.
- E. `kafka-configs` views and alters dynamic configurations for topics, brokers, users, and clients.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** B, D, A, E

**Explanation:**

Kafka ships a set of CLI tools that appear frequently on the exam. `kafka-topics` manages topic lifecycle and metadata — create, list, describe, and `--alter` (including increasing partitions). `kafka-console-producer` and `kafka-console-consumer` are quick manual produce/consume tools useful for testing and debugging. `kafka-consumer-groups` describes groups, shows current offset, log-end offset, and **lag** per partition, and can reset offsets (`--reset-offsets`). `kafka-configs` reads and dynamically alters configuration entities — topics, brokers, users, and clients (e.g. quotas, retention). Statement C misdescribes `kafka-reassign-partitions`: it moves partition replicas between brokers and changes replica assignments/throttles during rebalancing, it does **not** delete topic data (that is `kafka-topics --delete`).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Administering Kafka — CLI tools), https://kafka.apache.org/documentation/#operations

**Detailed explanation of each option:**

1. ✅ **A. `kafka-consumer-groups` describes groups and shows lag.**  
   **Correct**. Also resets offsets.

2. ✅ **B. `kafka-topics` creates/lists/describes/alters topics.**  
   **Correct**. The topic-management tool.

3. ❌ **C. `kafka-reassign-partitions` deletes topic data.**  
   **Incorrect**. It reassigns replicas across brokers, it does not delete data.

4. ✅ **D. console producer/consumer for quick testing.**  
   **Correct**. Manual produce/consume from the CLI.

5. ✅ **E. `kafka-configs` views/alters dynamic configs.**  
   **Correct**. Works on topics, brokers, users, clients.

</details>

## Question 78 (Kafka Setup and Operations):
Which statements about the `kafka-consumer-groups` (`kafka-consumer-groups.sh`) CLI tool are correct?

- A. `kafka-consumer-groups --reset-offsets --to-earliest --group app1 --topic orders --execute` resets the group's committed offsets to the beginning.
- B. `kafka-consumer-groups --list` lists the consumer groups known to the cluster.
- C. `kafka-groups.sh` is the standard tool for consumer group operations.
- D. `--reset-offsets` requires the consumer group to be active (members online) to take effect.
- E. `kafka-consumer-groups --describe --group app1` shows CURRENT-OFFSET, LOG-END-OFFSET, and LAG per partition, plus the assigned member/host.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, A

**Explanation:**

`kafka-consumer-groups` is the group-management and lag tool. `--list` enumerates all known groups. `--describe --group <id>` prints per-partition CURRENT-OFFSET, LOG-END-OFFSET, LAG (log-end minus current), and the member/consumer-id and host owning each partition — the standard way to diagnose lag. `--reset-offsets` repositions a group's committed offsets, with targets like `--to-earliest`, `--to-latest`, `--to-offset`, `--shift-by`, or `--to-datetime`, it supports a dry-run default and requires `--execute` to actually apply. Statement D is the opposite of the truth: resetting offsets requires the group to be **inactive** (no active members) — you cannot reset offsets of a group that currently has live consumers, or the command is rejected. Statement C is false because there is no `kafka-groups.sh`, the correct tool is `kafka-consumer-groups.sh`.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 12 (Consumer groups, offset management), https://kafka.apache.org/documentation/#basic_ops_consumer_group

**Detailed explanation of each option:**

1. ✅ **A. `--reset-offsets --to-earliest ... --execute`.**  
   **Correct**. Resets committed offsets to the start.

2. ✅ **B. `--list` lists groups.**  
   **Correct**. Enumerates consumer groups.

3. ❌ **C. `kafka-groups.sh` is the group tool.**  
   **Incorrect**. The correct tool is `kafka-consumer-groups.sh`.

4. ❌ **D. Reset requires the group to be active.**  
   **Incorrect**. The group must be **inactive** to reset offsets.

5. ✅ **E. `--describe` shows offsets, lag, member/host.**  
   **Correct**. The lag-inspection view.

</details>
