> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1

Where does Confluent Schema Registry store the registered schema information?

- A. In Zookeeper under the `/schemas` znode
- B. In a special Kafka topic named `_schemas`
- C. In a relational database configured in Schema Registry
- D. In the Kafka broker's `schema` directory on disk

<details>
<summary>Response:</summary> 

**Explanation:**
Confluent Schema Registry uses a special Kafka topic named `_schemas` to store the registered schema information. Each registered schema is stored as a message in this topic (the topic is compacted and has a single partition). Schema Registry keeps an in-memory cache built by consuming this topic.

- A: Schemas are never stored in Zookeeper (current Schema Registry versions do not use Zookeeper at all, and Kafka 4.x has no Zookeeper).
- C: Schema Registry does not use a relational database for schema storage by default. It leverages Kafka for reliable schema storage.
- D: Schemas are not stored on the Kafka broker's disk directly.

**Answer:** B

</details>

## Question 2

What serialization formats are supported by the Confluent Schema Registry for storing schemas? (Select all that apply)

- A. Avro
- B. Protobuf
- C. JSON Schema
- D. XML Schema
- E. Thrift

<details>
<summary>Response:</summary> 

**Explanation:**
The Confluent Schema Registry currently supports three serialization formats for storing schemas:

1. Apache Avro: Avro is a row-based serialization format that is compact, fast, and binary. It's the most commonly used format with the Schema Registry.
2. Protocol Buffers (Protobuf): Protobuf is Google's data interchange format. It's also compact and fast, and it supports schema evolution.
3. JSON Schema: JSON schema is a schema format for JSON, supported by the Schema Registry.

The other options are not currently supported:

- D (XML Schema) is a schema format for XML, but it's not supported by the Schema Registry for schema storage.
- E (Thrift) is another serialization format, but it's not currently supported by the Schema Registry.

**Answer:** A, B, C

</details>

## Question 3

Which of the following programming languages have official client libraries for interacting with the Confluent Schema Registry? (Select all that apply)

- A. Java
- B. Python
- C. Go
- D. C++
- E. JavaScript
- F. Ruby

<details>
<summary>Response:</summary> 

**Explanation:**
Confluent provides official Schema Registry clients for the following programming languages (among others, e.g. .NET):

1. Java: The Java client is part of the `kafka-schema-registry-client` library.
2. Python: The Python client is provided by the `confluent-kafka` Python package.
3. Go: The Go client is part of the `confluent-kafka-go` package.
4. JavaScript: The `confluent-kafka-javascript` package includes a Schema Registry client.

The other options do not currently have official client libraries from Confluent:

- D (C++) and F (Ruby) can still interact with the Schema Registry using its REST API, but there are no official Schema Registry client libraries provided by Confluent for these languages.

**Answer:** A, B, C, E

</details>

## Question 4

What is the purpose of the compatibility setting in the Confluent Schema Registry?

- A. It defines which serialization format (Avro, Protobuf) is used.
- B. It controls how schemas can evolve over time.
- C. It sets the compatibility between different Schema Registry versions.
- D. It configures compatibility between the Schema Registry and Kafka brokers.

<details>
<summary>Response:</summary> 

**Explanation:**
The compatibility setting in the Confluent Schema Registry is used to control schema evolution. It defines the rules for how a schema can change over time while still being considered compatible with previous versions.

The available compatibility settings are:

- BACKWARD: A new schema can be used to read data written by an old schema.
- FORWARD: An old schema can be used to read data written by a new schema.
- FULL: Both BACKWARD and FORWARD compatibilities are maintained.
- NONE: No compatibility checks are performed.
- BACKWARD_TRANSITIVE, FORWARD_TRANSITIVE, FULL_TRANSITIVE: the same checks, but against all previous versions instead of only the latest one.

The other options are incorrect:

