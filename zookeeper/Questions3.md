> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 21
A new node started with `process.roles=broker` joins a KRaft cluster. Is it a voter in the controller quorum?

- A. Yes, every broker automatically becomes a voter
- B. No, it only registers with the controllers and replicates the metadata log as an observer; voters are only controller nodes
- C. No, and it cannot join until it is added to `controller.quorum.voters`
- D. Yes, it replaces one of the existing voters

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Only nodes with the `controller` role take part in the Raft quorum as voters. Brokers (`process.roles=broker`) register with the active controller, fetch the metadata log as observers and never vote. A broker needs `controller.quorum.voters` (static quorum) or `controller.quorum.bootstrap.servers` (dynamic quorum, Kafka 4.x) only to locate the controllers; it does not have to appear in that list.

A and D are incorrect because brokers never become voters. C is incorrect because brokers are not listed in the voters list at all.

</details>

## 🚫 Question 22
What does the `kafka.server:type=SnapshotEmitter,name=LatestSnapshotGeneratedBytes` metric report in KRaft mode?

- A. The total size in bytes of the latest snapshot that the node has generated
- B. The number of snapshots that failed due to a timeout
- C. The size of the whole metadata log directory
- D. The number of bytes fetched from the controller per second

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
Docs: "The total size in bytes of the latest snapshot that the node has generated." Together with `LatestSnapshotGeneratedAgeMs` it shows how large and how fresh the latest metadata snapshot is. The original question used `SnapshotGenerationTimeoutCount`, which does not exist in the documented KRaft metrics.

</details>

## 🚫 Question 23
In Kafka 4.x with a dynamic KRaft quorum, how is a controller safely removed from the voter set?

- A. Delete it from `controller.quorum.voters` on all nodes and restart
- B. Run `kafka-metadata-quorum remove-controller` for that controller before shutting it down
- C. Delete its metadata log directory
- D. Run `kafka-storage format` with a new cluster ID

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
With dynamic quorums (KIP-853, `controller.quorum.bootstrap.servers`) controllers are added with `kafka-metadata-quorum add-controller` (after the new controller has caught up) and removed with `remove-controller` before it is shut down. With a static quorum (`controller.quorum.voters`) membership is fixed and changing it requires coordinated config changes and rolling restarts.

The original question treated brokers as members of `controller.quorum.voters`, which is incorrect: voters are controller nodes only.

</details>

## 🚫 Question 24
What is the impact of setting the `controller.quorum.election.backoff.max.ms` configuration to a very high value in KRaft mode?

- A. It increases the frequency of controller elections, improving fault tolerance
- B. It reduces the time taken for a new controller to be elected, minimizing downtime
- C. It prolongs the time taken for a new controller to be elected, potentially increasing downtime
- D. It has no impact on the controller election process

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Setting the `controller.quorum.election.backoff.max.ms` configuration to a very high value in KRaft mode can prolong the time taken for a new controller to be elected, potentially increasing downtime.

In KRaft, when the active controller becomes unavailable or fails, a new controller (leader of the metadata log) needs to be elected from among the controller voters. The election process involves a backoff mechanism to prevent multiple controllers from simultaneously attempting to become the new controller, which could lead to conflicts and instability.

The `controller.quorum.election.backoff.max.ms` configuration specifies the maximum time in milliseconds before starting new elections; it is the upper bound of the exponential backoff used between election attempts (default 1000 ms).

If the `controller.quorum.election.backoff.max.ms` is set to a very high value, controllers will potentially wait for a longer duration before initiating the election process. This can delay the selection of a new controller and extend the period during which the cluster operates without an active controller.

Consequently, setting the `controller.quorum.election.backoff.max.ms` to a very high value can increase the downtime experienced by the cluster during controller failover scenarios. It may take longer for a new controller to be elected, resulting in a prolonged period of unavailability or limited functionality.

