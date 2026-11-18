> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 11
What is the purpose of the `kafka-dump-log` tool in KRaft mode?

- A. To display the contents of the KRaft metadata log
- B. To modify the Kafka broker configuration
- C. To list the available Kafka topics
- D. To monitor the Kafka cluster performance

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In KRaft mode, the `kafka-dump-log` tool is used to display the contents of the KRaft metadata log. It allows you to inspect the log segments and snapshots for the cluster metadata directory.

By running the `kafka-dump-log` tool with the `--cluster-metadata-decoder` flag and specifying the path to the metadata log files, you can decode and print the records in the log segments. For example:

bin/kafka-dump-log.sh --cluster-metadata-decoder --files /path/to/kraft/metadata/log/00000000000000000000.log

This command will scan the specified log files and decode the metadata records, providing insights into the contents of the KRaft metadata log.

B is incorrect because modifying the Kafka broker configuration is not the purpose of the `kafka-dump-log` tool. Broker configurations are typically modified using the `server.properties` file or the `kafka-configs` tool.

C is incorrect because listing the available Kafka topics is not the responsibility of the `kafka-dump-log` tool. You can use the `kafka-topics` tool to list the existing topics in the cluster.

D is incorrect because monitoring the Kafka cluster performance is not the primary function of the `kafka-dump-log` tool. There are dedicated monitoring tools and metrics for tracking cluster performance.

</details>

## 🚫 Question 12
What is the purpose of the `kafka-metadata-shell` tool in KRaft mode?

- A. To modify the Kafka broker configuration
- B. To list the available Kafka topics
- C. To monitor the Kafka cluster performance
- D. To interactively inspect the KRaft metadata

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In KRaft mode, the `kafka-metadata-shell` tool is used to interactively inspect the KRaft metadata. It provides a shell-like interface for exploring the contents of the metadata log and examining the state of the cluster.

By running the `kafka-metadata-shell` tool and specifying a metadata snapshot file (a `.checkpoint` file in the metadata log directory), you can enter an interactive shell where you can execute various commands to analyze the metadata. For example:

bin/kafka-metadata-shell.sh --snapshot /path/to/__cluster_metadata-0/00000000000000000100-0000000001.checkpoint

Once inside the shell, you can use commands like `ls` to list the available metadata directories, `cat` to view the contents of specific metadata files, and navigate through the metadata hierarchy.

The `kafka-metadata-shell` tool is particularly useful for debugging and troubleshooting purposes, as it allows you to inspect the internal state of the KRaft metadata in a user-friendly manner.

A is incorrect because modifying the Kafka broker configuration is not the purpose of the `kafka-metadata-shell` tool. Broker configurations are typically modified using the `server.properties` file or the `kafka-configs` tool.

B is incorrect because listing the available Kafka topics is not the responsibility of the `kafka-metadata-shell` tool. You can use the `kafka-topics` tool to list the existing topics in the cluster.

C is incorrect because monitoring the Kafka cluster performance is not the primary function of the `kafka-metadata-shell` tool. There are dedicated monitoring tools and metrics for tracking cluster performance.

</details>

## 🚫 Question 13
What is the significance of the `kafka.controller:type=KafkaController,name=LastCommittedRecordOffset` metric in KRaft mode?

- A. It indicates the offset of the last record that was applied by the controller to the metadata partition
- B. It represents the number of records that have been committed to the metadata partition
- C. It measures the lag between the active controller and the last committed record in the metadata partition
- D. It tracks the offset of the last record that was committed by the active controller

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In KRaft mode, the `kafka.controller:type=KafkaController,name=LastCommittedRecordOffset` metric holds significant importance as it tracks the offset of the last record that was committed by the active controller in the metadata partition.

The active controller is responsible for committing records to the metadata partition, which contains crucial information about the cluster's state, such as topic configurations, partition assignments, and broker metadata. (Docs: "The offset of the last record committed to this Controller.") The `LastCommittedRecordOffset` metric provides visibility into the progress of the active controller in terms of committing these important records.

Monitoring the `LastCommittedRecordOffset` metric is essential for ensuring that the active controller is making progress and committing new records to the metadata partition. It allows you to track the latest committed offset and detect any potential issues or delays in the commitment process.

A is incorrect because the metric represents the offset of the last committed record, not the last applied record. The last applied record is tracked by a different metric, `LastAppliedRecordOffset`.

B is incorrect because the metric represents the offset of the last committed record, not the total number of committed records.

C is incorrect because the metric does not measure the lag between the active controller and the last committed record. The lag is tracked by a separate metric, `kafka.controller:type=KafkaController,name=LastAppliedRecordLagMs`.