- A is incorrect because the serialization format is not controlled by the compatibility setting.
- C is incorrect because the compatibility setting is about schema versions, not Schema Registry versions.
- D is incorrect because the compatibility setting does not configure compatibility with Kafka brokers.

**Answer:** B

</details>

## Question 5

In Avro, what is the effect of adding a field to a record schema without a default value?

- A. It is a backward compatible change
- B. It is a forward compatible change
- C. It is both a backward and forward compatible change
- D. It is an incompatible change

<details>
<summary>Response:</summary> 

**Explanation:**
In Avro, adding a field to a record schema without a default value is a forward compatible change. It only breaks backward compatibility.

- It is forward compatible because data written with the new schema can be read by code using the old schema. The old schema will simply ignore the added field.
- It breaks backward compatibility because data written with the old schema cannot be read by code using the new schema. The new schema will expect the new field to be present, but it will be missing in the old data.

To make adding a field backward compatible as well, you must provide a default value for the new field. This allows old data to be read by new code (the default is used for the missing field).

Therefore, statements A, C, and D are incorrect.

**Answer:** B

</details>

## Question 6

What is the Avro schema evolution rule for removing a field without default value?

- A. It is always a compatible change
- B. It is a backward compatible change
- C. It is a forward compatible change
- D. It is an incompatible change

<details>
<summary>Response:</summary> 

**Explanation:**
In Avro, removing a field from a record schema is a backward compatible change, but not a forward compatible change.

- It is backward compatible because data written with the old schema can be read by code using the new schema. The new schema simply ignores the removed field when reading old data.
- It is forward compatible only if the removed field had a default value in the old schema (the old reader then fills in the default). Removing a field without a default breaks forward compatibility, because the old schema expects the field but it is missing in the new data.

Therefore, removing a field always allows new code to read old data (backward compatibility); old code can read new data (forward compatibility) only if the removed field had a default.

Statements A and C are incorrect because removing a field is not always compatible or forward compatible. Statement D is incorrect because removing a field is backward compatible, not completely incompatible.

**Answer:** B

</details>

## Question 7

In Avro, what is the compatibility implication of changing the name of a record schema?

- A. It is a backward compatible change
- B. It is a forward compatible change
- C. It is both a backward and forward compatible change
- D. It is an incompatible change

<details>
<summary>Response:</summary> 

**Explanation:**
In Avro, changing the name of a record schema is an incompatible change. It breaks both backward and forward compatibility.

Avro schema resolution matches the writer's and reader's record by (full) name. Avro binary data does not contain the name itself, but the schema used to write it does, and the reader's schema must match it.

If the name of a record is changed (and no alias is defined):

- Data written with the old name cannot be resolved against the new reader schema, because the names do not match. This breaks backward compatibility.
- Data written with the new name cannot be resolved against the old reader schema. This breaks forward compatibility.

Note: Avro `aliases` on the reader schema can make a rename resolvable, but without aliases a rename is incompatible.

Therefore, changing the name of a record schema is an incompatible change. Statements A, B, and C are incorrect.

To evolve a schema while maintaining compatibility, you should not change the name of the schema. Instead, you should evolve the fields within the schema following the Avro compatibility rules.

**Answer:** D

</details>

## Question 8

What happens when a Kafka consumer using KafkaAvroDeserializer encounters a message without a schema ID?

- A. The consumer throws a SerializationException
- B. The consumer skips the message and moves to the next one
- C. The consumer attempts to deserialize the message using the latest schema
- D. The consumer falls back to using the GenericRecord deserializer

<details>
<summary>Response:</summary> 

**Explanation:**
When a Kafka consumer using the KafkaAvroDeserializer encounters a message that does not include a schema ID, it will throw a SerializationException.

The KafkaAvroDeserializer expects messages to be serialized with Confluent Schema Registry and to include the schema ID as part of the message payload. The schema ID is used to retrieve the corresponding schema from the Schema Registry for deserialization.

