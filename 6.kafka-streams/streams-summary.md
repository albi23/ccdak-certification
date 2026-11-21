## Kafka Streams: Building Real-Time Applications and Microservices

Kafka Streams is a client library (not a separate cluster) designed to build real-time applications and microservices inside your JVM (Java/Scala) application, with data both inputted from and outputted to Kafka clusters. It scales simply by running more instances of your app and provides fault tolerance via local state stores backed by Kafka changelog topics.

### Core Concepts of Kafka Streams

- **Stream Processing**: Real-time, record-by-record processing from Kafka topics.
- **Processor Topology**: A **static** DAG (defined at build time, not runtime) of **source processors** (read from topics) → **stream processors** (stateless or stateful transformations) → **sink processors** (write to topics). Use `topology.describe()` to inspect the topology and its sub-topologies.
- **KStream, KTable, and GlobalKTable**: The three core DSL abstractions.

### KStream vs KTable vs GlobalKTable

- **`KStream`**: Unbounded stream of records where each record is an independent event (**insert** semantics). Best for stateless transformations and individual event processing.
- **`KTable`**: Changelog stream where each record is an **upsert** by key (latest value per key wins), backed by a state store. Best for aggregations, joins, and maintaining a materialized view of latest values.
- **`GlobalKTable`**: Like a `KTable`, but **fully replicated to every application instance** (all partitions on every instance). Enables joins without co-partitioning or repartitioning, but is **not suitable for large datasets** and is populated from offset 0 on startup (startup time cost).

> ⚠️ **Exam traps:**
> - `KTable` requires records to have keys (null-key records are dropped / cause errors).
> - `GlobalKTable` joins **never** trigger repartitioning. `KStream`-`KTable` joins do if keys don't match.
> - `GlobalKTable` is populated from offset 0 on startup — factor in startup latency and memory/disk footprint.

**Stream-Table Duality:**

- **Stream as Table:** A stream can be viewed as a changelog of a table, where each record captures a state change. Replaying the changelog from the beginning reconstructs the table.
- **Table as Stream:** A table is a snapshot of the latest value for each key in a stream. Iterating over its key-value entries produces a stream.

---

### Time Semantics & Windowing

#### Time Semantics
- **`EventTime` (default)**: Uses the record timestamp (`message.timestamp.type=CreateTime`).
- **`ProcessingTime`**: Wall-clock time when the record is processed (`WallclockTimestampExtractor`).
- **`IngestionTime`**: Time when the broker appended the record (`LogAppendTime`).
- Override default timestamp extraction by implementing the `TimestampExtractor` interface.
  ```
  props.put(StreamsConfig.DEFAULT_TIMESTAMP_EXTRACTOR_CLASS_CONFIG, MyCustomTimestampExtractor.class);
  ```

#### Window Types
- **Tumbling Window**: Fixed-size, non-overlapping time windows (`TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(5))` or `TimeWindows.ofSizeAndGrace(...)`. Old `TimeWindows.of(...)` is removed in Kafka 4.0).
```
When the advance interval equals the window size, it is a tumbling window:
[0:00─────5:00][5:00─────10:00][10:00────15:00]
```
- **Hopping Window**: Fixed-size, overlapping time windows (`TimeWindows.ofSizeWithNoGrace(size).advanceBy(advance)`).
```
Fixed size with advance interval < window size:
[0:00────5:00]
  [1:00────6:00]
    [2:00────7:00]
```
- **Sliding Window**: Overlapping windows based on the time difference between record timestamps (used for aggregations via `SlidingWindows` and stream-stream joins via `JoinWindows`).
- **Session Window**: Dynamically sized, non-overlapping windows based on activity sessions and inactivity gaps (`SessionWindows.ofInactivityGapWithNoGrace(Duration.ofMinutes(5))` or `ofInactivityGapAndGrace(...)`).
```
Gap = 30 min:
User1: click t=1:00, click t=1:05, click t=1:20
       └──────────── session 1 ───────────┘
                                          (inactive > 30 min)
User1: click t=2:30, click t=2:45
       └───── session 2 ─────┘
```
- **Grace Period**: Controls how long after a window closes late-arriving records are still accepted.

