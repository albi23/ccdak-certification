> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1

When using the Confluent REST Proxy to produce messages, what happens if the `value_schema_id` is provided in the request payload?

- A. The REST Proxy validates the payload against the schema specified by the ID
- B. The REST Proxy retrieves the schema from the Schema Registry and includes it in the produced message
- C. The REST Proxy ignores the `value_schema_id` field and produces the message without any schema information
- D. The REST Proxy returns an error indicating that the `value_schema_id` is not supported

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
When producing messages through the Confluent REST Proxy, you can optionally provide the `value_schema_id` field in the request payload to specify the schema ID for the message value.

If the `value_schema_id` is provided, the REST Proxy performs the following steps:

1. It retrieves the schema corresponding to the specified ID from the Schema Registry.
2. It converts/validates the JSON payload against the retrieved schema (Avro, Protobuf or JSON Schema, depending on the Content-Type) to ensure that the payload adheres to the schema structure.
3. If the validation succeeds, the REST Proxy produces the message to the specified Kafka topic.
4. If the validation fails, the REST Proxy returns an error indicating that the payload does not match the schema.

By providing the `value_schema_id`, you can ensure that the message payload conforms to a specific schema before it is produced to Kafka. This helps maintain data consistency and avoids producing invalid or malformed messages.

Statement B is incorrect because the REST Proxy does not embed the schema itself in the produced message. The Avro serializer only prefixes the record with the schema ID (Confluent wire format: magic byte + 4-byte schema ID); the schema stays in the Schema Registry.

Statement C is incorrect because the REST Proxy does not ignore the `value_schema_id` field. It uses it to validate the payload against the specified schema.

Statement D is incorrect because the REST Proxy supports the `value_schema_id` field and uses it for schema validation. It does not return an error indicating that the field is not supported.

</details>

## Question 2

How does the Confluent REST Proxy (API v2) determine the embedded data format (e.g. JSON, binary, Avro) of record keys and values?

- A. Through the `key.converter` and `value.converter` configurations of the REST Proxy
- B. Through the Content-Type header of produce requests (e.g. `application/vnd.kafka.json.v2+json`) and the `format` field when creating a consumer instance
- C. Through the compression type configured on the topic
- D. Through the schema ID configured in the broker

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The REST Proxy always exchanges HTTP request/response bodies as JSON, but the embedded format of the keys and values is chosen per request:

- When producing, the `Content-Type` header selects the format: `application/vnd.kafka.json.v2+json`, `application/vnd.kafka.binary.v2+json` (base64-encoded bytes), `application/vnd.kafka.avro.v2+json` (also `protobuf` and `jsonschema`). For schema formats, the request contains `key_schema`/`value_schema` or `key_schema_id`/`value_schema_id`.
- When consuming, the `format` field (`json`, `binary`, `avro`, ...) is set when the consumer instance is created, and the `Accept` header must match it.

Statement A is incorrect because `key.converter` and `value.converter` are Kafka Connect worker/connector settings, not REST Proxy settings.

Statement C is incorrect because compression is a producer/topic setting unrelated to the REST payload format.

Statement D is incorrect because schema IDs are provided in the request payload (and resolved through the Schema Registry), not configured in the broker.

</details>

## 🚫 Question 3

How does the Confluent REST Proxy handle authentication and authorization for production and consumption of messages?

- A. The REST Proxy performs authentication and authorization based on the Kafka ACLs configured in the brokers
- B. The REST Proxy uses its own authentication and authorization mechanism independent of Kafka
- C. The REST Proxy relies on the Schema Registry for authentication and authorization
- D. The REST Proxy does not support authentication and authorization

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The Confluent REST Proxy uses its own authentication and authorization mechanism independent of Kafka for controlling access to the production and consumption of messages through the REST API.

When configuring the REST Proxy, you can enable HTTP-layer authentication (`authentication.method=BASIC` with `authentication.roles`/`authentication.realm` and a JAAS login module) or TLS client authentication on its HTTPS listener.

This authentication operates at the REST API layer and is separate from the Kafka brokers' security: the proxy connects to the brokers with its own configured identity (e.g. SASL/SSL settings with the `client.` prefix), so Kafka ACLs apply to the proxy's principal, not to each HTTP client. Propagating the end-user principal to the brokers requires Confluent's security plugins (RBAC), which is outside the exam scope.

Statement A is incorrect because the HTTP clients are not authenticated against Kafka ACLs by default; ACLs only see the proxy's own principal.

Statement C is incorrect because the REST Proxy does not use the Schema Registry for authentication and authorization. The Schema Registry is used for schema management, not security.

Statement D is incorrect because the REST Proxy does support authentication and authorization through its own mechanism. It is not true that it lacks support for these security features.

</details>

## Question 4

What is the purpose of the Kafka REST Proxy?

- A. To provide a RESTful interface for producing and consuming messages in Kafka
- B. To manage Kafka clusters and monitor their health
- C. To store and retrieve Avro schemas for Kafka messages
- D. To stream data between Kafka and external systems

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The primary purpose of the Kafka REST Proxy is to provide a RESTful interface for producing and consuming messages in Kafka. It allows applications that are not built using Kafka's native libraries to interact with Kafka clusters using standard HTTP requests.

The REST Proxy exposes endpoints for producing messages to Kafka topics and consuming messages from Kafka topics. It acts as a bridge between non-Kafka applications and Kafka, enabling seamless integration and communication.

