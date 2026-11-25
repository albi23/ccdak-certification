## Question 1 (Kafka Consumers):
There are 3 producers writing to a topic with 5 partitions. There are 10 consumers consuming from the topic as part of the same group. How many consumers will remain idle?

- A. 3
- B. 5
- C. 10
- D. None

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

One consumer per partition assignment will keep 5 consumers idle.

**Detailed explanation of each option:**

1. ❌ **A. 3**  
   **Incorrect**.

2. ✅ **B. 5**  
   **Correct**.

3. ❌ **C. 10**  
   **Incorrect**.

4. ❌ **D. None**  
   **Incorrect**.

</details>

## Question 2 (Programming & Serialization):
Which of the following is true regarding thread safety in the Java Kafka Clients?

- A. One Consumer needs to run in one thread
- B. One Producer needs to be run in one thread
- C. One Producer can be safely used in multiple threads
- D. One Consumer can be safely used in multiple threads

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. One Consumer needs to run in one thread**  
   **Correct**.

2. ❌ **B. One Producer needs to be run in one thread**  
   **Incorrect**.

3. ✅ **C. One Producer can be safely used in multiple threads**  
   **Correct**.

4. ❌ **D. One Consumer can be safely used in multiple threads**  
   **Incorrect**.

</details>

## Question 3 (Kafka Internals):
Partition leader election is done by

- A. Zookeeper
- B. The consumers
- C. Vote amongst the brokers
- D. The Kafka Broker that is the Controller

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The Controller is a broker that is responsible for electing partition leaders

**Detailed explanation of each option:**

1. ❌ **A. Zookeeper**  
   **Incorrect**.

2. ❌ **B. The consumers**  
   **Incorrect**.

3. ❌ **C. Vote amongst the brokers**  
   **Incorrect**.

4. ✅ **D. The Kafka Broker that is the Controller**  
   **Correct**.

</details>

## Question 4 (Kafka Consumers):
To read data from a topic, the following configuration is needed for the consumers

- A. any broker to connect to, and the topic name
- B. the list of brokers that have the data, the topic name and the partitions list
- C. any broker, and the list of topic partitions
- D. all brokers of the cluster, and the topic name

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. any broker to connect to, and the topic name**  
   **Correct**.

2. ❌ **B. the list of brokers that have the data, the topic name and the partitions list**  
   **Incorrect**.

3. ❌ **C. any broker, and the list of topic partitions**  
   **Incorrect**.

4. ❌ **D. all brokers of the cluster, and the topic name**  
   **Incorrect**.

</details>

## Question 5 (Kafka Producers):
To prevent network-induced duplicates when producing to Kafka, I should use

- A. retries=200000
- B. max.in.flight.requests.per.connection=1
- C. enable.idempotence=true
- D. batch.size=1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Producer idempotence helps prevent the network introduced duplicates. More details here: https://cwiki.apache.org/confluence/display/KAFKA/Idempotent+Producer

**Detailed explanation of each option:**

1. ❌ **A. retries=200000**  
   **Incorrect**.

2. ❌ **B. max.in.flight.requests.per.connection=1**  
   **Incorrect**.

3. ✅ **C. enable.idempotence=true**  
   **Correct**.

4. ❌ **D. batch.size=1**  
   **Incorrect**.

</details>

## Question 6 (Programming & Serialization):
Which of the following is not an Avro primitive type?

- A. int
- B. date
- C. null
- D. string
- E. long

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

date is a logical type

**Detailed explanation of each option:**

1. ❌ **A. int**  
   **Incorrect**.

2. ✅ **B. date**  
   **Correct**.

3. ❌ **C. null**  
   **Incorrect**.

4. ❌ **D. string**  
   **Incorrect**.

5. ❌ **E. long**  
   **Incorrect**.

</details>

## Question 7 (Kafka Setup and Operations):
What happens if you try to produce to a topic that does not yet exist? 

- A. There will be a runtime error.
- B. It depends on the broker setting “auto.create.topic.enable“.
- C. The topic gets created with the default server settings without any errors or warnings.
- D. A warning appears but the topic still gets created with the default server settings.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

If the broker setting auto.create.topic.enable is set to true, then Kafka will automatically create the topic with the default broker settings num.partitions and default.replication.factor. The option defaults to true. Hence it depends on the broker setting auto.create.topic.enable.

**Detailed explanation of each option:**

1. ❌ **A. There will be a runtime error.**  
   **Incorrect**.

2. ✅ **B. It depends on the broker setting “auto.create.topic.enable“.**  
   **Correct**.

3. ❌ **C. The topic gets created with the default server settings without any errors or warnings.**  
   **Incorrect**.

4. ❌ **D. A warning appears but the topic still gets created with the default server settings.**  
   **Incorrect**.

</details>

## Question 8 (Kafka Producers):
A producer is sending messages with null key to a topic with 6 partitions using the DefaultPartitioner. Where will the messages be stored?

- A. Partition 0
- B. The partition for the null key
- C. Partition 5
- D. Any of the topic partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Message with no keys will be stored with round-robin strategy among partitions.

**Detailed explanation of each option:**

1. ❌ **A. Partition 0**  
   **Incorrect**.

2. ❌ **B. The partition for the null key**  
   **Incorrect**.

3. ❌ **C. Partition 5**  
   **Incorrect**.

4. ✅ **D. Any of the topic partitions**  
   **Correct**.

</details>

## Question 9 (Kafka Consumers):
A consumer is configured with enable.auto.commit=false. What happens when close() is called on the consumer object?

