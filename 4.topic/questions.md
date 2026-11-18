## Question 1

Which of the following statements about `acks` and `min.insync.replicas` are true? (Select all that apply)

- A. `acks` is a producer configuration, while `min.insync.replicas` is a topic configuration
- B. `acks` and `min.insync.replicas` are both producer configurations
- C. `acks` and `min.insync.replicas` are both topic configurations
- D. `acks=all` and `min.insync.replicas=1` provides the strongest durability guarantee
- E. `acks=1` and `min.insync.replicas=2` provides the strongest durability guarantee
- F. For `acks=all` to provide any additional durability over `acks=1`, `min.insync.replicas` must be greater than 1

<details>
<summary>Response:</summary> 

**Answer:** A, F

**Explanation:**
`acks` and `min.insync.replicas` are two crucial configurations in Kafka that work together to control the durability of writes:

- `acks` is a producer configuration that specifies how many acknowledgments the producer requires the leader to have received before considering a write successful (`acks=all` is the default since Kafka 3.0).
- `min.insync.replicas` is a topic-level configuration (which can also be set as a broker default) that specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful.

With `acks=all` the leader waits for all current in-sync replicas, but `min.insync.replicas` is what enforces a minimum ISR size (otherwise the write fails with `NotEnoughReplicas`). For `acks=all` to provide a real durability guarantee over `acks=1`, `min.insync.replicas` must be greater than 1. If `min.insync.replicas=1`, the ISR may shrink to just the leader, and then `acks=all` is effectively equivalent to `acks=1`: the leader acknowledges as soon as the write is in its own log.

- B and C are incorrect because `acks` and `min.insync.replicas` are configurations at different levels (producer and topic/broker, respectively).
- D is incorrect because `acks=all` with `min.insync.replicas=1` gives no guarantee beyond the leader when the ISR shrinks to the leader only.
- E is incorrect because `acks=1` does not interact with `min.insync.replicas` at all, so this combination does not provide the strongest durability guarantee.

</details>

## Question 2

What is the relationship between `unclean.leader.election.enable` and `min.insync.replicas`?

- A. They control the same thing and should always be set to the same value
- B. `unclean.leader.election.enable` overrides `min.insync.replicas`
- C. They are independent and one does not affect the other
- D. If `unclean.leader.election.enable=true`, `min.insync.replicas` can be violated during leader election

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
`unclean.leader.election.enable` and `min.insync.replicas` are two Kafka configurations that can interact in certain scenarios:

- `unclean.leader.election.enable` is a broker-level (and topic-level overridable) configuration, `false` by default, that controls whether a replica that is out of sync with the leader can be elected as the new leader if the existing leader fails.
- `min.insync.replicas` is a topic-level configuration that specifies the minimum number of replicas that must be in-sync with the leader for writes to succeed.

Normally, a replica that is not fully in-sync with the leader cannot be elected as the new leader. This protects against data loss, as an out-of-sync replica may be missing some of the latest messages.

However, if `unclean.leader.election.enable` is set to `true`, this protection is disabled. In this case, if all the in-sync replicas fail and only out-of-sync replicas remain, one of those out-of-sync replicas can be elected as the new leader. The new leader may be missing committed records (data loss), and writes can continue even though fewer than `min.insync.replicas` in-sync replicas had the data. It trades consistency for availability.

- A and C are incorrect because the two configurations do not control the same thing and they are not completely independent.
- B is incorrect because `unclean.leader.election.enable` does not override `min.insync.replicas`, it just allows it to be violated in certain edge cases.

</details>

## Question 3

A Kafka cluster has 3 brokers. You create a topic with 6 partitions and 2 consumers in a consumer group subscribed to this topic. With the default partition assignors and both consumers healthy, how many partitions is each consumer assigned?

- A. 1
- B. 2
- C. 3
- D. 6

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In Kafka, the number of partitions assigned to each consumer in a consumer group depends on the total number of partitions and the number of consumers. The built-in assignors (range, round-robin, sticky, cooperative-sticky) spread partitions evenly, and the number of brokers is irrelevant.

With 6 partitions and 2 consumers, each consumer is assigned 3 partitions. Only if one consumer leaves or fails would the remaining consumer temporarily receive all 6.

It's important to note that having more partitions than consumers is a valid and common configuration. It allows for adding more consumers later to scale out consumption throughput.

- A and B are incorrect because 6 partitions are split over 2 consumers, so each gets 3. D would happen only if the other consumer is not part of the group.

</details>

## Question 4

A topic has 10 partitions and a replication factor of 3. There are 2 consumers in a consumer group subscribed to this topic. The cluster has 5 brokers. How would the partitions be assigned to the consumers to achieve maximum throughput?

