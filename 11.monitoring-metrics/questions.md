> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 1

Which tool is commonly used to monitor Kafka cluster health and performance?

- A. Nagios
- B. Prometheus
- C. Elasticsearch
- D. Splunk

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Prometheus is widely used for monitoring Kafka cluster health and performance. It collects metrics from Kafka brokers, producers, and consumers, and stores them in a time-series database. Prometheus can be used with Grafana for visualizing these metrics.

- A, C, and D are incorrect because while Nagios, Elasticsearch, and Splunk can be used for monitoring and logging, Prometheus is more specialized for metrics collection and monitoring.

</details>

## Question 2

What is the primary purpose of JMX in the context of Kafka monitoring?

- A. To configure Kafka brokers
- B. To provide real-time logging of Kafka events
- C. To expose Kafka metrics for monitoring
- D. To manage Kafka ACLs

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
JMX (Java Management Extensions) is used to expose Kafka metrics for monitoring. Kafka brokers expose various metrics (such as broker metrics, topic metrics, and consumer group metrics) through JMX, which can be collected and monitored by tools like Prometheus.

- A is incorrect because JMX is not used for configuring Kafka brokers. B is incorrect because JMX is not primarily used for real-time logging. D is incorrect because JMX does not manage Kafka ACLs.

</details>

## Question 3

Which Kafka metric would you monitor to detect message delivery delays in a Kafka cluster?

- A. `MessagesInPerSec`
- B. `TotalTimeMs` (`kafka.network:type=RequestMetrics`, `request=Produce`/`FetchConsumer`)
- C. `UnderReplicatedPartitions`
- D. `BytesOutPerSec`

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The broker request metric `TotalTimeMs` (`kafka.network:type=RequestMetrics,name=TotalTimeMs,request=Produce|FetchConsumer|FetchFollower`) is the total time spent handling a request (queue, local, remote, response queue and send time). Monitoring it (e.g. the 99th percentile) helps detect delivery delays in a Kafka cluster.

- A, C, and D are incorrect because they measure different aspects: `MessagesInPerSec` measures the rate of messages being produced, `UnderReplicatedPartitions` indicates partition replication issues, and `BytesOutPerSec` measures the rate of bytes being consumed.

</details>

## 🚫 Question 4

Which of the following tools can be used to visualize Kafka metrics collected by Prometheus?

- A. Kibana
- B. Grafana
- C. Logstash
- D. Fluentd

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Grafana is a popular tool used to visualize metrics collected by Prometheus. It can create dashboards to monitor Kafka metrics and provide insights into cluster performance.

- A, C, and D are incorrect because while Kibana is used for visualizing data from Elasticsearch, Logstash and Fluentd are used for log processing, not for visualizing Prometheus metrics.

</details>

## Question 5

What does the Kafka metric `UnderReplicatedPartitions` indicate?

- A. The number of partitions without a leader
- B. The number of partitions that have fewer in-sync replicas than assigned replicas
- C. The number of partitions that are not receiving messages
- D. The number of partitions with high message latency

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The `UnderReplicatedPartitions` metric indicates the number of partitions whose in-sync replica set (ISR) is smaller than the full set of assigned replicas (i.e. at least one follower is out of sync or its broker is down). This metric helps identify potential data reliability issues in the Kafka cluster.

- A, C, and D are incorrect because they describe different aspects of Kafka partition health and performance (A is `OfflinePartitionsCount`).

</details>

## Question 6

Which Kafka metric should be monitored to ensure sufficient disk space on Kafka brokers?

- A. `LogEndOffset`
- B. `LogSegmentCount`
- C. `Size` (`kafka.log:type=Log,name=Size`)
- D. `MessageRate`

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
The per-partition log `Size` metric (`kafka.log:type=Log,name=Size`, in bytes) shows how much disk each partition log uses, so summing it per broker helps predict disk exhaustion. Kafka itself does not expose free disk space over JMX (`FreeStorageSpace` is not a Kafka metric); free space must be monitored at the OS level.

- A, B, and D are incorrect because `LogEndOffset` is an offset, `LogSegmentCount` (the real metric is `NumLogSegments`) counts segments, and `MessageRate` is not a Kafka metric; none of them report disk usage.

</details>

## 🚫 Question 7

What is the role of Kafka Exporter in a Kafka monitoring setup?

- A. To collect logs from Kafka brokers
- B. To expose Kafka metrics to Prometheus
- C. To configure Kafka broker settings
- D. To manage Kafka consumer groups

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Kafka Exporter is used to expose Kafka metrics to Prometheus. It collects metrics from Kafka brokers and provides them in a format that Prometheus can scrape and store for monitoring purposes.

- A, C, and D are incorrect because Kafka Exporter does not collect logs, configure broker settings, or manage consumer groups.

</details>

## Question 8

