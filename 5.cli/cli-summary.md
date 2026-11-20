# Kafka CLI Tools Overview
> **Updated for Apache Kafka 4.2 (KRaft mode only)**
> 
> Source: kafka.apache.org/42 | Kafka: The Definitive Guide 2nd Edition
> 
> ⚠️ ZooKeeper has been completely removed in Kafka 4.0+. Only KRaft mode is supported.

---

## Key CLI Tools

### 1. `kafka-topics.sh`
Used for creating, deleting, describing, or altering topics on a Kafka broker.

```bash
# Create a topic
kafka-topics.sh --bootstrap-server localhost:9092 \
  --create --topic my-topic \
  --partitions 6 \
  --replication-factor 3

# List all topics
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

### Describe a topic
```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --describe --topic my-topic

# Result:
Topic: topic-name     TopicId: 4n-O8CRiSYqsQ5qvbeiCgQ PartitionCount: 2       ReplicationFactor: 1    Configs: max.message.bytes=104857600
        Topic: topic-name     Partition: 0    Leader: 1       Replicas: 1     Isr: 1
        Topic: topic-name     Partition: 1    Leader: 1       Replicas: 1     Isr: 1

```

### Alter (increase) partitions — can only be increased, never decreased!
```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --alter --topic my-topic \
  --partitions 12
```

### Delete a topic
```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --delete --topic my-topic
```

### Find under-replicated partitions
```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --describe --under-replicated-partitions
```

### Find unavailable partitions
```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --describe --unavailable-partitions
```

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka broker address(es). **Required**. Replaces deprecated `--zookeeper`. |
| `--create` | Creates a new topic. |
| `--delete` | Deletes an existing topic. |
| `--alter` | Alters an existing topic (e.g., increase partitions). |
| `--list` | Lists all available topics. |
| `--describe` | Describes topic details (partitions, replicas, ISR). |
| `--topic` | Specifies the topic name. |
| `--partitions` | Number of partitions (target total, not increment!). |
| `--replication-factor` | Replication factor for each partition. |
| `--config` | Topic-level configuration override (e.g., `retention.ms=86400000`). |
| `--if-exists` | Perform operation only if topic exists. |
| `--if-not-exists` | Create topic only if it does not already exist. |
| `--exclude-internal` | Exclude internal topics (e.g., `__consumer_offsets`) from listing. |
| `--under-replicated-partitions` | Show partitions where replicas are not in sync. |
| `--unavailable-partitions` | Show partitions with no leader. |
| `--at-min-isr-partitions` | Show partitions at minimum ISR threshold. |

---

### 2. `kafka-console-producer.sh`
Produces messages to a Kafka topic from the command line.

```bash
# Produce messages (interactive)
kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic

# Produce with key (tab-separated key:value)
kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --property parse.key=true \
  --property key.separator=:

# Produce with acks
kafka-console-producer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --producer-property acks=all
```

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka broker address(es). **Required**. ⚠️ NOT `--broker-list` (deprecated/removed)! |
| `--topic` | Topic to produce messages to. |
| `--producer-property` | Producer configuration property (e.g., `acks=all`, `compression.type=snappy`). |
| `--property` | Message formatter property (e.g., `parse.key=true`, `key.separator=:`). |
| `--compression-codec` | Compression type: `none`, `gzip`, `snappy`, `lz4`, `zstd`. |
| `--sync` | Send messages synchronously. |

---

### 3. `kafka-console-consumer.sh`
Consumes messages from a Kafka topic and displays them to standard output.


### Consume from beginning
```bash
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --from-beginning
```

### Consume with consumer group
```bash
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --group my-group
```

### Print key, value and timestamp
```bash
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --property print.key=true \
  --property print.timestamp=true \
  --property print.offset=true

#Result:
CreateTime:1795121930848        Offset:0        key-1   message-1 
CreateTime:1795121941827        Offset:1        key-2   message-2 
CreateTime:1795122168692        Offset:0        key-3   message-3 
```

### Consume from specific partition and offset
```bash
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic my-topic \
  --partition 0 \
  --offset 100
