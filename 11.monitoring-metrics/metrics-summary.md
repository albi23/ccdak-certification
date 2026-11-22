> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Monitoring and Metrics in Kafka

Monitoring and Metrics in Kafka Kafka exposes rich metrics to monitor the health, performance, and utilization metrics of Kafka brokers, producers, and consumers. The ability to obtain these metrics quickly and at scale is vital for troubleshooting and optimizing Kafka cluster .

### Points to Remember for CCDAK on Monitoring and Metrics

- **JMX Integration**: Kafka metrics can be exposed via JMX, allowing integration with monitoring tools.
- **Custom Reporters**: Kafka supports pluggable metrics reporters for flexibility in how metrics are reported and consumed.
- **Performance Tuning**: Metrics are key to identifying bottlenecks and tuning Kafka for optimal performance.
- **Operational Insight**: Monitoring provides insights into Kafka's operational status, including throughput, latency, and resource utilization.

### Important Monitoring and Metrics Properties

#### `kafka.metrics.reporters` (legacy, broker-side Yammer metrics)
- **Default**: ""
- **Description**: Comma-separated list of classes to report Kafka's **Yammer** (server-side) metrics. These reporters implement the `kafka.metrics.KafkaMetricsReporter` interface. This is the older broker-only mechanism. Most modern monitoring uses `metric.reporters` (the Kafka Metrics framework) plus the built-in `JmxReporter`.
- **Trade-offs**: Adding custom reporters can enhance monitoring capabilities but might introduce additional overhead.

#### `metric.reporters`
- **Default**: `org.apache.kafka.common.metrics.JmxReporter` (since Kafka 4.0; in older versions the default was "" but the built-in `JmxReporter` was always enabled). Note: `auto.include.jmx.reporter` was removed in 4.0, and the `metrics.jmx.whitelist`/`metrics.jmx.blacklist` configs were renamed to `metrics.jmx.include`/`metrics.jmx.exclude`.
- **Description**: Comma-separated list of classes to report metrics (brokers, producers, consumers, Streams). These reporters implement the `org.apache.kafka.common.metrics.MetricsReporter` interface.
- **Trade-offs**: Enables detailed monitoring of producer and consumer metrics, with the trade-off of potential performance impact due to monitoring overhead.

#### `metrics.num.samples`
- **Default**: 2
- **Description**: The number of samples maintained to compute metrics.
- **Trade-offs**: Higher values provide more accurate metrics but can consume more memory.

#### `metrics.sample.window.ms`
- **Default**: 30000 (30 seconds)
- **Description**: The time window associated with each sample. Affects how metrics are calculated over time.
- **Trade-offs**: Larger windows provide smoother metrics over time but may delay detection of spikes or drops in metric values.

#### `metrics.recording.level`
- **Default**: INFO
- **Description**: The highest recording level for metrics in clients. Options are INFO, DEBUG or TRACE.
- **Trade-offs**: DEBUG provides more granular metrics but can significantly increase the amount of data collected, impacting performance and storage.