It is generally recommended to set the `controller.quorum.election.backoff.max.ms` to a reasonable value that balances the need for preventing conflicts with the desire for prompt controller election. The default value of 1000 milliseconds (1 second) is often suitable for most use cases.

A is incorrect because increasing the `controller.quorum.election.backoff.max.ms` does not increase the frequency of controller elections. It actually delays the election process.

B is incorrect because a higher value of `controller.quorum.election.backoff.max.ms` does not reduce the time taken for a new controller to be elected. Instead, it potentially increases the election time.

D is incorrect because the `controller.quorum.election.backoff.max.ms` configuration does have an impact on the controller election process by influencing the backoff duration.

</details>

## 🚫 Question 25
What is the purpose of the `kafka.controller:type=KafkaController,name=ActiveControllerCount` metric in KRaft mode?

- A. It indicates the number of active controllers in the KRaft cluster
- B. It represents the number of brokers currently serving as controllers
- C. It measures the count of controllers that have been active since the cluster started
- D. It tracks the number of controller failover events that have occurred

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In KRaft mode, the `kafka.controller:type=KafkaController,name=ActiveControllerCount` metric serves the purpose of indicating the number of active controllers in the KRaft cluster.

In a KRaft cluster, there should be exactly one active controller at any given time. The active controller is responsible for managing the cluster's metadata, performing leader election, and handling various administrative tasks. All other controllers in the cluster act as standby controllers, ready to take over if the active controller fails.

Each controller node reports 1 if it is the active controller and 0 otherwise; in a healthy KRaft cluster the sum is exactly 1.

Monitoring the `ActiveControllerCount` metric is crucial for ensuring the stability and proper functioning of the KRaft cluster. If the metric deviates from the expected value of 1, it suggests an issue with the controller quorum.

If the sum of `ActiveControllerCount` is 0, it means that there is no active controller in the cluster, indicating a potential failure or a problem with the controller election process. This situation can lead to a loss of cluster functionality and requires immediate attention.

If the sum is greater than 1, it suggests that there are multiple controllers claiming to be active simultaneously. This can happen due to network partitions or misconfiguration and can result in conflicts and inconsistencies in the cluster metadata.

B is incorrect because the metric represents the count of active controllers, not the number of brokers serving as controllers. In KRaft mode, the controllers are separate from the brokers.

C is incorrect because the metric indicates the current count of active controllers, not the cumulative count since the cluster started.

D is incorrect because the metric does not track the number of controller failover events. It represents the instantaneous count of active controllers at a given point in time.

</details>

## 🚫 Question 26
What is the significance of the `kafka.controller:type=KafkaController,name=LastAppliedRecordTimestamp` metric in KRaft mode?

- A. It indicates the timestamp of the last record appended to the metadata log
- B. It represents the timestamp of the last record replicated to all the controllers
- C. It measures the timestamp of the last record applied by the active controller
- D. It tracks the timestamp of the last record committed by the active controller

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
In KRaft mode, the `kafka.controller:type=KafkaController,name=LastAppliedRecordTimestamp` metric holds significance as it measures the timestamp of the last record applied by the active controller.

The active controller in a KRaft cluster is responsible for managing the metadata log and applying the records to update the cluster's state. When a record is appended to the metadata log, the active controller processes and applies the record to make the corresponding changes in the cluster metadata.

The `LastAppliedRecordTimestamp` metric captures the timestamp of the most recent record that the active controller has applied. It represents the point in time up to which the active controller has processed and applied the metadata records.

Monitoring the `LastAppliedRecordTimestamp` metric provides insights into the current state of the active controller and the progress of metadata application. It helps in understanding how up-to-date the active controller is in terms of processing the metadata log.

If the `LastAppliedRecordTimestamp` metric is lagging significantly behind the current time or the timestamp of the last appended record, it indicates that the active controller is experiencing delays in applying the metadata records. This could be due to performance issues, resource constraints, or a high volume of metadata changes.