If a message does not contain a schema ID, the deserializer is unable to determine which schema to use for deserialization, and it cannot proceed. In this case, it will throw a SerializationException to indicate that the message cannot be deserialized due to the missing schema ID.

It's important to ensure that the producer is properly configured to use the KafkaAvroSerializer and that it is registering the schemas with the Schema Registry. This way, the produced messages will include the necessary schema ID for the consumer to deserialize them correctly.

Statement B is incorrect because the consumer does not skip messages without a schema ID. It throws an exception instead (typically "Unknown magic byte!", since Confluent-serialized messages start with a magic byte followed by a 4-byte schema ID).

Statement C is incorrect because the consumer cannot attempt to deserialize the message using the latest schema if there is no schema ID present. It needs the schema ID to retrieve the correct schema.

Statement D is incorrect because the consumer does not fall back to using a different deserializer when the schema ID is missing. The KafkaAvroDeserializer specifically relies on the schema ID for deserialization.

**Answer:** A

</details>

## Question 9

How can you handle a SerializationException thrown by the KafkaAvroDeserializer in a Kafka consumer?

- A. Catch the exception and retry deserializing the message with a different deserializer
- B. Catch the exception and skip the problematic message by committing its offset
- C. Catch the exception and manually retrieve the schema from the Schema Registry for deserialization
- D. Let the exception propagate and handle it at a higher level in the consumer application

<details>
<summary>Response:</summary> 

**Explanation:**
When a Kafka consumer using the KafkaAvroDeserializer encounters a SerializationException due to a missing schema ID or other deserialization issues, the exception surfaces from `poll()` (in recent clients wrapped in a `RecordDeserializationException`, which carries the partition and offset of the bad record). One way to handle it is to catch the exception and skip the problematic message by moving past its offset.

Here's how you can approach this:

1. Surround the code that consumes and processes the messages with a try-catch block.
2. In the catch block, if the exception is a SerializationException, log an error message indicating the failed deserialization.
3. Move past the problematic record: `seek()` to the failed offset + 1 (the next `poll()` would otherwise fail on the same record again) and commit offsets with commitSync() or commitAsync(). This tells Kafka that the consumer has processed the message, even though it couldn't deserialize it.
4. Continue consuming the next message.

- B. By skipping past the offset of the problematic message, the consumer acknowledges that it has processed the message and moves on to the next one. This prevents the consumer from getting stuck on the same message indefinitely.

However, it's important to note that skipping messages should be done with caution and only after careful consideration. Skipping messages means losing data, so it's crucial to have proper error handling and monitoring in place to detect and investigate such incidents.

Statement A is incorrect because retrying deserialization with a different deserializer is not a recommended approach. The KafkaAvroDeserializer is specifically designed to work with Confluent Schema Registry and Avro-serialized messages.

Statement C is incorrect because manually retrieving the schema from the Schema Registry is not a practical solution. The deserializer should handle schema retrieval automatically based on the schema ID.

Statement D is partially correct, as letting the exception propagate and handling it at a higher level is another valid approach. However, it doesn't address the specific action of skipping the problematic message by committing its offset.

**Answer:** B

</details>

## Question 10

What are the benefits of using Confluent Schema Registry and KafkaAvroDeserializer in a Kafka consumer?

- A. Automatic schema evolution and compatibility checks
- B. Improved deserialization performance compared to generic deserializers
- C. Ability to deserialize messages without knowing the schema upfront
- D. All of the above

<details>
<summary>Response:</summary> 

**Explanation:**
Using Confluent Schema Registry and KafkaAvroDeserializer in a Kafka consumer offers several benefits:

1. Automatic schema evolution and compatibility checks:
   - The Schema Registry allows you to store and manage schemas for your Kafka messages.
   - It enables schema evolution by allowing you to define compatibility rules for schema changes.
   - The KafkaAvroDeserializer automatically retrieves the appropriate schema from the Schema Registry based on the schema ID included in the message.
   - It ensures that the consumer can deserialize messages even if the schema has evolved, as long as the changes are compatible.