- A. A rebalance in the consumer group will happen immediately
- B. The group coordinator will discover that the consumer stopped sending heartbeats. It will cause rebalance after session.timeout.ms
- C. The uncommitted offsets are committed

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Calling close() on consumer immediately triggers a partition rebalance as the consumer will not be available anymore.

**Detailed explanation of each option:**

1. ✅ **A. A rebalance in the consumer group will happen immediately**  
   **Correct**.

2. ❌ **B. The group coordinator will discover that the consumer stopped sending heartbeats. It will cause rebalance after session.timeout.ms**  
   **Incorrect**.

3. ❌ **C. The uncommitted offsets are committed**  
   **Incorrect**.

</details>

## Question 10 (Kafka Consumers):
The kafka-console-consumer CLI, when used with the default options…

- A. always uses the same group id
- B. does not use a group id
- C. uses a random group id

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. always uses the same group id**  
   **Incorrect**.

2. ❌ **B. does not use a group id**  
   **Incorrect**.

3. ✅ **C. uses a random group id**  
   **Correct**.

</details>

## Question 11 (Kafka Consumers):
Consumer failed to process record # 10 and succeeded in processing record # 11. Select the course of action that you should choose to guarantee at least once processing

- A. Commit offsets at 10
- B. Commit offsets at 11
- C. Do not commit until successfully processing the record #10

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Here, you shouldn‘t commit offsets 11 or 10 as it would indicate that the message #10 has been processed successfully.

**Detailed explanation of each option:**

1. ❌ **A. Commit offsets at 10**  
   **Incorrect**.

2. ❌ **B. Commit offsets at 11**  
   **Incorrect**.

3. ✅ **C. Do not commit until successfully processing the record #10**  
   **Correct**.

</details>

## Question 12 (Kafka Consumers):
How to see if a consumer group is committing offsets at all, or how often offsets are being committed? 

- A. Use the consumer group to consume from the internal partition called __consumer_offsets.
- B. Consumer offsets are automatically stored and visualized in the Confluent Control Center.
- C. Use the console consumer to consume the internal topic called __consumer_offsets.
- D. Read the consumer log located under /bin/log/consumer-log.txt

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

It is sometimes useful to see what offsets are being committed for the cluster‘s consumer groups. You may want to see if a particular group is committing offsets at all, or how often offsets are being committed. This can be done by using the console consumer to consume the special internal topic called __consumer_offsets. All consumer offsets are written as messages to this topic. In order to decode the messages in this topic, you must use the formatter class kafka.coordinator.GroupMeta dataManager$OffsetsMessageFormatter.

**Detailed explanation of each option:**

1. ❌ **A. Use the consumer group to consume from the internal partition called __consumer_offsets.**  
   **Incorrect**.

2. ❌ **B. Consumer offsets are automatically stored and visualized in the Confluent Control Center.**  
   **Incorrect**.

3. ✅ **C. Use the console consumer to consume the internal topic called __consumer_offsets.**  
   **Correct**.

4. ❌ **D. Read the consumer log located under /bin/log/consumer-log.txt**  
   **Incorrect**.

</details>

## Question 13 (Kafka Consumers):
You have a consumer group of 12 consumers and when a consumer gets killed by the process management system, rather abruptly, it does not trigger a graceful shutdown of your consumer. Therefore, it takes up to 10 seconds for a rebalance to happen. The business would like to have a 3 seconds rebalance time. What should you do? 

- A. decrease max.poll.interval.ms
- B. Increase session.timeout.ms
- C. Decrease heartbeat.interval.ms
- D. Increase heartbeat.interval.ms
- E. Decrease session.timeout.ms
- F. increase max.poll.interval.ms

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** C, E

**Explanation:**

session.timeout.ms must be decreased to 3 seconds to allow for a faster rebalance, and the heartbeat thread must be quicker, so we also need to decrease heartbeat.interval.ms

**Detailed explanation of each option:**

1. ❌ **A. decrease max.poll.interval.ms**  
   **Incorrect**.

2. ❌ **B. Increase session.timeout.ms**  
   **Incorrect**.

3. ✅ **C. Decrease heartbeat.interval.ms**  
   **Correct**.

4. ❌ **D. Increase heartbeat.interval.ms**  
   **Incorrect**.

5. ✅ **E. Decrease session.timeout.ms**  
   **Correct**.

6. ❌ **F. increase max.poll.interval.ms**  
   **Incorrect**.

</details>

## Question 14 (Stream Processing):
Which of these joins does not require input topics to be sharing the same number of partitions?

- A. KTable-KTable join
- B. KStream-KStream join
- C. KStream-KTable join
- D. KStream-GlobalKTable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

GlobalKTables have their datasets replicated on each Kafka Streams instance and therefore no repartitioning is required

**Detailed explanation of each option:**

1. ❌ **A. KTable-KTable join**  
   **Incorrect**.

2. ❌ **B. KStream-KStream join**  
   **Incorrect**.

3. ❌ **C. KStream-KTable join**  
   **Incorrect**.

4. ✅ **D. KStream-GlobalKTable**  
   **Correct**.

</details>

## Question 15 (Programming & Serialization):
Which of the following message schema formats are supported out-of-the box with Confluent Platform, with serializers, deserializers, and command line tools available for each format? 

- A. Avro
- B. ProtoBuf
- C. JSON
- D. Bytes

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

The following schema formats are supported out-of-the box with Confluent Platform, with serializers, deserializers, and command line tools available for each format: – Avro: Relies on schemas. When Avro data is read, the schema used when writing it is always present. – JSON: It is a lightweight data-interchange format. It‘s easy for humans to read and write and It‘s easy for machines to parse and generate. JSON does not rely on schemas. – ProtoBuf: ProtoBuf or Protocol buffers are Google‘s language-neutral, platform-neutral, extensible mechanism for serializing structured data  think XML, but smaller, faster, and simpler. Further reading: Confluent Platform Schemas.

