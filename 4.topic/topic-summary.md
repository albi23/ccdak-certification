## Kafka Topic Configurations

Kafka topics are categorized into partitions for scalability and replicated across brokers for fault tolerance. Topic configuration parameters play a critical role in determining the behavior of topics in terms of performance, durability, and availability.

### Key Points for CCDAK on Topics

- **Durability and Fault Tolerance**: Configurations like `replication.factor` determine how data is replicated to ensure availability in case of broker failures.
- **Scalability**: The `partition` count of a topic influences how data is distributed across the cluster and impacts parallel processing capabilities.
- **Data Consistency**: The `acks` setting affects how producers receive acknowledgments from brokers, impacting data consistency guarantees.
- **Order Guarantee:** Kafka guarantees that any consumer of a given topic-partition will always read that partition's events in exactly the same order as they were written.
  - If maintaining strict order within a partition is critical, set `max.in.flight.requests.per.connection` to 1 (when idempotence is disabled). This ensures that while a message is retrying, no other messages can be sent that might overtake the retried message. With `enable.idempotence=true` (the default since Kafka 3.0) ordering is preserved with up to 5 in-flight requests.
- **Partition-Specific Order:** Order is guaranteed only within a partition, not across partitions.
  - Repartitioning can disrupt the order of messages in Kafka, primarily because it changes the way records are assigned to partitions.
- **Variable Message Count:** Partitions do not need to have the same number of messages.
- **Partition-Specific Offsets:** Offsets only have meaning within a specific partition.
- **Data Retention:** Messages are kept only for a limited time in Kafka, with the default being one week (`retention.ms` = 604.800.000, i.e. `log.retention.hours=168`).
- **Immutability:** Once data is written to a partition, it cannot be changed.
- **Partition Assignment:** If a key is provided, the partition is `toPositive(murmur2(key)) % numPartitions`. Records without a key are spread across partitions by the sticky partitioner (batch by batch, since Kafka 2.4), not strictly round-robin per record.

After adding partitions later, it cannot be guaranteed that old messages will be on the same partition as new messages with the same key.

### Important Topic Properties

#### `acks`
- **Scope**: Producer
- **Description**: Determines the number of acknowledgments the producer requires from brokers before considering a request complete. Valid values are `0`, `1`, or `all` (`-1`). The default is `all` since Kafka 3.0.
- **Impact**: This setting impacts data durability and producer throughput. Setting `acks=all` ensures higher data safety as it waits for all in-sync replicas to acknowledge (combine with topic-level `min.insync.replicas` >= 2 to enforce a minimum ISR size). However, this may lower throughput compared to `acks=1` or `acks=0`, where the latter offers the highest throughput but with potential data loss.

#### `replication.factor`
- **Scope**: Topic
- **Description**: Specifies the number of copies (replicas) of a topic to maintain across the cluster.
- **Default Value**: This is a topic-level configuration set at the time of topic creation and doesn't have a universal default. It often defaults to the cluster's `default.replication.factor`.
- **Impact**: A higher replication factor increases data availability and fault tolerance but requires more disk space and network bandwidth. It is critical for ensuring that even if some brokers are down, your data remains accessible.

#### `partitions`
- **Scope**: Topic
- **Description**: Determines the number of partitions within a topic. Partitions are the basic unit of parallelism in Kafka, with each partition being independently consumed.
- **Default Value**: This is set at the time of topic creation and typically defaults to the cluster's `num.partitions` setting.
- **Impact**: More partitions allow greater parallel processing of data but can increase the overhead on the Kafka cluster (controller metadata, replication, file handles). Finding the right balance is key to optimizing performance and resource utilization.

### Essential Kafka Topic Configuration Parameters

#### Durability and Fault Tolerance

- **`replication.factor`**: Defines the number of replicated copies of a topic across the cluster, enhancing data availability and fault tolerance. The actual number can be set per topic and is crucial for maintaining data integrity in the event of broker failures.

#### Scalability Through Partitioning

- **`partitions`**: Controls the partition count for a topic, directly influencing data distribution and parallel processing capabilities across consumers. More partitions support higher parallelism but may increase cluster management overhead.

#### Data Consistency and Throughput