### Broker Metrics:
- `UnderReplicatedPartitions`: Number of partitions that are under-replicated. Use case: Identifying replication issues. Alert if greater than 0.
- `ActiveControllerCount`: Number of active controllers in the cluster. Use case: Ensuring controller failover is working correctly. Should be 1. Alert if not 1. (The **unique** controller takes care of Leader Election, Cluster Metadata, Rebalancing Partitions and Handling Broker Failures)
- `OfflinePartitionsCount`: Number of partitions without an active leader. Use case: Detecting availability issues. Should be 0. Alert if greater than 0.
- `RequestHandlerAvgIdlePercent`: Average idle percentage of the request handler thread pool. Use case: Monitoring request handling capacity. Low values may indicate resource contention.
- `NetworkProcessorAvgIdlePercent`: Average idle percentage of the network thread pool. Use case: Monitoring network processing capacity. Low values suggest potential network bottlenecks.
- `IsrExpandsPerSec`: Rate at which the in-sync replica set is expanding. Use case: Tracking replica synchronization.
- `IsrShrinksPerSec`: Monitors the rate at which replicas are removed from the ISR list per second. Use case: Tracking replica synchronization issues.
- `BytesInPerSec` and `BytesOutPerSec`: Inbound and outbound byte rate of brokers. Use case: Monitoring data throughput.
- `MessagesInPerSec`: Rate at which messages are being produced to brokers. Use case: Tracking message production rate.
- `UnderMinIsrPartitionCount`: Number of partitions with insufficient in-sync replicas. Use case: Identifying replication issues.
- `PartitionCount`: Total number of partitions across all topics in the cluster. Use case: Monitoring cluster capacity.
- `LeaderCount`: Number of partitions for which a broker is the leader. Use case: Monitoring leadership distribution.
- `RequestQueueSize` and `ResponseQueueSize`: Size of request and response queues. Use case: Ensuring brokers can keep up with client requests.
- `TotalTimeMs` (`kafka.network:type=RequestMetrics`, tagged `request=Produce`, `FetchConsumer`, `FetchFollower`, ...): Total time taken to process a request, broken down into `RequestQueueTimeMs`, `LocalTimeMs`, `RemoteTimeMs` (waiting for followers, e.g. `acks=all`), `ResponseQueueTimeMs` and `ResponseSendTimeMs`. High values may indicate performance issues. Use case: Monitoring request latency.
- `RequestsPerSec`: Rate of requests per request type. Use case: Monitoring broker load.
- `FetchMessageConversionsPerSec`: Rate of message format conversions during fetch requests. Use case: Tracking message format compatibility.
- 🚫 `ZooKeeperRequestLatencyMs`: Latency of ZooKeeper requests made by Kafka. Use case: Monitoring ZooKeeper performance. (Legacy: ZooKeeper was removed in Kafka 4.0; KRaft clusters use `kafka.controller` / `kafka.server:type=raft-metrics` instead.)
- `ControllerState`: State of the controller (e.g. idle or running a particular operation) - it does not tell whether a node is the active controller. `ActiveControllerCount` (1 if active, 0 if not) does. Use case: Monitoring controller health.
- `LogFlushRateAndTimeMs`: Monitors the rate and time of log flushes. High values can indicate I/O bottlenecks. Use case: Identifying disk performance issues.
- `LeaderElectionRateAndTimeMs`: Monitors the rate and time taken for leader election. High values may indicate issues with the controller or network. Use case: Tracking controller performance and stability.
- `HeapMemoryUsage` (JVM MBean `java.lang:type=Memory`, not a Kafka-defined metric): Tracks heap usage, helping to identify potential memory leaks or insufficient heap sizes. Use case: Monitoring broker memory utilization.
- `CollectionTime` / `CollectionCount` (JVM MBean `java.lang:type=GarbageCollector,name=*`): Time spent in garbage collection. High values can indicate potential performance issues. Use case: Identifying JVM garbage collection overhead.
- 🚫 `ZooKeeperDisconnectsPerSec`: Rate of disconnects from ZooKeeper. Legacy (ZooKeeper removed in Kafka 4.0).
- `Size` (`kafka.log:type=Log,name=Size`): On-disk size of each partition log. Kafka does not expose free disk space over JMX. Monitor it at OS level.

### Consumer Metrics:
- `records-lag-max`: Maximum lag in terms of number of records for any partition in this window. Use case: Monitoring consumer lag.
- `fetch-latency-avg`: Average time taken for a fetch request. Use case: Monitoring consumer performance.
- `records-consumed-rate`: The average number of records consumed per second. Use case: Tracking consumer throughput.
- `fetch-rate`: Number of fetch requests per second. Use case: Monitoring consumer activity (broker side: `TotalFetchRequestsPerSec`).
- `records-lag` (per partition) / consumer lag: how many messages the consumer is behind. Lag is not a single broker JMX bean. It is also available from `kafka-consumer-groups.sh --describe` or tools such as Burrow.

### Producer Metrics:
- `record-send-rate`: The average number of records sent per second. Use case: Monitoring producer throughput.
- `request-latency-avg`: The average request latency in ms. Use case: Monitoring producer latency.
- `outgoing-byte-rate`: The average number of outgoing bytes sent per second to all servers. Use case: Monitoring producer network utilization.
- `request-rate`: Number of requests sent per second. Use case: Monitoring producer activity (broker side: `TotalProduceRequestsPerSec`).

### Topic Metrics:
- `BrokerTopicMetrics`: Monitors topic-specific metrics such as bytes in/out, messages in/out, etc. Use case: Analyzing performance at the topic level.