> ⚠️ **Exam traps:**
> - Without a grace period (`grace = 0`), late records are **dropped silently**.
> - A single record can fall into **multiple** hopping windows, but only **one** tumbling window.

---

### State Stores & Internal Topics

#### State Stores
- **What they are**: Embedded local key-value, window, or session stores used by stateful operations (aggregations, joins, windowing) and interactive queries.
- **Storage Types**:
  - **Persistent (RocksDB — default)**: Stored on local disk (`state.dir`, default `/tmp/kafka-streams`), survives restarts. Configured via `Stores.persistentKeyValueStore()`, `Stores.persistentWindowStore()`, etc.
  - **In-memory**: Faster, but lost on restart and must be rebuilt from the changelog topic.
- **Resource Management**: Always close `KeyValueIterator` / `WindowStoreIterator` instances after use to prevent resource leaks and OOM errors.
- **Fault Tolerance & Recovery**: Every state store is backed by a compacted Kafka **changelog topic**. On restart or failure, state is restored by replaying the changelog topic.
- **Standby Replicas (`num.standby.replicas`)**: Maintain pre-warmed shadow copies of state stores on other instances for near-instant failover.

> ⚠️ **Exam trap:** `num.standby.replicas=0` (default) means failover requires full state restoration from the changelog topic.

#### Internal Topics
Kafka Streams automatically creates and manages internal topics (do **not** configure or manually delete them):

| Topic Pattern | Purpose | Cleanup Policy |
|---|---|---|
| `<app-id>-<store-name>-changelog` | State store backup & restoration | **compact** |
| `<app-id>-<name>-repartition` | Key repartitioning across sub-topologies | **delete** |

> ⚠️ **Exam traps:**
> - Repartition topics use **`delete`** policy. Changelog topics use **`compact`** policy.
> - Do **not** manually delete changelog topics — state is permanently lost and must be fully rebuilt from source.

---

### Stateless vs Stateful Operations

#### Stateless Operations
Record-by-record transformations that require no state store:

| Operation | Changes Key? | Triggers Repartition? |
|---|---|---|
| `map` | YES | YES |
| `mapValues` | NO | NO |
| `filter` / `filterNot` | NO | NO |
| `flatMap` | YES | YES |
| `flatMapValues` | NO | NO |
| `selectKey` | YES | YES |
| `peek` / `foreach` | NO | NO |
| `merge` | NO | NO |
| `branch` / `split` | NO | NO |

> ⚠️ **Exam trap:** Any operation that modifies the key (`map`, `flatMap`, `selectKey`, `groupBy`) marks the stream as **repartition required** — Kafka Streams automatically inserts an internal repartition topic before the next downstream stateful operation. `mapValues` and `flatMapValues` preserve the key and never trigger repartitioning.

#### Stateful Operations & Aggregations
Operations that maintain state in a state store: `count()`, `reduce()`, `aggregate()`, joins, windowed aggregations, and `KTable` materialization.

- Aggregations require a key and **always return a `KTable`**.
- **`groupBy` vs `groupByKey`**:
  - `groupBy(...)` selects a new key → triggers repartitioning.
  - `groupByKey()` keeps the existing key → no repartitioning (unless an upstream key-changing op marked it dirty). Exists only on `KStream`.
  - A `KTable` is grouped with `groupBy(...)` → returns `KGroupedTable` and requires both an **adder** and a **subtractor** for `aggregate`/`reduce`.

---

### Join Operations & Co-Partitioning

#### Join Compatibility Matrix

| Join Type | Left | Right | Supported Joins | Repartition? | Window Required? | Result |
|---|---|---|---|---|---|---|
| **KStream–KStream** | `KStream` | `KStream` | Inner, Left, Outer | If keys differ | **YES** (`JoinWindows`) | `KStream` |
| **KStream–KTable** | `KStream` | `KTable` | Inner, Left *(no Outer)* | If keys differ | **NO** | `KStream` |
| **KStream–GlobalKTable** | `KStream` | `GlobalKTable` | Inner, Left *(no Outer)* | **NEVER** | **NO** | `KStream` |
| **KTable–KTable** | `KTable` | `KTable` | Inner, Left, Outer | If keys differ | **NO** | `KTable` |

