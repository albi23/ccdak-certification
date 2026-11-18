> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Kafka Cluster Administration Configurations 🚫

Effective Kafka cluster management involves tuning various configurations to ensure optimal operation, fault tolerance, and efficient resource utilization. Key administrative settings help in maintaining balance across the cluster, managing topic lifecycle, and ensuring leadership distribution for resilience.

### Key Points for CCDAK on Cluster Administration

- **Cluster Balance and Efficiency**: Settings related to leader election and rebalance are crucial for evenly distributing the load across the cluster.
- **Fault Tolerance**: Proper configuration ensures the cluster remains operational even when certain nodes or partitions fail.
- **Topic Management**: Ability to dynamically manage topics, including deletion, is essential for operational flexibility.
- Kafka uses a binary protocol over TCP.

### APIs

There are five key APIs in Kafka:

- **Producer API:** Enables applications to send streams of data to topics within the Kafka cluster.
- **Consumer API:** Allows applications to read streams of data from topics within the Kafka cluster.
- **Streams API:** Facilitates the transformation of data streams from input topics to output topics.
- **Connect API:** Provides the capability to implement connectors that continuously pull data from source systems into Kafka or push data from Kafka to sink systems.
- **Admin API:** Offers tools for managing and inspecting topics, brokers, and other Kafka objects.

### 🚫 Important Cluster Administration Properties

#### `controller.socket.timeout.ms`
- **Description**: Timeout for controller-to-broker sockets. This setting impacts how long the controller waits for a response from a broker.
- **Default Value**: 30000 milliseconds (30 seconds).
- **Impact**: Affects the responsiveness and reliability of controller commands. Lower values may cause premature timeouts, while higher values can delay cluster reconfiguration in case of broker failures.

#### `leader.imbalance.check.interval.seconds`
- **Description**: Frequency at which the leader imbalance checker runs. This tool assesses if leaders are evenly distributed across the brokers.
- **Default Value**: 300 seconds (5 minutes).
- **Impact**: Adjusting this interval affects how quickly the cluster reacts to imbalances. More frequent checks can lead to a more balanced cluster but at the cost of increased control-plane traffic.

#### `leader.imbalance.per.broker.percentage`
- **Description**: The allowed percentage of leader imbalance on a broker before triggering a leader rebalance.
- **Default Value**: 10 (percent).
- **Impact**: Defines the threshold for triggering rebalances. Lower thresholds aim for stricter balance but might lead to more frequent leadership changes, potentially impacting performance.

#### `auto.leader.rebalance.enable`
- **Description**: Enables automatic leader rebalancing to evenly distribute leader partitions across brokers in the cluster.
- **Default Value**: true.
- **Impact**: When enabled, it helps in maintaining balance and can improve overall cluster performance and fault tolerance. However, frequent rebalancing can sometimes cause temporary performance dips.

#### `delete.topic.enable`
- **Description**: Allows topics to be deleted. When enabled, topics can be deleted, and their resources reclaimed.
- **Default Value**: true (since Kafka 1.0).
- **Impact**: Provides flexibility in managing topics but requires careful consideration to avoid accidental data loss. Ensuring this is enabled allows for better topic lifecycle management.

### Internal Kafka Topics

Only `__consumer_offsets` and `__transaction_state` are Apache Kafka internal topics (and `__cluster_metadata` in KRaft mode, an internal metadata log not visible as a normal topic). The `connect-*` topic names are user-configurable (`config.storage.topic`, `offset.storage.topic`, `status.storage.topic`; `connect-configs`/`-offsets`/`-status` are only conventional names). `_schemas` is the default Schema Registry topic (`kafkastore.topic`). All `_confluent*` / `__confluent*` topics below are Confluent Platform specific and out of exam scope.

Here are the important internal topics:

1. `__consumer_offsets`:
  - Stores the offsets of consumer groups.
  - Contains information about the last committed offset for each partition consumed by a consumer group.
  - Helps in tracking the progress of consumers and enables them to resume from the last committed offset in case of failures or restarts.