On the other hand, if the `LastAppliedRecordTimestamp` metric is consistently close to the current time or the timestamp of the last appended record, it suggests that the active controller is efficiently processing and applying the metadata records without significant delays.

A is incorrect because the metric represents the timestamp of the last applied record, not the last appended record to the metadata log.

B is incorrect because the metric specifically measures the timestamp of the last record applied by the active controller, not the timestamp of the last record replicated to all the controllers.

D is incorrect because the metric tracks the timestamp of the last applied record, not the last committed record. The commitment of records is a separate process from the application of records by the active controller.

</details>

## 🚫 Question 27
What does the `kafka.controller:type=ControllerEventManager,name=EventQueueTimeMs` metric report in KRaft mode?

- A. A histogram of the time in milliseconds that requests spent waiting in the controller event queue
- B. The total size of the metadata log in bytes
- C. The number of active controller connections
- D. The time taken to generate a metadata snapshot

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
Docs: "A Histogram of the time in milliseconds that requests spent waiting in the Controller Event Queue." A consistently high value means the controller is struggling to keep up with the event backlog (heavy workload or limited resources). The original question used `ControllerChannelManager,name=TotalQueueSize`, a ZooKeeper-era controller metric that is not part of the documented KRaft metrics.

</details>

## 🚫 Question 28
What is the impact of having a large value for the `controller.quorum.request.timeout.ms` configuration in KRaft mode?

- A. It increases the time the controller waits for a quorum of voters to respond to a request
- B. It reduces the time the controller waits for a quorum of voters to respond to a request
- C. It sets the maximum time allowed for the controller to process a request
- D. It determines the frequency at which the controller sends heartbeats to the brokers

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In KRaft mode, setting a large value for the `controller.quorum.request.timeout.ms` configuration increases the time the controller waits for a quorum of voters to respond to a request.

The `controller.quorum.request.timeout.ms` configuration (default 2000 ms) is "the maximum amount of time the client will wait for the response of a request" sent between quorum members (e.g. Vote, Fetch, BeginQuorumEpoch requests). A larger value means a node waits longer before treating an unanswered quorum request as failed.

By setting a large value for `controller.quorum.request.timeout.ms`, you are allowing more time for the voters to respond to the controller's requests. This can be beneficial in scenarios where the voters are experiencing high load, network latency, or temporary issues that may delay their responses.

However, setting an excessively large value for `controller.quorum.request.timeout.ms` can also have drawbacks. If the timeout is set too high, it can prolong the time taken for the controller to detect and react to failures or unresponsive voters. This can impact the overall responsiveness and fault tolerance of the KRaft cluster.

It's important to strike a balance when configuring `controller.quorum.request.timeout.ms`. The value should be large enough to accommodate reasonable delays and allow for a quorum of voters to respond, but not so large that it significantly hinders the controller's ability to make timely decisions and maintain the cluster's stability.

The default value for `controller.quorum.request.timeout.ms` is 2000 milliseconds (2 seconds), which is suitable for most common scenarios. Adjusting this value requires careful consideration of the specific requirements and characteristics of your KRaft cluster.

B is incorrect because a larger value for `controller.quorum.request.timeout.ms` does not reduce the time the controller waits for a quorum of voters to respond. It actually increases the timeout duration.

C is incorrect because `controller.quorum.request.timeout.ms` does not set the maximum time allowed for the controller to process a request. It specifically relates to the timeout for receiving responses from voters.

D is incorrect because `controller.quorum.request.timeout.ms` does not determine the frequency at which the controller sends heartbeats to the brokers. Heartbeat configuration is controlled by separate parameters.

</details>

## 🚫 Question 29
What is the purpose of the `kafka.controller:type=KafkaController,name=LastCommittedRecordOffset` metric in KRaft mode?