**Detailed explanation of each option:**

1. ✅ **A. Avro**  
   **Correct**.

2. ✅ **B. ProtoBuf**  
   **Correct**.

3. ✅ **C. JSON**  
   **Correct**.

4. ❌ **D. Bytes**  
   **Incorrect**.

</details>

## Question 16 (Programming & Serialization):
In Java, Avro SpecificRecords classes are

- A. automatically generated from an Avro Schema
- B. written manually by the programmer
- C. automatically generated from an Avro Schema + a Maven / Gradle Plugin

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

SpecificRecord is created from generated record classes

**Detailed explanation of each option:**

1. ❌ **A. automatically generated from an Avro Schema**  
   **Incorrect**.

2. ❌ **B. written manually by the programmer**  
   **Incorrect**.

3. ✅ **C. automatically generated from an Avro Schema + a Maven / Gradle Plugin**  
   **Correct**.

</details>

## Question 17 (Kafka Internals):
By default, which replica will be elected as a partition leader? 

- A. Any of the replicas
- B. An in-sync replica
- C. Preferred leader broker if it is in-sync and auto.leader.rebalance.enable=false
- D. Preferred leader broker if it is in-sync and auto.leader.rebalance.enable=true

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Any of the replicas**  
   **Incorrect**.

2. ✅ **B. An in-sync replica**  
   **Correct**.

3. ❌ **C. Preferred leader broker if it is in-sync and auto.leader.rebalance.enable=false**  
   **Incorrect**.

4. ✅ **D. Preferred leader broker if it is in-sync and auto.leader.rebalance.enable=true**  
   **Correct**.

</details>

## Question 18 (Kafka Producers):
You are receiving orders from different customer in an “orders“ topic with multiple partitions. Each message has the customer name as the key. There is a special customer named ABC that generates a lot of orders and you would like to reserve a partition exclusively for ABC. The rest of the message should be distributed among other partitions. How can this be achieved?

- A. Define a Kafka Broker routing rule
- B. Add metadata to the producer record
- C. All messages with the same key will go the same partition, but the same partition may have messages with different keys. It is not possible to reserve
- D. Create a custom partitioner

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

A Custom Partitioner allows you to easily customise how the partition number gets computed from a source message.

**Detailed explanation of each option:**

1. ❌ **A. Define a Kafka Broker routing rule**  
   **Incorrect**.

2. ❌ **B. Add metadata to the producer record**  
   **Incorrect**.

3. ❌ **C. All messages with the same key will go the same partition, but the same partition may have messages with different keys. It is not possible to reserve**  
   **Incorrect**.

4. ✅ **D. Create a custom partitioner**  
   **Correct**.

</details>

## Question 19 (Kafka Core Concepts):
In Kafka, every broker… 

- A. contains all the topics and all the partitions
- B. knows all the metadata for all topics and partitions
- C. is a controller
- D. is a bootstrap broker
- E. knows the metadata for the topics and partitions it has on its disk
- F. contains only a subset of the topics and the partitions

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, D, F

**Explanation:**

Kafka topics are divided into partitions and spread across brokers. Each brokers knows about all the metadata and each broker is a bootstrap broker, but only one of them is elected controller

**Detailed explanation of each option:**

1. ❌ **A. contains all the topics and all the partitions**  
   **Incorrect**.

2. ✅ **B. knows all the metadata for all topics and partitions**  
   **Correct**.

3. ❌ **C. is a controller**  
   **Incorrect**.

4. ✅ **D. is a bootstrap broker**  
   **Correct**.

5. ❌ **E. knows the metadata for the topics and partitions it has on its disk**  
   **Incorrect**.

6. ✅ **F. contains only a subset of the topics and the partitions**  
   **Correct**.

</details>

## Question 20 (Kafka Core Concepts):
You are sending messages with keys to a topic. To increase throughput, you decide to increase the number of partitions of the topic. Select all that apply.

- A. All the existing records will get rebalanced among the partitions to balance load
- B. New records with the same key will get written to the partition where old records with that key were written
- C. Old records will stay in their partitions
- D. New records may get written to a different partition

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

Increasing the number of partition causes new messages keys to get hashed differently, and breaks the guarantee “same keys goes to the same partition“. Kafka logs are immutable and the previous messages are not re-shuffled

**Detailed explanation of each option:**

1. ❌ **A. All the existing records will get rebalanced among the partitions to balance load**  
   **Incorrect**.

2. ❌ **B. New records with the same key will get written to the partition where old records with that key were written**  
   **Incorrect**.

3. ✅ **C. Old records will stay in their partitions**  
   **Correct**.

4. ✅ **D. New records may get written to a different partition**  
   **Correct**.

</details>

## Question 21 (Kafka Core Concepts):
What is the disadvantage of request/response communication?

- A. Reliability
- B. Cost
- C. Coupling
- D. Scalability

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Point-to-point (request-response) style will couple client to the server.

**Detailed explanation of each option:**

1. ❌ **A. Reliability**  
   **Incorrect**.

2. ❌ **B. Cost**  
   **Incorrect**.

3. ✅ **C. Coupling**  
   **Correct**.

4. ❌ **D. Scalability**  
   **Incorrect**.

</details>

## Question 22 (Kafka Core Concepts):
The rule “same key goes to the same partition“ is true unless…