2. Improved deserialization performance compared to generic deserializers:
   - The KafkaAvroDeserializer is optimized for deserializing Avro-serialized messages.
   - It leverages the compact and efficient binary format of Avro, resulting in faster deserialization compared to generic deserializers like JSON.
   - The deserializer also benefits from the schema information stored in the Schema Registry, enabling efficient deserialization without the overhead of including the full schema in each message.

3. Ability to deserialize messages without knowing the schema upfront:
   - When using the KafkaAvroDeserializer, the consumer does not need to have prior knowledge of the schema for the messages it consumes.
   - The deserializer automatically retrieves the schema from the Schema Registry based on the schema ID included in the message.
   - This allows the consumer to deserialize messages from multiple topics or with different schemas without requiring explicit schema management in the consumer code.

By leveraging Confluent Schema Registry and KafkaAvroDeserializer, Kafka consumers can benefit from automatic schema evolution, improved deserialization performance, and the ability to deserialize messages without prior knowledge of the schema. These features simplify the development and maintenance of Kafka consumers while ensuring data compatibility and efficiency.

**Answer:** D

</details>
# Question 11

Which configuration is used to define the schema registry URL in Kafka clients?

- A. `schema.registry.url`
- B. `schema.registry.endpoint`
- C. `schema.registry.address`
- D. `schema.registry.host`

<details>
<summary>Response:</summary> 

**Explanation:**
The configuration `schema.registry.url` is used to specify the URL of the Confluent Schema Registry in Kafka clients. This URL is necessary for the clients to connect to the Schema Registry and retrieve the schemas.

- Options B, C, and D are incorrect as these are not the correct configuration properties for setting the schema registry URL in Kafka clients.

**Answer:** A

</details>

## Question 12

What is the primary purpose of a subject in the Confluent Schema Registry?

- A. To group schemas by type (Avro, Protobuf, JSON Schema)
- B. To manage versions of a schema for a specific topic or entity
- C. To specify the schema storage location
- D. To define the security policies for accessing schemas

<details>
<summary>Response:</summary> 

**Explanation:**
In the Confluent Schema Registry, a subject is used to manage versions of a schema for a specific topic or entity. It groups schemas together under a common name, and each schema can have multiple versions within that subject.

- Options A, C, and D are incorrect because subjects are specifically for managing schema versions rather than grouping by type, specifying storage locations, or defining security policies.

**Answer:** B

</details>

## Question 13

How does Confluent Schema Registry ensure compatibility when registering a new schema version?

- A. By comparing the new schema with the latest version only
- B. By comparing the new schema with all previous versions
- C. By comparing the new schema with a user-specified set of previous versions
- D. By ignoring previous versions and only validating the new schema

<details>
<summary>Response:</summary> 

**Explanation:**
By default (BACKWARD, FORWARD, FULL) Confluent Schema Registry compares the new schema with the latest registered version only. The compatibility check depends on the compatibility mode set for the subject.

- The `*_TRANSITIVE` modes (BACKWARD_TRANSITIVE, FORWARD_TRANSITIVE, FULL_TRANSITIVE) compare against all previous versions; this is the exception to the rule above.
- Options C and D are incorrect because there is no user-specified set of versions, and the new schema is never accepted without being validated (unless the mode is NONE).

**Answer:** A

</details>

## Question 14

What compatibility mode allows a new schema to both read data written by an old schema and write data that can be read by the old schema?

- A. BACKWARD
- B. FORWARD
- C. FULL
- D. NONE

<details>
<summary>Response:</summary> 

**Explanation:**
The FULL compatibility mode allows a new schema to both read data written by an old schema (backward compatibility) and write data that can be read by the old schema (forward compatibility).

- Options A and B are incorrect because BACKWARD only ensures backward compatibility and FORWARD only ensures forward compatibility. Option D (NONE) disables compatibility checks.