- A. It indicates the offset of the last record appended to the metadata log
- B. It represents the offset of the last record replicated to all the controllers
- C. It measures the offset of the last record applied by the active controller
- D. It tracks the offset of the last record committed by the active controller

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In KRaft mode, the `kafka.controller:type=KafkaController,name=LastCommittedRecordOffset` metric serves the purpose of tracking the offset of the last record committed by the active controller.

In a KRaft cluster, the active controller is responsible for managing the metadata log and ensuring that the committed records are replicated to a quorum of controllers. When a record is committed, it means that a majority of the controllers have acknowledged and persisted the record, making it durable and irreversible.

The `LastCommittedRecordOffset` metric provides the offset of the most recent record that has been committed by the active controller. It represents the highest offset in the metadata log that has been successfully replicated and acknowledged by a quorum of controllers.

Monitoring the `LastCommittedRecordOffset` metric is crucial for understanding the progress and consistency of the metadata replication process. It helps in tracking how up-to-date the controllers are with respect to the committed records in the metadata log.

If the `LastCommittedRecordOffset` metric is advancing steadily and is close to the offset of the last appended record, it indicates that the active controller is efficiently committing records and the controllers are successfully replicating the metadata.

However, if the `LastCommittedRecordOffset` metric is lagging significantly behind the offset of the last appended record, it suggests that there might be issues with the metadata replication process. It could indicate network problems, controller failures, or performance bottlenecks that are preventing the controllers from committing and replicating records in a timely manner.

A is incorrect because the metric tracks the offset of the last committed record, not the last appended record to the metadata log.

B is incorrect because the metric specifically measures the offset of the last record committed by the active controller, not the offset of the last record replicated to all the controllers.

C is incorrect because the metric represents the offset of the last committed record, not the last record applied by the active controller. The application of records is a separate process from the commitment of records.

</details>

## 🚫 Question 30
What is the impact of setting `controller.quorum.fetch.timeout.ms` to a very low value in KRaft mode?

- A. It increases the time a controller waits without a successful fetch from the leader before it becomes a candidate
- B. It reduces the time a controller waits without a successful fetch from the leader before it becomes a candidate and starts an election
- C. It sets the maximum time allowed for a controller to fetch data from the brokers
- D. It determines the frequency at which the controllers fetch data from the active controller

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In KRaft mode, `controller.quorum.fetch.timeout.ms` is the "maximum time without a successful fetch from the current leader before becoming a candidate" (default 2000 ms). Setting it to a very low value makes followers start elections sooner.

The `controller.quorum.fetch.timeout.ms` configuration is the maximum time a follower goes without a successful fetch from the leader before it becomes a candidate and starts a new election. It defines the timeout duration for the controllers to receive data from the active controller during the metadata replication process.

A low value lets followers detect an unresponsive leader quickly and trigger a failover sooner, but a value that is too low can cause false positives and unnecessary elections during short pauses or network delays.

It's important to find a balance when configuring `controller.quorum.fetch.timeout.ms`. The value should be low enough to detect genuine issues with the active controller promptly, but not so low that it triggers false alarms and unnecessary failovers.

The default value for `controller.quorum.fetch.timeout.ms` is 2000 milliseconds (2 seconds), which provides a reasonable balance for most scenarios. Adjusting this value requires careful consideration of the specific requirements and characteristics of your KRaft cluster, such as network latency, controller load, and failover sensitivity.

A is incorrect because a lower value for `controller.quorum.fetch.timeout.ms` does not increase the time the controllers wait for a fetch response. It actually reduces the timeout duration.

C is incorrect because `controller.quorum.fetch.timeout.ms` does not set the maximum time allowed for a controller to fetch data from the brokers. It specifically relates to the timeout for receiving a fetch response from the active controller.

D is incorrect because `controller.quorum.fetch.timeout.ms` does not determine the frequency at which the controllers fetch data from the active controller. The fetch frequency is controlled by separate parameters.