- A. the number of kafka broker changes
- B. the replication factor changes
- C. the number of producer changes
- D. the number of partition changes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Increasing the number of partition causes new messages keys to get hashed differently, and breaks the guarantee “same keys goes to the same partition“. Kafka logs are immutable and the previous messages are not re-shuffled.

**Detailed explanation of each option:**

1. ❌ **A. the number of kafka broker changes**  
   **Incorrect**.

2. ❌ **B. the replication factor changes**  
   **Incorrect**.

3. ❌ **C. the number of producer changes**  
   **Incorrect**.

4. ✅ **D. the number of partition changes**  
   **Correct**.

</details>

## Question 23 (Stream Processing):
In Kafka Streams, by what value are internal topics prefixed by?

- A. application.id
- B. kafka-streams-
- C. group.id
- D. tasks-

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In Kafka Streams, the application.id is also the underlying group.id for your consumers, and the prefix for all internal topics (repartition and state)

**Detailed explanation of each option:**

1. ✅ **A. application.id**  
   **Correct**.

2. ❌ **B. kafka-streams-**  
   **Incorrect**.

3. ❌ **C. group.id**  
   **Incorrect**.

4. ❌ **D. tasks-**  
   **Incorrect**.

</details>

## Question 24 (Kafka Setup and Operations):
When auto.create.topics.enable is set to true in Kafka configuration, what are the circumstances under which a Kafka broker automatically creates a topic? 

- A. Client alters number of partitions of a topic
- B. Producer sends message to a topic
- C. Client requests metadata for a topic
- D. Consumer reads message from a topic

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** B, C, D

**Explanation:**

A kafka broker automatically creates a topic under the following circumstances: – When a producer starts writing messages to the topic – When a consumer starts reading messages from the topic – When any client requests metadata for the topic

**Detailed explanation of each option:**

1. ❌ **A. Client alters number of partitions of a topic**  
   **Incorrect**.

2. ✅ **B. Producer sends message to a topic**  
   **Correct**.

3. ✅ **C. Client requests metadata for a topic**  
   **Correct**.

4. ✅ **D. Consumer reads message from a topic**  
   **Correct**.

</details>

## Question 25 (Kafka Setup and Operations):
What is not a valid authentication mechanism in Kafka?

- A. SASL/SCRAM
- B. SSL
- C. SAML
- D. SASL/GSSAPI

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Learn more about security here: https://kafka.apache.org/documentation/#security

**Detailed explanation of each option:**

1. ❌ **A. SASL/SCRAM**  
   **Incorrect**.

2. ❌ **B. SSL**  
   **Incorrect**.

3. ✅ **C. SAML**  
   **Correct**.

4. ❌ **D. SASL/GSSAPI**  
   **Incorrect**.

</details>

## Question 26 (Kafka Internals):
Kafka is configured with following parameters – log.retention.hours = 168 log.retention.minutes = 168 log.retention.ms = 168 How long will the messages be retained for?

- A. Broker will not start due to bad configuration
- B. 168 minutes
- C. 168 hours
- D. 168 ms

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

If more than one similar config is specified, the smaller unit size will take precedence.

**Detailed explanation of each option:**

1. ❌ **A. Broker will not start due to bad configuration**  
   **Incorrect**.

2. ❌ **B. 168 minutes**  
   **Incorrect**.

3. ❌ **C. 168 hours**  
   **Incorrect**.

4. ✅ **D. 168 ms**  
   **Correct**.

</details>

## Question 27 (Kafka Connect):
When using plain JSON data with Connect, you see the following error message: org.apache.kafka.connect.errors.DataException: JsonDeserializer with schemas.enable requires “schema“ and “payload“ fields and may not contain additional fields. How will you fix the error?

- A. Set key.converter, value.converter to AvroConverter and the schema registry url
- B. Set key.converter, value.converter to JsonConverter and the schema registry url
- C. Set key.converter.schemas.enable and value.converter.schemas.enable to false
- D. Use Single Message Transforms to add schema and payload fields in the message

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

You will need to set the schemas.enable parameters for the converter to false for plain text with no schema.

**Detailed explanation of each option:**

1. ❌ **A. Set key.converter, value.converter to AvroConverter and the schema registry url**  
   **Incorrect**.

2. ❌ **B. Set key.converter, value.converter to JsonConverter and the schema registry url**  
   **Incorrect**.

3. ✅ **C. Set key.converter.schemas.enable and value.converter.schemas.enable to false**  
   **Correct**.

4. ❌ **D. Use Single Message Transforms to add schema and payload fields in the message**  
   **Incorrect**.

</details>

## Question 28 (Programming & Serialization):
Which of the following options are Avro primitive types? 

- A. null
- B. timestamp
- C. bytes
- D. string

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, C, D

**Explanation:**

In Avro, primitive types have no specified attributes. The set of primitive type names is: – null: no value – boolean: a binary value – int: 32-bit signed integer – long: 64-bit signed integer – float: single precision (32-bit) IEEE 754 floating-point number – double: double precision (64-bit) IEEE 754 floating-point number – bytes: sequence of 8-bit unsigned bytes – string: unicode character sequence Further reading: Avro Primitive Types.

**Detailed explanation of each option:**

1. ✅ **A. null**  
   **Correct**.

2. ❌ **B. timestamp**  
   **Incorrect**.

3. ✅ **C. bytes**  
   **Correct**.

4. ✅ **D. string**  
   **Correct**.

</details>

## Question 29 (Kafka Consumers):
How can you gracefully make a Kafka consumer to stop immediately polling data from Kafka and gracefully shut down a consumer application?

- A. Call consumer.wakeUp() and catch a WakeUpException
- B. Call consumer.poll() in another thread
- C. Kill the consumer thread

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. Call consumer.wakeUp() and catch a WakeUpException**  
   **Correct**.

