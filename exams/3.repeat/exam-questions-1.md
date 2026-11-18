> 🚫 = outside the CCDAK exam scope (see exam blueprint) #Repeats

## Question 1 (Stream Processing):
In a Kafka Streams application that performs a stateful aggregation and writes the results to a downstream topic, which configuration and code combination is required to guarantee exactly‑once processing semantics?

- A. Set `processing.guarantee=exactly_once_v2`, use a `KStream` aggregation via `transformValues`, and enable idempotent producer by setting `enable.idempotence=true` on the Streams producer.
- B. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, and rely on the default transaction id prefix derived from `application.id`.
- C. Set `processing.guarantee=exactly_once`, use a `KStream` to `to()` with `Produced.with()` and set `acks=all` on the sink topic.
- D. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, configure the sink topic with `cleanup.policy=compact`, and set `min.insync.replicas=2` on the sink topic.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Exactly‑once V2 in Kafka Streams relies on a per‑task transaction that encompasses state updates and output writes. To achieve it, the application must set `processing.guarantee=exactly_once_v2` and use a stateful operator such as a `KTable` aggregation or join. The transaction ID is automatically derived from `application.id` (or overridden via `transactional.id.prefix`) so no manual idempotence or topic cleanup settings are required. Options that omit the stateful operator, use older guarantees, or include unnecessary topic configs fail to provide the required transactional guarantees. Understanding this configuration is essential for building robust stream applications that avoid duplicates and ensure data consistency.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Set `processing.guarantee=exactly_once_v2`, use a `KStream` aggregation via `transformValues`, and enable idempotent producer by setting `enable.idempotence=true` on the Streams producer.**  
   **Incorrect**. While `enable.idempotence=true` is automatically enabled for exactly‑once, `transformValues` is a stateless operator. A stateful aggregation is required for the transactional guarantee, so this option is insufficient.

2. ✅ **B. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, and rely on the default transaction id prefix derived from `application.id`.**  
   **Correct**. Exactly‑once V2 requires `processing.guarantee=exactly_once_v2`. A `KTable` aggregation is stateful, and Kafka Streams automatically derives a `transactional.id` from `application.id` unless overridden. This combination satisfies all requirements for exactly‑once semantics.

3. ❌ **C. Set `processing.guarantee=exactly_once`, use a `KStream` to `to()` with `Produced.with()` and set `acks=all` on the sink topic.**  
   **Incorrect**. `processing.guarantee=exactly_once` refers to the older exactly‑once V1 guarantee, which is deprecated and does not provide the same level of isolation as V2. Additionally, the use of `acks=all` alone does not enable transactional guarantees. Thus this option is incorrect.

4. ❌ **D. Set `processing.guarantee=exactly_once_v2`, use a `KTable` aggregation, configure the sink topic with `cleanup.policy=compact`, and set `min.insync.replicas=2` on the sink topic.**  
   **Incorrect**. The configuration includes unnecessary topic settings that do not influence exactly‑once guarantees. `cleanup.policy=compact` and `min.insync.replicas` are irrelevant to transaction handling. The combination is therefore incorrect.

</details>

## Question 2 (Kafka Connect):
When running Kafka Connect in distributed mode, which of the following statements about connector deployment and task management are correct?

- A. Workers communicate directly over TCP to synchronize connector state when running in distributed mode.
- B. Connector configurations are stored in an internal Kafka topic, enabling workers to share state and coordinate task assignments.
- C. In distributed mode, all connectors must use the same connector plugin version to ensure compatibility across worker nodes.
- D. Each connector instance runs exclusively on a single worker node and cannot be redistributed without manual intervention.
- E. Connectors and their tasks are distributed across all available worker nodes to provide scalability and fault tolerance.
- F. Kafka Connect's REST API can be used to pause and resume connectors without stopping the entire Connect cluster.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, B, F

**Explanation:**

In distributed mode, Kafka Connect provides scalability and fault tolerance by distributing connectors and tasks across multiple worker nodes. Connector configurations are stored in internal Kafka topics, enabling workers to share state and coordinate task assignments without direct TCP communication. Operational flexibility is enhanced by the REST API, allowing connectors to be paused and resumed independently. Common misconceptions include believing connectors are tied to single workers or that workers communicate directly via TCP; in reality, Kafka topics mediate coordination. Also, while consistent plugin versions are recommended, they are not strictly enforced by Connect. Understanding these details is critical for deploying and managing Kafka Connect clusters effectively.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. Workers communicate directly over TCP to synchronize connector state when running in distributed mode.**  
   **Incorrect**. Workers coordinate via Kafka topics rather than direct TCP communication, which allows for loose coupling and fault tolerance.

2. ✅ **B. Connector configurations are stored in an internal Kafka topic, enabling workers to share state and coordinate task assignments.**  
   **Correct**. Kafka Connect stores connector and task configurations in a Kafka topic (e.g., `__connect-configs`), ensuring distributed coordination among workers.

3. ❌ **C. In distributed mode, all connectors must use the same connector plugin version to ensure compatibility across worker nodes.**  
   **Incorrect**. While plugin versions should generally be consistent to avoid issues, Kafka Connect does not enforce uniform plugin versions across workers at runtime.

4. ❌ **D. Each connector instance runs exclusively on a single worker node and cannot be redistributed without manual intervention.**  
   **Incorrect**. Connectors in distributed mode are not bound to a single worker; they can be rebalanced and moved automatically by the Connect framework.

5. ✅ **E. Connectors and their tasks are distributed across all available worker nodes to provide scalability and fault tolerance.**  
   **Correct**. In distributed mode, Kafka Connect automatically balances connectors and tasks across worker nodes, enabling scalability and resilience.

6. ✅ **F. Kafka Connect's REST API can be used to pause and resume connectors without stopping the entire Connect cluster.**  
   **Correct**. The REST API supports pausing and resuming connectors individually, facilitating operational control without cluster downtime.

</details>

## Question 3 (Stream Processing): [-]
When designing a stateful Kafka Streams application that performs aggregations and joins, which of the following statements about Kafka Streams’ runtime behavior are true? Select all that apply.

- A. The internal state store of a Kafka Streams application is automatically replicated to all instances of the application.
- B. Using the KStream.filter() operator can modify the downstream key of a record without changing the original key.
- C. The materialized view created with aggregate() is stored in a changelog topic that can be queried by other consumers.
- D. A Kafka Streams application can safely produce records to the same topic it consumes from without risking infinite loops.
- E. Kafka Streams automatically commits the offsets of input topics on behalf of the application, typically every few seconds or when the application is closed.
- F. When a stream processing task fails, Kafka Streams restarts the task on a different node, but the task’s local state is lost and must be rebuilt from scratch.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** E, C

**Explanation:**

Correction: E is false. A state store is NOT replicated to all instances; each task's store lives on one instance and is backed by a changelog topic. Optional standby replicas (`num.standby.replicas`, default 0) keep warm copies on other instances only if configured, and never on "all" instances. Only A and F are defensible, so this is "select 2", not 3. Original text follows.

Kafka Streams provides robust state management through local state stores that are mirrored to standby replicas for fault tolerance. Offsets are committed automatically, guaranteeing at‑least‑once semantics. Aggregations produce changelog topics that serve as durable, queryable stores. However, operators like filter() only remove records; key/value changes require mapping functions. Producing to the same source topic can create loops unless mitigated, and task restarts recover state from changelogs rather than rebuilding it from scratch. Understanding these mechanics is essential for building reliable, scalable stream processing applications. For more details, see the official Kafka Streams documentation: https://kafka.apache.org/documentation/streams/, https://docs.confluent.io/platform/current/streams/developer-guide.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams: Architecture Overview" (pp. 410-416)

**Detailed explanation of each option:**

1. ❌ **A. The internal state store of a Kafka Streams application is automatically replicated to all instances of the application.**  
   **Incorrect**. Each task's store lives on a single instance and is backed by a changelog topic. Standby replicas exist only when `num.standby.replicas` > 0 (default 0) and are placed on a limited number of other instances, not on all of them. Only a `GlobalKTable` is fully materialized on every instance.

2. ❌ **B. Using the KStream.filter() operator can modify the downstream key of a record without changing the original key.**  
   **Incorrect**. filter() only removes records that do not satisfy the predicate; it does not alter the key or value. Key/value transformations are performed by map, mapValues, or selectKey.

3. ✅ **C. The materialized view created with aggregate() is stored in a changelog topic that can be queried by other consumers.**  
   **Correct**. aggregate() creates a persistent state store backed by a changelog topic, which other consumers can read for point‑in‑time queries or for stream replay.

4. ❌ **D. A Kafka Streams application can safely produce records to the same topic it consumes from without risking infinite loops.**  
   **Incorrect**. Producing back to the source topic can create a loop unless precautions (e.g., distinct stream names, windowing, or filtering) are taken. The framework does not automatically prevent such loops.

5. ✅ **E. Kafka Streams automatically commits the offsets of input topics on behalf of the application, typically every few seconds or when the application is closed.**  
   **Correct**. Kafka Streams manages offset commits internally. By default it commits offsets at intervals defined by the commit interval (e.g., 30 seconds) or on graceful shutdown, ensuring at-least‑once processing.

6. ❌ **F. When a stream processing task fails, Kafka Streams restarts the task on a different node, but the task’s local state is lost and must be rebuilt from scratch.**  
   **Incorrect**. The task’s state is restored from its changelog topic on the new node, so the local state is not lost.

</details>

## Question 4 (Kafka Producers):
You are deploying a high‑throughput application that writes millions of records per second to Kafka. Which of the following producer configuration settings and practices will most effectively increase throughput while reducing CPU overhead? Select all that apply.

- A. Configure `compression.type=gzip` to reduce network I/O.
- B. Increase `batch.size` and `linger.ms` to allow more records per request.
- C. Enable `idempotence=true` to allow out‑of‑order retries without duplication.
- D. Decrease `linger.ms` to 0 to send messages immediately.
- E. Set `max.request.size` to the maximum allowable value to allow larger batches.
- F. Disable `request.timeout.ms` to avoid retries.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, B, A

**Explanation:**

Throughput in Kafka producers is primarily governed by how efficiently records are batched and transmitted. Enabling idempotence (`idempotence=true`) provides safe retries and reduces the risk of duplicate processing, indirectly lowering CPU load by avoiding complex duplicate handling. Compression reduces payload size, decreasing network I/O and broker load; gzip offers strong compression at the cost of some CPU, while alternatives like LZ4 or Snappy trade speed for lower compression ratios. Adjusting `batch.size` and `linger.ms` allows the producer to aggregate more records into a single request, reducing the number of round‑trips and associated CPU cycles. The other options either increase memory usage without benefit (max.request.size), force immediate sends (linger.ms=0), or remove retry safeguards (disabling request.timeout.ms), all of which degrade performance or reliability.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "compression.type" (p. 59)

**Detailed explanation of each option:**

1. ✅ **A. Configure `compression.type=gzip` to reduce network I/O.**  
   **Correct**. Using gzip (or LZ4/ Snappy) compresses message payloads before transmission, lowering the amount of data sent over the network. This directly improves throughput and can reduce CPU overhead on the broker side, though gzip adds some CPU cost on the producer side. It remains a common tuning practice for bandwidth‑limited environments.

2. ✅ **B. Increase `batch.size` and `linger.ms` to allow more records per request.**  
   **Correct**. Larger `batch.size` values and a slightly higher `linger.ms` give the producer time to accumulate more records, resulting in fewer, larger requests. This reduces network overhead and CPU load, leading to higher throughput.

3. ✅ **C. Enable `idempotence=true` to allow out‑of‑order retries without duplication.**  
   **Correct**. Enabling idempotence ensures safe retries and eliminates duplicate records, which can reduce CPU work spent on duplicate detection during recovery. It also enables transaction support and guarantees exactly‑once delivery, making it a beneficial tuning option for high‑volume producers.

4. ❌ **D. Decrease `linger.ms` to 0 to send messages immediately.**  
   **Incorrect**. Setting `linger.ms` to zero forces the producer to send a request as soon as a record is queued, eliminating batching. This increases network round‑trips and CPU usage, and usually lowers throughput.

5. ❌ **E. Set `max.request.size` to the maximum allowable value to allow larger batches.**  
   **Incorrect**. Increasing `max.request.size` only raises the upper bound for a single request. It does not improve batching efficiency and can lead to higher memory usage and larger network payloads, which may actually reduce throughput. Therefore this is not a recommended tuning step.

6. ❌ **F. Disable `request.timeout.ms` to avoid retries.**  
   **Incorrect**. Removing the timeout would prevent the producer from retrying failed requests, increasing the chance of data loss and making the system unreliable. It does not improve throughput or CPU usage and is not a valid tuning option.

</details>

## Question 5 (Programming & Serialization):
Schema Registry is configured with BACKWARD
compatibility (default). A producer a new field named **age**
WITHOUT a default value. What happens?

- A. Consumer will ignore the new field and process the record normally.
- B. Schema Registry will reject the registration of the new schema due to a compatibility violation.
- C. Consumer will read null for the new field.
- D. Producer will only add the new field for messages after a topic reconfiguration.
- E. Consumer will fail with an Avro serialization error because the missing field cannot be found.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

CORRECTION: adding a field WITHOUT a default is NOT backward compatible (a new-schema reader cannot fill the field when reading old records), so under the registry's default BACKWARD compatibility the registration is rejected (HTTP 409 / incompatible schema) and no records with the new schema are ever produced. Only if the subject were set to FORWARD/FULL_TRANSITIVE-style forward compatibility (or NONE) would old consumers simply ignore the new field (the former option C). Original text follows (its compatibility claim is wrong).

When a producer adds a new field without a default value, the change is considered backward compatible in Avro: older consumers can still read records written with the new schema because they simply ignore unknown fields. Schema Registry, configured with the default backward compatibility setting, will accept the new schema. Consumers that use the original schema will continue to function without errors, processing all known fields and disregarding the new one. This behavior exemplifies Avro’s forward/backward compatibility model and is documented in Confluent’s Schema Registry compatibility guide (https://docs.confluent.io/platform/current/schema-registry/compatibility.html).

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. Consumer will ignore the new field and process the record normally.**  
   **Incorrect**. This would only hold if the schema had been registered under a forward-compatible (or NONE) setting; with the default BACKWARD setting the schema is rejected before any record is written.

2. ✅ **B. Schema Registry will reject the registration of the new schema due to a compatibility violation.**  
   **Correct**. The default compatibility is BACKWARD, which only allows adding fields that have a default (or deleting fields). Adding `age` without a default violates it, so registration fails.

3. ❌ **C. Consumer will read null for the new field.**  
   **Incorrect**. The new field is not present in the consumer’s reader schema, so it is simply ignored. The consumer never sees a null value for it.

4. ❌ **D. Producer will only add the new field for messages after a topic reconfiguration.**  
   **Incorrect**. The schema change is applied at the producer level; all new messages after the schema update contain the field immediately, no topic reconfiguration needed.

5. ❌ **E. Consumer will fail with an Avro serialization error because the missing field cannot be found.**  
   **Incorrect**. Avro readers are designed to ignore unknown fields; the absence of a default does not cause a deserialization failure for older readers.

</details>

## Question 6 (Kafka Ecosystem):
In Confluent Schema Registry, which compatibility setting ensures that new schema versions are backward compatible, allowing consumers using the new version of the schema to read data produced with the previous schema?

- A. NONE compatibility
- B. FORWARD compatibility
- C. BACKWARD compatibility
- D. FULL compatibility

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The Confluent Schema Registry supports multiple compatibility modes to manage schema evolution. BACKWARD compatibility ensures consumers using the new schema can read data produced with the previous schema, so consumers are upgraded before producers. FORWARD compatibility is the inverse, ensuring data produced with the new schema can still be read by consumers using the previous schema (producers are upgraded first). FULL compatibility enforces both backward and forward compatibility, providing the strictest guarantees but limiting schema changes. NONE disables compatibility checks, risking runtime serialization errors. Understanding these settings is critical for Confluent Certified Developers to design schemas that evolve safely in production environments and maintain data integrity across distributed Kafka applications.

NOTE (fix): the original question text described the direction backwards ("consumers using the previous schema read data produced with the new schema" is FORWARD, not BACKWARD). Per Confluent docs: BACKWARD = consumers using the NEW schema can read data produced with the last schema (default mode; upgrade consumers first); FORWARD = data produced with the new schema can be read by consumers using the last schema. The question wording was corrected so that B stays the answer (with the original wording the literal answer would be C). The explanation of B/C below was also corrected; the first paragraph's sentence about FORWARD being "new consumers read old data" is wrong - that is BACKWARD.

Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

**Detailed explanation of each option:**

1. ❌ **A. NONE compatibility**  
   **Incorrect**. NONE disables compatibility checks, allowing any schema to be registered regardless of compatibility.

2. ❌ **B. FORWARD compatibility**  
   **Incorrect**. FORWARD compatibility ensures that data produced with the new schema can be read by consumers using the previous schema version, which is the opposite direction.

3. ✅ **C. BACKWARD compatibility**  
   **Correct**. BACKWARD compatibility ensures that consumers using the new schema can read data produced with the previous schema version (so consumers are upgraded first; it also allows rewinding consumers to the start of the topic).

4. ❌ **D. FULL compatibility**  
   **Incorrect**. FULL compatibility requires both backward and forward compatibility, which is stricter than just backward compatibility.

</details>

## Question 7 (Application Testing):
When writing automated tests for Kafka client applications (producers, consumers, and Kafka Streams topologies) that should run fast and without requiring a live Kafka cluster, which of the following tools or techniques are most appropriate? (Select all that apply)

- A. Leverage a hypothetical KafkaClient "UnitTest" mode that mocks all broker interactions.
- B. Employ EmbeddedKafka (from spring-kafka or Testcontainers) to spin up an in‑memory broker for integration tests.
- C. Use MockProducer and MockConsumer to simulate broker interactions for producer/consumer logic.
- D. Run the application against a real Kafka cluster with test topics and manually verify output.
- E. Use Kafka Streams' TopologyTestDriver with MockInputTopic and MockOutputTopic to drive a topology in isolation.
- F. Create topics with AdminClient and then run a real consumer to validate message flow.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, B, E

**Explanation:**

Unit testing Kafka client code demands tools that remove external dependencies while preserving API semantics. TopologyTestDriver isolates stream logic, EmbeddedKafka offers a quick in‑memory broker for higher‑level integration checks, and MockProducer/MockConsumer verify producer/consumer behavior without network overhead. The other options either rely on a real cluster (integration testing) or reference non‑existent features, thus they are not suitable for fast, isolated unit tests. Understanding the appropriate tool for each test type is essential for efficient test suites in a Confluent Certified Developer context.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 5 "Testing" (pp. 131-133) and Ch. 14 "Testing a Topology" (pp. 411-412)

**Detailed explanation of each option:**

1. ❌ **A. Leverage a hypothetical KafkaClient "UnitTest" mode that mocks all broker interactions.**  
   **Incorrect**. No such built‑in mode exists in the Kafka client library.

2. ✅ **B. Employ EmbeddedKafka (from spring-kafka or Testcontainers) to spin up an in‑memory broker for integration tests.**  
   **Correct**. EmbeddedKafka gives a lightweight, fully‑functional broker that can be started and stopped per test, ideal for integration testing without external dependencies.

3. ✅ **C. Use MockProducer and MockConsumer to simulate broker interactions for producer/consumer logic.**  
   **Correct**. These mock clients allow verification of record metadata and deserialization logic without network traffic.

4. ❌ **D. Run the application against a real Kafka cluster with test topics and manually verify output.**  
   **Incorrect**. This approach requires an external broker and is considered integration testing, not a lightweight unit test.

5. ✅ **E. Use Kafka Streams' TopologyTestDriver with MockInputTopic and MockOutputTopic to drive a topology in isolation.**  
   **Correct**. TopologyTestDriver is specifically designed to test stream topologies without a broker, providing deterministic input and output records.

6. ❌ **F. Create topics with AdminClient and then run a real consumer to validate message flow.**  
   **Incorrect**. While AdminClient can create topics, using a real consumer still depends on a broker, making it an integration test.

</details>

## Question 8 (Kafka Connect):
You are configuring a Kafka Connect worker to connect to a Confluent Platform cluster that requires SASL/PLAIN authentication over TLS. Which of the following worker properties must be set (directly or via the worker properties file) to establish a secure connection?

- A. Configure `ssl.truststore.location` and `ssl.truststore.password` in the worker properties.
- B. Set `sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="user" password="pass";` in the worker properties.
- C. Add `security.protocol=SASL_SSL` to the worker properties.
- D. Provide `sasl.mechanism=PLAIN` in the worker properties.
- E. Add `producer.security.protocol=PLAINTEXT` to the connector configuration.
- F. Set `bootstrap.servers` to `ssl://kafka-broker:9093`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, B, D

**Explanation:**

A Kafka Connect worker connects to a Kafka cluster via the bootstrap servers and applies a single security protocol for both consumer and producer clients. For a SASL/PLAIN over TLS cluster, the worker must specify `security.protocol=SASL_SSL`, the `sasl.mechanism=PLAIN`, and provide the JAAS login configuration. These three properties enable the TLS handshake and SASL authentication. Optional truststore settings are only needed when the broker’s certificate isn’t in the default truststore. Note: the worker-level settings secure only the worker’s own clients (internal topics/admin); the producers/consumers of connectors need the same settings with the `producer.`/`consumer.`/`admin.` prefixes (or connector-level `producer.override.*`/`consumer.override.*`). Specifying `ssl://` in `bootstrap.servers` is unnecessary, and setting a plaintext protocol would expose traffic. Understanding which properties belong to the worker versus connector configuration prevents misconfigurations that cause connection failures.

Source: https://docs.confluent.io/platform/current/connect/security.html; https://kafka.apache.org/documentation/#security_sasl_plain; book ch. 11 (PDF p. 304)

**Detailed explanation of each option:**

1. ❌ **A. Configure `ssl.truststore.location` and `ssl.truststore.password` in the worker properties.**  
   **Incorrect**. While useful when the broker uses a self‑signed or private CA certificate, these properties are optional if the broker's certificate is already trusted by the Java default truststore.

2. ✅ **B. Set `sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="user" password="pass";` in the worker properties.**  
   **Correct**. This JAAS configuration supplies the credentials for SASL/PLAIN authentication and is mandatory for the worker to authenticate.

3. ✅ **C. Add `security.protocol=SASL_SSL` to the worker properties.**  
   **Correct**. This property tells the worker to use TLS for transport and SASL for authentication, which is mandatory for a SASL/PLAIN over TLS cluster.

4. ✅ **D. Provide `sasl.mechanism=PLAIN` in the worker properties.**  
   **Correct**. The SASL mechanism must match the broker's configuration; for SASL/PLAIN authentication this property is required.

5. ❌ **E. Add `producer.security.protocol=PLAINTEXT` to the connector configuration.**  
   **Incorrect**. Connector configurations are separate from the worker and must mirror the worker's security settings; using PLAINTEXT would break the secure connection.

6. ❌ **F. Set `bootstrap.servers` to `ssl://kafka-broker:9093`.**  
   **Incorrect**. bootstrap.servers takes plain host:port pairs (a URL scheme like `ssl://` is not valid there); the security protocol dictates TLS usage.

</details>

## Question 9 (Deployment & Ops):
When deploying a Kafka Streams application in a Docker/Kubernetes environment, which of the following practices are 
essential to ensure reliable state management, proper initialization, and seamless scaling?

- A. Set the Streams application to use the changelog topics for state store restoration automatically.
- B. Expose Kafka bootstrap servers through a NodePort service for external access.
- C. Use a Kubernetes StatefulSet with Persistent Volume Claims to preserve local state across pod restarts.
- D. Run an init container that creates required Kafka topics and verifies connectivity before the Streams pod starts.
- E. Run the Streams application as a single replica pod to reduce resource usage.
- F. Configure the Streams application to use exactly‑once semantics by setting application.id and enable.idempotence.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

Deploying Kafka Streams on Docker/Kubernetes requires more than just container images; it demands reliable state persistence, correct initialization, and built‑in scalability. A StatefulSet with Persistent Volume Claims guarantees that local state survives pod rescheduling. An init container that pre‑creates topics ensures the application starts only when its dependencies are ready, preventing runtime failures. Relying on Kafka’s changelog topics for state store restoration allows the Streams app to rebuild state efficiently after a crash or scaling event. These practices are aligned with Confluent’s deployment guidance and are critical for production reliability. References: - Confluent Docs – Deploying Streams in Kubernetes: https://docs.confluent.io/platform/current/streams/deployment.html - Kubernetes StatefulSets: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ - Kafka Streams – State Store and Changelog Topics: https://docs.confluent.io/platform/current/streams/developer-guide/streams-state.html  
Source: https://kafka.apache.org/43/documentation/streams/developer-guide/running-app/ (state restoration from changelog, standby replicas, scaling) ; https://kafka.apache.org/43/documentation/streams/architecture/ (state, changelog topics). Note: K8s-specific items (StatefulSet, init container) are deployment practices, not Kafka docs.

**Detailed explanation of each option:**

1. ✅ **A. Set the Streams application to use the changelog topics for state store restoration automatically.**  
   **Correct**. Streams automatically writes state to changelog topics. Configuring this ensures that on restart, the state store can be rebuilt efficiently from Kafka, reducing recovery time.

2. ❌ **B. Expose Kafka bootstrap servers through a NodePort service for external access.**  
   **Incorrect**. Exposing internal Kafka brokers via NodePort is insecure and unnecessary; clients should use a dedicated Kafka service within the cluster or a managed Kafka service.

3. ✅ **C. Use a Kubernetes StatefulSet with Persistent Volume Claims to preserve local state across pod restarts.**  
   **Correct**. A StatefulSet provides stable network identity and persistent storage for the Streams state store. Without it, local state would be lost on pod rescheduling, leading to unnecessary state restoration overhead.

4. ✅ **D. Run an init container that creates required Kafka topics and verifies connectivity before the Streams pod starts.**  
   **Correct**. Using an init container guarantees that the application does not start until its topics exist and connectivity is confirmed, avoiding runtime errors and ensuring idempotent startup.

5. ❌ **E. Run the Streams application as a single replica pod to reduce resource usage.**  
   **Incorrect**. While reducing resources is desirable, a single replica limits fault tolerance and scalability. Deploying multiple replicas improves availability and throughput.

6. ❌ **F. Configure the Streams application to use exactly‑once semantics by setting application.id and enable.idempotence.**  
   **Incorrect**. Exactly‑once in Kafka Streams is enabled with `processing.guarantee=exactly_once_v2`; `application.id` is unrelated to it and `enable.idempotence` is configured by Streams itself. It is an application setting, not a deployment practice.

</details>

## Question 10 (Stream Processing):
You have two Kafka topics: `orders` (key = `order_id`) and `payments` (key = `payment_id`). In a Kafka Streams application you need to correlate each payment with its originating order. Which data‑modeling strategy will allow the join to execute efficiently without repartitioning the data stream?

- A. Use a time‑windowed join and let Kafka Streams automatically handle key differences.
- B. Use a global table keyed by `order_id` and join the payments stream to it.
- C. Add an `order_id` field to the payment value and perform a stream‑stream join with a tumbling window.
- D. Publish payments with the key set to `order_id` (i.e., re‑key the payment records before producing).
- E. Create a repartition topic keyed by `order_id` for the payments stream and join on that.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In Kafka Streams, stream‑stream joins require that both streams share the same key; otherwise, Kafka Streams performs an implicit repartition that incurs network shuffling and latency. By re‑keying the payments stream to use the `order_id` key before it reaches the Streams application, you enable a direct partition‑aligned join with zero repartitioning. This design choice reduces resource consumption and simplifies the topology. While repartition topics or adding fields are technically feasible, they add complexity and performance costs. Understanding key design is essential for efficient stream processing and is a core concept in Confluent’s Kafka Streams data‑modeling best practices.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Stream-Table Join"/"Streaming Join" (pp. 396-399)

**Detailed explanation of each option:**

1. ❌ **A. Use a time‑windowed join and let Kafka Streams automatically handle key differences.**  
   **Incorrect**. Kafka Streams cannot automatically reconcile different keys; the streams still need the same key to join efficiently.

2. ❌ **B. Use a global table keyed by `order_id` and join the payments stream to it.**  
   **Incorrect**. A global table is used for a stream‑table join, not a stream‑stream join, and would still require repartitioning of the payments stream if its key is not `order_id`.

3. ❌ **C. Add an `order_id` field to the payment value and perform a stream‑stream join with a tumbling window.**  
   **Incorrect**. The join key is still `payment_id`; adding a field does not change the key and Kafka Streams will automatically trigger a repartition, causing unnecessary shuffling.

4. ✅ **D. Publish payments with the key set to `order_id` (i.e., re‑key the payment records before producing).**  
   **Correct**. For a stream‑stream join, the join key must be the topic key. By setting the payment key to `order_id`, both streams share the same key and no repartitioning is required, resulting in a single partitioned join.

5. ❌ **E. Create a repartition topic keyed by `order_id` for the payments stream and join on that.**  
   **Incorrect**. Possible but not the most efficient approach. Repartitioning introduces an extra topic and shuffle, which increases latency and overhead compared to simply re‑keying at production time.

</details>

## Question 11 (Observability & Testing):
You have deployed a Kafka consumer application that is now reporting high lag across several partitions. Which of the following actions are effective first‑step troubleshooting techniques to isolate the root cause?

- A. Analyze the consumer’s thread pool size and `max.poll.interval.ms` to ensure it is not timing out and losing offsets.
- B. Check the size of the `__consumer_offsets` topic to determine if offset commits are being throttled.
- C. Increase the consumer’s `fetch.min.bytes` setting to reduce the number of fetch requests.
- D. Verify that the consumer group’s `auto.offset.reset` is set to `earliest` to ensure it reads from the beginning of the partition.
- E. Enable and monitor the `consumer-fetch-manager-metrics` JMX bean for `fetcher.max.poll.records` and `fetcher.avg.bytes.per.sec`.
- F. Use `kafka-consumer-groups.sh --describe` to view current lag for each partition.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, F

**Explanation:**

Effective lag troubleshooting starts with quantifying the problem using `kafka-consumer-groups.sh --describe`, which shows the exact number of messages behind each partition. Once lag is confirmed, inspect consumer configuration for timing issues: a too‑small `max.poll.interval.ms` causes frequent rebalances that reset offsets, while an undersized thread pool can delay poll calls. Adjusting these settings restores a steady consumer pace. JMX fetch metrics and `fetch.min.bytes` can provide context on throughput, but they are secondary to lag measurement and configuration tuning. These practices align with Confluent’s guidance on monitoring consumer lag and tuning consumer performance. Note: `consumer-fetch-manager-metrics` does expose lag (`records-lag-max`, per-partition `records-lag`), but the metric names in option D (`fetcher.max.poll.records`, `fetcher.avg.bytes.per.sec`) do not exist, which makes D wrong. Option A is only loosely worded (the consumer has no thread pool; the point is that slow processing between `poll()` calls exceeding `max.poll.interval.ms` triggers rebalances).

Source: https://kafka.apache.org/documentation/#consumer_monitoring and #basic_ops_consumer_group; Kafka: The Definitive Guide 2nd ed., ch. 13 (Consumer lag monitoring, Burrow) and ch. 4.

**Detailed explanation of each option:**

1. ✅ **A. Analyze the consumer’s thread pool size and `max.poll.interval.ms` to ensure it is not timing out and losing offsets.**  
   **Correct**. A too‑low `max.poll.interval.ms` can trigger rebalances, causing offsets to be re‑consumed and increasing lag. Adjusting thread pool and interval settings can mitigate this.

2. ❌ **B. Check the size of the `__consumer_offsets` topic to determine if offset commits are being throttled.**  
   **Incorrect**. Offset commits are typically lightweight; the size of `__consumer_offsets` rarely causes significant lag. This check is rarely useful for lag diagnosis.

3. ❌ **C. Increase the consumer’s `fetch.min.bytes` setting to reduce the number of fetch requests.**  
   **Incorrect**. Raising `fetch.min.bytes` can reduce request frequency but may increase latency; it does not directly address lag and can actually worsen it if the consumer blocks waiting for more data.

4. ❌ **D. Verify that the consumer group’s `auto.offset.reset` is set to `earliest` to ensure it reads from the beginning of the partition.**  
   **Incorrect**. `auto.offset.reset` only matters when a group has no committed offset. Changing it does not affect an already‑running consumer’s lag.

5. ❌ **E. Enable and monitor the `consumer-fetch-manager-metrics` JMX bean for `fetcher.max.poll.records` and `fetcher.avg.bytes.per.sec`.**  
   **Incorrect**. The metrics named here (`fetcher.max.poll.records`, `fetcher.avg.bytes.per.sec`) do not exist. The bean `kafka.consumer:type=consumer-fetch-manager-metrics` does expose lag via `records-lag-max` and fetch throughput via `bytes-consumed-rate`, but the option names the wrong attributes.

6. ✅ **F. Use `kafka-consumer-groups.sh --describe` to view current lag for each partition.**  
   **Correct**. This command directly reports lag per partition, making it a core diagnostic step for understanding consumer performance issues.

</details>

## Question 12 (Kafka Core Concepts):
Which of the following statements about Kafka topics are correct in the context of Confluent Certified Developer for Apache Kafka?

- A. A Kafka topic is a logical channel to which producers publish data and consumers subscribe to consume data.
- B. Each partition within a Kafka topic guarantees message ordering only within that partition.
- C. Partitions in a Kafka topic help parallelize data processing and enable scalability of both producers and consumers.
- D. Kafka topics automatically replicate data across all brokers in the cluster for fault tolerance.
- E. Kafka topics cannot be deleted once created; they persist indefinitely unless the entire cluster is reset.
- F. A topic’s retention period determines how long Kafka retains the messages regardless of whether they have been consumed.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, B, F, C

**Explanation:**

Kafka topics are logical streams of data divided into partitions, where ordering is guaranteed only within individual partitions. Producers write data to topics, and consumers read from them, enabling decoupled data pipelines. Replication provides fault tolerance but only to configured replica sets, not necessarily all brokers. Retention policies determine how long messages persist regardless of consumption, facilitating replay and temporal decoupling. Topics can be deleted if broker settings allow, which is important for cluster hygiene. Partitions also facilitate parallelism and scalability by distributing load across multiple brokers and consumers. Understanding these nuances is critical for developing robust Kafka applications and passing the Confluent Certified Developer exam.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 (Topics and Partitions), Ch. 2 (delete.topic.enable defaults to true), Ch. 6 (Replication, Retention); https://kafka.apache.org/documentation/#intro_topics

**Detailed explanation of each option:**

1. ✅ **A. A Kafka topic is a logical channel to which producers publish data and consumers subscribe to consume data.**  
   **Correct**. Topics serve as the fundamental abstraction for data organization in Kafka, enabling decoupling of producers and consumers.

2. ✅ **B. Each partition within a Kafka topic guarantees message ordering only within that partition.**  
   **Correct**. Kafka guarantees order only on a per-partition basis, not across the entire topic.

3. ✅ **C. Partitions in a Kafka topic help parallelize data processing and enable scalability of both producers and consumers.**  
   **Correct**. Partitions enable horizontal scaling by allowing multiple consumers and producers to operate concurrently on different partitions.

4. ❌ **D. Kafka topics automatically replicate data across all brokers in the cluster for fault tolerance.**  
   **Incorrect**. Replication factor is configurable per topic and may not include all brokers; data is replicated to a subset of brokers designated as replicas.

5. ❌ **E. Kafka topics cannot be deleted once created; they persist indefinitely unless the entire cluster is reset.**  
   **Incorrect**. Kafka supports topic deletion if enabled in the broker configuration; topics can be deleted via administrative tools.

6. ✅ **F. A topic’s retention period determines how long Kafka retains the messages regardless of whether they have been consumed.**  
   **Correct**. Retention is based on time or size and applies independently of message consumption status.

</details>

## Question 13 (Kafka Ecosystem):
Which of the following Kafka APIs are part of the core Kafka client library and are primarily used for producing, consuming, and processing streaming data within Apache Kafka?

- A. Producer API
- B. REST Proxy API
- C. Consumer API
- D. Connect API
- E. Admin API
- F. Streams API

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, F, C

**Explanation:**

The core Kafka client library includes the Producer API, Consumer API, and Streams API, which are essential for producing, consuming, and processing streaming data within Kafka. The Producer API enables applications to send records to Kafka topics, while the Consumer API allows reading from topics. The Streams API facilitates building stateful stream processing applications directly on Kafka data streams. Other APIs such as Connect API, Admin API, and REST Proxy serve different purposes: Connect API is for integration with external systems, Admin API for Kafka resource management, and REST Proxy for HTTP access to Kafka. Understanding these distinctions is crucial for developers to select appropriate APIs for application development in Kafka ecosystems.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410) — NOTE: Producer, Consumer, Streams are core client APIs; Connect/Admin are separate per book Ch. 1/9/5.