2. `__transaction_state`:
  - Stores the state of ongoing transactions in Kafka.
  - Used by the Kafka transactional producer to ensure atomic writes across multiple partitions and topics.
  - Enables transaction coordination and ensures data integrity in transactional messaging.

3. 🚫 `__confluent.support.metrics`:
  - A topic used by Confluent's Proactive Support (telemetry) feature to collect support metrics about the cluster (not by Control Center).

4. `_schemas`:
  - A topic used by the Confluent Schema Registry to store schema information.
  - Contains versioned schemas associated with Kafka topics.
  - Enables schema evolution and compatibility checks for Kafka producers and consumers.

5. `connect-configs`:
  - A topic used by Kafka Connect to store connector and task configurations.
  - Contains the configuration settings for Kafka Connect connectors and their associated tasks.
  - Allows dynamic configuration updates and management of Kafka Connect deployments.

6. `connect-offsets`:
  - A topic used by Kafka Connect to store the offsets of connector tasks.
  - Contains information about the last processed offset for each partition by a connector task.
  - Enables fault tolerance and resumption of connector tasks from the last processed offset.

7. `connect-status`:
  - A topic used by Kafka Connect to store status information about connector tasks.
  - Contains status updates and metadata related to the execution of connector tasks.
  - Allows monitoring and tracking the health and progress of Kafka Connect tasks.

8. 🚫 `_confluent-command`:
  - A topic used by Confluent Control Center to store and manage command requests.
  - Enables sending and receiving control commands between Control Center and other Confluent components.
  - Facilitates actions like starting/stopping connectors, modifying configurations, and triggering rebalances.

9. 🚫 `_confluent-monitoring`:
  - A topic used by Confluent Control Center for monitoring purposes.
  - Contains monitoring data and metrics related to the Confluent Platform components.
  - Helps in collecting and analyzing health and performance data for the Confluent ecosystem.

10. 🚫 `_confluent-secrets`:
   - A topic used by Confluent Control Center to store and manage secrets securely.
   - Enables secure storage and retrieval of sensitive configuration values, such as passwords and API keys.
   - Provides a centralized and encrypted storage for secrets used across the Confluent Platform.

11. (removed) `__consumer_timestamps` is not an Apache Kafka or Confluent internal topic. Consumer progress is tracked only via committed offsets in `__consumer_offsets`.

12. 🚫 `_confluent-metrics`:
   - A topic used by Confluent Control Center to store and manage metrics data.
   - Contains metrics related to the performance and health of Kafka clusters, topics, and clients.
   - Enables data visualization, alerting, and monitoring in Control Center.

13. 🚫 `_confluent-telemetry-metrics`:
   - A topic used by Confluent Control Center to store and manage telemetry data.
   - Contains usage and analytics data related to the Confluent Platform components.
   - Helps in understanding platform usage, adoption, and performance trends.

14. 🚫 `ksql-clusterksql_processing_log`:
   - A topic used by Confluent ksqlDB for storing processing logs.
   - Contains information about the processing of ksqlDB queries, including errors and status updates.
   - Helps in monitoring and troubleshooting ksqlDB processing pipelines.

15. 🚫 `_confluent-license`:
   - A topic used by Confluent Control Center to store and manage license information.
   - Contains data related to the Confluent Platform license, including expiration and feature entitlements.
   - Helps in tracking and enforcing license compliance across the platform.

### 🚫 Default Ports

- **Broker**: 9092
- **Schema Registry**: 8081
- **REST Proxy**: 8082
- **KSQL**: 8088
  
- **Zookeeper Client Port**: 2181
- **Zookeeper Leader Port** (followers connect to leader): 2888
- **Zookeeper Election Port**: 3888
- **KRaft Controller Listener**: 9093 (conventional, set via `controller.listener.names`/`listeners`; ZooKeeper was removed in Kafka 4.0)