2. ❌ **B. Call consumer.poll() in another thread**  
   **Incorrect**.

3. ❌ **C. Kill the consumer thread**  
   **Incorrect**.

</details>

## Question 30 (Kafka Internals):
What is true about partitions? 

- A. Only out of sync replicas are replicas, the remaining partitions that are in sync are also leader
- B. A partition has one replica that is a leader, while the other replicas are followers
- C. You cannot have more partitions than the number of brokers in your cluster
- D. A broker can have a partition and its replica on its disk
- E. A broker can have different partitions numbers for the same topic on its disk

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** B, E

**Explanation:**

Only one of the replicas is elected as partition leader. And a broker can definitely hold many partitions from the same topic on its disk, try creating a topic with 12 partitions on one broker!

**Detailed explanation of each option:**

1. ❌ **A. Only out of sync replicas are replicas, the remaining partitions that are in sync are also leader**  
   **Incorrect**.

2. ✅ **B. A partition has one replica that is a leader, while the other replicas are followers**  
   **Correct**.

3. ❌ **C. You cannot have more partitions than the number of brokers in your cluster**  
   **Incorrect**.

4. ❌ **D. A broker can have a partition and its replica on its disk**  
   **Incorrect**.

5. ✅ **E. A broker can have different partitions numbers for the same topic on its disk**  
   **Correct**.

</details>

## Question 31 (Programming & Serialization):
If I want to send binary data through the REST proxy, it needs to be base64 encoded. Which component needs to encode the binary data into base 64?

- A. The REST Proxy
- B. The Producer
- C. Zookeeper
- D. The Kafka Broker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The REST Proxy requires to receive data over REST that is already base64 encoded, hence it is the responsibility of the producer

**Detailed explanation of each option:**

1. ❌ **A. The REST Proxy**  
   **Incorrect**.

2. ✅ **B. The Producer**  
   **Correct**.

3. ❌ **C. Zookeeper**  
   **Incorrect**.

4. ❌ **D. The Kafka Broker**  
   **Incorrect**.

</details>

## Question 32 (Kafka Producers):
To produce data to a topic, a producer must provide the Kafka client with…

- A. any broker from the cluster and the topic name
- B. all the brokers from the cluster and the topic name
- C. any broker from the cluster and the topic name and the partitions list
- D. the list of brokers that have the data, the topic name and the partitions list

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

All brokers can respond to a Metadata request, so a client can connect to any broker in the cluster and then figure out on its own which brokers to send data to.

**Detailed explanation of each option:**

1. ✅ **A. any broker from the cluster and the topic name**  
   **Correct**.

2. ❌ **B. all the brokers from the cluster and the topic name**  
   **Incorrect**.

3. ❌ **C. any broker from the cluster and the topic name and the partitions list**  
   **Incorrect**.

4. ❌ **D. the list of brokers that have the data, the topic name and the partitions list**  
   **Incorrect**.

</details>

## Question 33 (Kafka Internals):
What is true about replicas ?

- A. Follower replica handles all consume requests
- B. Leader replica handles all produce and consume requests
- C. Produce and consume requests are load-balanced between Leader and Follower replicas
- D. Produce requests can be done to the replicas that are followers

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Replicas are passive – they don‘t handle produce or consume request. Produce and consume requests get sent to the node hosting partition leader.

**Detailed explanation of each option:**

1. ❌ **A. Follower replica handles all consume requests**  
   **Incorrect**.

2. ✅ **B. Leader replica handles all produce and consume requests**  
   **Correct**.

3. ❌ **C. Produce and consume requests are load-balanced between Leader and Follower replicas**  
   **Incorrect**.

4. ❌ **D. Produce requests can be done to the replicas that are followers**  
   **Incorrect**.

</details>

## Question 34 (Kafka Setup and Operations):
A producer application in a developer machine was able to send messages to a Kafka topic. After copying the producer application into another developer‘s machine, the producer is able to connect to Kafka but unable to produce to the same Kafka topic because of an authorization issue. What is the likely issue?

- A. The Kafka ACL does not allow another machine IP
- B. The Kafka Broker needs to be rebooted
- C. Broker configuration needs to be changed to allow a different producer
- D. You cannot copy a producer application from one machine to another

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

ACLs take “Host“ as a parameter, which represents an IP. It can be * (all IP), or a specific IP. Here, it‘s a specific IP as moving a producer to a different machine breaks the producer, so the ACL needs to be updated

**Detailed explanation of each option:**

1. ✅ **A. The Kafka ACL does not allow another machine IP**  
   **Correct**.

2. ❌ **B. The Kafka Broker needs to be rebooted**  
   **Incorrect**.

3. ❌ **C. Broker configuration needs to be changed to allow a different producer**  
   **Incorrect**.

4. ❌ **D. You cannot copy a producer application from one machine to another**  
   **Incorrect**.

</details>

## Question 35 (Kafka Consumers):
A consumer sends a request to commit offset 2000. There is a temporary communication problem, so the broker never gets the request and therefore never responds. Meanwhile, the consumer processed another batch and successfully committed offset 3000. What should you do?

- A. Add a new consumer to the group
- B. Restart the consumer
- C. Use the kafka-consumer-group command to manually commit the offsets 2000 for the consumer group
- D. Nothing

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In this case, because the offset 3000 has been committed and all the messages between 0 and 3000 have all been processed, it is okay not to have committed offset 2000. The right answer is to do “nothing“, this behaviour is acceptable

**Detailed explanation of each option:**

1. ❌ **A. Add a new consumer to the group**  
   **Incorrect**.