```

### Consume internal __consumer_offsets topic
```
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic __consumer_offsets \
  --formatter "kafka.coordinator.group.GroupMetadataManager\$OffsetsMessageFormatter" \
  --consumer-property exclude.internal.topics=false \
  --from-beginning

#Result:
[console-group-name,test-topic,1]::OffsetAndMetadata(offset=2, leaderEpoch=Optional[0], metadata=, commitTimestamp=1795122258015, expireTimestamp=None)
[console-group-name,test-topic,0]::OffsetAndMetadata(offset=1, leaderEpoch=Optional[0], metadata=, commitTimestamp=1795122258015, expireTimestamp=None)
[console-group-name,test-topic,1]::OffsetAndMetadata(offset=2, leaderEpoch=Optional[0], metadata=, commitTimestamp=1795122263014, expireTimestamp=None)
[console-group-name,test-topic,0]::OffsetAndMetadata(offset=1, leaderEpoch=Optional[0], metadata=, commitTimestamp=1795122263014, expireTimestamp=None)

```

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka broker address(es). **Required**. |
| `--topic` | Topic to consume from. |
| `--from-beginning` | Start consuming from the earliest offset. |
| `--group` | Consumer group ID. Group is **created automatically** on first join. |
| `--partition` | Consume from a specific partition. |
| `--offset` | Start offset (`earliest`, `latest`, or specific number). |
| `--max-messages` | Maximum number of messages to consume before exiting. |
| `--consumer-property` | Consumer configuration property. |
| `--property` | Message formatter property. |
| `--formatter` | Message formatter class. |
| `--skip-message-on-error` | Skip messages that cannot be parsed. |

---

### 4. `kafka-consumer-groups.sh`
Manages Kafka consumer groups: listing, describing, deleting, and resetting offsets.

```bash
# List all consumer groups
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --list
```

### Describe a consumer group (shows LAG!)
```bash
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --describe --group my-group

#Result:
GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                           HOST            CLIENT-ID
console-group   topic-name      0          1               1               0               console-consumer-4d473722-3c52-44ce-b661-e2b022485c75 /127.0.0.1      console-consumer
console-group   topic-name      1          2               2               0               console-consumer-4d473722-3c52-44ce-b661-e2b022485c75 /127.0.0.1      console-consumer
  
```

### Delete a consumer group (must be inactive!)
```bash
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --delete --group my-group
```

### Reset offsets - dry-run (preview only)
```bash
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --group my-group \
  --reset-offsets \
  --to-earliest \
  --topic my-topic
```

### Reset offsets - execute (actual reset)
```bash
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --group my-group \
  --reset-offsets \
  --to-earliest \
  --all-topics \
  --execute
```

### Reset to specific datetime
```bash
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --group my-group \
  --reset-offsets \
  --to-datetime 2024-01-01T00:00:00.000 \
  --all-topics \
  --execute
```

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka broker address(es). **Required**. |
| `--group` | Consumer group ID. |
| `--list` | List all consumer groups. |
| `--describe` | Show group details: offsets, lag, consumer IDs, hosts. |
| `--delete` | Delete a consumer group (must be inactive). |
| `--reset-offsets` | Reset offsets for a consumer group. |
| `--execute` | **Required** to actually perform the reset. Without it: dry-run only. |
| `--all-topics` | Apply reset to all topics consumed by the group. |
| `--topic` | Apply reset to a specific topic. |
| `--to-earliest` | Reset to oldest available offset. |
| `--to-latest` | Reset to newest offset. |
| `--to-offset <Long>` | Reset to a specific offset number. |
| `--to-datetime <YYYY-MM-DDTHH:mm:SS.sss>` | Reset to offset at a specific point in time. |
| `--shift-by <Long>` | Shift offset by N (positive = forward, negative = backward). |
| `--by-duration <PnDTnHnMnS>` | Shift offset by ISO 8601 duration (e.g., `PT1H` = 1 hour back). |
| `--to-current` | Reset to current offset (useful with dry-run). |

**Output columns when using `--describe`:**

| Column | Description |
|--------|-------------|
| `GROUP` | Consumer group name. |
| `TOPIC` | Topic being consumed. |
| `PARTITION` | Partition ID. |
| `CURRENT-OFFSET` | Last committed offset by the consumer. |
| `LOG-END-OFFSET` | Latest offset on the broker. |
| `LAG` | `LOG-END-OFFSET - CURRENT-OFFSET`. 0 = healthy. |
| `CONSUMER-ID` | Unique consumer instance ID. |
| `HOST` | Host of the consumer instance. |
| `CLIENT-ID` | Client ID of the consumer. |

---

### 5. `kafka-configs.sh`
Manages dynamic configuration for brokers, topics, users, and clients.


### Describe topic configuration overrides
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --entity-type topics \
  --entity-name my-topic
```