- A. Consumer 1: Partitions 0-4, Consumer 2: Partitions 5-9
- B. Consumer 1: Partitions 0-9 and 0-1 replicas, Consumer 2: Partitions 0-9 and 3. replicas
- C. Consumer 1: Partitions 0, 1, 2, Consumer 2: Partitions 3, 4, 5, Unassigned: 6, 7, 8, 9
- D. Consumer 1: Partitions 0-9

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
To achieve maximum throughput, Kafka aims to evenly distribute the partitions among the available consumers in a consumer group. This allows for parallel consumption of data.

In this case, with 10 partitions and 2 consumers, the optimal distribution for maximum throughput is:

- Consumer 1: Partitions 0, 1, 2, 3, 4
- Consumer 2: Partitions 5, 6, 7, 8, 9

This way, each consumer handles 5 partitions, and all partitions are being consumed concurrently.

The replication factor and the number of brokers do not directly affect the partition assignment to consumers. The replication factor is about data durability and the number of brokers is about the cluster's capacity, but the consumer-partition assignment is computed by the partition assignor (on the group leader consumer, or on the broker with the new KIP-848 consumer protocol) and is independent of replicas. Consumers read from partition leaders (unless follower fetching via `client.rack` is configured).

- B is not acceptable because consumer groups do not consume from different replicas.
- C is suboptimal because it leaves some partitions unassigned, reducing total throughput.
- D is incorrect because it assigns all partitions to a single consumer, eliminating the benefits of parallel consumption.

</details>

## Question 5

Which of the following statements about Kafka topic configurations is true?

- A. Topic configurations can only be set when a topic is first created and cannot be changed later
- B. Topic configurations can be changed dynamically using the `kafka-configs.sh` tool
- C. Topic configurations are stored in Zookeeper and are not accessible through the Kafka broker
- D. Topic configurations are stored in the Kafka broker's configuration file and require a broker restart to take effect

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In Kafka, topic configurations can be changed dynamically using the `kafka-configs.sh` tool without requiring a broker restart.

Kafka provides a way to modify topic configurations on the fly through the `kafka-configs.sh` command-line tool. This tool allows you to alter topic configurations such as retention policy and other topic-level settings. (The replication factor is not a config; it is changed with a partition reassignment.)

When you modify a topic configuration using `kafka-configs.sh`:

1. The updated configuration is stored in the cluster metadata (the KRaft metadata log managed by the controllers; in legacy ZooKeeper clusters it was stored in ZooKeeper).
2. The Kafka brokers receive the updated configuration and apply the changes to the topic.
3. The changes take effect without requiring a restart of the Kafka brokers.

This dynamic configuration capability allows for flexibility in managing topic settings without impacting the availability of the Kafka cluster.

Statement A is incorrect because topic configurations can be changed after a topic is created. You don't have to define all configurations upfront and stick with them permanently.

Statement C is incorrect. ZooKeeper was removed in Kafka 4.0; even in older ZooKeeper clusters the configs were readable through the brokers (Admin API, `kafka-configs.sh`).

Statement D is incorrect because per-topic configurations are not stored in the broker's configuration file (it holds only broker-wide defaults), and changes do not require a broker restart.

</details>

## Question 6

What is the default cleanup policy for Kafka topics?

- A. Delete
- B. Compact
- C. Delete and Compact
- D. None

<details>
<summary>Response:</summary> 

**Answer:** A


**Explanation:**
The default cleanup policy for Kafka topics is "Delete".

In Kafka, the cleanup policy determines how Kafka handles old log segments when the retention time or size limit is reached. There are two cleanup policies available (they can also be combined as `compact,delete`):

1. Delete: This is the default policy. When the retention time or size limit is reached, Kafka deletes old log segments to free up space. This means that old messages are permanently removed based on the retention configuration.

2. Compact: With the compact policy, Kafka periodically compacts the log by removing obsolete records based on the message key. If a key appears multiple times in the log, only the latest value is retained, and the older duplicates are discarded. This is useful for maintaining a changelog or snapshot of the latest state for each key.

By default, when you create a new topic in Kafka, `cleanup.policy=delete`. Kafka then automatically deletes old log segments based on `retention.ms` (default 7 days) or `retention.bytes`.

If you want to use the "Compact" policy for a topic, you need to explicitly set it using the topic configuration `cleanup.policy=compact`. This can be done when creating the topic or by modifying the topic configuration later.

Statements B and C are incorrect because they are not the default. "Compact" must be set explicitly, and "Delete and Compact" is a valid but non-default combination (`cleanup.policy=compact,delete`).

Statement D is incorrect because Kafka does have a default cleanup policy, which is "Delete". It is not the case that no cleanup policy is set by default.

</details>