2. ❌ **B. Restart the consumer**  
   **Incorrect**.

3. ❌ **C. Use the kafka-consumer-group command to manually commit the offsets 2000 for the consumer group**  
   **Incorrect**.

4. ✅ **D. Nothing**  
   **Correct**.

</details>

## Question 36 (Kafka Setup and Operations):
What‘s is true about Kafka brokers and clients from version 0.10.2 onwards?

- A. A newer client can talk to a newer broker, and an older client can talk to a newer broker
- B. Clients and brokers must have the exact same version to be able to communicate
- C. A newer client can‘t talk to a newer broker, but an older client can talk to a newer broker
- D. A newer client can talk to a newer broker, but an older client cannot talk to a newer broker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka‘s new bidirectional client compatibility introduced in 0.10.2 allows this. Read more here: https://www.confluent.io/blog/upgrading-apache-kafka-clients-just-got-easier/

**Detailed explanation of each option:**

1. ✅ **A. A newer client can talk to a newer broker, and an older client can talk to a newer broker**  
   **Correct**.

2. ❌ **B. Clients and brokers must have the exact same version to be able to communicate**  
   **Incorrect**.

3. ❌ **C. A newer client can‘t talk to a newer broker, but an older client can talk to a newer broker**  
   **Incorrect**.

4. ❌ **D. A newer client can talk to a newer broker, but an older client cannot talk to a newer broker**  
   **Incorrect**.

</details>

## 🚫 Question 37 (Kafka Setup and Operations):
Running Kafka in production, what‘s a proper value for setting the java heap size? 

- A. 6 GB
- B. 6 TB
- C. 6 MB
- D. 6 KB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka relies heavily on the filesystem for storing and caching messages. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel‘s page cache. In most cases, Kafka can run optimally with 6 GB of RAM for heap space. For especially heavy production loads, use machines with 32 GB or more. Extra RAM will be used to bolster OS page cache and improve client throughput. While Kafka can run with less RAM, its ability to handle load is hampered when less memory is available.

**Detailed explanation of each option:**

1. ✅ **A. 6 GB**  
   **Correct**.

2. ❌ **B. 6 TB**  
   **Incorrect**.

3. ❌ **C. 6 MB**  
   **Incorrect**.

4. ❌ **D. 6 KB**  
   **Incorrect**.

</details>

## Question 38 (Stream Processing):
To transform data from a Kafka topic to another one, I should use

- A. Kafka Connect Source
- B. Consumer + Producer
- C. Kafka Connect Sink
- D. Kafka Streams

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Kafka Streams is a library for building streaming applications, specifically applications that transform input Kafka topics into output Kafka topics

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect Source**  
   **Incorrect**.

2. ❌ **B. Consumer + Producer**  
   **Incorrect**.

3. ❌ **C. Kafka Connect Sink**  
   **Incorrect**.

4. ✅ **D. Kafka Streams**  
   **Correct**.

</details>

## Question 39 (Kafka Setup and Operations):
How will you set the retention for the topic named “my-topic” to 1 hour?

- A. Set the topic config retention.ms to 3600000
- B. Set the consumer config retention.ms to 3600000
- C. Set the broker config log.retention.ms to 3600000
- D. Set the producer config retention.ms to 3600000

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. Set the topic config retention.ms to 3600000**  
   **Correct**.

2. ❌ **B. Set the consumer config retention.ms to 3600000**  
   **Incorrect**.

3. ❌ **C. Set the broker config log.retention.ms to 3600000**  
   **Incorrect**.

4. ❌ **D. Set the producer config retention.ms to 3600000**  
   **Incorrect**.

</details>

## Question 40 (Kafka Consumers):
Two consumers share the same group.id (consumer group id). Each consumer will…

- A. Read mutually exclusive offsets blocks on all the partitions
- B. Read all data from all partitions
- C. Read all the data on mutual exclusive partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Read mutually exclusive offsets blocks on all the partitions**  
   **Incorrect**.

2. ❌ **B. Read all data from all partitions**  
   **Incorrect**.

3. ✅ **C. Read all the data on mutual exclusive partitions**  
   **Correct**.

</details>

## Question 41 (Kafka Setup and Operations):
When you enable SSL encryption within Kafka, which feature cannot be used then anymore? 

- A. Horizontally Scaling
- B. Data Compression
- C. Zero Copy Data Transfer
- D. Data Batching

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Most traditional data systems use random-access memory (RAM) for data storage, as RAM provides extremely low latencies. Kafka avoids Random Access Memory, it achieves low latency message delivery through Zero Copy Principle. A zero copy optimization consists on removing the second and third data copies, making the data being transferred directly from the read buffer to the socket buffer. Since SSL allows to encrypt data in flight, we no longer send over wire the same data that is stored on the Broker. This means that when SSL is enabled, zero copy optimization is lost, since the Broker needs to decrypt and encrypt the data.

**Detailed explanation of each option:**

1. ❌ **A. Horizontally Scaling**  
   **Incorrect**.

2. ❌ **B. Data Compression**  
   **Incorrect**.

3. ✅ **C. Zero Copy Data Transfer**  
   **Correct**.

4. ❌ **D. Data Batching**  
   **Incorrect**.

</details>

## Question 42 (Kafka Internals):
Your manager would like to have topic availability over consistency. Which setting do you need to change in order to enable that?

- A. unclean.leader.election.enable
- B. min.insync.replicas
- C. compression.type

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

unclean.leader.election.enable=true allows non ISR replicas to become leader, ensuring availability but losing consistency as data loss will occur

**Detailed explanation of each option:**