</details>

## 🚫 Question 14
What is the purpose of the `metadata.max.idle.interval.ms` configuration in KRaft mode?

- A. To set the maximum time allowed for a metadata request to be idle before it is cancelled
- B. To specify the maximum time the active controller can be idle before a new controller is elected
- C. To configure the frequency at which the active controller writes no-op records to the metadata partition
- D. To define the maximum interval allowed between two consecutive metadata log segments

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In KRaft mode, the `metadata.max.idle.interval.ms` configuration is used to specify the frequency at which the active controller writes no-op records to the metadata partition.

No-op records, short for "no operation" records, are dummy records that the active controller periodically appends to the metadata partition. These records let the high watermark advance and let followers/brokers observe progress when there are no real metadata changes.

By setting the `metadata.max.idle.interval.ms` configuration, you can control how often the active controller writes these no-op records. The default value is 500 milliseconds (not verified against the docs page; check your Kafka version), which means that if no other records are being appended, the active controller writes a no-op record about every 500 ms. A value of 0 disables no-op records.

Writing no-op records helps in maintaining the liveness of the metadata partition and ensures that the followers can continuously replicate the latest metadata changes. 
A is incorrect because the `metadata.max.idle.interval.ms` configuration is not related to the idleness of metadata requests. It pertains to the idleness of the metadata partition itself.

B is incorrect because the configuration does not specify the maximum idle time for the active controller before a new controller is elected. Controller election is governed by a separate mechanism.

D is incorrect because the configuration does not define the maximum interval between consecutive metadata log segments. It controls the frequency of writing no-op records within a single log segment.

</details>

## 🚫 Question 15
What does the `MaxFollowerLag` value reported by `kafka-metadata-quorum describe --status` indicate in KRaft mode?

- A. It measures the maximum lag between the active controller and the last committed record in the metadata partition
- B. It indicates the maximum lag between the active controller and the followers in terms of metadata records
- C. It represents the maximum number of records that a follower can lag behind the active controller
- D. It tracks the maximum lag between the followers and the last applied record in the metadata partition

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In KRaft mode, the `MaxFollowerLag` field of `kafka-metadata-quorum describe --status` (it is reported by the quorum tool, not a `kafka.controller` MBean) plays a crucial role in monitoring the health and synchronization of the KRaft controllers. It indicates the maximum lag between the active controller and the followers in terms of metadata records.

The active controller is responsible for appending new records to the metadata partition and advancing the high watermark. The followers continuously replicate these records from the active controller to stay in sync with the latest metadata changes.

The `MaxFollowerLag` metric measures the maximum lag, in terms of the number of records, between the active controller's log end offset (LEO) and the followers' LEO. In other words, it represents how far behind the slowest follower is compared to the active controller.

Monitoring the `MaxFollowerLag` metric is essential to ensure that the followers are keeping up with the active controller and are not falling behind in replicating the metadata records. A high value of `MaxFollowerLag` indicates that one or more followers are lagging significantly, which can impact the overall consistency and reliability of the KRaft cluster.

A is incorrect because the metric measures the lag between the active controller and the followers, not the lag between the active controller and the last committed record.

C is incorrect because the metric represents the actual lag in terms of the number of records, not the maximum allowed lag.

D is incorrect because the metric measures the lag between the active controller and the followers, not the lag between the followers and the last applied record.

</details>

## 🚫 Question 16
What is the significance of the `kafka.server:type=SnapshotEmitter,name=LatestSnapshotGeneratedAgeMs` metric in KRaft mode?

- A. It indicates the age of the latest snapshot in milliseconds since the snapshot was generated
- B. It measures the time taken to generate the latest snapshot in milliseconds
- C. It represents the age of the latest snapshot in milliseconds since the process was started
- D. It tracks the time elapsed since the latest snapshot was loaded in milliseconds

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In KRaft mode, the `kafka.server:type=SnapshotEmitter,name=LatestSnapshotGeneratedAgeMs` metric holds significance as it indicates the age of the latest snapshot in milliseconds since the snapshot was generated.

Snapshots play a vital role in the KRaft consensus protocol. They are used to capture the state of the metadata log at a particular point in time and provide a compact representation of the metadata. Snapshots help in reducing the size of the metadata log and enable faster recovery of the controllers during startup or failover.

The `LatestSnapshotGeneratedAgeMs` metric provides information about how long ago the latest snapshot was generated. It measures the time elapsed since the snapshot was created, expressed in milliseconds.