### Set topic retention to 2 weeks
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --alter \
  --entity-type topics \
  --entity-name my-topic \
  --add-config retention.ms=1209600000
```

### Delete topic configuration override (reverts to broker default)
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --alter \
  --entity-type topics \
  --entity-name my-topic \
  --delete-config retention.ms
```

### Modify specific broker configuration
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --alter \
  --entity-type brokers \
  --entity-name 0 \
  --add-config log.retention.ms=86400000
```

### Modify default configuration for ALL brokers
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --alter \
  --entity-type brokers \
  --entity-default \
  --add-config log.retention.ms=86400000
```

### Set producer quota for a client
```bash
kafka-configs.sh \
  --bootstrap-server localhost:9092 \
  --alter \
  --entity-type clients \
  --entity-name my-client \
  --add-config producer_byte_rate=1048576
```

| Flag | Description |
|------|-------------|
| `--bootstrap-server` | Kafka broker address(es). **Required**. |
| `--describe` | Show current configuration overrides. |
| `--alter` | Modify configuration. |
| `--entity-type` | Type: `topics`, `brokers`, `clients`, `users`. |
| `--entity-name` | Name/ID of the entity (topic name, broker ID, client ID). |
| `--entity-default` | Apply to all entities of the given type (broker-wide default). |
| `--add-config` | Add or update configuration key=value pairs. |
| `--delete-config` | Remove configuration override (reverts to default). |

---

### 6. `kafka-reassign-partitions.sh`
Reassigns partitions across brokers (used for cluster rebalancing, broker decommissioning).

```bash
# Step 1: Define topics to move (topics.json)
# {"topics": [{"topic": "my-topic"}], "version": 1}

# Step 2: Generate reassignment proposal
kafka-reassign-partitions.sh \
  --bootstrap-server localhost:9092 \
  --topics-to-move-json-file topics.json \
  --broker-list 1,2,3 \
  --generate

# Step 3: Execute reassignment
kafka-reassign-partitions.sh \
  --bootstrap-server localhost:9092 \
  --reassignment-json-file reassignment.json \
  --execute

# Step 4: Verify progress
kafka-reassign-partitions.sh \
  --bootstrap-server localhost:9092 \
  --reassignment-json-file reassignment.json \
  --verify

# With throttle to limit network impact
kafka-reassign-partitions.sh \
  --bootstrap-server localhost:9092 \
  --reassignment-json-file reassignment.json \
  --execute \
  --throttle 52428800
```

| Flag | Description |
|------|-------------|
| `--generate` | Generate a reassignment proposal (does NOT execute). |
| `--execute` | Execute the reassignment. |
| `--verify` | Check status of an in-progress reassignment. |
| `--cancel` | Cancel an in-progress reassignment. |
| `--throttle <bytes/sec>` | Limit replication traffic during reassignment. |
| `--topics-to-move-json-file` | JSON file with topics to reassign. |
| `--reassignment-json-file` | JSON file with the reassignment plan. |
| `--broker-list` | Target broker IDs for the reassignment. |
| `--disable-rack-aware` | Disable rack-aware assignment. |