**Answer:** C

</details>

## Question 15

Which schema types are supported by Confluent Schema Registry but not by Apache Avro? (Select all that apply)

- A. Protobuf
- B. Thrift
- C. JSON Schema
- D. XML Schema

<details>
<summary>Response:</summary> 

**Explanation:**
Confluent Schema Registry supports Protobuf and JSON Schema in addition to Avro. The Apache Avro library itself only handles Avro schemas, so Protobuf and JSON Schema are schema types supported by the Schema Registry but not by Avro.

- Options B and D are incorrect as Thrift and XML Schema are not supported by the Schema Registry.

**Answer:** A, C

</details>

## Question 16

In the context of Confluent Schema Registry, what is the main advantage of using Avro over JSON Schema?

- A. Avro schemas are human-readable
- B. Avro provides a compact and fast binary serialization format
- C. Avro does not require schema registration
- D. Avro supports all JSON types natively

<details>
<summary>Response:</summary> 

**Explanation:**
The main advantage of using Avro over JSON Schema is that Avro provides a compact and fast binary serialization format, which is efficient for data storage and transfer.

- Options A and C are incorrect because while Avro schemas can be human-readable, the main advantage is their compactness and speed. Avro always requires a schema, and with the Confluent serializers the schema is registered in Schema Registry (automatically by default, `auto.register.schemas=true`). Option D is incorrect as JSON Schema supports JSON types natively, not Avro.

**Answer:** B

</details>

## Question 17

What is the default compatibility mode in Confluent Schema Registry?

- A. BACKWARD
- B. FORWARD
- C. FULL
- D. NONE

<details>
<summary>Response:</summary> 

**Explanation:**
The default compatibility mode in Confluent Schema Registry is BACKWARD. This mode ensures that consumers using the new schema can read data produced with the previous (latest) version of the schema. Note it is BACKWARD, not BACKWARD_TRANSITIVE.

- Options B, C, and D are incorrect because FORWARD and FULL are not the default modes, and NONE disables compatibility checks.

**Answer:** A

</details>

## Question 18

How does the Confluent Schema Registry handle schema evolution?

- A. By automatically converting old schemas to new schemas
- B. By storing all schema versions and applying compatibility checks
- C. By enforcing schema changes directly on the producer side
- D. By modifying the schema directly in the consumer application

<details>
<summary>Response:</summary> 

**Explanation:**
The Confluent Schema Registry handles schema evolution by storing all schema versions and applying compatibility checks to ensure that new schema versions are compatible with previous versions according to the configured compatibility mode.

- Options A, C, and D are incorrect because the registry does not automatically convert schemas or enforce changes directly on the producer or consumer sides.

**Answer:** B

</details>

## Question 19

What happens if a schema fails the compatibility check when being registered in the Confluent Schema Registry?

- A. The schema is registered with a warning
- B. The schema is rejected, and an error is returned
- C. The schema is registered, but compatibility is disabled
- D. The schema is registered with a lower priority

<details>
<summary>Response:</summary> 

**Explanation:**
If a schema fails the compatibility check when being registered in the Confluent Schema Registry, the schema is rejected, and an error is returned. The schema cannot be registered until it passes the compatibility check.

- Options A, C, and D are incorrect because the registry does not register schemas that fail compatibility checks under any conditions.

**Answer:** B

</details>

## Question 20

Which interface is the standard way to manage schemas, subjects, and compatibility settings in the Confluent Schema Registry?

- A. JMX
- B. The REST API (e.g. using `curl`)
- C. `kafka-topics.sh`
- D. The Zookeeper shell

<details>
<summary>Response:</summary> 

**Explanation:**
Confluent Schema Registry exposes a RESTful API (default port 8081) that is used to register schemas, retrieve schemas by ID or subject/version, test compatibility, and change compatibility settings. It can be called with any HTTP client such as `curl`, or through the Confluent CLI/Control Center, which wrap the same API.