1. ✅ **A. unclean.leader.election.enable**  
   **Correct**.

2. ❌ **B. min.insync.replicas**  
   **Incorrect**.

3. ❌ **C. compression.type**  
   **Incorrect**.

</details>

## Question 43 (Stream Processing):
An ecommerce wesbite sells some custom made goods. What‘s the natural way of modeling this data in Kafka streams?

- A. Purchase as stream, Product as stream, Customer as stream
- B. Purchase as table, Product as table, Customer as table
- C. Purchase as stream, Product as table, Customer as stream
- D. Purchase as stream, Product as table, Customer as table

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Mostly-static data is modeled as a table whereas business transactions should be modeled as a stream.

**Detailed explanation of each option:**

1. ❌ **A. Purchase as stream, Product as stream, Customer as stream**  
   **Incorrect**.

2. ❌ **B. Purchase as table, Product as table, Customer as table**  
   **Incorrect**.

3. ❌ **C. Purchase as stream, Product as table, Customer as stream**  
   **Incorrect**.

4. ✅ **D. Purchase as stream, Product as table, Customer as table**  
   **Correct**.

</details>

## Question 44 (Stream Processing):
Select the Kafka Streams joins that are always windowed joins.

- A. KStream-KStream join
- B. KStream-KTable join
- C. KStream-GlobalKTable
- D. KTable-KTable join

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

See: https://docs.confluent.io/current/streams/developer-guide/dsl-api.html#joining

**Detailed explanation of each option:**

1. ✅ **A. KStream-KStream join**  
   **Correct**.

2. ❌ **B. KStream-KTable join**  
   **Incorrect**.

3. ❌ **C. KStream-GlobalKTable**  
   **Incorrect**.

4. ❌ **D. KTable-KTable join**  
   **Incorrect**.

</details>

## Question 45 (Kafka Ecosystem):
What are the programming languages Apache Kafka is written in? 

- A. Python
- B. Java
- C. PHP
- D. Scala

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** B, D

**Explanation:**

Apache Kafka is a distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. It‘s open-source and developed by the Apache Software Foundation written in Scala and Java. Further reading: Apache Kafka.

**Detailed explanation of each option:**

1. ❌ **A. Python**  
   **Incorrect**.

2. ✅ **B. Java**  
   **Correct**.

3. ❌ **C. PHP**  
   **Incorrect**.

4. ✅ **D. Scala**  
   **Correct**.

</details>

## Question 46 (Kafka Setup and Operations):
If you enable an SSL endpoint in Kafka, what feature of Kafka will be lost?

- A. Zero copy
- B. Exactly-once delivery
- C. Support for Avro format
- D. Cross-cluster mirroring

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

With SSL, messages will need to be encrypted and decrypted, by being first loaded into the JVM, so you lose the zero copy optimization. See more information here: https://twitter.com/ijuma/status/1161303431501324293?s=09

**Detailed explanation of each option:**

1. ✅ **A. Zero copy**  
   **Correct**.

2. ❌ **B. Exactly-once delivery**  
   **Incorrect**.

3. ❌ **C. Support for Avro format**  
   **Incorrect**.

4. ❌ **D. Cross-cluster mirroring**  
   **Incorrect**.

</details>

## Question 47 (Kafka Internals):
A producer application was sending messages to a partition with a replication factor of 2 by connecting to Broker 1 that was hosting partition leader. If the Broker 1 goes down, what will happen?

- A. The producer will automatically produce to the broker that has been elected leader
- B. The producer will stop working
- C. The topic will be unavailable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. The producer will automatically produce to the broker that has been elected leader**  
   **Correct**.

2. ❌ **B. The producer will stop working**  
   **Incorrect**.

3. ❌ **C. The topic will be unavailable**  
   **Incorrect**.

</details>

## Question 48 (Kafka Producers):
Which of the following options are true for Kafka producers? 

- A. Kafka producers send a produce request to the leader of a topic partition.
- B. Kafka guarantees that all producer messages will be sent to the same partition.
- C. Kafka producers have no need for group coordination.
- D. Kafka producers can send data with a key, in which case the data will be send round-robin to all available brokers.

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** A, C

**Explanation:**

In Kafka, producers create and write messages to topic partitions. Some concepts of producers are: – Producers are conceptually much simpler than consumers since they have no need for group coordination. – Producers automatically know to which broker and partition to write to. – A producer partitioner maps each message to a topic partition, and the producer sends a produce request to the leader of that partition. – The partitioners shipped with Kafka guarantee that all messages with the same non-empty key will be sent to the same partition. – If producers send data without a key, then the data will be send round-robin to all available brokers. – Producers can choose to receive acknowledgement of data writes. Further reading: Producer Concepts.

**Detailed explanation of each option:**

1. ✅ **A. Kafka producers send a produce request to the leader of a topic partition.**  
   **Correct**.

2. ❌ **B. Kafka guarantees that all producer messages will be sent to the same partition.**  
   **Incorrect**.

3. ✅ **C. Kafka producers have no need for group coordination.**  
   **Correct**.

4. ❌ **D. Kafka producers can send data with a key, in which case the data will be send round-robin to all available brokers.**  
   **Incorrect**.

</details>

## Question 49 (Kafka Consumers):
A consumer starts and has auto.offset.reset=none, and the topic partition currently has data for offsets going from 45 to 2311. The consumer group has committed the offset 10 for the topic before. Where will the consumer read from?

- A. offset 45
- B. it will crash
- C. offset 10
- D. offset 2311

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

auto.offset.reset=none means that the consumer will crash if the offsets it‘s recovering from have been deleted from Kafka, which is the case here, as 10 < 45