> ⚠️ **Exam traps:**
> - **KStream–KStream** joins **require** a window (`JoinWindows`).
> - **KStream–KTable** joins are **non-windowed** — updates to the `KTable` do **not** re-trigger joins for past `KStream` records.
> - **KStream–GlobalKTable** joins use a `KeyValueMapper` — the right-side lookup key can be derived from the left record's **key or value**, and no co-partitioning is required.
> - **KTable–KTable** join result is a **`KTable`**, not a `KStream`.

#### Co-Partitioning Rules
Co-partitioning means two or more topics have aligned partitions so that records with the same key land in the same partition number across topics:

1. **Same Number of Partitions**: Joined source topics must have the exact same partition count (otherwise Kafka Streams throws a `TopologyException`).
2. **Consistent Partitioning Strategy**: Producers must use the same key type and partitioner across co-partitioned topics.
3. **Developer Responsibility**: Kafka Streams does **not** automatically co-partition source topics — it only validates partition counts. It only auto-repartitions when a key was changed upstream (`selectKey`, `map`, `groupBy`).
4. **Exception**: `GlobalKTable` joins do **not** require co-partitioning.
5. **Scaling**: Adding partitions to one co-partitioned topic requires scaling all paired topics consistently.

#### How Repartitioning Works
When Kafka Streams requires repartitioning, it:
1. Writes records with the new keys to an internal `<app-id>-<name>-repartition` topic.
2. Splits the topology into **sub-topologies**, creating a new set of independent tasks that consume and process events from the repartition topic in parallel.

---

### Message Delivery Guarantees & Exactly-Once Semantics (EOS)

Kafka supports three delivery guarantees:
- **At-most-once**: Messages may be lost on failure. Never duplicated.
- **At-least-once (default)**: No message loss, but duplicates can occur on retries/rebalances.
- **Exactly-once**: No duplicates and no data loss for Kafka-to-Kafka workflows.

**Exactly-Once in Kafka Streams:**
- Enable via `processing.guarantee=exactly_once_v2` (requires brokers ≥ 2.5. Older `exactly_once` and `exactly_once_beta` are deprecated and removed in Kafka 4.0). No code changes required.
- **How it works**: Uses an idempotent, transactional producer with epoch-based fencing to atomically commit (1) output records, (2) state-store changelog writes, and (3) consumed input offsets (`__consumer_offsets`) in a single transaction per commit interval.
- **Internal consumer isolation**: `isolation.level=read_committed` is set automatically on internal Streams consumers. Downstream consumers reading output topics must also set `isolation.level=read_committed`.
- **Commit interval**: `commit.interval.ms` defaults to **100 ms** under EOS (vs **30,000 ms** under `at_least_once`).
- **Performance cost**: ~20–30% throughput overhead compared to `at_least_once`.
- **Scope**: Covers Kafka → Kafka processing only. External side effects (HTTP calls, DB writes) require an idempotent sink/consumer.

> ⚠️ **Exam trap:** EOS requires `replication.factor >= 2` for internal topics (repartition + changelog) and proper broker transaction log settings (`transaction.state.log.replication.factor=3`, `min.isr=2` in production).

---

### SerDes (Serializers & Deserializers)

- Every `KStream` and `KTable` requires a `Serde` (Serializer + Deserializer) for both keys and values.
- **Built-in Serdes**: `Serdes.String()`, `Serdes.Integer()`, `Serdes.Long()`, `Serdes.ByteArray()`, `Serdes.Double()`, etc.
- **Schema Registry formats**: Use Confluent's `KafkaAvroSerde` (or Protobuf / JSON Schema equivalents) with Schema Registry.
- Configure globally via `default.key.serde` / `default.value.serde` (defaults to `Serdes.ByteArray()`) or override per operation (`Consumed.with(...)`, `Produced.with(...)`, `Grouped.with(...)`, `Materialized.with(...)`).

> ⚠️ **Exam trap:** If you don't specify a `Serde` explicitly and the default doesn't match the runtime type, Kafka Streams throws a `ClassCastException` at runtime.