- **`acks`**: Configures acknowledgment requirements from brokers to producers, balancing between data consistency and throughput. Values range from `0` (fire and forget), `1` (leader acknowledgment), to `all` (full ISR acknowledgment).

### Advanced Topic Configurations for Fine-Tuning

#### Log Compaction and Retention

- **`cleanup.policy`**: Supports log compaction (`"compact"`) to retain at least the last known value for each key within a topic, crucial for stateful applications. 
  - The default `cleanup.policy` for Kafka topics is `delete`. (Kafka will delete records that are older than the retention period specified by `retention.ms`.)
  - Use `kafka-configs.sh --alter` or the Admin API to change the policy for existing topics (altering configs via `kafka-topics.sh` is no longer supported).
  - The `delete` policy might also be used in tandem to prevent the state store from growing indefinitely, especially when windowed operations are involved. (Use `"compact,delete"` )
  - Kafka Streams often requires that the latest state be recoverable even after restarts or rebalancing, making compaction a necessity.
- **`min.cleanable.dirty.ratio`**: Determines the ratio of log segments eligible for compaction. Lower values trigger compaction sooner, helping maintain a cleaner log with less overhead.

#### Segment Management and Efficiency

- **`segment.ms`**: Configures the time Kafka waits before closing the current log segment and starting a new one. Segment management affects storage and can impact log compaction and retention behavior.

#### Timestamps and Ordering

- **`message.timestamp.type`**: Defines whether Kafka should use the message creation time (`CreateTime` - default) or the time of log append (`LogAppendTime`). This setting can impact message ordering and log retention policies.
```
CreateTime (default):
  Producer sets ts=10:00:00.000
  Network delay: 500ms
  Broker appends at 10:00:00.500
  Stored timestamp: 10:00:00.000  ← producer's time

LogAppendTime:
  Producer sets ts=10:00:00.000  (ignored)
  Broker appends at 10:00:00.500
  Stored timestamp: 10:00:00.500  ← broker's time
```
### Key Considerations for Message Key and Size

#### Message Key Usage

- Utilizing a message key (`key!=null`) ensures that messages with the same key are always sent to the same partition, facilitating message ordering per key. However, modifying the partition count can disrupt this consistency.

#### Managing Message Sizes

- Kafka's default message size limit is 1MB. Exceeding this without proper configuration adjustments (broker/topic `message.max.bytes` / `max.message.bytes`, `replica.fetch.max.bytes`, producer `max.request.size`, consumer `max.partition.fetch.bytes`) will result in a `RecordTooLargeException` on the producer.


## Best Practices for Modifying Topics (CCDAK)

- **Partitions can only be increased, never decreased** (`kafka-topics.sh --alter --partitions N`). To reduce, create a new topic and migrate data.
- **Increasing partitions breaks key→partition mapping** (`murmur2(key) % numPartitions` changes): new records for an existing key may go to a different partition → per-key ordering and Streams/state co-partitioning are affected, and existing data is **not** moved. Preferably create a new topic with the right partition count and copy/replay data to it.
- **Replication factor** cannot be changed with `--alter`. Use `kafka-reassign-partitions.sh` with a JSON reassignment that lists more/fewer replicas (use `--throttle` to limit impact).
- **Config changes** are dynamic and need no restart: `kafka-configs.sh --alter --entity-type topics --entity-name T --add-config retention.ms=...` (use `--delete-config` to fall back to the broker default). Topic-level overrides take priority over broker defaults.
- Changing `cleanup.policy` or retention can immediately delete data older than the new retention — check before lowering `retention.ms`.
- Deleting a topic requires `delete.topic.enable=true` (default true) and is irreversible. Consumers/producers with auto-create enabled might recreate it.
- Partition count sizing: target throughput / per-partition throughput ≥ max number of consumers in a group, but too many partitions increase open files, leader election time and end-to-end latency. Over-provision a bit (e.g. 2–3x) to avoid later increases.
- Don't rely on `auto.create.topics.enable` in production — create topics explicitly with deliberate partitions and RF.
- Message size changes must be consistent end to end: `message.max.bytes` (broker/topic `max.message.bytes`), `replica.fetch.max.bytes`, producer `max.request.size`, consumer `max.partition.fetch.bytes`.