Which broker request-metric component captures the time a produce request (acks=all) waits for the follower replicas to replicate it?

- A. `RemoteTimeMs`
- B. `FetchLatency`
- C. `ProducerLatency`
- D. `ISRTime`

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
`RemoteTimeMs` (`kafka.network:type=RequestMetrics,name=RemoteTimeMs,request=Produce`) is the time a request waits for the followers; with `acks=all` it is the time until all in-sync replicas have the record. A large value points to slow replication.

- B, C, and D are incorrect because `FetchLatency`, `ProducerLatency` and `ISRTime` are not standard Kafka broker metrics.

</details>

## Question 9

Why is it important to monitor the `RequestsPerSec` metric in Kafka?

- A. To measure the number of messages being produced
- B. To measure the number of bytes being consumed
- C. To measure the rate of requests being handled by Kafka brokers
- D. To measure the number of partitions

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Monitoring the `RequestsPerSec` metric (`kafka.network:type=RequestMetrics,name=RequestsPerSec,request=...`) is important because it measures the rate of requests being handled by Kafka brokers. High request rates can indicate high load on the brokers, which may affect their performance.

- A, B, and D are incorrect because they describe different aspects of Kafka performance and health.

</details>

## Question 10

What does the Kafka metric `ConsumerLag` indicate?

- A. The number of messages a consumer has consumed
- B. The number of messages a consumer is behind in processing
- C. The time a consumer takes to process a message
- D. The number of partitions a consumer is subscribed to

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Consumer lag is the number of messages (log-end offset minus committed/current offset) a consumer is behind. It is not a single broker JMX bean: clients expose `records-lag-max` (and per-partition `records-lag`), and lag can also be read with `kafka-consumer-groups.sh --describe` or external tools such as Burrow. It is a crucial metric for ensuring that consumers are keeping up with the message production rate and not falling behind.

- A, C, and D are incorrect because they describe different aspects of consumer performance and subscriptions.

</details>

## Question 11

Which Kafka metric would you monitor to identify potential leader election issues?

- A. `LeaderElectionRateAndTimeMs`
- B. `RequestsPerSec`
- C. `MessagesInPerSec`
- D. `ISRTime`

<details>
<summary>Response:</summary> 

**Explanation:**

`LeaderElectionRateAndTimeMs` is the Kafka metric that indicates the rate and time taken for leader elections. Monitoring this metric can help identify potential issues with leader election processes within the Kafka cluster.

- B, C, and D are incorrect because they do not specifically measure leader election-related metrics.

**Answer:** A

</details>

## Question 12

What is the purpose of the `ActiveControllerCount` metric in Kafka?

- A. To count the number of active consumers
- B. To indicate the number of active brokers
- C. To show the number of active controller nodes
- D. To measure the rate of message production

<details>
<summary>Response:</summary> 

**Explanation:**

The `ActiveControllerCount` metric indicates the number of active controller nodes in a Kafka cluster. There should be exactly one active controller in a healthy Kafka cluster: each controller-capable node reports 1 (active) or 0, so the sum across the cluster must be 1.

- A, B, and D are incorrect because they measure different aspects of Kafka performance and health.

**Answer:** C

</details>

## Question 13

Which Kafka metric helps in monitoring the health of consumer groups?

- A. `ConsumerLag`
- B. `ProducerRequestRate`
- C. `BytesOutPerSec`
- D. `FetchLatency`

<details>
<summary>Response:</summary> 

**Explanation:**

Consumer lag (client metric `records-lag-max`, or lag reported by `kafka-consumer-groups.sh`) helps in monitoring the health of consumer groups by indicating how far behind a consumer group is in processing messages. This metric is crucial for ensuring timely message consumption.

- B, C, and D are incorrect because they measure different aspects of Kafka performance and health.

**Answer:** A

</details>

## 🚫 Question 14

Which tool can be used to collect JMX metrics from Kafka brokers for monitoring?

- A. Logstash
- B. JConsole
- C. Metricbeat
- D. Telegraf

<details>
<summary>Response:</summary> 

**Explanation:**

Telegraf is a tool that can be used to collect JMX metrics from Kafka brokers for monitoring (e.g. via its Jolokia input plugin, which reads JMX over HTTP). It can be configured to scrape metrics and forward them to a monitoring system like InfluxDB or Prometheus.

- A, B, and C are incorrect because while Logstash and Metricbeat can be used for other monitoring tasks, JConsole is typically used for viewing JMX metrics interactively, not for automated metric collection.

**Answer:** D

</details>

## Question 15

What does the `BytesOutPerSec` metric (`kafka.server:type=BrokerTopicMetrics`) measure in Kafka?

- A. The number of bytes produced to a topic per second
- B. The number of bytes consumed from a topic per second
- C. The number of bytes replicated per second
- D. The number of bytes stored in a topic

<details>
<summary>Response:</summary> 

**Explanation:**