---

### Threading Model, Scaling & Fault Tolerance

#### Threading & Parallelism
- One `KafkaStreams` application instance runs `N` stream threads (`num.stream.threads`, default `1`).
- Kafka Streams splits the topology into **tasks** — one task per input partition.
- Each stream thread executes one or more tasks independently.
- **Maximum parallelism = number of input partitions**. Extra threads or instances beyond the partition count sit idle.
- **Scale out**: Start more instances with the **same `application.id`** → tasks redistribute automatically via the consumer group protocol using **`StreamsPartitionAssignor`**.

> ⚠️ **Exam trap:** `application.id` is the consumer group ID and internal topic prefix — changing it resets offsets and creates a brand-new set of internal topics/state.

#### Fault Tolerance & Rebalancing
- **Changelog restoration**: If an instance fails and loses local state, the reassigned instance replays the changelog topic to rebuild the state store.
- **Standby replicas (`num.standby.replicas`)**: Tasks fail over to an instance that already has a warm state copy → near-instant recovery.
- **Warm-up tasks (Kafka Streams 2.6+, KIP-562)**: New instances receive tasks as warm-up replicas first before becoming active, minimizing rebalance-induced downtime/lag.
- **Static membership (`group.instance.id`)**: Prevents unnecessary rebalances during rolling restarts.
- **Consumer liveness**: Standard consumer configs (`session.timeout.ms`, `heartbeat.interval.ms`) apply to Streams' internal consumers.

---

### Interactive Queries

Interactive Queries allow you to query local state stores directly from within the Kafka Streams application without sinking results to another topic or external database:

- Query a local store via `KafkaStreams.store(StoreQueryParameters.fromNameAndType("countsStore", QueryableStoreTypes.keyValueStore()))`.
- For distributed apps, use `KafkaStreams.metadataForKey(...)` (or `queryMetadataForKey(...)`) to discover which application instance hosts the partition for a given key, then route the request (e.g., via HTTP/RPC) to that instance.

> ⚠️ **Exam trap:** Interactive queries are strictly **read-only** — you cannot write to a state store through interactive queries.

---

### Key Configuration Properties & Performance Tuning

```properties
# Identity
application.id              # unique app ID - consumer group ID & prefix for internal topics
bootstrap.servers           # Kafka broker list

# Processing guarantee
processing.guarantee        # at_least_once (default) | exactly_once_v2

# Threading
num.stream.threads          # 1 (default) — stream threads per instance

# State
num.standby.replicas        # 0 (default) — standby state store copies for fast failover
state.dir                   # /tmp/kafka-streams (default) — local RocksDB directory

# Commit
commit.interval.ms          # 30000ms (default, at_least_once) | 100ms (exactly_once_v2)

# Caching
cache.max.bytes.buffering   # 10MB (default) — 0 disables caching (statestore.cache.max.bytes in 3.4+)

# Replication
replication.factor          # -1 (default, uses broker default) for internal topics

# Serdes
default.key.serde           # Serdes.ByteArray() default
default.value.serde         # Serdes.ByteArray() default

# Join tuning
max.task.idle.ms            # 0 (default) — wait for missing partition data before processing
```