Monitoring the `LatestSnapshotGeneratedAgeMs` metric is important for understanding the freshness of the snapshots and ensuring that snapshots are being generated regularly. A high value of this metric indicates that the latest snapshot is relatively old, and it may be beneficial to trigger a new snapshot generation to capture the latest state of the metadata log.

B is incorrect because the metric measures the age of the latest snapshot, not the time taken to generate it.

C is incorrect because the metric represents the age of the snapshot since it was generated, not since the process was started.

D is incorrect because the metric tracks the age of the generated snapshot, not the time elapsed since the snapshot was loaded.

</details>

## 🚫 Question 17
What does the `kafka.controller:type=KafkaController,name=FencedBrokerCount` metric report in KRaft mode?

- A. The number of brokers that have failed a controlled shutdown
- B. The number of brokers observed by this controller as fenced (e.g. missed heartbeats or shutting down)
- C. The number of brokers currently serving as controllers
- D. The number of topics being deleted

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In KRaft mode, brokers send heartbeats to the active controller; a broker that stops heartbeating (or is shutting down) is fenced, and fenced brokers cannot lead partitions. `FencedBrokerCount` is the number of fenced brokers observed by the controller, while `ActiveBrokerCount` is the number of active ones.

A, C and D are incorrect: there is no controlled-shutdown-count metric in KRaft (the original question used a ZooKeeper-era name that does not exist in current docs), brokers and controllers are separate processes in production, and topic deletion is not reported by this metric.

</details>

## 🚫 Question 18
What is the significance of the `kafka.controller:type=KafkaController,name=GlobalTopicCount` metric in KRaft mode?

- A. It represents the total number of topics in the Kafka cluster
- B. It indicates the number of global topics that are not associated with any specific cluster
- C. It measures the number of topics that have global replication enabled
- D. It tracks the count of topics that are globally accessible across all Kafka clusters

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In KRaft mode, the `kafka.controller:type=KafkaController,name=GlobalTopicCount` metric holds significance as it represents the total number of topics in the Kafka cluster.

The Kafka controller is responsible for managing the topic metadata and maintaining a consistent view of the topics across the cluster. The `GlobalTopicCount` metric provides a count of all the topics that exist in the cluster, as observed by this controller.

Monitoring the `GlobalTopicCount` metric gives you an overview of the topic landscape in your Kafka cluster. It allows you to track the growth of topics over time and helps in capacity planning and resource allocation. An increasing trend in the `GlobalTopicCount` metric indicates that new topics are being created, while a decreasing trend suggests that topics are being deleted.

Additionally, the `GlobalTopicCount` metric can be useful for monitoring the overall health and performance of the Kafka cluster. A sudden spike in the topic count may indicate a misconfiguration or an unexpected behavior that requires investigation.

B is incorrect because the metric does not specifically indicate the number of global topics that are not associated with any cluster. It represents the total number of topics within a single Kafka cluster.

C is incorrect because the metric does not measure the number of topics with global replication enabled. Topic replication is configured on a per-topic basis and is not directly related to the `GlobalTopicCount` metric.

D is incorrect because the metric tracks the count of topics within a single Kafka cluster, not across all Kafka clusters. Topics are typically specific to a particular cluster and are not globally accessible across different clusters.

</details>

## 🚫 Question 19
What does the `kafka.controller:type=KafkaController,name=GlobalPartitionCount` metric report in KRaft mode?

- A. The number of global partitions as observed by this controller
- B. The number of partitions that are under-replicated
- C. The number of partitions that have been deleted
- D. The number of partitions per broker

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
`GlobalPartitionCount` is "the number of global partitions as observed by this Controller" (counterpart of `GlobalTopicCount`). Under-replicated partitions are reported by the broker metric `kafka.server:type=ReplicaManager,name=UnderReplicatedPartitions`, and offline partitions by `OfflinePartitionsCount`. The original question used `TopicDeletionCount`, which is not in the documented KRaft metrics.

</details>

## 🚫 Question 20
What does the `kafka.controller:type=KafkaController,name=PreferredReplicaImbalanceCount` metric report in KRaft mode?

- A. The number of partitions whose current leader is not the preferred replica
- B. The number of replicas that are out of the ISR
- C. The number of topics whose replication factor changed
- D. The rate of topic creations

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
`PreferredReplicaImbalanceCount` counts partitions where the leader is not the preferred (first-listed) replica. It is the signal behind automatic leader rebalancing (`auto.leader.rebalance.enable`, `leader.imbalance.check.interval.seconds`, `leader.imbalance.per.broker.percentage`). The original question's `TopicChangeRate` metric is not part of the documented KRaft metrics and the question had no answer.

</details>