- A: JMX exposes metrics only.
- C: `kafka-topics.sh` manages Kafka topics, not schemas.
- D: Schema Registry does not use Zookeeper for schema management.

**Answer:** B

</details>

## Question 21

What is the purpose of the Confluent Schema Registry in a Kafka ecosystem?

- A. To store and manage Avro schemas for Kafka messages
- B. To provide a REST API for producing and consuming Kafka messages
- C. To handle authentication and authorization for Kafka clients
- D. To monitor and manage Kafka clusters and their performance

<details>
<summary>Response:</summary> 

**Explanation:**
The primary purpose of the Confluent Schema Registry in a Kafka ecosystem is to store and manage schemas (Avro, Protobuf, JSON Schema) for Kafka messages. The Schema Registry provides a centralized repository for storing and retrieving schemas, enabling schema evolution and compatibility checks. It allows Kafka producers and consumers to work with structured data in Avro format, ensuring that the data adheres to a well-defined schema. By storing schemas in the Schema Registry, producers and consumers can refer to schemas by their unique identifier, eliminating the need to include the full schema with each message. This promotes schema reuse, reduces message size, and enables schema evolution over time.

**Answer:** A

</details>

## Question 22

How does the Confluent Schema Registry ensure compatibility between different versions of a schema?

- A. By enforcing strict backward compatibility for all schema changes
- B. By allowing schema changes that are both backward and forward compatible
- C. By automatically generating compatibility reports for schema versions
- D. By using a compatibility setting to define allowed schema evolution rules

<details>
<summary>Response:</summary> 

**Explanation:**
The Confluent Schema Registry uses a compatibility setting to define allowed schema evolution rules and ensure compatibility between different versions of a schema. The compatibility setting determines how schema changes are validated and whether they are allowed or rejected. The available compatibility settings are:

- BACKWARD: A new schema is backward compatible with the latest version.
- FORWARD: A new schema is forward compatible with the latest version.
- FULL: A new schema is both backward and forward compatible with the latest version.
- NONE: No compatibility checks are performed.

By configuring the appropriate compatibility setting, you can control the schema evolution process and ensure that new schema versions are compatible with existing data and applications. The Schema Registry validates schema changes against the configured compatibility rules and rejects changes that violate the rules. This helps maintain data integrity and prevents incompatible schema changes from being registered.

**Answer:** D

</details>

## Question 23

How can you retrieve the latest version of a schema from the Confluent Schema Registry using its REST API?

- A. Send a GET request to `/subjects/<subject>/versions/latest`
- B. Send a POST request to `/schemas/<subject>/versions/latest`
- C. Send a GET request to `/schemas/<subject>/versions/latest`
- D. Send a POST request to `/subjects/<subject>/versions/latest`

<details>
<summary>Response:</summary> 

**Explanation:**
To retrieve the latest version of a schema from the Confluent Schema Registry using its REST API, you need to send a GET request to the endpoint `/subjects/<subject>/versions/latest`. The `<subject>` placeholder represents the name of the schema subject for which you want to retrieve the latest version. The Schema Registry organizes schemas into subjects, typically corresponding to Kafka topic names. By making a GET request to this endpoint, the Schema Registry will respond with the latest version of the schema associated with the specified subject. The response will include the schema details, such as the schema ID, version number, and the schema definition itself.

**Answer:** A

</details>

## Question 24

🚫 What is the purpose of the `kafkastore.topic` configuration in the Confluent Schema Registry?

- A. To specify the Kafka topic where the Schema Registry stores its schema data
- B. To define the compatibility setting for schema evolution
- C. To set the frequency at which the Schema Registry checks for schema updates
- D. To configure the retention period for old schema versions

<details>
<summary>Response:</summary> 