**Performance Tuning Tips:**
- **`cache.max.bytes.buffering=0`**: Disables record caching/deduplication → every update is forwarded immediately (higher downstream volume - useful for testing).
- **`commit.interval.ms`**: Increasing it reduces commit overhead and improves throughput, at the cost of a larger rebalance recovery window.
- **`num.stream.threads`**: Increase for CPU-bound workloads (up to the input partition count).
- **`num.standby.replicas`**: Increase for faster failover at the cost of extra disk and network bandwidth.
- **`state.dir` on persistent SSD**: Critical for RocksDB performance and fast restarts (only missing deltas need to be restored from changelog).
- **`max.task.idle.ms > 0`**: Useful when joining streams with skewed partition arrival times to avoid joining against empty partitions.
- **`StreamsConfig.TOPOLOGY_OPTIMIZATION`**:  Tells Kafka Streams to rewrite the topology at build time to eliminate unnecessary repartition topics and state stores that would otherwise be created naively.
  ```java
  // Example 
  StreamsBuilder builder = new StreamsBuilder();

  KStream<String, String> stream1 = builder.stream("topic-1");
  KStream<String, String> stream2 = builder.stream("topic-2");
  
  // Both streams change the key — each marks repartition required
  KStream<String, String> mapped1 = stream1.selectKey((k, v) -> v.split(",")[0]);
  KStream<String, String> mapped2 = stream2.selectKey((k, v) -> v.split(",")[0]);
  
  // Merge the two streams
  KStream<String, String> merged = mapped1.merge(mapped2);
  
  // Stateful op downstream — triggers repartition
  merged.groupByKey()
  .count()
  .toStream()
  .to("output-topic");
  ```

  Result:
  ```bash
   # NO_OPTIMIZATION
  topic-1 → selectKey → [repartition-topic-1] ──┐
                                                merge → groupByKey → count → output
  topic-2 → selectKey → [repartition-topic-2] ──┘
  
  #OPTIMIZE
  topic-1 → selectKey ──┐
                        merge → [repartition-topic] → groupByKey → count → output
  topic-2 → selectKey ──┘
  ```
---

### Developing with Kafka Streams (Syntax & APIs)

#### Word Count Example
```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> textLines = builder.stream("inputTopic");
KTable<String, Long> wordCounts = textLines
    .flatMapValues(textLine -> Arrays.asList(textLine.toLowerCase().split("\\W+")))
    .groupBy((key, word) -> word)
    .count(Materialized.as("countsStore"));
wordCounts.toStream().to("outputTopic", Produced.with(Serdes.String(), Serdes.Long()));
```

#### Common KStream Operations
- `map` (changes key → repartition):
  ```java
  KStream<String, Integer> doubled = stream.map((key, value) -> new KeyValue<>(key, value * 2));
  ```
- `mapValues` (preserves key → no repartition):
  ```java
  KStream<String, Integer> transformed = stream.mapValues(value -> value.length());
  ```
- `filter`:
  ```java
  KStream<String, Integer> filtered = stream.filter((key, value) -> value > 100);
  ```
- `flatMapValues`:
  ```java
  KStream<String, String> words = stream.flatMapValues(value -> Arrays.asList(value.split("\\s+")));
  ```
- `split` / `branch` (`KStream#branch(Predicate...)` is deprecated and removed in Kafka 4.0. Use `split()`):
  ```java
  stream.split()
        .branch((key, value) -> value > 100, Branched.withConsumer(big -> big.to("big-topic")))
        .defaultBranch(Branched.withConsumer(small -> small.to("small-topic")));
  ```
- `merge`:
  ```java
  KStream<String, Integer> merged = stream1.merge(stream2);
  ```
- Aggregating & joining:
  ```java
  KTable<String, Long> aggregated = stream.groupByKey().count();
  KStream<String, String> joined = stream.leftJoin(table, (streamValue, tableValue) -> streamValue + "-" + tableValue);
  ```

#### Common KTable Operations
A `KTable` is grouped with `groupBy` (returning a `KGroupedTable`) and requires both an adder and a subtractor for `aggregate`/`reduce`:
- `aggregate`:
  ```java
  KTable<String, Long> sums = table
      .groupBy((key, value) -> KeyValue.pair(value.category(), value.amount()), Grouped.with(Serdes.String(), Serdes.Long()))
      .aggregate(() -> 0L, (aggKey, newValue, aggValue) -> aggValue + newValue, (aggKey, oldValue, aggValue) -> aggValue - oldValue);
  ```
- `reduce`:
  ```java
  KTable<String, Integer> reduced = table
      .groupBy((key, value) -> KeyValue.pair(key, value))
      .reduce((agg, v) -> agg + v, (agg, old) -> agg - old);
  ```
- `join`:
  ```java
  KTable<String, String> joined = table1.join(table2, (value1, value2) -> value1 + "-" + value2);
  ```
- `count`:
  ```java
  KTable<Integer, Long> counts = table.groupBy((key, value) -> KeyValue.pair(value % 10, value)).count();
  ```

---

