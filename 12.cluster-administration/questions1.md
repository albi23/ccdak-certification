> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 1

Which of the following were stored in ZooKeeper for a ZooKeeper-based Kafka cluster (Kafka 3.x and earlier; ZooKeeper was removed in Kafka 4.0)? (Select two)

- A. Consumer offsets
- B. Kafka broker information (registrations)
- C. Producer client IDs
- D. Topic-level configurations
- E. Message payloads

<details>
<summary>Response:</summary> 

**Answer:** B, D

**Explanation:**
In ZooKeeper mode (Kafka 3.x and earlier), ZooKeeper stored cluster metadata. This included:

- Broker registrations (ephemeral znodes under `/brokers/ids`).
- Topic-level configurations (`/config/topics`), as well as topic/partition assignments (`/brokers/topics`), ACLs and the controller election znode.

The other options are stored elsewhere:

- A: Consumer offsets are stored in the `__consumer_offsets` topic in Kafka itself (not in ZooKeeper, for modern consumers).
- C: Producer client IDs are not stored anywhere; they are just identifiers used in client requests and quotas/metrics.
- E: Message payloads are stored in partition logs on brokers.

Note: since Kafka 4.0 (KRaft only) none of this lives in ZooKeeper; cluster metadata is kept in the `__cluster_metadata` log managed by the KRaft controller quorum. (The original question listed "Topic partition assignments" as a distractor, but in ZooKeeper mode those were stored in ZooKeeper too, so the option was replaced.)

</details>

## Question 2

In a Kafka cluster, you have a topic with 6 partitions and a replication factor of 3. How many replicas of each partition will be spread across the brokers?

- A. 1 replica per partition
- B. 2 replicas per partition
- C. 3 replicas per partition
- D. 6 replicas per partition

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In Kafka, the replication factor determines the number of copies (replicas) of each partition that will be maintained across the brokers in the cluster. When you create a topic with a specific replication factor, Kafka ensures that each partition has the specified number of replicas distributed across different brokers.

In this case, with a replication factor of 3, each partition will have 3 replicas. These replicas will be spread across different brokers in the cluster to provide fault tolerance and high availability.

Here's how the replicas will be distributed:

- Each partition will have one leader replica and two follower replicas.
- The leader replica handles all produce requests and, by default, all consume requests for the partition.
- The follower replicas continuously replicate the data from the leader replica to maintain an identical copy.
- In-sync follower replicas are ready to take over as the leader if the current leader fails.

With 6 partitions and a replication factor of 3, there will be a total of 18 replicas (6 partitions × 3 replicas per partition) distributed across the brokers in the cluster. Kafka will automatically assign the replicas to different brokers to ensure data redundancy and fault tolerance.

It's important to note that the number of replicas per broker may vary depending on the number of brokers in the cluster and how Kafka distributes the replicas. Kafka aims to evenly distribute the replicas across the available brokers to balance the load and ensure optimal performance.

</details>

## Question 3

What happens to the replicas when a broker in a Kafka cluster goes down?

- A. All replicas on the failed broker are permanently lost
- B. The replicas on the failed broker are automatically redistributed to other brokers
- C. The replicas on the failed broker become unavailable until the broker is restarted
- D. The replicas on the failed broker are immediately promoted to be leaders on other brokers

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When a broker in a Kafka cluster goes down, the replicas hosted on that broker become unavailable until the broker is restarted. Kafka is designed to handle broker failures and ensure data integrity and availability through replication.

Here's what happens to the replicas when a broker fails:

1. The replicas hosted on the failed broker become inaccessible.
2. For partitions where the failed broker was hosting the leader replica:
   - One of the follower replicas on another broker is promoted to become the new leader.
   - Clients (producers and consumers) automatically reconnect to the new leader replica.
   - The new leader starts accepting read and write operations for the partition.
3. For partitions where the failed broker was hosting a follower replica:
   - The leader replica on another broker continues to serve read and write operations.
   - The follower replicas on other brokers continue to replicate data from the leader.
4. When the failed broker is restarted:
   - It rejoins the cluster and starts catching up with the latest data from the leader replicas.
   - Once the replicas on the restarted broker are fully caught up, they can serve as leaders or followers again.

It's important to note that while the replicas on the failed broker are unavailable, Kafka maintains data availability and integrity through replication on other brokers. As long as there are enough in-sync replicas (ISRs) available, Kafka can continue serving read and write operations for the affected partitions.

However, if the number of in-sync replicas falls below the configured `min.insync.replicas` setting, producers using `acks=all` will receive `NotEnoughReplicas` errors and writes are rejected to prevent data loss (reads continue).

</details>

## Question 4

How does Kafka ensure data integrity and consistency across replicas?

- A. By using a two-phase commit protocol
- B. By relying on ZooKeeper for distributed consensus
- C. By implementing a leader-follower replication model
- D. By using a gossip protocol for eventual consistency

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Kafka ensures data consistency across replicas by implementing a leader-follower replication model. In this model, each partition has one leader replica and zero or more follower replicas.

Here's how Kafka maintains data integrity and consistency:

1. Leader replica:
   - The leader replica is responsible for handling all produce requests (and by default consume requests) for a partition.
   - When a producer writes data to a partition, it sends the data to the leader replica.
   - The leader replica appends the data to its log and assigns it an offset.
2. Follower replicas:
   - The follower replicas continuously replicate data from the leader replica.
   - They fetch new data from the leader and append it to their own logs.
   - The follower replicas aim to stay in sync with the leader by replicating data as quickly as possible.
3. In-sync replicas (ISRs):
   - An in-sync replica is a replica (leader or follower) that is fully caught up with the leader and has all the latest data.
   - The set of in-sync replicas is maintained by the leader and communicated to the cluster controller.
   - Only in-sync replicas are eligible to become the leader in case of a failure.
4. Consistency guarantees:
   - Kafka considers data committed only when it has been replicated to all replicas currently in the ISR (high watermark); with `acks=all` and `min.insync.replicas` the producer gets the guarantee.
   - Options A and D are incorrect: Kafka uses neither two-phase commit nor gossip for replication. Option B is incorrect: ZooKeeper (removed in 4.0) was used for controller election/metadata, not for replicating data; replication is done by followers fetching from the leader.
   - Producers can specify the `acks` configuration to control the level of durability (default is `acks=all` since Kafka 3.0).
   - Consumers only read up to the high watermark (committed data), normally from the leader replica (follower fetching, KIP-392, is optional).

Using this leader-follower replication model, Kafka ensures that data is consistently replicated across multiple brokers. The leader replica acts as the authoritative source of data, and the follower replicas continuously replicate data from the leader to maintain consistency.

Kafka's replication mechanism provides fault tolerance, high availability, and data durability. If a leader replica fails, one of the in-sync follower replicas is automatically promoted to be the new leader, ensuring continued availability of data.