**Explanation:**
The `kafkastore.topic` configuration in the Confluent Schema Registry is used to specify the Kafka topic where the Schema Registry stores its schema data. The Schema Registry uses Kafka as its underlying storage mechanism to persist and distribute schema information across multiple instances. By default, the Schema Registry uses a Kafka topic named `_schemas` to store the schema data. However, you can customize the topic name by setting the `kafkastore.topic` configuration property. Schema Registry instances that form one cluster must share the same topic; a different topic name is needed only when several independent Schema Registry clusters use the same Kafka cluster.

**Answer:** A

</details>

## Question 25

What is the default compatibility setting in the Confluent Schema Registry for schema evolution?

- A. BACKWARD
- B. FORWARD
- C. FULL
- D. NONE

<details>
<summary>Response:</summary> 

**Explanation:**
The default compatibility setting in the Confluent Schema Registry for schema evolution is BACKWARD. When a new version of a schema is registered, the Schema Registry checks its compatibility with the existing schema versions based on the configured compatibility setting. The BACKWARD compatibility setting ensures that a new schema can be used to read data written by the previous schema version. In other words, consumers using the new schema can still read data produced with the old schema. This is the most commonly used compatibility setting as it allows for schema evolution while maintaining backward compatibility. If you require different compatibility rules, you can change the setting to FORWARD, FULL, or NONE based on your specific requirements.

**Answer:** A

</details>

## Question 26

How can you change the compatibility setting for a specific subject in the Confluent Schema Registry using its REST API?

- A. Send a PUT request to `/config/<subject>`
- B. Send a POST request to `/config/<subject>`
- C. Send a PUT request to `/compatibility/<subject>`
- D. Send a POST request to `/compatibility/<subject>`

<details>
<summary>Response:</summary> 

**Explanation:**
To change the compatibility setting for a specific subject in the Confluent Schema Registry using its REST API, you need to send a PUT request to the endpoint `/config/<subject>`. The `<subject>` placeholder represents the name of the schema subject for which you want to modify the compatibility setting. In the request body, you need to provide the new compatibility setting as a JSON object. For example:

```json
{
  "compatibility": "FULL"
}
```

- B: `/config/<subject>` accepts PUT for updates; C and D: there is no `/compatibility/<subject>` endpoint for changing settings (`/compatibility/subjects/...` only tests schema compatibility via POST).

**Answer:** A

</details>

## Question 27

What is the impact of removing a required field that has a default value in an Avro schema?

- A. It is a backward compatible change
- B. It is a forward compatible change
- C. It is both a backward and forward compatible change
- D. It is an incompatible change

<details>
<summary>Response:</summary> 

**Explanation:**
Removing a field that has a default value in an Avro schema is both a backward and a forward compatible change, i.e. FULL compatible.

- It is backward compatible because the new schema simply does not contain the field; when reading old data, the reader skips the field that the writer wrote.
- It is forward compatible because the old schema still expects the field, but when reading data written with the new schema (which lacks it) the old reader fills in the field's default value.

If the removed field had no default, the change would only be backward compatible (old readers could not read new data).

**Answer:** C

</details>

## Question 28

What compatibility level is maintained when adding a new optional field to an Avro schema?

- A. Backward compatibility
- B. Forward compatibility
- C. Full compatibility
- D. No compatibility

<details>
<summary>Response:</summary> 

**Explanation:**
Adding a new optional field to an Avro schema maintains both backward and forward compatibility, which is known as full compatibility.

When a new optional field is added to the schema, it means that the field is not required and has a default value. This change is backward compatible because data written with the old schema can still be read by applications using the new schema. The new schema will treat the missing field as having its default value.

Additionally, adding an optional field is forward compatible because data written with the new schema can be read by applications using the old schema. The old schema will simply ignore the additional field that it doesn't recognize.

Since both backward and forward compatibility are maintained, adding a new optional field to an Avro schema provides full compatibility. It allows both old and new applications to read data written with either schema version.

**Answer:** C

</details>

## Question 29 [x]

What is the effect of changing the data type of a field in an Avro schema?

