> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Kafka REST Proxy Overview 🚫
The Kafka REST Proxy provides a RESTful interface to a Kafka cluster, enabling the production and consumption of Kafka messages over HTTP. It's a critical component for integrating non-JVM applications with Kafka.

### Key Points for CCDAK on REST Proxy
- **Accessibility**: Allows applications that cannot use Kafka's native client libraries to interact with Kafka topics via HTTP requests.
- **Integration**: Simplifies integration with web-based applications and services, enabling a broader range of technologies to connect with Kafka.

### Important Features of Kafka REST Proxy
#### HTTP-Based Interaction
- **Scope**: Client-Server Communication
- **Description**: Facilitates the production and consumption of messages through standard HTTP methods, making Kafka accessible from any language that can make HTTP requests.
- **Impact**: Broadens Kafka's usability beyond traditional back-end systems to front-end and external systems without native Kafka support.

#### Consumer Group Management
- **Scope**: Consumption
- **Description**: Supports the creation and management of consumer groups via RESTful endpoints, allowing detailed control over message consumption.
- **Impact**: Enables efficient message processing and load balancing across multiple consumers using standard web technologies.

### Essential REST Proxy Configuration Parameters
#### Proxy Server Settings
- **`listeners`**: Configures the network address the REST Proxy listens on, defining how clients connect to the proxy.
- **`host.name`** (deprecated in favour of `listeners`/`advertised.listeners`): Host name advertised to clients, e.g. in consumer instance base URIs.
- **`bootstrap.servers`** / **`schema.registry.url`**: Kafka cluster and Schema Registry the proxy connects to. Settings prefixed with `producer.`, `consumer.`, `client.` are passed to the embedded clients.

#### Security and Authentication
- 🚫 **`authentication.method`**: `NONE` (default) or `BASIC` (with `authentication.roles` and `authentication.realm` and a JAAS login module) to control access to the REST Proxy.
- 🚫 **HTTPS**: Use an `https://` URL in `listeners` plus `ssl.keystore.*` settings (there is no `ssl.enabled` property); proxy-to-broker security uses `client.*` settings.

### Advanced REST Proxy Configurations for Fine-Tuning
#### Request and Consumer Settings
- **`consumer.request.timeout.ms`**: Maximum time a consume request waits for records if `consumer.request.max.bytes` has not been reached (default 1000 ms).
- **`consumer.instance.timeout.ms`**: Idle time after which a consumer instance is automatically destroyed if no further requests are received (default 300000 ms). Helps manage server load and resource allocation.

#### Producing and Consuming Enhancements
- **`consumer.request.max.bytes`**: Maximum number of bytes of message data returned in a single consume response.
- **`consumer.fetch.min.bytes`** (and other `consumer.`-prefixed settings): Passed through to the embedded Kafka consumers.
- Legacy: the old v1 API and its simple consumer settings (e.g. `simple.consumer.pool.size.max`) are deprecated; use the v2 (and v3) APIs.

### Key Considerations for Scalability and Reliability
#### Load Balancing
- Utilizing multiple REST Proxy instances behind a load balancer can help distribute client requests evenly, improving throughput and reducing latency.

#### High Availability
- Deploying REST Proxy instances in different physical locations or availability zones can increase fault tolerance and ensure continuous availability of services.

#### Monitoring and Management
- Monitoring the REST Proxy's performance and logs is crucial for maintaining an efficient and reliable system, enabling proactive management of potential issues.

### Additional Points for CCDAK on REST Proxy
#### Data Formats
- The REST Proxy supports various embedded data formats for producing and consuming messages, including JSON, binary, Avro, Protobuf and JSON Schema. The format is chosen via the `Content-Type` header when producing (e.g. `application/vnd.kafka.json.v2+json`) and the `format` field when creating a consumer instance.
- It integrates with the Confluent Schema Registry for schema-based serialization and deserialization (`value_schema` / `value_schema_id` fields).
- For the binary format the data must be base64 encoded by the producer (and is returned base64 encoded to consumers); JSON and schema-based formats are sent as plain JSON.
- Produce requests use `POST /topics/{topic}`; consumers are created with `POST /consumers/{group}`, then subscribed, polled with `GET .../records`, and offsets committed explicitly or automatically. Offsets are stored by the Kafka brokers in `__consumer_offsets`.
- The REST Proxy is a Confluent component (also reimplemented by Karapace), not part of Apache Kafka.

#### Authentication and Authorization
- 🚫 The REST Proxy supports HTTP Basic authentication and TLS (HTTPS, optionally client certificates) for access control at the HTTP layer.
- 🚫 Towards Kafka, the proxy uses its own configured principal, so Kafka ACLs apply to the proxy's identity; per-user principal propagation requires Confluent security plugins (RBAC, out of exam scope).

#### Error Handling and Response Codes
- The REST Proxy handles errors and returns appropriate HTTP response codes for different scenarios, such as invalid requests, authentication failures, or Kafka-related errors.
- Clients can handle and interpret these response codes to effectively deal with errors and take appropriate actions.

#### Performance Considerations
- Using the REST Proxy introduces some performance overhead compared to using Kafka's native client libraries directly.
- It's important to consider the trade-offs between ease of use and performance when deciding to use the REST Proxy.

#### Monitoring and Metrics
- The REST Proxy provides metrics and monitoring endpoints for tracking its health and performance.
- These metrics can be integrated with monitoring tools and dashboards for effective monitoring and alerting.

#### Integration with Confluent Platform
- The REST Proxy integrates with the Confluent Schema Registry for schema-based formats.
- 🚫 Confluent Platform-specific management features (e.g. Control Center, RBAC) are outside the exam scope.