### Confluent-Specific Metrics (🚫 vendor-specific, outside exam scope):
- Schema Registry: `schema-registry.registered.count`: Number of registered schemas. Use case: Monitoring schema usage.
- Kafka Connect: `connect-worker.connector-started-task-count`: Number of tasks started for a connector. Use case: Monitoring connector health.
- 🚫 ksqlDB: `ksql-server.query-stats.bytes-consumed-total`: Total bytes consumed by ksqlDB queries. Use case: Monitoring ksqlDB resource usage.

### Important Kafka Metrics

#### `UnderReplicatedPartitions`
- **Description**: Represents the number of partitions that are under-replicated, meaning they have fewer in-sync replicas (ISRs) than the desired replication factor.
- **Importance**: This metric is crucial for monitoring the health and reliability of the Kafka cluster. A non-zero value indicates that some partitions are at risk of data loss if a broker fails.
- **Monitoring Recommendations**:
 - Alert if the value is consistently greater than 0.
 - Investigate the root cause of under-replication, such as broker failures, network issues, or insufficient disk space.
 - Ensure that the replication factor is set appropriately based on the desired fault tolerance.

#### `ActiveControllerCount`
- **Description**: Indicates the number of active controllers in the Kafka cluster. In a healthy cluster, there should be exactly one active controller.
- **Importance**: The controller is responsible for managing partition leader elections and maintaining the overall state of the cluster. Having multiple active controllers can lead to conflicts and instability.
- **Monitoring Recommendations**:
 - Alert if the value deviates from 1.
 - If multiple controllers are detected, investigate the root cause, such as network partitions or issues with the KRaft controller quorum (ZooKeeper in pre-4.0 clusters).

#### `OfflinePartitionsCount`
- **Description**: Represents the number of partitions without an active leader. These partitions are unavailable for producing or consuming messages.
- **Importance**: Offline partitions indicate a problem with the Kafka cluster and can impact data availability and processing.
- **Monitoring Recommendations**:
 - Alert if the value is greater than 0.
 - Investigate the reasons for offline partitions, such as broker failures, network issues, or insufficient replicas.

#### `BytesInPerSec` and `BytesOutPerSec`
- **Description**: Measures the inbound and outbound byte rate of Kafka brokers, indicating the amount of data being produced to and consumed from the cluster.
- **Importance**: Monitoring these metrics helps in understanding the data throughput and identifying potential bottlenecks or performance issues.
- **Monitoring Recommendations**:
 - Set appropriate thresholds based on the expected data volume and network capacity.
 - Monitor trends over time to detect anomalies or sudden spikes in data throughput.
 - Correlate with other metrics like `MessagesInPerSec` and `TotalProduceRequestsPerSec` to gain insights into producer and consumer behavior.

#### Consumer lag (`records-lag-max`)
- **Description**: Represents the lag of consumers, indicating how many messages they are behind the latest offset in the partition they are consuming from.
- **Importance**: Consumer lag is a critical metric for monitoring the health and performance of Kafka consumers. High consumer lag can indicate issues like slow processing, insufficient consumer resources, or problems with the consumer application.
- **Monitoring Recommendations**:
 - Set appropriate lag thresholds based on the acceptable delay in message processing.
 - Alert if the lag exceeds the defined thresholds consistently.
 - Investigate the root cause of high consumer lag, such as slow processing logic, resource contention, or network issues.

#### `TotalTimeMs` (`request=Produce` / `request=Fetch*`)
- **Description**: Measures the total time taken for produce and fetch requests, respectively. These metrics provide insights into the latency of producer and consumer operations.
- **Importance**: Monitoring these metrics helps in identifying performance bottlenecks and ensuring that produce and fetch operations are within acceptable latency ranges.
- **Monitoring Recommendations**:
 - Set appropriate latency thresholds based on the requirements of the application.
 - Alert if the latency consistently exceeds the defined thresholds.
 - Analyze trends over time to detect degradation in performance and investigate the underlying causes.

## Logging and log4j Configuration (CCDAK)

