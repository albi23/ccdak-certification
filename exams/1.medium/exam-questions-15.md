## Question 1 (Kafka Core Concepts):
When the auto.create.topics.enable setting is configured as true in Kafka, what are the conditions in which a Kafka broker will autonomously generate a topic? 

- A. Consumer reads message from a topic
- B. Producer sends message to a topic
- C. Client requests metadata for a topic
- D. Client alters number of partitions of a topic

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, B, C

**Explanation:**

When auto.create.topics.enable is set to true in Kafka broker configuration, the circumstances under which a Kafka broker automatically creates a topic are:1. Producer sends message to a topic: If a producer sends a message to a topic that does not exist, and auto.create.topics.enable is true, the Kafka broker will automatically create the topic with default settings.2. Consumer reads message from a topic: Similarly, if a consumer tries to read from a topic that does not exist, the broker will create the topic automatically if auto.create.topics.enable is set to true.3. Client requests metadata for a topic: When a client requests metadata for a topic that does not exist, if auto.create.topics.enable is true, the broker will create the topic. This might occur when a client is checking for the existence of a topic or its properties.Altering the number of partitions of a topic (Client alters number of partitions of a topic) does not automatically create a topic. The topic must exist before its partition count can be altered. If a topic doesn‘t exist, trying to change its partition count won‘t lead to automatic topic creation, even if auto.create.topics.enable is true.

**Detailed explanation of each option:**

1. ✅ **A. Consumer reads message from a topic**  
   **Correct**.

2. ✅ **B. Producer sends message to a topic**  
   **Correct**.

3. ✅ **C. Client requests metadata for a topic**  
   **Correct**.

4. ❌ **D. Client alters number of partitions of a topic**  
   **Incorrect**.

</details>

## Question 2 (Kafka Consumers):
What is the process by which a Kafka consumer commits offsets?

- A. It interacts with the Group Coordinator broker
- B. It directly commits the offsets in Zookeeper
- C. It directly sends a message to the __consumer_offsets topic

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

It interacts with the Group Coordinator broker.Here‘s why:Zookeeper: Zookeeper used to be responsible for storing committed offsets in earlier versions of Kafka. However, since Kafka 0.11, offsets are no longer stored in Zookeeper.__consumer_offsets topic: Although a topic named __consumer_offsets exists, consumers don‘t directly send messages to it to commit offsets. This topic is internal and managed by the Kafka cluster.Group Coordinator broker: Each consumer group has a designated Group Coordinator broker responsible for managing the group‘s membership, offset coordination, and failover handling. Therefore, when a consumer commits offsets, it sends a request to the Group Coordinator, which updates the offsets information across the cluster.So, to reiterate, consumers commit offsets by interacting with their designated Group Coordinator broker, ensuring coordination and consistency within the consumer group.I hope this clarifies the process of how consumers commit offsets in Kafka!

**Detailed explanation of each option:**

1. ✅ **A. It interacts with the Group Coordinator broker**  
   **Correct**.

2. ❌ **B. It directly commits the offsets in Zookeeper**  
   **Incorrect**.

3. ❌ **C. It directly sends a message to the __consumer_offsets topic**  
   **Incorrect**.

</details>

## Question 3 (Kafka Consumers):
A consumer in a Kafka cluster is experiencing lag. What does this mean in terms of message consumption?

- A. Consumer is consuming messages too quickly.
- B. Consumer is consuming messages too slowly.
- C. Consumer is consuming messages in the correct order.
- D. Consumer is not consuming any messages.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The consumer is consuming messages too slowly. Explanation: Consumer lag in Kafka refers to the scenario where a consumer is falling behind in processing messages compared to the rate at which new messages are produced. This lag can occur when the consumer is not able to keep up with the incoming message rate, leading to a delay in message consumption. Consumer lag can be attributed to factors such as slow processing, inadequate resources, or inefficient handling of messages by the consumer application. Monitoring and addressing consumer lag is crucial to maintaining real-time or near-real-time processing in Kafka systems.

**Detailed explanation of each option:**

1. ❌ **A. Consumer is consuming messages too quickly.**  
   **Incorrect**.

2. ✅ **B. Consumer is consuming messages too slowly.**  
   **Correct**.

3. ❌ **C. Consumer is consuming messages in the correct order.**  
   **Incorrect**.

4. ❌ **D. Consumer is not consuming any messages.**  
   **Incorrect**.

</details>

## Question 4 (Kafka Producers):
You want to configure a Kafka producer to wait for acknowledgment from the leader broker before considering a message as sent. Which acknowledgment setting should you use?

- A. acks=0
- B. acks=1
- C. acks=all
- D. acks=-1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To configure a Kafka producer to wait for acknowledgment from the leader broker before considering a message as sent, you should use: acks=1 Explanation: The acks configuration parameter in Kafka producer settings determines the number of acknowledgments the producer requires from the broker before considering a message as sent. acks=0: The producer does not wait for any acknowledgment, which may lead to potential message loss if the leader broker fails before replicating the message to any replica. acks=1: The producer waits for acknowledgment from the leader broker. Once the leader acknowledges the message, the producer considers it sent. This setting provides a balance between performance and reliability. acks=all or acks=-1: The producer waits for acknowledgment from all in-sync replicas, ensuring higher durability at the cost of increased latency. For waiting for acknowledgment from the leader, acks=1 is typically used to achieve a good balance between performance and reliability.

**Detailed explanation of each option:**

1. ❌ **A. acks=0**  
   **Incorrect**.

2. ✅ **B. acks=1**  
   **Correct**.

3. ❌ **C. acks=all**  
   **Incorrect**.

4. ❌ **D. acks=-1**  
   **Incorrect**.

</details>

## Question 5 (Reliable Data Delivery):
A Kafka producer is configured with acks=all. What does this setting ensure regarding message acknowledgment?

- A. No acknowledgment is required.
- B. Leader acknowledgment is sufficient.
- C. Acknowledgment from all in-sync replicas is required.
- D. Acknowledgment from the producer is required.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

When a Kafka producer is configured with acks=all, it ensures that: Acknowledgment from all in-sync replicas is required. Explanation: The acks (acknowledgments) configuration in Kafka specifies how many acknowledgments the producer requires from brokers to consider a message as sent. acks=0: No acknowledgment is required, and the producer does not wait for acknowledgment from the broker. acks=1: Acknowledgment from the leader broker is sufficient. acks=all or acks=-1: Acknowledgment from all in-sync replicas is required. In this mode, the producer waits for acknowledgments from all replicas that are in sync with the leader for the partition. Configuring acks=all provides a higher level of durability, as it ensures that a message is not considered sent until it has been replicated to all in-sync replicas. However, it also comes with increased latency compared to lower acknowledgment settings.

**Detailed explanation of each option:**

1. ❌ **A. No acknowledgment is required.**  
   **Incorrect**.

2. ❌ **B. Leader acknowledgment is sufficient.**  
   **Incorrect**.

3. ✅ **C. Acknowledgment from all in-sync replicas is required.**  
   **Correct**.

4. ❌ **D. Acknowledgment from the producer is required.**  
   **Incorrect**.

</details>

## Question 6 (Programming & Serialization):
Which of the following is not an Avro primitive type?

- A. string
- B. int
- C. long
- D. null
- E. date

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** E

**Explanation:**

In Avro, the type that is not a primitive type is:dateAvro‘s primitive types include null, boolean, int, long, float, double, bytes, and string. These are the basic types that Avro directly supports for serialization and deserialization without additional specifications.date is not a primitive type in Avro. Instead, it is typically represented using an int or long type with a logical type annotation. Avro supports logical types which are a way to extend the basic Avro types to provide a clearer semantic for certain data patterns. For example, a date can be represented as an int with a logical type of date.

**Detailed explanation of each option:**

1. ❌ **A. string**  
   **Incorrect**.

2. ❌ **B. int**  
   **Incorrect**.

3. ❌ **C. long**  
   **Incorrect**.

4. ❌ **D. null**  
   **Incorrect**.

5. ✅ **E. date**  
   **Correct**.

</details>

## Question 7 (Kafka Ecosystem):
You need to interact with a Kafka cluster using HTTP requests for producing messages. Which Confluent component provides the capability to access Kafka clusters through HTTP?

- A. Confluent Control Center
- B. Confluent REST Proxy
- C. Confluent Schema Registry
- D. Confluent Connect

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The Confluent component that provides the capability to interact with a Kafka cluster using HTTP requests for producing messages is: Confluent REST Proxy Explanation: Confluent REST Proxy is a component that enables HTTP access to Kafka clusters. It acts as a RESTful interface to a Kafka cluster, allowing producers and consumers to interact with Kafka using HTTP requests. With Confluent REST Proxy, you can use simple HTTP requests to produce messages to Kafka topics and consume messages from Kafka topics. It provides a convenient HTTP-based interface for applications that may not have direct access to the Kafka client libraries, making it easier to integrate with Kafka in various programming languages.

**Detailed explanation of each option:**

1. ❌ **A. Confluent Control Center**  
   **Incorrect**.

2. ✅ **B. Confluent REST Proxy**  
   **Correct**.

3. ❌ **C. Confluent Schema Registry**  
   **Incorrect**.

4. ❌ **D. Confluent Connect**  
   **Incorrect**.

</details>

## Question 8 (Kafka Consumers):
You want to configure a Kafka consumer to start consuming messages from the earliest offset when there is no previously committed offset. What should you set auto.offset.reset to?

- A. earliest
- B. latest
- C. none
- D. all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To configure a Kafka consumer to start consuming messages from the earliest offset when there is no previously committed offset, you should set auto.offset.reset to: earliest Explanation: The auto.offset.reset configuration in Kafka determines the behavior of the consumer when there is no previously committed offset for a partition or when the committed offset is invalid. earliest: This setting causes the consumer to start consuming messages from the earliest available offset if there is no previously committed offset. It reads all messages from the beginning of the partition. latest: This setting makes the consumer start consuming messages from the latest offset in the partition if there is no previously committed offset. It ensures that the consumer reads only new messages produced after the consumer starts. none: This setting throws an exception if no offset is found for the consumer group, requiring explicit offset initialization. all: This setting is not a valid option for auto.offset.reset. In this case, setting auto.offset.reset to earliest is appropriate to begin consuming messages from the earliest offset when no committed offset is available.