### Full flow — moving leader replica from Broker A → Broker B:
```
kafka-reassign-partitions.sh --execute
        │
        ▼
Step 1: ADD Broker B as a new replica (RF temporarily increases)
        
        Before:  Leader=A  Replicas=[A, C]  ISR=[A, C]
        After:   Leader=A  Replicas=[A, C, B]  ISR=[A, C]
                                          ^^^
                           B starts replicating from leader A
        
        ── Producers/consumers still talk to A (leader) ──
        ── ZERO interruption ──
        
        │
        ▼
Step 2: B catches up → joins ISR
        
        Leader=A  Replicas=[A, C, B]  ISR=[A, C, B]
                                               ^^^
        B is now fully caught up (in ISR)
        
        │
        ▼
Step 3: Controller triggers preferred leader election
        
        Leader switches A → B
        
        Leader=B  Replicas=[B, C]  ISR=[B, C]
        
        ── Brief leader election: milliseconds ──
        ── Producers get NOT_LEADER_FOR_PARTITION ──
        ── Client retries automatically ──
        
        │
        ▼
Step 4: A is removed from replica list
        
        Final:  Leader=B  Replicas=[B, C]  ISR=[B, C]
```
---

### 7. `kafka-leader-election.sh`
Triggers preferred or unclean leader election for partitions.

```bash
# Trigger preferred leader election for all partitions
kafka-leader-election.sh \
  --bootstrap-server localhost:9092 \
  --election-type preferred \
  --all-topic-partitions

# Trigger preferred leader election for specific partitions
kafka-leader-election.sh \
  --bootstrap-server localhost:9092 \
  --election-type preferred \
  --path-to-json-file partitions.json

# Trigger unclean leader election (risk of data loss!)
kafka-leader-election.sh \
  --bootstrap-server localhost:9092 \
  --election-type unclean \
  --all-topic-partitions
```

| Flag | Description |
|------|-------------|
| `--election-type` | `preferred` (safe) or `unclean` (risk of data loss!). |
| `--all-topic-partitions` | Apply to all partitions. |
| `--topic` | Apply to a specific topic. |
| `--partition` | Apply to a specific partition. |
| `--path-to-json-file` | JSON file with specific partitions to elect. |

---

### 8. `kafka-acls.sh`
Manages Access Control Lists (ACLs) for Kafka resources.

```bash
# Grant producer access to a topic
kafka-acls.sh \
  --bootstrap-server localhost:9092 \
  --add \
  --allow-principal User:Alice \
  --operation Write \
  --topic my-topic

# Grant consumer access to a topic and group
kafka-acls.sh \
  --bootstrap-server localhost:9092 \
  --add \
  --allow-principal User:Bob \
  --operation Read \
  --topic my-topic \
  --group my-group

# List ACLs for a topic
kafka-acls.sh \
  --bootstrap-server localhost:9092 \
  --list \
  --topic my-topic

# Remove an ACL
kafka-acls.sh \
  --bootstrap-server localhost:9092 \
  --remove \
  --allow-principal User:Alice \
  --operation Write \
  --topic my-topic
```

| Flag | Description |
|------|-------------|
| `--add` | Add a new ACL. |
| `--remove` | Remove an existing ACL. |
| `--list` | List existing ACLs. |
| `--allow-principal` | Principal to grant access (e.g., `User:Alice`). |
| `--deny-principal` | Principal to deny access. |
| `--operation` | Operation: `Read`, `Write`, `Create`, `Delete`, `Alter`, `Describe`, `All`. |
| `--topic` | Apply ACL to a topic. |
| `--group` | Apply ACL to a consumer group. |
| `--cluster` | Apply ACL to the cluster. |

---

### 9. `connect-mirror-maker.sh` (MirrorMaker 2)
Replicates data between Kafka clusters. Based on Kafka Connect framework.
⚠️ Replaces the deprecated `kafka-mirror-maker.sh` (MirrorMaker 1).

```bash
# Start MirrorMaker 2
connect-mirror-maker.sh \
  connect-mirror-maker.properties
```

**Example `connect-mirror-maker.properties`:**
```properties
clusters = source, target
source.bootstrap.servers = source-broker:9092
target.bootstrap.servers = target-broker:9092
source->target.enabled = true
source->target.topics = .*
replication.factor = 3
```

---

### 10. `kafka-dump-log.sh`
Inspects Kafka log segment files on disk.

