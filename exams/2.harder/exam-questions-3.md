> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1 (Application Observability):
Which of the following application metrics are most useful for monitoring the performance and health of a Kafka producer in a Confluent environment? Select all that apply.

- A. JVM garbage collection pause time
- B. Producer bytes out per second
- C. Producer error rate (e.g., produce request failures)
- D. Consumer lag
- E. Number of active producer connections
- F. Producer request latency (average and percentile)

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

Kafka producers expose several metrics that are critical for observing their health and performance in a Confluent environment. Producer request latency (option 1) shows how quickly data is acknowledged by brokers, bytes out per second (option 2) reflects throughput, and producer error rate (option 4) indicates failures that may cause data loss. Metrics like consumer lag, connection counts, and generic JVM GC times (options 3, 5, 6) are either irrelevant to producer performance or too generic to be primary indicators. Monitoring these core metrics via Confluent Control Center or Prometheus enables developers to detect bottlenecks, optimize throughput, and ensure reliable message delivery. Refer to the Kafka Metrics Overview (https://kafka.apache.org/documentation/#metrics) and Confluent Monitoring guide (https://docs.confluent.io/platform/current/monitoring/monitoring.html).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Producer Metrics" (pp. 370-373)

**Detailed explanation of each option:**

1. ❌ **A. JVM garbage collection pause time**  
   **Incorrect**. This is a generic JVM metric that may affect overall application performance but is not specific to Kafka producer health or throughput.

2. ✅ **B. Producer bytes out per second**  
   **Correct**. It measures the throughput of data being sent by the producer. Low values may indicate back‑pressure or throttling, while high values confirm that the producer is saturated and sending data efficiently.

3. ✅ **C. Producer error rate (e.g., produce request failures)**  
   **Correct**. A rising error rate (e.g., serialization errors, broker errors, network failures) signals problems that can lead to data loss or application instability.

4. ❌ **D. Consumer lag**  
   **Incorrect**. Consumer lag applies to consumers, not producers. It measures how far behind a consumer is from the latest record, and is irrelevant for producer health.

5. ❌ **E. Number of active producer connections**  
   **Incorrect**. While the number of connections can be monitored for troubleshooting, it is not a primary performance metric for producers. It does not directly reflect throughput or latency.

6. ✅ **F. Producer request latency (average and percentile)**  
   **Correct**. This metric reflects how long a producer send request takes to reach the broker and return a response. It directly indicates network and broker responsiveness, and high latency often signals throttling or broker overload.

</details>

## Question 2 (Application Development):[-]
When developing a Kafka client that must connect to a secured Confluent Cloud cluster, which of the following configurations are required (or mandatory) to establish a secure connection?

- A. Add the JAAS config directly to the client using the system property `sasl.jaas.config`.
- B. Use `metadata.max.age.ms` to reduce latency in a secure cluster.
- C. Set `security.protocol=SSL` and provide the broker’s truststore via `ssl.truststore.location` and `ssl.truststore.password`.
- D. Set `client.id` to a unique value for monitoring purposes.
- E. Include `ssl.keystore.location` and `ssl.keystore.password` to provide a client certificate for mutual TLS.
- F. Configure `sasl.mechanism=PLAIN` and supply a JAAS configuration with username/password.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

A secured Kafka cluster requires TLS for encryption and certificate validation, which is achieved by setting `security.protocol=SSL` and supplying a truststore. If the cluster also demands SASL authentication, the client must specify a mechanism (e.g., PLAIN, SCRAM) and provide credentials, typically via a JAAS configuration passed through `sasl.jaas.config`. The keystore is only necessary for mutual TLS, which is not standard for Confluent Cloud. Other properties such as `client.id` and `metadata.max.age.ms` are unrelated to the security handshake. Mastering these configurations ensures that the client can authenticate, encrypt traffic, and safely communicate with the cluster.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ✅ **A. Add the JAAS config directly to the client using the system property `sasl.jaas.config`.**  
   **Correct**. This is a common way to embed JAAS credentials for SASL authentication without an external JAAS file.

2. ❌ **B. Use `metadata.max.age.ms` to reduce latency in a secure cluster.**  
   **Incorrect**. This property controls how often metadata is refreshed, it does not affect security or authentication.

3. ✅ **C. Set `security.protocol=SSL` and provide the broker’s truststore via `ssl.truststore.location` and `ssl.truststore.password`.**  
   **Correct**. TLS encryption requires the client to validate the broker’s certificate. The truststore contains the CA certificates that signed the broker’s cert.

4. ❌ **D. Set `client.id` to a unique value for monitoring purposes.**  
   **Incorrect**. While useful for tracking, `client.id` does not contribute to security or authentication.

5. ❌ **E. Include `ssl.keystore.location` and `ssl.keystore.password` to provide a client certificate for mutual TLS.**  
   **Incorrect**. for a typical secured cluster that only requires broker authentication. The keystore is only needed if the broker requires client certificates (mTLS).

6. ✅ **F. Configure `sasl.mechanism=PLAIN` and supply a JAAS configuration with username/password.**  
   **Correct**. If the cluster uses SASL authentication (often with SASL_SSL), a mechanism such as PLAIN (or SCRAM) and the JAAS credentials are mandatory for auth.

</details>

## Question 3 (Kafka Connect):
Which of the following statements accurately describe core concepts of Kafka Connect? Select all that apply.

- A. The sink connector automatically commits offsets to Kafka after processing records, relieving the user from manual offset handling.
- B. Connect uses a cluster of worker processes that host and run connector instances.
- C. Connectors are single-threaded components that cannot be parallelized across the cluster.
- D. Tasks are the unit of parallelism within a connector, each handling a portion of the data source or sink.
- E. Connect supports exactly‑once semantics by default for all sink connectors.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, D

**Explanation:**

Kafka Connect is a distributed framework that abstracts the mechanics of data movement into connectors and tasks. Connectors run in worker processes and can be scaled across a cluster, while tasks provide parallelism by processing data slices independently. Offset handling is built into the Connect framework: sink connector offsets are committed automatically as consumer-group offsets (in __consumer_offsets, group connect-<connector>), while source connector offsets go to the connect-offsets topic. By default, Connect offers at‑least‑once delivery, exactly‑once semantics require explicit configuration. Understanding these fundamentals is essential for designing scalable, reliable integration pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. The sink connector automatically commits offsets to Kafka after processing records, relieving the user from manual offset handling.**  
   **Correct**. True. Connect manages offset commits for sink connectors automatically (as a regular consumer group stored in __consumer_offsets), though advanced connectors can override this behavior via preCommit().

2. ✅ **B. Connect uses a cluster of worker processes that host and run connector instances.**  
   **Correct**. True. In a Connect cluster, each worker can host connectors and tasks, connectors are distributed across the cluster for high availability.

3. ❌ **C. Connectors are single-threaded components that cannot be parallelized across the cluster.**  
   **Incorrect**. False. While a single connector instance may run in one thread, it can spawn multiple tasks for parallel processing of data.

4. ✅ **D. Tasks are the unit of parallelism within a connector, each handling a portion of the data source or sink.**  
   **Correct**. True. The number of tasks is specified in the connector configuration, each task runs independently, enabling parallel data flow.

5. ❌ **E. Connect supports exactly‑once semantics by default for all sink connectors.**  
   **Incorrect**. False. The default guarantee is at‑least‑once, exactly‑once must be enabled through configuration (e.g., idempotent sinks or transactions).

</details>

## Question 4 (Programming & Serialization):
A Kafka producer writes records to a topic using Avro serialization with schema version 1. The schema is then evolved to version 2 by adding a new field named "age" with a default value of 0 and registered in Confluent Schema Registry. A consumer using the Avro deserializer reads the topic after the schema update. Which of the following best describes what the consumer will observe when it processes records originally produced with schema version 1?

- A. The consumer reads the record successfully and the new field "age" is omitted entirely from the returned record.
- B. The consumer throws a SerializationException because the schema of the record does not match the current registered schema.
- C. The consumer reads the record successfully, and the new field "age" is populated with the default value 0.
- D. The consumer reads the record successfully but all old fields are ignored and only the new field "age" is present.
- E. The consumer reads the record successfully but the new field "age" is null.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When a schema is evolved in Avro by adding a new field that includes a default value, Confluent’s Avro deserializer treats older records as valid. The deserializer fills the new field with its default during deserialization, ensuring backward compatibility. Consumers using the updated schema can continue to read older data without failure, which is essential for long‑running Kafka streams. This behavior distinguishes Avro from plain JSON, which requires manual handling of missing fields. Understanding this mechanism is critical for designing robust, schema‑evolving Kafka applications.

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. The consumer reads the record successfully and the new field "age" is omitted entirely from the returned record.**  
   **Incorrect**. The field is present in the schema, and Avro will populate it with its default. Omission would occur only if the consumer explicitly ignores unknown fields.

2. ❌ **B. The consumer throws a SerializationException because the schema of the record does not match the current registered schema.**  
   **Incorrect**. Avro’s backward compatibility rules allow the consumer to read older records when new fields have default values. The deserializer will not fail for version differences in this scenario.

3. ✅ **C. The consumer reads the record successfully, and the new field "age" is populated with the default value 0.**  
   **Correct**. Avro’s backward compatibility guarantees that consumers using the updated schema can deserialize older records and will receive default values for newly added fields.

4. ❌ **D. The consumer reads the record successfully but all old fields are ignored and only the new field "age" is present.**  
   **Incorrect**. Old fields remain available, only new fields with defaults are added to the record.

5. ❌ **E. The consumer reads the record successfully but the new field "age" is null.**  
   **Incorrect**. In Avro, if a new field has a default value, the deserializer supplies that default. Null is only used when no default is defined and the field is missing.

</details>

## Question 5 (Kafka Producers):
In the Kafka producer configuration, which setting directly limits the number of unacknowledged requests that can be in-flight to a broker, and why should it be set to 5 when idempotence is enabled?

- A. linger.ms=0
- B. enable.idempotence=true
- C. max.in.flight.requests.per.connection=5
- D. batch.size=16384

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka’s idempotent producer relies on limiting the number of unacknowledged requests so that acknowledgments arrive in order and duplicates are not produced. The `max.in.flight.requests.per.connection` setting is the only configuration that controls this concurrency. Setting it to 5 or lower ensures that, even with retries, the broker receives requests in the same order as they were sent, maintaining idempotence guarantees. Other properties such as `enable.idempotence` enable the feature, while `linger.ms` and `batch.size` affect batching behavior but not request limits. Understanding this distinction is crucial for developers tuning producers for reliability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "max.in.flight.requests.per.connection" / "Ordering Guarantees" (p. 60)

**Detailed explanation of each option:**

1. ❌ **A. linger.ms=0**  
   **Incorrect**. This controls how long the producer waits before sending a batch. While it affects throughput and latency, it does not limit the number of in‑flight requests.

2. ❌ **B. enable.idempotence=true**  
   **Incorrect**. This property turns on exactly‑once delivery semantics by preventing duplicate records, but it does not control the number of in‑flight requests. It is a prerequisite for safe idempotence, but not the configuration that limits request concurrency.

3. ✅ **C. max.in.flight.requests.per.connection=5**  
   **Correct**. This setting caps the number of outstanding requests a producer can send on a single connection. When idempotence is enabled, the producer must keep this value at or below 5 to preserve record ordering and avoid duplicate deliveries caused by out‑of‑order responses.

4. ❌ **D. batch.size=16384**  
   **Incorrect**. This defines the maximum size of a batch in bytes. It influences how many records are grouped together, but it does not directly limit the count of in‑flight requests.

</details>

## Question 6 (Application Observability):
In a Kafka Streams application, you want to verify that the stream processing is not falling behind the source topic. Which JMX metric would provide the most direct indication of the consumer group lag for the internal consumer used by the Streams application?

- A. kafka.consumer:type=consumer-fetch-manager-metrics,client-id=streams-application,broker=,name=records-lag-max
- B. kafka.consumer:type=consumer-fetch-manager-metrics,client-id=streams-application,broker=,name=records-consumed-total
- C. kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec
- D. kafka.streams:type=stream-task-metrics,task-id=0,name=records-emitted-total

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Monitoring consumer lag is critical in a Kafka Streams application to ensure timely processing. The JMX metric `records-lag-max` reports the maximum number of records a consumer group is behind the latest offset, making it the most direct way to detect back‑pressure or processing delays. Other metrics like `MessagesInPerSec` or `records-consumed-total` provide throughput or consumption counts but do not reveal lag. `records-emitted-total` is useful for output side monitoring but irrelevant to input lag. Refer to the Kafka JMX documentation and Confluent Streams monitoring guide for detailed usage. References: https://kafka.apache.org/documentation/#jmx https://docs.confluent.io/current/streams/developer-guide/monitoring.html

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Consumer Metrics" / "Lag Monitoring" (pp. 373-377)

**Detailed explanation of each option:**

1. ✅ **A. kafka.consumer:type=consumer-fetch-manager-metrics,client-id=streams-application,broker=,name=records-lag-max**  
   **Correct**. records-lag-max reports the maximum lag across all partitions for the consumer group. For a Kafka Streams internal consumer this metric is the most direct indicator of how many records the stream is behind the source topic.

2. ❌ **B. kafka.consumer:type=consumer-fetch-manager-metrics,client-id=streams-application,broker=,name=records-consumed-total**  
   **Incorrect**. records-consumed-total counts the total number of records consumed by the client, but it does not provide any information about the offsets still pending. It cannot indicate lag directly.

3. ❌ **C. kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec**  
   **Incorrect**. This metric reports the rate of messages entering the broker for a given topic. It reflects producer throughput, not how far the consumer group is behind the latest offset. Therefore, it is not useful for measuring consumer lag.

4. ❌ **D. kafka.streams:type=stream-task-metrics,task-id=0,name=records-emitted-total**  
   **Incorrect**. records-emitted-total counts the number of records produced by the stream task, not the consumer lag. It is useful for output monitoring but not for measuring how far behind the input is.

</details>

## Question 7 (Kafka Connect):
Which of the following statements correctly describe Kafka Connect core concepts related to task distribution, fault tolerance, configuration, and connector implementation?

- A. Kafka Connect distributes tasks across worker nodes in a cluster, with each task assigned to a single worker.
- B. The offset for each connector task is stored in the __consumer_offsets topic.
- C. If a worker node fails, its tasks are automatically reassigned to other workers after the group rebalance.
- D. Connect automatically scales by adding more Kafka brokers to the cluster.
- E. Connect connectors can be written in Java, Scala, or Python, with Python support provided via the PyKafka library.
- F. Connect's worker configuration property "plugin.path" determines the location of connector JAR files.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

Kafka Connect partitions work into connectors, tasks, and workers. A connector may spawn multiple tasks, each task runs on a single worker, enabling parallelism. Workers form a consumer group, so when a node fails its tasks are reassigned to surviving workers during rebalancing, ensuring fault tolerance. Task offsets are persisted in the dedicated __connect_offsets topic, not the generic __consumer_offsets. The plugin.path setting tells workers where to load connector JARs. Although Connect is built for Java/Scala, Python connectors are not supported via PyKafka and require separate implementation. Scaling Connect means adding workers, not Kafka brokers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. Kafka Connect distributes tasks across worker nodes in a cluster, with each task assigned to a single worker.**  
   **Correct**. A connector may be configured with multiple tasks, Connect assigns each task to a single worker in the worker group. This enables parallel processing of data streams.

2. ❌ **B. The offset for each connector task is stored in the __consumer_offsets topic.**  
   **Incorrect**. Connect stores offsets in the dedicated __connect_offsets topic, not in __consumer_offsets.

3. ✅ **C. If a worker node fails, its tasks are automatically reassigned to other workers after the group rebalance.**  
   **Correct**. Connect uses the Kafka consumer group protocol. When a worker leaves or fails, its partitions (tasks) are reassigned to remaining workers during the next rebalance.

4. ❌ **D. Connect automatically scales by adding more Kafka brokers to the cluster.**  
   **Incorrect**. Scaling Connect requires adding more worker nodes, adding brokers affects the Kafka cluster, not the Connect cluster.

5. ❌ **E. Connect connectors can be written in Java, Scala, or Python, with Python support provided via the PyKafka library.**  
   **Incorrect**. While connectors are typically written in Java or Scala, Python connectors require a separate worker implementation (e.g., via a custom Python worker) and are not natively supported by PyKafka.

6. ✅ **F. Connect's worker configuration property "plugin.path" determines the location of connector JAR files.**  
   **Correct**. The plugin.path property tells the worker where to look for connector classes and their dependencies.

</details>

## 🚫 Question 8 (Kafka Setup and Operations):
You are deploying a Confluent Platform cluster with Kafka broker and Kafka Connect workers using Docker Compose. The goal is to allow internal Docker containers to communicate with the broker on port 9092, while also exposing a client-facing REST endpoint on the host at port 9093. Which set of `KAFKA_LISTENERS` and `KAFKA_ADVERTISED_LISTENERS` configuration values will correctly achieve this, ensuring that the broker advertises the correct internal address for containers and the correct external address for clients, without causing misrouting or listener conflicts?

- A. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,INTERNAL://kafka:9092` and expose both ports 9092 and 9093.
- B. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092`, then expose port 9092 on the host.
- C. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092` and `KAFKA_LISTENERS=PLAINTEXT://kafka:9092` with no host port exposed.
- D. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092,EXTERNAL://localhost:9093` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,EXTERNAL://0.0.0.0:9093`, expose port 9093 on the host.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In a Docker Compose deployment, each Kafka listener must have a unique protocol name and corresponding advertised address. To expose the broker to both internal containers (PLAINTEXT) and external clients (EXTERNAL), you create two listeners: `PLAINTEXT://0.0.0.0:9092` for internal traffic and `EXTERNAL://0.0.0.0:9093` for external traffic. Advertised listeners are set to `PLAINTEXT://kafka:9092` (the Docker hostname) and `EXTERNAL://localhost:9093` (the host). The host must map port 9093 to expose the external listener. Option 3 correctly reflects this pattern, while the others either misadvertise addresses, omit necessary ports, or use invalid listener names, leading to connectivity or startup failures.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Docker listener/advertised-listener setup is a deployment/networking detail not covered by the book or the exam.

**Detailed explanation of each option:**

1. ❌ **A. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,INTERNAL://kafka:9092` and expose both ports 9092 and 9093.**  
   **Incorrect**. The listener type INTERNAL is not a valid Kafka listener name, Kafka only supports PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL, and custom listener names. This configuration will result in a startup error. Even if it succeeded, it advertises only the internal address.

2. ❌ **B. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092`, then expose port 9092 on the host.**  
   **Incorrect**. This configuration advertises only an internal address (kafka:9092). External clients cannot resolve 'kafka' and the host port is 9092, not the desired 9093. The broker will not listen for external traffic on a different port, so the requirement is not met.

3. ❌ **C. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092` and `KAFKA_LISTENERS=PLAINTEXT://kafka:9092` with no host port exposed.**  
   **Incorrect**. Advertised host is localhost, which is unreachable from other containers. Additionally, the broker only listens on the internal Docker network address 'kafka:9092', and no external port is mapped, so clients cannot reach the broker or Connect REST API.

4. ✅ **D. Set `KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092,EXTERNAL://localhost:9093` and `KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,EXTERNAL://0.0.0.0:9093`, expose port 9093 on the host.**  
   **Correct**. This defines two listeners: an internal PLAINTEXT listener on 9092 for Docker containers and an external listener on 9093 for clients. The advertised addresses match the listener types, and the host port 9093 is exposed, allowing external clients to connect. This setup satisfies all requirements.

</details>

## 🚫 Question 9 (Kafka Setup and Operations):
Which of the following is NOT a supported Custom Resource Definition (CRD) by the Confluent Operator when deploying Confluent Platform on Kubernetes?

- A. Kafka
- B. Connect
- C. RestProxy
- D. Zookeeper
- E. SchemaRegistry

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

CORRECTION: Confluent for Kubernetes (the successor of Confluent Operator) DOES provide a standalone `Zookeeper` CRD (kind: Zookeeper, alongside Kafka, Connect, SchemaRegistry, KsqlDB, ControlCenter, KafkaRestProxy, ...), so D is a supported CRD. The only option that is not a real CRD kind is `RestProxy` - the actual kind is `KafkaRestProxy`. Original text follows (its claim about Zookeeper is wrong).

Confluent Operator simplifies Kubernetes deployments by exposing platform components as Custom Resources. The supported CRDs include Kafka, Connect, SchemaRegistry, and RestProxy, each providing declarative lifecycle management. Zookeeper, however, is not a separate CRD, it is bundled with the Kafka CRD when ZooKeeper mode is used. Developers often mistakenly try to create a Zookeeper resource, expecting independent management. Recognizing this distinction is essential for correctly provisioning a Confluent cluster and avoiding unnecessary custom resources that the operator does not support.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Confluent Operator CRDs (CFK) are not in the book, verified against Confluent for Kubernetes docs.

**Detailed explanation of each option:**

1. ❌ **A. Kafka**  
   **Incorrect**. The Confluent Operator includes a `Kafka` CRD that allows declarative configuration and management of Kafka clusters.

2. ❌ **B. Connect**  
   **Incorrect**. A `Connect` (or `KafkaConnect`) CRD is supported, enabling deployment of distributed Kafka Connect workers with operator‑driven scaling.

3. ✅ **C. RestProxy**  
   **Correct**. There is no CRD kind named `RestProxy`, the REST Proxy CRD is called `KafkaRestProxy`. This is the only listed name that is not a supported CRD.

4. ❌ **D. Zookeeper**  
   **Incorrect**. Confluent for Kubernetes/Operator exposes ZooKeeper as its own `Zookeeper` CRD, so it is a supported resource.

5. ❌ **E. SchemaRegistry**  
   **Incorrect**. The operator provides a `SchemaRegistry` CRD for deploying and managing Confluent Schema Registry instances.

</details>

## Question 10 (Kafka Connect):
Which of the following statements about the `key.converter` configuration property in Kafka Connect is **false**?

- A. If not specified, the default value is `org.apache.kafka.connect.storage.StringConverter`.
- B. It specifies the converter class used to serialize the record key for all data sent to Kafka topics.
- C. It can be set to `org.apache.kafka.connect.storage.StringConverter` when the key is a plain UTF‑8 string.
- D. It must be the same converter for all connectors in a Kafka Connect cluster, otherwise the cluster will reject the connector configuration.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The `key.converter` property determines how Kafka Connect serializes the key part of records before sending them to Kafka. It can be any converter class, such as `StringConverter` for plain strings or `JsonConverter` for JSON payloads. Connectors can set their own converters, the cluster does not enforce a single converter across all connectors, so option 3 is the false statement. Misconceptions often arise from conflating the need for a common converter with the cluster’s ability to mix converters. Understanding this property is essential for proper schema handling and data format compatibility in production deployments. Refer to the official Kafka Connect configuration documentation for details.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Verified against Kafka Connect docs: key.converter is per-connector/worker, the Connect worker default is JsonConverter, not StringConverter (option A's premise is itself inaccurate, but D is the stated false statement).

**Detailed explanation of each option:**

1. ❌ **A. If not specified, the default value is `org.apache.kafka.connect.storage.StringConverter`.**  
   **Incorrect**. The default converter for keys is the StringConverter.

2. ❌ **B. It specifies the converter class used to serialize the record key for all data sent to Kafka topics.**  
   **Incorrect**. The `key.converter` property defines which serializer/deserializer is applied to the key of every Kafka record produced by the connector.

3. ❌ **C. It can be set to `org.apache.kafka.connect.storage.StringConverter` when the key is a plain UTF‑8 string.**  
   **Incorrect**. `StringConverter` is a valid built‑in converter suitable for simple string keys.

4. ✅ **D. It must be the same converter for all connectors in a Kafka Connect cluster, otherwise the cluster will reject the connector configuration.**  
   **Correct**. Each connector can independently specify its own `key.converter`, the cluster does not enforce a uniform converter across connectors.

</details>

## 🚫 Question 11 (Kafka Connect):
You are deploying Kafka Connect in distributed mode on a Confluent Platform cluster that has 3 broker nodes. In order to guarantee high availability for connector configurations, offsets, and status, which set of configuration values for the internal topics is correct?

- A. config.storage.replication.factor=3, offset.storage.replication.factor=3, status.storage.replication.factor=1
- B. config.storage.replication.factor=3, offset.storage.replication.factor=1, status.storage.replication.factor=3
- C. config.storage.replication.factor=3, offset.storage.replication.factor=3, status.storage.replication.factor=3
- D. config.storage.replication.factor=1, offset.storage.replication.factor=3, status.storage.replication.factor=1
- E. config.storage.replication.factor=1, offset.storage.replication.factor=1, status.storage.replication.factor=1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Connect uses three internal Kafka topics—config, offset, and status—to store connector metadata, progress, and health data. In a distributed deployment, these topics must be replicated across the Kafka cluster to survive broker failures. The replication factor (e.g., 3 for a three‑node cluster) dictates how many broker replicas each topic partition has. Setting all three topics to the same replication factor equal to the broker count is the recommended high‑availability configuration. Lower replication factors compromise data durability and can cause connectors to lose configuration or offset information after a broker crash, leading to duplicate processing or data loss.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Internal-topic replication factors verified against Kafka Connect distributed-mode docs.

**Detailed explanation of each option:**

1. ❌ **A. config.storage.replication.factor=3, offset.storage.replication.factor=3, status.storage.replication.factor=1**  
   **Incorrect**. While config and offset topics are protected, the status topic would still be at 1, meaning connector status information could be lost. All topics should be replicated for full HA.

2. ❌ **B. config.storage.replication.factor=3, offset.storage.replication.factor=1, status.storage.replication.factor=3**  
   **Incorrect**. The offset topic controls which messages have been processed, a replication factor of 1 makes it vulnerable to broker failure, breaking fault tolerance.

3. ✅ **C. config.storage.replication.factor=3, offset.storage.replication.factor=3, status.storage.replication.factor=3**  
   **Correct**. In a 3‑node cluster, setting all three internal topics (config, offset, status) to a replication factor of 3 ensures that the data survives the loss of any single broker. The Confluent documentation recommends matching the replication factor to the cluster size for HA: https://docs.confluent.io/platform/current/connect/references/configuration.html#internal-tuning.

4. ❌ **D. config.storage.replication.factor=1, offset.storage.replication.factor=3, status.storage.replication.factor=1**  
   **Incorrect**. While the offset topic is critical for HA, the config and status topics are left at 1, meaning connector metadata would be lost if a broker dies. For full HA, all three topics should have the same replication factor.

5. ❌ **E. config.storage.replication.factor=1, offset.storage.replication.factor=1, status.storage.replication.factor=1**  
   **Incorrect**. This is the default configuration for a non‑HA setup. All three internal topics would have a replication factor of 1, exposing the cluster to data loss if any broker fails.

</details>

## Question 12 (Kafka Ecosystem):
You need to increase the number of partitions of an existing topic named "orders" from 3 to 5 using the Kafka Admin API from a Java client. Which AdminClient method should you invoke to achieve this?

- A. AdminClient.deleteTopics(...) – delete and recreate the topic with new partitions.
- B. AdminClient.describeTopics(...) – retrieve current topic metadata, it cannot change partitions.
- C. AdminClient.createTopics(...) – create a new topic with the same name and new partitions.
- D. AdminClient.alterConfigs(...) – modify the topic configuration including partitions.
- E. AdminClient.createPartitions(...) – add partitions to an existing topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

The Kafka AdminClient exposes a set of asynchronous APIs for cluster management. To increase partitions for an existing topic you must call createPartitions, which updates the topic metadata with the new total partition count. createTopics cannot be used because it will fail on an existing topic, and alterConfigs cannot modify partitions. describeTopics only reads metadata, while deleteTopics removes the topic entirely. The createPartitions API is idempotent for the new partition count and is the recommended path for scaling a topic. For more details see the Apache Kafka AdminClient documentation (https://kafka.apache.org/documentation/#adminclient).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Adding Partitions to a Topic" (pp. 127-128)

**Detailed explanation of each option:**

1. ❌ **A. AdminClient.deleteTopics(...) – delete and recreate the topic with new partitions.**  
   **Incorrect**. deleteTopics removes the topic entirely. While you could recreate it with a different partition count, this approach is unnecessary and riskier compared to createPartitions.

2. ❌ **B. AdminClient.describeTopics(...) – retrieve current topic metadata, it cannot change partitions.**  
   **Incorrect**. describeTopics is a read‑only operation that returns TopicDescription objects. It is useful for inspecting the current state but does not perform any modifications.

3. ❌ **C. AdminClient.createTopics(...) – create a new topic with the same name and new partitions.**  
   **Incorrect**. This method is used to create a brand‑new topic. If the topic already exists, the call will fail with a TopicExistsException. It cannot modify the partition count of an existing topic.

4. ❌ **D. AdminClient.alterConfigs(...) – modify the topic configuration including partitions.**  
   **Incorrect**. alterConfigs changes configuration values (e.g., cleanup.policy) but does not support changing the number of partitions. Partition count is immutable via configs.

5. ✅ **E. AdminClient.createPartitions(...) – add partitions to an existing topic.**  
   **Correct**. This is the correct method for increasing partitions. It accepts a map of topic names to NewPartitions objects, allowing you to specify the desired total partition count. Partitions can only be increased, not decreased.

</details>

## 🚫 Question 13 (Stream Processing):
When modeling event data for a Kafka stream processing pipeline that uses ksqlDB to perform aggregates and maintain event‑time semantics, which of the following design choices are considered best practices?

- A. Encode timestamps as epoch milliseconds and include them as a separate header rather than payload.
- B. Store events as Avro with a schema registry and include an event_type discriminator field.
- C. Avoid including a record key unless you need partitioning or stateful joins.
- D. Use a flat JSON structure with only fields needed for downstream processing.
- E. Include a monotonically increasing surrogate key in every event.
- F. Use a compound key of user_id and event_timestamp for all events to guarantee ordering within a partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

In stream processing with ksqlDB, event data should be schema‑based, typically Avro with the Confluent Schema Registry, to support evolution and type safety. A discriminator field such as event_type allows the system to handle multiple event shapes in a single topic. The Kafka record key is only required for partitioning, ordering, or stateful joins, otherwise it can be omitted. Payload timestamps are essential for event‑time windows, so they must be in the record body, not headers. Avoiding unnecessary keys and using a simple, consistent schema reduces complexity and maximizes throughput.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 14 "Stream Processing Concepts" (pp. 385-392) — NOTE: ksqlDB specifics verified against ksqlDB docs (out of exam scope).

**Detailed explanation of each option:**

1. ❌ **A. Encode timestamps as epoch milliseconds and include them as a separate header rather than payload.**  
   **Incorrect**. Kafka message headers are not reliably exposed to ksqlDB, and event‑time processing requires the timestamp to be part of the payload so that aggregations and windows can use it.

2. ✅ **B. Store events as Avro with a schema registry and include an event_type discriminator field.**  
   **Correct**. Avro with Schema Registry provides compact, versioned schemas and enables schema evolution. An event_type field supports unions and lets ksqlDB route events to appropriate tables or processors.

3. ✅ **C. Avoid including a record key unless you need partitioning or stateful joins.**  
   **Correct**. The record key should be used only for logical ordering, partitioning, or for stateful operations. Leaving it null avoids unnecessary shuffling.

4. ❌ **D. Use a flat JSON structure with only fields needed for downstream processing.**  
   **Incorrect**. Minimizing payload size is useful, but using plain JSON without a schema registry makes schema evolution fragile and provides no type safety. For stream processing, a schema‑based format such as Avro, Protobuf, or JSON Schema with Confluent Schema Registry is preferred.

5. ❌ **E. Include a monotonically increasing surrogate key in every event.**  
   **Incorrect**. A surrogate key is unnecessary for stream processing, the Kafka record key is used for partitioning and stateful joins, not for identifying records. Adding it only adds overhead and can create confusion.

6. ❌ **F. Use a compound key of user_id and event_timestamp for all events to guarantee ordering within a partition.**  
   **Incorrect**. A compound key inflates the number of partitions and reduces parallelism. Ordering within a partition is guaranteed by the Kafka record order, the key is not needed for that.

</details>

## Question 14 (Stream Processing):
In a distributed Kafka Streams application, a stateful operator (e.g., a windowed aggregation or a KJoin) must maintain its state across failures. Which mechanism does Kafka Streams employ to guarantee that the operator can rebuild its state after a task is restarted on a different node?

- A. Every state change is appended to a dedicated changelog topic that is fully replicated across the Kafka cluster. When a task restarts, it reads the changelog to rebuild the state store.
- B. State is periodically checkpointed to HDFS and restored when a task fails.
- C. Zookeeper maintains a copy of each state store and synchronizes it with the application during failures.
- D. The operator’s state is stored only in a local RocksDB instance and is never replicated. When a task fails, its state is lost and the application must restart from the beginning of the input topic.
- E. The operator’s state is kept only in memory and is regenerated by replaying the original input topic when needed.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams achieves fault tolerance for stateful operators by persisting each state store’s changes to a dedicated changelog topic that is replicated across the Kafka cluster. When a task dies, the re‑assigned task reads the changelog to rebuild its state, ensuring exactly‑once semantics. This design removes the need for external systems such as Zookeeper or HDFS, keeps recovery fast, and guarantees that state is durable even if the node fails. Misconceptions often arise from conflating in‑memory state with durable storage, only the changelog topic provides the required durability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "State" / "Surviving Failures" (pp. 388-389, 415-416)

**Detailed explanation of each option:**

1. ✅ **A. Every state change is appended to a dedicated changelog topic that is fully replicated across the Kafka cluster. When a task restarts, it reads the changelog to rebuild the state store.**  
   **Correct**. This is the core fault‑tolerance strategy in Kafka Streams. Each state store has an associated changelog topic, and the data is replicated with the broker’s replication factor. Upon failure, the new task reads the changelog to reconstruct the state.

2. ❌ **B. State is periodically checkpointed to HDFS and restored when a task fails.**  
   **Incorrect**. Kafka Streams does not use external distributed file systems like HDFS for state durability, it relies on changelog topics for replication.

3. ❌ **C. Zookeeper maintains a copy of each state store and synchronizes it with the application during failures.**  
   **Incorrect**. Zookeeper is used for cluster metadata and coordination but not for storing state of stream processing tasks.

4. ❌ **D. The operator’s state is stored only in a local RocksDB instance and is never replicated. When a task fails, its state is lost and the application must restart from the beginning of the input topic.**  
   **Incorrect**. Kafka Streams requires state durability, keeping state only in local memory or a non-replicated store would cause permanent loss of processed data.

5. ❌ **E. The operator’s state is kept only in memory and is regenerated by replaying the original input topic when needed.**  
   **Incorrect**. Relying solely on replaying the input topic would be impractical for large or long‑running streams and would not guarantee fast recovery or state consistency.

</details>

## 🚫 Question 15 (Kafka Fundamentals):
Which of the following options are valid mechanisms to secure both client‑to‑broker communication and inter‑broker communication in a Confluent Platform deployment? Select all that apply.

- A. Set the property `inter.broker.listener.name` to "EXTERNAL" to secure inter‑broker traffic.
- B. Apply ACLs on topics and consumer groups to limit access.
- C. Use plaintext (PLAINTEXT) listeners with password authentication.
- D. Enable broker IP allowlists by specifying `listeners` to accept connections only from specified IP ranges.
- E. Set up Kerberos (SASL/KRB5) authentication for clients and brokers.
- F. Configure SASL/PLAIN authentication with TLS encryption for both client‑to‑broker and inter‑broker traffic.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, F

**Explanation:**

Securing a Kafka cluster involves both authentication and authorization. Authentication is typically achieved via SASL mechanisms (PLAIN, GSSAPI/Kerberos) that can be combined with TLS for encryption. Once a principal is authenticated, Access Control Lists (ACLs) restrict which operations that principal can perform on topics, consumer groups, and cluster resources. Plaintext listeners provide no protection and should never be used for production traffic. The `inter.broker.listener.name` property must reference the internal listener, pointing it to an external listener compromises security. IP allowlisting is not a built‑in Kafka feature, it must be enforced at the network or OS level. These distinctions are critical for Confluent Certified Developers to correctly configure secure clusters.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 11 "Authorization" / "AclAuthorizer" (pp. 291-295)

**Detailed explanation of each option:**

1. ❌ **A. Set the property `inter.broker.listener.name` to "EXTERNAL" to secure inter‑broker traffic.**  
   **Incorrect**. Inter‑broker traffic must use the internal listener, setting it to EXTERNAL would expose brokers to the public network and removes the internal security controls.

2. ✅ **B. Apply ACLs on topics and consumer groups to limit access.**  
   **Correct**. ACLs control which principals can perform operations, providing authorization once authentication succeeds.

3. ❌ **C. Use plaintext (PLAINTEXT) listeners with password authentication.**  
   **Incorrect**. PLAINTEXT listeners transmit data without encryption and do not support password authentication, only SASL mechanisms provide authentication.

4. ❌ **D. Enable broker IP allowlists by specifying `listeners` to accept connections only from specified IP ranges.**  
   **Incorrect**. Kafka does not natively support IP allowlisting in the `listeners` configuration, network filtering must be performed outside Kafka.

5. ✅ **E. Set up Kerberos (SASL/KRB5) authentication for clients and brokers.**  
   **Correct**. Kerberos is a widely used SASL mechanism that authenticates principals and can be enabled for both client and broker traffic.

6. ✅ **F. Configure SASL/PLAIN authentication with TLS encryption for both client‑to‑broker and inter‑broker traffic.**  
   **Correct**. SASL/PLAIN is a supported authentication mechanism and when combined with TLS it provides both encryption and authentication for all traffic.

</details>

## Question 16 (Kafka Core Concepts):
Which statement most accurately describes how Apache Kafka preserves message ordering for consumers?

- A. Kafka uses a global queue that all producers and consumers share to enforce ordering.
- B. Kafka guarantees global ordering of messages across all partitions by maintaining a single, ordered log.
- C. Kafka orders messages based on the producer’s timestamp field in the record header.
- D. Kafka maintains ordering within a partition based on the sequential offset assigned at write time, writes to the same partition are serialized.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s ordering guarantees are limited to a single partition. When a producer sends records to a partition, the broker assigns sequential offsets in the order records are written. Because writes to a partition are serialized, a consumer that reads records sequentially will see them in the same order they were produced. Global ordering across multiple partitions is not provided, partitions operate independently. The producer timestamp and other metadata do not influence the ordering mechanism. Understanding this behavior is essential for designing applications that rely on message ordering, such as stateful stream processing or transactional updates.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6), ordering per partition

**Detailed explanation of each option:**

1. ❌ **A. Kafka uses a global queue that all producers and consumers share to enforce ordering.**  
   **Incorrect**. Kafka does not use a global queue, each partition is an independent log, and ordering guarantees are only per partition.

2. ❌ **B. Kafka guarantees global ordering of messages across all partitions by maintaining a single, ordered log.**  
   **Incorrect**. Kafka does not provide global ordering. Ordering is only guaranteed within a single partition, different partitions are independent.

3. ❌ **C. Kafka orders messages based on the producer’s timestamp field in the record header.**  
   **Incorrect**. The producer timestamp is informational and not used to determine the order in which messages are written to a partition.

4. ✅ **D. Kafka maintains ordering within a partition based on the sequential offset assigned at write time, writes to the same partition are serialized.**  
   **Correct**. Offsets are assigned in the order messages are appended to a partition, and the broker ensures that writes to a partition are serialized, preserving ordering for consumers that read sequentially.

</details>

## Question 17 (Kafka Producers):
When configuring compression for a Kafka producer, which of the following statements best describes how the compression mechanism works and its impact on throughput and latency?

- A. Using a high‑level compression codec like LZ4 can reduce latency compared to GZIP, but it can increase CPU usage.
- B. The producer compresses an entire batch of records into a single block, reducing the size of the batch but adding a small compression overhead, latency depends on batch size and compression algorithm.
- C. Compression settings affect only the log segment size on the broker side and have no impact on network traffic.
- D. The compression type is negotiated with the broker and can change mid‑stream.
- E. Compression is applied to each individual record before it is sent, guaranteeing lower latency but higher CPU usage.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka producers compress data at the batch level using the codec specified by the `compression.type` configuration. The entire batch is serialized into a single compressed block before transmission, which reduces payload size and improves throughput. The trade‑off is a small CPU overhead and the latency impact depends on batch size and chosen codec, faster codecs (e.g., LZ4) yield lower CPU usage and latency but lower compression ratio, while slower codecs (GZIP, Snappy) offer higher compression at the cost of more CPU and slightly higher latency. Understanding this balance is critical for optimizing performance in real‑time streaming applications. For more details, see the official Kafka documentation on Producer Configs and Compression.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "compression.type" (p. 59)

**Detailed explanation of each option:**

1. ❌ **A. Using a high‑level compression codec like LZ4 can reduce latency compared to GZIP, but it can increase CPU usage.**  
   **Incorrect**. Partially true but misleading. LZ4 is faster than GZIP, resulting in lower CPU usage and often lower latency, but it provides a weaker compression ratio. It is not the best answer to the question.

2. ✅ **B. The producer compresses an entire batch of records into a single block, reducing the size of the batch but adding a small compression overhead, latency depends on batch size and compression algorithm.**  
   **Correct**. This is the correct description. The Producer aggregates records into a batch, compresses the whole batch, and then transmits it. The choice of codec and batch size influences throughput and latency.

3. ❌ **C. Compression settings affect only the log segment size on the broker side and have no impact on network traffic.**  
   **Incorrect**. Compression reduces the bytes sent over the wire, directly affecting network traffic and consumer read times.

4. ❌ **D. The compression type is negotiated with the broker and can change mid‑stream.**  
   **Incorrect**. The compression type is configured on the producer and is fixed for the lifetime of the connection, the broker does not negotiate or change it mid‑stream.

5. ❌ **E. Compression is applied to each individual record before it is sent, guaranteeing lower latency but higher CPU usage.**  
   **Incorrect**. Kafka compresses data at the **batch** level, not per record. Compressing each record individually would add overhead and actually increase latency.

</details>

## Question 18 (Kafka Connect):
Which of the following statements correctly describe core features and capabilities of Kafka Connect’s runtime that help manage connector deployment, scaling, and data transformations?

- A. Kafka Connect exposes a REST API but only for starting and stopping connectors, not for configuration.
- B. Kafka Connect distributes connector tasks across workers for load balancing and fault tolerance.
- C. Kafka Connect supports Single Message Transforms (SMTs) for on-the-fly data transformation.
- D. Kafka Connect automatically registers schemas in the Schema Registry for all connectors.
- E. Kafka Connect automatically rolls back connector configuration changes if the connector fails to start.
- F. Kafka Connect can automatically create destination topics when running sink connectors if the auto.create.topics.enabled property is set.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

CORRECTION: only B and C are true (this is a "select 2" question). F is false: Connect's automatic topic creation (KIP-158, `topic.creation.enable` plus `topic.creation.*` settings) applies to SOURCE connectors that write new topics, sink connectors only read existing topics, and `auto.create.topics.enabled` is not a Connect property (it is not the broker's `auto.create.topics.enable` either). Original text follows (its mention of sink topic creation is wrong).

Kafka Connect is designed as a scalable, fault‑tolerant framework for integrating Kafka with external systems. Key runtime features include automatic topic creation for sinks (when enabled), dynamic task distribution across workers for load balancing and high availability, and a comprehensive REST API that manages connector life‑cycle and configuration. Additionally, Connect supports Single Message Transforms (SMTs) that allow lightweight, per‑message processing without external code. Misconceptions often arise around automatic schema registration and configuration rollback, these are optional or manual actions, not built‑in Connect capabilities. Understanding these distinctions is critical for configuring robust, production‑grade pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect exposes a REST API but only for starting and stopping connectors, not for configuration.**  
   **Incorrect**. The REST API supports full lifecycle operations: creating, updating, deleting, and querying connector configurations, status, and task information.

2. ✅ **B. Kafka Connect distributes connector tasks across workers for load balancing and fault tolerance.**  
   **Correct**. Each connector is split into tasks that can run on any worker in the cluster. The Connect worker group automatically balances tasks and reassigns them if a worker fails, providing scalability and high availability.

3. ✅ **C. Kafka Connect supports Single Message Transforms (SMTs) for on-the-fly data transformation.**  
   **Correct**. SMTs are lightweight, reusable components applied to each message during source ingestion or sink output, enabling field renaming, masking, or filtering without external code.

4. ❌ **D. Kafka Connect automatically registers schemas in the Schema Registry for all connectors.**  
   **Incorrect**. Schema registration is optional and performed by the connector implementation, not automatically by Connect itself. Connect can use the Schema Registry when configured, but it does not enforce automatic schema registration for every connector.

5. ❌ **E. Kafka Connect automatically rolls back connector configuration changes if the connector fails to start.**  
   **Incorrect**. If a connector fails to start, it enters the FAILED state, Connect does not automatically revert the configuration change. The user must manually adjust or delete the connector.

6. ❌ **F. Kafka Connect can automatically create destination topics when running sink connectors if the auto.create.topics.enabled property is set.**  
   **Incorrect**. Connect can create topics only for source connectors (via `topic.creation.enable` and `topic.creation.*`, KIP-158). Sink connectors consume from existing topics, and `auto.create.topics.enabled` is not a Connect setting.

</details>

## Question 19 (Programming & Serialization):
Which of the following statements about message keying in Apache Kafka are true, particularly in the context of partitioning, ordering, and use of the Confluent Schema Registry?

- A. If a key is not present, the consumer can still guarantee ordering of all messages within a topic.
- B. Keyless records are still routed to partitions based on the value's hash if a default partitioner is used.
- C. Records with null keys are placed in a random partition.
- D. The key serializer must be registered with the Schema Registry if Avro is used for the key.
- E. The message key must be serializable using the same serializer as the value.
- F. Using a key allows the consumer to retrieve only records from a specific partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

In Kafka, message keys influence partitioning, ordering, and serialization. A null key causes the default round‑robin partitioner to scatter records across partitions, which is why option 2 is true. Keys and values may use different serializers, the requirement to register the key schema only applies when the key itself is an Avro (or other schema‑aware) type, making option 6 correct. Options 1, 3, 4, and 5 describe misconceptions: keys need not match the value serializer, the default partitioner does not hash the value for keyless records, consumers cannot target a partition by key, and ordering guarantees exist only per partition, not globally without keys. Understanding these nuances is essential for designing robust Kafka data pipelines with Confluent Schema Registry.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Partitions" (pp. 68-70) — NOTE: Avro key registration verified against Schema Registry docs.

**Detailed explanation of each option:**

1. ❌ **A. If a key is not present, the consumer can still guarantee ordering of all messages within a topic.**  
   **Incorrect**. Ordering is only guaranteed within a single partition. Without a key, multiple partitions break global ordering.

2. ❌ **B. Keyless records are still routed to partitions based on the value's hash if a default partitioner is used.**  
   **Incorrect**. With a null key the default partitioner does **not** hash the value, it simply selects partitions round‑robin.

3. ✅ **C. Records with null keys are placed in a random partition.**  
   **Correct**. When the key is null, Kafka’s default partitioner uses a round‑robin strategy across the topic’s partitions.

4. ✅ **D. The key serializer must be registered with the Schema Registry if Avro is used for the key.**  
   **Correct**. When Avro is used for the key, the serializer must be configured with the Schema Registry to retrieve and register the key schema.

5. ❌ **E. The message key must be serializable using the same serializer as the value.**  
   **Incorrect**. The key and value can use entirely different serializers, for example, a String key with an Avro value is common.

6. ❌ **F. Using a key allows the consumer to retrieve only records from a specific partition.**  
   **Incorrect**. Consumers read from partitions, not by key. A key can be used for filtering after retrieval but does not change the consumer API.

</details>

## Question 20 (Stream Processing):
Which of the following statements about Kafka Streams components and APIs are true? Select all that apply.

- A. The `transform` method allows a KStream to be processed using the Processor API while retaining the original key/value semantics.
- B. The `through` method writes records to an intermediate topic but discards the original key/value pairs.
- C. A KTable is a changelog‑backed materialized view that can be queried via the Interactive Queries API.
- D. Global tables are replicated to all instances but cannot be queried by the Interactive Queries API.
- E. Global tables are replicated to all instances and can be read from any instance but are not mutable by user code.
- F. All state stores in Kafka Streams are automatically backed by changelog topics, and users do not need to configure them.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, E

**Explanation:**

Kafka Streams distinguishes between KStreams (unbounded event streams) and KTables (stateful changelog‑backed tables). KTables expose state stores that are persisted via changelog topics and can be queried interactively, which makes option 1 true. The DSL ‘through’ operator preserves the original record while writing to an intermediate topic, invalidating option 2. Global tables are fully replicated and queryable, contradicting option 3, but option 6 correctly states that they are read‑only and replicated. The ‘transform’ operator bridges the DSL with the Processor API, allowing stateful processing without altering key/value semantics, validating option 4. Finally, not all stores are changelog‑backed, transient stores lack changelogs, so option 5 is false. This knowledge is essential for designing fault‑tolerant, stateful stream applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ✅ **A. The `transform` method allows a KStream to be processed using the Processor API while retaining the original key/value semantics.**  
   **Correct**. `transform` is a DSL operator that delegates to a user‑supplied Transformer which can use state stores and emit zero, one or more output records while preserving the stream’s semantics.

2. ❌ **B. The `through` method writes records to an intermediate topic but discards the original key/value pairs.**  
   **Incorrect**. The `through` method simply forwards each record to a topic and then re‑reads it, preserving the original key/value pairs. It does not discard data.

3. ✅ **C. A KTable is a changelog‑backed materialized view that can be queried via the Interactive Queries API.**  
   **Correct**. KTables store their state in a persistent changelog topic and expose a state store that can be queried at runtime via the Interactive Queries API. This is documented in the Kafka Streams Developer Guide.

4. ❌ **D. Global tables are replicated to all instances but cannot be queried by the Interactive Queries API.**  
   **Incorrect**. Global tables are fully replicated to every instance and their state stores are accessible via the Interactive Queries API, just like local KTables.

5. ✅ **E. Global tables are replicated to all instances and can be read from any instance but are not mutable by user code.**  
   **Correct**. Global tables are read‑only views that are replicated to each instance, and applications cannot mutate them directly, updates come only from the source topic.

6. ❌ **F. All state stores in Kafka Streams are automatically backed by changelog topics, and users do not need to configure them.**  
   **Incorrect**. Only persistent state stores are backed by changelog topics, transient (in‑memory) stores are not. Users must declare the store type in the topology.

</details>

## Question 21 (Kafka Consumers):
In a single Kafka consumer group, how many consumer instances can simultaneously consume records from the same partition, and why?

- A. Up to the number of replicas can read concurrently because replicas can serve reads.
- B. Multiple consumers can read concurrently if they use the same group id but are in separate consumer processes.
- C. Any number of consumers can read concurrently if they use different consumer group ids.
- D. Only one consumer can read from a partition at a time because the partition’s log is ordered and its offset is exclusive to a consumer within a group.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka’s parallelism model is built around partitions. A partition is an immutable, ordered sequence of records, and within a consumer group each partition can be assigned to only one consumer instance. This guarantees a single consumer updates the offset for that partition, preserving order and enabling fault tolerance. Multiple consumers in the same group cannot share a partition, they are balanced across the group’s partitions. However, consumers in different groups can all read the same partition independently. Understanding this partition‑to‑consumer mapping is essential for designing scalable consumer applications and for correctly interpreting offsets, group rebalancing, and exactly‑once semantics.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Consumers and Consumer Groups" (pp. 77-83)

**Detailed explanation of each option:**

1. ❌ **A. Up to the number of replicas can read concurrently because replicas can serve reads.**  
   **Incorrect**. Replicas are used for redundancy and failover, not for concurrent consumer reads. Read requests are directed to the partition leader only.

2. ❌ **B. Multiple consumers can read concurrently if they use the same group id but are in separate consumer processes.**  
   **Incorrect**. Even in separate processes, the same group id results in a partition being assigned to only one consumer per group.

3. ❌ **C. Any number of consumers can read concurrently if they use different consumer group ids.**  
   **Incorrect**. While consumers in different groups can read the same data independently, the question asks about a single consumer group.

4. ✅ **D. Only one consumer can read from a partition at a time because the partition’s log is ordered and its offset is exclusive to a consumer within a group.**  
   **Correct**. Kafka partitions provide an ordered log, and within a consumer group each partition is assigned to exactly one consumer. The assigned consumer is responsible for maintaining the offset for that partition, ensuring at-least-once delivery semantics.

</details>

## Question 22 (Kafka Core Concepts):
A topic is configured with the following properties: `retention.ms=604800000` (7 days), `retention.bytes=1073741824` (1 GB), and `segment.bytes=10485760` (10 MB). After 3 days the topic contains 2 GB of data. Which statement correctly describes what the broker will do regarding data deletion?

- A. E. The broker will delete segments only if they both exceed 1 GB and are older than 7 days.
- B. D. The broker will not delete any segments until the oldest segment is older than 7 days.
- C. A. The broker will delete log segments that are older than 7 days, ignoring the 1 GB size limit.
- D. C. The broker will delete segments that are either older than 7 days or cause the size to exceed 1 GB, whichever condition is met first.
- E. B. The broker will delete the oldest log segments until the total size of the topic falls below 1 GB, regardless of segment age.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka uses two independent retention controls: `retention.ms` (age-based) and `retention.bytes` (size-based). When the log grows beyond the size limit, the broker will trim the oldest segments first until the size falls below `retention.bytes`, regardless of how recent those segments are. Only if the size stays within the limit will `retention.ms` trigger deletion of segments older than the specified age. Thus, in the scenario where the topic reaches 2 GB in 3 days, the broker will immediately start deleting the oldest segments to reduce the size below 1 GB, even though the age threshold has not yet been met. This behavior ensures predictable disk usage while also honoring time-based retention. References: - https://kafka.apache.org/documentation/#brokerconfigs_retentionms - https://kafka.apache.org/documentation/#brokerconfigs_retentionbytes - https://kafka.apache.org/documentation/#log_retention

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 "Topic Defaults" (retention.ms/retention.bytes, pp. 27-33) and Ch. 6 "File Management" (pp. 152-153) — NOTE: retention.bytes triggers deletion of oldest segments until size is under the limit, independent of retention.ms.

**Detailed explanation of each option:**

1. ❌ **A. E. The broker will delete segments only if they both exceed 1 GB and are older than 7 days.**  
   **Incorrect**. Deletion is triggered by each limit independently, the broker does not require both to be satisfied simultaneously.

2. ❌ **B. D. The broker will not delete any segments until the oldest segment is older than 7 days.**  
   **Incorrect**. The size limit can trigger deletion before the age threshold is reached.

3. ❌ **C. A. The broker will delete log segments that are older than 7 days, ignoring the 1 GB size limit.**  
   **Incorrect**. The size limit defined by `retention.bytes` is enforced in addition to age, the broker will not ignore it.

4. ❌ **D. C. The broker will delete segments that are either older than 7 days or cause the size to exceed 1 GB, whichever condition is met first.**  
   **Incorrect**. The broker does not wait for both conditions, it will enforce the size limit before the age limit when the size is exceeded.

5. ✅ **E. B. The broker will delete the oldest log segments until the total size of the topic falls below 1 GB, regardless of segment age.**  
   **Correct**. When the total log size exceeds `retention.bytes`, the broker trims the oldest segments first to bring the size under the limit, even if those segments are younger than the age threshold.

</details>

## Question 23 (Kafka Producers):
When developing a Kafka client, which of the following techniques are valid ways to handle send errors in a producer application?

- A. Set `acks=0` to skip broker acknowledgements, preventing send failures from propagating to the client.
- B. Enable idempotence (`enable.idempotence=true`) which turns on retries and duplicate suppression for transient errors.
- C. Configure `retries` and `retry.backoff.ms` so the producer automatically retries on transient failures.
- D. Configure `linger.ms` to delay sends, this will buffer errors and reduce failures.
- E. Set `max.block.ms` to a low value to reduce latency, errors will be returned immediately.
- F. Use the `Callback` interface when calling `send()` to receive asynchronous error information.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

In a Kafka producer, error handling is primarily managed through configuration and callbacks. The `retries` and `retry.backoff.ms` settings let the client automatically retry transient failures. The `Callback` interface provides asynchronous notification of send success or failure, allowing the application to react without blocking. Enabling idempotence (`enable.idempotence=true`) internally configures retries and ensures exactly‑once delivery by coordinating with the broker. Settings like `max.block.ms`, `acks=0`, and `linger.ms` affect throughput or blocking behavior but do not directly manage error recovery. Understanding these mechanisms is crucial for building resilient client applications that meet Confluent Certified Developer expectations.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Sending a Message..." (pp. 52-54) and Ch. 7 "Configuring Producer Retries" (p. 171)

**Detailed explanation of each option:**

1. ❌ **A. Set `acks=0` to skip broker acknowledgements, preventing send failures from propagating to the client.**  
   **Incorrect**. While `acks=0` eliminates the acknowledgment requirement, it also removes guarantee of delivery and any failure notification, it does not provide error handling.

2. ✅ **B. Enable idempotence (`enable.idempotence=true`) which turns on retries and duplicate suppression for transient errors.**  
   **Correct**. Idempotence automatically configures `retries`, `acks=all`, and `max.in.flight.requests.per.connection=5` to guarantee per-partition exactly‑once (no duplicates, no reordering) writes and safe retries for transient errors, simplifying error handling.

3. ✅ **C. Configure `retries` and `retry.backoff.ms` so the producer automatically retries on transient failures.**  
   **Correct**. The Producer configuration `retries` controls the number of retry attempts, and `retry.backoff.ms` specifies the wait time between retries. These settings allow the producer to recover from temporary network or broker issues without application intervention.

4. ❌ **D. Configure `linger.ms` to delay sends, this will buffer errors and reduce failures.**  
   **Incorrect**. `linger.ms` controls batching delay to improve throughput but does not influence error handling or retry behavior.

5. ❌ **E. Set `max.block.ms` to a low value to reduce latency, errors will be returned immediately.**  
   **Incorrect**. `max.block.ms` limits how long `send()` may block when the producer's buffer is full, it does not affect error detection or retry logic.

6. ✅ **F. Use the `Callback` interface when calling `send()` to receive asynchronous error information.**  
   **Correct**. The `send(ProducerRecord, Callback)` overload delivers a `Callback` that receives a `RecordMetadata` on success or a `Throwable` on failure, enabling non‑blocking error handling.

</details>

## Question 24 (Application Observability):
When developing a Kafka client application in a Confluent environment, which of the following are valid and recommended approaches for monitoring its performance and health?

- A. Integrate the application with Prometheus using the Prometheus JMX exporter or Micrometer to expose client metrics.
- B. Use Confluent Control Center to view consumer lag, throughput, and overall system health.
- C. Use the JMX metrics exposed by the Kafka client libraries and ingest them into a monitoring system.
- D. Configure the application to write logs to STDOUT and parse them with an ELK stack for monitoring.
- E. Rely solely on Kafka's AdminClient to query metrics at runtime.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Monitoring Kafka clients relies on collecting structured metrics rather than raw logs. JMX metrics are the built‑in, low‑overhead source of client telemetry. Exposing these metrics to Prometheus (via exporters or Micrometer) allows real‑time visualization and alerting. Confluent Control Center aggregates these metrics across the ecosystem, offering dashboards for consumer lag, throughput, and broker health, which are essential for observing application behavior at scale. Logging, while useful for troubleshooting, does not provide the quantitative data needed for observability, and the AdminClient does not support continuous metric collection. These three methods together form a comprehensive monitoring strategy for Confluent Certified Developer for Apache Kafka candidates.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Client Monitoring" (pp. 370-378)

**Detailed explanation of each option:**

1. ✅ **A. Integrate the application with Prometheus using the Prometheus JMX exporter or Micrometer to expose client metrics.**  
   **Correct**. Prometheus can scrape JMX metrics via an exporter, or libraries like Micrometer can convert metrics to Prometheus format. This approach enables real‑time dashboards and alerts. (Correct)

2. ✅ **B. Use Confluent Control Center to view consumer lag, throughput, and overall system health.**  
   **Correct**. Control Center aggregates metrics from Kafka brokers, Connect, and clients, presenting them in dashboards that track lag, throughput, and system health. It is a recommended tool for monitoring application performance. (Correct)

3. ✅ **C. Use the JMX metrics exposed by the Kafka client libraries and ingest them into a monitoring system.**  
   **Correct**. Kafka clients publish a rich set of JMX metrics (e.g., records sent, fetch latency, batch size). These can be scraped by JMX exporters or consumed directly by monitoring tools such as Prometheus or Grafana. This is the standard, low‑overhead way to observe client behavior. (Correct)

4. ❌ **D. Configure the application to write logs to STDOUT and parse them with an ELK stack for monitoring.**  
   **Incorrect**. While logging is useful for debugging, it does not provide structured, queryable metrics for performance monitoring. Logs are not the primary mechanism for observability of Kafka clients. (Incorrect)

5. ❌ **E. Rely solely on Kafka's AdminClient to query metrics at runtime.**  
   **Incorrect**. AdminClient is intended for topic and cluster management, not for continuous metric collection or observability. It cannot provide real‑time monitoring of application performance. (Incorrect)

</details>

## Question 25 (Kafka Core Concepts):
Which statement accurately describes the behavior of the leader replica in a Kafka partition when the partition’s replication factor is greater than one?

- A. The leader replica accepts all read and write requests, while followers only replicate the leader’s log.
- B. The leader replica replicates its log to all follower replicas but does not receive any write requests itself.
- C. The leader replica is responsible only for read requests, write requests are forwarded to follower replicas.
- D. The leader replica can be any broker in the cluster and may change arbitrarily without affecting consumers.
- E. The leader replica must have the highest broker ID in the cluster to be elected.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In a replicated partition, the leader broker is the single source of truth for that partition: it accepts all producer writes and consumer reads, and it streams its log entries to follower replicas. Followers do not process client requests, they only replicate the leader’s data to provide durability and high availability. Leader election is deterministic based on broker state and configuration, not on broker IDs, and rebalancing can affect consumer offsets. Understanding this leader/follower dynamic is crucial for troubleshooting replication lag, designing partition assignments, and optimizing consumer performance. For more detail, see the official Kafka documentation on leaders and followers (https://kafka.apache.org/documentation/#leadersandfollowers).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-141)

**Detailed explanation of each option:**

1. ✅ **A. The leader replica accepts all read and write requests, while followers only replicate the leader’s log.**  
   **Correct**. In Kafka, the leader is the sole broker that processes client read/write operations for a partition, followers simply copy the leader’s log for fault tolerance.

2. ❌ **B. The leader replica replicates its log to all follower replicas but does not receive any write requests itself.**  
   **Incorrect**. The leader does receive all writes, it then streams those writes to followers.

3. ❌ **C. The leader replica is responsible only for read requests, write requests are forwarded to follower replicas.**  
   **Incorrect**. The leader handles both reads and writes, followers never receive client writes.

4. ❌ **D. The leader replica can be any broker in the cluster and may change arbitrarily without affecting consumers.**  
   **Incorrect**. Partially incorrect. While any broker can become leader, a rebalance can affect consumer offsets and pause/resume behavior, so it is not arbitrary or invisible.

5. ❌ **E. The leader replica must have the highest broker ID in the cluster to be elected.**  
   **Incorrect**. Leader election is based on partition assignment and follower liveness, not broker ID.

</details>

## Question 26 (Kafka Ecosystem):
A development team needs to build a microservice that processes real‑time click‑stream data, enriches each event with stateful aggregation (e.g., per‑user click counts), and emits the transformed records to another topic. The service must be lightweight, deployed in a container, and use a client library that abstracts away most of the boilerplate of managing partitions and offsets. Which Kafka client API should the team use?

- A. Kafka Producer API
- B. KSQL
- C. Kafka Streams API
- D. Kafka Consumer API
- E. Kafka Connect API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The Kafka Streams API is the appropriate client for lightweight, container‑deployed microservices that need stateful, real‑time processing. It abstracts partition management, offset commits, and fault tolerance while providing DSL primitives for joins, aggregations, and windowing. The Producer and Consumer APIs are low‑level and would force manual handling of state and offset logic. Kafka Connect is geared toward integration pipelines, not in‑app transformations. KSQL is a separate service offering declarative SQL, but it requires its own runtime. Refer to the official Kafka Streams documentation for detailed usage patterns: https://kafka.apache.org/23/documentation/streams/overview.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ❌ **A. Kafka Producer API**  
   **Incorrect**. The Producer API is a low‑level client for sending records. It does not provide built‑in stateful processing or aggregation capabilities, so the team would need to implement all logic manually, which defeats the purpose of a lightweight microservice.

2. ❌ **B. KSQL**  
   **Incorrect**. KSQL is a streaming SQL engine that runs as a separate service. While it offers declarative stream processing, it requires an additional process and is not a client library to be embedded in a microservice.

3. ✅ **C. Kafka Streams API**  
   **Correct**. Kafka Streams is a high‑level client library that provides composable DSL for transformations, stateful operations, windowing, and built‑in fault tolerance. It runs as a lightweight Java application, ideal for microservices that require real‑time processing and aggregation.

4. ❌ **D. Kafka Consumer API**  
   **Incorrect**. The Consumer API is a low‑level client for reading records. While it can be used to implement custom logic, it also lacks out‑of‑the‑box state management, windowing, and exactly‑once guarantees needed for real‑time aggregation.

5. ❌ **E. Kafka Connect API**  
   **Incorrect**. Kafka Connect is designed for ETL pipelines between Kafka and external systems. It is not intended for fine‑grained, stateful transformations within a microservice.

</details>

## Question 27 (Application Observability):
When diagnosing a Kafka application that is experiencing inconsistent message consumption and occasional timeouts, which of the following approaches are appropriate for effective troubleshooting and observability? (Select all that apply)

- A. Run kafka-consumer-groups.sh --bootstrap-server <broker> --describe --group <group-id> to view offsets and lag.
- B. Inspect broker logs for exceptions such as TimeoutException or NotEnoughReplicas to identify network or replication issues.
- C. Use Confluent Control Center’s consumer‑group lag view to see which partitions are behind.
- D. Query the internal __consumer_offsets topic directly with kafka-console-consumer.sh to calculate lag.
- E. Rely solely on the consumer application stack trace to determine the root cause.
- F. Use kafka-run-class kafka.tools.ConsumerGroupCommand to display consumer group offsets.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

Effective Kafka troubleshooting combines application‑level insight with broker‑level observability. Inspecting broker logs (option 2) uncovers systemic failures, while Control Center (option 3) and the consumer‑group describe CLI (option 4) provide real‑time metrics on lag and throughput. These tools are part of the official Confluent ecosystem and align with the platform’s monitoring guidance (see https://docs.confluent.io/platform/current/monitoring/monitoring.html and https://docs.confluent.io/platform/current/monitoring/control-center.html). Directly reading __consumer_offsets (option 1) or using legacy commands (option 5) is technically possible but not recommended for routine diagnostics. Relying only on stack traces (option 6) ignores critical infrastructure signals. Together, options 2‑4 offer a comprehensive, supported approach to diagnosing consumer lag and timeout issues.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Consumer Metrics" / "Lag Monitoring" (pp. 373-377)

**Detailed explanation of each option:**

1. ✅ **A. Run kafka-consumer-groups.sh --bootstrap-server <broker> --describe --group <group-id> to view offsets and lag.**  
   **Correct**. The CLI tool provides partition‑level offset information, current lag, and assignment details. It is a lightweight, scriptable way to audit consumer health and is an official, supported method for troubleshooting.

2. ✅ **B. Inspect broker logs for exceptions such as TimeoutException or NotEnoughReplicas to identify network or replication issues.**  
   **Correct**. Broker logs provide definitive evidence of underlying problems that can cause consumer stalls or timeouts. They expose network partitions, replication lags, or disk I/O bottlenecks that impact overall throughput. This is a core observability practice and is therefore a correct troubleshooting step.

3. ✅ **C. Use Confluent Control Center’s consumer‑group lag view to see which partitions are behind.**  
   **Correct**. Control Center aggregates JMX metrics and presents real‑time lag, throughput, and consumer health. It is specifically designed for visibility into consumer performance and is the recommended tool for observing lag issues.

4. ❌ **D. Query the internal __consumer_offsets topic directly with kafka-console-consumer.sh to calculate lag.**  
   **Incorrect**. While it is technically possible to read the __consumer_offsets topic, the data is encoded in a binary format and requires manual offset calculations. This low‑level approach is error‑prone and not recommended for day‑to‑day troubleshooting. Use the built‑in metrics or tools instead.

5. ❌ **E. Rely solely on the consumer application stack trace to determine the root cause.**  
   **Incorrect**. Application stack traces may indicate errors in the consumer code, but they do not reveal broker‑level issues such as replication lag or network delays. Therefore, this approach is insufficient on its own.

6. ❌ **F. Use kafka-run-class kafka.tools.ConsumerGroupCommand to display consumer group offsets.**  
   **Incorrect**. This older command is still functional but has been superseded by kafka-consumer-groups.sh. While it can work, it is not the preferred or most up‑to‑date approach for observability.

</details>

## 🚫 Question 28 (Kafka Producers):
When deploying Kafka producer clients in a high‑performance environment, which of the following configuration options or deployment strategies are recommended for maximizing throughput and minimizing latency?

- A. Set "max.in.flight.requests.per.connection" to a high value (e.g., 20) to allow more outstanding requests and reduce latency.
- B. Disable "enable.idempotence" to avoid the overhead of duplicate detection and increase throughput.
- C. Configure a larger "batch.size" and a small "linger.ms" to allow the producer to send larger batches more quickly.
- D. Specify a unique "client.id" for each producer instance to improve metrics visibility and debugging.
- E. Create a single producer instance that is shared by all threads in the application.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, E

**Explanation:**

High‑performance Kafka deployments focus on tuning batch sizes and reusing producer resources. A larger batch.size with a small linger.ms lets the producer accumulate more records per request, reducing per‑record overhead and improving throughput. The Kafka producer is thread‑safe, and sharing a single producer instance across all application threads is the recommended pattern: it amortizes buffer memory, batching, and connections, yielding higher throughput than creating many producers. Pushing max.in.flight.requests.per.connection to very high values (e.g., 20) gives little real benefit and risks reordering, with idempotence enabled it is capped at 5 anyway. Disabling idempotence trades reliability for a negligible gain, and a unique client.id only aids observability. These align with the producer guidance in the book and the official docs.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 3 "Constructing a Kafka Producer" (p. 51, "a producer object can be used by multiple threads") and "linger.ms"/"batch.size" (pp. 59-60).

**Detailed explanation of each option:**

1. ❌ **A. Set "max.in.flight.requests.per.connection" to a high value (e.g., 20) to allow more outstanding requests and reduce latency.**  
   **Incorrect**. A handful of in‑flight requests already saturates the connection, pushing it to 20 yields little additional throughput and increases the risk of out‑of‑order delivery. When idempotence is enabled, Kafka caps this value at 5, so a setting of 20 is not even honored. This is not a recommended tuning.

2. ❌ **B. Disable "enable.idempotence" to avoid the overhead of duplicate detection and increase throughput.**  
   **Incorrect**. Idempotence adds negligible overhead and, since Kafka 3.0, is enabled by default. Disabling it sacrifices duplicate‑free, ordered delivery for no meaningful performance gain, so it is not recommended.

3. ✅ **C. Configure a larger "batch.size" and a small "linger.ms" to allow the producer to send larger batches more quickly.**  
   **Correct**. Increasing batch.size increases the amount of data sent per request, and a small linger.ms reduces the delay before a batch is sent. Together they improve throughput without adding noticeable latency, and are recommended for high‑performance deployments.

4. ❌ **D. Specify a unique "client.id" for each producer instance to improve metrics visibility and debugging.**  
   **Incorrect**. client.id does not affect throughput or latency. It provides unique identifiers for metrics, logs, and broker‑side tracing, which help monitoring and troubleshooting but are not a performance tuning.

5. ✅ **E. Create a single producer instance that is shared by all threads in the application.**  
   **Correct**. The Kafka producer is thread‑safe and is explicitly designed to be shared across threads. A single shared instance amortizes its record accumulator, batching, buffer memory, and broker connections, generally achieving higher throughput than many independent producers.

</details>

## Question 29 (Stream Processing):
In a Kafka Streams application that aggregates sensor readings by device ID, you want to guarantee that every record processed before a failure is reflected in the aggregate when the application restarts. Which Streams configuration setting is essential to enable this guarantee?

- A. Set the replication factor of the input topic to 3.
- B. Configure `state.dir` to point to a persistent, non‑volatile storage location.
- C. Set `num.standby.replicas` to 2.
- D. Set `commit.interval.ms` to a very low value.
- E. Set the property `processing.guarantee` to `exactly_once`.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka Streams achieves lossless, exactly‑once processing through the `processing.guarantee` configuration. When set to `exactly_once` (or the newer `exactly_once_v2`), Streams ensures that state updates and output records are written atomically to both the local state store and the changelog topics, and that offset commits are synchronized with state updates. This guarantees that upon restart, the application can recover a complete and consistent state without replaying or losing any records. Other settings such as commit interval, state directory location, topic replication, or standby replicas influence performance or fault tolerance but do not provide the core exactly‑once guarantee required for reliable aggregation after failures.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Set the replication factor of the input topic to 3.**  
   **Incorrect**. Increasing replication reduces the likelihood of a topic becoming unavailable, but it does not affect the atomicity of state updates or the guarantee that all processed records survive a crash.

2. ❌ **B. Configure `state.dir` to point to a persistent, non‑volatile storage location.**  
   **Incorrect**. While a persistent `state.dir` is good practice for durability, Streams automatically recovers state from changelog topics even if `state.dir` is on a temporary filesystem. Therefore, it is not strictly essential for the guarantee of exact‑once semantics.

3. ❌ **C. Set `num.standby.replicas` to 2.**  
   **Incorrect**. Standby replicas provide fault tolerance for state stores but are not required for the application to recover exactly‑once semantics, they only improve recoverability after a node failure.

4. ❌ **D. Set `commit.interval.ms` to a very low value.**  
   **Incorrect**. A low commit interval reduces the time between offset commits, but it does not prevent loss of state updates if the application crashes before a commit. It merely makes the system more resilient to short outages, not to full failures.

5. ✅ **E. Set the property `processing.guarantee` to `exactly_once`.**  
   **Correct**. This setting enables Kafka Streams’ exactly‑once processing semantics. It ensures that state updates and output records are committed atomically and that any records processed before a failure are reliably reflected in the aggregate upon recovery. Without this guarantee, records could be lost or duplicated during a crash.

</details>

## Question 30 (Kafka Producers):
Which of the following Kafka producer configuration settings can you adjust to increase throughput and lower latency for a producer application while maintaining reasonable data reliability?

- A. Set acks to 0.
- B. Enable idempotence=true.
- C. Increase max.block.ms to 60,000 ms.
- D. Set compression.type to snappy.
- E. Set batch.size to 1,048,576 bytes (1 MB).
- F. Set linger.ms to 5 ms.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, E, F

**Explanation:**

Producer tuning primarily focuses on batching, linger, and compression to reduce network round‑trips and payload size, thereby boosting throughput and lowering latency. A larger batch.size lets the broker pack more records into a single request, improving throughput but potentially adding a small delay if records arrive slowly. A small linger.ms allows the producer to wait briefly for additional records before sending, striking a balance between batch fullness and response time. Compression (e.g., snappy) cuts the message payload, reducing bandwidth usage and time spent on network I/O, while still keeping CPU overhead reasonable. Settings like acks=0, max.block.ms, or enabling idempotence are not intended for performance gains, they either trade durability for speed or introduce unnecessary blocking/overhead.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "compression.type" (p. 59)

**Detailed explanation of each option:**

1. ❌ **A. Set acks to 0.**  
   **Incorrect**. While this maximizes write speed, it removes durability guarantees. It is not a recommended tuning step for maintaining reasonable data reliability.

2. ❌ **B. Enable idempotence=true.**  
   **Incorrect**. Idempotence ensures exactly‑once semantics but adds a small CPU overhead. It is a reliability feature, not a performance‑tuning option.

3. ❌ **C. Increase max.block.ms to 60,000 ms.**  
   **Incorrect**. This parameter controls how long the producer blocks when its buffer is full. Raising it can cause longer blocking periods and increased latency, and does not directly improve throughput.

4. ✅ **D. Set compression.type to snappy.**  
   **Correct**. Compressing records reduces the amount of data sent over the network, lowering bandwidth usage and network I/O time. Snappy offers a good balance of compression ratio and CPU cost, making it suitable for throughput‑centric tuning.

5. ✅ **E. Set batch.size to 1,048,576 bytes (1 MB).**  
   **Correct**. A larger batch allows the producer to group more records into a single network request, reducing per‑record overhead and increasing throughput. If the batch does not fill quickly, a modest delay may occur, but the trade‑off is usually acceptable for high‑volume workloads.

6. ✅ **F. Set linger.ms to 5 ms.**  
   **Correct**. This setting tells the producer to wait up to 5 ms for more records before sending a batch. It improves batch completion without introducing significant latency, thereby boosting throughput.

</details>

## Question 31 (Application Development):
Which of the following configuration settings or code practices are required to implement **exactly‑once** processing semantics in Apache Kafka when using the Java Producer and Consumer APIs? Select all that apply.

- A. Calling `Consumer.commitSync()` after each message is processed.
- B. Using `Producer.send()` without a callback.
- C. Setting the producer property `acks=all`.
- D. Setting a unique `transactional.id` on the producer.
- E. Configuring the consumer with `enable.auto.commit=false`.
- F. Setting the producer property `enable.idempotence=true`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, E, F

**Explanation:**

Exactly‑once processing in Kafka hinges on three key practices: the producer must be idempotent and transactional, which requires `enable.idempotence=true` and a unique `transactional.id`, the consumer must disable automatic offset commits so that offsets can be committed only after the transaction succeeds (`enable.auto.commit=false`). The other options are either redundant (acks=all is set automatically), optional, or incorrect (callbacks and per‑message commits). These settings together ensure that records are neither lost nor duplicated even across failures. For more detail, see the Kafka Producer configuration docs (https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence) and the Exactly‑Once semantics guide (https://docs.confluent.io/platform/current/kafka/producer.html#exactly-once).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 "Exactly-Once Semantics" (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Calling `Consumer.commitSync()` after each message is processed.**  
   **Incorrect**. Manual commits are required, but committing after every message is not necessary, committing after the transaction commit is sufficient. Thus this option is not a distinct requirement.

2. ❌ **B. Using `Producer.send()` without a callback.**  
   **Incorrect**. The callback is optional and does not influence exactly‑once semantics, it merely provides async error handling.

3. ❌ **C. Setting the producer property `acks=all`.**  
   **Incorrect**. While `acks=all` contributes to idempotence, it is not a separate requirement when `enable.idempotence` is true, the producer automatically sets `acks=all`. Therefore this option alone is not a distinct requirement for exactly‑once semantics.

4. ✅ **D. Setting a unique `transactional.id` on the producer.**  
   **Correct**. A transactional producer requires a persistent transactional ID to identify the transaction across restarts, without it, `beginTransaction` fails.

5. ✅ **E. Configuring the consumer with `enable.auto.commit=false`.**  
   **Correct**. Offsets must be committed manually after a successful transaction commit to preserve exactly‑once behavior.

6. ✅ **F. Setting the producer property `enable.idempotence=true`.**  
   **Correct**. This enables the producer to deduplicate retries, a core part of exactly‑once delivery. It must be set for transactional writes.

</details>

## Question 32 (Programming & Serialization):
When a Producer sends a record with a non‑null key, which of the following best describes how Kafka determines the target partition for that record?

- A. Kafka applies the Murmur2 hash on the byte array of the key and then takes the modulo of the result with the topic’s partition count.
- B. Kafka distributes the record using SHA‑256 of the key to calculate the partition index.
- C. Kafka uses a consistent hashing algorithm that places the key on a virtual ring, minimizing re‑balancing when partitions change.
- D. Kafka simply uses the Java Object.hashCode() of the key, applies an XOR with 0xFFFFFFFF, then takes the modulo with the partition count.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka’s default partitioner is deterministic: it hashes the key’s raw bytes with Murmur2 (Kafka uses Murmur2 only, never Murmur3), then applies modulo with the number of partitions to decide the target partition. This ensures that records with the same key consistently go to the same partition, enabling key‑based ordering and efficient consumer grouping. It is not consistent hashing, nor does it use Java’s hashCode or SHA‑256, which would produce different distributions and potentially poorer performance. Understanding this behavior is essential for designing producers that rely on key ordering or load balancing across partitions.

Source: Apache Kafka docs/source - DefaultPartitioner uses Murmur2 over the serialized key bytes, Kafka: The Definitive Guide 2nd ed. Ch. 3 "Partitions" (pp. 68-70, book notes Kafka's own hash algorithm)

**Detailed explanation of each option:**

1. ✅ **A. Kafka applies the Murmur2 hash on the byte array of the key and then takes the modulo of the result with the topic’s partition count.**  
   **Correct**. The default Kafka partitioner uses the Murmur2 hash function (not Murmur3) on the key’s bytes and maps the (made‑positive) hash to a partition by modding with the number of partitions.

2. ❌ **B. Kafka distributes the record using SHA‑256 of the key to calculate the partition index.**  
   **Incorrect**. SHA‑256 is not used by Kafka’s default partitioner, it relies on Murmur hashing for performance and distribution.

3. ❌ **C. Kafka uses a consistent hashing algorithm that places the key on a virtual ring, minimizing re‑balancing when partitions change.**  
   **Incorrect**. The default partitioner does not implement consistent hashing, it uses a simple modulo approach.

4. ❌ **D. Kafka simply uses the Java Object.hashCode() of the key, applies an XOR with 0xFFFFFFFF, then takes the modulo with the partition count.**  
   **Incorrect**. The partitioner operates on the raw byte array of the key, not on the Java hashCode. It also does not perform the described XOR operation.

</details>

## Question 33 (Kafka Connect):
In Kafka Connect, which Single Message Transform (SMT) can be used to convert a record value that is a numeric string into a Long type, assuming the field name is "amount" and the source schema is String?

- A. ExtractField – extracts a nested field from a complex schema
- B. RegexRouter – modifies the topic name based on a regex
- C. Cast – with "field" set to "amount" and "target.type" set to "org.apache.kafka.connect.data.Long"
- D. StringToLong – a built‑in SMT that casts string to long
- E. TimeFormat – formats timestamp fields

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka Connect provides a set of Single Message Transforms (SMTs) that can be applied on the fly to each record. The Cast SMT is specifically designed for type conversion, by configuring the "field" and "target.type" properties you can transform a String field into a Long, Double, etc. Other SMTs such as RegexRouter or TimeFormat serve different purposes (topic routing, timestamp formatting) and cannot perform type conversion. Understanding which SMT to apply is crucial for data‑shape transformations required by downstream systems or schema registries. See the Confluent documentation on SMTs for syntax and examples.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Single Message Transformations" (pp. 223-225) — NOTE: Cast SMT verified against Kafka Connect SMT docs.

**Detailed explanation of each option:**

1. ❌ **A. ExtractField – extracts a nested field from a complex schema**  
   **Incorrect**. ExtractField retrieves a field from a complex structure, it does not cast the type of a simple string field.

2. ❌ **B. RegexRouter – modifies the topic name based on a regex**  
   **Incorrect**. RegexRouter only changes the destination topic, it does not modify field types.

3. ✅ **C. Cast – with "field" set to "amount" and "target.type" set to "org.apache.kafka.connect.data.Long"**  
   **Correct**. The built‑in Cast SMT changes the type of the specified field to the target type. Setting target.type to org.apache.kafka.connect.data.Long will parse the numeric string into a Long.

4. ❌ **D. StringToLong – a built‑in SMT that casts string to long**  
   **Incorrect**. There is no built‑in SMT named StringToLong in the standard Kafka Connect distribution.

5. ❌ **E. TimeFormat – formats timestamp fields**  
   **Incorrect**. TimeFormat rewrites timestamp fields for Kafka Connect schemas, it is not used for numeric string to Long conversion.

</details>

## Question 34 (Kafka Ecosystem):
When designing a stateful aggregation that requires low‑latency and high throughput, which programming language’s client library is the only one that provides native support for the Kafka Streams API, allowing you to build and deploy stream processing applications directly in the Confluent Platform?

- A. Java, using the official Kafka Streams library
- B. C#, using Confluent.Kafka
- C. Rust, using rdkafka‑rust
- D. Go, using sarama
- E. Python, using confluent-kafka-python

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams is a Java‑based stream processing library that delivers low‑latency, stateful transformations and aggregations with fault‑tolerance and exactly‑once semantics. Because it is only available in Java, the Java client is the sole choice for applications that need native Streams support. All other language clients (Python, Go, .NET, Rust) expose only the Producer/Consumer APIs and lack a dedicated Streams API, forcing developers to implement aggregation logic manually or rely on external frameworks. Selecting Java ensures the highest performance and full integration with the Confluent Schema Registry and other platform services.

Source: Apache Kafka docs - Kafka Streams is a Java/JVM library (no native non-JVM Streams client), Kafka: The Definitive Guide 2nd ed. Ch. 14 (pp. 381-382)

**Detailed explanation of each option:**

1. ✅ **A. Java, using the official Kafka Streams library**  
   **Correct**. Kafka Streams is a pure Java library and is the only client that exposes the Streams API. It provides stateful processing, exactly‑once semantics, and tight integration with the Confluent Schema Registry for Avro/Protobuf. The library is optimized for JVM execution and offers built‑in support for topology building, repartitioning, and windowed aggregations.

2. ❌ **B. C#, using Confluent.Kafka**  
   **Incorrect**. The .NET client offers Producer and Consumer APIs only. It does not include a Streams implementation, so stateful aggregations must be coded manually.

3. ❌ **C. Rust, using rdkafka‑rust**  
   **Incorrect**. rdkafka‑rust wraps librdkafka and supports Producer/Consumer APIs but does not provide a Streams API or built‑in stateful processing primitives.

4. ❌ **D. Go, using sarama**  
   **Incorrect**. sarama provides Producer and Consumer functionality but lacks a dedicated Streams library. Go developers typically implement stateful logic in application code or use external stream processing frameworks.

5. ❌ **E. Python, using confluent-kafka-python**  
   **Incorrect**. confluent‑kafka‑python is a wrapper around the native C librdkafka client and offers only the Producer and Consumer APIs. It does not expose the Streams API, stateful processing must be implemented manually or via external services.

</details>

## Question 35 (Programming & Serialization):
Which of the following statements about Kafka SerDes and Confluent Schema Registry are true?

- A. Using `KeyValueSerde` with Avro serializes both key and value under the same schema ID.
- B. Each message encoded by Confluent SerDe has a magic byte followed by a 4‑byte schema ID that references the Schema Registry.
- C. The `KafkaAvroSerializer` automatically registers a new schema with the Schema Registry when it encounters an unknown schema.
- D. The `KafkaProtobufSerializer` embeds the Protobuf schema in every message so no registration is needed.
- E. Setting `specific.avro.reader=true` in the `KafkaAvroDeserializer` configuration causes the deserializer to return a POJO generated from the Avro schema.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

Confluent SerDes follow a common pattern: a magic byte and a 4‑byte schema ID precede the payload, allowing the consumer to retrieve the schema from the registry. The Avro serializer will automatically register unknown schemas, whereas Protobuf also requires registration—embedding the schema is not supported. `KeyValueSerde` treats key and value separately, each with its own schema ID. When `specific.avro.reader=true`, the Avro deserializer returns POJOs instead of generic records. Understanding these behaviors is essential for schema‑management and data‑modeling in Kafka streams.

Source: Confluent Schema Registry docs - "Wire format" (magic byte 0 + 4-byte schema ID), Kafka: The Definitive Guide 2nd ed. Ch. 3 "Using Avro Records with Kafka" (pp. 65-68)

**Detailed explanation of each option:**

1. ❌ **A. Using `KeyValueSerde` with Avro serializes both key and value under the same schema ID.**  
   **Incorrect**. False. `KeyValueSerde` serializes the key and value independently, each getting its own schema ID in the message.

2. ✅ **B. Each message encoded by Confluent SerDe has a magic byte followed by a 4‑byte schema ID that references the Schema Registry.**  
   **Correct**. True. This prefix is used by all Confluent SerDes (Avro, JSON Schema, Protobuf) to locate the schema in the registry.

3. ✅ **C. The `KafkaAvroSerializer` automatically registers a new schema with the Schema Registry when it encounters an unknown schema.**  
   **Correct**. True. The serializer checks the registry and, if the schema is not present, it registers it under the specified subject before serializing.

4. ❌ **D. The `KafkaProtobufSerializer` embeds the Protobuf schema in every message so no registration is needed.**  
   **Incorrect**. False. Protobuf requires the schema to be registered, the serializer writes a magic byte and a 4‑byte schema ID just like Avro.

5. ✅ **E. Setting `specific.avro.reader=true` in the `KafkaAvroDeserializer` configuration causes the deserializer to return a POJO generated from the Avro schema.**  
   **Correct**. True. When this flag is set and the classpath contains the generated classes, the deserializer instantiates the specific record type.

</details>

## Question 36 (Kafka Connect):
In a Kafka Connect distributed cluster, how are source connector tasks assigned to workers, and what happens when a worker that hosts tasks fails?

- A. All tasks of a connector are assigned to a single worker for fault isolation, when the worker fails, the tasks are reassigned automatically to a standby worker.
- B. Workers poll a shared registry to fetch tasks, if a worker fails, its tasks are lost until a new worker registers and manually reconfigures them.
- C. Kafka Connect uses round‑robin to assign tasks to workers but does not reassign on failure, connectors must be manually restarted to recover.
- D. Each task is independently assigned to any available worker, when a worker fails, the group coordinator automatically reassigns those tasks to other workers in the cluster.
- E. Tasks are assigned based on the number of topic partitions, a worker’s failure causes only the affected partitions’ tasks to be reassigned.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Connect distributes connector tasks across workers using a group coordinator that maintains a shared view of task ownership. Each task is independent, and the coordinator ensures that tasks are balanced among all active workers. If a worker dies or leaves the group, the coordinator reassigns the tasks that were owned by that worker to the remaining workers, preventing data loss and maintaining throughput. This design eliminates the need for manual task reassignment and provides built‑in fault tolerance. Understanding this mechanism is essential for designing resilient Connect deployments, tuning scalability, and diagnosing issues during worker failures. For more details see the official Connect overview documentation.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. All tasks of a connector are assigned to a single worker for fault isolation, when the worker fails, the tasks are reassigned automatically to a standby worker.**  
   **Incorrect**. Kafka Connect does not bind all tasks of a connector to one worker. Tasks are distributed across workers to achieve load balancing and fault tolerance. A standby worker is not a concept in Kafka Connect.

2. ❌ **B. Workers poll a shared registry to fetch tasks, if a worker fails, its tasks are lost until a new worker registers and manually reconfigures them.**  
   **Incorrect**. Connect does not use a manual registry for tasks. Tasks are automatically rebalanced through the group coordinator without manual reconfiguration.

3. ❌ **C. Kafka Connect uses round‑robin to assign tasks to workers but does not reassign on failure, connectors must be manually restarted to recover.**  
   **Incorrect**. While Connect does use a round‑robin style load distribution, it also handles rebalancing automatically. Manual intervention is not required for task recovery.

4. ✅ **D. Each task is independently assigned to any available worker, when a worker fails, the group coordinator automatically reassigns those tasks to other workers in the cluster.**  
   **Correct**. Connect uses a group coordinator that tracks task ownership. If a worker leaves (e.g., due to failure), the coordinator reassigns its tasks to other workers, maintaining continuous operation.

5. ❌ **E. Tasks are assigned based on the number of topic partitions, a worker’s failure causes only the affected partitions’ tasks to be reassigned.**  
   **Incorrect**. Task assignment is not partition‑aware, tasks are independent of the underlying topic partitions. All tasks of a connector are treated the same in the assignment process.

</details>

## Question 37 (Application Observability):
Which command-line invocation correctly displays the current lag for a consumer group on a Kafka cluster using Confluent Platform 7.x?

- A. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe
- B. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe --topic <topic>
- C. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --offsets
- D. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --list

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The `kafka-consumer-groups` tool is the primary CLI for inspecting consumer group state, including committed offsets and lag. To obtain lag metrics you must use the `--describe` flag, which outputs committed offset, log end offset, and lag for each partition of the specified group. The `--bootstrap-server` flag supplies the broker list, and the `--group` flag identifies the target group. No other flags such as `--topic`, `--offsets`, or `--list` provide the desired lag information. Refer to Confluent’s official documentation for the full syntax: https://docs.confluent.io/platform/current/kafka/cli/kafka-consumer-groups.html

Source: Kafka: The Definitive Guide 2nd ed. Appendix B "Additional Kafka Tools" (pp. 427-432) and Ch. 12 "Consumer Groups" (pp. 312-314)

**Detailed explanation of each option:**

1. ✅ **A. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe**  
   **Correct**. This is the correct syntax. The `--describe` flag causes the tool to output the committed offsets and the current lag for each partition of the group. The `--bootstrap-server` provides the cluster address, and `--group` specifies which consumer group to inspect.

2. ❌ **B. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe --topic <topic>**  
   **Incorrect**. `--topic` IS a recognized flag of `kafka-consumer-groups`, but it is documented for `--reset-offsets`/`--delete-offsets`, not as a filter for `--describe`, A is the canonical invocation for showing lag.

3. ❌ **C. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --offsets**  
   **Incorrect**. `--offsets` is only a sub-option of `--describe` (and is its default). Used alone, no action (`--describe`, `--list`, ...) is specified and the tool errors out.

4. ❌ **D. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --list**  
   **Incorrect**. `--list` lists all consumer groups in the cluster, not the offsets or lag for a specific group. It does not provide the information requested.

</details>

## Question 38 (Stream Processing):
In a Kafka Streams application that performs a stateful aggregation and writes the results to a downstream topic, which configuration and code combination is required to guarantee exactly‑once processing semantics?

- A. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, configure the sink topic with `cleanup.policy=compact`, and set `min.insync.replicas=2` on the sink topic.
- B. Set `processing.guarantee=exactly_once_v2`, use a `KStream` aggregation via `transformValues`, and enable idempotent producer by setting `enable.idempotence=true` on the Streams producer.
- C. Set `processing.guarantee=exactly_once`, use a `KStream` to `to()` with `Produced.with()` and set `acks=all` on the sink topic.
- D. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, and rely on the default transaction id prefix derived from `application.id`.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Exactly‑once V2 in Kafka Streams relies on a per‑task transaction that encompasses state updates and output writes. To achieve it, the application must set `processing.guarantee=exactly_once_v2` and use a stateful operator such as a `KTable` aggregation or join. The transaction ID is automatically derived from `application.id` (or overridden via `transactional.id.prefix`) so no manual idempotence or topic cleanup settings are required. Options that omit the stateful operator, use older guarantees, or include unnecessary topic configs fail to provide the required transactional guarantees. Understanding this configuration is essential for building robust stream applications that avoid duplicates and ensure data consistency.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, configure the sink topic with `cleanup.policy=compact`, and set `min.insync.replicas=2` on the sink topic.**  
   **Incorrect**. The configuration includes unnecessary topic settings that do not influence exactly‑once guarantees. `cleanup.policy=compact` and `min.insync.replicas` are irrelevant to transaction handling. The combination is therefore incorrect.

2. ❌ **B. Set `processing.guarantee=exactly_once_v2`, use a `KStream` aggregation via `transformValues`, and enable idempotent producer by setting `enable.idempotence=true` on the Streams producer.**  
   **Incorrect**. While `enable.idempotence=true` is automatically enabled for exactly‑once, `transformValues` is a stateless operator. A stateful aggregation is required for the transactional guarantee, so this option is insufficient.

3. ❌ **C. Set `processing.guarantee=exactly_once`, use a `KStream` to `to()` with `Produced.with()` and set `acks=all` on the sink topic.**  
   **Incorrect**. `processing.guarantee=exactly_once` refers to the older exactly‑once V1 guarantee, which is deprecated and does not provide the same level of isolation as V2. Additionally, the use of `acks=all` alone does not enable transactional guarantees. Thus this option is incorrect.

4. ✅ **D. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, and rely on the default transaction id prefix derived from `application.id`.**  
   **Correct**. Exactly‑once V2 requires `processing.guarantee=exactly_once_v2`. A `KTable` aggregation is stateful, and Kafka Streams automatically derives a `transactional.id` from `application.id` unless overridden. This combination satisfies all requirements for exactly‑once semantics.

</details>

## Question 39 (Stream Processing):
In a Kafka Streams application that performs a stateful join and writes the results to a sink using the Streams API, which configuration is required to guarantee exactly‑once processing semantics across the join and the sink?

- A. Setting `processing.guarantee=exactly_once_v2` alone is sufficient, Kafka Streams will automatically handle idempotent producers, transaction boundaries, and state store snapshots.
- B. Setting `processing.guarantee=exactly_once_v2` **and** `commit.interval.ms=10000` is required to commit offsets for exactly‑once.
- C. Setting `processing.guarantee=exactly_once_v2` **and** `transaction.state.log.replication.factor=3` is required to enable transactions.
- D. Setting `processing.guarantee=exactly_once_v2` **and** `cache.max.bytes.buffering=0` is required for exactly‑once semantics.
- E. Setting `processing.guarantee=exactly_once_v2` **and** `enable.idempotence=true` on the underlying producer is necessary for exactly‑once.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams implements exactly‑once semantics through a single configuration property, `processing.guarantee=exactly_once_v2`. This setting enables transactional producers and consumers, idempotence, and state store snapshot handling internally. No other application‑level properties are required, all auxiliary settings (e.g., commit interval, cache size, or manual idempotence) are either optional or automatically managed. Misconceptions often arise from conflating these auxiliary properties with the core guarantee. Understanding that `processing.guarantee` alone is sufficient allows developers to correctly configure and reason about fault‑tolerance and idempotency in stream processing pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ✅ **A. Setting `processing.guarantee=exactly_once_v2` alone is sufficient, Kafka Streams will automatically handle idempotent producers, transaction boundaries, and state store snapshots.**  
   **Correct**. The single `processing.guarantee` setting enables the full exactly‑once processing stack in Streams, including transactional producer/consumer, idempotence, and state store checkpoints. No additional properties are required.

2. ❌ **B. Setting `processing.guarantee=exactly_once_v2` **and** `commit.interval.ms=10000` is required to commit offsets for exactly‑once.**  
   **Incorrect**. While `commit.interval.ms` controls how often offsets are committed, it is not a prerequisite for exactly‑once semantics. The guarantee is achieved solely by the `processing.guarantee` setting.

3. ❌ **C. Setting `processing.guarantee=exactly_once_v2` **and** `transaction.state.log.replication.factor=3` is required to enable transactions.**  
   **Incorrect**. The replication factor of the internal transaction log topics is managed by the cluster and does not need to be configured in the Streams application.

4. ❌ **D. Setting `processing.guarantee=exactly_once_v2` **and** `cache.max.bytes.buffering=0` is required for exactly‑once semantics.**  
   **Incorrect**. Disabling the cache affects performance but not the exactly‑once guarantee.

5. ❌ **E. Setting `processing.guarantee=exactly_once_v2` **and** `enable.idempotence=true` on the underlying producer is necessary for exactly‑once.**  
   **Incorrect**. Kafka Streams automatically sets `enable.idempotence=true` when `processing.guarantee` is enabled. Adding it manually is redundant.

</details>

## Question 40 (Kafka Producers):
You are deploying a high‑throughput application that writes millions of records per second to Kafka. Which of the following producer configuration settings and practices will most effectively increase throughput while reducing CPU overhead? Select all that apply.

- A. Enable `idempotence=true` to allow out‑of‑order retries without duplication.
- B. Set `max.request.size` to the maximum allowable value to allow larger batches.
- C. Decrease `linger.ms` to 0 to send messages immediately.
- D. Increase `batch.size` and `linger.ms` to allow more records per request.
- E. Disable `request.timeout.ms` to avoid retries.
- F. Configure `compression.type=gzip` to reduce network I/O.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

Throughput in Kafka producers is primarily governed by how efficiently records are batched and transmitted. Enabling idempotence (`idempotence=true`) provides safe retries and reduces the risk of duplicate processing, indirectly lowering CPU load by avoiding complex duplicate handling. Compression reduces payload size, decreasing network I/O and broker load, gzip offers strong compression at the cost of some CPU, while alternatives like LZ4 or Snappy trade speed for lower compression ratios. Adjusting `batch.size` and `linger.ms` allows the producer to aggregate more records into a single request, reducing the number of round‑trips and associated CPU cycles. The other options either increase memory usage without benefit (max.request.size), force immediate sends (linger.ms=0), or remove retry safeguards (disabling request.timeout.ms), all of which degrade performance or reliability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "compression.type" (p. 59)

**Detailed explanation of each option:**

1. ✅ **A. Enable `idempotence=true` to allow out‑of‑order retries without duplication.**  
   **Correct**. Enabling idempotence ensures safe retries and eliminates duplicate records, which can reduce CPU work spent on duplicate detection during recovery. It also enables transaction support and guarantees exactly‑once delivery, making it a beneficial tuning option for high‑volume producers.

2. ❌ **B. Set `max.request.size` to the maximum allowable value to allow larger batches.**  
   **Incorrect**. Increasing `max.request.size` only raises the upper bound for a single request. It does not improve batching efficiency and can lead to higher memory usage and larger network payloads, which may actually reduce throughput. Therefore this is not a recommended tuning step.

3. ❌ **C. Decrease `linger.ms` to 0 to send messages immediately.**  
   **Incorrect**. Setting `linger.ms` to zero forces the producer to send a request as soon as a record is queued, eliminating batching. This increases network round‑trips and CPU usage, and usually lowers throughput.

4. ✅ **D. Increase `batch.size` and `linger.ms` to allow more records per request.**  
   **Correct**. Larger `batch.size` values and a slightly higher `linger.ms` give the producer time to accumulate more records, resulting in fewer, larger requests. This reduces network overhead and CPU load, leading to higher throughput.

5. ❌ **E. Disable `request.timeout.ms` to avoid retries.**  
   **Incorrect**. Removing the timeout would prevent the producer from retrying failed requests, increasing the chance of data loss and making the system unreliable. It does not improve throughput or CPU usage and is not a valid tuning option.

6. ✅ **F. Configure `compression.type=gzip` to reduce network I/O.**  
   **Correct**. Using gzip (or LZ4/ Snappy) compresses message payloads before transmission, lowering the amount of data sent over the network. This directly improves throughput and can reduce CPU overhead on the broker side, though gzip adds some CPU cost on the producer side. It remains a common tuning practice for bandwidth‑limited environments.

</details>

## Question 41 (Kafka Consumers):
A new Kafka consumer group has started consuming
from a topic but has never committed any offsets.
Which configuration property and value causes the
consumer to read ALL historical records from the
beginning of each partition?

- A. session.timeout.ms=10000
- B. auto.offset.reset=latest
- C. auto.offset.reset=earliest
- D. group.id="my-group"
- E. enable.auto.commit=true

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When a consumer restarts, it queries the broker for the last committed offset for its group. If none exists—such as with a new group or after offsets have been deleted—the consumer falls back to the value of the auto.offset.reset configuration. Setting this property to "earliest" makes the consumer start at the very beginning of each partition, ensuring all historical records are processed. Setting it to "latest" causes the consumer to skip past existing data and only consume new records. The other listed properties affect offset committing, group liveness, or identification, but do not influence the start position for a group without committed offsets. See the Kafka consumer config documentation for more details: https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "auto.offset.reset" (p. 91)

**Detailed explanation of each option:**

1. ❌ **A. session.timeout.ms=10000**  
   **Incorrect**. Controls how long a consumer can be inactive before the group coordinator considers it dead, it has no effect on the start offset.

2. ❌ **B. auto.offset.reset=latest**  
   **Incorrect**. This setting tells the consumer to start at the latest offset (i.e., it will only read records that arrive after the consumer starts). It does **not** apply when a committed offset exists.

3. ✅ **C. auto.offset.reset=earliest**  
   **Correct**. When no committed offset exists for the consumer group, this property causes the consumer to read from the beginning of each partition, allowing replay of historical data.

4. ❌ **D. group.id="my-group"**  
   **Incorrect**. Identifies the consumer group but does not influence the starting offset. It is required for group coordination.

5. ❌ **E. enable.auto.commit=true**  
   **Incorrect**. This flag enables automatic committing of offsets after each poll, but it does not decide where the consumer starts reading when there is no committed offset.

</details>

## Question 42 (Kafka Core Concepts):
When creating a topic with the Kafka command‑line tool (kafka-topics.sh --create) which of the following settings **cannot be** specified as a topic configuration?

- A. num.network.threads
- B. cleanup.policy
- C. retention.ms
- D. compression.type

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Topic configurations are key/value pairs that tailor log behavior on a per‑topic basis. Valid settings include retention.ms, cleanup.policy, compression.type, min.insync.replicas, segment.bytes, max.message.bytes, and more, and can be passed with --config during topic creation. The exception is num.network.threads, a broker‑level property that controls how many threads the broker uses to handle network requests. It applies to the broker process as a whole and has no per‑topic override, so it cannot be specified with --config when creating a topic. Understanding which configs are per‑topic versus broker‑only is essential for correctly tuning Kafka and for passing certification exams. (Note: min.insync.replicas is NOT broker‑only — it has a broker default and a valid topic‑level override, so it can be set per topic.)

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Essential Topic Management" (pp. 118-121) and Ch. 12 "Overriding Topic Configuration Defaults" (pp. 315-317). Verified against Apache Kafka topic-level vs. broker-level config docs: num.network.threads is a broker-only config and has no per-topic override.

**Detailed explanation of each option:**

1. ✅ **A. num.network.threads**  
   **Correct**. num.network.threads is a broker‑level configuration that sets the number of network request handler threads for the broker process. It has no per‑topic equivalent and cannot be passed with --config when creating a topic.

2. ❌ **B. cleanup.policy**  
   **Incorrect**. cleanup.policy (e.g., delete or compact) is a topic‑level setting that can be overridden during topic creation.

3. ❌ **C. retention.ms**  
   **Incorrect**. retention.ms controls how long messages are kept in the log and can be set per topic at creation time.

4. ❌ **D. compression.type**  
   **Incorrect**. compression.type (e.g., gzip, snappy, lz4, zstd) is a valid per‑topic configuration that can be set during creation.

</details>

## Question 43 (Programming & Serialization):
Confluent’s Schema Registry supports several serialization formats for Kafka records. Which of the following formats are fully supported by the Schema Registry for schema registration and evolution?

- A. String
- B. Binary (Bytes)
- C. JSON Schema
- D. JSON (plain)
- E. Protobuf
- F. Avro

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, E, F

**Explanation:**

The Confluent Schema Registry is designed to store, version, and validate schemas for structured data formats. It natively supports Avro, JSON Schema, and Protocol Buffers, offering schema compatibility checks (backward, forward, full) and automatic ID assignment for efficient encoding. While plain JSON, String, and raw Bytes can be used as key/value payloads, they lack the metadata and validation features that the registry provides. Knowing which formats are fully supported helps developers choose the right schema type for compatibility, performance, and tooling integration.

Source: Confluent Schema Registry docs - supported formats: Avro, JSON Schema, Protobuf

**Detailed explanation of each option:**

1. ❌ **A. String**  
   **Incorrect**. String is a primitive type without a schema, the Schema Registry does not manage or enforce schemas for plain string values.

2. ❌ **B. Binary (Bytes)**  
   **Incorrect**. Raw bytes are treated as opaque data, the registry does not impose a schema on arbitrary binary payloads.

3. ✅ **C. JSON Schema**  
   **Correct**. JSON Schema support was added in later releases, enabling the registry to store, validate, and evolve JSON messages using the JSON Schema standard.

4. ❌ **D. JSON (plain)**  
   **Incorrect**. Plain JSON has no built‑in schema or compatibility enforcement, the Schema Registry does not natively validate or version plain JSON messages.

5. ✅ **E. Protobuf**  
   **Correct**. Starting with Confluent Platform 5.5, the Schema Registry added support for Protocol Buffers. It assigns unique IDs and performs compatibility checks similar to Avro.

6. ✅ **F. Avro**  
   **Correct**. The Schema Registry was originally built for Avro schemas and provides strict schema validation, compatibility checks, and automatic ID assignment for Avro messages.

</details>

## Question 44 (Stream Processing):
A Kafka Streams application performs a `groupBy()` followed by an `aggregate()` on a KStream that is sourced from topic **sales** with 3 partitions. The aggregation creates an internal repartition topic with the same number of partitions (3). How many downstream tasks will the Streams application create, and why?

- A. Unlimited tasks, because tasks can be added or removed dynamically during runtime.
- B. Nine tasks, because the number of tasks is the product of the partitions of the source topic and the internal repartition topic.
- C. Six tasks, because the number of tasks is the sum of the partitions of the source topic and the internal repartition topic.
- D. Three tasks, because the number of tasks equals the maximum number of partitions among all source and internal topics, and both topics have 3 partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka Streams, a *task* is a unit of parallelism that processes one partition of each source topic. The total number of tasks is determined by the maximum partition count among all source topics and any internal topics created by the topology (e.g., repartition topics for groupBy). Here both the source topic and the internal repartition topic have 3 partitions, so the maximum is 3. Therefore, the application creates three tasks. Misconceptions often arise from thinking tasks multiply or sum partition counts, but the Streams runtime only uses the maximum value. This behavior is documented in the Kafka Streams Developer Guide under "Task assignment" (https://kafka.apache.org/documentation/streams/developer-guide.html#task_assignment).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Scaling a Topology" (pp. 412-415)

**Detailed explanation of each option:**

1. ❌ **A. Unlimited tasks, because tasks can be added or removed dynamically during runtime.**  
   **Incorrect**. The number of tasks is bounded by the number of partitions of the most‑partitioned source or internal topic and cannot grow beyond that without changing topic partitions.

2. ❌ **B. Nine tasks, because the number of tasks is the product of the partitions of the source topic and the internal repartition topic.**  
   **Incorrect**. Tasks are not created as a product of partitions. The Streams runtime uses the maximum partition count, not the product.

3. ❌ **C. Six tasks, because the number of tasks is the sum of the partitions of the source topic and the internal repartition topic.**  
   **Incorrect**. Kafka Streams does not sum partition counts to determine the number of tasks, it uses the maximum.

4. ✅ **D. Three tasks, because the number of tasks equals the maximum number of partitions among all source and internal topics, and both topics have 3 partitions.**  
   **Correct**. Kafka Streams assigns one task per partition of the topic with the most partitions. Since both the source and the internal topic have 3 partitions, the maximum is 3, so three tasks are created.

</details>

## Question 45 (Kafka Connect):
Which of the following statements about the operation and configuration of Kafka Connect workers, connectors, and tasks are true? Select all that apply.

- A. The number of tasks for a connector is fixed at deployment and cannot be changed without redeploying.
- B. Adding a new worker to a distributed Connect cluster automatically triggers a rebalance of tasks across the cluster.
- C. Connect workers coordinate via ZooKeeper to maintain cluster membership.
- D. Sink connectors automatically delete Kafka topics when the connector is stopped.
- E. Kafka Connect can run in both standalone and distributed modes.
- F. Source connectors can use a file‑based offset storage only when running in standalone mode.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, E, F

**Explanation:**

Kafka Connect offers two deployment modes: standalone for single‑process local testing and distributed for scalable, fault‑tolerant production use. Connector configuration includes "tasks.max" which dictates parallelism and can be altered at runtime to trigger rebalancing. Source connectors rely on file‑based offset storage only in standalone mode, distributed mode stores offsets in Kafka. Task rebalancing is automatic when workers join or leave a distributed cluster. Connect does not delete topics on stop and no longer relies on ZooKeeper for coordination. Understanding these distinctions is essential for designing reliable data pipelines with Connect.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ❌ **A. The number of tasks for a connector is fixed at deployment and cannot be changed without redeploying.**  
   **Incorrect**. The "tasks.max" property in the connector configuration determines the maximum number of parallel tasks, changing it can trigger a rebalance without redeploying the connector.

2. ✅ **B. Adding a new worker to a distributed Connect cluster automatically triggers a rebalance of tasks across the cluster.**  
   **Correct**. Workers register with the cluster and the Connect coordinator rebalances tasks to maintain load balance when the cluster topology changes.

3. ❌ **C. Connect workers coordinate via ZooKeeper to maintain cluster membership.**  
   **Incorrect**. Kafka Connect uses Kafka itself (a dedicated topic) for coordination, ZooKeeper is no longer used in current versions.

4. ❌ **D. Sink connectors automatically delete Kafka topics when the connector is stopped.**  
   **Incorrect**. Sink connectors do not delete topics, they simply stop producing to them. Topic lifecycle is independent.

5. ✅ **E. Kafka Connect can run in both standalone and distributed modes.**  
   **Correct**. Standalone mode runs a single worker process for local testing, while distributed mode runs a cluster of workers that share connector configuration and coordinate via Kafka.

6. ✅ **F. Source connectors can use a file‑based offset storage only when running in standalone mode.**  
   **Correct**. In standalone mode the offset storage is specified by "offset.storage.file.filename". In distributed mode offsets are stored in a Kafka topic.

</details>

## Question 46 (Application Testing):
When writing automated tests for Kafka client applications (producers, consumers, and Kafka Streams topologies) that should run fast and without requiring a live Kafka cluster, which of the following tools or techniques are most appropriate? (Select all that apply)

- A. Run the application against a real Kafka cluster with test topics and manually verify output.
- B. Use MockProducer and MockConsumer to simulate broker interactions for producer/consumer logic.
- C. Employ EmbeddedKafka (from spring-kafka or Testcontainers) to spin up an in‑memory broker for integration tests.
- D. Create topics with AdminClient and then run a real consumer to validate message flow.
- E. Leverage a hypothetical KafkaClient "UnitTest" mode that mocks all broker interactions.
- F. Use Kafka Streams' TopologyTestDriver with MockInputTopic and MockOutputTopic to drive a topology in isolation.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

Unit testing Kafka client code demands tools that remove external dependencies while preserving API semantics. TopologyTestDriver isolates stream logic, EmbeddedKafka offers a quick in‑memory broker for higher‑level integration checks, and MockProducer/MockConsumer verify producer/consumer behavior without network overhead. The other options either rely on a real cluster (integration testing) or reference non‑existent features, thus they are not suitable for fast, isolated unit tests. Understanding the appropriate tool for each test type is essential for efficient test suites in a Confluent Certified Developer context.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Testing" (pp. 131-133) and Ch. 14 "Testing a Topology" (pp. 411-412)

**Detailed explanation of each option:**

1. ❌ **A. Run the application against a real Kafka cluster with test topics and manually verify output.**  
   **Incorrect**. This approach requires an external broker and is considered integration testing, not a lightweight unit test.

2. ✅ **B. Use MockProducer and MockConsumer to simulate broker interactions for producer/consumer logic.**  
   **Correct**. These mock clients allow verification of record metadata and deserialization logic without network traffic.

3. ✅ **C. Employ EmbeddedKafka (from spring-kafka or Testcontainers) to spin up an in‑memory broker for integration tests.**  
   **Correct**. EmbeddedKafka gives a lightweight, fully‑functional broker that can be started and stopped per test, ideal for integration testing without external dependencies.

4. ❌ **D. Create topics with AdminClient and then run a real consumer to validate message flow.**  
   **Incorrect**. While AdminClient can create topics, using a real consumer still depends on a broker, making it an integration test.

5. ❌ **E. Leverage a hypothetical KafkaClient "UnitTest" mode that mocks all broker interactions.**  
   **Incorrect**. No such built‑in mode exists in the Kafka client library.

6. ✅ **F. Use Kafka Streams' TopologyTestDriver with MockInputTopic and MockOutputTopic to drive a topology in isolation.**  
   **Correct**. TopologyTestDriver is specifically designed to test stream topologies without a broker, providing deterministic input and output records.

</details>

## Question 47 (Kafka Producers):
You are deploying a Kafka producer in a latency-sensitive application that sends small JSON messages. Which producer configuration will most directly reduce the round‑trip time for each message while still maintaining safe delivery semantics?

- A. Set `compression.type` to "lz4" and keep the default `linger.ms`.
- B. Set `acks` to "all" and increase `request.timeout.ms` to 30,000.
- C. Set `max.in.flight.requests.per.connection` to 5 and enable idempotence.
- D. Set `batch.size` to 16KB and `linger.ms` to 5ms.
- E. Set `batch.size` to 16KB and `linger.ms` to 0.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

In a latency‑sensitive scenario with small payloads, the producer should avoid any unnecessary wait. Setting `linger.ms` to 0 forces immediate sends, which removes the batching delay that would otherwise add up to `linger.ms` milliseconds per record. While larger batch sizes can improve throughput, they are irrelevant when the linger time is zero. The other options either introduce deliberate delays (linger 5 ms), add CPU overhead (compression), increase replication confirmation time (acks "all"), or alter safety semantics without affecting latency (idempotence + in‑flight). Therefore, the correct choice is option 1. For reference, see the Kafka Producer Configuration docs at https://kafka.apache.org/documentation/#producerconfigs and the Confluent Producer guide https://docs.confluent.io/platform/current/clients/producer.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "linger.ms"/"batch.size" (pp. 59-60)

**Detailed explanation of each option:**

1. ❌ **A. Set `compression.type` to "lz4" and keep the default `linger.ms`.**  
   **Incorrect**. Compression reduces network payload but adds CPU overhead and is ineffective for very small messages. It does not directly lower round‑trip latency and can even increase it if the producer spends time compressing.

2. ❌ **B. Set `acks` to "all" and increase `request.timeout.ms` to 30,000.**  
   **Incorrect**. Acks set to "all" requires confirmation from all in‑sync replicas, adding round‑trip delays. Increasing `request.timeout.ms` only enlarges the time the producer will wait for a response, further increasing latency.

3. ❌ **C. Set `max.in.flight.requests.per.connection` to 5 and enable idempotence.**  
   **Incorrect**. This configuration improves safety by preventing duplicate messages during retries, but it does not directly influence the time a single record spends in the producer before being sent. It can actually limit throughput if retries are frequent.

4. ❌ **D. Set `batch.size` to 16KB and `linger.ms` to 5ms.**  
   **Incorrect**. A 5 ms linger introduces a deliberate pause to accumulate records before sending, which actually adds up to 5 ms of latency per message. While this can improve throughput, it is not optimal for latency‑sensitive workloads.

5. ✅ **E. Set `batch.size` to 16KB and `linger.ms` to 0.**  
   **Correct**. Setting `linger.ms` to 0 tells the producer to send a record immediately after it is produced, eliminating the wait that would otherwise allow the batch to fill. This reduces latency for every record, which is critical for small messages. The larger `batch.size` is irrelevant when linger is 0 because the producer will not wait to accumulate messages. Safe delivery is preserved as long as other idempotence or acks settings remain unchanged.

</details>

## Question 48 (Reliable Data Delivery):
Which of the following statements correctly describe Kafka’s data replication behavior and configuration? (Select all that apply.)

- A. Increasing replication factor reduces the write latency because writes are acknowledged by fewer replicas.
- B. The replication factor can be increased after topic creation by using the `kafka-topics.sh` tool with the `--alter` command.
- C. Disabling `unclean.leader.election.enable` can prevent a topic from having a leader if all in‑sync replicas are down.
- D. If a broker hosting the leader replica fails, Kafka automatically elects a new leader from the set of in‑sync replicas, preserving exactly‑once semantics for producers.
- E. Kafka replicates data to all brokers listed in the `broker.id` property, regardless of their availability.
- F. Setting `min.insync.replicas` to a value greater than 1 guarantees that all replicas will be up-to-date before a producer commit.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

CORRECTION: B is false and the question is "select 2". `kafka-topics.sh --alter` can only change the partition count (and configs in older versions), it cannot change the replication factor. To raise the replication factor you must run `kafka-reassign-partitions.sh` with a reassignment JSON that lists additional replicas. Original text follows (its claim about `--alter` is wrong).

Kafka guarantees durability by replicating each partition’s log to multiple brokers as defined by the replication factor. The `min.insync.replicas` setting controls how many replicas must acknowledge a write before it is considered successful, while `unclean.leader.election.enable` determines whether a leader can be elected from an out‑of‑sync replica when all ISR members fail. Leader election always selects from the ISR, preserving data integrity and enabling producers that use idempotence or transactions to maintain exactly‑once semantics. Topic replication factor can be adjusted post‑creation only via partition reassignment (`kafka-reassign-partitions.sh`), not `kafka-topics.sh --alter`, and increasing it increases write latency, not decreases it. Understanding these settings is essential for designing fault‑tolerant Kafka deployments.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-142) and Ch. 7 "Replication" (pp. 163-168)

**Detailed explanation of each option:**

1. ❌ **A. Increasing replication factor reduces the write latency because writes are acknowledged by fewer replicas.**  
   **Incorrect**. A higher replication factor means writes must be replicated to more brokers, which typically increases acknowledgment latency.

2. ❌ **B. The replication factor can be increased after topic creation by using the `kafka-topics.sh` tool with the `--alter` command.**  
   **Incorrect**. `--alter` cannot change the replication factor, use `kafka-reassign-partitions.sh` with a custom reassignment plan that adds replicas (the factor cannot exceed the broker count).

3. ✅ **C. Disabling `unclean.leader.election.enable` can prevent a topic from having a leader if all in‑sync replicas are down.**  
   **Correct**. When `unclean.leader.election.enable` is set to false, Kafka will not elect a leader from a replica that is not in the ISR, meaning the partition can become leaderless if the ISR is empty.

4. ✅ **D. If a broker hosting the leader replica fails, Kafka automatically elects a new leader from the set of in‑sync replicas, preserving exactly‑once semantics for producers.**  
   **Correct**. Leader election is performed from the ISR, ensuring that no committed data is lost. Producers with idempotence or transactional settings can continue to achieve exactly‑once semantics because no records are replayed.

5. ❌ **E. Kafka replicates data to all brokers listed in the `broker.id` property, regardless of their availability.**  
   **Incorrect**. Replication targets are the brokers that belong to the cluster’s ISR. If a broker is down or not in the cluster, it will not receive data.

6. ❌ **F. Setting `min.insync.replicas` to a value greater than 1 guarantees that all replicas will be up-to-date before a producer commit.**  
   **Incorrect**. `min.insync.replicas` only requires that at least that many in‑sync replicas (ISR) acknowledge the write. Replicas that are not in ISR may be out of date, so the write can succeed even if not all replicas are fully up‑to‑date.

</details>

## Question 49 (Kafka Core Concepts):
Which of the following statements about Kafka topic partitions and offsets are true?

- A. Offsets can be rolled back by consuming from a lower offset value.
- B. Offsets are global across all partitions of a topic and are unique for each record.
- C. A record's key is hashed to determine its partition, ensuring that records with the same key are written to the same partition.
- D. A consumer's committed offset is stored in ZooKeeper and is shared across all consumer groups.
- E. The maximum number of partitions per topic is limited by the broker's configured `num.partitions` setting.
- F. When a new partition is added to a topic, existing consumers automatically start consuming from the new partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

Kafka topics are logical namespaces split into partitions, each with its own ordered, immutable log. Offsets are indices within a partition, starting at 0, and are the consumer’s position marker. Consumers store committed offsets in the internal topic __consumer_offsets, providing isolation per consumer group. The default partitioner hashes a record’s key, ensuring records with the same key are routed to the same partition and preserving order for those keys. If a consumer needs to reprocess data, it can seek to a lower offset, effectively rolling back. Misconceptions often arise around global offsets, ZooKeeper usage, and automatic consumption of new partitions, understanding these nuances is essential for correct design and troubleshooting.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6)

**Detailed explanation of each option:**

1. ✅ **A. Offsets can be rolled back by consuming from a lower offset value.**  
   **Correct**. A consumer can seek to an earlier offset (e.g., using seek() or resetting offsets) to reprocess messages.

2. ❌ **B. Offsets are global across all partitions of a topic and are unique for each record.**  
   **Incorrect**. Offsets are maintained per partition, the same offset number can appear in many partitions.

3. ✅ **C. A record's key is hashed to determine its partition, ensuring that records with the same key are written to the same partition.**  
   **Correct**. The default partitioner uses a key hash to consistently map the same key to a specific partition, guaranteeing intra-key ordering.

4. ❌ **D. A consumer's committed offset is stored in ZooKeeper and is shared across all consumer groups.**  
   **Incorrect**. Since Kafka 0.10, committed offsets are stored in the internal topic __consumer_offsets, not ZooKeeper, and each consumer group has its own offset state.

5. ❌ **E. The maximum number of partitions per topic is limited by the broker's configured `num.partitions` setting.**  
   **Incorrect**. `num.partitions` is only a default value, topics can have more partitions, though large numbers can impact broker performance.

6. ❌ **F. When a new partition is added to a topic, existing consumers automatically start consuming from the new partition.**  
   **Incorrect**. Adding partitions triggers a rebalance, consumers may or may not receive assignments to the new partitions depending on group dynamics.

</details>

## Question 50 (Programming & Serialization):
Which statements about message keying in Apache Kafka are correct? (Select all that apply.)

- A. The key can be omitted, Kafka will automatically generate a key based on timestamp.
- B. Including a key ensures that messages with the same key are stored in the same partition.
- C. The key must be non‑null for any partitioned topic.
- D. The key is used by the partitioner to assign records to a partition.
- E. The key should be unique across the entire topic to avoid duplicates.
- F. When using schema registry, the key schema must be registered separately from the value schema.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

In Kafka, a message key is optional but critical for controlling partitioning and ordering. The partitioner hashes the key, so records with identical keys always land in the same partition, preserving their relative order. Keys can be null, Kafka treats them the same for partitioning, though compaction topics ignore null‑key records. Schema Registry treats key and value schemas separately, enabling distinct schemas for each. Common misconceptions include assuming keys must be unique or that Kafka auto‑generates keys. Understanding these nuances is essential for designing efficient, ordered streaming applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Partitions" (pp. 68-70)

**Detailed explanation of each option:**

1. ❌ **A. The key can be omitted, Kafka will automatically generate a key based on timestamp.**  
   **Incorrect**. If no key is provided, Kafka will use the default partitioner that hashes a null key, which is effectively random across partitions.

2. ✅ **B. Including a key ensures that messages with the same key are stored in the same partition.**  
   **Correct**. This guarantees ordering for those keys within that partition.

3. ❌ **C. The key must be non‑null for any partitioned topic.**  
   **Incorrect**. Kafka allows null keys, they are treated the same as any other key for partitioning but are ignored by the compaction process. Thus this statement is false.

4. ✅ **D. The key is used by the partitioner to assign records to a partition.**  
   **Correct**. True. The default partitioner hashes the key to determine the partition, ensuring all records with the same key go to the same partition.

5. ❌ **E. The key should be unique across the entire topic to avoid duplicates.**  
   **Incorrect**. False. A key is only required to group records within a partition, uniqueness is not enforced and is unnecessary for ordering.

6. ✅ **F. When using schema registry, the key schema must be registered separately from the value schema.**  
   **Correct**. True. Key and value schemas are registered independently, allowing different schema versions for each.

</details>

## Question 51 (Programming & Serialization):
Schema Registry is configured with BACKWARD
compatibility (default). A producer a new field named **age**
WITHOUT a default value. What happens?

- A. Consumer will read null for the new field.
- B. Producer will only add the new field for messages after a topic reconfiguration.
- C. Consumer will ignore the new field and process the record normally.
- D. Consumer will fail with an Avro serialization error because the missing field cannot be found.
- E. Schema Registry will reject the registration of the new schema due to a compatibility violation.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

CORRECTION: adding a field WITHOUT a default is NOT backward compatible (a new-schema reader cannot fill the field when reading old records), so under the registry's default BACKWARD compatibility the registration is rejected (HTTP 409 / incompatible schema) and no records with the new schema are ever produced. Only if the subject were set to FORWARD/FULL_TRANSITIVE-style forward compatibility (or NONE) would old consumers simply ignore the new field (the former option C). Original text follows (its compatibility claim is wrong).

When a producer adds a new field without a default value, the change is considered backward compatible in Avro: older consumers can still read records written with the new schema because they simply ignore unknown fields. Schema Registry, configured with the default backward compatibility setting, will accept the new schema. Consumers that use the original schema will continue to function without errors, processing all known fields and disregarding the new one. This behavior exemplifies Avro’s forward/backward compatibility model and is documented in Confluent’s Schema Registry compatibility guide (https://docs.confluent.io/platform/current/schema-registry/compatibility.html).

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. Consumer will read null for the new field.**  
   **Incorrect**. The new field is not present in the consumer’s reader schema, so it is simply ignored. The consumer never sees a null value for it.

2. ❌ **B. Producer will only add the new field for messages after a topic reconfiguration.**  
   **Incorrect**. The schema change is applied at the producer level, all new messages after the schema update contain the field immediately, no topic reconfiguration needed.

3. ❌ **C. Consumer will ignore the new field and process the record normally.**  
   **Incorrect**. This would only hold if the schema had been registered under a forward-compatible (or NONE) setting, with the default BACKWARD setting the schema is rejected before any record is written.

4. ❌ **D. Consumer will fail with an Avro serialization error because the missing field cannot be found.**  
   **Incorrect**. Avro readers are designed to ignore unknown fields, the absence of a default does not cause a deserialization failure for older readers.

5. ✅ **E. Schema Registry will reject the registration of the new schema due to a compatibility violation.**  
   **Correct**. The default compatibility is BACKWARD, which only allows adding fields that have a default (or deleting fields). Adding `age` without a default violates it, so registration fails.

</details>

## Question 52 (Stream Processing):
A Kafka Streams application reads from topic **orders**, groups by order category, aggregates the total
amount per category, and writes the results to topic **category_totals**. The application is configured
with **processing.guarantee=exactly_once_v2** and uses the default state store. Which of the following
statements is FALSE?
A Kafka Streams application reads from topic **orders**,
groups by order category (changing the key),
aggregates the total amount per category, and writes
the results to topic **category_totals**. The application
is configured with ``processing.guarantee=exactly_once_v2``,
``application.id=orders-processor``, and uses the default
RocksDB state store named **category-store**.
Which of the following statements is FALSE?

- A. The aggregation can be replayed from the beginning without affecting downstream consumers that use isolation.level=read_committed.
- B. The output topic **category_totals** will be idempotently written to avoid duplicates.
- C. The application will write to a changelog topic named **orders-agg-<store>** to maintain state.
- D. The offsets of the input topic will be committed only after the aggregation result is published to the output topic.
- E. The application will create a repartition topic named **orders-repartition** to ensure keys are aligned for the groupBy.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Exactly‑once guarantees in Kafka Streams rely on a combination of idempotent producers, transactional writes, and state changelog topics. When replaying a stream, the application recomputes state and emits new aggregate results. Even though the producer is idempotent, downstream consumers that do not handle idempotence can still observe duplicate or out‑of‑order events, making the statement that replaying has no downstream effect false. The other statements correctly describe changelog topics, idempotent writes, repartitioning for groupBy, and transactional offset commits. Understanding these nuances is essential for designing robust stream processing applications that meet exactly‑once requirements.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. The aggregation can be replayed from the beginning without affecting downstream consumers.**  
   **Correct**. Downstream consumers configured with isolation.level=read_committed only see committed transactions. Aborted transactions from failed replays are never visible. Statement is TRUE → not the FALSE answer.

2. ❌ **B. The output topic **category_totals** will be idempotently written to avoid duplicates.**  
   **Incorrect**. With **processing.guarantee=exactly_once_v2**, the Streams library uses an idempotent producer to write to output topics, ensuring no duplicate records are produced even on retries.

3. ✅ **C. The application will write to a changelog topic named **orders-agg-<store>** to maintain state.**  
   **Incorrect**.  Changelog topic naming convention: <application.id>-<store-name>-changelog
   "orders-agg-<store>" is WRONG!
   Correct name for this application: orders-processor-category-store-changelog
   Source: kafka.apache.org/43/streams/  architecture/#streams_architecture_state

4. ❌ **D. The offsets of the input topic will be committed only after the aggregation result is published to the output topic.**  
   **Incorrect**. Exactly‑once semantics commit input offsets only after the corresponding output record has been successfully written, guaranteeing atomicity.

5. ❌ **E. The application will create a repartition topic named **orders-repartition** to ensure keys are aligned for the groupBy.**  
   **Incorrect**. The **groupBy** operation triggers an implicit repartition. Kafka Streams creates a repartition topic (orders-repartition) to redistribute records by key for the aggregation.

</details>

## Question 53 (Programming & Serialization):
When a producer uses the Confluent Avro Serializer with Schema Registry, which of the following best describes how the schema is handled during serialization?

- A. The serializer registers the schema once, receives a unique numeric ID from Schema Registry, and writes that ID followed by the Avro binary representation of the record.
- B. The producer does not need the Schema Registry, the consumer infers the schema from the Avro binary payload alone.
- C. The full Avro schema is embedded in every record and the Schema Registry is only queried for validation.
- D. For every record, the serializer fetches the schema from Schema Registry and embeds the entire schema in the message header.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Confluent Avro Serializer is designed to keep Kafka message size minimal while enabling schema evolution. It caches schema IDs locally, upon first use, it registers the schema with Schema Registry, receives a numeric ID, and prefixes the Avro binary payload with that ID. Subsequent records use the cached ID, eliminating round‑trips. This approach enables backward/forward compatibility checks in the registry while keeping payloads lightweight. Understanding this flow is essential for configuring producers and consumers correctly in a Confluent Platform deployment.

Source: Confluent Schema Registry docs - "Wire format" (magic byte 0 + 4-byte schema ID), Kafka: The Definitive Guide 2nd ed. Ch. 3 "Using Avro Records with Kafka" (pp. 65-68)

**Detailed explanation of each option:**

1. ✅ **A. The serializer registers the schema once, receives a unique numeric ID from Schema Registry, and writes that ID followed by the Avro binary representation of the record.**  
   **Correct**. The Confluent Avro Serializer first checks its local cache for the schema. If not found, it registers the schema with the Registry, obtains an ID, caches it, and then writes the 4-byte ID prefix followed by the Avro-encoded record.

2. ❌ **B. The producer does not need the Schema Registry, the consumer infers the schema from the Avro binary payload alone.**  
   **Incorrect**. Without the registry, the consumer cannot map the binary data to the appropriate schema version, leading to deserialization errors.

3. ❌ **C. The full Avro schema is embedded in every record and the Schema Registry is only queried for validation.**  
   **Incorrect**. While the schema can be embedded, the Confluent Avro Serializer does not send the full schema with each message, it relies on a numeric ID instead, which keeps payload size small.

4. ❌ **D. For every record, the serializer fetches the schema from Schema Registry and embeds the entire schema in the message header.**  
   **Incorrect**. Fetching the schema for every message would be inefficient, the serializer caches the schema ID after the first lookup and does not embed the full schema in the header.

</details>

## Question 54 (Application Testing):
Which of the following approaches are valid for unit‑testing Kafka client applications (producers, consumers, or stream processors) without requiring a live, external Kafka cluster?

- A. Use the EmbeddedKafka cluster provided by the kafka-clients library to spin up an in‑memory broker during tests.
- B. Instantiate a MockProducer and send messages to a real Kafka cluster to verify serialization logic.
- C. Leverage Kafka Streams TopologyTestDriver to test stream processing logic without a running cluster.
- D. Employ the Kafka TestUtils’s produceMessages and consumeMessages helpers that use a real external broker.
- E. Rely solely on Confluent Cloud’s TestClient API to validate message serialization.
- F. Use the Kafka Connect Test harness to unit test source/sink connectors as client applications.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

Unit‑testing Kafka clients relies on in‑process or mocked components to keep tests fast and deterministic. The EmbeddedKafka cluster or TestKafkaServer spins up a local broker, enabling real network interactions. The TopologyTestDriver runs stream topologies without a broker, ideal for pure logic tests. The Connect test harness allows connectors—also Kafka clients—to be validated in isolation. MockProducer/MockConsumer are useful for checking send/receive logic but do not simulate broker communication, and real broker helpers or nonexistent TestClient APIs are unsuitable for unit tests. These patterns align with Confluent’s recommended practices for testing client code.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Testing" (pp. 131-133) and Ch. 14 "Testing a Topology" (pp. 411-412)

**Detailed explanation of each option:**

1. ✅ **A. Use the EmbeddedKafka cluster provided by the kafka-clients library to spin up an in‑memory broker during tests.**  
   **Correct**. The EmbeddedKafka (or TestKafkaServer) allows tests to run a lightweight broker locally, enabling end‑to‑end producer/consumer interactions while keeping the test isolated.

2. ❌ **B. Instantiate a MockProducer and send messages to a real Kafka cluster to verify serialization logic.**  
   **Incorrect**. The MockProducer is a stand‑in that records sent records but does not communicate with an actual broker, it cannot be used to validate message delivery to a real cluster.

3. ✅ **C. Leverage Kafka Streams TopologyTestDriver to test stream processing logic without a running cluster.**  
   **Correct**. The TopologyTestDriver runs the stream topology in process, letting developers send and receive records directly, which is ideal for unit tests of stream processors.

4. ❌ **D. Employ the Kafka TestUtils’s produceMessages and consumeMessages helpers that use a real external broker.**  
   **Incorrect**. These helpers require a live broker, making them unsuitable for isolated unit tests, they are more appropriate for integration tests.

5. ❌ **E. Rely solely on Confluent Cloud’s TestClient API to validate message serialization.**  
   **Incorrect**. Confluent Cloud does not expose a dedicated TestClient API for unit testing, developers must use local mocks or embedded clusters.

6. ✅ **F. Use the Kafka Connect Test harness to unit test source/sink connectors as client applications.**  
   **Correct**. The Connect test harness provides an in‑process Connect framework that can be used to validate connector logic without external dependencies.

</details>

## Question 55 (Stream Processing):
You have two Kafka topics: `orders` (key = `order_id`) and `payments` (key = `payment_id`). In a Kafka Streams application you need to correlate each payment with its originating order. Which data‑modeling strategy will allow the join to execute efficiently without repartitioning the data stream?

- A. Use a time‑windowed join and let Kafka Streams automatically handle key differences.
- B. Create a repartition topic keyed by `order_id` for the payments stream and join on that.
- C. Publish payments with the key set to `order_id` (i.e., re‑key the payment records before producing).
- D. Add an `order_id` field to the payment value and perform a stream‑stream join with a tumbling window.
- E. Use a global table keyed by `order_id` and join the payments stream to it.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka Streams, stream‑stream joins require that both streams share the same key, otherwise, Kafka Streams performs an implicit repartition that incurs network shuffling and latency. By re‑keying the payments stream to use the `order_id` key before it reaches the Streams application, you enable a direct partition‑aligned join with zero repartitioning. This design choice reduces resource consumption and simplifies the topology. While repartition topics or adding fields are technically feasible, they add complexity and performance costs. Understanding key design is essential for efficient stream processing and is a core concept in Confluent’s Kafka Streams data‑modeling best practices.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Stream-Table Join"/"Streaming Join" (pp. 396-399)

**Detailed explanation of each option:**

1. ❌ **A. Use a time‑windowed join and let Kafka Streams automatically handle key differences.**  
   **Incorrect**. Kafka Streams cannot automatically reconcile different keys, the streams still need the same key to join efficiently.

2. ❌ **B. Create a repartition topic keyed by `order_id` for the payments stream and join on that.**  
   **Incorrect**. Possible but not the most efficient approach. Repartitioning introduces an extra topic and shuffle, which increases latency and overhead compared to simply re‑keying at production time.

3. ✅ **C. Publish payments with the key set to `order_id` (i.e., re‑key the payment records before producing).**  
   **Correct**. For a stream‑stream join, the join key must be the topic key. By setting the payment key to `order_id`, both streams share the same key and no repartitioning is required, resulting in a single partitioned join.

4. ❌ **D. Add an `order_id` field to the payment value and perform a stream‑stream join with a tumbling window.**  
   **Incorrect**. The join key is still `payment_id`, adding a field does not change the key and Kafka Streams will automatically trigger a repartition, causing unnecessary shuffling.

5. ❌ **E. Use a global table keyed by `order_id` and join the payments stream to it.**  
   **Incorrect**. A global table is used for a stream‑table join, not a stream‑stream join, and would still require repartitioning of the payments stream if its key is not `order_id`.

</details>

## 🚫 Question 56 (Kafka Fundamentals):
In Confluent Cloud, which of the following statements correctly describes the behavior of encryption at rest for data stored in Kafka topics?

- A. Encryption at rest is automatically enabled for all resources and cannot be turned off by the user.
- B. Encryption at rest is optional and must be enabled through the Confluent Cloud UI before any data is ingested.
- C. Users can disable encryption at rest by setting the topic‑level config `encryption.type=none`.
- D. Clients must implement client‑side encryption, the broker does not provide any encryption at rest.
- E. Confluent Cloud only provides encryption in transit, encryption at rest must be handled by the customer.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Confluent Cloud offers end‑to‑end security, including automatic encryption at rest via the underlying cloud provider’s Key Management Service (KMS). This encryption is enabled by default and cannot be disabled, ensuring data remains protected even if the storage infrastructure is compromised. Unlike some self‑hosted setups where encryption at rest requires explicit configuration, Confluent Cloud abstracts these details, allowing developers to focus on application logic rather than low‑level security plumbing. This design eliminates common misconceptions that clients must manage server‑side encryption themselves and reinforces the platform’s commitment to data confidentiality. References: - Confluent Cloud Security Overview: https://docs.confluent.io/cloud/current/security/index.html - Confluent Platform Encryption Docs: https://docs.confluent.io/platform/current/security/encryption.html

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 11 "Encryption" / "End-to-End Encryption" (pp. 289-291) — NOTE: Confluent Cloud encryption-at-rest verified against Confluent Cloud docs (out of exam scope).

**Detailed explanation of each option:**

1. ✅ **A. Encryption at rest is automatically enabled for all resources and cannot be turned off by the user.**  
   **Correct**. Confluent Cloud encrypts all persistent data at rest using cloud provider KMS by default. The feature is part of the service offering and is not configurable or disableable by users. This is the correct statement.

2. ❌ **B. Encryption at rest is optional and must be enabled through the Confluent Cloud UI before any data is ingested.**  
   **Incorrect**. Encryption at rest is not optional, it is enabled by default for all services and cannot be switched off, so this statement is incorrect.

3. ❌ **C. Users can disable encryption at rest by setting the topic‑level config `encryption.type=none`.**  
   **Incorrect**. There is no `encryption.type` topic configuration in Confluent Cloud. Attempts to set such a key will be ignored or cause an error, making this statement incorrect.

4. ❌ **D. Clients must implement client‑side encryption, the broker does not provide any encryption at rest.**  
   **Incorrect**. While client‑side encryption is possible, the broker automatically encrypts data at rest. The broker itself provides encryption, making this statement inaccurate.

5. ❌ **E. Confluent Cloud only provides encryption in transit, encryption at rest must be handled by the customer.**  
   **Incorrect**. The platform handles both in‑transit and at‑rest encryption. Customers do not need to provide their own encryption for data stored in topics, so this statement is false.

</details>

## Question 57 (Application Development):
You are developing a Kafka producer that must connect to a Confluent Cloud cluster configured with SASL authentication over TLS (SASL_SSL) using SCRAM-SHA-512 credentials. Which client configuration property value is required to enable both encryption and authentication?

- A. security.protocol=SASL_SSL
- B. security.protocol=SASL_PLAINTEXT
- C. security.protocol=SSL
- D. security.protocol=PLAINTEXT

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In a Confluent Cloud cluster that uses SASL authentication over TLS, the client must configure the security.protocol property to SASL_SSL. This value enables both the encryption layer (TLS) and the SASL authentication mechanism (e.g., SCRAM-SHA-512). Using SSL alone omits authentication, SASL_PLAINTEXT omits encryption, and PLAINTEXT omits both, all of which would cause the connection to fail. The correct configuration aligns with Confluent's security guidelines, ensuring data confidentiality and identity verification. For more details, see the Confluent Kafka Clients documentation on SSL and SASL configuration.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ✅ **A. security.protocol=SASL_SSL**  
   **Correct**. SASL_SSL combines SASL authentication (e.g., SCRAM) with TLS encryption, matching the cluster's security requirements. This is the correct setting.

2. ❌ **B. security.protocol=SASL_PLAINTEXT**  
   **Incorrect**. SASL_PLAINTEXT enables SASL authentication but leaves the channel unencrypted, which is not permitted for a Confluent Cloud cluster that requires TLS.

3. ❌ **C. security.protocol=SSL**  
   **Incorrect**. SSL provides encryption but does not enable SASL authentication. The client would establish a secure channel but would fail to authenticate.

4. ❌ **D. security.protocol=PLAINTEXT**  
   **Incorrect**. PLAINTEXT provides no encryption or authentication, so the client would be rejected by the secured cluster.

</details>

## Question 58 (Kafka Core Concepts):
Which of the following statements about Kafka message headers are correct? (Select all that apply.)

- A. Header keys must be unique per message, duplicate keys are allowed but only the last value is kept.
- B. Header names cannot contain null bytes and are case-sensitive.
- C. Header values can be compressed using GZIP to reduce record size.
- D. Headers can store arbitrary binary data and are transmitted with the record to the broker.
- E. The total size of all headers is limited to 1 MB, independent of the record size.
- F. Header values are persisted in the Kafka broker as part of the record metadata and are available to consumers regardless of client version.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

Kafka message headers are a lightweight, map‑based mechanism that transports arbitrary binary metadata alongside the record payload. They are stored as part of the record on the broker and can be accessed by any consumer supporting the header API, making them useful for cross‑cutting concerns such as tracing or routing. Header keys are non-null strings and are case‑sensitive (duplicates are allowed), while values are raw byte arrays. Header data is included in the overall message size limit governed by broker configuration (e.g., max.message.bytes). Unlike record payload compression, headers are not individually compressed. Understanding these nuances ensures efficient use of headers in producer and consumer code and prevents common pitfalls such as duplicate keys or misinterpreting size limits.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Headers" (p. 71)

**Detailed explanation of each option:**

1. ❌ **A. Header keys must be unique per message, duplicate keys are allowed but only the last value is kept.**  
   **Incorrect**. Kafka headers are an ordered list of (key, value) pairs, duplicate keys ARE allowed and ALL values are kept (`lastHeader(key)` returns the last, `headers(key)` all of them). Keys are not required to be unique and nothing is dropped.

2. ✅ **B. Header names cannot contain null bytes and are case-sensitive.**  
   **Correct**. Header keys are strings, the Java implementation forbids null characters, and key comparison is case-sensitive.

3. ❌ **C. Header values can be compressed using GZIP to reduce record size.**  
   **Incorrect**. Compression applies to the entire record payload, not to individual headers. Header values are transmitted as raw bytes.

4. ✅ **D. Headers can store arbitrary binary data and are transmitted with the record to the broker.**  
   **Correct**. In Kafka, a header consists of a string key and a byte array value, allowing any binary payload. Headers travel with the record and are persisted by the broker.

5. ❌ **E. The total size of all headers is limited to 1 MB, independent of the record size.**  
   **Incorrect**. The broker imposes a single maximum message size (default 1 MB) that includes key, value, headers, and any compression overhead.

6. ✅ **F. Header values are persisted in the Kafka broker as part of the record metadata and are available to consumers regardless of client version.**  
   **Correct**. Header data is stored with the record and can be retrieved by any consumer that supports the header API. Older clients simply ignore headers but the data remains intact.

</details>

## Question 59 (Programming & Serialization):
You have an Avro schema registered under the subject `UserRecord` in Confluent Schema Registry. The current schema is:
```
{
  "type": "record",
  "name": "UserRecord",
  "fields": [
    {
      "name": "id",
      "type": "int"
    },
    {
      "name": "name",
      "type": "string"
    }
  ]
} 

```
The registry is configured with the default **BACKWARD** compatibility setting. Which of the following schema evolution changes would **break existing consumers** that still use the current schema?

- A. Remove the field "id".
- B. Add a new field "email" of type string with a default value of an empty string.
- C. Change the type of field "name" from string to int.
- D. Add a new field "email" of type string without a default value.
- E. Reorder the fields so that "name" comes before "id".

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

CORRECTION: the question asks what breaks EXISTING consumers that still use the current schema, i.e. old readers reading data written with the new schema. Both A and C do: removing the required field "id" (no default) leaves old readers without a value for it, and changing "name" to int is a type mismatch. B, D and E do not break old readers (they ignore the extra field, field order is irrelevant). Note that BACKWARD compatibility protects NEW readers of OLD data, so the registry would accept A (and reject C and D). The original explanation below wrongly says removal is safe for existing consumers and that D is safe under BACKWARD (D is rejected by BACKWARD, though it does not break old consumers). Original text follows.

Under Confluent Schema Registry’s default BACKWARD compatibility, a new schema must be readable by older consumers. Adding new fields (with or without defaults), removing fields, or reordering fields all preserve compatibility because unknown fields are ignored or defaults provide values. The only change that violates this rule is altering a field’s type – here, changing "name" from string to int. Older consumers still expect a string and will fail to deserialize the new int value, breaking backward compatibility. For detailed rules see Confluent’s compatibility guide (https://docs.confluent.io/platform/current/schema-registry/compatibility.html) and Avro’s schema evolution spec (https://avro.apache.org/docs/current/spec.html).

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ✅ **A. Remove the field "id".**  
   **Correct**. Allowed by BACKWARD compatibility, but it breaks existing consumers: new records no longer contain `id`, and the old reader schema has no default for it, so deserialization fails.

2. ❌ **B. Add a new field "email" of type string with a default value of an empty string.**  
   **Incorrect**. Also safe. Adding a field with a default ensures that if a new consumer reads older data that lacks the field, it receives the default value, while old consumers continue to ignore it.

3. ✅ **C. Change the type of field "name" from string to int.**  
   **Correct**. This breaks BACKWARD compatibility. Old consumers expect a string, a producer that writes an int will cause a schema‑validation error or deserialization failure on the consumer side.

4. ❌ **D. Add a new field "email" of type string without a default value.**  
   **Incorrect**. Does not break existing consumers: old readers ignore the unknown field. (Under BACKWARD compatibility the registry would still reject it, since a new reader could not read old data lacking the field.)

5. ❌ **E. Reorder the fields so that "name" comes before "id".**  
   **Incorrect**. Safe. Avro matches fields by name, not order, so reordering does not affect compatibility.

</details>

## 🚫 Question 60 (Application Observability):
You have just deployed a Kafka Streams application on Kubernetes and need to monitor its processing latency and throughput. Which option describes the correct approach to expose these metrics to Prometheus and subsequently visualize them with Grafana?

- A. Configure the Streams application to send metrics directly to Prometheus via a custom exporter.
- B. Enable the Confluent Control Center monitoring, which automatically exposes metrics to Grafana dashboards.
- C. Configure the application to expose JMX metrics, deploy the JMX exporter as a sidecar, and use Prometheus to scrape the metrics.
- D. Use the Kafka Connect JMX metrics exporter to collect stream metrics.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

For Kafka Streams, the recommended way to monitor processing latency and throughput in a Prometheus/Grafana stack is to expose JMX metrics, convert them to Prometheus format using the JMX Exporter, and scrape them with Prometheus. This approach leverages built‑in JMX metrics, requires minimal configuration, and integrates seamlessly with existing monitoring tools. Alternative options either target the wrong component (Kafka Connect), lack native support (direct Prometheus push), or do not provide Prometheus endpoints (Control Center). Understanding the distinction between JMX, Prometheus, and Control Center is essential for building effective observability for Kafka applications.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 13 "Monitoring Kafka" (pp. 339-378) — NOTE: JMX-exporter sidecar + Prometheus/Grafana pattern verified against Confluent monitoring docs.

**Detailed explanation of each option:**

1. ❌ **A. Configure the Streams application to send metrics directly to Prometheus via a custom exporter.**  
   **Incorrect**. Kafka Streams does not provide a built-in mechanism for pushing metrics to Prometheus. A custom exporter would need to be implemented and integrated, which is unnecessary because the JMX exporter handles this task efficiently. Without a custom implementation, the application will not expose Prometheus-compatible metrics. References: https://kafka.apache.org/documentation/streams/streams-monitoring.html

2. ❌ **B. Enable the Confluent Control Center monitoring, which automatically exposes metrics to Grafana dashboards.**  
   **Incorrect**. Confluent Control Center collects and stores metrics from the cluster, but it does not expose those metrics as Prometheus endpoints. Grafana dashboards in Control Center are internal, they cannot be used directly by an external Prometheus instance. Therefore, this option does not provide the required Prometheus-compatible metrics. References: https://docs.confluent.io/platform/current/control-center/index.html

3. ✅ **C. Configure the application to expose JMX metrics, deploy the JMX exporter as a sidecar, and use Prometheus to scrape the metrics.**  
   **Correct**. Kafka Streams automatically publishes JMX metrics for latency, throughput, and other performance indicators. The Prometheus JMX Exporter converts these JMX metrics into Prometheus exposition format. By running the exporter as a sidecar or inside the same pod, Prometheus can scrape the metrics endpoint, and Grafana can use Prometheus as a datasource to build dashboards. This is the standard, supported method for monitoring Streams metrics with Prometheus. References: https://kafka.apache.org/documentation/streams/streams-monitoring.html, https://github.com/prometheus/jmx_exporter

4. ❌ **D. Use the Kafka Connect JMX metrics exporter to collect stream metrics.**  
   **Incorrect**. The Kafka Connect JMX exporter is designed to scrape JMX metrics from Connect workers and connectors, not from Kafka Streams applications. It cannot expose Streams-specific metrics, so this approach would not provide the required latency or throughput information. References: https://docs.confluent.io/platform/current/connect/index.html

</details>