**Detailed explanation of each option:**

1. ✅ **A. earliest**  
   **Correct**.

2. ❌ **B. latest**  
   **Incorrect**.

3. ❌ **C. none**  
   **Incorrect**.

4. ❌ **D. all**  
   **Incorrect**.

</details>

## Question 9 (Stream Processing):
In a Kafka Streams application, you are aggregating values and need to handle out-of-order events gracefully. What Kafka Streams operation should you use for handling out-of-order events?

- A. filter
- B. map
- C. windowedBy
- D. gracefulOutOfOrderHandling

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In a Kafka Streams application, if you need to handle out-of-order events gracefully, you should use the windowedBy operation with a time window combined with a custom grace period. Explanation: Out-of-order events can occur when events in your Kafka stream are not strictly ordered by their timestamps. To handle such situations gracefully, you can use time windows with a custom grace period. The windowedBy operation in Kafka Streams is used to define time windows, and you can set a grace period to handle out-of-order events.

**Detailed explanation of each option:**

1. ❌ **A. filter**  
   **Incorrect**.

2. ❌ **B. map**  
   **Incorrect**.

3. ✅ **C. windowedBy**  
   **Correct**.

4. ❌ **D. gracefulOutOfOrderHandling**  
   **Incorrect**.

</details>

## Question 10 (Kafka Consumers):
while (true) { ConsumerRecords records = consumer.poll(100); try { consumer.commitSync(); } catch (CommitFailedExceptio? { log.error(“commit failed“? } for (ConsumerRecord record : records) { System.out.printf(“topic = %s, partition = %s, offset = %d, customer = %s, country = %s“, record.topic(), record.partition(), record.offset(), record.key(), record.value()); }}What type of delivery assurance does this consumer provide?

- A. Exactly-once
- B. At-most-once
- C. At-least-once

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Here offset is committed before processing the message. If consumer crashes before processing the message, message will be lost when it comes back up.

**Detailed explanation of each option:**

1. ❌ **A. Exactly-once**  
   **Incorrect**.

2. ✅ **B. At-most-once**  
   **Correct**.

3. ❌ **C. At-least-once**  
   **Incorrect**.

</details>

## Question 11 (Kafka Producers):
You want to configure a Kafka producer to send messages to multiple brokers in parallel. Which producer configuration setting should you adjust?

- A. acks
- B. retries
- C. max.in.flight.requests.per.connection
- D. batch.size

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

configure a Kafka producer to send messages to multiple brokers in parallel, you should adjust the max.in.flight.requests.per.connection configuration setting. Explanation: The max.in.flight.requests.per.connection configuration in Kafka determines the maximum number of unacknowledged requests that can be in-flight to a broker before blocking further sends. By increasing this value, you allow the producer to have more concurrent in-flight requests to different brokers, which can improve parallelism in message sending. The other options: acks: This configuration controls the number of acknowledgments the producer requires for a message to be considered sent. It doesn‘t directly impact the parallelism of sending messages to multiple brokers. retries: This setting specifies the number of retries the producer should attempt in case of message send failures. It does not control parallelism across multiple brokers. batch.size: This configuration controls the number of bytes that trigger a send to the broker. While adjusting it can impact the efficiency of message batching, it doesn‘t directly affect sending messages to multiple brokers in parallel.

**Detailed explanation of each option:**

1. ❌ **A. acks**  
   **Incorrect**.

2. ❌ **B. retries**  
   **Incorrect**.

3. ✅ **C. max.in.flight.requests.per.connection**  
   **Correct**.

4. ❌ **D. batch.size**  
   **Incorrect**.

</details>

## Question 12 (Kafka Producers):
What two effects will occur when the compression.type=snappy setting is used in a Kafka producer configuration?

- A. The Consumers have to compress the data
- B. The Kafka brokers have to de-compress the data
- C. The Kafka brokers have to compress the data
- D. The Producers have to compress the data
- E. The Consumers have to de-compress the data

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** D, E

**Explanation:**

If you apply the setting compression.type=snappy to your producer, the following two things will happen:1. The Producers have to compress the data.2. The Consumers have to de-compress the data.Producers Compress the Data: When you specify compression.type=snappy in the producer configuration, it instructs the Kafka producer to compress messages using the Snappy compression algorithm before sending them to the Kafka brokers. This can improve performance, especially for large messages, by reducing the amount of data transmitted over the network.Consumers Decompress the Data: On the consumer side, the messages are received in their compressed form. Therefore, the Kafka consumers are responsible for decompressing the messages after they are retrieved from the Kafka brokers but before they are processed by the consumer application.Kafka Brokers: The Kafka brokers do not perform the compression or decompression in this case. They store and forward the messages in whatever form they receive them. If the producers send compressed messages, the brokers store them compressed and then pass them to the consumers in the same compressed form.

**Detailed explanation of each option:**

1. ❌ **A. The Consumers have to compress the data**  
   **Incorrect**.

2. ❌ **B. The Kafka brokers have to de-compress the data**  
   **Incorrect**.

3. ❌ **C. The Kafka brokers have to compress the data**  
   **Incorrect**.

4. ✅ **D. The Producers have to compress the data**  
   **Correct**.

5. ✅ **E. The Consumers have to de-compress the data**  
   **Correct**.

</details>

## Question 13 (Kafka Core Concepts):
How does Kafka handle the ordering of messages within a partition?

- A. Messages are always ordered by timestamp.
- B. Messages are ordered by the producer.
- C. Messages are randomly ordered.
- D. Messages are ordered by their offset.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Messages within a Kafka partition are ordered by their offset. Explanation: Kafka assigns a unique offset to each message within a partition. The ordering of messages is based on these offsets. As messages are produced to a partition, each message receives an offset greater than the offsets of previously produced messages in that partition. When consumers read messages from a partition, they do so in the order of these offsets, ensuring a sequential and ordered processing of messages within that partition. This offset-based ordering is a fundamental aspect of Kafka, providing a reliable and deterministic sequence for messages within a partition.

**Detailed explanation of each option:**

1. ❌ **A. Messages are always ordered by timestamp.**  
   **Incorrect**.

2. ❌ **B. Messages are ordered by the producer.**  
   **Incorrect**.

3. ❌ **C. Messages are randomly ordered.**  
   **Incorrect**.

4. ✅ **D. Messages are ordered by their offset.**  
   **Correct**.

</details>

## Question 14 (Stream Processing):
A Kafka Streams application is consuming data from a topic, and you need to store the latest state for each key. What Kafka Streams operation should you use for this requirement?

- A. filter
- B. map
- C. windowedBy
- D. suppress

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. filter**  
   **Incorrect**.

2. ❌ **B. map**  
   **Incorrect**.

3. ❌ **C. windowedBy**  
   **Incorrect**.

4. ✅ **D. suppress**  
   **Correct**.

</details>

## Question 15 (Kafka Producers):
How does a KafkaProducer manage the transmission of a 3 MB message to a topic that is set up with the default configuration for message sizes?

- A. KafkaProducer divides messages into sizes of message.max.bytes and sends them in order
- B. MessageSizeTooLarge exception will be thrown, KafkaProducer will not retry and return exception immediately
- C. MessageSizeTooLarge exception will be thrown, KafkaProducer retries until the number of retries are exhausted
- D. KafkaProducer divides messages into sizes of max.request.size and sends them in order

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

If you try to send a message of size 3 MB to a Kafka topic with the default message size configuration, the behavior will be:MessageSizeTooLarge exception will be thrown, KafkaProducer will not retry and return exception immediatelyKafka has a default maximum message size limit (message.max.bytes for the broker and max.request.size for the producer). By default, this is typically set to 1 MB.If a message exceeds this limit, Kafka does not automatically split the message into smaller chunks. Kafka expects messages to be within the configured size limits.When a message that exceeds this limit is sent, a MessageSizeTooLarge exception is thrown. This is an immediate response indicating that the message size exceeds the configured maximum.KafkaProducer does not automatically retry sending a message that has thrown a MessageSizeTooLarge exception. The retry mechanism in KafkaProducer typically handles transient errors (like a temporary network issue), but a message size being too large is considered a non-transient, definitive error.To successfully send larger messages, you would need to manually increase the message.max.bytes setting on the broker and the max.request.size on the producer to accommodate the larger message size. However, increasing these limits should be done with caution, as very large messages can affect performance and stability.

**Detailed explanation of each option:**

1. ❌ **A. KafkaProducer divides messages into sizes of message.max.bytes and sends them in order**  
   **Incorrect**.

2. ✅ **B. MessageSizeTooLarge exception will be thrown, KafkaProducer will not retry and return exception immediately**  
   **Correct**.

3. ❌ **C. MessageSizeTooLarge exception will be thrown, KafkaProducer retries until the number of retries are exhausted**  
   **Incorrect**.

4. ❌ **D. KafkaProducer divides messages into sizes of max.request.size and sends them in order**  
   **Incorrect**.

</details>

## Question 16 (Kafka Setup and Operations):
You want to monitor Kafka metrics related to message throughput and latency. Which Kafka tools can provide these metrics?

- A. Kafka Connect
- B. Kafka Streams
- C. Prometheus with Grafana
- D. Kafka Mirror Maker

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Option C. Prometheus with Grafana Correct because Prometheus can scrape Kafka JMX metrics (through exporters) and Grafana can visualize them. This combination is widely used to monitor Kafka clusters, providing dashboards for throughput, latency, consumer lag, broker health, and topic metrics. It is the industry‑standard solution for Kafka monitoring and alerting. Incorrect Option A. Kafka Connect Incorrect because Kafka Connect is used for data integration (moving data between Kafka and external systems). While it exposes some metrics about connectors and tasks, it is not designed to provide cluster‑wide throughput and latency monitoring. Option B. Kafka Streams Incorrect because Kafka Streams is a stream processing library for building applications. It provides application‑level metrics (like task throughput), but it does not monitor Kafka cluster metrics such as broker latency or topic throughput. Option D. Kafka Mirror Maker Incorrect because Mirror Maker is used for replicating topics across clusters. It does not provide monitoring capabilities for throughput and latency; instead, it focuses on data replication.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Connect**  
   **Incorrect**.

2. ❌ **B. Kafka Streams**  
   **Incorrect**.

3. ✅ **C. Prometheus with Grafana**  
   **Correct**.

4. ❌ **D. Kafka Mirror Maker**  
   **Incorrect**.

</details>

## 🚫 Question 17 (Kafka Ecosystem):
You are dealing with a Kafka topic that contains nested JSON structures, and you want to extract specific fields from these nested structures in KSQL. What KSQL function should you use for nested field extraction?

- A. EXTRACT
- B. FLATTEN
- C. UNPACK
- D. JSONEXTRACT

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

JSONEXTRACT Explanation: To extract specific fields from nested JSON structures in KSQL, you should use the JSONEXTRACT function. This function allows you to navigate through nested structures and extract the desired fields. Therefore, the correct option is: JSONEXTRACT

**Detailed explanation of each option:**

1. ❌ **A. EXTRACT**  
   **Incorrect**.

2. ❌ **B. FLATTEN**  
   **Incorrect**.

3. ❌ **C. UNPACK**  
   **Incorrect**.

4. ✅ **D. JSONEXTRACT**  
   **Correct**.

</details>

## Question 18 (Kafka Setup and Operations):
With a cluster consisting of five brokers, a topic having 10 partitions, a replication factor of 3, and a specified quota of “producer_bytes_rate“ set to 1 MB/sec for the client, what is the client‘s maximum permissible throughput?

- A. 0.33 MB/s
- B. 1 MB/s
- C. 10 MB/s
- D. 5 MB/s

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

The maximum throughput allowed for the client would be 5 MB/s.In this setup, each producer is permitted to produce at a rate of 1 MB/s per broker.Since there are five brokers in the cluster, and the producer can send data to each broker at the maximum rate, the total throughput is effectively the sum of the throughput to each broker.Hence, the total maximum throughput allowed for the client is 5 MB/s (1 MB/s per broker multiplied by 5 brokers).This approach takes advantage of the distributed nature of Kafka, where a producer can interact with multiple brokers, thereby increasing the overall throughput capacity.

**Detailed explanation of each option:**

1. ❌ **A. 0.33 MB/s**  
   **Incorrect**.

2. ❌ **B. 1 MB/s**  
   **Incorrect**.

3. ❌ **C. 10 MB/s**  
   **Incorrect**.

4. ✅ **D. 5 MB/s**  
   **Correct**.

</details>

## Question 19 (Kafka Internals):
You want to configure a Kafka topic to have multiple copies of each message distributed across different brokers. What configuration should you adjust?

- A. Replication factor
- B. Producer acknowledgment setting
- C. Consumer fetch size
- D. Topic partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The configuration you should adjust to have multiple copies of each message distributed across different brokers in Kafka is the “Replication factor.“ Explanation: The replication factor in Kafka determines how many copies, or replicas, of each partition should be maintained across different brokers. By increasing the replication factor, you ensure that each message stored in a partition is replicated to multiple brokers, providing fault tolerance and high availability. If one broker fails, the replicas on other brokers can still serve the data. Adjusting the replication factor is a key factor in designing a resilient Kafka system with data redundancy and distribution across the cluster.

**Detailed explanation of each option:**

1. ✅ **A. Replication factor**  
   **Correct**.

2. ❌ **B. Producer acknowledgment setting**  
   **Incorrect**.

3. ❌ **C. Consumer fetch size**  
   **Incorrect**.

4. ❌ **D. Topic partitions**  
   **Incorrect**.

</details>

## Question 20 (Kafka Consumers):
In Kafka, what is the purpose of the “offset.retention.minutes“ configuration?

- A. Retention period for consumer offsets.
- B. Retention period for producer offsets.
- C. Time before consumer rebalancing.
- D. Time before partition leader election.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The purpose of the “offset.retention.minutes“ configuration in Kafka is: Retention period for consumer offsets. Explanation: The “offset.retention.minutes“ configuration in Kafka determines the retention period for consumer offsets. Consumer offsets are used to track the progress of consumers in a consumer group, indicating the last successfully processed message in each partition. This configuration specifies the time period for which these consumer offsets are retained. If a consumer has not sent heartbeats or committed offsets within this duration, the consumer group coordinator may consider it inactive and trigger a rebalance. Setting an appropriate offset retention period is essential for managing consumer group stability and ensuring that consumer offsets are retained for a sufficient duration to handle potential delays or temporary failures in consumer processing.

**Detailed explanation of each option:**

1. ✅ **A. Retention period for consumer offsets.**  
   **Correct**.

2. ❌ **B. Retention period for producer offsets.**  
   **Incorrect**.

3. ❌ **C. Time before consumer rebalancing.**  
   **Incorrect**.

4. ❌ **D. Time before partition leader election.**  
   **Incorrect**.

</details>

## Question 21 (Stream Processing):
For calculating the average of all events within each five-minute window, with updates every minute, what type of windowing should be implemented in Kafka Streams

- A. Hopping window
- B. Sliding window
- C. Session window
- D. Tumbling window

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

For computing the average of all events in every five-minute window, updated every minute, you would require a Hopping window in Kafka Streams.Explanation:Hopping Window: A hopping window is a type of windowing mechanism that moves forward in fixed increments. For your requirement, where you want the window to be five minutes long and to update every minute, a hopping window is ideal. The window “hops“ every minute, but each window covers a five-minute span of events.Sliding Window: A sliding window is another type of window, but it calculates results over a period of time that slides for each event. It‘s more suitable for cases where you need to compute results over a dynamic time frame that changes with each new event.Session Window: A session window is used when the window duration is not fixed and can vary based on the activity (or inactivity) of each key. Session windows are typically used to capture bursts of activity. This doesn‘t align with the requirement for a fixed, regularly updated window.Tumbling Window: Tumbling windows are fixed-sized, non-overlapping windows. They are a special case of hopping windows where the hop size is equal to the window size. This type of window wouldn‘t be appropriate for your case since you need overlapping windows (every minute within a five-minute span).

**Detailed explanation of each option:**

1. ✅ **A. Hopping window**  
   **Correct**.

2. ❌ **B. Sliding window**  
   **Incorrect**.

3. ❌ **C. Session window**  
   **Incorrect**.

4. ❌ **D. Tumbling window**  
   **Incorrect**.

</details>

## Question 22 (Kafka Internals):
Given the Kafka configuration parameters: log.retention.hours = 168, log.retention.minutes = 168, and log.retention.ms = 168, what is the duration for which messages will be retained?

- A. 168 hours
- B. 168 ms
- C. 168 minutes
- D. Broker will not start due to bad configuration

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In Kafka, when multiple log retention settings are provided with different time units, the smallest unit takes precedence. In your configuration, you have log.retention.hours = 168, log.retention.minutes = 168, and log.retention.ms = 168.Since milliseconds (ms) is the smallest unit among hours, minutes, and milliseconds, log.retention.ms = 168 will take precedence. Therefore, the messages will be retained for 168 milliseconds.So, the correct answer is:168 ms

**Detailed explanation of each option:**

1. ❌ **A. 168 hours**  
   **Incorrect**.

2. ✅ **B. 168 ms**  
   **Correct**.

3. ❌ **C. 168 minutes**  
   **Incorrect**.

4. ❌ **D. Broker will not start due to bad configuration**  
   **Incorrect**.

</details>

## Question 23 (Kafka Setup and Operations):
Which of the following is not recognized as an authentication method in Kafka?

- A. SSL
- B. SAML
- C. SASL/GSSAPI
- D. SASL/SCRAM

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The option that is not a valid authentication mechanism in Kafka is:SAMLExplanation:SSL (Secure Sockets Layer): SSL is a standard security technology for establishing an encrypted link between a server and a client. In Kafka, SSL can be used for encrypting data in transit as well as for authentication.SASL/SCRAM (Simple Authentication and Security Layer/Salted Challenge Response Authentication Mechanism): SASL/SCRAM is a widely used authentication mechanism in Kafka that provides username and password-based authentication.SASL/GSSAPI (Simple Authentication and Security Layer/Generic Security Services Application Program Interface): This is another supported SASL mechanism in Kafka, often used for integrating with systems like Kerberos for authentication.SAML (Security Assertion Markup Language): SAML is a standard for exchanging authentication and authorization data between parties, but it is not a supported authentication mechanism in Kafka. Kafka‘s authentication mechanisms are primarily based around SSL and SASL.

**Detailed explanation of each option:**

1. ❌ **A. SSL**  
   **Incorrect**.

2. ✅ **B. SAML**  
   **Correct**.

3. ❌ **C. SASL/GSSAPI**  
   **Incorrect**.

4. ❌ **D. SASL/SCRAM**  
   **Incorrect**.

</details>

## Question 24 (Stream Processing):
In a scenario where your Kafka Streams application is consuming data from an input topic with 5 partitions, and you have deployed 5 instances of your application, each configured with num.streams.threads set to 5, how many stream tasks will be instantiated, and how many of them will be actively processing data?

- A. 25 created, 25 active
- B. 25 created, 5 active
- C. 5 created, 1 active
- D. 5 created, 5 active

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. 25 created, 5 active Correct because Kafka Streams creates stream threads based on the configured num.streams.threads. There are 5 application instances, each with 5 stream threads: 5 instances × 5 threads = 25 stream threads Therefore, up to 25 stream tasks can be instantiated across the application instances. However, the input topic has only 5 partitions. A stream task is associated with one or more partitions, and a partition can be actively processed by only one task within the application. Therefore, only 5 tasks can be active at a time because there are only 5 input partitions. The remaining tasks are created but remain idle because there are not enough partitions to assign to them. Incorrect: Option A. 25 created, 25 active Incorrect because there are only 5 partitions in the input topic. All 25 tasks cannot actively process data simultaneously when only 5 partitions are available. Therefore, only 5 tasks can be active. Option C. 5 created, 1 active Incorrect because the number of tasks is not determined only by the number of partitions. With 5 application instances × 5 stream threads, up to 25 stream tasks can be instantiated. Since there are 5 partitions, 5 tasks can actively process them. Option D. 5 created, 5 active Incorrect because although 5 tasks can be active, the configured 5 stream threads per instance across 5 instances results in 25 task/thread slots being created. Only 5 of those can actively process the 5 available partitions.

**Detailed explanation of each option:**

1. ❌ **A. 25 created, 25 active**  
   **Incorrect**.

2. ✅ **B. 25 created, 5 active**  
   **Correct**.

3. ❌ **C. 5 created, 1 active**  
   **Incorrect**.

4. ❌ **D. 5 created, 5 active**  
   **Incorrect**.

</details>

## Question 25 (Kafka Consumers):
A Kafka consumer is encountering a “group rebalance“ frequently. What consumer configuration setting might you adjust to address this issue?

- A. enable.auto.commit
- B. group.id
- C. auto.offset.reset
- D. max.poll.interval.ms

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

To address frequent “group rebalance“ issues in Kafka, you might adjust the max.poll.interval.ms consumer configuration setting. Explanation: The max.poll.interval.ms configuration in Kafka sets the maximum amount of time the consumer is allowed to spend processing messages during a poll() before it must commit its offsets. If the processing time exceeds this interval, the consumer is considered inactive, and a rebalance may be triggered to redistribute partitions among the consumers in the consumer group. By increasing the max.poll.interval.ms, you provide more time for the consumer to process messages without triggering frequent rebalances. However, it‘s important to strike a balance, as setting this value too high could delay detecting consumer failures. The other options: enable.auto.commit: This setting controls whether the consumer‘s offsets are automatically committed. Adjusting it might impact the commit frequency but may not directly address rebalance issues. group.id: This is the identifier for the consumer group. Changing it could result in the creation of a new consumer group, but it won‘t directly address frequent rebalances. auto.offset.reset: This setting determines the behavior when no offset is committed. Adjusting it might affect where the consumer starts reading messages, but it won‘t directly address the rebalance issue.

**Detailed explanation of each option:**

1. ❌ **A. enable.auto.commit**  
   **Incorrect**.

2. ❌ **B. group.id**  
   **Incorrect**.

3. ❌ **C. auto.offset.reset**  
   **Incorrect**.

4. ✅ **D. max.poll.interval.ms**  
   **Correct**.

</details>

## Question 26 (Kafka Connect):
You are configuring a Kafka Connect Source Connector to read Avro data from a Kafka topic. What configuration setting should you adjust to specify the Avro schema registry URL?

- A. connector.class
- B. schema.registry.url
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To specify the Avro schema registry URL when configuring a Kafka Connect Source Connector to read Avro data from a Kafka topic, you should adjust the configuration setting: schema.registry.url Explanation: The schema.registry.url configuration setting is used to specify the URL of the Avro schema registry. This registry is responsible for storing and managing Avro schemas, which are used for serialization and deserialization of Avro data. Here‘s an example of how you might configure the schema.registry.url: “schema.registry.url=http://your-schema-registry:port“ Replace your-schema-registry and port with the actual host and port where your Avro schema registry is running.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. schema.registry.url**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## Question 27 (Kafka Connect):
A Kafka Connect worker is running with multiple connectors. How does Kafka Connect ensure the parallelism of tasks across multiple connectors?

- A. Each connector has its worker.
- B. All tasks are executed sequentially.
- C. Tasks are distributed across available workers.
- D. Only one connector can run at a time.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

In Kafka Connect, when a Kafka Connect worker is running with multiple connectors, parallelism of tasks across multiple connectors is ensured by: Tasks are distributed across available workers. Explanation: Kafka Connect achieves parallelism by distributing tasks across multiple worker instances. Each connector can have multiple tasks, and these tasks are distributed and executed in parallel across the available worker nodes in a Kafka Connect cluster. The parallelism is achieved by dividing the work into tasks, where each task corresponds to a unit of work for a connector. Each task processes a subset of the data, and by having multiple tasks running in parallel, Kafka Connect can efficiently scale and handle a higher volume of data. This distributed and parallel processing allows Kafka Connect to achieve better throughput and scalability, making it suitable for handling large-scale data integration scenarios.

**Detailed explanation of each option:**

1. ❌ **A. Each connector has its worker.**  
   **Incorrect**.

2. ❌ **B. All tasks are executed sequentially.**  
   **Incorrect**.

3. ✅ **C. Tasks are distributed across available workers.**  
   **Correct**.

4. ❌ **D. Only one connector can run at a time.**  
   **Incorrect**.

</details>

## 🚫 Question 28 (Kafka Ecosystem):
What port does the KSQL server use by default for listening?

- A. 9092
- B. 2181
- C. 8088
- D. 8083

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The default port that the KSQL server listens on is 8088.9092: This is the default port for Kafka brokers, not for KSQL.2181: This is the default port for ZooKeeper, which Kafka uses for cluster management.8088: This is the correct default port for the KSQL server. KSQL is a streaming SQL engine that provides an interactive interface for running continuous SQL queries on Kafka streams and tables.8083: This is commonly the default port for Kafka Connect, a tool for streaming data between Apache Kafka and other data systems.

**Detailed explanation of each option:**

1. ❌ **A. 9092**  
   **Incorrect**.

2. ❌ **B. 2181**  
   **Incorrect**.

3. ✅ **C. 8088**  
   **Correct**.

4. ❌ **D. 8083**  
   **Incorrect**.

</details>

## Question 29 (Kafka Consumers):
In a situation where a Kafka consumer is set with auto.offset.reset=latest, and it‘s consuming from a topic partition that contains data within offset range 45 to 2311, and the consumer group has no prior committed offsets for this topic, at which offset will the consumer begin reading?

- A. offset 45
- B. offset 0
- C. offset 2311
- D. it will crash

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

If a consumer has auto.offset.reset=latest, and the topic partition currently has data for offsets ranging from 45 to 2311, and the consumer group has never committed offsets for the topic before, the consumer will start reading from:offset 2311auto.offset.reset=latest: This setting determines where a consumer starts reading if no offset has been committed. With latest, the consumer starts reading from the end of the log, which means it will only consume messages that are produced after the consumer starts.Since the offsets range from 45 to 2311, the “end“ of the log is at offset 2311. Therefore, the consumer will start reading from any new messages that arrive after offset 2311.offset 45, offset 0, and it will crash are incorrect in this context:offset 45: This would be the starting point if the auto.offset.reset were set to earliest and there were no committed offsets.offset 0: This is not applicable as it‘s outside the current range of the topic‘s data and would be relevant if the topic had no data and auto.offset.reset was set to earliest.It will crash: Kafka consumers don‘t crash in this scenario; they will start consuming from the specified offset based on the auto.offset.reset setting.

**Detailed explanation of each option:**

1. ❌ **A. offset 45**  
   **Incorrect**.

2. ❌ **B. offset 0**  
   **Incorrect**.

3. ✅ **C. offset 2311**  
   **Correct**.

4. ❌ **D. it will crash**  
   **Incorrect**.

</details>

## Question 30 (Kafka Internals):
You are implementing a Kafka application for a financial system, and you want to ensure that only the latest transaction details for each account are stored. What is the primary advantage of using log compaction in this scenario?

- A. Improved Kafka producer latency
- B. Reduced Kafka topic replication
- C. Efficient storage of the latest transaction details
- D. Increased Kafka broker memory usage

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Efficient storage of the latest transaction details Explanation: The primary advantage of using log compaction in this scenario is efficient storage of the latest transaction details. Log compaction in Kafka ensures that for each key (e.g., account number in this case), only the latest record is retained in the topic. This feature helps in reducing storage requirements and ensures that the Kafka topic retains the most recent state for each account.

**Detailed explanation of each option:**

1. ❌ **A. Improved Kafka producer latency**  
   **Incorrect**.

2. ❌ **B. Reduced Kafka topic replication**  
   **Incorrect**.

3. ✅ **C. Efficient storage of the latest transaction details**  
   **Correct**.

4. ❌ **D. Increased Kafka broker memory usage**  
   **Incorrect**.

</details>

## 🚫 Question 31 (Kafka Connect):
You are configuring a Kafka Connect Source Connector to read data from an FTP server. What configuration setting should you adjust to specify the FTP server address?

- A. connector.class
- B. ftp.server.address
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To specify the FTP server address when configuring a Kafka Connect Source Connector to read data from an FTP server, you should adjust the configuration setting: http://ftp.server.address Explanation: The http://ftp.server.address configuration setting is typically used in Kafka Connect Source Connectors designed for reading data from FTP servers. This setting allows you to provide the address or hostname of the FTP server from which the connector should fetch data. When configuring the Kafka Connect Source Connector for FTP, you would set the http://ftp.server.address parameter to the actual address or hostname of your FTP server. The other options: connector.class: This configuration setting specifies the class implementing the connector and is not specifically for providing the FTP server address. topics: This setting is used to specify the Kafka topics to which the connector should publish the data. key.converter: This setting determines the converter used for the key in the Kafka messages but is not related to specifying the FTP server address.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. ftp.server.address**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## 🚫 Question 32 (Kafka Connect):
You are configuring a Kafka Connect Sink Connector to write data to an Elasticsearch index. What configuration setting should you adjust to specify the Elasticsearch connection URL?

- A. connector.class
- B. elasticsearch.url
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Option B. elasticsearch.url Correct: This property specifies the connection URL for the Elasticsearch cluster. It tells the connector where to send data (e.g., http://localhost:9200 or the cluster endpoint). Without this setting, the connector cannot establish communication with Elasticsearch. Incorrect Option A. connector.class Incorrect: This defines the Java class implementing the connector (e.g., io.confluent.connect.elasticsearch.ElasticsearchSinkConnector). It does not specify the connection URL. Option C. topics Incorrect: This property defines which Kafka topics the connector consumes from. It controls the source of data, not the destination connection. Option D. key.converter Incorrect: This specifies how message keys are serialized/deserialized (e.g., JSON, Avro). It does not configure the Elasticsearch connection.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. elasticsearch.url**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## Question 33 (Kafka Internals):
When dealing with a log-compacted topic and attempting to send a message containing a key (K) and a null value, what is the expected outcome?

- A. The broker will delete all messages with the key K upon cleanup
- B. The message will get ignored by the Kafka broker
- C. The broker will delete the message with the key K and null value only upon cleanup
- D. The producer will throw a Runtime exception

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The broker will delete all messages with the key K upon cleanup. In Kafka, when using a log-compacted topic, sending a message with a key and a null value is a way to indicate that messages with that key should be deleted. This is known as a “tombstone“ message. When a tombstone message (a message with a key and a null value) is sent to a log-compacted topic, Kafka will eventually remove all messages with that key during the log compaction process.The key points are:The broker will delete all messages with the key K upon cleanup: This is correct. The tombstone message acts as a marker to delete all previous messages with the same key when log compaction runs.The message will get ignored by the Kafka broker: This is incorrect. Kafka brokers do not ignore messages with null values in log-compacted topics; they use them for the specific purpose of log compaction.The broker will delete the message with the key K and null value only upon cleanup: This is partially correct but incomplete. Not only will the broker eventually delete the tombstone message itself, but it will also delete all previous messages with that key.The producer will throw a Runtime exception: This is incorrect. Sending a message with a key and a null value is a valid operation in Kafka and does not result in a runtime exception.

**Detailed explanation of each option:**

1. ✅ **A. The broker will delete all messages with the key K upon cleanup**  
   **Correct**.

2. ❌ **B. The message will get ignored by the Kafka broker**  
   **Incorrect**.

3. ❌ **C. The broker will delete the message with the key K and null value only upon cleanup**  
   **Incorrect**.

4. ❌ **D. The producer will throw a Runtime exception**  
   **Incorrect**.

</details>

## Question 34 (Kafka Producers):
Which two exceptions are likely to be intercepted by the following producer code snippet?
```
ProducerRecord record = new ProducerRecord<>(“topic1“, “key1“, “value1“); 
try { producer.send(record); } 
catch (Exceptio? { e.printStackTrace();}
```


- A. SerializationException
- B. BrokerNotAvailableException
- C. InvalidPartitionsException
- D. BufferExhaustedException

Choose the correct answers .

<details>
<summary>Response:</summary>

**Answer:** A, D

**Explanation:**

The exceptions that may be caught by the given producer code snippet are:1. SerializationException2. BufferExhaustedExceptionSerializationException: This exception is thrown when there is an issue in serializing the key or value of the ProducerRecord. Since the producer needs to serialize the record‘s key and value into bytes before sending it to Kafka, any serialization errors will result in a SerializationException.BufferExhaustedException: This occurs when the producer is unable to allocate memory for the record within the maximum buffer size specified. If the producer buffer is full (i.e., all memory allocated for the buffer is being used and hasn‘t yet been sent to or acknowledged by the Kafka broker), and the producer is unable to send the record before reaching the configured max.block.ms, it throws a BufferExhaustedException.BrokerNotAvailableException: This exception is not directly relevant in this context. Kafka client libraries typically handle broker availability internally and try to connect to other brokers in the cluster if one is not available.InvalidPartitionsException: This exception is not a standard Kafka client exception in the context of sending messages. Issues related to partitioning typically manifest in different ways, not through an InvalidPartitionsException during a send operation.Hence, the most relevant exceptions in this scenario are SerializationException and BufferExhaustedException.

**Detailed explanation of each option:**

1. ✅ **A. SerializationException**  
   **Correct**.

2. ❌ **B. BrokerNotAvailableException**  
   **Incorrect**.

3. ❌ **C. InvalidPartitionsException**  
   **Incorrect**.

4. ✅ **D. BufferExhaustedException**  
   **Correct**.

</details>

## Question 35 (Reliable Data Delivery):
If the min.insync.replicas is configured as 2 for a topic with three replicas, and two out of three replicas are unavailable, what is the outcome when a consumer sends a request to the broker?

- A. An empty message will be returned
- B. NotEnoughReplicasException will be returned
- C. A new leader for the partition will be elected
- D. Data will be returned from the remaining in-sync replica

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

`min.insync.replicas` only constrains **writes** (producers with `acks=all`), not **reads**. A consumer always fetches from the partition **leader**, which remains available here, so the read request succeeds and returns the data it has — up to the high watermark. (A producer using `acks=all`, by contrast, would be blocked with `NotEnoughReplicas` because fewer than 2 replicas are in sync.)

**Detailed explanation of each option:**

1. ❌ **A. An empty message will be returned**  
   **Incorrect**. The leader still serves the records it holds; the read is not forced to return empty.

2. ❌ **B. NotEnoughReplicasException will be returned**  
   **Incorrect**. That error applies to producer writes with `acks=all`, not to consumer reads.

3. ❌ **C. A new leader for the partition will be elected**  
   **Incorrect**. The current leader is still available, so no new election is triggered by a read.

4. ✅ **D. Data will be returned from the remaining in-sync replica**  
   **Correct**. Reads are served by the available leader regardless of `min.insync.replicas`.

</details>

## Question 36 (Programming & Serialization):
In Avro, what type of schema evolution is represented by adding an element to an enum without specifying a default value?

- A. backward
- B. breaking
- C. forward
- D. full

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The answer is breaking schema evolution.Here‘s why:Avro Schema EvolutionAvro supports schema evolution, allowing changes to schemas without breaking compatibility with existing data.It defines rules for compatibility between different schema versions.Enum CompatibilityAdding a new element to an enum without a default value is considered a breaking change in Avro.This is because:Forward compatibility: Readers using the new schema can handle data written with the old schema, as they can ignore unknown enum values.Backward compatibility: Readers using the old schema cannot handle data written with the new schema, as they don‘t know how to interpret the new enum value.Default Value ImportanceProviding a default value for the new enum element would make the change backward compatible.Readers using the old schema would use the default value for any unknown enum values, ensuring data can still be read successfully.

**Detailed explanation of each option:**

1. ❌ **A. backward**  
   **Incorrect**.

2. ✅ **B. breaking**  
   **Correct**.

3. ❌ **C. forward**  
   **Incorrect**.

4. ❌ **D. full**  
   **Incorrect**.

</details>

## 🚫 Question 37 (Kafka Ecosystem):
You are dealing with a scenario where events in a Kafka topic have a nested array, and you want to flatten this array in KSQL. What KSQL function should you use for array flattening?

- A. UNNEST
- B. FLATTEN
- C. EXPAND
- D. EXPLODE

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

In KSQL, to flatten a nested array in events from a Kafka topic, you should use the function: EXPLODE Explanation: The EXPLODE function in KSQL is used to flatten nested arrays. It takes an array column as input and produces a new row for each element in the array, effectively “exploding“ the array into multiple rows.

**Detailed explanation of each option:**

1. ❌ **A. UNNEST**  
   **Incorrect**.

2. ❌ **B. FLATTEN**  
   **Incorrect**.

3. ❌ **C. EXPAND**  
   **Incorrect**.

4. ✅ **D. EXPLODE**  
   **Correct**.

</details>

## Question 38 (Kafka Consumers):
In order for consumers to read data from a topic, what configuration settings are required?

- A. the list of brokers that have the data, the topic name and the partitions list
- B. any broker to connect to, and the topic name
- C. all brokers of the cluster, and the topic name
- D. any broker, and the list of topic partitions

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

any broker to connect to, and the topic name. To read data from a Kafka topic, a consumer needs to know:Any broker to connect to: The consumer only needs the address of at least one broker (not necessarily all) to connect to the Kafka cluster. This is often provided as a list of bootstrap servers. Once connected to one broker, the consumer can discover the rest of the cluster.The topic name: The consumer needs to specify the name of the topic from which it wants to read data.Knowing just any broker and the topic name is sufficient because Kafka brokers are aware of the entire cluster‘s metadata, including which broker holds which partitions for a topic. The consumer does not need to know all the brokers in the cluster or the specific partitions of the topic initially. Kafka handles partition assignment and can dynamically balance partitions across consumers in a consumer group.

**Detailed explanation of each option:**

1. ❌ **A. the list of brokers that have the data, the topic name and the partitions list**  
   **Incorrect**.

2. ✅ **B. any broker to connect to, and the topic name**  
   **Correct**.

3. ❌ **C. all brokers of the cluster, and the topic name**  
   **Incorrect**.

4. ❌ **D. any broker, and the list of topic partitions**  
   **Incorrect**.

</details>

## Question 39 (Reliable Data Delivery):
In a Kafka streaming application with Exactly-Once Semantics, what is the role of the acks configuration property in the producer?

- A. It specifies the number of acknowledgments the producer requires
- B. It controls the maximum number of retries for messages
- C. It sets the isolation level for transactions
- D. It defines the producer‘s unique identifier

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

In a Kafka streaming application with Exactly-Once Semantics, the role of the acks configuration property in the producer is: It specifies the number of acknowledgments the producer requires. Explanation: The acks (acknowledgments) configuration property in the Kafka producer determines the number of acknowledgments the producer requires the broker to receive before considering a message as sent. For Exactly-Once Semantics, it is crucial to configure the acks property appropriately to ensure that messages are reliably acknowledged by the broker before the producer considers them sent. The common values for acks are: acks=0: The producer does not wait for any acknowledgment. This mode provides the lowest level of reliability. acks=1: The producer waits for acknowledgment from the leader broker. This provides better reliability than acks=0. acks=all or acks=-1: The producer waits for acknowledgment from all in-sync replicas. This ensures the highest level of reliability but may introduce more latency. By configuring the acks property, you control the trade-off between reliability and latency in message delivery, making it an essential parameter when working with Exactly-Once Semantics or other delivery guarantees.

**Detailed explanation of each option:**

1. ✅ **A. It specifies the number of acknowledgments the producer requires**  
   **Correct**.

2. ❌ **B. It controls the maximum number of retries for messages**  
   **Incorrect**.

3. ❌ **C. It sets the isolation level for transactions**  
   **Incorrect**.

4. ❌ **D. It defines the producer‘s unique identifier**  
   **Incorrect**.

</details>

## Question 40 (Kafka Connect):
A Kafka Connect Sink Connector is writing duplicate records to a target database. What could be a potential reason for this issue?

- A. Incorrect connector.class setting
- B. Missing topics configuration
- C. Incorrect primary key configuration
- D. Incompatible data types

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

A potential reason for a Kafka Connect Sink Connector writing duplicate records to a target database could be: Incorrect primary key configuration Explanation: When using a Kafka Connect Sink Connector to write data to a target database, it‘s essential to configure the connector with the correct primary key settings. The primary key is used to uniquely identify records in the target database. If the primary key is not configured correctly, it may lead to the connector being unable to accurately determine whether a record already exists in the database.

**Detailed explanation of each option:**

1. ❌ **A. Incorrect connector.class setting**  
   **Incorrect**.

2. ❌ **B. Missing topics configuration**  
   **Incorrect**.

3. ✅ **C. Incorrect primary key configuration**  
   **Correct**.

4. ❌ **D. Incompatible data types**  
   **Incorrect**.

</details>

## 🚫 Question 41 (Kafka Connect):
A Kafka Connect worker is encountering classpath issues when loading custom converters. What Kafka tool can you use to troubleshoot and manage the classpath configurations for connectors and converters?

- A. Kafka Manager
- B. Kafka Streams
- C. Confluent Control Center
- D. Kafka Connect REST API

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Classpath/plugin-loading problems in Kafka Connect are diagnosed using the worker's `plugin.path` configuration together with the worker startup logs, and verified through the **Kafka Connect REST API**: the `GET /connector-plugins` endpoint lists the connector, converter, and transformation plugins that the worker has successfully loaded, letting you confirm whether a custom converter is on the classpath. There is no dedicated "classpath inspector" tool in Kafka.

**Detailed explanation of each option:**

1. ❌ **A. Kafka Manager**  
   **Incorrect**. Kafka Manager is a cluster/topic administration and monitoring tool; it does not manage Connect worker classpaths or plugins.

2. ❌ **B. Kafka Streams**  
   **Incorrect**. Kafka Streams is a client library for stream processing, unrelated to Connect plugin loading.

3. ❌ **C. Confluent Control Center**  
   **Incorrect**. Control Center is a monitoring/management UI; it does not expose or troubleshoot a worker's plugin classpath.

4. ✅ **D. Kafka Connect REST API**  
   **Correct**. `GET /connector-plugins` reports which plugins the worker loaded, so you can verify whether a custom converter is correctly on the classpath (combined with `plugin.path` and the worker logs).

</details>

## Question 42 (Kafka Connect):
In the context of using plain JSON data with Connect, when encountering the error message: “org.apache.kafka.connect.errors.DataException: JsonDeserializer with schemas.enable requires ‘schema‘ and ‘payload‘ fields and may not contain additional fields,“ what steps can be taken to resolve this error?

- A. Use Single Message Transforms to add schema and payload fields in the message
- B. Set key.converter, value.converter to AvroConverter and the schema registry url
- C. Set key.converter, value.converter to JsonConverter and the schema registry url
- D. Set key.converter.schemas.enable and value.converter.schemas.enable to false

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Set key.converter.schemas.enable and value.converter.schemas.enable to false.The error message org.apache.kafka.connect.errors.DataException: JsonDeserializer with schemas.enable requires “schema“ and “payload“ fields and may not contain additional fields indicates that the JsonDeserializer is expecting the JSON data to have a specific format with “schema“ and “payload“ fields due to the schemas.enable setting being true.To fix this error for plain JSON data that does not follow this format, you should set both key.converter.schemas.enable and value.converter.schemas.enable to false in your Kafka Connect configuration. This tells Kafka Connect that the JSON data being consumed does not contain separate schema and payload fields, allowing it to process plain JSON data correctly.Use Single Message Transforms to add schema and payload fields in the message: This is an unnecessary complication for handling plain JSON data and doesn‘t directly address the configuration issue.Set key.converter, value.converter to AvroConverter and the schema registry url: This solution is not relevant if you are working with plain JSON data. AvroConverter is used when you are dealing with Avro data formats.Set key.converter, value.converter to JsonConverter and the schema registry url: This configuration is already likely to be in place if you‘re encountering this error. The issue is not with the converter type but with the schemas.enable setting within the JsonConverter.

**Detailed explanation of each option:**

1. ❌ **A. Use Single Message Transforms to add schema and payload fields in the message**  
   **Incorrect**.

2. ❌ **B. Set key.converter, value.converter to AvroConverter and the schema registry url**  
   **Incorrect**.

3. ❌ **C. Set key.converter, value.converter to JsonConverter and the schema registry url**  
   **Incorrect**.

4. ✅ **D. Set key.converter.schemas.enable and value.converter.schemas.enable to false**  
   **Correct**.

</details>

## Question 43 (Kafka Setup and Operations):
In a scenario where a producer application initially functions on one developer‘s machine, but when copied to another developer‘s machine, it successfully connects to Kafka but encounters an authorization problem when attempting to produce to the same Kafka topic, what is the probable cause of this issue?

- A. You cannot copy a producer application from one machine to another
- B. The Kafka ACL does not allow another machine IP
- C. The Kafka Broker needs to be rebooted
- D. Broker configuration needs to be changed to allow a different producer

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The Kafka ACL does not allow another machine IP. In Kafka, access control lists (ACLs) are often used to manage permissions for producing and consuming from topics. If a producer application works on one machine but encounters an authorization issue on another machine, a likely cause is that the Kafka ACLs are set up to restrict access based on the IP address or some other identifying characteristic of the client.Heres why the other options are less likely:You cannot copy a producer application from one machine to another: This is not true. You can copy a producer application across machines. The issue arises from configuration or access control, not the act of copying.The Kafka Broker needs to be rebooted: Kafka brokers typically do not require a reboot for access control changes to take effect. Additionally, if the broker was the issue, it would likely affect all producers, not just the one on the new machine.Broker configuration needs to be changed to allow a different producer: While its possible that broker configuration might play a role, its more likely to be related to ACLs rather than a fundamental broker configuration, especially since the producer works fine on the original machine.To resolve this issue, you would typically check the ACL settings in your Kafka cluster and ensure that the new machines IP address or producer credentials are authorized to produce to the specified topic.

**Detailed explanation of each option:**

1. ❌ **A. You cannot copy a producer application from one machine to another**  
   **Incorrect**.

2. ✅ **B. The Kafka ACL does not allow another machine IP**  
   **Correct**.

3. ❌ **C. The Kafka Broker needs to be rebooted**  
   **Incorrect**.

4. ❌ **D. Broker configuration needs to be changed to allow a different producer**  
   **Incorrect**.

</details>

## Question 44 (Kafka Consumers):
Which Kafka consumer configuration determines the group under which committed offsets are tracked and stored?

- A. group.id
- B. value.deserializer
- C. enable.auto.commit
- D. auto.offset.reset

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Option A. group.id Correct because Kafka stores consumer offsets based on the consumer group. The group.id identifies the consumer group whose offsets are being committed and tracked. Consumers belonging to the same group share partition assignments and maintain offsets for their group in Kafka’s internal offset storage. Incorrect: Option B. value.deserializer Incorrect because value.deserializer specifies how Kafka converts message values from bytes into the required data type. It has no role in committing consumer offsets. Option C. enable.auto.commit Incorrect because enable.auto.commit controls whether offsets are committed automatically. It is a configuration setting, not the mechanism that identifies where the committed offsets belong. Option D. auto.offset.reset Incorrect because auto.offset.reset determines what to do when a consumer has no valid committed offset, such as whether to start from the earliest or latest available record. It does not commit offsets.

**Detailed explanation of each option:**

1. ✅ **A. group.id**  
   **Correct**.

2. ❌ **B. value.deserializer**  
   **Incorrect**.

3. ❌ **C. enable.auto.commit**  
   **Incorrect**.

4. ❌ **D. auto.offset.reset**  
   **Incorrect**.

</details>

## Question 45 (Kafka Connect):
In Kafka, what is the role of the Kafka Connect framework?

- A. Producing messages to Kafka topics.
- B. Consuming messages from Kafka topics.
- C. Integrating external systems with Kafka.
- D. Managing Kafka topic partitions.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Integrating external systems with Kafka. Explanation: The primary role of the Kafka Connect framework is to integrate external systems with Kafka. Kafka Connect is a framework for building and running connectors, which are plugins for moving data between Kafka and other systems. Connectors handle the details of communication with external systems, enabling seamless integration of data between Kafka topics and various data sources or sinks.

**Detailed explanation of each option:**

1. ❌ **A. Producing messages to Kafka topics.**  
   **Incorrect**.

2. ❌ **B. Consuming messages from Kafka topics.**  
   **Incorrect**.

3. ✅ **C. Integrating external systems with Kafka.**  
   **Correct**.

4. ❌ **D. Managing Kafka topic partitions.**  
   **Incorrect**.

</details>

## 🚫 Question 46 (Kafka Connect):
You are configuring a Kafka Connect Source Connector to read data from a MongoDB collection. What configuration setting should you adjust to specify the MongoDB connection string?

- A. connector.class
- B. mongodb.connection.url
- C. topics
- D. key.converter

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

mongodb.connection.url Explanation: The mongodb.connection.url configuration setting is used to specify the connection string for MongoDB. This connection string contains information such as the MongoDB server addresses, authentication details, and other configuration options. Here‘s an example of how to set mongodb.connection.url in the connector configuration: ((mongodb.connection.url=mongodb://username:password@localhost:27017/database)) In this example, the mongodb.connection.url is set to the MongoDB connection string, including the username, password, host, port, and database information.

**Detailed explanation of each option:**

1. ❌ **A. connector.class**  
   **Incorrect**.

2. ✅ **B. mongodb.connection.url**  
   **Correct**.

3. ❌ **C. topics**  
   **Incorrect**.

4. ❌ **D. key.converter**  
   **Incorrect**.

</details>

## Question 47 (Kafka Consumers):
You want to configure a Kafka consumer to start consuming messages from the latest offset when there is no previously committed offset. What should you set auto.offset.reset to?

- A. earliest
- B. latest
- C. none
- D. all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

To configure a Kafka consumer to start consuming messages from the latest offset when there is no previously committed offset, you should set auto.offset.reset to: latest Explanation: The auto.offset.reset configuration in Kafka determines the behavior of the consumer when there is no previously committed offset for a partition or when the committed offset is invalid. latest: This setting causes the consumer to start consuming messages from the latest offset in the partition if there is no previously committed offset. It ensures that the consumer reads only new messages produced after the consumer starts. earliest: This setting makes the consumer start consuming messages from the earliest available offset if there is no previously committed offset. It reads all messages from the beginning of the partition. none: This setting throws an exception if no offset is found for the consumer group, requiring explicit offset initialization. all: This setting is not a valid option for auto.offset.reset. In this case, setting auto.offset.reset to latest is appropriate to begin consuming messages from the latest offset when no committed offset is available.

**Detailed explanation of each option:**

1. ❌ **A. earliest**  
   **Incorrect**.

2. ✅ **B. latest**  
   **Correct**.

3. ❌ **C. none**  
   **Incorrect**.

4. ❌ **D. all**  
   **Incorrect**.

</details>

## Question 48 (Kafka Consumers):
When configuring Kafka consumers, what is the purpose of the “group.id“ setting?

- A. Consumer group identification
- B. Kafka broker identification
- C. Topic identification
- D. Consumer unique identifier

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

When configuring Kafka consumers, the purpose of the “group.id“ setting is: Consumer group identification. Explanation: The “group.id“ setting in Kafka consumers is used to identify the consumer group to which a consumer belongs. Kafka consumers can be organized into consumer groups, and each group processes the messages from one or more topics. The “group.id“ setting helps Kafka track the progress of consumers within a consumer group and ensures that each partition in a topic is consumed by only one consumer within the group.

**Detailed explanation of each option:**

1. ✅ **A. Consumer group identification**  
   **Correct**.

2. ❌ **B. Kafka broker identification**  
   **Incorrect**.

3. ❌ **C. Topic identification**  
   **Incorrect**.

4. ❌ **D. Consumer unique identifier**  
   **Incorrect**.

</details>

## Question 49 (Stream Processing):
Among the following types of joins, which one does not necessitate that the input topics have an identical number of partitions?

- A. KStream-GlobalKTable
- B. KStream-KStream join
- C. KStream-KTable join
- D. KTable-KTable join

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The join operation that does not require input topics to share the same number of partitions is:KStream-GlobalKTable joinKStream-GlobalKTable join: In this type of join, a KStream (stream) is joined with a GlobalKTable (table). The GlobalKTable is a distributed table, but it doesn‘t have partitions like a regular KTable. It‘s replicated across all instances of your application, so it can be efficiently joined with any KStream partition without the need for matching partition counts.KStream-KStream join: In this case, both input KStreams need to have the same number of partitions for the join to work efficiently, as it involves matching partitions between the two streams.KStream-KTable join: In this join, the KTable is treated as a stream with changelog events, and the input KStream and KTable should have matching partition counts for efficient processing.KTable-KTable join: Similar to KStream-KStream joins, both input KTables need to have the same number of partitions for efficient processing.

**Detailed explanation of each option:**

1. ✅ **A. KStream-GlobalKTable**  
   **Correct**.

2. ❌ **B. KStream-KStream join**  
   **Incorrect**.

3. ❌ **C. KStream-KTable join**  
   **Incorrect**.

4. ❌ **D. KTable-KTable join**  
   **Incorrect**.

</details>

## Question 50 (Stream Processing):
You are implementing a Kafka Streams application to enrich records by joining them with additional information from an external source. What Kafka Streams operation should you use for this purpose?

- A. join
- B. flatMap
- C. process
- D. map

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

The Kafka Streams operation that you should use for enriching records by joining them with additional information from an external source is join. Explanation: join: This operation is used to combine records from two or more input streams based on a common key. In the context of enriching records, you would typically join your primary stream with another stream that contains the additional information you want to include. So, the correct answer is join.

**Detailed explanation of each option:**

1. ✅ **A. join**  
   **Correct**.

2. ❌ **B. flatMap**  
   **Incorrect**.

3. ❌ **C. process**  
   **Incorrect**.

4. ❌ **D. map**  
   **Incorrect**.

</details>

## Question 51 (Kafka Producers):
In order to send data to a topic, what does a producer need to furnish to the Kafka client?

- A. all the brokers from the cluster and the topic name
- B. any broker from the cluster and the topic name and the partitions list
- C. any broker from the cluster and the topic name
- D. the list of brokers that have the data, the topic name and the partitions list

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

any broker from the cluster and the topic name.Broker Information: In Kafka, a producer needs to know at least one broker (also known as a Kafka server) to connect to the cluster. This broker acts as an initial contact point. Once the producer is connected, it gets the full list of brokers and other metadata from the initial broker it connected to. It‘s not necessary to provide all brokers in the cluster; just one is sufficient to establish the initial connection.Topic Name: The producer must specify the topic name to which it wants to send messages. The Kafka cluster uses this to route the messages to the correct topic.Partitions List: Specifying the partitions list is not a requirement for the producer. Kafka producers automatically handle the partitioning of messages based on the partitioning strategy (like round-robin or key-based partitioning) if a partition is not explicitly specified in the message. The Kafka client takes care of determining which partition within the topic to send the messages to, often based on a key within the message or other partitioning logic.Therefore, for a producer to send messages to a Kafka topic, it needs to know just any broker from the cluster and the name of the topic. The rest is handled by the Kafka client and the cluster itself.

**Detailed explanation of each option:**

1. ❌ **A. all the brokers from the cluster and the topic name**  
   **Incorrect**.

2. ❌ **B. any broker from the cluster and the topic name and the partitions list**  
   **Incorrect**.

3. ✅ **C. any broker from the cluster and the topic name**  
   **Correct**.

4. ❌ **D. the list of brokers that have the data, the topic name and the partitions list**  
   **Incorrect**.

</details>

## Question 52 (Kafka Setup and Operations):
What protocol do Kafka clients utilize for secure connections to the Confluent REST Proxy?

- A. HTTPS (SSL/TLS)
- B. Kerberos
- C. HTTP
- D. SASL

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka clients use the HTTPS (SSL/TLS) protocol to securely connect to the Confluent REST Proxy.HTTPS (SSL/TLS): HTTPS, which stands for Hypertext Transfer Protocol Secure, is the secure version of HTTP. It uses SSL/TLS to encrypt the data transmitted between clients and the server. In the context of the Confluent REST Proxy, HTTPS is used to secure the communication, ensuring that the data exchanged between Kafka clients and the REST Proxy is encrypted and secure.Kerberos: While Kerberos is a popular authentication protocol used in some Kafka setups, it is not a protocol used for securing the connection to the Confluent REST Proxy. Kerberos is typically used for authenticating clients to the Kafka brokers.HTTP: HTTP is the basic, unsecured version of the protocol used for web communications. While the REST Proxy can technically operate over HTTP, it would not be secure. For secure communication, HTTPS must be used.SASL (Simple Authentication and Security Layer): SASL is a framework for authentication and data security in Internet protocols. It is used within Kafka for authentication but is not the protocol used for securing connections to the Confluent REST Proxy. For encryption and secure data transmission, SSL/TLS (as part of HTTPS) is used.

**Detailed explanation of each option:**

1. ✅ **A. HTTPS (SSL/TLS)**  
   **Correct**.

2. ❌ **B. Kerberos**  
   **Incorrect**.

3. ❌ **C. HTTP**  
   **Incorrect**.

4. ❌ **D. SASL**  
   **Incorrect**.

</details>

## Question 53 (Kafka Internals):
To prioritize topic availability over consistency, what configuration adjustment should you make?

- A. unclean.leader.election.enable
- B. compression.type
- C. min.insync.replicas

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

To prioritize topic availability over consistency in a Kafka cluster, you should consider changing the unclean.leader.election.enable setting.Explanation:unclean.leader.election.enable: This setting determines whether an out-of-sync replica can be elected as the leader. By default, Kafka prioritizes consistency by ensuring that only in-sync replicas (ISRs) can be elected as leaders for a partition. If unclean.leader.election.enable is set to true, Kafka allows out-of-sync replicas to become leaders. This can increase availability (as it reduces the likelihood of a partition becoming unavailable if the current leader fails and no in-sync replicas are available) but at the cost of potentially losing data consistency, as the new leader might not have all the latest messages that were acknowledged to the client.compression.type: This setting deals with how messages are compressed on the broker and doesn‘t directly impact the trade-off between availability and consistency.min.insync.replicas: This setting specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. Lowering this value can improve availability (as it would be easier to complete a write operation), but it primarily impacts the durability and consistency of writes rather than the availability of the topic itself.So, if your manager is looking to favor availability even at the risk of potential data inconsistencies, enabling unclean.leader.election.enable would be the appropriate choice. This setting allows the cluster to maintain high availability by allowing partitions to continue to be writable even when a clean leader is not available.

**Detailed explanation of each option:**

1. ✅ **A. unclean.leader.election.enable**  
   **Correct**.

2. ❌ **B. compression.type**  
   **Incorrect**.

3. ❌ **C. min.insync.replicas**  
   **Incorrect**.

</details>

## Question 54 (Kafka Setup and Operations):
What is the impact of configuring the “broker.rack“ setting in the broker configuration of a Kafka cluster?

- A. Each rack contains all the topics and partitions, effectively making Kafka highly available
- B. Replicas for a partition are spread across different racks
- C. Replicas for a partition are placed in the same rack
- D. You can use the same broker.id as long as they have different broker.rack configuration

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Replicas for a partition are spread across different racks.Explanation: In Kafka, when the broker.rack configuration is provided, it enables the rack awareness feature. The main objective of this feature is to ensure that replicas of a partition are distributed across different racks. This distribution enhances the resilience of the Kafka cluster by protecting it against failures that might affect an entire rack, such as power outages or network issues. By spreading replicas across racks, Kafka ensures that even if one rack fails, other racks can continue to serve the data, thereby maintaining high availability and fault tolerance. The broker.rack setting informs the Kafka cluster about the physical location (rack or datacenter) of each broker, which is then used to optimize the placement of partition replicas.

**Detailed explanation of each option:**

1. ❌ **A. Each rack contains all the topics and partitions, effectively making Kafka highly available**  
   **Incorrect**.

2. ✅ **B. Replicas for a partition are spread across different racks**  
   **Correct**.

3. ❌ **C. Replicas for a partition are placed in the same rack**  
   **Incorrect**.

4. ❌ **D. You can use the same broker.id as long as they have different broker.rack configuration**  
   **Incorrect**.

</details>

## Question 55 (Kafka Consumers):
If a consumer begins with auto.offset.reset=none, and the topic partition contains data spanning from offsets 45 to 2311, while the consumer group has previously committed offset 10 for the same topic, from which offset will the consumer commence reading?

- A. offset 10
- B. offset 2311
- C. it will crash
- D. offset 45

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

it will crash.Explanation: When a Kafka consumer starts with auto.offset.reset=none, it means the consumer will not reset its offset if its current offset is not valid or if it‘s starting for the first time. In this scenario, since the consumer group has committed offset 10 previously, the consumer will attempt to start reading from offset 10. However, since the available data in the topic partition starts from offset 45 (as mentioned), offset 10 is no longer valid.Given that the consumer‘s starting offset (10) is not within the range of available offsets (45 to 2311) and auto.offset.reset=none, the consumer will encounter an OffsetOutOfRangeException and typically crash or throw an exception. This setting (auto.offset.reset=none) tells the consumer to either find a valid offset or fail, and in this case, it fails because a valid offset is not found.To handle this situation, the auto.offset.reset policy should be set to a value like earliest (to start from the earliest available offset) or latest (to start from the latest offset), depending on the desired behavior.

**Detailed explanation of each option:**

1. ❌ **A. offset 10**  
   **Incorrect**.

2. ❌ **B. offset 2311**  
   **Incorrect**.

3. ✅ **C. it will crash**  
   **Correct**.

4. ❌ **D. offset 45**  
   **Incorrect**.

</details>

## Question 56 (Kafka Core Concepts):
Which of the following statements are true regarding the number of partitions of a topic?

- A. We can add partitions in a topic by adding a broker to the cluster
- B. We can remove partitions in a topic by removing a broker
- C. We can add partitions in a topic using the kafka-topics.sh command
- D. We can remove partitions in a topic using the kafka-topics.sh command
- E. The number of partitions in a topic cannot be altered

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

We can add partitions in a topic using the kafka-topics.sh commandFalse statements:We can add partitions in a topic by adding a broker to the clusterWe can remove partitions in a topic by removing a brokerWe can remove partitions in a topic using the kafka-topics.sh commandThe number of partitions in a topic cannot be altered1. Adding Partitions with kafka-topics.sh: Kafka allows you to increase the number of partitions of a topic using the kafka-topics.sh script with the –alter option. This is often done to accommodate increased load or to improve parallelism.2. Adding a Broker Does Not Add Partitions: Adding a new broker to a Kafka cluster doesn‘t automatically increase the number of partitions in a topic. Partitions can be redistributed to include the new broker for load balancing, but their count remains the same unless explicitly increased.3. Removing Partitions Is Not Supported: Kafka does not support reducing the number of partitions of a topic. This means you cannot remove partitions either by removing a broker or using the kafka-topics.sh command. Once created, the number of partitions can only be increased, not decreased.4. Partitions Can Be Altered: The statement that the number of partitions in a topic cannot be altered is false, as you can increase (but not decrease) the number of partitions.

**Detailed explanation of each option:**

1. ❌ **A. We can add partitions in a topic by adding a broker to the cluster**  
   **Incorrect**.

2. ❌ **B. We can remove partitions in a topic by removing a broker**  
   **Incorrect**.

3. ✅ **C. We can add partitions in a topic using the kafka-topics.sh command**  
   **Correct**.

4. ❌ **D. We can remove partitions in a topic using the kafka-topics.sh command**  
   **Incorrect**.

5. ❌ **E. The number of partitions in a topic cannot be altered**  
   **Incorrect**.

</details>

## Question 57 (Kafka Setup and Operations):
In Kafka, what is the role of the sasl.mechanism configuration setting?

- A. Configuring topic partitions
- B. Specifying the SASL protocol version
- C. Identifying the SASL mechanism for authentication
- D. Controlling producer acknowledgment

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

The role of the “sasl.mechanism“ configuration setting in Kafka is: Identifying the SASL mechanism for authentication. Explanation: The “sasl.mechanism“ configuration setting in Kafka is used to specify the SASL (Simple Authentication and Security Layer) mechanism for authentication. SASL provides a framework for adding authentication support to connection-based protocols, and Kafka uses it to enable secure authentication between clients (producers and consumers) and brokers. The “sasl.mechanism“ setting allows you to choose a specific SASL mechanism, such as PLAIN, GSSAPI, or SCRAM-SHA-256, for authenticating and securing the communication between Kafka clients and brokers. This setting is crucial for configuring the appropriate authentication mechanism based on the security requirements of your Kafka deployment.

**Detailed explanation of each option:**

1. ❌ **A. Configuring topic partitions**  
   **Incorrect**.

2. ❌ **B. Specifying the SASL protocol version**  
   **Incorrect**.

3. ✅ **C. Identifying the SASL mechanism for authentication**  
   **Correct**.

4. ❌ **D. Controlling producer acknowledgment**  
   **Incorrect**.

</details>

## Question 58 (Kafka Consumers):
A Kafka consumer is not processing messages as quickly as expected, leading to lag. What consumer configuration setting might you adjust to improve processing speed?

- A. enable.auto.commit
- B. group.id
- C. auto.offset.reset
- D. max.poll.records

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

To improve the processing speed of a Kafka consumer and reduce lag, you might consider adjusting the max.poll.records configuration setting. Explanation: The max.poll.records configuration in Kafka determines the maximum number of records (messages) the consumer can fetch in a single poll() request. By increasing this value, you allow the consumer to fetch and process more records in each iteration, potentially improving processing speed. The other options: enable.auto.commit: This setting controls whether the consumer‘s offsets are automatically committed. Adjusting it might impact the commit frequency but won‘t directly affect the processing speed. group.id: This is the identifier for the consumer group. Changing it might result in a new consumer group, but it won‘t directly impact the processing speed. auto.offset.reset: This setting determines the behavior when no offset is committed. Adjusting it might affect where the consumer starts reading messages, but it won‘t directly impact processing speed. In the context of improving processing speed and reducing lag, adjusting max.poll.records is a common approach to allow the consumer to process more records in each poll iteration.

**Detailed explanation of each option:**

1. ❌ **A. enable.auto.commit**  
   **Incorrect**.

2. ❌ **B. group.id**  
   **Incorrect**.

3. ❌ **C. auto.offset.reset**  
   **Incorrect**.

4. ✅ **D. max.poll.records**  
   **Correct**.

</details>

## Question 59 (Kafka Consumers):
In a setup where there are 3 producers publishing to a topic containing 5 partitions, and a consumer group of 10 consumers is consuming from the same topic, how many consumers will be in an idle state?

- A. 3
- B. 5
- C. None
- D. 10

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

5In Kafka, each partition can be consumed by only one consumer from a consumer group at a time. This is a fundamental part of Kafka‘s consumer group protocol, which ensures that each message is delivered to one consumer in the group, and thus each partition is processed by only one consumer in the group.Given that there are 5 partitions in the topic and 10 consumers in the same consumer group, only 5 of these consumers can be actively consuming from the topic (one consumer per partition). The other 5 consumers will remain idle because there are no more partitions left to be assigned to them.The number of producers does not directly affect this partition-consumer assignment logic in Kafka consumer groups.

**Detailed explanation of each option:**

1. ❌ **A. 3**  
   **Incorrect**.

2. ✅ **B. 5**  
   **Correct**.

3. ❌ **C. None**  
   **Incorrect**.

4. ❌ **D. 10**  
   **Incorrect**.

</details>

## Question 60 (Kafka Ecosystem):
In a scenario where Confluent REST Proxy is used for producing messages, and you want to restrict the maximum size of messages that can be sent. What configuration setting should you adjust to specify the maximum message size?

- A. max.message.bytes
- B. max.request.size
- C. max.record.bytes
- D. max.body.bytes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

For Confluent REST Proxy, the correct configuration setting to adjust for specifying the maximum message size is: max.request.size This setting determines the maximum size of a request, including all messages within the request. Therefore, adjusting max.request.size will effectively limit the size of messages that can be sent through the REST Proxy.

**Detailed explanation of each option:**

1. ❌ **A. max.message.bytes**  
   **Incorrect**.

2. ✅ **B. max.request.size**  
   **Correct**.

3. ❌ **C. max.record.bytes**  
   **Incorrect**.

4. ❌ **D. max.body.bytes**  
   **Incorrect**.

</details>