- Kafka brokers and tools use **Log4j** (Kafka ≤ 3.x: `config/log4j.properties`; Kafka 4.0+ moved to **Log4j2**: `config/log4j2.yaml`). Clients (producer/consumer) use **SLF4J** — you supply the binding (log4j/logback) in your application.
- Key broker log files / appenders: `server.log` (general), `controller.log`, `state-change.log` (partition/replica state changes — useful for leader-election debugging), `kafka-request.log` (per request, `TRACE`/`DEBUG` only for debugging), `log-cleaner.log` (compaction), `kafka-authorizer.log` (ACL allow/deny audit).
- Appenders usually `DailyRollingFileAppender`/rolling file. Levels: `TRACE < DEBUG < INFO < WARN < ERROR < FATAL`.
- **Change at runtime** (no restart): `kafka-configs.sh --bootstrap-server ... --entity-type broker-loggers --entity-name 0 --alter --add-config kafka.server.KafkaApis=DEBUG` (dynamic logger levels via the Admin API / JMX `Log4jController`).
- Select the config at startup with `KAFKA_LOG4J_OPTS="-Dlog4j.configuration=file:/path/log4j.properties"` (Log4j2: `-Dlog4j2.configurationFile=`). `LOG_DIR` env var sets the log directory.
- **Don't confuse**: `server.log` (application logs, `LOG_DIR`) ≠ **data/commit logs** (`log.dirs`, the topic segments).
- Kafka Connect: `connect-log4j.properties`. Connect REST API can change logger levels at runtime: `PUT /admin/loggers/{logger}` with `{"level":"DEBUG"}`, and `GET /admin/loggers`. Connect adds connector context (`[connector|task-0]`) to log lines (`connector.client.config.override.policy`, MDC).
- Kafka Streams: log level for `org.apache.kafka.streams` — use `DEBUG` to see task assignment / state restoration.
- Avoid `DEBUG`/`TRACE` globally in production (volume and latency).

## Common Errors (CCDAK)

| Error / exception | Meaning / typical cause | Fix |
|---|---|---|
| `NotEnoughReplicasException` / `NotEnoughReplicasAfterAppendException` | ISR size < `min.insync.replicas` with `acks=all` | Restore brokers. Check `min.insync.replicas` vs RF |
| `NotLeaderOrFollowerException` (formerly `NotLeaderForPartition`) | Request sent to a broker that is no longer leader (retriable) | Metadata refresh happens automatically. Retries |
| `LeaderNotAvailableException` | Leader election in progress / no leader (retriable) | Wait/retry |
| `TimeoutException` (e.g. "Topic not present in metadata after max.block.ms", "Expiring N records... delivery.timeout.ms") | Broker unreachable, wrong `bootstrap.servers`/`advertised.listeners`, topic missing, or batch not delivered in time | Check connectivity/listeners, `delivery.timeout.ms`, `max.block.ms` |
| `RecordTooLargeException` / `MessageSizeTooLargeException` | Record > `max.request.size` / `message.max.bytes` | Raise limits consistently or reduce size/compress |
| `SerializationException` / `RecordDeserializationException` | Wrong or mismatched serializer/deserializer, bad data (poison pill) | Align serdes. Skip/DLQ bad record |
| `CommitFailedException` | Consumer lost partitions (rebalance, `max.poll.interval.ms` exceeded) before committing | Reduce `max.poll.records`, speed processing, raise `max.poll.interval.ms` |
| `RebalanceInProgressException` | Commit/operation during a rebalance | Retry after rebalance |
| `OffsetOutOfRangeException` | Offset deleted by retention or beyond end | `auto.offset.reset` or seek |
| `UnknownTopicOrPartitionException` | Topic doesn't exist (and auto-create disabled) | Create topic |
| `TopicAuthorizationException` / `GroupAuthorizationException` / `SaslAuthenticationException` | Missing ACL or bad credentials | Add ACLs. Check `sasl.jaas.config` |
| `SSLHandshakeException` / "unable to find valid certification path" | Bad truststore/keystore or hostname mismatch (`ssl.endpoint.identification.algorithm`) | Fix certs/SANs |
| `ProducerFencedException` / `InvalidProducerEpochException` | Another producer with the same `transactional.id` took over | Close fenced producer |
| `InvalidTopicException`, `InvalidReplicationFactorException` | RF > number of alive brokers, bad topic name | Fix request |
| `FencedInstanceIdException` | Duplicate `group.instance.id` | Unique ids per instance |
| Consumer stuck / constant rebalances | Processing time > `max.poll.interval.ms`, or heartbeat/`session.timeout.ms` too low | Tune poll/heartbeat settings |
| "Connection to node -1 could not be established" | Cannot reach bootstrap server / wrong listener | Check `advertised.listeners`, network, security protocol |