```bash
# Dump log segment metadata
kafka-dump-log.sh \
  --files /tmp/kafka-logs/my-topic-0/00000000000000000000.log

# Dump with message payload
kafka-dump-log.sh \
  --files /tmp/kafka-logs/my-topic-0/00000000000000000000.log \
  --print-data-log

# Dump cluster metadata log (KRaft)
kafka-dump-log.sh \
  --cluster-metadata-decoder \
  --files /var/kafka/metadata/__cluster_metadata-0/00000000000000000000.log
```

---

## Important Notes for CCDAK Exam

### ⚠️ Critical Facts

```
1. ZooKeeper is COMPLETELY REMOVED in Kafka 4.x
   → NEVER use --zookeeper flag
   → ALWAYS use --bootstrap-server

2. --broker-list is DEPRECATED/REMOVED
   → Use --bootstrap-server in kafka-console-producer.sh

3. Consumer Groups are created AUTOMATICALLY
   → No CLI command to explicitly create a group
   → Group is created on first JoinGroup request

4. Partitions can only be INCREASED, never decreased
   → kafka-topics.sh --alter --partitions <higher-number>
   → Provide TOTAL number, not increment!

5. --execute is REQUIRED for offset reset
   → Without --execute: dry-run (preview only)
   → With --execute: actual reset performed

6. MirrorMaker 2 = connect-mirror-maker.sh
   → NOT kafka-mirror-maker.sh (MirrorMaker 1, deprecated)
```

### Retention Configuration Quick Reference

```
TOPIC level (specific topic):
  retention.ms          → topic config
  retention.bytes       → topic config

BROKER level (default for all topics):
  log.retention.ms      → broker config (highest priority)
  log.retention.minutes → broker config (secondary)
  log.retention.hours   → broker config (tertiary, default=168h)
  log.retention.bytes   → broker config

2 weeks = 1,209,600,000 ms
1 day   = 86,400,000 ms
1 week  = 604,800,000 ms
```

### CLI Tool Quick Reference

| Task | Tool |
|------|------|
| Create/delete/alter topic | `kafka-topics.sh` |
| Produce messages | `kafka-console-producer.sh` |
| Consume messages | `kafka-console-consumer.sh` |
| Check consumer lag | `kafka-consumer-groups.sh --describe` |
| Reset consumer offsets | `kafka-consumer-groups.sh --reset-offsets` |
| Modify topic/broker config | `kafka-configs.sh` |
| Reassign partitions | `kafka-reassign-partitions.sh` |
| Trigger leader election | `kafka-leader-election.sh` |
| Manage ACLs | `kafka-acls.sh` |
| Cross-cluster replication | `connect-mirror-maker.sh` |
| Inspect log segments | `kafka-dump-log.sh` |

### Best Practices

- **Security**: Always configure ACLs and SSL/TLS in production environments.
- **Consumer Lag Monitoring**: Use `kafka-consumer-groups.sh --describe` for CLI monitoring. Use **Burrow** for continuous automated monitoring.
- **Configuration Management**: Use `kafka-configs.sh` for dynamic configuration changes without broker restarts.
- **Partition Reassignment**: Always use `--throttle` during reassignment to prevent network saturation.
- **Offset Reset**: Always do a dry-run first (without `--execute`) before committing to an offset reset.
- **Leader Election**: Run preferred leader election after broker maintenance to restore balance.
- **Durability over flush**: Do NOT configure `log.flush.interval.ms` manually — rely on replication (`acks=all`, `min.insync.replicas=2`) for durability.

---

# Application Testing, Scaling and Deployment (CCDAK)

## Common Testing Tools