</details>

## Question 5

Which HTTP method is used to produce messages to a Kafka topic via the REST Proxy?

- A. GET
- B. POST
- C. PUT
- D. DELETE

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
To produce messages to a Kafka topic using the Kafka REST Proxy, you need to send a POST request to the appropriate endpoint. The POST method is used to submit data to be processed to a specified resource, which in this case is a Kafka topic.

The REST Proxy expects the message data to be included in the request body, typically in JSON format. It then forwards the message to the Kafka broker, which appends it to the specified topic.

</details>

## Question 6

How does the Kafka REST Proxy handle consumer offsets?

- A. It stores consumer offsets in its own local database
- B. It manages consumer offsets using ZooKeeper (removed in Kafka 4.0)
- C. It relies on the Kafka brokers to store consumer offsets
- D. It does not manage consumer offsets

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
The Kafka REST Proxy relies on the Kafka brokers to store and manage consumer offsets. When a consumer instance is created through the REST Proxy, it joins a consumer group, and offsets are committed to the Kafka brokers either automatically (if `auto.commit.enable` is set to true when creating the instance) or explicitly with `POST /consumers/{group}/instances/{instance}/offsets`.

Kafka brokers maintain the offsets for each consumer group in a special internal topic called `__consumer_offsets`. The REST Proxy does not directly manage or store consumer offsets itself. Instead, it leverages the native offset management mechanism provided by Kafka.

</details>

## 🚫 Question 7

What is the purpose of the `consumer.request.timeout.ms` configuration parameter in the Kafka REST Proxy?

- A. To set the maximum time to wait for a message to be consumed
- B. To set the maximum time to wait for a response from the Kafka broker
- C. To set the maximum time to keep a consumer instance alive without further requests
- D. To set the maximum time to wait for a consumer to join a consumer group

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
`consumer.request.timeout.ms` is the maximum total time the REST Proxy waits for messages when serving a consume (`GET .../records`) request, if the maximum response size (`max_bytes`/`consumer.request.max.bytes`) has not been reached yet (default 1000 ms). The request then returns whatever records were collected.

The idle lifetime of a consumer instance is controlled by a different setting, `consumer.instance.timeout.ms` (default 300000 ms): instances with no requests within that time are automatically destroyed, which is what option C describes. `consumer.request.timeout.ms` is also not a broker response timeout (B) nor a group-join timeout (D).

</details>

## 🚫 Question 8

How does the Kafka REST Proxy handle authentication?

- A. It uses Kafka's native authentication mechanisms
- B. It supports basic authentication using username and password
- C. It relies on SSL/TLS for authentication
- D. It does not provide built-in authentication mechanisms

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The Kafka REST Proxy supports basic authentication using username and password. It allows clients to include authentication credentials in the HTTP request headers to authenticate themselves when making requests to the REST Proxy.

To enable authentication in the REST Proxy, you need to configure the `authentication.method` parameter in the REST Proxy's configuration file (`BASIC`, or `NONE` by default), together with `authentication.roles` and `authentication.realm` pointing to a JAAS login module. TLS client authentication (`ssl.client.authentication`) is an alternative on an HTTPS listener.

When authentication is enabled, clients must include the appropriate authentication headers in their requests to access the REST Proxy endpoints. The REST Proxy validates the provided credentials against the configured authentication mechanism before allowing access to the requested resources.

</details>

## Question 9

What is the role of the optional `partition` field of a record in a produce request (API v2) to the Kafka REST Proxy?

- A. It specifies the Kafka topic to produce the message to
- B. It specifies the partition the record is sent to, instead of using the partitioner
- C. It represents the key of the message
- D. It is a client-side identifier that is ignored by Kafka

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In `POST /topics/{topic}` (v2) the request body has a `records` array, and each record has a `value`, an optional `key`, and an optional `partition`. When `partition` is set, the record is written to that partition; otherwise the producer's default partitioner chooses it (based on the key hash, or sticky/round-robin without a key). The topic is part of the URL path, not the payload, and the key is the `key` field. The response lists, for each record, the `partition` and `offset` it was written to (or an `error_code`).

There is no `id` field in the produce payload.

</details>

## 🚫 Question 10

How can you configure the Kafka REST Proxy to use SSL/TLS for secure communication?

- A. Configure an `https://` listener in `listeners` and set the `ssl.keystore.*` properties in the REST Proxy configuration
- B. Enable SSL/TLS in the Kafka broker configuration
- C. Configure SSL/TLS in the client application code
- D. No additional configuration is required

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
To configure the Kafka REST Proxy to use SSL/TLS for secure communication with its HTTP clients, you set an `https://` URL in the `listeners` configuration (there is no `ssl.enabled` property) and provide the keystore with `ssl.keystore.location`, `ssl.keystore.password`, `ssl.key.password`, and other relevant `ssl.*` parameters.

By default, the REST Proxy listens on plain-text HTTP (`http://0.0.0.0:8082`). Securing the proxy-to-broker connection is configured separately with the `client.*` prefixed properties (e.g. `client.security.protocol=SSL`).

Clients communicating with the REST Proxy over SSL/TLS need to use the HTTPS protocol and ensure that they trust the SSL/TLS certificate presented by the REST Proxy.

Enabling SSL/TLS in the Kafka broker configuration is not directly related to configuring SSL/TLS for the REST Proxy itself. The REST Proxy acts as a separate entity and requires its own SSL/TLS configuration.

</details>
