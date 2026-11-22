> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Schema Registry and Avro Overview

Confluent Schema Registry and Avro serialization provide a robust way to ensure that Kafka messages conform to a schema, enabling schema evolution and ensuring data compatibility. Understanding these components is essential for building resilient and forward-compatible Kafka applications.

### Schema Registry Key Concepts

- **Centralized Schema Management**: Schema Registry stores and manages Avro, JSON Schema, and Protobuf schemas, ensuring that producers and consumers agree on schema formats.
- **Schema Evolution**: Supports schema evolution with backward, forward, and full compatibility checks, preventing breaking changes.
- **Integration with Kafka**: Integrates with Kafka, enabling schemas to be applied to Kafka messages, ensuring data consistency across the system.

The following schema formats are supported out-of-the-box with Confluent Platform, with serializers, deserializers, and command line tools available for each format:

- **Avro:** Relies on schemas. When Avro data is read, the schema used when writing it is always present.
- **JSON:** A lightweight data-interchange format. It's easy for humans to read and write, and it's easy for machines to parse and generate. JSON itself does not rely on schemas. Schema Registry adds validation using JSON Schema.
- **ProtoBuf:** Protocol Buffers (ProtoBuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data – think XML, but smaller, faster, and simpler.

### Avro 

- **Binary Format**: Avro is a compact binary format that enables efficient serialization and deserialization of data.
- **Schema Evolution**: Avro supports schema evolution, allowing schemas to be updated without breaking existing applications.

The set of primitive types:

- **null**: no value
- **boolean**: a binary value
- **int**: 32-bit signed integer
- **long**: 64-bit signed integer
- **float**: single precision (32-bit) IEEE 754 floating-point number
- **double**: double precision (64-bit) IEEE 754 floating-point number
- **bytes**: sequence of 8-bit unsigned bytes
- **string**: unicode character sequence

Avro supports six types of complex data structures: records, enums, arrays, maps, unions, and fixed.

**Records** are defined with the type name "record" and include the following attributes:

- **name:** A required JSON string that specifies the record's name.
- **namespace:** A JSON string that qualifies the record's name.
- **doc:** An optional JSON string that provides documentation for the schema.
- **aliases:** An optional JSON array of strings that provides alternate names for the record.
- **fields:** A required JSON array that lists the fields of the record.

### Key Advantages of Schema Registry and Avro

#### Centralized Schema Management
- The Schema Registry serves as a centralized repository for storing Avro, JSON Schema, and Protobuf schemas, facilitating schema sharing and enforcement across producers and consumers.

#### Schema Evolution Support
- Both Schema Registry and Avro support schema evolution, allowing schemas to be updated while maintaining compatibility, thus preventing breaking changes.

Backward compatibility: Focus on what the **new system can handle from the old**. It’s about not breaking old producers or data.
Forward compatibility: Concentrate on what the **old system can handle from the new**. It’s about not breaking old consumers with new data.

- **Backward** (default): New schema can read data written in old schema. This means your applications can read old data even after the schema has been updated. Allowed changes:
1. Removing a field (any field)
2. Adding a field with a default value
3. Widening a type via Avro promotion (e.g. int to long)
- **Forward**: Old schema **can read data written in new schema**. This allows applications using an older schema to read data that was produced with a newer schema. Allowed changes:
1. Adding a field (with or without a default)
2. Removing a field that has a default value
- **Full**: both. Only add or remove fields that have default values.
- **Breaking**: Such as changing field types incompatibly, renaming a record or field (without aliases), adding a required field (no default) under BACKWARD, or removing a required field (no default) under FORWARD.
- **Transitive** variants (`BACKWARD_TRANSITIVE`, `FORWARD_TRANSITIVE`, `FULL_TRANSITIVE`) check against all previous versions. The non-transitive modes check only the latest version.
  
```
┌──────────────────────────┬──────────┬─────────┬──────┐
│ Change                   │ Backward │ Forward │ Full │
├──────────────────────────┼──────────┼─────────┼──────┤
│ Add field WITH default   │ ✅       │ ✅      │ ✅  │
│ Add field WITHOUT default│ ❌       │ ✅      │ ❌  │ 
│ Remove field WITH default│ ✅       │ ✅      │ ✅  │
│ Remove field WITHOUT def │ ✅       │ ❌      │ ❌  │
└──────────────────────────┴──────────┴─────────┴──────┘

```

#### Mnemonic: "CF-PS" (Consumer First, Producer Second)
In most cases, it's safer to update the consumer first and then the producer. This approach ensures that the consumer can handle both the old and new schema versions, minimizing the risk of disruption.
To remember the general rule for updating consumers and producers, use the mnemonic "CF-PS":
* **C (Consumer)**: Update the Consumer first
* **F (Forward)**: Consumer can handle forward compatible changes
* **P (Producer)**: Update the Producer second
* **S (Special)**: In Special cases, like **backward compatible** changes or urgent fixes, update the producer first

**Enums:** Adding enum symbols is backward-compatible. Removing enum symbols is a breaking change. Reordering enum symbols is a breaking change. "Add, Remove (break), Reorder (break)" (ARR)
Since Avro 1.9.1 (>= 1.9.1): Default value for enums. Writer's symbol not in reader's enum => Use default value if specified, else error.

| Compatibility   | Change                            |
|-----------------|-----------------------------------|
| Backward        | Delete fields                     | 
| Backward        | Add optional fields               | 
| Forward         | Add fields                        | 
| Forward         | Delete fields with defaults       | 
| Full            | Add fields with defaults          |
| Full            | Delete fields with defaults       |
| Transitive      | Backward/Forward/Full compatibility | 


#### Efficient Data Serialization
- Avro provides a compact, fast, binary data format, significantly reducing the payload size and improving data serialization and deserialization efficiency. 

### Implementing Schema Registry and Avro

#### Schema Registration
- Register schemas via the Schema Registry's REST API to enforce schema consistency across messages.
  ``` 
  # Command to register a schema
  curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
       --data '{ "schema": "{\"type\":\"record\",\"name\":\"Test\",\"fields\":[{\"name\":\"field1\",\"type\":\"string\"}]}" }' \
       http://localhost:8081/subjects/test-topic-value/versions
  ```

#### Avro in Kafka Producers and Consumers
- Utilize Avro serializers and deserializers in Kafka clients, integrating seamlessly with the Schema Registry for schema management.

### Essential Schema Registry and Avro Operations

#### Viewing and Managing Schemas
- List registered schemas or test schema compatibility using the Schema Registry's REST API.
  ``` 
  # List all subjects
  curl -X GET http://localhost:8081/subjects
  # Test schema compatibility
  curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
       --data '{ "schema": "{\"type\":\"record\",\"name\":\"TestNew\",\"fields\":[{\"name\":\"field1\",\"type\":\"string\"}]}" }' \
       http://localhost:8081/compatibility/subjects/test-topic-value/versions/latest
  ```

### Avro Serialization Details

- **Data Types**: Supports both primitive (e.g., int, string) and complex types (e.g., enums, arrays, maps), enabling diverse data representation.
- **Schema Evolution**: Avro allows for backward, forward, and full compatibility modes, facilitating flexible schema updates.

### Schema Registry Integration with Kafka

- **Schema Storage**: Schemas are stored in a Kafka topic (`_schemas`), managed by the Schema Registry, separating schema management from data storage.
- **Security and Efficiency**: Reduces message size by sending schema IDs instead of full schemas with each message, while also supporting secure client communication protocols (HTTP, HTTPS).

### Important Operations and Concepts

- **Registering Schemas**:
  ```
  # Example command to register a schema using the Schema Registry REST API
  curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
    --data '{ "schema": "{\"type\":\"record\",\"name\":\"Test\",\"fields\":[{\"name\":\"field1\",\"type\":\"string\"}]}" }' \
    http://localhost:8081/subjects/test-topic-value/versions
  ```
- **Schema Compatibility**: Configuring compatibility settings in Schema Registry to ensure that schema updates are compatible with consumer expectations.
- **Using Avro with Kafka Producers and Consumers**: Implementing Kafka producers and consumers using Avro serialization requires using specific serializers and deserializers that integrate with Schema Registry.

### Useful Commands

- **Viewing Registered Schemas**:
  ```
  # List all subjects
  curl -X GET http://localhost:8081/subjects
  ```
- **Checking Schema Compatibility**:
  ```
  # Test compatibility of a schema with the latest schema under a subject
  curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
    --data '{ "schema": "{\"type\":\"record\",\"name\":\"TestNew\",\"fields\":[{\"name\":\"field1\",\"type\":\"string\"}]}" }' \
    http://localhost:8081/compatibility/subjects/test-topic-value/versions/latest
  ```

### Schema Registry In-Depth

#### 1. Overview
- Schema Registry is a centralized service for storing and managing schemas used for serializing and deserializing data in Kafka.
- It provides a RESTful API for storing and retrieving schemas, as well as enforcing schema compatibility rules.
- Schema Registry integrates with Kafka clients, allowing them to retrieve schemas for serialization and deserialization.
- It supports multiple serialization formats, including Avro, Protobuf, and JSON Schema.
- Schema Registry ensures data compatibility between producers and consumers by:
 - Storing a schema for each unique topic-key or topic-value combination.
 - Allowing producers and consumers to retrieve schemas based on the topic and key/value type.
 - Enforcing compatibility rules to ensure that producers and consumers use compatible schemas.
 - Rejecting incompatible schemas and ensuring that data can be deserialized correctly by consumers.

#### 2. Schema Compatibility
- Schema compatibility defines which schema changes are allowed, so that producers and consumers using different schema versions can still read each other's data.
- Schema Registry supports seven compatibility types: `BACKWARD` (default), `FORWARD`, `FULL`, their `_TRANSITIVE` variants, and `NONE`. The core four are:
 - `BACKWARD`: Consumers using the new schema can read data produced with the last schema.
   - Allows adding new fields that have a default value.
   - Allows removing fields (with or without a default).
   - Check is against the latest version only (`BACKWARD_TRANSITIVE`: all versions). Default mode.
 - `FORWARD`: Consumers using the last schema can read data produced with the new schema.
   - Allows adding new fields (with or without a default).
   - Allows removing only fields that have a default value.
 - `FULL`: Both `BACKWARD` and `FORWARD` compatibilities are maintained.
   - Allows adding new optional fields.
   - Allows removing fields with default values.
   - Adding or removing fields without defaults is not allowed.
 - `NONE`: No compatibility checks are performed.
- Compatibility can be configured globally or per subject (topic-key or topic-value).
- Schema evolution is supported by allowing compatible schema changes, such as adding optional fields or removing fields with default values.
- When a producer tries to register an incompatible schema:
 - Schema Registry rejects the registration request.
 - The producer receives an error indicating that the schema is incompatible.
 - The producer must update its schema to be compatible with the existing schema before successfully registering the schema and producing data.

Think of "BA" in "BAckward" as standing for "Adding". (Adding, optional, defaults.)
`FORWARD`: "FORward is for FOllowing defaults" (Adding, defaults.)

#### 3. Subject Naming Strategies
- Subjects in Schema Registry represent a unique combination of a topic and a key or value schema.
- Schema Registry supports three subject naming strategies:
 - `TopicNameStrategy` (default): The subject name is the topic name suffixed with `-key` or `-value`.
   - All messages in a topic must have the same schema.
   - Suitable when all messages in a topic have the same schema.
 - `RecordNameStrategy`: The subject name is the fully-qualified name of the record schema.
   - Allows different topics to use the same schema.
   - All topics with the same record name must have the same schema version.
   - Useful when multiple topics share the same schema.
 - `TopicRecordNameStrategy`: The subject name is the topic name concatenated with the record name.
   - Allows different topics to have different schemas for the same record name.
   - Provides flexibility for schema evolution per topic.
- The subject naming strategy determines how schemas are grouped and evolved within Schema Registry.

#### 4. Schema Registry REST API
- Schema Registry exposes a RESTful API for interacting with schemas and subjects.
- Key endpoints include:
 - `POST /subjects/(string: subject)/versions`: Register a new schema version under the specified subject.
 - `GET /subjects/(string: subject)/versions/(versionId: version)`: Retrieve a specific version of the schema registered under the given subject.
 - `POST /compatibility/subjects/(string: subject)/versions/(versionId: version)`: Test schema compatibility against a specified version.
 - `GET /schemas/ids/(int: id)`: Retrieve the schema string associated with the given schema ID.
 - `GET /subjects/(string: subject)/versions/latest`: Retrieve the latest version of a schema for a given subject.
 - `GET /subjects/(string: subject)/versions`: List all version numbers registered under a given subject.
 - `PUT /config/(string: subject)`: Set the compatibility level for a subject (`PUT /config` sets the global level).
- The API allows registering schemas, retrieving schemas by ID or version, and testing schema compatibility.

#### 5. Serializers and Deserializers
- Schema Registry provides serializers and deserializers for Avro, Protobuf, and JSON Schema.
- Serializers and deserializers are used by Kafka producers and consumers to convert between Java objects and Kafka's byte[] (serializers write a magic byte plus the 4-byte schema ID before the payload).
- Key classes include:
 - `KafkaAvroSerializer` and `KafkaAvroDeserializer` for Avro.
 - `KafkaProtobufSerializer` and `KafkaProtobufDeserializer` for Protobuf.
 - `KafkaJsonSchemaSerializer` and `KafkaJsonSchemaDeserializer` for JSON Schema.
- Serializers and deserializers are configured with the Schema Registry URL and handle schema registration and retrieval automatically.
- When a serializer tries to serialize data with an unregistered schema:
 - By default (`auto.register.schemas=true`) the serializer automatically registers the schema with Schema Registry before serializing the data.
 - The serializer makes a call to the Schema Registry API to register the schema and retrieve the schema ID.
 - If the schema registration is successful, the serializer proceeds with serializing the data using the registered schema.
 - If the schema registration fails (e.g., due to incompatibility), the serializer throws an exception, and the data is not serialized.

#### 6. 🚫 Multi-Datacenter Setup
- Schema Registry supports multi-datacenter deployments for high availability and disaster recovery.
- In a multi-datacenter setup, each datacenter has its own Schema Registry instances, but only the primary datacenter accepts writes. The secondary instances are configured as not leader-eligible (`leader.eligibility=false`).
- The `_schemas` topic is copied from the primary to the secondary Kafka cluster with a cross-cluster tool (Confluent Replicator or MirrorMaker), not by Kafka's internal replication.
- Producers and consumers in each datacenter interact with their local Schema Registry cluster for schema registration and retrieval.
- Schema replication in a multi-datacenter setup works as follows:
 - One datacenter is designated as the primary (or master) datacenter, and the others are secondary (or slave) datacenters.
 - When a schema is registered or updated in the primary datacenter, the Schema Registry cluster in the primary datacenter writes the schema to a special Kafka topic (`_schemas` by default).
 - The Schema Registry instances in the secondary datacenters consume the replicated `_schemas` topic and apply the changes locally.
 - Replication is asynchronous, so secondary datacenters are eventually consistent. On primary failure an operator must promote a secondary.

#### 7. 🚫 Schema Registry Security
- Schema Registry supports authentication and authorization to secure access to schemas and the API.
- Authentication mechanisms include:
 - Basic Auth: Username and password-based authentication.
 - SSL/TLS: Encryption and authentication using certificates.
 - OAuth/OIDC (in newer Confluent Platform versions).
- Authorization of subjects/API endpoints is provided by Confluent add-ons (e.g. RBAC, Schema Registry ACL authorizer), which are outside the exam scope.
- Securing Schema Registry's own connection to Kafka is configured with the `kafkastore.*` properties (e.g. `kafkastore.security.protocol`, `kafkastore.sasl.*`, `kafkastore.ssl.*`).
- Securing the REST API is configured separately (e.g. `listeners` with `https://`, `authentication.method=BASIC`).
- Clients provide credentials with `basic.auth.credentials.source` and `basic.auth.user.info` (or SSL key/trust stores).

#### 8. 🚫 Confluent Control Center Integration
- Schema Registry integrates with Confluent Control Center, a web-based user interface for managing and monitoring Kafka clusters.
- Control Center provides a graphical interface for viewing and managing schemas, subject compatibility, and schema evolution.
- It allows searching for schemas, viewing schema details, and testing schema compatibility.
- Control Center also provides monitoring and alerting capabilities for Schema Registry, including metrics on schema registration, retrieval, and compatibility checks.
- To view the schema history for a subject in Confluent Control Center:
 - Navigate to the "Schema Registry" section.
 - Select the desired subject from the list of available subjects.
 - In the subject details page, the schema history is displayed, including the version number, schema, and timestamp of each registered schema version.
 - Different versions of the schema can be compared to see the changes between them.
 - Control Center provides a user-friendly interface to explore the schema history and track the evolution of schemas over time.

#### 9. Best Practices
- Use a meaningful and consistent subject naming convention based on your use case and subject naming strategy.
- Define schemas with appropriate compatibility rules to allow for schema evolution while maintaining compatibility.
- Use Avro, Protobuf, or JSON Schema for strong typing and schema validation.
- Ensure that producers and consumers are configured with the correct serializers and deserializers that match the schemas.
- Monitor Schema Registry metrics and logs to identify any issues or performance bottlenecks.
- Implement proper security measures, such as authentication and authorization, to protect sensitive schema information.
- Use Schema Registry in conjunction with Kafka Connect (and Kafka Streams) to enable seamless data integration and stream processing with schema validation.
- Common schema evolution use cases include:
 - Adding a new optional field to a schema: Producers can start including the new field in the data, while consumers can handle data with or without the field.
 - Removing an existing field from a schema: Producers can stop including the field in the data, and consumers can handle data with or without the field (assuming a default value is provided).
 - Renaming a field: Add a new field with the new name and mark the old field as deprecated. Consumers can handle both the old and new field names until the old field is completely removed.
 - Changing the data type of a field: This requires careful consideration and may involve a multi-step process, such as adding a new field with the new data type and gradually migrating producers and consumers to use the new field.
 - Evolving schemas in a backward or forward compatible manner allows for smooth updates and reduces the risk of data incompatibility between producers and consumers.

### Additional Key Concepts

#### Schema Validation
- **Validation**: Ensure that the schema conforms to the expected structure and data types.
  - The Schema Registry provides a way to validate schemas before registering them.
  - Validation helps to catch errors early and enforce schema correctness.
- **Schema References**: Use schema references to manage shared schemas and reduce redundancy.
  - Particularly useful for complex schema structures.
  - References can help maintain consistency and ease of schema updates.

#### Advanced Avro Features
- **Logical Types**: Utilize logical types in Avro for precise representations of specific data types.
  - Examples: dates, times, decimal values.
  - Improves readability and interoperability of data.
- **Default Values**: Define default values for fields to handle missing data gracefully.
  - Important for schema evolution and backward compatibility.
  - Helps ensure that older consumers can still process newer data.

### Implementing Schema Registry and Avro

#### Configuration Tips
- **Global Compatibility Setting**: Configure a global compatibility level for the Schema Registry.
  - Ensures consistent schema evolution policies across all subjects.
  - Reduces the risk of introducing breaking changes.
- **Caching**: Enable caching for schema lookups to improve performance.
  - Particularly beneficial in high-throughput environments.
  - Reduces latency in schema retrievals.

#### Monitoring and Metrics
- **Metrics Collection**: Use monitoring tools to track metrics related to schema operations.
  - Confluent Control Center is a recommended tool.
  - Metrics to track: schema registrations, retrievals, compatibility checks.
- **Alerting**: Set up alerts for common issues.
  - Schema compatibility violations.
  - High latency in schema retrievals.

### Kafka Streams and Schema Registry Integration
- **Kafka Streams**: Integrate Schema Registry with Kafka Streams for stream processing.
  - Use `SpecificAvroSerde` or `GenericAvroSerde` for serialization and deserialization.
  - Ensure schema compatibility to avoid runtime errors.

### Avro Serialization Details

#### Custom Avro Conversions
- **Custom Conversions**: Implement custom conversions for complex data types.
  - Useful for types not natively supported by Avro.
  - Can include certain Java objects or third-party library types.
  - Enhances flexibility in handling diverse data formats.

### 🚫 Security and Governance

#### Data Governance
- **Schema Governance**: Implement schema governance policies.
  - Manage schema lifecycle, access control, and audit logging.
  - Maintains data quality and ensures compliance with regulations.
- **Schema Evolution Strategies**: Plan and document schema evolution strategies.
  - Include versioning conventions and deprecation policies.
  - Ensures smooth transitions and minimizes disruptions.

### Common Issues and Troubleshooting

#### Debugging Tips
- **Schema Not Found**: Ensure correct configuration for producer and consumer.
  - Verify the Schema Registry URL.
  - Check that schemas are correctly registered.
- **Serialization Errors**: Common issues and resolutions.
  - Missing schemas: Ensure schemas are registered before producing data.
  - Incompatible schema changes: Review schema compatibility settings.
  - Incorrect data types: Validate data against the schema.

### Additional Useful Commands

#### Schema Deletion
- **Deleting Schemas**: Use Schema Registry API for schema deletion.
  - Ensure deletion does not impact existing consumers.
  ```
  # Delete a specific schema version
  curl -X DELETE http://localhost:8081/subjects/test-topic-value/versions/1
  ```

#### Bulk Operations
- **Bulk Schema Retrieval**: Retrieve all versions of a schema.
  - Useful for auditing or migration purposes.
  ```
  # Retrieve all versions of a schema
  curl -X GET http://localhost:8081/subjects/test-topic-value/versions
  ```