The `BytesOutPerSec` metric measures the number of bytes consumed (fetched by consumers) from a topic or broker per second; replication traffic is reported separately by `ReplicationBytesOutPerSec`. It provides insights into the data throughput on the consumer side.

- A, C, and D are incorrect because they describe different aspects of data flow and storage in Kafka.

**Answer:** B

</details>

## Question 16

Which metric should be monitored to detect uneven leader distribution across brokers in a Kafka cluster?

- A. `PartitionCount`
- B. `LeaderCount`
- C. `UnderReplicatedPartitions`
- D. `PartitionLoad`

<details>
<summary>Response:</summary> 

**Explanation:**

`LeaderCount` (`kafka.server:type=ReplicaManager,name=LeaderCount`) is the number of partitions a broker leads; comparing it across brokers reveals leader imbalance (clients produce to and fetch from leaders), which can be fixed by preferred leader election.

- A is incorrect because `PartitionCount` counts all replicas on a broker, not leadership. C indicates replication problems, not imbalance. D, `PartitionLoad`, is not a Kafka metric.

**Answer:** B

</details>

## Question 17

Which Kafka metric indicates the rate of log flush operations?

- A. `LogFlushRateAndTimeMs`
- B. `DiskFlushRate`
- C. `LogRetentionRate`
- D. `FlushTime`

<details>
<summary>Response:</summary> 

**Explanation:**

`LogFlushRateAndTimeMs` is the Kafka metric that indicates the rate and time of log flush operations. This metric helps monitor how often logs are being flushed to disk, which is critical for data durability and performance.

- B, C, and D are incorrect because they either do not exist or measure different aspects of Kafka performance.

**Answer:** A

</details>

## Question 18

What is the significance of the `RequestQueueSize` metric in Kafka?

- A. It measures the number of requests waiting to be processed by Kafka brokers.
- B. It indicates the number of active consumer requests.
- C. It shows the total number of requests handled by Kafka brokers.
- D. It measures the size of the message queue in bytes.

<details>
<summary>Response:</summary> 

**Explanation:**

The `RequestQueueSize` metric measures the number of requests waiting to be processed by Kafka brokers. A high value may indicate that brokers are overloaded and unable to process requests in a timely manner.

- B, C, and D are incorrect because they measure different aspects of request handling and message queuing.

**Answer:** A

</details>

## Question 19

Which Kafka metric would you monitor to understand the latency experienced by producers?

- A. `ProducerRequestRate`
- B. `ProducerLatency`
- C. `RequestQueueSize`
- D. `RequestQueueTimeMs` (`request=Produce`)

<details>
<summary>Response:</summary> 

**Explanation:**

`RequestQueueTimeMs` (`kafka.network:type=RequestMetrics,name=RequestQueueTimeMs,request=Produce`) measures the time produce requests wait in the broker request queue; `TotalTimeMs` and the producer client metric `request-latency-avg` give the end-to-end view. Monitoring this metric helps understand the delay producers face before their requests are processed by the broker.

- A, B, and C are incorrect because `ProducerLatency` and `ProducerRequestRate` are not standard broker metrics and `RequestQueueSize` counts queued requests, not time.

**Answer:** D

</details>

## Question 20

Which metric is critical for monitoring Kafka broker heap memory usage?

- A. `BrokerHeapMemoryUsed`
- B. `JvmMemoryUsage`
- C. `HeapMemoryUsage`
- D. `BrokerJvmHeap`

<details>
<summary>Response:</summary> 

**Explanation:**

`HeapMemoryUsage` is the attribute of the standard JVM MBean `java.lang:type=Memory`, which every JVM (including the Kafka broker) exposes over JMX. It shows heap used/committed/max, which is essential for identifying memory-related issues. Kafka does not define its own heap metric.

- A, B, and D are incorrect as they are not standard JMX/Kafka metric names.

**Answer:** C

</details>

## Question 21

How can the `client.id` setting be useful in monitoring and troubleshooting Kafka clients?

- A. It allows setting different configuration parameters for each client
- B. It enables tracking and correlating client activity in logs and metrics
- C. It determines the partitioning strategy used by the client
- D. It specifies the maximum number of connections the client can establish

<details>
<summary>Response:</summary> 

**Explanation:**

The `client.id` setting can be useful in monitoring and troubleshooting Kafka clients by enabling tracking and correlating client activity in logs and metrics. When the `client.id` is set to a unique value for each client, it becomes easier to identify and trace the behavior of individual clients within a Kafka cluster. Kafka brokers include the `client.id` in the metadata of requests received from the clients, allowing you to associate specific requests and activities with particular clients. This information is valuable for debugging and performance analysis. By examining the logs and metrics with the `client.id`, you can isolate issues, track message flow, and understand the behavior of specific clients, facilitating effective troubleshooting and monitoring.

**Answer:** B

</details>