**Detailed explanation of each option:**

1. ❌ **A. offset 45**  
   **Incorrect**.

2. ✅ **B. it will crash**  
   **Correct**.

3. ❌ **C. offset 10**  
   **Incorrect**.

4. ❌ **D. offset 2311**  
   **Incorrect**.

</details>

## Question 50 (Kafka Producers):
If I supply the setting compression.type=snappy to my producer, what will happen? 

- A. The Kafka brokers have to de-compress the data
- B. The Producers have to compress the data
- C. The Consumers have to compress the data
- D. The Kafka brokers have to compress the data
- E. The Consumers have to de-compress the data

Choose the correct answers.

<details>
<summary>Response:</summary>

**Answer:** B, E

**Explanation:**

Kafka transfers data with zero copy and no transformation. Any transformation (including compression) is the responsibility of clients.

**Detailed explanation of each option:**

1. ❌ **A. The Kafka brokers have to de-compress the data**  
   **Incorrect**.

2. ✅ **B. The Producers have to compress the data**  
   **Correct**.

3. ❌ **C. The Consumers have to compress the data**  
   **Incorrect**.

4. ❌ **D. The Kafka brokers have to compress the data**  
   **Incorrect**.

5. ✅ **E. The Consumers have to de-compress the data**  
   **Correct**.

</details>

## Question 51 (Kafka Setup and Operations):
What happens when broker.rack configuration is provided in broker configuration in Kafka cluster?

- A. Replicas for a partition are placed in the same rack
- B. Replicas for a partition are spread across different racks
- C. You can use the same broker.id as long as they have different broker.rack configuration
- D. Each rack contains all the topics and partitions, effectively making Kafka highly available

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Partitions for newly created topics are assigned in a rack alternating manner, this is the only change broker.rack does

**Detailed explanation of each option:**

1. ❌ **A. Replicas for a partition are placed in the same rack**  
   **Incorrect**.

2. ✅ **B. Replicas for a partition are spread across different racks**  
   **Correct**.

3. ❌ **C. You can use the same broker.id as long as they have different broker.rack configuration**  
   **Incorrect**.

4. ❌ **D. Each rack contains all the topics and partitions, effectively making Kafka highly available**  
   **Incorrect**.

</details>

## Question 52 (Stream Processing):
An ecommerce website maintains two topics – a high volume “purchase“ topic with 5 partitions and low volume “customer“ topic with 3 partitions. You would like to do a stream-table join of these topics. How should you proceed?

- A. Repartition customer topic to have 5 partitions
- B. Repartition the purchase topic to have 3 partitions
- C. Model customer as a GlobalKTable
- D. Do a KStream / KTable join after a repartition step

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In case of KStream-KStream join, both need to be co-partitioned. This restriction is not applicable in case of join with GlobalKTable, which is the most efficient here.

**Detailed explanation of each option:**

1. ❌ **A. Repartition customer topic to have 5 partitions**  
   **Incorrect**.

2. ❌ **B. Repartition the purchase topic to have 3 partitions**  
   **Incorrect**.

3. ✅ **C. Model customer as a GlobalKTable**  
   **Correct**.

4. ❌ **D. Do a KStream / KTable join after a repartition step**  
   **Incorrect**.

</details>

## Question 53 (Kafka Consumers):
In the Kafka consumer metrics it is observed that fetch‑rate is very high and each fetch is small. What steps will you take to increase throughput?

- A. Decrease fetch.max.bytes
- B. Increase fetch.min.bytes
- C. Decrease fetch.min.bytes
- D. Increase fetch.max.wait
- E. Increase fetch.max.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Decrease fetch.max.bytes**  
   **Incorrect**.

2. ✅ **B. Increase fetch.min.bytes**  
   **Correct**.

3. ❌ **C. Decrease fetch.min.bytes**  
   **Incorrect**.

4. ❌ **D. Increase fetch.max.wait**  
   **Incorrect**.

5. ❌ **E. Increase fetch.max.bytes**  
   **Incorrect**.

</details>

## Question 54 (Kafka Connect):
Using Kafka Connect Source to read data from an external database, which processes do the actual work and execute connectors and tasks? 

- A. Transformers
- B. Workers
- C. Brokers
- D. Converters

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka Connect is a framework to stream data into and out of Apache Kafka. In order to efficiently discuss the inner workings of Kafka Connect, it is helpful to establish a few major concepts: – Connectors: the high level abstraction that coordinates data streaming by managing tasks. – Tasks: the implementation of how data is copied to or from Kafka. – Workers: the running processes that execute connectors and tasks. – Converters: the code used to translate data between Connect and the system sending or receiving data. – Transforms: simple logic to alter each message produced by or sent to a connector. – Dead Letter Queue: how Connect handles connector errors. Further reading: Kafka Connect Concepts.

**Detailed explanation of each option:**

1. ❌ **A. Transformers**  
   **Incorrect**.

2. ✅ **B. Workers**  
   **Correct**.

3. ❌ **C. Brokers**  
   **Incorrect**.

4. ❌ **D. Converters**  
   **Incorrect**.

</details>

## 🚫 Question 55 (Kafka Setup and Operations):
How much should be the heap size of a broker in a production setup on a machine with 256 GB of RAM, in PLAINTEXT mode?

- A. 4 GB
- B. 16 GB
- C. 128 GB
- D. 512 MB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. 4 GB**  
   **Correct**.

2. ❌ **B. 16 GB**  
   **Incorrect**.

3. ❌ **C. 128 GB**  
   **Incorrect**.

4. ❌ **D. 512 MB**  
   **Incorrect**.

</details>