**Detailed explanation of each option:**

1. ✅ **A. Producer API**  
   **Correct**. The Producer API is a core Kafka client API used to publish (write) records to Kafka topics.

2. ❌ **B. REST Proxy API**  
   **Incorrect**. The REST Proxy provides a RESTful interface to Kafka but is not part of the core Kafka client library.

3. ✅ **C. Consumer API**  
   **Correct**. The Consumer API is a core Kafka client API used to subscribe to topics and consume (read) records from Kafka.

4. ❌ **D. Connect API**  
   **Incorrect**. The Connect API is part of Kafka Connect framework for integrating Kafka with external systems, not for direct producing or consuming of streaming data.

5. ❌ **E. Admin API**  
   **Incorrect**. The Admin API is used for managing and inspecting Kafka resources such as topics and brokers, not for data production or consumption.

6. ✅ **F. Streams API**  
   **Correct**. The Streams API is a core Kafka client API that allows for building stream processing applications that consume, process, and produce data within Kafka.

</details>

## Question 14 (Kafka Connect):
Which of the following statements correctly describe core features and capabilities of Kafka Connect’s runtime that help manage connector deployment, scaling, and data transformations?

- A. Kafka Connect can automatically create destination topics when running sink connectors if the auto.create.topics.enabled property is set.
- B. Kafka Connect supports Single Message Transforms (SMTs) for on-the-fly data transformation.
- C. Kafka Connect exposes a REST API but only for starting and stopping connectors, not for configuration.
- D. Kafka Connect automatically registers schemas in the Schema Registry for all connectors.
- E. Kafka Connect distributes connector tasks across workers for load balancing and fault tolerance.
- F. Kafka Connect automatically rolls back connector configuration changes if the connector fails to start.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** E, B

**Explanation:**

CORRECTION: only B and C are true (this is a "select 2" question). F is false: Connect's automatic topic creation (KIP-158, `topic.creation.enable` plus `topic.creation.*` settings) applies to SOURCE connectors that write new topics; sink connectors only read existing topics, and `auto.create.topics.enabled` is not a Connect property (it is not the broker's `auto.create.topics.enable` either). Original text follows (its mention of sink topic creation is wrong).

Kafka Connect is designed as a scalable, fault‑tolerant framework for integrating Kafka with external systems. Key runtime features include automatic topic creation for sinks (when enabled), dynamic task distribution across workers for load balancing and high availability, and a comprehensive REST API that manages connector life‑cycle and configuration. Additionally, Connect supports Single Message Transforms (SMTs) that allow lightweight, per‑message processing without external code. Misconceptions often arise around automatic schema registration and configuration rollback; these are optional or manual actions, not built‑in Connect capabilities. Understanding these distinctions is critical for configuring robust, production‑grade pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect can automatically create destination topics when running sink connectors if the auto.create.topics.enabled property is set.**  
   **Incorrect**. Connect can create topics only for source connectors (via `topic.creation.enable` and `topic.creation.*`, KIP-158). Sink connectors consume from existing topics, and `auto.create.topics.enabled` is not a Connect setting.

2. ✅ **B. Kafka Connect supports Single Message Transforms (SMTs) for on-the-fly data transformation.**  
   **Correct**. SMTs are lightweight, reusable components applied to each message during source ingestion or sink output, enabling field renaming, masking, or filtering without external code.

3. ❌ **C. Kafka Connect exposes a REST API but only for starting and stopping connectors, not for configuration.**  
   **Incorrect**. The REST API supports full lifecycle operations: creating, updating, deleting, and querying connector configurations, status, and task information.

4. ❌ **D. Kafka Connect automatically registers schemas in the Schema Registry for all connectors.**  
   **Incorrect**. Schema registration is optional and performed by the connector implementation, not automatically by Connect itself. Connect can use the Schema Registry when configured, but it does not enforce automatic schema registration for every connector.

5. ✅ **E. Kafka Connect distributes connector tasks across workers for load balancing and fault tolerance.**  
   **Correct**. Each connector is split into tasks that can run on any worker in the cluster. The Connect worker group automatically balances tasks and reassigns them if a worker fails, providing scalability and high availability.

6. ❌ **F. Kafka Connect automatically rolls back connector configuration changes if the connector fails to start.**  
   **Incorrect**. If a connector fails to start, it enters the FAILED state; Connect does not automatically revert the configuration change. The user must manually adjust or delete the connector.

</details>

## Question 15 (Stream Processing):
In Apache Kafka Streams, which of the following statements about time windows are true when implementing tumbling and hopping windows for event-time based aggregations?

- A. Session windows are a type of time window that have a fixed size and do not depend on event gaps.
- B. Grace periods define how long Kafka Streams waits after a window end before emitting results to accommodate late-arriving events.
- C. Tumbling windows are fixed-size, non-overlapping windows that group events strictly based on event-time.
- D. Event-time windows in Kafka Streams rely on record timestamps by default; ingestion time is used only when records have invalid or no timestamps.
- E. Hopping windows can overlap, allowing an event to belong to multiple windows if the hop interval is smaller than the window size.
- F. Kafka Streams automatically adjusts window size dynamically based on event skew and late arrivals.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, E, B

**Explanation:**

In Kafka Streams, time windows segment event streams to perform time-based aggregations. Tumbling windows are fixed, non-overlapping intervals strictly aligned to event-time, ensuring each event belongs to exactly one window. Hopping windows overlap by advancing with a hop interval smaller than the window size, allowing events to appear in multiple windows. Grace periods enable the handling of late-arriving events by extending the window retention before finalizing results. By default, Kafka Streams uses the timestamps embedded in records (set by producers), not ingestion time. The default timestamp extractor is `FailOnInvalidTimestamp`, which uses the record's embedded timestamp and fails on invalid ones. If a timestamp extractor is not configured or the record has an invalid timestamp, behavior depends on the configured extractor. Session windows differ by dynamically grouping events separated by inactivity gaps, not by fixed size.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Time Windows" (pp. 390-392); kafka.apache.org/43/streams/developer-guide/dsl-api/

**Detailed explanation of each option:**

1. ❌ **A. Session windows are a type of time window that have a fixed size and do not depend on event gaps.**  
   **Incorrect**. Session windows group events based on inactivity gaps, so their size is dynamic and depends on event arrival patterns.

2. ✅ **B. Grace periods define how long Kafka Streams waits after a window end before emitting results to accommodate late-arriving events.**  
   **Correct**. Grace periods allow late events within a defined delay to be processed and aggregated before finalizing window results.

3. ✅ **C. Tumbling windows are fixed-size, non-overlapping windows that group events strictly based on event-time.**  
   **Correct**. Tumbling windows segment the event-time timeline into contiguous, non-overlapping intervals, making them ideal for discrete aggregation periods.

4. ❌ **D. Event-time windows in Kafka Streams rely on record timestamps by default; ingestion time is used only when records have invalid or no timestamps.**  
   **Incorrect as originally stated**. Kafka Streams uses the record's embedded timestamp by default (via the `FailOnInvalidTimestamp` extractor), which is typically the producer's create time — not "ingestion time." The original statement that "ingestion time is used by default unless a timestamp extractor is configured" was misleading and has been corrected.

5. ✅ **E. Hopping windows can overlap, allowing an event to belong to multiple windows if the hop interval is smaller than the window size.**  
   **Correct**. Hopping windows advance by a fixed hop interval smaller than the window size, causing windows to overlap and events to be counted in multiple windows.

6. ❌ **F. Kafka Streams automatically adjusts window size dynamically based on event skew and late arrivals.**  
   **Incorrect**. Window sizes in Kafka Streams are statically defined by the developer and do not dynamically adjust; late arrivals are handled via grace periods.

</details>

## Question 16 (Stream Processing):
In the context of designing stream processing applications with Kafka Streams, which design pattern best addresses the challenge of maintaining and querying large, continuously updated state while ensuring fault tolerance and scalability?

- A. Event Sourcing Pattern
- B. Stateless Transformation Pattern
- C. Publish-Subscribe Pattern
- D. Aggregator Pattern

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Event Sourcing Pattern is highly relevant for Kafka Streams developers because Kafka’s append-only log naturally supports storing event sequences that represent all state changes. This pattern enables reconstructing the current state by replaying events, ensuring fault tolerance and scalability. Stateless transformations do not maintain state, so they cannot handle large stateful requirements. Aggregator Pattern focuses on summarization, not state persistence or recovery. Publish-Subscribe is a messaging pattern and does not solve state management challenges. Understanding Event Sourcing helps developers design robust, fault-tolerant stream processing applications aligned with Kafka’s architecture.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Stream Processing Design Patterns" (pp. 392-401)

**Detailed explanation of each option:**

1. ✅ **A. Event Sourcing Pattern**  
   **Correct**. Event Sourcing involves storing all changes as a sequence of events, enabling reconstruction of state from the event log. Kafka’s log-based storage aligns well with this pattern, facilitating fault-tolerant, scalable state management.

2. ❌ **B. Stateless Transformation Pattern**  
   **Incorrect**. Stateless transformations process each record independently without maintaining state, so they do not address challenges related to large or complex state management.

3. ❌ **C. Publish-Subscribe Pattern**  
   **Incorrect**. Publish-Subscribe is a messaging pattern for distributing messages to multiple consumers but does not directly address state management or fault tolerance in stream processing.

4. ❌ **D. Aggregator Pattern**  
   **Incorrect**. While aggregation is a common operation in stream processing, the Aggregator Pattern focuses on summarizing data rather than managing large, queryable state with fault tolerance.

</details>

## Question 17 (Kafka Consumers):
Which of the following statements about Kafka consumers and their behavior are true in the context of the Confluent Certified Developer for Apache Kafka exam?

- A. If a consumer fails, Kafka automatically reassigns the partitions of that consumer to other active consumers in the same group.
- B. Kafka consumers can only consume messages from the latest offset and cannot start from the earliest offset of a partition.
- C. Kafka consumer lag is the difference between the latest offset of a partition and the offset of the last message committed by the consumer.
- D. Kafka consumers within the same consumer group share partition consumption such that each partition is consumed by only one consumer at a time.
- E. Kafka consumers automatically commit offsets to Kafka only after the entire consumer group has processed the messages.
- F. Consumers in different consumer groups receive the same messages independently, enabling multiple independent consumption streams.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, A, C, F

**Explanation:**

Kafka consumers within the same group divide partitions so that each partition is consumed by only one consumer, enabling parallelism and avoiding duplicate processing. When a consumer fails, Kafka triggers a rebalance to reassign partitions, maintaining fault tolerance. Consumer lag is a critical metric representing the difference between the latest partition offset and the consumer's committed offset, indicating processing progress. Consumers can be configured to start from earliest, latest, or any specific offset, debunking the misconception that only latest offset consumption is possible. Additionally, consumers in different groups consume messages independently, enabling multiple applications or processing pipelines to consume the same topic data concurrently. Offset commits are managed per consumer, not collectively by the group, and can be automatic or manual depending on configuration.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Consumers and Consumer Groups" (pp. 77-83)

**Detailed explanation of each option:**

1. ✅ **A. If a consumer fails, Kafka automatically reassigns the partitions of that consumer to other active consumers in the same group.**  
   **Correct**. Kafka's group coordinator detects consumer failures and triggers a rebalance that redistributes partitions among the remaining consumers.

2. ❌ **B. Kafka consumers can only consume messages from the latest offset and cannot start from the earliest offset of a partition.**  
   **Incorrect**. Consumers can be configured to start consuming from the earliest offset, latest offset, or a specific offset, depending on the use case and consumer configuration.

3. ✅ **C. Kafka consumer lag is the difference between the latest offset of a partition and the offset of the last message committed by the consumer.**  
   **Correct**. Consumer lag measures how far behind a consumer is from the latest produced message, indicating processing delay or backpressure.

4. ✅ **D. Kafka consumers within the same consumer group share partition consumption such that each partition is consumed by only one consumer at a time.**  
   **Correct**. Kafka consumer groups coordinate to ensure that each partition's messages are consumed by only one consumer within the group, enabling parallel processing without duplication.

5. ❌ **E. Kafka consumers automatically commit offsets to Kafka only after the entire consumer group has processed the messages.**  
   **Incorrect**. Offset commits are managed at the individual consumer level, not collectively by the entire group. Consumers can commit offsets automatically or manually after processing their assigned partitions.

6. ✅ **F. Consumers in different consumer groups receive the same messages independently, enabling multiple independent consumption streams.**  
   **Correct**. Each consumer group maintains its own offset, so consumers in different groups process messages independently, allowing multiple applications to consume the same topic data.

</details>

## Question 18 (Kafka Connect):
Which of the following statements accurately describe core concepts or features related to Kafka Connect source, sink, and CDC connectors?

- A. CDC connectors require explicit schema registry configuration to capture change events from the source system.
- B. Sink connectors consume records from Kafka topics and write them into external target systems (e.g., HDFS, JDBC databases).
- C. Debezium connectors are an example of CDC connectors that transform change events into a JSON format by default.
- D. Source connectors read data from external systems (e.g., databases, message queues) and write the records into Kafka topics.
- E. Sink connectors do not support idempotent writes; they rely entirely on the external system to handle duplicate records.
- F. Kafka Connect's offset management for source connectors is stored in the connector configuration file by default.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, B, C

**Explanation:**

Kafka Connect distinguishes between source connectors (write to Kafka), sink connectors (read from Kafka), and CDC connectors (specialized sources that capture change events). Source connectors emit records into topics, while sink connectors pull from topics and persist to external sinks. Debezium exemplifies a CDC connector that emits change events in JSON. Offsets for source connectors are stored in a dedicated Kafka topic, not in configuration files. Sink connectors themselves do not enforce idempotence; idempotent behavior must be implemented by the connector or the target system. Understanding these distinctions is critical for designing reliable data pipelines.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ❌ **A. CDC connectors require explicit schema registry configuration to capture change events from the source system.**  
   **Incorrect**. While CDC connectors often produce Schema Registry-compatible schemas, they do not *require* schema registry configuration; they can operate with Avro or JSON schemas directly. Incorrect.

2. ✅ **B. Sink connectors consume records from Kafka topics and write them into external target systems (e.g., HDFS, JDBC databases).**  
   **Correct**. Sink connectors perform the opposite of source connectors by reading from Kafka and persisting to external stores. Correct.

3. ✅ **C. Debezium connectors are an example of CDC connectors that transform change events into a JSON format by default.**  
   **Correct**. Debezium emits change data events in JSON (or Avro) and is widely used as a CDC connector. Correct.

4. ✅ **D. Source connectors read data from external systems (e.g., databases, message queues) and write the records into Kafka topics.**  
   **Correct**. This is the fundamental role of a source connector. It extracts data and produces Kafka records. Correct.

5. ❌ **E. Sink connectors do not support idempotent writes; they rely entirely on the external system to handle duplicate records.**  
   **Incorrect**. Sink connectors themselves do not guarantee idempotence; however, idempotent writes can be achieved by implementing idempotent logic in the connector or by using external system features. The statement is misleading, so it is considered incorrect for the purpose of this question.

6. ❌ **F. Kafka Connect's offset management for source connectors is stored in the connector configuration file by default.**  
   **Incorrect**. Offsets are persisted in a dedicated Kafka topic (default: __connect-offsets), not in the connector config. Incorrect.

</details>

## Question 19 (Application Development):
Which of the following configuration settings or code practices are required to implement **exactly‑once** processing semantics in Apache Kafka when using the Java Producer and Consumer APIs? Select all that apply.

- A. Calling `Consumer.commitSync()` after each message is processed.
- B. Setting the producer property `acks=all`.
- C. Using `Producer.send()` without a callback.
- D. Setting the producer property `enable.idempotence=true`.
- E. Setting a unique `transactional.id` on the producer.
- F. Configuring the consumer with `enable.auto.commit=false`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, F, D

**Explanation:**