- A. It is a backward compatible change
- B. It is a forward compatible change
- C. It is both a backward and forward compatible change
- D. It is an incompatible change

<details>
<summary>Response:</summary> 

**Explanation:**
Changing the data type of a field in an Avro schema is, in general, an incompatible change. It breaks both backward and forward compatibility. (Exception: Avro type promotion, e.g. int to long, float or double, is allowed when reading, so such a widening is backward compatible only.)

When the data type of a field is changed, it means that the serialized representation of the data for that field is different between the old and new schemas. Applications using the old schema will not be able to deserialize data written with the new schema correctly because the data type of the field has changed. Similarly, applications using the new schema will not be able to deserialize data written with the old schema correctly.

For example, if a field's data type is changed from an integer to a string, the serialized data will be different, and the applications expecting an integer will fail to deserialize the string value correctly.

Therefore, changing the data type of a field in an Avro schema is an incompatible change that breaks both backward and forward compatibility. It requires careful consideration and coordination between producers and consumers to handle the schema evolution properly.

**Answer:** D

</details>

## Question 30

In the Confluent Schema Registry, what is the default compatibility setting for new schemas?

- A. BACKWARD
- B. FORWARD
- C. FULL
- D. NONE



<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The Confluent Schema Registry default compatibility type is BACKWARD (checked against the latest version only; BACKWARD_TRANSITIVE checks all versions). The main reason that BACKWARD compatibility mode is the default, and preferred for Kafka, is so that you can rewind consumers to the beginning of the topic.

- BACKWARD compatibility means that code using the new schema can read data written with the old schema.
- FORWARD compatibility means that code using the old schema can read data written with the new schema.
- FULL compatibility means that both BACKWARD and FORWARD compatibilities are required.
- NONE means that no compatibility checking is performed.

</details>

## Question 31

🚫 Where does the Confluent Schema Registry read its own server configuration from?

- A. From Zookeeper
- B. From a Kafka topic
- C. From a properties file on the filesystem
- D. From a database

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
The Schema Registry server is configured with a properties file (e.g. `schema-registry.properties`) passed at startup, containing settings such as `listeners`, `kafkastore.bootstrap.servers`, and `kafkastore.topic`. Schema Registry does not use Zookeeper any more (older versions used it only for leader election).

The schemas themselves, and the subject/global compatibility settings that you change through the REST API, are stored in the Kafka topic `_schemas` (not in the server configuration file).

- A is incorrect because Zookeeper is not used for configuration (and Kafka 4.x has no Zookeeper).
- B is incorrect because the topic holds schemas and compatibility config set via the API, not the server's own configuration.
- D is incorrect because Schema Registry does not use a database.

</details>

## Question 32

🚫 How does the Confluent Schema Registry ensure high availability?

- A. By running multiple instances with one elected primary (leader)
- B. By relying on the availability of the underlying Kafka cluster
- C. By replicating data across multiple Zookeeper instances
- D. By using a distributed consensus protocol among instances

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The Confluent Schema Registry achieves high availability by running multiple instances in a cluster with a primary/follower architecture (formerly called master/slave):

- One instance is elected the primary (leader) at any given time. Only the primary writes to the `_schemas` topic, so all registrations and config changes go through it.
- All instances can serve read requests. Follower instances forward write requests to the primary.
- Every instance consumes the `_schemas` topic to keep its own cache up to date.
- If the primary goes down, a new one is automatically elected from the remaining eligible instances (`leader.eligibility=true`; formerly `master.eligibility`). Election uses the Kafka group protocol (`kafkastore.bootstrap.servers`); older versions could use Zookeeper.

- B is incorrect because while durability of the data depends on Kafka, availability of the service comes from running multiple instances.
- C is incorrect because current Schema Registry does not use Zookeeper for storing data.
- D is incorrect because Schema Registry does not run a consensus protocol like Raft or Paxos among its instances; leader election is delegated to the Kafka group coordinator.

</details>