- **Retriable** errors (`NotLeaderOrFollower`, `LeaderNotAvailable`, `NotEnoughReplicas`, timeouts) are retried by the producer. **Non-retriable** (`RecordTooLarge`, `Serialization`, authorization) fail immediately.

## Configuring Alerts (CCDAK)

Alert on symptoms in these metrics (JMX / Prometheus / Burrow / Confluent Control Center):

| Metric | Alert condition | Meaning |
|---|---|---|
| `UnderReplicatedPartitions` | **> 0** for a sustained period | Followers are lagging / broker down — most important broker alert |
| `ActiveControllerCount` | **≠ 1** (sum across cluster) | 0 = no controller; >1 = split brain |
| `OfflinePartitionsCount` | **> 0** | Partitions with no leader — unavailable for read/write |
| `UnderMinIsrPartitionCount` | **> 0** | Producers with `acks=all` will fail |
| `IsrShrinksPerSec` / `IsrExpandsPerSec` | Frequent shrinks without expands | Unstable replicas / slow disks / network |
| `UncleanLeaderElectionsPerSec` | **> 0** | Possible data loss |
| `records-lag-max` / group lag (`kafka-consumer-groups.sh --describe`, Burrow) | Lag **growing** over time (not just high) | Consumers can't keep up |
| `RequestHandlerAvgIdlePercent` / `NetworkProcessorAvgIdlePercent` | < ~20–30 % | Broker thread pools saturated |
| `RequestQueueSize`, `TotalTimeMs` (Produce/Fetch) | Rising / above SLA | Latency problem |
| `BytesInPerSec` / `BytesOutPerSec` | Deviation from baseline / near NIC limit | Capacity |
| Disk usage of `log.dirs`, open file descriptors, JVM heap/GC pause | > 80 % / near limit | Resource exhaustion |
| Producer `record-error-rate`, `record-retry-rate` | Above 0 / rising | Delivery problems |
| Connect `connector-status`/ task `FAILED`, `deadletterqueue-produce-requests` | Task failed or DLQ growing | Pipeline errors |

- Alert on **rate of change / duration** (e.g. "URP > 0 for 5 min") instead of single spikes to avoid noise.
- Tools: Prometheus + JMX exporter + Alertmanager, Grafana, Datadog, Burrow (lag evaluation, status OK/WARN/ERR), Confluent Control Center.


## Exam Quick-Reference Cheat Sheet

| # | Trap |
|---|---|
| 1 | `UnderReplicatedPartitions > 0` = replicas lagging, NOT necessarily offline |
| 2 | `OfflinePartitionsCount > 0` = partitions with NO leader — writes/reads impossible |
| 3 | `ActiveControllerCount` must be exactly **1** — 0 means no controller, >1 is impossible in practice |
| 4 | Consumer lag is NOT a broker metric — check via `kafka-consumer-groups.sh` or consumer JMX |
| 5 | `records-lag-max` = max lag across all partitions for that consumer client |
| 6 | `UncleanLeaderElectionsPerSec > 0` means **data was lost** (out-of-sync replica became leader) |
| 7 | `NetworkProcessorAvgIdlePercent < 30%` → add network threads (`num.network.threads`) |
| 8 | `RequestHandlerAvgIdlePercent < 30%` → add I/O threads (`num.io.threads`) — dynamic config |
| 9 | `IsrShrinksPerSec` sustained high = brokers can't keep up with replication — investigate GC, disk, network |
| 10 | Per-topic metrics require `,topic=my-topic` appended to MBean name |
| 11 | Streams lag = internal consumer `records-lag-max` on repartition/source topics |
| 12 | Connect task status via REST (`/connectors/{name}/status`), not JMX alone |
| 13 | `record-error-rate > 0` on producer = failed sends (check `acks`, `retries`, broker health) |
| 14 | `buffer-available-bytes` dropping to 0 → producer blocked (`max.block.ms` will throw if exceeded) |
| 15 | `LeaderElectionRateAndTimeMs` elevated = broker instability — check GC pauses, disk I/O |