### Comparisons (CCDAK)

#### Kafka Streams vs Plain Consumer/Producer API

| | Consumer/Producer API | Kafka Streams |
|---|---|---|
| Nature | Low-level clients | Library on top of them (embedded in your app, no separate cluster) |
| State | You manage it yourself | Built-in **state stores** (RocksDB + changelog topics) |
| Operations | Manual | Declarative: `map`, `filter`, `groupBy`, `aggregate`, `join`, windowing |
| Scaling | Consumer group | Consumer group underneath (`StreamsPartitionAssignor`). Tasks = partitions |
| Fault tolerance | Manual | Automatic state restore from changelog topics + `num.standby.replicas` |
| Exactly-once | Manual transactions | `processing.guarantee=exactly_once_v2` |
| Output | Topic-to-anywhere | Kafka topic → Kafka topic only (use Kafka Connect for external systems) |

#### Kafka Streams vs Other Stream Processors & ksqlDB

| Framework | Architecture | Best Fit |
|---|---|---|
| **Kafka Streams** | Embedded JVM library (no separate cluster), local RocksDB state, EOS via Kafka transactions | Event-driven microservices, Kafka → Kafka processing with Java/Scala control |
| **ksqlDB** | SQL interface built **on top of Kafka Streams** (persistent queries run as Kafka Streams apps) | SQL-first analytics, rapid prototyping, teams preferring SQL over Java/Scala |
| **Apache Flink** | Distributed processing cluster, external state, EOS via checkpointing | Complex event processing, ultra-low-latency multi-source pipelines beyond Kafka |
| **Spark Streaming** | Distributed cluster, micro-batch processing, higher latency | Unified batch + streaming analytics at scale |

#### Streams DSL vs Processor API

| | Streams **DSL** | **Processor API** |
|---|---|---|
| Level | High-level, declarative (`StreamsBuilder`, `KStream`, `KTable`) | Low-level, imperative (`Topology`, `Processor`, `ProcessorContext`) |
| Operations | Predefined operators | Anything: custom logic, custom state-store access |
| Control | Limited | Full control of forwarding, **punctuations** (scheduled callbacks by stream-time or wall-clock), manual commits |
| Effort | Less code, recommended default | More code and responsibility |
| State | Managed behind operators | Attach `StateStore` to processor explicitly |

- Both APIs can be mixed: DSL `process()` / `processValues()` hook a custom `Processor` into a DSL topology.
- Use the Processor API when you need custom timing (`punctuate`), non-standard state access, or logic the DSL cannot express.

---

### CCDAK Exam Quick-Reference Cheat Sheet

| # | Exam Trap / Key Fact |
|---|---|
| 1 | `selectKey` / `map` / `flatMap` → always marks stream for **repartition** before a stateful op |
| 2 | `mapValues` / `flatMapValues` / `filter` → **never** triggers repartition |
| 3 | `KTable`–`KTable` join result is a **`KTable`**, not a `KStream` |
| 4 | `KStream`–`KStream` join **requires** a window (`JoinWindows`) |
| 5 | `GlobalKTable` is replicated to **all** instances — don't use for large datasets. Never triggers repartition |
| 6 | `exactly_once_v2` requires broker ≥ 2.5 and `replication.factor >= 2` for internal topics |
| 7 | `application.id` is the consumer group ID — changing it resets offsets and state |
| 8 | Repartition topics use **`delete`**. Changelog topics use **`compact`** |
| 9 | Grace period = 0 → late records are **silently dropped** |
| 10 | Max parallelism = number of partitions of the input topic |
| 11 | `groupBy` changes key → repartition, `groupByKey` does not |
| 12 | `KStream`–`KTable` join: `KTable` updates do **not** re-trigger for past `KStream` records |
| 13 | `cache.max.bytes.buffering=0` → every record emitted immediately (no deduplication) |
| 14 | `num.standby.replicas=0` (default) → full changelog replay on failover |
| 15 | Topology is **static** — defined at build time, not configurable at runtime |
| 16 | Interactive queries are **read-only** — cannot write to state stores |
| 17 | Missing/mismatched `Serde` → `ClassCastException` at runtime |