| Tool | Purpose |
|---|---|
| `MockProducer<K,V>` / `MockConsumer<K,V>` (`kafka-clients` test utils) | Unit-test producer/consumer code with **no broker**: `MockProducer` records `history()` of sent records and can simulate errors/transactions. `MockConsumer` is fed records via `addRecord()`, `assign()/updateBeginningOffsets()` |
| `TopologyTestDriver` (`kafka-streams-test-utils`) | Unit-test a Kafka Streams topology without a broker: `createInputTopic()` / `createOutputTopic()`, `TestInputTopic.pipeInput()`, `TestOutputTopic.readKeyValue()`, `getKeyValueStore()`. Synchronous, advance time with `advanceWallClockTime`. Not a full integration (no real consumers/threads/rebalancing) |
| **Testcontainers** (`KafkaContainer`) | Integration tests against a real Kafka broker in Docker |
| Embedded Kafka (`EmbeddedKafkaCluster`, Spring `@EmbeddedKafka`) | In-JVM broker for integration tests |
| `kafka-console-producer.sh` / `kafka-console-consumer.sh` | Manual smoke tests / debugging |
| `kafka-producer-perf-test.sh` / `kafka-consumer-perf-test.sh` | **Load / throughput / latency tests** (`--num-records --record-size --throughput -1 --producer-props acks=all bootstrap.servers=...`) |
| `kafka-verifiable-producer.sh` / `kafka-verifiable-consumer.sh` | Verify delivery (acked / consumed JSON events) during failure tests |
| `kafka-e2e-latency.sh` | Measure end-to-end latency |
| Trogdor | Fault-injection / workload test framework for clusters |
| `kafka-dump-log.sh`, `kafka-get-offsets.sh` | Inspect on-disk segments and offsets while debugging |
| Schema Registry / Connect REST (`curl`) | Test schemas, compatibility, connector config validation |

- Unit tests (Mock*, TopologyTestDriver) → fast, no network. Integration tests (Testcontainers/Embedded) → real broker semantics.
- `kafka-topics.sh --describe` and `kafka-consumer-groups.sh --describe` verify results of a test (partitions, ISR, lag).

## Horizontal vs Vertical Scaling

| | **Horizontal** (scale out) | **Vertical** (scale up) |
|---|---|---|
| Meaning | Add more instances/brokers | Bigger machine (CPU, RAM, disk, network) |
| **Consumers** | Add consumers to the group → more partitions processed in parallel. Limited by **partition count** (extra consumers idle) | More threads (consumer is single-threaded per instance; use one consumer per thread) / bigger processing power |
| **Producers** | Add producer instances | Tune `batch.size`, `linger.ms`, `compression.type`, `buffer.memory` |
| **Brokers** | Add brokers, then **reassign partitions** (`kafka-reassign-partitions.sh`) — new brokers don't get existing partitions automatically | More RAM (page cache), faster disks/network, `num.io.threads`, `num.network.threads` |
| **Topics** | More partitions (raises max parallelism, can't be reduced, changes key mapping) | n/a |
| **Streams** | Start more instances with same `application.id` (tasks rebalanced). Max = number of input partitions | Raise `num.stream.threads` |
| **Connect** | Add workers, raise `tasks.max` | Larger worker heap/CPU |

- Kafka favours **horizontal** scaling. Consumer group size > partitions is useless.
- Scaling consumers when lag grows: first check processing slowness, then add consumers (≤ partitions), then add partitions.

## Common Deployment Frameworks

- **Docker / Docker Compose** — local dev and testing clusters (`apache/kafka`, `confluentinc/cp-kafka` images). Expose `advertised.listeners` correctly for host vs container networks.
- **Kubernetes** — production: StatefulSets with persistent volumes. Operators such as **Strimzi** (open source) and **Confluent for Kubernetes (CFK)** manage brokers, topics (CRDs: `Kafka`, `KafkaTopic`, `KafkaUser`, `KafkaConnect`), rolling upgrades, TLS certs. **Helm charts** for packaging.
- **Ansible** (`cp-ansible`), **Terraform** — provisioning bare-metal/VM clusters and managed resources.
- **Confluent Cloud / managed Kafka** (MSK, Aiven) — fully managed.
- Stateless apps (producers, consumers, Streams) deploy as normal Deployments. Streams with state benefit from StatefulSets/persistent volumes (faster restore) or standby replicas.
- Rolling restarts: one broker at a time, wait until `UnderReplicatedPartitions=0` before restarting the next. Controlled shutdown (`controlled.shutdown.enable=true`) moves leaders first.
- KRaft mode (no ZooKeeper) is the default in Kafka 4.x.