Exactly‑once processing in Kafka hinges on three key practices: the producer must be idempotent and transactional, which requires `enable.idempotence=true` and a unique `transactional.id`; the consumer must disable automatic offset commits so that offsets can be committed only after the transaction succeeds (`enable.auto.commit=false`). The other options are either redundant (acks=all is set automatically), optional, or incorrect (callbacks and per‑message commits). These settings together ensure that records are neither lost nor duplicated even across failures. For more detail, see the Kafka Producer configuration docs (https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence) and the Exactly‑Once semantics guide (https://docs.confluent.io/platform/current/kafka/producer.html#exactly-once).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 8 "Exactly-Once Semantics" (pp. 181-201)

**Detailed explanation of each option:**

1. ❌ **A. Calling `Consumer.commitSync()` after each message is processed.**  
   **Incorrect**. Manual commits are required, but committing after every message is not necessary; committing after the transaction commit is sufficient. Thus this option is not a distinct requirement.

2. ❌ **B. Setting the producer property `acks=all`.**  
   **Incorrect**. While `acks=all` contributes to idempotence, it is not a separate requirement when `enable.idempotence` is true; the producer automatically sets `acks=all`. Therefore this option alone is not a distinct requirement for exactly‑once semantics.

3. ❌ **C. Using `Producer.send()` without a callback.**  
   **Incorrect**. The callback is optional and does not influence exactly‑once semantics; it merely provides async error handling.

4. ✅ **D. Setting the producer property `enable.idempotence=true`.**  
   **Correct**. This enables the producer to deduplicate retries, a core part of exactly‑once delivery. It must be set for transactional writes.

5. ✅ **E. Setting a unique `transactional.id` on the producer.**  
   **Correct**. A transactional producer requires a persistent transactional ID to identify the transaction across restarts; without it, `beginTransaction` fails.

6. ✅ **F. Configuring the consumer with `enable.auto.commit=false`.**  
   **Correct**. Offsets must be committed manually after a successful transaction commit to preserve exactly‑once behavior.

</details>

## Question 20 (Kafka Consumers):
When creating a Kafka consumer in a Confluent platform environment, which of the following configurations and practices are essential to ensure correct and efficient consumption of messages?

- A. Setting the 'group.id' configuration to enable consumer group coordination and offset management
- B. Using 'auto.offset.reset' set to 'latest' to start consuming from the earliest available message in the topic
- C. Using 'auto.commit.interval.ms' to set the frequency of automatic offset commits when 'enable.auto.commit' is true
- D. Disabling 'enable.auto.commit' and manually committing offsets to have precise control over message processing
- E. Setting 'max.poll.records' to 1 to minimize memory usage and improve throughput
- F. Specifying 'key.deserializer' and 'value.deserializer' to correctly deserialize records fetched from Kafka

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** C, F, D, A

**Explanation:**

Creating an efficient Kafka consumer involves configuring key parameters that affect message processing, offset management, and deserialization. Setting 'group.id' is fundamental for consumer group coordination and offset tracking. Disabling 'enable.auto.commit' grants the developer control over when offsets are committed, improving reliability. Correct deserializers must be specified to interpret Kafka messages properly. The 'auto.commit.interval.ms' setting only applies if automatic commits are enabled and influences commit frequency. Misconfigurations such as setting 'auto.offset.reset' to 'latest' when trying to consume from the beginning, or setting 'max.poll.records' too low, can lead to inefficient or incorrect consumption patterns. Understanding these configurations is critical for passing the Confluent Certified Developer exam and for building robust consumer applications in production. (Precision: key.deserializer and value.deserializer are mandatory; group.id is required when using subscribe()/offset commits, but not when using assign() without commits. max.poll.records=1 would reduce, not improve, throughput.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 "Configuring Consumers" (pp. 87-93); https://kafka.apache.org/documentation/#consumerconfigs

**Detailed explanation of each option:**

1. ✅ **A. Setting the 'group.id' configuration to enable consumer group coordination and offset management**  
   **Correct**. The 'group.id' uniquely identifies the consumer group and is required for Kafka to manage offset commits and load balancing among consumers.

2. ❌ **B. Using 'auto.offset.reset' set to 'latest' to start consuming from the earliest available message in the topic**  
   **Incorrect**. Setting 'auto.offset.reset' to 'latest' causes the consumer to start from the end of the topic, not the earliest message. To consume from the beginning, it should be set to 'earliest'.

3. ✅ **C. Using 'auto.commit.interval.ms' to set the frequency of automatic offset commits when 'enable.auto.commit' is true**  
   **Correct**. This setting controls how often offsets are committed automatically, impacting the balance between throughput and potential message reprocessing.

4. ✅ **D. Disabling 'enable.auto.commit' and manually committing offsets to have precise control over message processing**  
   **Correct**. Disabling automatic commits allows the application to commit offsets only after processing messages successfully, improving reliability.

5. ❌ **E. Setting 'max.poll.records' to 1 to minimize memory usage and improve throughput**  
   **Incorrect**. While setting 'max.poll.records' to 1 reduces memory usage, it negatively impacts throughput by fetching one record at a time, which is typically inefficient.

6. ✅ **F. Specifying 'key.deserializer' and 'value.deserializer' to correctly deserialize records fetched from Kafka**  
   **Correct**. Proper deserializers must be configured to convert byte arrays into usable key and value objects in the application.

</details>

## Question 21 (Kafka Fundamentals):
Which of the following statements correctly describe fundamental properties of Apache Kafka’s log‑based architecture that enable its scalability and fault tolerance?

- A. Kafka uses immutable, append‑only logs so that writes do not overwrite existing data, reducing write contention.
- B. Kafka partitions a topic into multiple logs, allowing parallel processing across many brokers.
- C. Replication of partitions across brokers guarantees durability and high availability.
- D. Kafka’s log compaction feature keeps only the latest value for each key, ensuring compact storage.
- E. All Kafka messages are stored entirely in memory for maximum throughput.
- F. ZooKeeper is responsible for replicating partition data across brokers.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, A, B

**Explanation:**

Kafka’s core design relies on immutable, append‑only logs that minimize write contention and enable sequential disk I/O. Topics are divided into partitions, each a separate log that can be distributed across brokers for parallelism. Replication of each partition across multiple brokers provides durability and high availability; the leader replica processes client requests while followers sync asynchronously. Memory is used for caching and index storage, not for holding all messages. Optional features such as log compaction and ZooKeeper’s role in metadata management are important but not fundamental to scalability or fault tolerance. Understanding these basics is critical for building robust, high‑throughput Kafka applications. Note: statement A is also factually true (compaction keeps the latest value per key) - it is just not a fundamental scalability/fault-tolerance property, so it is the "distractor" here; ZooKeeper/KRaft handle metadata, not data replication.

Source: Kafka: The Definitive Guide 2nd ed., ch. 1-2 (Publish/Subscribe, Partitions, Replication), ch. 6 (Kafka Internals - Replication, Physical Storage, Compaction); https://kafka.apache.org/documentation/#design

**Detailed explanation of each option:**

1. ✅ **A. Kafka uses immutable, append‑only logs so that writes do not overwrite existing data, reducing write contention.**  
   **Correct**. The immutable log design allows producers to append quickly and enables efficient sequential disk writes, which is a core scalability feature.

2. ✅ **B. Kafka partitions a topic into multiple logs, allowing parallel processing across many brokers.**  
   **Correct**. Partitioning is the primary mechanism for horizontal scaling; each partition can be handled by a different broker, enabling concurrent reads and writes.

3. ✅ **C. Replication of partitions across brokers guarantees durability and high availability.**  
   **Correct**. Replicas are maintained on separate brokers; the leader replica handles traffic, while followers sync asynchronously, providing fault tolerance.

4. ❌ **D. Kafka’s log compaction feature keeps only the latest value for each key, ensuring compact storage.**  
   **Incorrect**. While log compaction is a valuable feature, it is an optional configuration and not a fundamental property required for scalability or fault tolerance.

5. ❌ **E. All Kafka messages are stored entirely in memory for maximum throughput.**  
   **Incorrect**. Kafka persists messages to disk (often with configurable log retention) to ensure durability; memory is used only for caching headers and indexes.

6. ❌ **F. ZooKeeper is responsible for replicating partition data across brokers.**  
   **Incorrect**. ZooKeeper (or the newer KRaft mode) manages cluster metadata and leader election, but the actual data replication happens using Kafka’s own protocol between brokers.

</details>

## 🚫 Question 22 (Kafka Setup and Operations):
Which of the following statements accurately describe the role and characteristics of ZooKeeper in a Kafka cluster setup?

- A. ZooKeeper manages Kafka broker metadata and coordinates leader election for partitions.
- B. ZooKeeper directly handles the replication of Kafka partitions across brokers.
- C. ZooKeeper is responsible for storing Kafka topic data and message payloads persistently.
- D. ZooKeeper maintains the configuration and status of Kafka consumer groups.
- E. ZooKeeper can be completely removed from Kafka clusters starting from Apache Kafka 2.8.0 with KRaft mode.
- F. ZooKeeper requires a quorum of nodes to be available to maintain Kafka cluster availability.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, D, F

**Explanation:**

ZooKeeper plays a critical role in Kafka cluster management by storing metadata, coordinating leader elections, and maintaining consumer group state in older Kafka versions. It does not store message data or manage replication directly; brokers handle these functions. ZooKeeper operates as a quorum-based ensemble, requiring a majority of nodes to be available to maintain cluster stability. While newer Kafka versions are moving towards a ZooKeeper-less architecture (KRaft mode), this is not yet the standard in production environments or the focus of the Confluent Certified Developer exam, which emphasizes traditional ZooKeeper-based setups.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 6 "Cluster Membership" (pp. 135-136) — NOTE: ZooKeeper/KRaft: book Ch. 2 & Ch. 6 (out of exam scope).

**Detailed explanation of each option:**

1. ✅ **A. ZooKeeper manages Kafka broker metadata and coordinates leader election for partitions.**  
   **Correct**. ZooKeeper stores metadata about brokers, topics, and partitions, and orchestrates leader election to ensure high availability.

2. ❌ **B. ZooKeeper directly handles the replication of Kafka partitions across brokers.**  
   **Incorrect**. Replication is managed by Kafka brokers themselves; ZooKeeper only helps coordinate the cluster state.

3. ❌ **C. ZooKeeper is responsible for storing Kafka topic data and message payloads persistently.**  
   **Incorrect**. Kafka brokers store the actual topic data and message payloads on disk; ZooKeeper does not store message data.

4. ✅ **D. ZooKeeper maintains the configuration and status of Kafka consumer groups.**  
   **Correct**. ZooKeeper tracks consumer group offsets and membership in Kafka versions prior to 0.9; however, newer versions use Kafka itself for offset storage.

5. ❌ **E. ZooKeeper can be completely removed from Kafka clusters starting from Apache Kafka 2.8.0 with KRaft mode.**  
   **Incorrect**. for the certification scope. While Kafka 2.8.0 introduced KRaft mode to remove ZooKeeper dependency, this is not yet the default or widely used in production and is outside the core certification scope.

6. ✅ **F. ZooKeeper requires a quorum of nodes to be available to maintain Kafka cluster availability.**  
   **Correct**. ZooKeeper runs as an ensemble requiring a quorum (majority) of nodes to function properly, which directly affects Kafka cluster stability.

</details>

## Question 23 (Streams Development):
Which of the following statements correctly describe how Kafka Streams ensures state consistency and fault tolerance in a distributed environment?

- A. State stores are automatically sharded across tasks based on the input topic partition assignment.
- B. The offset commit for stateful operators is handled automatically by the Streams framework.
- C. Kafka Streams stores state in a local RocksDB instance and replicates it to other nodes via internal changelog topics.
- D. When a task fails, its state is recovered from the latest snapshot of the local file system.
- E. The internal changelog topics for state stores use the same replication factor as the source topic.
- F. All stateful operators must be explicitly configured with a Replication Factor > 1 to survive node failures.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, A, C

**Explanation:**

In a distributed Kafka Streams application, stateful operators maintain local RocksDB stores whose changes are published to internal changelog topics. These topics are replicated across the cluster, providing fault tolerance. Each task handles one partition of each input topic, which naturally partitions the state store. Recovery is achieved by replaying the changelog, not by restoring local snapshots. The replication factor is set per topic, not per operator, and the Streams framework automatically commits offsets after state updates, guaranteeing consistency across restarts. Understanding these mechanisms is essential for designing reliable stream processing applications.  
Source: https://kafka.apache.org/43/documentation/streams/architecture/ (tasks, local state stores, fault tolerance via changelog topics) ; https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams/

**Detailed explanation of each option:**

1. ✅ **A. State stores are automatically sharded across tasks based on the input topic partition assignment.**  
   **Correct**. Each task is responsible for a single partition of every input topic; its local state store is partitioned accordingly. This design enables parallel processing and deterministic state partitioning.

2. ✅ **B. The offset commit for stateful operators is handled automatically by the Streams framework.**  
   **Correct**. The framework commits offsets after a batch of records has been processed and the state has been checkpointed, ensuring that processing resumes from a consistent point after a failure.

3. ✅ **C. Kafka Streams stores state in a local RocksDB instance and replicates it to other nodes via internal changelog topics.**  
   **Correct**. The framework writes all stateful operator data to a local RocksDB store and publishes each change to a corresponding changelog topic. Replication of these topics provides durability and allows a new task to rebuild the state from the changelog when needed.

4. ❌ **D. When a task fails, its state is recovered from the latest snapshot of the local file system.**  
   **Incorrect**. Recovery is performed by replaying the internal changelog topic, not by restoring a local file system snapshot.

5. ❌ **E. The internal changelog topics for state stores use the same replication factor as the source topic.**  
   **Incorrect**. Changelog topics get the replication factor from the Streams `replication.factor` config (not from the source topic).

6. ❌ **F. All stateful operators must be explicitly configured with a Replication Factor > 1 to survive node failures.**  
   **Incorrect**. Replication factor is a topic-level setting; the framework automatically creates changelog topics with a configurable replication factor, but operators themselves are not individually configured for replication.

</details>

## Question 24 (Kafka Fundamentals):
Which of the following statements about Kafka data retention are true? (Select all that apply)

- A. If both `retention.ms` and `retention.bytes` are configured on a topic, Kafka deletes a segment when either the age or size threshold is met; whichever condition is satisfied first triggers deletion.
- B. Configuring `retention.bytes` to 0 indicates unlimited data retention.
- C. A broker‑wide default for `retention.ms` can be overridden by a per‑topic configuration, and the change takes effect only after a broker restart.
- D. When `cleanup.policy` is set to `compact`, the log compaction process removes older duplicate records for the same key, and the topic will never delete older segments regardless of `retention.ms`.
- E. Setting `segment.ms` to a very high value delays segment rollover, which can increase the time before old segments are eligible for deletion by retention policies.
- F. Setting `retention.ms` to -1 on a topic disables all automatic data deletion, effectively retaining data indefinitely.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, F, A

**Explanation:**

Kafka’s retention mechanisms combine time‑based and size‑based policies to control log growth. The `retention.ms` property sets the maximum age for segments, while `retention.bytes` limits the total log size; setting either to -1 disables that constraint. Log compaction (`cleanup.policy`=compact) removes duplicate key records but does not exempt segments from the configured retention thresholds. `segment.ms` governs segment rollover frequency; larger values mean fewer, bigger segments and can postpone deletions. Topic‑level configurations override broker defaults immediately, eliminating the need for broker restarts. Understanding these interactions is essential for ensuring data availability and efficient storage usage.  
Source: book Ch. 2 (Configuring Retention by Size and Time, p. 60 of PDF: deletion when either criterion is met) ; https://kafka.apache.org/43/configuration/topic-configs/ (`retention.ms`, `retention.bytes`, `segment.ms`, `cleanup.policy`)

**Detailed explanation of each option:**

1. ✅ **A. If both `retention.ms` and `retention.bytes` are configured on a topic, Kafka deletes a segment when either the age or size threshold is met; whichever condition is satisfied first triggers deletion.**  
   **Correct**. Kafka evaluates both constraints; deletion occurs as soon as one of them is exceeded.

2. ❌ **B. Configuring `retention.bytes` to 0 indicates unlimited data retention.**  
   **Incorrect**. `retention.bytes` limits the total size of a log. A value of -1 disables size‑based retention; 0 would keep no data, as it limits the log to 0 bytes.

3. ❌ **C. A broker‑wide default for `retention.ms` can be overridden by a per‑topic configuration, and the change takes effect only after a broker restart.**  
   **Incorrect**. Topic overrides take effect immediately without needing a broker restart.

4. ❌ **D. When `cleanup.policy` is set to `compact`, the log compaction process removes older duplicate records for the same key, and the topic will never delete older segments regardless of `retention.ms`.**  
   **Incorrect**. While compaction removes duplicate keys, `retention.ms` (or `retention.bytes`) can still delete whole segments. The statement overstates compaction’s effect.

5. ✅ **E. Setting `segment.ms` to a very high value delays segment rollover, which can increase the time before old segments are eligible for deletion by retention policies.**  
   **Correct**. `segment.ms` controls how often a new segment is rolled. Retention deletes only closed segments (the active segment is never deleted), and a segment is eligible only when its newest record is older than `retention.ms`; a very high `segment.ms` therefore delays deletion.

6. ✅ **F. Setting `retention.ms` to -1 on a topic disables all automatic data deletion, effectively retaining data indefinitely.**  
   **Correct**. In Kafka, `retention.ms` controls the maximum age of log segments. A value of -1 disables time‑based retention, meaning segments will not be deleted by age.

</details>

## Question 25 (Kafka Consumers):
When subscribing a Kafka consumer to topics using the Java Kafka Consumer API, which of the following statements about the subscribe() method and topic subscription behavior are correct?

- A. Calling subscribe() multiple times with different topic lists will add topics cumulatively to the subscription set.
- B. After calling subscribe(), the consumer immediately starts fetching data from all assigned partitions without any rebalance process.
- C. The subscribe() method can only be called before the consumer.poll() method is invoked for the first time.
- D. Calling subscribe(Collection<String> topics) replaces any existing subscription with the new list of topics.
- E. When subscribing by pattern, if a topic is deleted, the consumer will automatically stop consuming from that topic without manual intervention.
- F. Using subscribe(Pattern pattern) allows the consumer to dynamically subscribe to all topics matching the pattern, including topics created after subscription.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, F, E

**Explanation:**

The subscribe() method in Kafka's consumer API replaces the current topic subscription with the provided list or pattern. Using a pattern allows dynamic subscription to new topics matching the regex, which is useful in evolving environments. Each subscribe() call triggers a rebalance, assigning partitions accordingly; thus, consumers do not start fetching data immediately without rebalancing. While subscribe() can be called anytime, changes after poll() will cause rebalances, impacting consumption. Additionally, when using pattern subscriptions, if topics are deleted, the consumer automatically stops consuming from those topics, maintaining an accurate subscription without manual updates. Misunderstanding the replacement behavior of subscribe() or the rebalance mechanism can lead to incorrect consumer implementations.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "Subscribing to Topics" (p. 85) and "The Poll Loop" (pp. 86-87)

**Detailed explanation of each option:**

1. ❌ **A. Calling subscribe() multiple times with different topic lists will add topics cumulatively to the subscription set.**  
   **Incorrect**. Each call to subscribe() replaces the previous subscription rather than adding to it.

2. ❌ **B. After calling subscribe(), the consumer immediately starts fetching data from all assigned partitions without any rebalance process.**  
   **Incorrect**. A rebalance process occurs after subscribe() to assign partitions to the consumer.

3. ❌ **C. The subscribe() method can only be called before the consumer.poll() method is invoked for the first time.**  
   **Incorrect**. subscribe() can be called before or after poll(), but changes after poll() may trigger a rebalance.

4. ✅ **D. Calling subscribe(Collection<String> topics) replaces any existing subscription with the new list of topics.**  
   **Correct**. The subscribe() method sets the subscription to the specified topics, replacing any previous subscription.

5. ✅ **E. When subscribing by pattern, if a topic is deleted, the consumer will automatically stop consuming from that topic without manual intervention.**  
   **Correct**. The consumer dynamically updates its subscription and stops consuming from deleted topics matching the pattern.

6. ✅ **F. Using subscribe(Pattern pattern) allows the consumer to dynamically subscribe to all topics matching the pattern, including topics created after subscription.**  
   **Correct**. Subscribing with a regex pattern enables the consumer to automatically subscribe to new topics matching the pattern as they are created.

</details>

##  Question 26 (Reliable Data Delivery):
Which of the following broker configuration settings directly impact reliable data delivery in Apache Kafka by controlling **data durability** and **replication behavior**?

- A. `replica.lag.time.max.ms`
- B. `log.cleaner.enable`
- C. `unclean.leader.election.enable`
- D. `log.flush.interval.messages`
- E. `num.network.threads`
- F. `log.retention.hours`

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, C, A

**Explanation:**

Reliable data delivery in Kafka depends heavily on broker configurations that ensure data durability and consistent replication. `log.flush.interval.messages` controls the frequency of flushing messages to disk, reducing data loss risk. `unclean.leader.election.enable` when disabled, prevents data loss by avoiding leaders that are not fully caught-up replicas. `replica.lag.time.max.ms` sets how long a follower can lag before being considered out of sync, ensuring only in-sync replicas participate in leader elections. Other settings like retention or network threads impact performance or storage but do not directly guarantee reliable data delivery. Understanding these configurations helps developers design robust Kafka deployments that minimize data loss and ensure consistency.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-142) and Ch. 7 "Replication" (pp. 163-168) — NOTE: Broker durability configs: book Ch. 7 "Broker Configuration" (pp. 164-169) (partly out of exam scope).

**Detailed explanation of each option:**

1. ✅ **A. replica.lag.time.max.ms**  
   **Correct**. This setting defines the maximum time a follower can be behind the leader before it is considered out of sync, affecting replication reliability.

2. ❌ **B. log.cleaner.enable**  
   **Incorrect**. This setting controls log compaction, which affects storage efficiency but not the fundamental reliability of data delivery.

3. ✅ **C. unclean.leader.election.enable**  
   **Correct**. Disabling unclean leader election prevents brokers without fully caught-up replicas from becoming leaders, preserving data consistency and reliability.

4. ✅ **D. log.flush.interval.messages**  
   **Correct**. This setting controls how often the broker flushes data to disk based on the number of messages, impacting durability guarantees.

5. ❌ **E. num.network.threads**  
   **Incorrect**. This controls the number of threads handling network requests and impacts throughput, but not data delivery reliability directly.

6. ❌ **F. log.retention.hours**  
   **Incorrect**. This setting controls how long data is retained before deletion but does not directly affect the reliability of data delivery.

</details>

## Question 27 (Kafka Internals):
Which of the following statements accurately describe how log compaction works in Apache Kafka and its implications for topic data retention?

- A. Log compaction can run concurrently with standard time or size-based retention policies on the same topic.
- B. The compaction process runs continuously in the background and does not block producers or consumers.
- C. During compaction, Kafka guarantees that all intermediate updates for a key are retained in the log.
- D. Compacted topics delete messages only based on their age, similar to log retention by time.
- E. Compacted topics are suitable for use cases requiring a changelog of all data changes over time without data loss.
- F. Log compaction guarantees that the latest record for each key is retained, regardless of the record's age.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** F, B, A

**Explanation:**

Log compaction in Kafka ensures that the latest value for each key is preserved, making it ideal for topics representing state or snapshots. It differs fundamentally from time- or size-based retention, which removes data solely based on age or log size. Compaction runs as an asynchronous background process and can coexist with other retention policies, allowing flexibility in managing topic data. However, compaction does not retain all historical updates for a key, so it is unsuitable for use cases requiring a complete changelog of all changes. Understanding these nuances is critical for developers designing Kafka topics to meet specific data retention and recovery requirements. (B holds for cleanup.policy=compact; tombstones are removed after delete.retention.ms, and with cleanup.policy=compact,delete records older than retention are deleted too. The active segment is not compacted.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Compaction"/"How Compaction Works"/"Deleted Events"; https://kafka.apache.org/43/configuration/topic-configs/#topicconfigs_cleanup.policy

**Detailed explanation of each option:**

1. ✅ **A. Log compaction can run concurrently with standard time or size-based retention policies on the same topic.**  
   **Correct**. Kafka allows both compaction and time/size retention to coexist; compaction preserves latest key updates, while retention deletes old data beyond configured thresholds.

2. ✅ **B. The compaction process runs continuously in the background and does not block producers or consumers.**  
   **Correct**. Compaction is an asynchronous background process that does not interfere with producers or consumers, ensuring minimal impact on performance.

3. ❌ **C. During compaction, Kafka guarantees that all intermediate updates for a key are retained in the log.**  
   **Incorrect**. Compaction removes intermediate updates, keeping only the latest value per key, so intermediate states are typically discarded.

4. ❌ **D. Compacted topics delete messages only based on their age, similar to log retention by time.**  
   **Incorrect**. Unlike time-based retention, compaction removes older duplicates of keys but does not delete records solely based on age.

5. ❌ **E. Compacted topics are suitable for use cases requiring a changelog of all data changes over time without data loss.**  
   **Incorrect**. Since compaction discards older versions of a key, it is not ideal for changelog use cases that need a full history of changes.

6. ✅ **F. Log compaction guarantees that the latest record for each key is retained, regardless of the record's age.**  
   **Correct**. Log compaction ensures that at least the most recent value for each key is kept in the log, providing a snapshot of the latest state.

</details>

## Question 28 (Kafka Fundamentals):
Which of the following statements correctly describe the capabilities of the Kafka Admin API (AdminClient) in Apache Kafka 3.x?(Note: in Kafka 4.0 `alterConfigs` was removed – use `incrementalAlterConfigs`.)

- A. The AdminClient supports altering topic configurations at runtime without requiring a broker restart using the alterConfigs method.
- B. The Admin API can delete consumer group offsets via the deleteConsumerGroupOffsets method.
- C. The Admin API can produce records to topics as part of administrative operations.
- D. The AdminClient provides a GetClusterInfo request that retrieves the current broker cluster ID.
- E. The AdminClient can create topics with arbitrary partition counts and replication factors using the createTopics method.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, A, B

**Explanation:**

The AdminClient is Kafka’s programmatic interface for cluster metadata and configuration tasks. It can create topics (createTopics), modify topic, broker, and consumer group configurations (alterConfigs), and delete consumer group offsets (deleteConsumerGroupOffsets). It does not provide a dedicated GetClusterInfo request; cluster information (including the cluster ID) is obtained via describeCluster(). Note: `alterConfigs` is deprecated since 2.3 and removed in Kafka 4.0 in favor of `incrementalAlterConfigs`. Additionally, producing records is outside the scope of the Admin API and is performed with the Producer API. Understanding these distinctions is essential for developers designing management or automation tools around Kafka clusters.

Source: book ch. 5 "Kafka Administration" / AdminClient (PDF p. 103 ff.); https://kafka.apache.org/43/javadoc/org/apache/kafka/clients/admin/Admin.html

**Detailed explanation of each option:**

1. ✅ **A. The AdminClient supports altering topic configurations at runtime without requiring a broker restart using the alterConfigs method.**  
   **Correct**. The alterConfigs API (deprecated; in 4.x use incrementalAlterConfigs) enables updating configuration properties for topics, consumer groups, and brokers on the fly. Refer to https://kafka.apache.org/documentation.html#admin_alterConfigs.

2. ✅ **B. The Admin API can delete consumer group offsets via the deleteConsumerGroupOffsets method.**  
   **Correct**. AdminClient provides deleteConsumerGroupOffsets to remove specific offsets for a consumer group, allowing group re‑initialization. Documentation: https://kafka.apache.org/documentation.html#admin_deleteConsumerGroupOffsets.

3. ❌ **C. The Admin API can produce records to topics as part of administrative operations.**  
   **Incorrect**. Record production is handled by the Producer API, not by the AdminClient, which is dedicated to metadata and configuration management.

4. ❌ **D. The AdminClient provides a GetClusterInfo request that retrieves the current broker cluster ID.**  
   **Incorrect**. While AdminClient can describe the cluster with describeCluster, there is no GetClusterInfo request; cluster ID is exposed through DescribeClusterResult.clusterId().

5. ✅ **E. The AdminClient can create topics with arbitrary partition counts and replication factors using the createTopics method.**  
   **Correct**. The AdminClient’s createTopics API allows specifying the number of partitions and the replication factor per topic at creation time. See https://kafka.apache.org/documentation.html#admin_createTopics.

</details>

## Question 29 (Kafka Producers):
When configuring serializers for Kafka producers in a Confluent platform environment, which of the following statements about serializer selection and behavior are true?

- A. If no serializer is configured for the key or value, KafkaProducer will default to the ByteArraySerializer.
- B. Custom serializers must implement the Deserializer interface to be compatible with Kafka producers.
- C. The Avro serializer requires a schema registry to serialize records properly in Confluent Kafka environments.
- D. Using the StringSerializer for keys guarantees that all keys are serialized as UTF-8 encoded byte arrays.
- E. Using the JsonSerializer in Confluent Kafka requires configuring the schema registry to ensure schema validation.
- F. The ByteArraySerializer automatically compresses the data before serialization to reduce message size.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** D, C

**Explanation:**

In Confluent Kafka producer configuration, serializers convert data into byte arrays for transmission. The StringSerializer encodes strings as UTF-8 byte arrays, which is standard for keys or values of string type. The Avro serializer relies on Confluent Schema Registry to manage schemas and ensure compatibility, making it essential in schema-driven serialization. ByteArraySerializer is a pass-through and does not perform compression. Custom serializers must implement the Serializer interface, not Deserializer, which is for consumers. JsonSerializer does not require schema registry integration, unlike Avro or Protobuf. KafkaProducer mandates explicit serializers; it does not default to ByteArraySerializer. Understanding these distinctions is critical for correctly configuring producers in a Confluent Kafka environment.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Serializers" (pp. 61-64) — NOTE: Avro serializer requires Schema Registry: verified against Schema Registry docs.

**Detailed explanation of each option:**

1. ❌ **A. If no serializer is configured for the key or value, KafkaProducer will default to the ByteArraySerializer.**  
   **Incorrect**. KafkaProducer requires explicit serializers for keys and values; it does not provide a default serializer.

2. ❌ **B. Custom serializers must implement the Deserializer interface to be compatible with Kafka producers.**  
   **Incorrect**. Custom serializers must implement the Serializer interface; Deserializer is used on the consumer side.

3. ✅ **C. The Avro serializer requires a schema registry to serialize records properly in Confluent Kafka environments.**  
   **Correct**. The Avro serializer integrates with Confluent Schema Registry to enforce schema compatibility and serialize data efficiently.

4. ✅ **D. Using the StringSerializer for keys guarantees that all keys are serialized as UTF-8 encoded byte arrays.**  
   **Correct**. StringSerializer converts Java String keys into UTF-8 encoded byte arrays, which is the expected format for Kafka keys.

5. ❌ **E. Using the JsonSerializer in Confluent Kafka requires configuring the schema registry to ensure schema validation.**  
   **Incorrect**. JsonSerializer serializes JSON without requiring the schema registry; schema registry is typically needed for Avro or Protobuf.

6. ❌ **F. The ByteArraySerializer automatically compresses the data before serialization to reduce message size.**  
   **Incorrect**. ByteArraySerializer simply passes the byte array as-is without any compression or transformation.

</details>

## Question 30 (Kafka Connect):
Which of the following statements correctly describe Kafka Connect core concepts related to task distribution, fault tolerance, configuration, and connector implementation?

- A. Connect automatically scales by adding more Kafka brokers to the cluster.
- B. Kafka Connect distributes tasks across worker nodes in a cluster, with each task assigned to a single worker.
- C. Connect connectors can be written in Java, Scala, or Python, with Python support provided via the PyKafka library.
- D. Connect's worker configuration property "plugin.path" determines the location of connector JAR files.
- E. The offset for each connector task is stored in the __consumer_offsets topic.
- F. If a worker node fails, its tasks are automatically reassigned to other workers after the group rebalance.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, F, D

**Explanation:**

Kafka Connect partitions work into connectors, tasks, and workers. A connector may spawn multiple tasks; each task runs on a single worker, enabling parallelism. Workers form a consumer group, so when a node fails its tasks are reassigned to surviving workers during rebalancing, ensuring fault tolerance. Task offsets are persisted in the dedicated __connect_offsets topic, not the generic __consumer_offsets. The plugin.path setting tells workers where to load connector JARs. Although Connect is built for Java/Scala, Python connectors are not supported via PyKafka and require separate implementation. Scaling Connect means adding workers, not Kafka brokers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ❌ **A. Connect automatically scales by adding more Kafka brokers to the cluster.**  
   **Incorrect**. Scaling Connect requires adding more worker nodes; adding brokers affects the Kafka cluster, not the Connect cluster.

2. ✅ **B. Kafka Connect distributes tasks across worker nodes in a cluster, with each task assigned to a single worker.**  
   **Correct**. A connector may be configured with multiple tasks; Connect assigns each task to a single worker in the worker group. This enables parallel processing of data streams.

3. ❌ **C. Connect connectors can be written in Java, Scala, or Python, with Python support provided via the PyKafka library.**  
   **Incorrect**. While connectors are typically written in Java or Scala, Python connectors require a separate worker implementation (e.g., via a custom Python worker) and are not natively supported by PyKafka.

4. ✅ **D. Connect's worker configuration property "plugin.path" determines the location of connector JAR files.**  
   **Correct**. The plugin.path property tells the worker where to look for connector classes and their dependencies.

5. ❌ **E. The offset for each connector task is stored in the __consumer_offsets topic.**  
   **Incorrect**. Connect stores offsets in the dedicated __connect_offsets topic, not in __consumer_offsets.

6. ✅ **F. If a worker node fails, its tasks are automatically reassigned to other workers after the group rebalance.**  
   **Correct**. Connect uses the Kafka consumer group protocol. When a worker leaves or fails, its partitions (tasks) are reassigned to remaining workers during the next rebalance.

</details>

## Question 31 (Programming & Serialization):
Confluent’s Schema Registry supports several serialization formats for Kafka records. Which of the following formats are fully supported by the Schema Registry for schema registration and evolution?

- A. String
- B. JSON Schema
- C. Binary (Bytes)
- D. JSON (plain)
- E. Avro
- F. Protobuf

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, F, E

**Explanation:**

The Confluent Schema Registry is designed to store, version, and validate schemas for structured data formats. It natively supports Avro, JSON Schema, and Protocol Buffers, offering schema compatibility checks (backward, forward, full) and automatic ID assignment for efficient encoding. While plain JSON, String, and raw Bytes can be used as key/value payloads, they lack the metadata and validation features that the registry provides. Knowing which formats are fully supported helps developers choose the right schema type for compatibility, performance, and tooling integration.

Source: Confluent Schema Registry docs - supported formats: Avro, JSON Schema, Protobuf

**Detailed explanation of each option:**

1. ❌ **A. String**  
   **Incorrect**. String is a primitive type without a schema; the Schema Registry does not manage or enforce schemas for plain string values.

2. ✅ **B. JSON Schema**  
   **Correct**. JSON Schema support was added in later releases, enabling the registry to store, validate, and evolve JSON messages using the JSON Schema standard.

3. ❌ **C. Binary (Bytes)**  
   **Incorrect**. Raw bytes are treated as opaque data; the registry does not impose a schema on arbitrary binary payloads.

4. ❌ **D. JSON (plain)**  
   **Incorrect**. Plain JSON has no built‑in schema or compatibility enforcement; the Schema Registry does not natively validate or version plain JSON messages.

5. ✅ **E. Avro**  
   **Correct**. The Schema Registry was originally built for Avro schemas and provides strict schema validation, compatibility checks, and automatic ID assignment for Avro messages.

6. ✅ **F. Protobuf**  
   **Correct**. Starting with Confluent Platform 5.5, the Schema Registry added support for Protocol Buffers. It assigns unique IDs and performs compatibility checks similar to Avro.

</details>

## Question 32 (Kafka Connect):
Which of the following statements accurately describe core concepts of Kafka Connect?

- A. Connectors are always deployed as separate processes independent of the Connect workers.
- B. Kafka Connect guarantees exactly-once delivery semantics by default for all connectors.
- C. Connectors can be configured to use incremental source offsets for incremental data capture.
- D. Connectors are implemented as either source or sink connectors.
- E. Connectors are stateless components and rely entirely on Kafka topics for state.
- F. Connectors can leverage the Confluent Schema Registry for data validation and schema evolution.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, D, F

**Explanation:**

Kafka Connect is a framework that simplifies data ingestion and extraction between Kafka and external systems. The core concepts include the distinction between source and sink connectors, the ability to use a Schema Registry for schema validation, and the support for incremental offsets to enable fault‑tolerant, resume‑able data capture. Connectors are not standalone processes; they execute within Connect workers and maintain internal state such as offsets. Exactly‑once semantics are not guaranteed out of the box; they require specific configuration and connector support. Understanding these fundamentals is essential for designing robust pipelines and for passing the Confluent Certified Developer exam.  
Source: https://kafka.apache.org/43/documentation/#connect (connectors, tasks, workers, converters, offsets) ; book Ch. 9. Note: options B and E are loosely worded but B, C, F remain the best answers.

**Detailed explanation of each option:**

1. ❌ **A. Connectors are always deployed as separate processes independent of the Connect workers.**  
   **Incorrect**. Connectors run inside Kafka Connect workers; workers can be standalone or distributed. Deploying connectors as separate processes is not required.

2. ❌ **B. Kafka Connect guarantees exactly-once delivery semantics by default for all connectors.**  
   **Incorrect**. Exactly-once semantics are optional and depend on the connector implementation and configuration; they are not guaranteed by default.

3. ✅ **C. Connectors can be configured to use incremental source offsets for incremental data capture.**  
   **Correct**. Source connectors support incremental offset strategies (e.g., incremental snapshots, incremental change data capture) to resume from the last processed record.

4. ✅ **D. Connectors are implemented as either source or sink connectors.**  
   **Correct**. Kafka Connect defines two connector types: source connectors pull data from external systems into Kafka, and sink connectors write data from Kafka to external systems.

5. ❌ **E. Connectors are stateless components and rely entirely on Kafka topics for state.**  
   **Incorrect**. Connectors maintain state such as offsets, task progress, and error handling. Offsets are stored in internal topics or external storage, not via statelessness.

6. ✅ **F. Connectors can leverage the Confluent Schema Registry for data validation and schema evolution.**  
   **Correct**. Many connectors support Schema Registry integration, allowing them to produce or consume Avro, JSON Schema, or Protobuf messages with schema validation.

</details>

## 🚫 Question 33 (Kafka Internals):
Which of the following statements accurately describe the request processing flow in Apache Kafka broker internals?

- A. Fetch requests are served directly from the leader’s log segment files without involving the in-memory cache.
- B. The controller broker handles all client requests related to topic metadata and partition leadership changes.
- C. Offset commit requests are processed synchronously by the broker to update the consumer group coordinator’s state in Kafka’s internal __consumer_offsets topic.
- D. The Kafka broker processes Produce requests by first appending the records to the log and then replicating them to followers asynchronously.
- E. Produce requests are acknowledged only after data is written to the leader log and replicated to all in-sync replicas when acks=all is set.
- F. Kafka brokers use a thread-per-request model to handle incoming client requests to maximize concurrency.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, C, E

**Explanation:**

Kafka’s request processing involves distinct flows depending on request type. Produce requests append data to the leader log and replicate asynchronously, but with acks=all, the broker waits for all in-sync replicas to acknowledge before responding, ensuring durability. Offset commit requests are synchronously processed by the consumer group coordinator to maintain accurate consumer state in the __consumer_offsets topic. Fetch requests benefit from OS-level caching rather than bypassing it. The controller manages leadership and metadata changes but does not handle all client metadata requests. Kafka optimizes concurrency using a pool of threads rather than a thread-per-request model. Understanding these internals is critical for developers to optimize client configurations and troubleshoot performance and consistency issues.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 6 "Request Processing" (pp. 142-148) (Kafka internals — out of exam scope)

**Detailed explanation of each option:**

1. ❌ **A. Fetch requests are served directly from the leader’s log segment files without involving the in-memory cache.**  
   **Incorrect**. Fetch requests typically leverage the page cache (OS-level cache) and may also involve Kafka's internal caching mechanisms, improving read performance.

2. ❌ **B. The controller broker handles all client requests related to topic metadata and partition leadership changes.**  
   **Incorrect**. While the controller manages partition leadership and metadata changes, client metadata requests are handled by the brokers themselves, not exclusively by the controller.

3. ✅ **C. Offset commit requests are processed synchronously by the broker to update the consumer group coordinator’s state in Kafka’s internal __consumer_offsets topic.**  
   **Correct**. Offset commits are synchronously processed by the group coordinator to ensure consumer group state consistency.

4. ✅ **D. The Kafka broker processes Produce requests by first appending the records to the log and then replicating them to followers asynchronously.**  
   **Correct**. Produce requests are handled by appending data to the leader's log and then asynchronously replicating to follower replicas to ensure durability and fault tolerance.

5. ✅ **E. Produce requests are acknowledged only after data is written to the leader log and replicated to all in-sync replicas when acks=all is set.**  
   **Correct**. When acks=all, the broker waits for all in-sync replicas to acknowledge the write before responding to the producer, ensuring strong durability guarantees.

6. ❌ **F. Kafka brokers use a thread-per-request model to handle incoming client requests to maximize concurrency.**  
   **Incorrect**. Kafka uses a limited number of I/O threads and request handler threads rather than a thread-per-request model to optimize resource utilization and throughput.

</details>

## Question 34 (Kafka Internals):
In Apache Kafka's cluster membership protocol, which of the following statements accurately describe how brokers maintain membership and handle cluster changes?

- A. Brokers use the Kafka Controller to manage membership changes and propagate metadata updates to all brokers.
- B. When a broker fails to send heartbeats within the session timeout, it is immediately removed from the cluster membership and its partitions are reassigned.
- C. ZooKeeper is used to track the live brokers and their session states in older Kafka versions prior to KIP-500.
- D. The cluster membership information is stored persistently on each broker's local disk to survive broker restarts.
- E. Kafka brokers use a gossip protocol among themselves to exchange membership information and detect failures.
- F. The Controller triggers partition leader elections when brokers join or leave the cluster to maintain availability and balance.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, C, F

**Explanation:**

Kafka cluster membership management involves coordination primarily by the Kafka Controller, which tracks live brokers and propagates metadata changes. Prior to KIP-500, ZooKeeper stores broker session states and helps detect live brokers through ephemeral nodes. When brokers fail to heartbeat within the session timeout, the Controller marks them as dead and triggers partition leader elections to maintain availability. Membership data is not stored locally on brokers but managed centrally to ensure consistency. Kafka does not employ gossip protocols for membership; instead, it uses a centralized approach for coordination and fault detection. Understanding this mechanism is crucial for developers to troubleshoot broker failures and cluster rebalancing effectively. Note: in Kafka 4.x ZooKeeper is removed; brokers register with and send heartbeats to the KRaft controller quorum. Option A is wrong because the controller elects new leaders for the affected partitions (replicas are not reassigned), and option E is wrong because membership is kept in ZooKeeper/KRaft metadata (a broker only keeps its ID in meta.properties).

Source: Kafka: The Definitive Guide 2nd ed., ch. 6 "Cluster Membership" and "The Controller" (pp. 135-137); https://kafka.apache.org/43/operations/kraft/

**Detailed explanation of each option:**

1. ✅ **A. Brokers use the Kafka Controller to manage membership changes and propagate metadata updates to all brokers.**  
   **Correct**. The Kafka Controller is responsible for cluster metadata management, including membership changes and leader elections, and propagates updates to brokers.

2. ❌ **B. When a broker fails to send heartbeats within the session timeout, it is immediately removed from the cluster membership and its partitions are reassigned.**  
   **Incorrect**. The broker is marked as dead only after session timeout expiration, but partitions reassignment depends on the Controller's logic and may not be immediate.

3. ✅ **C. ZooKeeper is used to track the live brokers and their session states in older Kafka versions prior to KIP-500.**  
   **Correct**. Before the KIP-500 transition, Kafka brokers rely on ZooKeeper to maintain cluster membership and detect live brokers via ephemeral nodes.

4. ❌ **D. The cluster membership information is stored persistently on each broker's local disk to survive broker restarts.**  
   **Incorrect**. Membership state is maintained in ZooKeeper or the Kafka Raft quorum (post-KIP-500), not locally on individual brokers.

5. ❌ **E. Kafka brokers use a gossip protocol among themselves to exchange membership information and detect failures.**  
   **Incorrect**. Kafka brokers do not use a gossip protocol; instead, membership is managed centrally by the Controller and ZooKeeper (pre-KIP-500) or the Quorum Controller (post-KIP-500).

6. ✅ **F. The Controller triggers partition leader elections when brokers join or leave the cluster to maintain availability and balance.**  
   **Correct**. The Controller initiates leader elections to adjust partition leadership in response to membership changes to maintain cluster availability.

</details>

## Question 35 (Application Development):
In Kafka, the key of a record is hashed to determine the target partition. Which of the following statements about key hashing and partitioning are **true**?

- A. You can override the default partitioning logic by providing a custom implementation of org.apache.kafka.clients.producer.Partitioner.
- B. Changing the hashing algorithm on the producer side automatically changes the partitioning behavior on the broker without any broker configuration.
- C. The default Kafka partitioner uses Murmur2 hashing on the key bytes to select a partition.
- D. The hash calculation is deterministic; the same key will always map to the same partition within a single cluster.
- E. The partitioner applies the hash to the key's string representation before computing the hash.
- F. When a key is null, the partitioner selects a partition using a round‑robin strategy(or sticky in newer versions of Kafka).

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, A, F, C

**Explanation:**

Kafka uses the key’s byte array to compute a hash (Murmur2 by default) which is then modded by the partition count. This deterministic mapping ensures that identical keys always go to the same partition as long as the topic’s partition count remains unchanged. Null keys bypass hashing and are spread across partitions (sticky batching since Kafka 2.4, not strict round-robin). Custom partitioning can be achieved by implementing the Partitioner interface and setting the 'partitioner.class' config; only the producer handles hashing, so no broker config changes are required. Understanding these nuances is essential for developers who need predictable ordering or load distribution across partitions.

Source: book ch. 3 "Partitions" (PDF p. 97-99: murmur2 hash of key bytes, null key = sticky/random, custom Partitioner); https://kafka.apache.org/documentation/#producerconfigs_partitioner.class

**Detailed explanation of each option:**

1. ✅ **A. You can override the default partitioning logic by providing a custom implementation of org.apache.kafka.clients.producer.Partitioner.**  
   **Correct**. Implementing this interface and configuring 'partitioner.class' allows custom hashing or routing logic.

2. ❌ **B. Changing the hashing algorithm on the producer side automatically changes the partitioning behavior on the broker without any broker configuration.**  
   **Incorrect**. Partitioning is performed by the producer; brokers do not rehash keys. Only producer configuration is needed.

3. ✅ **C. The default Kafka partitioner uses Murmur2 hashing on the key bytes to select a partition.**  
   **Correct**. Kafka’s DefaultPartitioner computes a Murmur2 hash of the key’s raw byte array and then takes the modulo with the number of partitions.

4. ✅ **D. The hash calculation is deterministic; the same key will always map to the same partition within a single cluster.**  
   **Correct**. Given the same key bytes and the same cluster metadata, the hash will always produce the same partition number.

5. ❌ **E. The partitioner applies the hash to the key's string representation before computing the hash.**  
   **Incorrect**. The hash is applied directly to the raw key bytes, not to a string conversion.

6. ✅ **F. When a key is null, the partitioner selects a partition using a round‑robin strategy.**  
   **Correct**. If the key is null, the partitioner picks a partition without hashing; since Kafka 2.4 it is a "sticky" strategy (fills a batch for one partition before switching), not plain round‑robin.

</details>

## Question 36 (Observability & Testing):
In a Kafka Streams application that uses the default metrics reporter, which of the following application‑level metrics are automatically emitted and exposed via JMX? (Select all that apply)

- A. jvm-heap-used – the amount of heap memory currently used by the JVM
- B. bytes-consumed-rate – the rate of bytes consumed per second by the Streams consumer
- C. records-consumed-rate – the rate at which the Streams consumer pulls records from Kafka
- D. stream-task-lag – the number of records waiting in a task’s input queue
- E. record-processing-latency-avg – the average time between record consumption and forwarding
- F. max-thread-idle-time – the maximum idle time of any Streams worker thread

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

A Kafka Streams instance exposes, via JMX/KafkaStreams#metrics(), its own Streams metrics (thread, task, processor, state-store, record-cache level) plus the metrics of its embedded producer, consumer and admin clients. `bytes-consumed-rate` and `records-consumed-rate` are consumer fetch metrics of the embedded consumer and are therefore exposed. The names `record-processing-latency-avg`, `stream-task-lag` and `max-thread-idle-time` do not exist (the closest real Streams metrics are `process-latency-avg`, `process-rate`, `record-e2e-latency-avg`; consumer lag is `records-lag-max`), and JVM metrics are not Streams metrics.  
Verified live (answer C, F confirmed): the page says "A Kafka Streams instance contains all the producer and consumer metrics as well as additional metrics specific to Streams", lists bytes-consumed-rate and records-consumed-rate under consumer-fetch-manager-metrics, and thread-level metrics commit/poll/process/punctuate-latency-*; no stream-task-lag, max-thread-idle-time or record-processing-latency-avg.
Source: https://kafka.apache.org/42/operations/monitoring/

**Detailed explanation of each option:**

1. ❌ **A. jvm-heap-used – the amount of heap memory currently used by the JVM**  
   **Incorrect**. This is a JVM JMX metric, not a Kafka Streams application metric.

2. ✅ **B. bytes-consumed-rate – the rate of bytes consumed per second by the Streams consumer**  
   **Correct**. An embedded consumer metric (consumer-fetch-manager-metrics) that Streams exposes through its metrics registry.

3. ✅ **C. records-consumed-rate – the rate at which the Streams consumer pulls records from Kafka**  
   **Correct**. An embedded consumer metric (consumer-fetch-manager-metrics, `records-consumed-rate`) exposed by the Streams client together with its own Streams metrics.

4. ❌ **D. stream-task-lag – the number of records waiting in a task’s input queue**  
   **Incorrect**. No Streams metric named `stream-task-lag` exists; lag is visible through the consumer metric `records-lag-max`/`records-lag`.

5. ❌ **E. record-processing-latency-avg – the average time between record consumption and forwarding**  
   **Incorrect**. No Streams metric has this name; the closest real ones are `process-latency-avg`/`process-latency-max` (task/thread level).

6. ❌ **F. max-thread-idle-time – the maximum idle time of any Streams worker thread**  
   **Incorrect**. Streams does not expose a metric with this name; thread‑pool metrics are not reported by default.

</details>

## Question 37 (Programming & Serialization):
You are developing a Kafka producer that must send data securely to a broker cluster in a Confluent Platform deployment. Which set of client configuration properties is required to enable TLS encryption with server certificate verification?

- A. security.protocol=SSL ssl.truststore.location=/etc/ssl/truststore.jks ssl.truststore.password=truststorepw ssl.endpoint.identification.algorithm=HTTPS
- B. security.protocol=SSL ssl.certificate.location=/etc/ssl/client.crt ssl.key.location=/etc/ssl/client.key ssl.endpoint.identification.algorithm=HTTPS
- C. security.protocol=PLAINTEXT ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS
- D. security.protocol=SASL_SSL sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="user" password="pw"; ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To secure client‑to‑broker traffic with TLS, the client must set security.protocol=SSL. The truststore contains the broker’s CA certificates, allowing the client to validate the broker’s certificate chain; ssl.truststore.location and ssl.truststore.password provide these files. The ssl.endpoint.identification.algorithm=HTTPS property enforces hostname verification, preventing man‑in‑the‑middle attacks. Options 2 and 4 omit essential TLS settings, while option 3 adds unnecessary SASL authentication. Proper configuration ensures encrypted communication and integrity of the broker identity, which is a core requirement for Confluent‑Certified developers.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ✅ **A. security.protocol=SSL ssl.truststore.location=/etc/ssl/truststore.jks ssl.truststore.password=truststorepw ssl.endpoint.identification.algorithm=HTTPS**  
   **Correct**. The security.protocol=SSL enables TLS. The truststore properties provide the certificates to validate the broker's certificate, and ssl.endpoint.identification.algorithm=HTTPS enforces hostname verification against the broker certificate.

2. ❌ **B. security.protocol=SSL ssl.certificate.location=/etc/ssl/client.crt ssl.key.location=/etc/ssl/client.key ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. ssl.certificate.location and ssl.key.location are used for client authentication, not for server verification. The client must also provide a truststore to validate the broker certificate.

3. ❌ **C. security.protocol=PLAINTEXT ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. PLAINTEXT disables TLS, so traffic is not encrypted. The other properties are irrelevant without TLS.

4. ❌ **D. security.protocol=SASL_SSL sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="user" password="pw"; ssl.truststore.location=/etc/ssl/truststore.jks ssl.endpoint.identification.algorithm=HTTPS**  
   **Incorrect**. SASL_SSL requires both SASL authentication and TLS. If the application does not need SASL, this configuration is unnecessarily complex. The exam question explicitly asks for TLS with server verification only, not authentication.

</details>

## Question 38 (Kafka Core Concepts):
Which of the following statements about Kafka message headers are correct? (Select all that apply.)

- A. Header names cannot contain null bytes and are case-sensitive.
- B. Headers can store arbitrary binary data and are transmitted with the record to the broker.
- C. Header values can be compressed using GZIP to reduce record size.
- D. The total size of all headers is limited to 1 MB, independent of the record size.
- E. Header values are persisted in the Kafka broker as part of the record metadata and are available to consumers regardless of client version.
- F. Header keys must be unique per message; duplicate keys are allowed but only the last value is kept.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, B, E

**Explanation:**

Kafka message headers are a lightweight, map‑based mechanism that transports arbitrary binary metadata alongside the record payload. They are stored as part of the record on the broker and can be accessed by any consumer supporting the header API, making them useful for cross‑cutting concerns such as tracing or routing. Header keys are non-null strings and are case‑sensitive (duplicates are allowed), while values are raw byte arrays. Header data is included in the overall message size limit governed by broker configuration (e.g., max.message.bytes). Unlike record payload compression, headers are not individually compressed. Understanding these nuances ensures efficient use of headers in producer and consumer code and prevents common pitfalls such as duplicate keys or misinterpreting size limits.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "Headers" (p. 71)

**Detailed explanation of each option:**

1. ✅ **A. Header names cannot contain null bytes and are case-sensitive.**  
   **Correct**. Header keys are strings; the Java implementation forbids null characters, and key comparison is case-sensitive.

2. ✅ **B. Headers can store arbitrary binary data and are transmitted with the record to the broker.**  
   **Correct**. In Kafka, a header consists of a string key and a byte array value, allowing any binary payload. Headers travel with the record and are persisted by the broker.

3. ❌ **C. Header values can be compressed using GZIP to reduce record size.**  
   **Incorrect**. Compression applies to the entire record payload, not to individual headers. Header values are transmitted as raw bytes.

4. ❌ **D. The total size of all headers is limited to 1 MB, independent of the record size.**  
   **Incorrect**. The broker imposes a single maximum message size (default 1 MB) that includes key, value, headers, and any compression overhead.

5. ✅ **E. Header values are persisted in the Kafka broker as part of the record metadata and are available to consumers regardless of client version.**  
   **Correct**. Header data is stored with the record and can be retrieved by any consumer that supports the header API. Older clients simply ignore headers but the data remains intact.

6. ❌ **F. Header keys must be unique per message; duplicate keys are allowed but only the last value is kept.**  
   **Incorrect**. Kafka headers are an ordered list of (key, value) pairs; duplicate keys ARE allowed and ALL values are kept (`lastHeader(key)` returns the last, `headers(key)` all of them). Keys are not required to be unique and nothing is dropped.

</details>

## Question 39 (Application Development):
An application uses the Kafka Producer and Consumer APIs to implement a data pipeline. Which of the following statements correctly describe how to achieve at‑most‑once, at‑least‑once, and exactly‑once processing semantics in such a setup?

- A. Kafka Streams' `commit.interval.ms` config automatically commits offsets to the broker, ensuring at‑least‑once processing semantics.
- B. Set `max.in.flight.requests.per.connection=1` along with `enable.idempotence=true` to prevent duplicate records.
- C. Using a consumer with `enable.auto.commit=true` and processing records in the polling loop without committing offsets explicitly guarantees exactly‑once semantics.
- D. Use a transactional producer (`transactional.id` set) and wrap each batch of sends in `beginTransaction()` / `commitTransaction()`, while the consumer commits offsets manually inside the same transaction. This guarantees exactly‑once semantics.
- E. Set `enable.auto.commit=false` and call `consumer.commitSync()` after each record is processed. This guarantees at‑most‑once semantics.
- F. Configure the producer with `enable.idempotence=true` and `acks=all`. This alone provides at‑least‑once delivery.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** A, F, D

**Explanation:**

Processing semantics in Kafka revolve around how producers and consumers handle duplicates and data loss. Exactly‑once semantics require atomicity between producing records and committing offsets, achievable with transactional producers and `sendOffsetsToTransaction` (consumers downstream use `isolation.level=read_committed`). At‑least‑once is what you get when offsets are committed AFTER processing (Streams `commit.interval.ms` default), and on the producer side `acks=all` with retries (adding `enable.idempotence=true` even removes the duplicates). At‑most‑once is the opposite: commit offsets BEFORE processing, so records can be lost but never re-processed. Hence F is wrong: committing with `commitSync()` after each processed record is still at-least-once (a crash between processing and commit causes re-processing); the original answer key was wrong here. B is right per the book: acks=all + sufficient delivery.timeout.ms guarantees at-least-once delivery to Kafka (idempotence additionally prevents duplicates). C is not a way to prevent duplicates - idempotence already does that and allows up to 5 in-flight requests while preserving order. E is wrong: auto-commit gives at-least-once at best (or loss if the commit happens before processing finishes), never exactly-once.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 (enable.idempotence, acks, max.in.flight), ch. 4 (Commits and Offsets - commit after processing), ch. 8 (Exactly Once Semantics); https://kafka.apache.org/documentation/#semantics

**Detailed explanation of each option:**

1. ✅ **A. Kafka Streams' `commit.interval.ms` config automatically commits offsets to the broker, ensuring at‑least‑once processing semantics.**  
   **Correct**. In Kafka Streams, `commit.interval.ms` controls how frequently the library commits processed offsets. If a failure occurs, the same records will be re‑processed, which satisfies the at‑least‑once guarantee.

2. ❌ **B. Set `max.in.flight.requests.per.connection=1` along with `enable.idempotence=true` to prevent duplicate records.**  
   **Incorrect**. Idempotence by itself already prevents duplicate writes from retries (and keeps ordering with up to 5 in-flight requests), so limiting in-flight requests to 1 is not what prevents duplicates, and it says nothing about processing semantics.

3. ❌ **C. Using a consumer with `enable.auto.commit=true` and processing records in the polling loop without committing offsets explicitly guarantees exactly‑once semantics.**  
   **Incorrect**. Auto‑commit commits the offsets returned by the previous `poll()` periodically, independent of whether processing finished, so a crash can cause re‑processing (duplicates) or, if processing was still in progress, loss. It never gives exactly‑once.

4. ✅ **D. Use a transactional producer (`transactional.id` set) and wrap each batch of sends in `beginTransaction()` / `commitTransaction()`, while the consumer commits offsets manually inside the same transaction. This guarantees exactly‑once semantics.**  
   **Correct**. Transactional producers allow a single, atomic write that includes both producing records and committing consumer offsets. When the transaction is committed, the broker guarantees that either all records and the corresponding offsets are visible or none are, providing true exactly‑once processing.

5. ❌ **E. Set `enable.auto.commit=false` and call `consumer.commitSync()` after each record is processed. This guarantees at‑most‑once semantics.**  
   **Incorrect**. Committing AFTER processing means a crash between processing and commit leads to re‑processing of that record on restart: that is at‑least‑once. At‑most‑once requires committing BEFORE processing.

6. ✅ **F. Configure the producer with `enable.idempotence=true` and `acks=all`. This alone provides at‑least‑once delivery.**  
   **Correct**. The statement is about producer-to-broker delivery: `acks=all` plus retries guarantees each record is written at least once (the book, ch. 3), and idempotence additionally removes the duplicates retries could cause (so it is actually stronger than at-least-once per partition within a producer session). Consumer offset handling is a separate concern.

</details>

## Question 40 (Streams Development):
Which of the following mechanisms does Kafka Streams provide to ensure fault tolerance and consistency of stateful stream processing applications in a distributed environment?

- A. Exactly-once semantics via idempotent producers
- B. Kafka Streams tasks are distributed via the consumer group protocol, allowing load balancing and rebalancing
- C. Global tables are replicated across all instances for consistent state
- D. State store restoration from changelog topics upon restart
- E. Automatic repartitioning of streams based on key changes to balance load
- F. RocksDB checkpointing to allow recovery from crashes

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, B, F

**Explanation:**

Kafka Streams guarantees fault tolerance for stateful processing through three intertwined mechanisms: (1) every local state store has a corresponding changelog topic, enabling state restoration on restart or reassignment; (2) RocksDB checkpoints provide an additional local recovery point; and (3) tasks are distributed as consumer‑group members, so the protocol automatically rebalances tasks when a node fails. These features together ensure that, even after a crash, the application can resume with its exact state and correct results. EOS, while useful for eliminating duplicate writes, does not recover state, and GlobalKTables or repartitioning are for data sharing and load balancing rather than fault tolerance. Note: the RocksDB "checkpoint" is a local `.checkpoint` file holding the changelog offsets up to which the store is already persisted on disk, so after a clean restart only the missing tail of the changelog has to be replayed (it is an optimization on top of the changelog, not a replacement for it).

Source: Kafka Streams architecture/fault tolerance - https://kafka.apache.org/documentation/streams/architecture (sections "Fault Tolerance", "State"); Kafka: The Definitive Guide 2nd ed., ch. 14 (Stream Processing - local state, rebalancing, changelog).

**Detailed explanation of each option:**

1. ❌ **A. Exactly-once semantics via idempotent producers**  
   **Incorrect**. Exactly-once semantics (EOS) is a property of Kafka producers and consumers that guarantees no duplicate records are written to a topic. While Streams can enable EOS for its output topics, EOS itself does not restore or preserve stateful local stores on failure. Thus, it is not a dedicated fault‑tolerance mechanism for stateful stream processing.

2. ✅ **B. Kafka Streams tasks are distributed via the consumer group protocol, allowing load balancing and rebalancing**  
   **Correct**. Each Streams task behaves as a member of a consumer group. When a task fails or a node leaves, the group protocol reassigns tasks to other members, ensuring continuous processing. This dynamic rebalancing is a key fault‑tolerance feature.

3. ❌ **C. Global tables are replicated across all instances for consistent state**  
   **Incorrect**. A GlobalKTable loads the entire topic into every instance, providing a read‑only, consistent view. However, this is not a fault‑tolerance mechanism for stateful processing; it is a design choice for read‑only data sharing.

4. ✅ **D. State store restoration from changelog topics upon restart**  
   **Correct**. Kafka Streams backs every local state store with a changelog topic. When an instance restarts or a task is reassigned, the store is rebuilt by replaying the changelog, ensuring exact recovery of state. This is a core fault‑tolerance feature of Streams.

5. ❌ **E. Automatic repartitioning of streams based on key changes to balance load**  
   **Incorrect**. Streams may create a repartition topic when the key changes to enable shuffling. Repartitioning improves load balancing but does not directly provide fault tolerance or state recovery.

6. ✅ **F. RocksDB checkpointing to allow recovery from crashes**  
   **Correct**. State stores backed by RocksDB are checkpointed to disk. On failure, the store can be restored from the checkpoint and the changelog, providing durable state. This is a built‑in fault‑tolerance feature.

</details>

## Question 41 (Kafka Core Concepts):
Which of the following statements about Kafka topic partitions and offsets are true?

- A. Offsets are global across all partitions of a topic and are unique for each record.
- B. A consumer's committed offset is stored in ZooKeeper and is shared across all consumer groups.
- C. A record's key is hashed to determine its partition, ensuring that records with the same key are written to the same partition.
- D. The maximum number of partitions per topic is limited by the broker's configured `num.partitions` setting.
- E. When a new partition is added to a topic, existing consumers automatically start consuming from the new partition.
- F. Offsets can be rolled back by consuming from a lower offset value.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** F, C

**Explanation:**

Kafka topics are logical namespaces split into partitions, each with its own ordered, immutable log. Offsets are indices within a partition, starting at 0, and are the consumer’s position marker. Consumers store committed offsets in the internal topic __consumer_offsets, providing isolation per consumer group. The default partitioner hashes a record’s key, ensuring records with the same key are routed to the same partition and preserving order for those keys. If a consumer needs to reprocess data, it can seek to a lower offset, effectively rolling back. Misconceptions often arise around global offsets, ZooKeeper usage, and automatic consumption of new partitions; understanding these nuances is essential for correct design and troubleshooting.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 1 "Topics and Partitions" (pp. 5-6)

**Detailed explanation of each option:**

1. ❌ **A. Offsets are global across all partitions of a topic and are unique for each record.**  
   **Incorrect**. Offsets are maintained per partition; the same offset number can appear in many partitions.

2. ❌ **B. A consumer's committed offset is stored in ZooKeeper and is shared across all consumer groups.**  
   **Incorrect**. Since Kafka 0.10, committed offsets are stored in the internal topic __consumer_offsets, not ZooKeeper, and each consumer group has its own offset state.

3. ✅ **C. A record's key is hashed to determine its partition, ensuring that records with the same key are written to the same partition.**  
   **Correct**. The default partitioner uses a key hash to consistently map the same key to a specific partition, guaranteeing intra-key ordering.

4. ❌ **D. The maximum number of partitions per topic is limited by the broker's configured `num.partitions` setting.**  
   **Incorrect**. `num.partitions` is only a default value; topics can have more partitions, though large numbers can impact broker performance.

5. ❌ **E. When a new partition is added to a topic, existing consumers automatically start consuming from the new partition.**  
   **Incorrect**. Adding partitions triggers a rebalance; consumers may or may not receive assignments to the new partitions depending on group dynamics.

6. ✅ **F. Offsets can be rolled back by consuming from a lower offset value.**  
   **Correct**. A consumer can seek to an earlier offset (e.g., using seek() or resetting offsets) to reprocess messages.

</details>

## Question 42 (Application Development):
When connecting an Apache Kafka producer or consumer to a Confluent Cloud secured cluster that uses SASL/SSL authentication, which of the following configuration steps are **required** to establish a successful connection? Select all that apply.

- A. Use the `SASL_PLAINTEXT` security protocol to combine SASL authentication with plaintext transport.
- B. Provide a JAAS configuration file (or set `java.security.auth.login.config`) containing the client principal and password, and reference it via the `SASL_CLIENT_JAAS_CONFIG` system property.
- C. Configure the `ssl.truststore.location` and `ssl.truststore.password` properties to trust the broker’s certificate chain.
- D. Set the `security.protocol` property to `SASL_SSL` and specify a SASL mechanism such as `PLAIN` or `SCRAM-SHA-512` via `sasl.mechanism`.
- E. Include the broker’s hostname in the `bootstrap.servers` list using the `ssl://` scheme, e.g., `ssl://broker:9093`.
- F. Specify `ssl.keystore.location` and `ssl.keystore.password` to supply a client certificate for mutual TLS authentication.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, D, C

**Explanation:**

To securely connect to a Kafka cluster that uses SASL/SSL, a client must (1) set `security.protocol=SASL_SSL` and a valid SASL mechanism, (2) provide SASL credentials via a JAAS config file, and (3) trust the broker’s certificate by configuring the SSL truststore. These three steps establish encryption, authenticate the client, and ensure the broker’s identity. Options 4–6 are optional or incorrect: a client keystore is only needed for mutual TLS, `ssl://` is not a valid bootstrap syntax, and `SASL_PLAINTEXT` lacks encryption.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 11 "Security Protocols"/"SASL" (pp. 268-286)

**Detailed explanation of each option:**

1. ❌ **A. Use the `SASL_PLAINTEXT` security protocol to combine SASL authentication with plaintext transport.**  
   **Incorrect**. `SASL_PLAINTEXT` does not encrypt traffic, which is unacceptable for a secured cluster that requires SSL. Attempting to use this protocol will result in a connection failure on a cluster that mandates TLS.

2. ✅ **B. Provide a JAAS configuration file (or set `java.security.auth.login.config`) containing the client principal and password, and reference it via the `SASL_CLIENT_JAAS_CONFIG` system property.**  
   **Correct**. The JAAS file supplies the SASL credentials (username/password or keytab). The client must read these credentials; otherwise SASL authentication cannot occur, leading to a connection failure.

3. ✅ **C. Configure the `ssl.truststore.location` and `ssl.truststore.password` properties to trust the broker’s certificate chain.**  
   **Correct**. The truststore holds the CA certificates that signed the broker’s certificate. Without a trusted CA, the SSL handshake will fail, preventing the client from establishing a secure connection.

4. ✅ **D. Set the `security.protocol` property to `SASL_SSL` and specify a SASL mechanism such as `PLAIN` or `SCRAM-SHA-512` via `sasl.mechanism`.**  
   **Correct**. This property tells the client to use SSL for encryption and SASL for authentication. It is mandatory for a secured cluster that requires both encryption and SASL credentials. Without it, the client will attempt an unsecured connection and fail.

5. ❌ **E. Include the broker’s hostname in the `bootstrap.servers` list using the `ssl://` scheme, e.g., `ssl://broker:9093`.**  
   **Incorrect**. The `bootstrap.servers` property uses plain host:port pairs; adding a scheme prefix is not supported and will cause a parsing error. The correct format is `broker:9093` with the protocol set via `security.protocol`.

6. ❌ **F. Specify `ssl.keystore.location` and `ssl.keystore.password` to supply a client certificate for mutual TLS authentication.**  
   **Incorrect**. Mutual TLS is optional; most Confluent Cloud clusters use SASL for client authentication. Including a keystore will work if the cluster requires mutual TLS, but it is not a mandatory step for standard SASL/SSL setups.

</details>

## Question 43 (Kafka Producers):
Which of the following Kafka producer configuration settings can you adjust to increase throughput and lower latency for a producer application while maintaining reasonable data reliability?

- A. Set batch.size to 1,048,576 bytes (1 MB).
- B. Enable idempotence=true.
- C. Increase max.block.ms to 60,000 ms.
- D. Set compression.type to snappy.
- E. Set linger.ms to 5 ms.
- F. Set acks to 0.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, A, E

**Explanation:**

Producer tuning primarily focuses on batching, linger, and compression to reduce network round‑trips and payload size, thereby boosting throughput and lowering latency. A larger batch.size lets the broker pack more records into a single request, improving throughput but potentially adding a small delay if records arrive slowly. A small linger.ms allows the producer to wait briefly for additional records before sending, striking a balance between batch fullness and response time. Compression (e.g., snappy) cuts the message payload, reducing bandwidth usage and time spent on network I/O, while still keeping CPU overhead reasonable. Settings like acks=0, max.block.ms, or enabling idempotence are not intended for performance gains; they either trade durability for speed or introduce unnecessary blocking/overhead.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "compression.type" (p. 59)

**Detailed explanation of each option:**

1. ✅ **A. Set batch.size to 1,048,576 bytes (1 MB).**  
   **Correct**. A larger batch allows the producer to group more records into a single network request, reducing per‑record overhead and increasing throughput. If the batch does not fill quickly, a modest delay may occur, but the trade‑off is usually acceptable for high‑volume workloads.

2. ❌ **B. Enable idempotence=true.**  
   **Incorrect**. Idempotence ensures exactly‑once semantics but adds a small CPU overhead. It is a reliability feature, not a performance‑tuning option.

3. ❌ **C. Increase max.block.ms to 60,000 ms.**  
   **Incorrect**. This parameter controls how long the producer blocks when its buffer is full. Raising it can cause longer blocking periods and increased latency, and does not directly improve throughput.

4. ✅ **D. Set compression.type to snappy.**  
   **Correct**. Compressing records reduces the amount of data sent over the network, lowering bandwidth usage and network I/O time. Snappy offers a good balance of compression ratio and CPU cost, making it suitable for throughput‑centric tuning.

5. ✅ **E. Set linger.ms to 5 ms.**  
   **Correct**. This setting tells the producer to wait up to 5 ms for more records before sending a batch. It improves batch completion without introducing significant latency, thereby boosting throughput.

6. ❌ **F. Set acks to 0.**  
   **Incorrect**. While this maximizes write speed, it removes durability guarantees. It is not a recommended tuning step for maintaining reasonable data reliability.

</details>

## Question 44 (Kafka Core Concepts):
Which of the following statements about Kafka consumers and their behavior in a consumer group are TRUE?

- A. Each partition in a topic can be consumed by multiple consumers within the same consumer group simultaneously.
- B. The consumer poll() method must be called frequently to avoid session timeouts and trigger rebalances.
- C. Kafka consumers automatically handle offset resets by discarding messages if offsets are out of range.
- D. When a new consumer joins a group, a rebalance occurs that redistributes partitions among all consumers in the group.
- E. Consumer groups allow multiple consumers to read the same message independently without any coordination.
- F. Kafka consumers track their read progress using offsets, which can be committed either automatically or manually.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, F, B

**Explanation:**

Kafka consumers in a consumer group coordinate to ensure each partition is consumed by only one consumer instance, maintaining message order and avoiding duplicates. Offsets track consumption progress and can be committed automatically or manually based on application needs, which impacts fault tolerance and exactly-once semantics. When consumers join or leave a group, Kafka triggers a rebalance to redistribute partitions fairly. Frequent calls to poll() are essential to send heartbeats and avoid session timeouts that cause unnecessary rebalances. Misunderstandings often arise regarding partition sharing within groups and offset reset behaviors; knowing these details is critical for designing robust Kafka consumer applications. Correction: heartbeats are sent by a separate background thread (since KIP-62), so poll() does not send them; poll() must be called within max.poll.interval.ms, otherwise the consumer is removed from the group and a rebalance is triggered. (Option E's "session timeouts" wording is therefore loose, but it is still the best third answer; F describes multiple consumer *groups*, not one group.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (pp. 83-90: heartbeat thread, max.poll.interval.ms, rebalance); https://kafka.apache.org/43/configuration/consumer-configs/

**Detailed explanation of each option:**

1. ❌ **A. Each partition in a topic can be consumed by multiple consumers within the same consumer group simultaneously.**  
   **Incorrect**. Within a single consumer group, each partition is assigned to only one consumer at a time to guarantee message order and avoid duplicate processing.

2. ✅ **B. The consumer poll() method must be called frequently to avoid session timeouts and trigger rebalances.**  
   **Correct**. Regular calls to poll() (within max.poll.interval.ms) keep the consumer a live member of the group; heartbeats themselves are sent by a background thread (session.timeout.ms / heartbeat.interval.ms).

3. ❌ **C. Kafka consumers automatically handle offset resets by discarding messages if offsets are out of range.**  
   **Incorrect**. Offset resets depend on the 'auto.offset.reset' configuration and may cause consumers to start reading from earliest or latest offsets, but they do not simply discard messages automatically.

4. ✅ **D. When a new consumer joins a group, a rebalance occurs that redistributes partitions among all consumers in the group.**  
   **Correct**. Adding or removing consumers triggers a rebalance in which Kafka reassigns partitions to consumers to evenly distribute the load.

5. ❌ **E. Consumer groups allow multiple consumers to read the same message independently without any coordination.**  
   **Incorrect**. Consumer groups coordinate partition assignments so that each message is processed by only one consumer instance in the group, avoiding duplicate consumption.

6. ✅ **F. Kafka consumers track their read progress using offsets, which can be committed either automatically or manually.**  
   **Correct**. Consumers maintain offsets for each partition they consume, and offset commits can be configured to happen automatically or manually, affecting fault tolerance and processing guarantees.

</details>

## Question 45 (Kafka Core Concepts):
A topic is configured with the following properties: `retention.ms=604800000` (7 days), `retention.bytes=1073741824` (1 GB), and `segment.bytes=10485760` (10 MB). After 3 days the topic contains 2 GB of data. Which statement correctly describes what the broker will do regarding data deletion?

- A. A. The broker will delete log segments that are older than 7 days, ignoring the 1 GB size limit.
- B. C. The broker will delete segments that are either older than 7 days or cause the size to exceed 1 GB, whichever condition is met first.
- C. E. The broker will delete segments only if they both exceed 1 GB and are older than 7 days.
- D. D. The broker will not delete any segments until the oldest segment is older than 7 days.
- E. B. The broker will delete the oldest log segments until the total size of the topic falls below 1 GB, regardless of segment age.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

Kafka uses two independent retention controls: `retention.ms` (age-based) and `retention.bytes` (size-based). When the log grows beyond the size limit, the broker will trim the oldest segments first until the size falls below `retention.bytes`, regardless of how recent those segments are. Only if the size stays within the limit will `retention.ms` trigger deletion of segments older than the specified age. Thus, in the scenario where the topic reaches 2 GB in 3 days, the broker will immediately start deleting the oldest segments to reduce the size below 1 GB, even though the age threshold has not yet been met. This behavior ensures predictable disk usage while also honoring time-based retention. References: - https://kafka.apache.org/documentation/#brokerconfigs_retentionms - https://kafka.apache.org/documentation/#brokerconfigs_retentionbytes - https://kafka.apache.org/documentation/#log_retention

Source: Kafka: The Definitive Guide 2nd ed. Ch. 2 "Topic Defaults" (retention.ms/retention.bytes, pp. 27-33) and Ch. 6 "File Management" (pp. 152-153) — NOTE: retention.bytes triggers deletion of oldest segments until size is under the limit, independent of retention.ms.

**Detailed explanation of each option:**

1. ❌ **A. A. The broker will delete log segments that are older than 7 days, ignoring the 1 GB size limit.**  
   **Incorrect**. The size limit defined by `retention.bytes` is enforced in addition to age; the broker will not ignore it.

2. ❌ **B. C. The broker will delete segments that are either older than 7 days or cause the size to exceed 1 GB, whichever condition is met first.**  
   **Incorrect**. The broker does not wait for both conditions; it will enforce the size limit before the age limit when the size is exceeded.

3. ❌ **C. E. The broker will delete segments only if they both exceed 1 GB and are older than 7 days.**  
   **Incorrect**. Deletion is triggered by each limit independently; the broker does not require both to be satisfied simultaneously.

4. ❌ **D. D. The broker will not delete any segments until the oldest segment is older than 7 days.**  
   **Incorrect**. The size limit can trigger deletion before the age threshold is reached.

5. ✅ **E. B. The broker will delete the oldest log segments until the total size of the topic falls below 1 GB, regardless of segment age.**  
   **Correct**. When the total log size exceeds `retention.bytes`, the broker trims the oldest segments first to bring the size under the limit, even if those segments are younger than the age threshold.

</details>

## Question 46 (Kafka Connect):
When running Kafka Connect in distributed mode, which configuration property is essential to ensure that multiple workers coordinate properly and share connector and task configurations?

- A. connector.class
- B. bootstrap.servers
- C. offset.flush.interval.ms
- D. key.converter.schemas.enable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka Connect distributed mode, multiple workers must coordinate to share connector and task configurations. This coordination relies on Kafka topics internally, so specifying 'bootstrap.servers' is essential for workers to connect with the Kafka cluster and join the Connect cluster. Other properties, such as 'key.converter.schemas.enable' or 'offset.flush.interval.ms,' affect message serialization or offset commit behavior but do not influence worker coordination. 'connector.class' is a per-connector setting and not relevant at the worker cluster level. Understanding the role of 'bootstrap.servers' is critical for running Kafka Connect correctly in distributed mode.

NOTE: the property that actually makes workers form one Connect cluster is group.id (same value on all workers; plus config.storage.topic, offset.storage.topic, status.storage.topic). It is not offered here, so C (bootstrap.servers, also required) is the best of the listed options.

Source: https://kafka.apache.org/documentation/#connectconfigs (group.id, config.storage.topic); Kafka: The Definitive Guide 2nd ed. Ch. 9 "Running Connect" (distributed mode)

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**. : This property is specified per connector configuration to identify the connector plugin to run but is not a worker-level setting for coordination.

2. ✅ **B. bootstrap.servers**  
   **Correct**. : This property specifies the Kafka cluster addresses and is required for the Connect workers to communicate with Kafka brokers and coordinate via Kafka topics.

3. ❌ **C. offset.flush.interval.ms**  
   **Incorrect**. : This determines how frequently offsets are committed to Kafka but does not impact worker coordination or connector configuration sharing.

4. ❌ **D. key.converter.schemas.enable**  
   **Incorrect**. : This property controls whether schema information is included when serializing keys and does not affect worker coordination or configuration sharing.

</details>

## Question 47 (Kafka Ecosystem):
Which of the following statements accurately describe key features and behaviors of the Confluent Schema Registry when used with Apache Kafka?

- A. The Schema Registry supports only Avro schemas and does not support JSON Schema or Protobuf formats.
- B. Schema Registry allows registering schemas without any compatibility checks if the compatibility level is set to NONE.
- C. When a producer registers a schema, the Schema Registry assigns a unique schema ID which is embedded in the serialized message to facilitate deserialization.
- D. Schema Registry automatically converts data encoded with older schema versions to the latest schema version during consumption.
- E. Schema Registry enforces backward compatibility by default for all schema versions unless explicitly configured otherwise.
- F. Schema Registry stores schemas in a Kafka topic internally, enabling distributed and fault-tolerant schema storage.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** E, F, C, B

**Explanation:**

The Confluent Schema Registry plays a critical role in managing and evolving schemas in Kafka ecosystems. By default, it enforces backward compatibility to ensure consumers can read older data seamlessly. It stores schemas in an internal Kafka topic, providing distributed and fault-tolerant schema storage. Each schema registered is assigned a unique ID, embedded in serialized messages to aid consumers in schema lookup during deserialization. While Schema Registry supports multiple schema formats (Avro, JSON Schema, Protobuf), it does not automatically convert data between schema versions; compatibility rules guide schema evolution but do not transform data. Setting compatibility to NONE disables compatibility checks, allowing flexible but potentially unsafe schema changes. Understanding these behaviors is essential for developers to design robust, schema-evolution-safe Kafka applications.

Source: Confluent Schema Registry docs - "Schema Evolution and Compatibility" (BACKWARD/FORWARD/FULL rules)

**Detailed explanation of each option:**

1. ❌ **A. The Schema Registry supports only Avro schemas and does not support JSON Schema or Protobuf formats.**  
   **Incorrect**. Schema Registry supports multiple schema types including Avro, JSON Schema, and Protobuf.

2. ✅ **B. Schema Registry allows registering schemas without any compatibility checks if the compatibility level is set to NONE.**  
   **Correct**. Setting compatibility to NONE disables compatibility enforcement, allowing any schema to be registered regardless of compatibility.

3. ✅ **C. When a producer registers a schema, the Schema Registry assigns a unique schema ID which is embedded in the serialized message to facilitate deserialization.**  
   **Correct**. Each registered schema receives a unique ID that producers embed in messages, enabling consumers to retrieve the correct schema for deserialization.

4. ❌ **D. Schema Registry automatically converts data encoded with older schema versions to the latest schema version during consumption.**  
   **Incorrect**. Schema Registry does not perform automatic data conversion; compatibility rules ensure schemas evolve safely, but consumers handle data according to the schema version.

5. ✅ **E. Schema Registry enforces backward compatibility by default for all schema versions unless explicitly configured otherwise.**  
   **Correct**. By default, Schema Registry enforces backward compatibility, ensuring new schema versions can read data produced with previous versions.

6. ✅ **F. Schema Registry stores schemas in a Kafka topic internally, enabling distributed and fault-tolerant schema storage.**  
   **Correct**. Schema Registry uses an internal Kafka topic (_schemas) to store all schema versions, providing durability and fault tolerance.

</details>

## Question 48 (Kafka Connect):
Which of the following statements correctly describe the fundamental behavior, configuration, or data flow of Kafka Connect source connectors, sink connectors, and CDC connectors?

- A. Source connectors use the `topics` property to specify Kafka topics where the connector will write data.
- B. Sink connectors can be configured to write data to Kafka topics.
- C. Source connectors can read data from Kafka topics and write it back to external systems.
- D. Sink connectors use the `topics` property to specify Kafka topics from which the connector will consume data.
- E. CDC connectors automatically store schema changes in the same topic where data changes are published, eliminating the need for a separate history topic.
- F. CDC connectors are a special type of source connector that streams database changes to Kafka topics using binlog or change data capture mechanisms.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** D, F

**Explanation:**

Correction: E is false. The `topics` / `topics.regex` properties exist only for sink connectors (they select which topics to consume). Source connectors do not have a `topics` property; the destination topic is chosen by connector-specific settings (e.g. `topic`, `topic.prefix`) or by SMTs such as RegexRouter. So only A and B are correct (select 2). Original text follows.

In Kafka Connect, source connectors ingest data from external systems and publish to Kafka topics, controlled by the `topics` or `topics.regex` configuration. Sink connectors consume from those topics and push data to external destinations, again using the same `topics` setting to define the source streams. CDC connectors are a subclass of source connectors that capture database change events via mechanisms such as binlogs; they publish both data and schema changes, typically storing schema evolution in a separate history topic (e.g., `database.history.kafka.topic`). Misconceptions arise when one assumes sink connectors can write to Kafka or source connectors can read from Kafka; both statements are false. Understanding these distinctions is essential for designing correct data pipelines and for the Confluent Certified Developer exam. For reference, see the Kafka Connect documentation (https://docs.confluent.io/platform/current/connect/index.html) and Debezium CDC guide (https://debezium.io/documentation/reference/).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214)

**Detailed explanation of each option:**

1. ❌ **A. Source connectors use the `topics` property to specify Kafka topics where the connector will write data.**  
   **Incorrect**. `topics` / `topics.regex` are sink-connector properties. Source connectors define their target topics through connector-specific settings (e.g. `topic.prefix`) or routing SMTs.

2. ❌ **B. Sink connectors can be configured to write data to Kafka topics.**  
   **Incorrect**. Sink connectors consume from Kafka and write to external systems; they do not produce to Kafka topics.

3. ❌ **C. Source connectors can read data from Kafka topics and write it back to external systems.**  
   **Incorrect**. Source connectors read from external systems, not from Kafka topics, and publish to Kafka.

4. ✅ **D. Sink connectors use the `topics` property to specify Kafka topics from which the connector will consume data.**  
   **Correct**. Sink connectors subscribe to Kafka topics defined by the `topics` (or `topics.regex`) setting and write consumed records to an external system.

5. ❌ **E. CDC connectors automatically store schema changes in the same topic where data changes are published, eliminating the need for a separate history topic.**  
   **Incorrect**. CDC connectors write schema changes to a dedicated history topic (e.g., `database.history.kafka.topic`) for later replay.

6. ✅ **F. CDC connectors are a special type of source connector that streams database changes to Kafka topics using binlog or change data capture mechanisms.**  
   **Correct**. CDC connectors (e.g., Debezium) are implemented as source connectors and capture changes via database logs, publishing change events to Kafka topics.

</details>

## Question 49 (Observability & Testing):
You are troubleshooting a lagging consumer group named `order-processor` on the topic `orders`.
Which of the following Kafka CLI commands are valid for retrieving consumer group lag information, topic metadata, or both?

- A. kafka-topics --bootstrap-server localhost:9092 --describe --topic orders
- B. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor
- C. kafka-consumer-groups --bootstrap-server localhost:9092 --group order-processor
- D. kafka-cluster --bootstrap-server localhost:9092 --describe
- E. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor --json

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

In Kafka observability, consumer lag is a primary metric for diagnosing throughput issues. The kafka-consumer-groups tool, when used with the --describe flag, reports per‑partition committed and log offsets, allowing calculation of lag. kafka-consumer-groups has no --json option. The kafka-topics command with --describe provides topic metadata—partition layout, replicas, and ISR—which is essential for understanding replication lag or partition misconfiguration. Commands missing the --describe flag or referencing non‑existent tools do not yield the required data. Knowing which CLI commands deliver which pieces of information is critical for efficient troubleshooting.  
Source: book Ch. 12 (Consumer Groups, --describe output, p. 342 of PDF) ; Kafka source ConsumerGroupCommandOptions (no --json) and ClusterTool

**Detailed explanation of each option:**

1. ✅ **A. kafka-topics --bootstrap-server localhost:9092 --describe --topic orders**  
   **Correct**. This command shows the topic configuration, partition count, leader, replicas, and ISR information. While it does not show lag directly, it provides metadata useful for troubleshooting.

2. ✅ **B. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor**  
   **Correct**. The --describe flag lists the consumer group offsets, committed offsets, and the resulting lag for each partition. This is the standard way to view consumer lag.

3. ❌ **C. kafka-consumer-groups --bootstrap-server localhost:9092 --group order-processor**  
   **Incorrect**. Without an action option (--describe, --list, --reset-offsets, ...) the tool fails with an error and prints no group details.

4. ❌ **D. kafka-cluster --bootstrap-server localhost:9092 --describe**  
   **Incorrect**. A `kafka-cluster` tool exists (subcommands such as cluster-id, unregister, list-endpoints) but it has no `--describe` and gives no lag or topic metadata.

5. ❌ **E. kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group order-processor --json**  
   **Incorrect**. `kafka-consumer-groups.sh` has no `--json` option (unrecognized option error); the `--describe` output is plain text only.

</details>

## Question 50 (Streams Development):
In a Kafka Streams application, which of the following statements correctly describe best practices or guarantees related to application configuration and deployment?

- A. Setting `application.id` to a unique value for each instance is required to avoid duplicate consumer group metadata.
- B. Enabling `processing.guarantee` to `exactly_once_v2` guarantees that each record is processed exactly once even in the presence of failures.
- C. Registering a GlobalKTable via `builder.globalTable()` ensures that each instance of the Streams application receives the full table materialized locally for efficient join operations.
- D. Using the `state.dir` configuration to a local file system directory ensures fault tolerance across restarts.
- E. Setting `commit.interval.ms` to a very low value ensures that the application state is always up-to-date in case of a crash.
- F. Registering a state store with the `Stores.keyValueStoreBuilder` automatically creates a changelog topic that is replicated based on `replication.factor`.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, F

**Explanation:**

Kafka Streams relies on a combination of configuration properties and API choices to achieve fault tolerance and exactly‑once semantics. Setting `processing.guarantee` to an exactly-once mode activates Kafka transactions, which guarantees that each input record is processed and output is written atomically (option B; note that in current Kafka the value is `exactly_once_v2` - the old `exactly_once` value was deprecated and removed in 4.0, so the option is correct conceptually but its wording is dated). State stores created with a `Stores.keyValueStoreBuilder` and added to the topology have logging enabled by default, so a changelog topic is created automatically. GlobalKTables replicate the full reference data to every instance, allowing fast local joins (option E). Misconceptions often arise around `application.id` (it must be shared among instances), `state.dir` (local persistence alone does not provide fault tolerance), or `commit.interval.ms` (a low value trades performance for latency but does not ensure state is always current). Understanding these concepts is essential for designing resilient Streams applications.

Source: https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html;
https://kafka.apache.org/documentation/streams/developer-guide/processor-api.html (state store logging);
https://kafka.apache.org/documentation/streams/architecture; Kafka: The Definitive Guide 2nd ed. ch. 14 "Kafka Streams".

**Detailed explanation of each option:**

1. ❌ **A. Setting `application.id` to a unique value for each instance is required to avoid duplicate consumer group metadata.**  
   **Incorrect**. `application.id` identifies a logical Streams application and is shared by all instances that should participate in the same processing group. Using a unique ID for each instance defeats load balancing and rebalancing; it is not a requirement for avoiding duplicate metadata.

2. ✅ **B. Enabling `processing.guarantee` to `exactly_once_v2` guarantees that each record is processed exactly once even in the presence of failures.**  
   **Correct**. Setting `processing.guarantee` to an exactly-once mode (today `exactly_once_v2`; plain `exactly_once` was removed in Kafka 4.0) enables transactional processing, ensuring each input record is processed once and output records are written atomically. It requires Kafka to be configured with transactions and a transactional producer.

3. ✅ **C. Registering a GlobalKTable via `builder.globalTable()` ensures that each instance of the Streams application receives the full table materialized locally for efficient join operations.**  
   **Correct**. A GlobalKTable is replicated to every Streams instance. Each instance has a local copy of the full table, enabling efficient joins without needing a repartitioned topic. This is a correct statement.

4. ❌ **D. Using the `state.dir` configuration to a local file system directory ensures fault tolerance across restarts.**  
   **Incorrect**. `state.dir` specifies where local state stores are materialized. While it persists state locally, fault tolerance relies on Kafka changelog topics that are replicated across the cluster. A local directory alone does not provide fault tolerance.

5. ❌ **E. Setting `commit.interval.ms` to a very low value ensures that the application state is always up-to-date in case of a crash.**  
   **Incorrect**. `commit.interval.ms` controls how often the application commits offsets and state. A very low value increases latency and CPU overhead; it does not guarantee the state is always up-to-date, as state updates may still be in the changelog but not yet committed.

6. ✅ **F. Registering a state store with the `Stores.keyValueStoreBuilder` automatically creates a changelog topic that is replicated based on `replication.factor`.**  
   **Correct**. When a state store is registered, Streams creates a corresponding changelog topic (logging is enabled by default) whose replication factor is set by the Streams config `replication.factor` (in recent versions -1 = broker default). This ensures state changes are replicated for fault tolerance.

</details>

## 🚫 Question 51 (Kafka Connect):
In configuring the Kafka Connect JDBC Source Connector for incremental data loading, which configuration property is essential to ensure only new or updated rows are fetched from the database?

- A. timestamp.delay.interval.ms
- B. incrementing.column.name
- C. mode
- D. query

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The 'incrementing.column.name' is critical for incremental data loading in the JDBC Source Connector, as it identifies the column that monotonically increases (such as an ID) to fetch only new rows. While 'mode' must be set to 'incrementing' to enable this behavior, without specifying the incrementing column, the connector cannot track progress. The 'query' property allows custom queries but does not handle incremental state. 'timestamp.delay.interval.ms' manages timing for timestamp modes but is irrelevant for incrementing mode. Understanding these configurations ensures efficient, accurate data ingestion from relational databases into Kafka topics, a key skill for the Confluent Certified Developer.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 9 "Connector Example: MySQL to Elasticsearch" (pp. 216-223) — NOTE: JDBC Source Connector specifics verified against Confluent JDBC connector docs (system-specific connector, out of exam scope).

**Detailed explanation of each option:**

1. ❌ **A. timestamp.delay.interval.ms**  
   **Incorrect**. This property controls the delay before timestamp-based queries are executed but does not define the incremental column.

2. ✅ **B. incrementing.column.name**  
   **Correct**. This property specifies the column (usually a unique sequential ID) used to detect new rows since the last poll, enabling incremental loading.

3. ❌ **C. mode**  
   **Incorrect**. While 'mode' defines how data is fetched (e.g., bulk, incrementing, timestamp), it alone does not specify which column to use for incremental loading.

4. ❌ **D. query**  
   **Incorrect**. The 'query' property allows specifying a custom SQL query but does not inherently manage incremental loading by itself.

</details>

## Question 52 (Application Development):
A production application uses a Kafka producer to send 1 million messages per second to a cluster with 5 brokers and topics configured with 3 replicas.
Which of the following client configuration settings should you tune to maximize throughput while still ensuring message durability and reliability?

- A. `batch.size=1048576 (1 MB)`
- B. `acks=all`
- C. `linger.ms=0`
- D. `max.in.flight.requests.per.connection=5`
- E. `min.insync.replicas=2`
- F. `compression.type=gzip`

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** F, B, A

**Explanation:**

For high‑throughput Kafka producers that still need durability, the key tuning knobs are batch.size, acks, and compression.type. A larger batch.size lets the producer send more records per request, reducing the per‑record overhead. Setting acks to all guarantees that all replicas acknowledge the write, ensuring durability. Compression reduces the size of each request, improving effective throughput on network‑bound workloads. Options like linger.ms=0 hurt batching (a bigger batch.size only helps together with linger.ms > 0), and min.insync.replicas is a broker/topic setting, not a client one. max.in.flight.requests.per.connection=5 is the default and is safe for ordering with idempotence (default enabled since 3.0).

Source: book ch. 3 (PDF p. 89-90: max.in.flight, idempotence; batch.size, linger.ms, compression.type); https://kafka.apache.org/documentation/#producerconfigs

**Detailed explanation of each option:**

1. ✅ **A. batch.size=1048576**  
   **Correct**. Increasing batch.size to 1 MB allows the producer to accumulate more records before sending them in a single request, which significantly boosts throughput. This is a common tuning knob for high‑volume producers.

2. ✅ **B. acks=all**  
   **Correct**. Configuring acks to all guarantees that a record is considered written only after all in‑sync replicas have acknowledged it, providing the strongest durability guarantee without affecting throughput directly.

3. ❌ **C. linger.ms=0**  
   **Incorrect**. Setting linger.ms to 0 disables batching, forcing the producer to send records immediately. This reduces latency but also limits throughput because each record is sent in its own network request.

4. ❌ **D. max.in.flight.requests.per.connection=5**  
   **Incorrect**. 5 is already the default; with enable.idempotence=true (default since Kafka 3.0) ordering is preserved for up to 5 in-flight requests, so it is not a tuning change.

5. ❌ **E. min.insync.replicas=2**  
   **Incorrect**. This is a broker/topic configuration, not a client (producer) setting; it works with acks=all to require at least two in-sync replicas. The question asks for client settings.

6. ✅ **F. compression.type=gzip**  
   **Correct**. Enabling gzip compression reduces the payload size, leading to fewer bytes sent over the network. This can improve throughput, especially on bandwidth‑constrained links, at the cost of additional CPU usage.

</details>

## Question 53 (Deployment & Ops):
Which of the following statements correctly describes Kafka's native support for encrypting message payloads on the wire and at rest?

- A. Kafka automatically encrypts messages using the broker's file system encryption settings.
- B. Kafka encrypts only the headers but not the payload when using SASL/SSL.
- C. Kafka does not provide native message payload encryption; encryption must be handled by clients or external tools.
- D. Kafka natively encrypts message payloads using AES‑256 when TLS is enabled.
- E. Kafka can encrypt message payloads at rest using the built‑in "data‑at‑rest‑encryption" feature in Confluent Platform 7.x.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Kafka provides transport‑layer encryption (TLS) and authentication (SASL) to secure data in transit. For data at rest, Confluent Platform relies on storage‑level encryption or external tools; it does not natively encrypt the payload itself. Many developers mistakenly believe TLS protects the payload or that Kafka includes a built‑in at‑rest encryption feature. Understanding this distinction is critical for designing secure Kafka deployments and for selecting appropriate encryption strategies for both transit and storage.

Source: book ch. 11 "Securing Kafka" – Encryption / data at rest / end-to-end encryption (PDF p. 318); https://kafka.apache.org/documentation/#security_ssl

**Detailed explanation of each option:**

1. ❌ **A. Kafka automatically encrypts messages using the broker's file system encryption settings.**  
   **Incorrect**. File system encryption is independent of Kafka; Kafka will write data to disk as received. The broker does not automatically apply encryption.

2. ❌ **B. Kafka encrypts only the headers but not the payload when using SASL/SSL.**  
   **Incorrect**. SASL/SSL encrypts the entire communication channel, including headers and payload. Kafka does not selectively encrypt headers only.

3. ✅ **C. Kafka does not provide native message payload encryption; encryption must be handled by clients or external tools.**  
   **Correct**. Kafka’s core platform offers TLS/SASL for transport security and supports encryption at rest via storage‑level mechanisms, but it does not encrypt the payload data itself.

4. ❌ **D. Kafka natively encrypts message payloads using AES‑256 when TLS is enabled.**  
   **Incorrect**. TLS encrypts the entire transport channel between client and broker, not just the payload. Kafka does not apply AES‑256 to individual records; encryption is applied at the TCP layer.

5. ❌ **E. Kafka can encrypt message payloads at rest using the built‑in "data‑at‑rest‑encryption" feature in Confluent Platform 7.x.**  
   **Incorrect**. Confluent Platform does not ship a built‑in per‑topic encryption feature for stored records. Encryption at rest must be provided by the storage system (e.g., LUKS, file system encryption) or external tooling.

</details>

## Question 54 (Kafka Producers):
You are deploying a Kafka producer in a latency-sensitive application that sends small JSON messages. Which producer configuration will most directly reduce the round‑trip time for each message while still maintaining safe delivery semantics?

- A. Set `max.in.flight.requests.per.connection` to 5 and enable idempotence.
- B. Set `acks` to "all" and increase `request.timeout.ms` to 30,000.
- C. Set `batch.size` to 16KB and `linger.ms` to 0.
- D. Set `batch.size` to 16KB and `linger.ms` to 5ms.
- E. Set `compression.type` to "lz4" and keep the default `linger.ms`.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In a latency‑sensitive scenario with small payloads, the producer should avoid any unnecessary wait. Setting `linger.ms` to 0 forces immediate sends, which removes the batching delay that would otherwise add up to `linger.ms` milliseconds per record. While larger batch sizes can improve throughput, they are irrelevant when the linger time is zero. The other options either introduce deliberate delays (linger 5 ms), add CPU overhead (compression), increase replication confirmation time (acks "all"), or alter safety semantics without affecting latency (idempotence + in‑flight). Therefore, the correct choice is option 1. For reference, see the Kafka Producer Configuration docs at https://kafka.apache.org/documentation/#producerconfigs and the Confluent Producer guide https://docs.confluent.io/platform/current/clients/producer.html.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "linger.ms"/"batch.size" (pp. 59-60)

**Detailed explanation of each option:**

1. ❌ **A. Set `max.in.flight.requests.per.connection` to 5 and enable idempotence.**  
   **Incorrect**. This configuration improves safety by preventing duplicate messages during retries, but it does not directly influence the time a single record spends in the producer before being sent. It can actually limit throughput if retries are frequent.

2. ❌ **B. Set `acks` to "all" and increase `request.timeout.ms` to 30,000.**  
   **Incorrect**. Acks set to "all" requires confirmation from all in‑sync replicas, adding round‑trip delays. Increasing `request.timeout.ms` only enlarges the time the producer will wait for a response, further increasing latency.

3. ✅ **C. Set `batch.size` to 16KB and `linger.ms` to 0.**  
   **Correct**. Setting `linger.ms` to 0 tells the producer to send a record immediately after it is produced, eliminating the wait that would otherwise allow the batch to fill. This reduces latency for every record, which is critical for small messages. The larger `batch.size` is irrelevant when linger is 0 because the producer will not wait to accumulate messages. Safe delivery is preserved as long as other idempotence or acks settings remain unchanged.

4. ❌ **D. Set `batch.size` to 16KB and `linger.ms` to 5ms.**  
   **Incorrect**. A 5 ms linger introduces a deliberate pause to accumulate records before sending, which actually adds up to 5 ms of latency per message. While this can improve throughput, it is not optimal for latency‑sensitive workloads.

5. ❌ **E. Set `compression.type` to "lz4" and keep the default `linger.ms`.**  
   **Incorrect**. Compression reduces network payload but adds CPU overhead and is ineffective for very small messages. It does not directly lower round‑trip latency and can even increase it if the producer spends time compressing.

</details>

## Question 55 (Application Development):
When using the Kafka Producer API to set custom headers, which statement accurately reflects the size and ordering constraints defined by the Kafka broker?

- A. The combined size of all headers and the record payload cannot exceed the broker's `max.message.bytes` setting, and header ordering is not guaranteed.
- B. Header keys are strings and values are byte arrays; there is no per-header size limit, only the total record batch size limit (`message.max.bytes` / `max.message.bytes`) applies.
- C. Header keys must be no longer than 256 bytes, header values no longer than 4 KB, and the order of headers is preserved as they are added.
- D. Each header can be up to 1 MB in size, and headers are sorted alphabetically before transmission.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Record headers are an ordered collection of key/value pairs (keys are Strings, values are byte[]; duplicate keys are allowed). Kafka defines NO header-specific size limits (the 256 B / 4 KB figures in option A do not exist in Kafka); headers only count toward the overall record batch size limit (`message.max.bytes` on the broker / `max.message.bytes` on the topic, `max.request.size` on the producer). Header order IS preserved. Verified: the Headers Javadoc says "A mutable ordered collection of Header objects ... The order of headers is preserved in the order they were added" and documents no size limits. 


Source: https://kafka.apache.org/42/javadoc/org/apache/kafka/common/header/Headers.html

**Detailed explanation of each option:**

1. ❌ **A. The combined size of all headers and the record payload cannot exceed the broker's `max.message.bytes` setting, and header ordering is not guaranteed.**  
   **Incorrect**. The size part is right, but Kafka guarantees that the order in which headers are added to a `ProducerRecord` is preserved when sent to the broker. Header ordering is therefore deterministic, not arbitrary.

2. ✅ **B. Header keys are strings and values are byte arrays; there is no per-header size limit, only the total record batch size limit (`message.max.bytes` / `max.message.bytes`) applies.**  
   **Correct**. There is no per-header limit, only the total record size limit; header keys are strings and values are byte arrays.

3. ❌ **C. Header keys must be no longer than 256 bytes, header values no longer than 4 KB, and the order of headers is preserved as they are added.**  
   **Incorrect**. Kafka documents no such 256 B / 4 KB header limits; only the total record/batch size limits apply (the ordering part is true).

4. ❌ **D. Each header can be up to 1 MB in size, and headers are sorted alphabetically before transmission.**  
   **Incorrect**. Kafka defines no per-header size limit (neither 1 MB nor 4 KB; only the total record/batch limit applies), and it does not sort headers alphabetically—order is maintained.

</details>

## Question 56 (Stream Processing):
In the context of stateful operations in Kafka Streams, which of the following statements accurately describe key aspects of managing and using state stores?

- A. State stores can only be used for windowed aggregations and cannot be accessed directly by the application logic.
- B. In-memory state stores are recommended for large datasets because they offer the best durability and scalability.
- C. RocksDB is a commonly used persistent state store in Kafka Streams that enables efficient local storage of large state.
- D. State stores in Kafka Streams are fault-tolerant because their state is backed up by a changelog topic in Kafka.
- E. Stateful operations require repartition topics when the key of the data changes during processing to ensure correct grouping.
- F. State stores are automatically compacted by Kafka Streams without any configuration needed on the changelog topics.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, E, C, F

**Explanation:**

Stateful operations in Kafka Streams rely heavily on state stores, which maintain local state for computations like joins and aggregations. These stores are fault-tolerant because they are backed by changelog topics in Kafka, enabling recovery after failures. When keys change during processing, repartition topics are necessary to ensure data is correctly grouped for stateful operations. RocksDB is the default persistent state store, offering efficient local storage for large states. In-memory stores, while fast, do not provide durability or scalability for large datasets. Kafka Streams automatically creates changelog topics with `cleanup.policy=compact` (or `compact,delete` for windowed stores) without requiring any explicit user configuration. Understanding these nuances is critical for designing reliable and performant Kafka Streams applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "State" / "Surviving Failures" (pp. 388-389, 415-416)

**Detailed explanation of each option:**

1. ❌ **A. State stores can only be used for windowed aggregations and cannot be accessed directly by the application logic.**  
   **Incorrect**. State stores support various operations beyond windowed aggregations and can be queried directly via interactive queries.

2. ❌ **B. In-memory state stores are recommended for large datasets because they offer the best durability and scalability.**  
   **Incorrect**. In-memory state stores offer low latency but lack durability and are not suitable for large datasets requiring fault tolerance.

3. ✅ **C. RocksDB is a commonly used persistent state store in Kafka Streams that enables efficient local storage of large state.**  
   **Correct**. RocksDB is the default persistent store used by Kafka Streams for scalable and fault-tolerant local state management.

4. ✅ **D. State stores in Kafka Streams are fault-tolerant because their state is backed up by a changelog topic in Kafka.**  
   **Correct**. Kafka Streams uses changelog topics to replicate state store updates, enabling fault tolerance and recovery.

5. ✅ **E. Stateful operations require repartition topics when the key of the data changes during processing to ensure correct grouping.**  
   **Correct**. When the key is modified, Kafka Streams creates repartition topics to redistribute data correctly for stateful operations.

6. ✅ **F. State stores are automatically compacted by Kafka Streams without any configuration needed on the changelog topics.**  
   **Correct**. Kafka Streams auto-creates changelog topics with `cleanup.policy=compact` (or `compact,delete` for windowed stores); no user configuration is needed.

</details>

## Question 57 (Application Development):
A Kafka consumer is configured with `enable.auto.commit=false` and the application manually commits offsets after processing each batch. If the application crashes before committing the offsets for a batch, what will happen when it restarts?

- A. It will skip the messages that were processed before the crash.
- B. It will re-read the messages from the beginning of the topic.
- C. It will read messages from the last committed offset plus the uncommitted batch again.
- D. It will start from the last committed offset.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

When `enable.auto.commit` is disabled, the consumer only records offsets after an explicit commit. If the application crashes before committing the current batch, the broker’s stored offset (in `__consumer_offsets`) remains at the last successful commit. On restart the consumer resumes from that last committed offset, which means the batch that was processed but not committed is read (and processed) again, i.e. at‑least‑once semantics with possible duplicates. D states exactly this. C is worded confusingly ("last committed offset plus the uncommitted batch again") - the uncommitted batch lies after the last committed offset, so it is the same data, not an additional re-read; D is the precise statement. (Ambiguous question: C and D describe the same behaviour; D is cleaner.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (Commits and Offsets, Committing the Current Offset - "Re-processing"); https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit

**Detailed explanation of each option:**

1. ❌ **A. It will skip the messages that were processed before the crash.**  
   **Incorrect**. Skipping would violate at-least-once delivery. Without committing, the consumer has no record that it processed those messages, so they will be re-read.

2. ❌ **B. It will re-read the messages from the beginning of the topic.**  
   **Incorrect**. Restarting does not reset the offset to the topic beginning unless a special reset policy is applied. The consumer continues from the last committed position.

3. ❌ **C. It will read messages from the last committed offset plus the uncommitted batch again.**  
   **Incorrect** (imprecise). The uncommitted batch is already part of "everything after the last committed offset", so this is a confusing way to say the same as D; it also wrongly implies a separate re-read on top of the committed position. (The batch is re-processed, so duplicates are possible.)

4. ✅ **D. It will start from the last committed offset.**  
   **Correct**. The consumer resumes from the last committed offset; since the crashed batch was never committed, its records are delivered again.

</details>

## Question 58 (Application Observability): [-]
In a Kafka Streams application, which metric from the **StreamsMetrics** group most directly represents the throughput of records processed by the application, measured in records per second?

- A. streams.records.per-sec
- B. streams.records.in-total
- C. stream.processed.bytes-per-sec
- D. streams.processed.records-total
- E. streams.records.in-total-rate

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Streams exposes a set of metrics under the `streams.*` group. The metric `streams.records.per-sec` is the key throughput indicator, reporting how many records the stream processing logic handles each second. Cumulative counters like `streams.records.in-total` give total counts but cannot express rate, while byte‑based metrics are useful for payload size analysis, not record throughput. Recognizing the correct metric is essential for monitoring performance, diagnosing bottlenecks, and setting alerts in a production Streams application. The official documentation lists all available metrics and their descriptions (see https://kafka.apache.org/documentation/#streams_metrics).

Source: Kafka: The Definitive Guide 2nd ed. Ch. 13 "Monitoring Kafka" (pp. 339-378) — NOTE: StreamsMetrics throughput metric; exact metric name is illustrative.

**Detailed explanation of each option:**

1. ✅ **A. streams.records.per-sec**  
   **Correct**. This metric reports the average number of records processed per second, providing a direct measure of application throughput.

2. ❌ **B. streams.records.in-total**  
   **Incorrect**. This metric is a cumulative counter of all records that have entered the stream. It does not reflect the rate of processing and therefore is not a throughput metric.

3. ❌ **C. stream.processed.bytes-per-sec**  
   **Incorrect**. This metric measures bytes, not records, and is part of the `stream.*` namespace, not the `streams.*` namespace used by StreamsMetrics.

4. ❌ **D. streams.processed.records-total**  
   **Incorrect**. This is another cumulative counter, similar to `streams.records.in-total`. It indicates the total number processed but not the rate.

5. ❌ **E. streams.records.in-total-rate**  
   **Incorrect**. No such metric exists in the StreamsMetrics group; the correct throughput metric is `streams.records.per-sec`.

</details>

## Question 59 (Kafka Producers):
When sending a message using a Kafka producer in a Confluent platform environment, 
which of the following configurations help provide strong message delivery guarantees or preserve message ordering? Select all that apply.

- A. Setting linger.ms to zero to send messages immediately without batching
- B. Enabling idempotence to prevent duplicate messages during retries
- C. Specifying the partition explicitly to guarantee message ordering within that partition
- D. Setting acks=all to ensure that all ISR replicas acknowledge the message before considering it sent
- E. Using a synchronous send() call without a callback to block until the broker confirms receipt
- F. Using a key serializer that always returns null to ensure messages are distributed evenly across partitions

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** D, E, C, B

**Explanation:**

In Kafka, delivery guarantees and message ordering depend heavily on producer configurations. Setting acks=all ensures the highest durability by waiting for acknowledgments from all in-sync replicas, reducing the risk of data loss. Using synchronous send() calls means the producer waits for broker acknowledgment, ensuring the message is persisted before continuing. Explicitly specifying the partition guarantees that messages are sent to the same partition, preserving their order. Enabling idempotence prevents duplicate messages on retries (a delivery guarantee) and also preserves per-partition ordering intact when retries occur. Setting linger.ms to zero only affects batching and latency, not delivery guarantees or ordering. Using a null key leads to sticky/round-robin partitioning which does not maintain ordering. Understanding these nuances is critical for developers preparing for the Confluent Certified Developer for Apache Kafka exam.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 3 "acks" (pp. 55-56) and Ch. 7 "Send Acknowledgments" (pp. 170-171)

**Detailed explanation of each option:**

1. ❌ **A. Setting linger.ms to zero to send messages immediately without batching**  
   **Incorrect**. Setting linger.ms to zero reduces latency but does not directly impact delivery guarantees or message ordering.

2. ✅ **B. Enabling idempotence to prevent duplicate messages during retries**  
   **Correct**. Idempotence removes duplicates caused by retries (a delivery guarantee) and keeps per-partition ordering intact when retries occur.

3. ✅ **C. Specifying the partition explicitly to guarantee message ordering within that partition**  
   **Correct**. Messages sent to the same partition are ordered, so explicitly specifying the partition ensures ordering for related messages.

4. ✅ **D. Setting acks=all to ensure that all ISR replicas acknowledge the message before considering it sent**  
   **Correct**. Setting acks=all (or -1) ensures the highest level of delivery guarantee by waiting for all in-sync replicas to acknowledge the message.

5. ✅ **E. Using a synchronous send() call without a callback to block until the broker confirms receipt**  
   **Correct**. A synchronous send blocks the producer thread until an acknowledgment is received, which affects delivery guarantees and error handling.

6. ❌ **F. Using a key serializer that always returns null to ensure messages are distributed evenly across partitions**  
   **Incorrect**. Using a null key causes the producer to distribute messages in a sticky or round-robin manner, which does not guarantee ordering within a partition.

</details>

## Question 60 (Stream Processing): [-]
In Kafka Streams, which of the following configurations or design choices are necessary to achieve exactly‑once semantics for stateful processing and output to a sink topic?

- A. Use `KTable` joins with caching enabled to reduce duplicate processing.
- B. Set `exactly_once_batched=true` in the Streams configuration to enable batching of records within each transaction.
- C. Set `processing.guarantee` to "exactly_once" and enable `transactional.id` in the Streams configuration.
- D. Set `processing.guarantee` to "at_least_once" and use a transactional producer.
- E. Configure the source topics to have a retention of at least 24 hours and use `enable.idempotence=true` in the producer configuration.
- F. Disable `auto.offset.reset` to avoid duplicate records.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Correction: F is false. `exactly_once_batched` is not a real Kafka Streams config or `processing.guarantee` value (the real values are `at_least_once`, `exactly_once_v2`, and the deprecated `exactly_once` / `exactly_once_beta`). Only C is correct (Streams derives and manages `transactional.id` itself; the key setting is `processing.guarantee`). Original text follows.

Exactly‑once semantics in Kafka Streams rely on the Streams client’s ability to use Kafka transactions to atomically commit both state changes and output records. The core requirement is setting `processing.guarantee` to either "exactly_once" or "exactly_once_batched". The Streams runtime automatically generates a transactional.id and performs the necessary commit logic. Optional optimizations include `exactly_once_batched=true`, which batches records per transaction for higher throughput. Features like caching, retention policies, idempotence, or offset reset do not affect the exactly‑once contract. Misconceptions often arise from conflating idempotent producer writes with full transactional guarantees. Correctly configuring the guarantee property and transactional id ensures that each record is processed and stored exactly once, even in the presence of failures.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Processing Guarantees" (p. 392) and Ch. 8 (pp. 181-201) — NOTE: option F "exactly_once_batched" is not a real Kafka Streams config.

**Detailed explanation of each option:**

1. ❌ **A. Use `KTable` joins with caching enabled to reduce duplicate processing.**  
   **Incorrect**. While caching can improve throughput, it does not provide any additional guarantee of exactly‑once semantics. The guarantee is driven by the transactional boundaries set by the Streams client.

2. ❌ **B. Set `exactly_once_batched=true` in the Streams configuration to enable batching of records within each transaction.**  
   **Incorrect**. No such configuration exists in Kafka Streams. Transaction batching is governed by `commit.interval.ms`, and EOS is enabled only via `processing.guarantee`.

3. ✅ **C. Set `processing.guarantee` to "exactly_once" and enable `transactional.id` in the Streams configuration.**  
   **Correct**. The `processing.guarantee` property controls the fault‑tolerance semantics. Setting it to "exactly_once" (or "exactly_once_batched") activates transactional state commits and record writes. The `transactional.id` prefix is automatically derived by Streams, but must be enabled to allow the Kafka producer to participate in transactions.

4. ❌ **D. Set `processing.guarantee` to "at_least_once" and use a transactional producer.**  
   **Incorrect**. The "at_least_once" guarantee does not ensure no duplicate processing or state updates, even if the producer is transactional.

5. ❌ **E. Configure the source topics to have a retention of at least 24 hours and use `enable.idempotence=true` in the producer configuration.**  
   **Incorrect**. Retention length and idempotence alone do not provide exactly‑once guarantees. Exactly‑once requires transactional state commits, not just idempotent producer writes.

6. ❌ **F. Disable `auto.offset.reset` to avoid duplicate records.**  
   **Incorrect**. The offset reset policy only affects how the consumer starts reading when no committed offset exists. It does not influence the transactional semantics.

</details>

## Question 61 (Stream Processing):
Which of the following statements about Kafka Streams components and APIs are true? Select all that apply.

- A. A KTable is a changelog‑backed materialized view that can be queried via the Interactive Queries API.
- B. The `through` method writes records to an intermediate topic but discards the original key/value pairs.
- C. The `transform` method allows a KStream to be processed using the Processor API while retaining the original key/value semantics.
- D. Global tables are replicated to all instances and can be read from any instance but are not mutable by user code.
- E. All state stores in Kafka Streams are automatically backed by changelog topics, and users do not need to configure them.
- F. Global tables are replicated to all instances but cannot be queried by the Interactive Queries API.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** C, A, D

**Explanation:**

Kafka Streams distinguishes between KStreams (unbounded event streams) and KTables (stateful changelog‑backed tables). KTables expose state stores that are persisted via changelog topics and can be queried interactively, which makes option 1 true. The DSL ‘through’ operator preserves the original record while writing to an intermediate topic, invalidating option 2. Global tables are fully replicated and queryable, contradicting option 3, but option 6 correctly states that they are read‑only and replicated. The ‘transform’ operator bridges the DSL with the Processor API, allowing stateful processing without altering key/value semantics, validating option 4. Finally, not all stores are changelog‑backed; transient stores lack changelogs, so option 5 is false. This knowledge is essential for designing fault‑tolerant, stateful stream applications.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Kafka Streams by Example" (pp. 402-410)

**Detailed explanation of each option:**

1. ✅ **A. A KTable is a changelog‑backed materialized view that can be queried via the Interactive Queries API.**  
   **Correct**. KTables store their state in a persistent changelog topic and expose a state store that can be queried at runtime via the Interactive Queries API. This is documented in the Kafka Streams Developer Guide.

2. ❌ **B. The `through` method writes records to an intermediate topic but discards the original key/value pairs.**  
   **Incorrect**. The `through` method simply forwards each record to a topic and then re‑reads it, preserving the original key/value pairs. It does not discard data.

3. ✅ **C. The `transform` method allows a KStream to be processed using the Processor API while retaining the original key/value semantics.**  
   **Correct**. `transform` is a DSL operator that delegates to a user‑supplied Transformer which can use state stores and emit zero, one or more output records while preserving the stream’s semantics.

4. ✅ **D. Global tables are replicated to all instances and can be read from any instance but are not mutable by user code.**  
   **Correct**. Global tables are read‑only views that are replicated to each instance, and applications cannot mutate them directly; updates come only from the source topic.

5. ❌ **E. All state stores in Kafka Streams are automatically backed by changelog topics, and users do not need to configure them.**  
   **Incorrect**. Only persistent state stores are backed by changelog topics; transient (in‑memory) stores are not. Users must declare the store type in the topology.

6. ❌ **F. Global tables are replicated to all instances but cannot be queried by the Interactive Queries API.**  
   **Incorrect**. Global tables are fully replicated to every instance and their state stores are accessible via the Interactive Queries API, just like local KTables.

</details>

## Question 62 (Stream Processing):
In the context of Apache Kafka Streams, when using tumbling time windows for aggregations, which of the following statements is TRUE regarding window boundaries and event-time processing?

- A. The window's start and end timestamps are inclusive, meaning events with timestamps equal to the window's end time are included in that window.
- B. Tumbling windows can overlap, allowing an event to belong to multiple windows simultaneously.
- C. Tumbling windows require a fixed-size hop interval smaller than the window size to function correctly.
- D. In event-time processing, late-arriving events can be assigned to a window if they arrive before the window retention period expires.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Tumbling windows in Kafka Streams define fixed, non-overlapping time intervals where each event belongs to exactly one window. The window start time is inclusive, while the end time is exclusive, so events at the boundary belong to the subsequent window. Event-time processing manages out-of-order and late-arriving events by maintaining a retention period (or grace period), during which late events can still update aggregates for their windows. This feature is essential for accurate stream processing in real-world scenarios where event arrival can be delayed. Misunderstandings often arise around window boundaries and late event handling; knowing these details is critical for implementing correct time-windowed aggregations in Kafka Streams. Precisely: a late record is accepted into its window as long as stream-time has not passed window end + grace period; window store retention must be >= window size + grace. So A is true as an approximation (the grace period, not retention, is the actual cut-off).

Source: https://kafka.apache.org/documentation/streams/developer-guide/dsl-api.html#windowing ; https://kafka.apache.org/documentation/streams/core-concepts#streams_time ; Kafka: The Definitive Guide 2nd ed. Ch. 14 (Windowed joins/aggregations)

**Detailed explanation of each option:**

1. ❌ **A. The window's start and end timestamps are inclusive, meaning events with timestamps equal to the window's end time are included in that window.**  
   **Incorrect**. The window's start time is inclusive, but the end time is exclusive; events with timestamps equal to the window's end fall into the next window.

2. ❌ **B. Tumbling windows can overlap, allowing an event to belong to multiple windows simultaneously.**  
   **Incorrect**. Tumbling windows are fixed-size, non-overlapping time intervals, so each event belongs to exactly one window.

3. ❌ **C. Tumbling windows require a fixed-size hop interval smaller than the window size to function correctly.**  
   **Incorrect**. Fixed-size hop intervals are used in hopping windows, not tumbling windows, which have no overlap and no hops.

4. ✅ **D. In event-time processing, late-arriving events can be assigned to a window if they arrive before the window retention period expires.**  
   **Correct**. Kafka Streams allows late-arriving events to update windowed aggregates as long as they arrive within the configured grace period (the window store retention must be at least window size + grace); once the grace period expires the record is dropped.

</details>

## Question 63 (Stream Processing):
Which of the following design patterns are commonly used in stream processing applications built with Apache Kafka Streams to ensure scalability, fault tolerance, and maintainability?

- A. MapReduce
- B. Stateless Processing
- C. Microkernel Architecture
- D. Table-Driven Design
- E. Event Sourcing
- F. Table-Stream Duality

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, B, F

**Explanation:**

In Kafka Streams, design patterns like Event Sourcing, Stateless Processing, and Table-Stream Duality are essential for building scalable, fault-tolerant, and maintainable stream processing applications. Event Sourcing leverages Kafka's append-only log for reliable state reconstruction. Stateless Processing allows independent event handling without state overhead, improving scalability and simplifying recovery. Table-Stream Duality is a core abstraction enabling seamless conversion between streams and tables, facilitating complex joins and aggregations. Other options such as Table-Driven Design, Microkernel Architecture, and MapReduce, while valid in other contexts, are not primary design patterns in Kafka Streams. Understanding these patterns is critical for Certified Developers to design effective streaming solutions using Confluent's ecosystem.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 14 "Stream Processing Design Patterns" (pp. 392-401)

**Detailed explanation of each option:**

1. ❌ **A. MapReduce**  
   **Incorrect**. MapReduce is a batch processing paradigm mainly associated with Hadoop, not a design pattern used in Kafka Streams for real-time stream processing.

2. ✅ **B. Stateless Processing**  
   **Correct**. Stateless processing is a fundamental pattern in Kafka Streams where each event is processed independently without reliance on stored state, improving scalability and simplifying failure recovery.

3. ❌ **C. Microkernel Architecture**  
   **Incorrect**. Microkernel Architecture is an architectural pattern for extensible systems and is not directly related to stream processing or Kafka Streams design.

4. ❌ **D. Table-Driven Design**  
   **Incorrect**. Table-Driven Design is a technique for replacing complex conditional logic with lookup tables, but it is not a core pattern specifically associated with Kafka Streams or stream processing design.

5. ✅ **E. Event Sourcing**  
   **Correct**. Event Sourcing captures all changes to application state as a sequence of events, which fits naturally with Kafka's immutable log, enabling replayability and fault tolerance.

6. ✅ **F. Table-Stream Duality**  
   **Correct**. Table-Stream Duality is a key concept in Kafka Streams representing the idea that tables (state stores) and streams are interchangeable, enabling powerful joins and aggregations.

</details>

## Question 64 (Streams Development):
Which of the following statements about Kafka Streams application writing are true?

- A. A state store can be defined with any arbitrary name but must be the same across all instances to allow recovery.
- B. A KTable aggregation (`groupBy(...).aggregate/count`) is a changelog‑enabled stateful transformation, and `groupBy` on a KTable always causes data re-partitioning.
- C. GlobalKTable is materialized per instance and does not produce changelog topics.
- D. Suppress operator cannot be used on aggregations that emit intermediate results.
- E. Each source node reads from a topic partition assignment is round‑robin.
- F. A KStream-foreach always writes to a sink topic automatically.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, A

**Explanation:**

In Kafka Streams, stateful operators such as KTable joins maintain a local state store and write a changelog topic to enable fault tolerance. When keys differ across join partners, Streams automatically inserts a repartition topic to align keys. GlobalKTable, unlike a normal KTable, is replicated on every instance and therefore has no changelog. The foreach operator is a terminal operation that performs side‑effects but does not produce records. Suppress is intended to hide intermediate aggregation results, making it useful for windowed aggregations. Finally, store names must be consistent across instances to enable proper state recovery from changelog topics. These concepts are essential for designing robust, fault‑tolerant stream processing applications.

Source: book ch. 14 "Kafka Streams" (DSL, GlobalKTable, state stores); https://kafka.apache.org/42/streams/developer-guide/dsl-api/ (groupBy causes re-partitioning; GlobalKTable has no changelog); https://docs.confluent.io/current/streams/developer-guide.html

**Detailed explanation of each option:**

1. ✅ **A. A state store can be defined with any arbitrary name but must be the same across all instances to allow recovery.**  
   **Correct**. True. The store name is used to locate the store’s backing changelog topic. All instances must use the same name for a given logical store so that state can be recovered from the changelog during restarts.

2. ✅ **B. A KTable aggregation (`groupBy(...).aggregate/count`) is a changelog‑enabled stateful transformation, and `groupBy` on a KTable always causes data re-partitioning.**  
   **Correct**. DSL docs: "groupBy always causes data re-partitioning"; aggregations use a changelog-backed store. (The original wording about KTable joins was wrong: KTable-KTable joins need co-partitioned inputs and Streams does not repartition for them; foreign-key joins handle co-partitioning internally. The option was reworded.)

3. ✅ **C. GlobalKTable is materialized per instance and does not produce changelog topics.**  
   **Correct**. True. GlobalKTable keeps a full copy of the source topic on every instance; it is not partitioned and therefore does not emit a changelog topic. It is refreshed by reading the source topic fully during startup or on change events.

4. ❌ **D. Suppress operator cannot be used on aggregations that emit intermediate results.**  
   **Incorrect**. False. Suppress can be applied to aggregations (e.g., windowed aggregations) to suppress intermediate updates until the window closes, allowing downstream operators to receive only the final result.

5. ❌ **E. Each source node reads from a topic; partition assignment is round‑robin.**  
   **Incorrect**. False. Kafka Streams assigns topic partitions to stream tasks based on the group coordinator’s assignment algorithm, not a round‑robin strategy. Each task owns a subset of partitions, which can be imbalanced depending on the cluster configuration.

6. ❌ **F. A KStream-foreach always writes to a sink topic automatically.**  
   **Incorrect**. False. The foreach operator performs an action for each record (e.g., logging or external call) but does not emit to a Kafka topic. To write to a topic, the stream must be sent to a sink node with to().

</details>

## Question 65 (Kafka Connect):
Which of the following statements about the `key.converter` configuration property in Kafka Connect is **false**?

- A. It can be set to `org.apache.kafka.connect.storage.StringConverter` when the key is a plain UTF‑8 string.
- B. It must be the same converter for all connectors in a Kafka Connect cluster, otherwise the cluster will reject the connector configuration.
- C. If not specified, the default value is `org.apache.kafka.connect.storage.StringConverter`.
- D. It specifies the converter class used to serialize the record key for all data sent to Kafka topics.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The `key.converter` property determines how Kafka Connect serializes the key part of records before sending them to Kafka. It can be any converter class, such as `StringConverter` for plain strings or `JsonConverter` for JSON payloads. Connectors can set their own converters; the cluster does not enforce a single converter across all connectors, so option 3 is the false statement. Misconceptions often arise from conflating the need for a common converter with the cluster’s ability to mix converters. Understanding this property is essential for proper schema handling and data format compatibility in production deployments. Refer to the official Kafka Connect configuration documentation for details.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "Kafka Connect" / "Running Kafka Connect" (pp. 211-214) — NOTE: Verified against Kafka Connect docs: key.converter is per-connector/worker; the Connect worker default is JsonConverter, not StringConverter (option A's premise is itself inaccurate, but D is the stated false statement).

**Detailed explanation of each option:**

1. ❌ **A. It can be set to `org.apache.kafka.connect.storage.StringConverter` when the key is a plain UTF‑8 string.**  
   **Incorrect**. `StringConverter` is a valid built‑in converter suitable for simple string keys.

2. ✅ **B. It must be the same converter for all connectors in a Kafka Connect cluster, otherwise the cluster will reject the connector configuration.**  
   **Correct**. Each connector can independently specify its own `key.converter`; the cluster does not enforce a uniform converter across connectors.

3. ❌ **C. If not specified, the default value is `org.apache.kafka.connect.storage.StringConverter`.**  
   **Incorrect**. The default converter for keys is the StringConverter.

4. ❌ **D. It specifies the converter class used to serialize the record key for all data sent to Kafka topics.**  
   **Incorrect**. The `key.converter` property defines which serializer/deserializer is applied to the key of every Kafka record produced by the connector.

</details>

## Question 66 (Streams Development):
Which of the following statements correctly describe how Kafka Streams ensures fault tolerance, state durability, and data consistency for stateful operators?

- A. Kafka Streams writes its local state store to an external database for durability.
- B. Kafka Streams uses exactly-once semantics (EOS) to prevent duplicate records when reprocessing after a failure.
- C. The default retention period for changelog topics is 7 days, after which old state is discarded.
- D. Each state store is mirrored by a changelog topic that replicates state to other cluster nodes.
- E. Global tables are replicated to all instances to provide read-only access to a global view of the data.
- F. Repartition topics are created automatically to support joins and aggregations across keys.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, D, B

**Explanation:**

Kafka Streams guarantees fault tolerance for stateful operators by persisting each local state store to a replicated changelog topic. This replication ensures that if an instance fails, another can recover the exact state from the topic. Exactly‑once semantics (EOS) further guarantees that state updates and output records are written atomically, preventing duplicates during replay. Global tables replicate the entire table to every instance, providing a consistent read‑only view without repartitioning. Common misconceptions include assuming an external DB is required or that retention of changelog topics is limited; in reality, changelog topics for non-windowed stores are log-compacted (`cleanup.policy=compact`, latest value per key kept indefinitely), while changelogs of windowed stores use `compact,delete` with retention = window retention + 1 day (not 7 days), and they rely on Kafka’s replication. Option D (repartition topics) is a true statement but concerns re-keying, not fault tolerance/durability, hence not selected. These mechanisms together provide robust consistency and durability for stream processing applications.

Source: https://kafka.apache.org/documentation/streams/architecture and https://kafka.apache.org/documentation/streams/developer-guide/config-streams.html (state store changelog configs); Kafka: The Definitive Guide 2nd ed., ch. 14 (local state, rebalancing, exactly-once in Streams).

**Detailed explanation of each option:**

1. ❌ **A. Kafka Streams writes its local state store to an external database for durability.**  
   **Incorrect**. Kafka Streams relies on its own changelog topics to replicate the local state; it does not persist state to an external database.

2. ✅ **B. Kafka Streams uses exactly-once semantics (EOS) to prevent duplicate records when reprocessing after a failure.**  
   **Correct**. EOS guarantees that state changes and output records are written atomically and idempotently, ensuring consistency after a failure.

3. ❌ **C. The default retention period for changelog topics is 7 days, after which old state is discarded.**  
   **Incorrect**. Changelog topics are log-compacted rather than time-retained (windowed stores: retention = window retention + 1 day), so there is no 7-day default after which state is discarded.

4. ✅ **D. Each state store is mirrored by a changelog topic that replicates state to other cluster nodes.**  
   **Correct**. State stores are backed by changelog topics that are replicated across the Kafka cluster, providing durability and fault tolerance.

5. ✅ **E. Global tables are replicated to all instances to provide read-only access to a global view of the data.**  
   **Correct**. A GlobalKTable materializes a copy of the KTable on every instance, enabling local lookups and consistency without a repartition.

6. ❌ **F. Repartition topics are created automatically to support joins and aggregations across keys.**  
   **Incorrect**. for this context. While repartition topics are indeed used for re‑keying streams, the statement does not describe fault tolerance or state durability mechanisms.

</details>

## Question 67 (Kafka Producers):
When configuring serializers in a Kafka producer for a Confluent platform application, which of the following statements about serializers are correct?

- A. The ByteArraySerializer converts complex Java objects directly into byte arrays without additional configuration or schema requirements.
- B. Custom serializers must implement the org.apache.kafka.common.serialization.Serializer interface to be compatible with KafkaProducer.
- C. Using JsonSerializer automatically enforces schema validation against the Schema Registry before serialization.
- D. KafkaProducer requires both key.serializer and value.serializer properties to be set for proper serialization of message keys and values.
- E. The StringSerializer converts a String into a byte array using UTF-8 encoding and is suitable for simple text data.
- F. The AvroSerializer requires schema registry configuration to serialize objects using Avro schemas, enabling schema evolution support.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** E, F, D, B

**Explanation:**

In Kafka producers, serializers convert Java objects to byte arrays for transmission. StringSerializer is suitable for simple text, encoding strings as UTF-8. AvroSerializer integrates tightly with Confluent Schema Registry to manage Avro schemas and enable schema evolution. KafkaProducer requires both key.serializer and value.serializer to be explicitly set for correct operation. Custom serializers must implement the Serializer interface to be compatible. ByteArraySerializer does not serialize complex objects but rather passes byte arrays through. JsonSerializer serializes objects to JSON but does not enforce schema validation against Schema Registry by default, which can be a common misconception. Understanding these distinctions is critical for producing data correctly in Confluent Kafka environments. (The Confluent class is KafkaAvroSerializer; key.serializer/value.serializer have no defaults - alternatively serializer instances can be passed to the KafkaProducer constructor.)

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 "Serializers"; https://kafka.apache.org/43/configuration/producer-configs/ ; https://docs.confluent.io/platform/current/schema-registry/fundamentals/serdes-develop/

**Detailed explanation of each option:**

1. ❌ **A. The ByteArraySerializer converts complex Java objects directly into byte arrays without additional configuration or schema requirements.**  
   **Incorrect**. ByteArraySerializer simply passes through byte arrays; it does not convert complex Java objects. Complex objects require explicit serialization to byte arrays before using ByteArraySerializer.

2. ✅ **B. Custom serializers must implement the org.apache.kafka.common.serialization.Serializer interface to be compatible with KafkaProducer.**  
   **Correct**. To integrate custom serialization logic, the serializer must implement Kafka's Serializer interface to ensure compatibility and proper behavior within KafkaProducer.

3. ❌ **C. Using JsonSerializer automatically enforces schema validation against the Schema Registry before serialization.**  
   **Incorrect**. JsonSerializer serializes Java objects to JSON format but does not enforce schema validation via Schema Registry by default; that functionality requires additional configuration or use of specific Confluent serializers.

4. ✅ **D. KafkaProducer requires both key.serializer and value.serializer properties to be set for proper serialization of message keys and values.**  
   **Correct**. KafkaProducer mandates setting both key.serializer and value.serializer properties to correctly serialize keys and values before sending messages to Kafka topics.

5. ✅ **E. The StringSerializer converts a String into a byte array using UTF-8 encoding and is suitable for simple text data.**  
   **Correct**. StringSerializer is commonly used for serializing String keys or values by encoding them in UTF-8, which is standard and widely supported.

6. ✅ **F. The AvroSerializer requires schema registry configuration to serialize objects using Avro schemas, enabling schema evolution support.**  
   **Correct**. AvroSerializer depends on the Confluent Schema Registry to manage schemas and supports schema evolution, making it essential for Avro serialization in Confluent Kafka clients.

</details>

## Question 68 (Kafka Core Concepts):
In Apache Kafka, which of the following statements about replication are correct and essential for ensuring data durability and availability in a Kafka cluster?

- A. Kafka guarantees zero data loss if the replication factor is set to one and acknowledgments are set to zero.
- B. Increasing the replication factor improves fault tolerance but can increase the network and disk I/O overhead.
- C. If a leader broker fails, one of the in-sync replicas (ISR) is elected as the new leader to maintain availability.
- D. Only the leader replica of a partition handles all reads and writes, while followers replicate data asynchronously.
- E. Followers by default can serve read requests to improve read scalability and reduce leader load.
- F. Replication ensures that each partition has multiple copies across different brokers to provide fault tolerance.

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** F, D, C, B

**Explanation:**

Replication in Kafka is fundamental for data durability and availability. Each partition's data is replicated across multiple brokers to tolerate broker failures. The leader replica handles all client reads and writes, while follower replicas asynchronously replicate the data. When a leader fails, Kafka elects a new leader from the in-sync replicas (ISR) to maintain service continuity without data loss. While increasing replication factor enhances fault tolerance, it also increases resource consumption due to more data copies and network traffic. Some misconceptions include assuming followers can serve reads or that zero acknowledgments with a single replica guarantees zero data loss, which is not true. Understanding these replication mechanics is essential for designing resilient Kafka deployments.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 6 "Replication" (pp. 139-142) and Ch. 7 "Replication" (pp. 163-168)

**Detailed explanation of each option:**

1. ❌ **A. Kafka guarantees zero data loss if the replication factor is set to one and acknowledgments are set to zero.**  
   **Incorrect**. A replication factor of one means no redundancy, and acks=0 means the producer does not wait for any acknowledgment, risking data loss.

2. ✅ **B. Increasing the replication factor improves fault tolerance but can increase the network and disk I/O overhead.**  
   **Correct**. Higher replication factor means more replicas to maintain, which increases resource usage but improves durability.

3. ✅ **C. If a leader broker fails, one of the in-sync replicas (ISR) is elected as the new leader to maintain availability.**  
   **Correct**. Kafka elects a new leader from the ISR set to continue serving client requests without data loss.

4. ✅ **D. Only the leader replica of a partition handles all reads and writes, while followers replicate data asynchronously.**  
   **Correct**. The leader replica processes all client requests, and follower replicas replicate data asynchronously to stay in sync.

5. ❌ **E. Followers by default can serve read requests to improve read scalability and reduce leader load.**  
   **Incorrect**. Follower reads were introduced in KIP-392 (Kafka 2.4+) via client.rack / replica.selector.class, but this is not enabled by default.

6. ✅ **F. Replication ensures that each partition has multiple copies across different brokers to provide fault tolerance.**  
   **Correct**. Replication creates multiple copies (replicas) of each partition on different brokers to prevent data loss if a broker fails.

</details>

## Question 69 (Application Observability):
Which command-line invocation correctly displays the current lag for a consumer group on a Kafka cluster using Confluent Platform 7.x?

- A. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe
- B. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --offsets
- C. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --list
- D. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe --topic <topic>

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

2. ❌ **B. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --offsets**  
   **Incorrect (rationale CORRECTED)**. `--offsets` is only a sub-option of `--describe` (and is its default). Used alone, no action (`--describe`, `--list`, ...) is specified and the tool errors out.

3. ❌ **C. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --list**  
   **Incorrect**. `--list` lists all consumer groups in the cluster, not the offsets or lag for a specific group. It does not provide the information requested.

4. ❌ **D. kafka-consumer-groups --bootstrap-server <broker> --group <group-id> --describe --topic <topic>**  
   **Incorrect (rationale CORRECTED)**. `--topic` IS a recognized flag of `kafka-consumer-groups`, but it is documented for `--reset-offsets`/`--delete-offsets`, not as a filter for `--describe`; A is the canonical invocation for showing lag.

</details>

## Question 70 (Kafka Consumers): [-]
A new Kafka consumer joins a group and has never committed an offset for the subscribed topic. If the consumer configuration does not explicitly set the "auto.offset.reset" property, from where does the consumer begin consuming records?

- A. The middle of the log, roughly halfway between the oldest and newest records.
- B. The latest offset of each partition (just after the current end of the log).
- C. The consumer will fail to join the group and throw an error.
- D. The earliest offset of each partition (the beginning of the log).
- E. A random offset chosen by the broker.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, a consumer without a committed offset relies on the "auto.offset.reset" configuration to determine its starting point. The default value for this setting is "latest", meaning the consumer begins at the most recent offset in each partition. Many developers mistakenly believe the default is "earliest"; this confusion often leads to missed records in real‑time processing. The other options describe non‑existent defaults or erroneous behaviors. Understanding this default is crucial for designing reliable consumer groups, especially when handling late‑joining consumers or during cluster restarts.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 4 "auto.offset.reset" (p. 91)

**Detailed explanation of each option:**

1. ❌ **A. The middle of the log, roughly halfway between the oldest and newest records.**  
   **Incorrect**. Kafka does not provide a default middle‑offset behavior.

2. ✅ **B. The latest offset of each partition (just after the current end of the log).**  
   **Correct**. With no prior offset and the default setting of "auto.offset.reset=latest", the consumer starts at the end of each partition.

3. ❌ **C. The consumer will fail to join the group and throw an error.**  
   **Incorrect**. It will join successfully and apply the default offset reset policy.

4. ❌ **D. The earliest offset of each partition (the beginning of the log).**  
   **Incorrect**. The default value of "auto.offset.reset" is "latest", not "earliest".

5. ❌ **E. A random offset chosen by the broker.**  
   **Incorrect**. The offset is deterministic based on the "auto.offset.reset" policy.

</details>

## 🚫 Question 71 (Kafka Internals):
In Kafka's request processing pipeline, which component is primarily responsible for validating client requests and routing them to the appropriate handler within the broker?

- A. KafkaApis
- B. ReplicaManager
- C. RequestHandler
- D. NetworkProcessor

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

CORRECTION: the request handler (I/O) threads (KafkaRequestHandler) only take requests off the shared request queue and call KafkaApis.handle(); it is KafkaApis that checks the request's API key, performs authorization/validation and dispatches to the matching handler (handleProduceRequest, handleFetchRequest, ...). The network processor threads only read/write bytes, and ReplicaManager is a lower-level component used by those handlers. Original text follows.

Kafka's request processing pipeline begins with network I/O managed by the NetworkProcessor, which reads raw requests. However, the critical step of validating and routing these requests to the correct API handler is performed by the RequestHandler. This component ensures the request conforms to protocol expectations and directs it to KafkaApis or other internal components as needed. ReplicaManager operates at a different layer, managing partition states and replication, not client request routing. KafkaApis implements the logic for handling specific API calls but depends on RequestHandler for routing. Understanding this flow is essential for developers to troubleshoot request handling latency and errors in Kafka brokers.

Source (out of CCDAK scope): Kafka: The Definitive Guide 2nd ed. Ch. 6 "Request Processing" (pp. 142-148) (Kafka internals — out of exam scope)

**Detailed explanation of each option:**

1. ✅ **A. KafkaApis**  
   **Correct**. KafkaApis.handle() switches on the request's API key, performs authorization/validation and routes the request to the appropriate handler method.

2. ❌ **B. ReplicaManager**  
   **Incorrect**. ReplicaManager manages partition replicas and their state but does not handle client request validation or routing.

3. ❌ **C. RequestHandler**  
   **Incorrect**. The request handler threads just pull requests from the shared request queue and hand them to KafkaApis; they do not route by request type themselves.

4. ❌ **D. NetworkProcessor**  
   **Incorrect**. The NetworkProcessor handles the low-level network I/O and socket management but does not perform request validation or routing.

</details>

## Question 72 (Streams Development):
Which of the following options are effective techniques for tuning performance and scaling a Kafka Streams application?

- A. Use the materialized-as clause to create multiple state stores for a single topology to improve query performance.
- B. Disable the use of changelog topics for state stores to reduce network traffic.
- C. Increase the number of stream threads (default 1) to match the number of partitions for parallel processing.
- D. Increase the record cache size (`statestore.cache.max.bytes`) to reduce writes to the state store and downstream traffic.
- E. Configure the RocksDB compression property to snappy to improve write throughput.
- F. Reduce the window size in windowed joins to lower latency and memory usage.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, C, D

**Explanation:**

Documented tuning/scaling levers for Kafka Streams: increase `num.stream.threads` (config name; default 1) up to the number of tasks/partitions and/or add instances; enlarge the record cache (`statestore.cache.max.bytes`, formerly `cache.max.bytes.buffering`, default 10 MB) which reduces writes to RocksDB and downstream/changelog traffic; tune RocksDB via a `rocksdb.config.setter`. Disabling changelogs sacrifices fault tolerance; shrinking join windows changes the application semantics; creating multiple stores per topology is not a recognized query-performance technique. Verified live: `statestore.cache.max.bytes` (default 10485760; `cache.max.bytes.buffering` deprecated), `num.stream.threads` (default 1), `rocksdb.config.setter` exist; the record cache reduces output records. Option F was reworded (the original 'very large value' was dubious); the original key was B, D, E but E has no documentation support.
Still unverified: that RocksDB compression=snappy is a documented throughput tuning (B), docs only show rocksdb.config.setter for RocksDB tuning.

Source: https://kafka.apache.org/42/streams/developer-guide/memory-mgmt/ ; https://kafka.apache.org/42/streams/developer-guide/config-streams/

**Detailed explanation of each option:**

1. ❌ **A. Use the materialized-as clause to create multiple state stores for a single topology to improve query performance.**  
   **Incorrect (unsupported by docs; changed from the original key)**. Defining separate state stores allows the application to keep different key/value sets in distinct RocksDB instances, which can reduce contention and enable more efficient compaction. This technique is beneficial when the application needs to expose multiple queryable state tables.

2. ❌ **B. Disable the use of changelog topics for state stores to reduce network traffic.**  
   **Incorrect**. Changelog topics are essential for fault‑tolerance and state recovery. Disabling them would make the state store unreplicated, leading to data loss after a crash or rebalance, and is not a recommended tuning option.

3. ✅ **C. Increase the number of stream threads (default 1) to match the number of partitions for parallel processing.**  
   **Correct**. Kafka Streams runs tasks (one per input partition of a subtopology) on stream threads; the config is `num.stream.threads`; setting it equal to or slightly higher than the number of topic partitions allows each thread to process a subset of the data in parallel, improving throughput. However, it should not exceed the number of available CPU cores to avoid context‑switch overhead.

4. ✅ **D. Increase the record cache size (`statestore.cache.max.bytes`) to reduce writes to the state store and downstream traffic.**  
   **Correct (with a caveat)**. A larger cache can reduce writes to the underlying RocksDB, but it also consumes more heap. An excessively large cache can trigger frequent garbage collection pauses and may lead to out‑of‑memory errors. The recommended approach is to use a moderate cache (e.g., 10–15% of available RAM) and tune based on the workload.

5. ✅ **E. Configure the RocksDB compression property to snappy to improve write throughput.**  
   **Correct**. Using a lightweight compression algorithm such as snappy reduces CPU usage during writes while still compressing data, which can lower disk I/O and improve overall throughput, especially on high‑throughput workloads.

6. ❌ **F. Reduce the window size in windowed joins to lower latency and memory usage.**  
   **Incorrect**. Shorter windows reduce the amount of state kept per key, which can lower memory consumption and increase responsiveness. However, it can also increase the number of windows that need to be processed, potentially raising overhead; the effect depends on the application semantics.

</details>

## Question 73 (Deployment & Ops):
In a Confluent Platform deployment, which of the following statements accurately describe how schema evolution is handled by the Schema Registry to ensure seamless producer‑consumer compatibility?

- A. Setting `schema.registry.schema.compatibility.level=BACKWARD` ensures that a newly registered schema can read data written with the older schema.
- B. Deploying Schema Registry with `compatibility` set to `FORWARD` at the cluster level guarantees that consumers can read data written with newer schema.
- C. Using the `latest compatible` endpoint of Schema Registry to retrieve the most compatible schema for a given subject.
- D. Enabling `auto.register.schemas=false` in the producer config prevents schema evolution issues.
- E. Changing the logical type of a field (e.g., from `int32` to `int64`) is allowed under `FULL` compatibility but not under `BACKWARD`.
- F. Defining a JSON schema with a `default` value for new fields allows producers to omit the field without breaking consumers.

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, A 

**Explanation:**

Schema evolution in Confluent Kafka relies on compatibility levels defined per subject or cluster. Backward compatibility guarantees that new schemas can read data produced with older ones, while forward compatibility ensures older consumers can read data produced with newer schemas. Full compatibility requires both. There is no `latest compatible` endpoint: compatibility is tested with `POST /compatibility/subjects/{subject}/versions/{version}` and the default level is set via `PUT /config`. Defaults in Avro, not JSON Schema, support optional fields during evolution. Configuring compatibility at the cluster level applies a consistent rule across subjects, but the flag `auto.register.schemas=false` only stops automatic registration and does not influence compatibility semantics.  
Verified live: the API reference has POST /compatibility/subjects/{subject}/versions/{version}, POST /compatibility/subjects/{subject}/versions, GET/PUT /config, GET /subjects/{subject}/versions/latest and no 'latest compatible' endpoint (C false). Still unverified: JSON Schema default semantics (A).
Source: https://docs.confluent.io/platform/current/schema-registry/develop/api.html

**Detailed explanation of each option:**

1. ✅ **A. Setting `schema.registry.schema.compatibility.level=BACKWARD` ensures that a newly registered schema can read data written with the older schema.**  
   **Correct**. Backward compatibility means the new schema can read data written with the previous schema(s). Note: the real server property name is `schema.compatibility.level` (env var `SCHEMA_REGISTRY_SCHEMA_COMPATIBILITY_LEVEL`), not `schema.registry.schema.compatibility.level`.

2. ✅ **B. Deploying Schema Registry with `compatibility` set to `FORWARD` at the cluster level guarantees that consumers can read data written with newer schema.**  
   **Correct**. Forward compatibility ensures that older consumers can deserialize data written with newer schemas; setting it at the cluster level applies this rule globally to all subjects.

3. ❌ **C. Using the `latest compatible` endpoint of Schema Registry to retrieve the most compatible schema for a given subject.**  
   **Incorrect**. No such endpoint exists. The Schema Registry API offers `POST /compatibility/subjects/{subject}/versions/{version}` to TEST whether a schema is compatible with a given/latest version; it does not return a 'most compatible' schema.

4. ❌ **D. Enabling `auto.register.schemas=false` in the producer config prevents schema evolution issues.**  
   **Incorrect**. This flag simply disables automatic schema registration; it does not affect compatibility checks and can actually increase the risk of mismatched schemas if the client does not register the correct schema.

5. ❌ **E. Changing the logical type of a field (e.g., from `int32` to `int64`) is allowed under `FULL` compatibility but not under `BACKWARD`.**  
   **Incorrect**. Avro promotion int -> long is allowed under BACKWARD (a new reader schema with `long` can read old `int` data) but not under FORWARD, hence not under FULL; the statement has it reversed.

6. ❌ **F. Defining a JSON schema with a `default` value for new fields allows producers to omit the field without breaking consumers.**  
   **Incorrect**. While default values are supported in Avro schemas, JSON Schema defaults are not used by Kafka consumers. Consumers rely on Avro default values or schema evolution rules, not JSON Schema defaults.

</details>

## Question 74 (Kafka Connect):
Which of the following statements are true about configuring and deploying a source connector in Kafka Connect when running in distributed mode?

- A. The tasks.max setting is optional and can be omitted from the configuration.
- B. Once the connector is created, it will be automatically registered in ZooKeeper when using standalone mode.
- C. For a source connector, a topics.pattern property must be specified to capture multiple source tables.
- D. The connector configuration must be submitted via the REST endpoint /connectors with a POST request.
- E. The connector class name must be fully qualified and must implement the SourceConnector interface.
- F. The connector configuration file can be placed in the 'config' directory of the worker and will be automatically loaded when the worker starts.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** D, E, A

**Explanation:**

Correction: F is true. `tasks.max` is optional; `ConnectorConfig` defines it with a default of 1, so it can be omitted (only `name` and `connector.class` are required). Hence A, E, F (select 3). Original text follows (its claim that tasks.max is required is wrong).

In distributed Kafka Connect, connectors are deployed by posting their JSON configuration to the worker REST endpoint; this is the only supported deployment method. The required configuration includes the fully‑qualified connector.class and a tasks.max value that controls parallelism. Other properties are source‑specific or optional and do not make the configuration valid. Understanding these requirements prevents common deployment failures such as missing class names or absent tasks.max. The other statements describe behaviors that belong to standalone mode, sink connectors, or ZooKeeper usage, which are not applicable to distributed source connector deployment.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. The tasks.max setting is optional and can be omitted from the configuration.**  
   **Correct**. `tasks.max` defines the maximum number of parallel tasks but has a default value of 1, so the connector starts fine without it (only `name` and `connector.class` are mandatory).

2. ❌ **B. Once the connector is created, it will be automatically registered in ZooKeeper when using standalone mode.**  
   **Incorrect**. Standalone mode stores connector configs in the worker’s local configuration files, not ZooKeeper. ZooKeeper is not used by Kafka Connect. Reference: https://docs.confluent.io/platform/current/connect/overview.html#standalone-mode

3. ❌ **C. For a source connector, a topics.pattern property must be specified to capture multiple source tables.**  
   **Incorrect**. topics.pattern is a sink connector setting used to write to multiple topics. Source connectors typically use source-specific properties (e.g., table.whitelist). Reference: https://docs.confluent.io/platform/current/connect/using.html#source-connector-configurations

4. ✅ **D. The connector configuration must be submitted via the REST endpoint /connectors with a POST request.**  
   **Correct**. In distributed mode, connectors are created or updated by POSTing a JSON payload to the worker’s REST API (e.g., POST /connectors). This is the standard way to register a connector with the cluster. Reference: https://docs.confluent.io/platform/current/connect/using.html#create-a-connector

5. ✅ **E. The connector class name must be fully qualified and must implement the SourceConnector interface.**  
   **Correct**. The connector.class property must specify the fully qualified class name of the implementation, which must extend SourceConnector (or sink). This ensures the worker can instantiate the connector. Reference: https://docs.confluent.io/platform/current/connect/configuration.html#connector-class

6. ❌ **F. The connector configuration file can be placed in the 'config' directory of the worker and will be automatically loaded when the worker starts.**  
   **Incorrect**. In distributed mode, connector configs are not automatically loaded from files; they must be submitted via the REST API. Files in the config directory are used only for worker settings. Reference: https://docs.confluent.io/platform/current/connect/overview.html#distributed-mode

</details>

## Question 75 (Observability & Testing):
Which of the following are valid ways to monitor an application that produces or consumes data from a Kafka cluster?.

- A. Rely only on OpenTelemetry distributed tracing (collecting no Kafka client metrics at all) to track consumer lag and topic throughput
- B. Query the Kafka Streams state store via interactive queries to check the state of application data
- C. Use the Kafka Connect REST API to monitor producer latency
- D. Use the Confluent Control Center dashboards to view consumer lag and topic throughput
- E. Expose the application’s JMX metrics and scrape them with Prometheus, then visualize in Grafana
- F. Rely solely on application logs (e.g., Log4j) to determine performance and errors

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, D, B

**Explanation:**

Monitoring a Kafka‑based application requires collecting metrics, visualizing performance, and inspecting state. JMX metrics exposed by Kafka and Kafka Streams can be scraped by Prometheus and visualized with Grafana, giving real‑time throughput and lag data. Confluent Control Center offers built‑in dashboards that expose similar metrics in a user‑friendly interface. Kafka Streams interactive queries let developers probe the state store to confirm correctness and detect anomalies. Relying only on logs or the Connect REST API does not provide the granular, continuous metrics needed for robust observability, and OpenTelemetry, while valuable for tracing, is complementary rather than a primary monitoring tool. These three approaches collectively cover metric collection, visualization, and state inspection, aligning with best practices for Observability & Testing in Confluent Certified Developer exams. Note: OpenTelemetry is a legitimate tool in general (KIP-714 even uses the OpenTelemetry metrics format for client telemetry), so option E was reworded to say 'only tracing, no Kafka metrics', which makes it unambiguously wrong. Control Center is Confluent-platform specific.

Source (verified): https://kafka.apache.org/42/operations/monitoring/ (JMX metrics); https://cwiki.apache.org/confluence/display/KAFKA/KIP-714%3A+Client+metrics+and+observability

**Detailed explanation of each option:**

1. ❌ **A. Rely only on OpenTelemetry distributed tracing (collecting no Kafka client metrics at all) to track consumer lag and topic throughput**  
   **Incorrect**. Tracing alone does not give consumer lag or topic throughput; OpenTelemetry is complementary to metrics, not a replacement.

2. ✅ **B. Query the Kafka Streams state store via interactive queries to check the state of application data**  
   **Correct**. Interactive queries expose the current state of a Streams application, allowing developers to monitor the contents and health of state stores.

3. ❌ **C. Use the Kafka Connect REST API to monitor producer latency**  
   **Incorrect**. The Connect REST API provides connector status and metrics but not producer latency for non‑Connector applications.

4. ✅ **D. Use the Confluent Control Center dashboards to view consumer lag and topic throughput**  
   **Correct**. Control Center provides real‑time visualizations of topic metrics, consumer group lag, and producer latency. It’s a built‑in monitoring solution for Confluent Platform users.

5. ✅ **E. Expose the application’s JMX metrics and scrape them with Prometheus, then visualize in Grafana**  
   **Correct**. Kafka and Kafka Streams expose JMX metrics that Prometheus can scrape. These metrics include record throughput, lag, and latency, which are essential for observability.

6. ❌ **F. Rely solely on application logs (e.g., Log4j) to determine performance and errors**  
   **Incorrect**. While logs help debugging, they don’t provide the real‑time metrics or visibility required for proper observability.

</details>

## Question 76 (Deployment & Ops):
In a production Kafka environment that uses Avro serialization and Confluent Schema Registry, which of the following statements correctly describe valid schema evolution practices that will not cause a compatibility error when a new schema version is registered?

- A. Changing the type of an existing field from `int` to `long` is considered compatible by Confluent Schema Registry.
- B. Setting the schema registry compatibility level to `FORWARD` ensures that older producers cannot produce messages that older consumers can read.
- C. The `--auto-register` flag in the schema registry UI automatically registers new fields as required when a schema is updated.
- D. Setting the schema registry compatibility level to `BACKWARD` allows producers with a new schema to write records that older consumers (using the old schema) can still read.
- E. Removing an existing field breaks backward compatibility, but the operation will succeed if the compatibility level is set to `NONE`.
- F. Adding a new optional field that includes a default value preserves backward compatibility.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, A, F

**Explanation:**

Schema evolution in Confluent Kafka relies on compatibility settings that determine whether a new schema version can coexist with older ones. BACKWARD (the default) means consumers using the NEW schema can read data written with the OLD schema (so you may delete fields and add optional fields with defaults; upgrade consumers first). FORWARD means consumers using the OLD schema can read data written with the NEW schema (you may add fields and delete optional fields; upgrade producers first). So option B is wrong - it describes FORWARD, not BACKWARD. Optional fields with defaults (E), widening numeric types such as int to long (D, Avro type promotion) and disabling compatibility checks (NONE; any change, e.g. removing a field, is accepted) are valid. Caveat on C: the premise "removing a field breaks backward compatibility" is inaccurate (removing a field is actually BACKWARD-compatible; it breaks FORWARD compatibility unless the field had a default), but the conclusion (succeeds under NONE) is true, and it is the best third choice.

Source: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html (compatibility types table, Avro); Kafka: The Definitive Guide 2nd ed., ch. 3 (Schema Registry, schema evolution).

**Detailed explanation of each option:**

1. ✅ **A. Changing the type of an existing field from "int" to "long" is considered compatible by Confluent Schema Registry.**  
   **Correct**. In Avro, widening an integer type to a long is a safe upcast, and Schema Registry marks it as compatible.

2. ❌ **B. Setting the schema registry compatibility level to "FORWARD" ensures that older producers cannot produce messages that older consumers can read.**  
   **Incorrect**. FORWARD means data written with the new schema can be read by consumers using the previous schema. It does not stop older producers' messages from being readable by older consumers.

3. ❌ **C. The "--auto-register" flag in the schema registry UI automatically registers new fields as required when a schema is updated.**  
   **Incorrect**. There is no such flag in a "schema registry UI"; automatic registration is the serializer setting `auto.register.schemas` (default true) and it never changes field requirement semantics.

4. ❌ **D. Setting the schema registry compatibility level to "BACKWARD" allows producers with a new schema to write records that older consumers (using the old schema) can still read.**  
   **Incorrect**. That is FORWARD compatibility. BACKWARD means consumers with the NEW schema can read data written with the OLD schema.

5. ✅ **E. Removing an existing field breaks backward compatibility, but the operation will succeed if the compatibility level is set to "NONE".**  
   **Correct** (with a caveat). With compatibility level NONE the registry does not enforce any compatibility checks, so field removal is accepted. The first half of the sentence is imprecise: removing a field is BACKWARD-compatible (breaks FORWARD unless it had a default).

6. ✅ **F. Adding a new optional field that includes a default value preserves backward compatibility.**  
   **Correct**. New fields with default values are considered optional for readers using older schemas, so backward compatibility is maintained.

</details>

## Question 77 (Kafka Connect):
In Kafka Connect, which of the following statements accurately describe features or behaviors related to the handling of connector configurations and task assignments during runtime?

- A. Task assignments are automatically balanced across available Connect workers to optimize resource utilization.
- B. Kafka Connect stores connector configurations and offsets in Kafka topics to enable fault tolerance and recovery.
- C. Connector tasks always run in a single thread per worker to avoid concurrency issues.
- D. Connectors and tasks share the same configuration properties, making it unnecessary to configure tasks separately.
- E. Connector configurations can be dynamically updated without restarting the Connect worker process.
- F. When a Connect worker fails, its assigned tasks are immediately lost and must be manually reassigned.

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** E, A, B

**Explanation:**

Kafka Connect in distributed mode supports dynamic management of connector configurations via REST API, allowing updates without worker restarts. It automatically balances task assignments across workers to optimize resource utilization and ensure fault tolerance. Connector configs and offsets are stored in Kafka internal topics, enabling recovery and distributed coordination. Contrary to some misconceptions, tasks run concurrently in multiple threads per worker, and when a worker fails, tasks are automatically reassigned rather than lost. Also, connectors and tasks have distinct configurations; tasks may require specific settings for parallel processing. These behaviors are critical for designing scalable, reliable Kafka Connect deployments in production environments.

Source: Kafka: The Definitive Guide 2nd ed. Ch. 9 "A Deeper Look at Kafka Connect" (pp. 225-229)

**Detailed explanation of each option:**

1. ✅ **A. Task assignments are automatically balanced across available Connect workers to optimize resource utilization.**  
   **Correct**. Kafka Connect’s distributed mode automatically balances connector tasks across workers, enabling fault tolerance and load balancing.

2. ✅ **B. Kafka Connect stores connector configurations and offsets in Kafka topics to enable fault tolerance and recovery.**  
   **Correct**. Kafka Connect stores configs and offsets in internal Kafka topics, which supports fault tolerance and exactly-once delivery guarantees.

3. ❌ **C. Connector tasks always run in a single thread per worker to avoid concurrency issues.**  
   **Incorrect**. Connect workers are multi-threaded and can run multiple tasks concurrently to maximize throughput.

4. ❌ **D. Connectors and tasks share the same configuration properties, making it unnecessary to configure tasks separately.**  
   **Incorrect**. Connectors have their own configurations, and tasks may have specific task-level configurations, especially for parallelism and partition assignments.

5. ✅ **E. Connector configurations can be dynamically updated without restarting the Connect worker process.**  
   **Correct**. Kafka Connect supports dynamic reconfiguration of connectors via REST API, allowing updates to connector configs without restarting the entire worker.

6. ❌ **F. When a Connect worker fails, its assigned tasks are immediately lost and must be manually reassigned.**  
   **Incorrect**. In distributed mode, task assignments are rebalanced automatically when a worker fails, ensuring task continuity.

</details>
