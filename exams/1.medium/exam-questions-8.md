
## Question 1 (Kafka Connect):
What isn‘t an internal Kafka Connect topic?

- A. connect-configs
- B. connect-jars
- C. connect-status
- D. connect-offsets

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

connect-configs stores configurations, connect-status helps to elect leaders for connect, and connect-offsets store source offsets for source connectors

**Detailed explanation of each option:**

1. ❌ **A. connect-configs**  
   **Incorrect**.

2. ✅ **B. connect-jars**  
   **Correct**.

3. ❌ **C. connect-status**  
   **Incorrect**.

4. ❌ **D. connect-offsets**  
   **Incorrect**.

</details>

## Question 2 (Reliable Data Delivery):
A topic has three replicas and you set `min.insync.replicas` to 2. If two out of three replicas are not available, what happens when a produce request with acks=all is sent to broker?

- A. Produce request is honored with single in-sync replica
- B. Produce request will block till one of the two unavailable partition is available again.
- C. NotEnoughReplicasException will be returned

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

With this configuration, a single in-sync replica becomes read-only. Produce request will receive NotEnoughReplicasException.

**Detailed explanation of each option:**

1. ❌ **A. Produce request is honored with single in-sync replica**  
   **Incorrect**.

2. ❌ **B. Produce request will block till one of the two unavailable partition is available again.**  
   **Incorrect**.

3. ✅ **C. NotEnoughReplicasException will be returned**  
   **Correct**.

</details>

## Question 3 (Kafka Consumers):
How does a consumer commit offsets in Kafka?

- A. It directly sends a message to the `__consumer_offsets` topic
- B. It interacts with the Group Coordinator broker
- C. It directly commits the offsets in Zookeeper

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Consumers do not directly write to the __consumer_offsets topic, they instead interact with a broker that has been elected to manage that topic, which is the Group Coordinator broker

**Detailed explanation of each option:**

1. ❌ **A. It directly sends a message to the __consumer_offsets topic**  
   **Incorrect**.

2. ✅ **B. It interacts with the Group Coordinator broker**  
   **Correct**.

3. ❌ **C. It directly commits the offsets in Zookeeper**  
   **Incorrect**.

</details>

## Question 4 (Kafka Producers):
Which of the following setting increases the chance of batching for a Kafka Producer?

- A. Increase `batch.size`
- B. Increase the number of producer threads
- C. Increase `message.max.bytes`
- D. Increase `linger.ms`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Increase batch.size**  
   **Incorrect**.

2. ❌ **B. Increase the number of producer threads**  
   **Incorrect**.

3. ❌ **C. Increase message.max.bytes**  
   **Incorrect**.

4. ✅ **D. Increase linger.ms**  
   **Correct**.

</details>

## Question 5 (Kafka Consumers):
A topic receives all the orders for the products that are available on a commerce site. Two applications want to process all the messages independently – order fulfilment and monitoring. The topic has 4 partitions, how would you organise the consumers for optimal performance and resource usage?

- A. Create 8 consumers in the same group with 4 consumers for each application
- B. Create two consumer groups for two applications with 4 consumers in each
- C. Create four consumers in the same group, one for each partition - two for fulfilment and two for monitoring
- D. Create two consumers groups for two applications with 8 consumers in each

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

two partitions groups – one for each application so that all messages are delivered to both the application. 4 consumers in each as there are 4 partitions of the topic, and you cannot have more consumers per groups than the number of partitions (otherwise they will be inactive and wasting resources) two partitions groups – one for each application so that all messages are delivered to both the application. 4 consumers in each as there are 4 partitions of the topic, and you cannot have more consumers per groups than the number of partitions (otherwise they will be inactive and wasting resources)

**Detailed explanation of each option:**

1. ❌ **A. Create 8 consumers in the same group with 4 consumers for each application**  
   **Incorrect**.

2. ✅ **B. Create two consumer groups for two applications with 4 consumers in each**  
   **Correct**.

3. ❌ **C. Create four consumers in the same group, one for each partition - two for fulfilment and two for monitoring**  
   **Incorrect**.

4. ❌ **D. Create two consumers groups for two applications with 8 consumers in each**  
   **Incorrect**.

</details>

## Question 6 (Kafka Producers):
What is the risk of increasing `max.in.flight.requests.per.connection` while also enabling retries in a producer?

- A. Message order not preserved
- B. At least once delivery is not guaranteed
- C. Reduce throughput
- D. Less resilient

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. Message order not preserved**  
   **Correct**.

2. ❌ **B. At least once delivery is not guaranteed**  
   **Incorrect**.

3. ❌ **C. Reduce throughput**  
   **Incorrect**.

4. ❌ **D. Less resilient**  
   **Incorrect**.

</details>

## Question 7 (Kafka Internals):
If a topic has a replication factor of 3…

- A. Each partition will live on 4 different brokers
- B. 3 replicas of the same data will live on 1 broker
- C. Each partition will live on 3 different brokers
- D. Each partition will live on 2 different brokers

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Replicas are spread across available brokers, and each replica = one broker. RF 3 = 3 brokers

**Detailed explanation of each option:**

1. ❌ **A. Each partition will live on 4 different brokers**  
   **Incorrect**.

2. ❌ **B. 3 replicas of the same data will live on 1 broker**  
   **Incorrect**.

3. ✅ **C. Each partition will live on 3 different brokers**  
   **Correct**.

4. ❌ **D. Each partition will live on 2 different brokers**  
   **Incorrect**.

</details>

## Question 8 (Stream Processing):
You are running a Kafka Streams application in a Docker container managed by Kubernetes, and upon application restart, it takes a long time for the docker container to replicate the state and get back to processing the data. How can you improve dramatically the application restart?

- A. Increase the number of partitions in your inputs topic
- B. Reduce the Streams caching property
- C. Increase the number of Streams threads
- D. Mount a persistent volume for your RocksDB

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Although any Kafka Streams application is stateless as the state is stored in Kafka, it can take a while and lots of resources to recover the state from Kafka. In order to speed up recovery, it is advised to store the Kafka Streams state on a persistent volume, so that only the missing part of the state needs to be recovered.

**Detailed explanation of each option:**

1. ❌ **A. Increase the number of partitions in your inputs topic**  
   **Incorrect**.

2. ❌ **B. Reduce the Streams caching property**  
   **Incorrect**.

3. ❌ **C. Increase the number of Streams threads**  
   **Incorrect**.

4. ✅ **D. Mount a persistent volume for your RocksDB**  
   **Correct**.

</details>

## Question 9 (Kafka Connect):
You are using a JDBC source connector to copy data from 2 tables to two Kafka topics. There is one connector created with `max.tasks = 2` deployed on a cluster of 3 workers. How many tasks are launched?

- A. 1
- B. 6
- C. 3
- D. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. 1**  
   **Incorrect**.

2. ❌ **B. 6**  
   **Incorrect**.

3. ❌ **C. 3**  
   **Incorrect**.

4. ✅ **D. 2**  
   **Correct**.

</details>

## Question 10 (Kafka Setup and Operations):
How do you create a topic named test with 3 partitions and 3 replicas using the Kafka CLI?

- A. bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3 --topic test
- B. bin/kafka-topics.sh --create --broker-list localhost:9092 --replication-factor 3 --partitions 3 --topic test
- C. bin/kafka-topics-create.sh --zookeeper localhost:9092 --replication-factor 3 --partitions 3 --topic test
- D. bin/kafka-topics.sh --create --bootstrap-server localhost:2181 --replication-factor 3 --partitions 3 --topic test

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

As of Kafka 2.3, the kafka-topics.sh command can take –bootstrap-server localhost:9092 as an argument. You could also use the (now deprecated) option of –zookeeper localhost:2181.

**Detailed explanation of each option:**

1. ✅ **A. bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3 --topic test**  
   **Correct**.

2. ❌ **B. bin/kafka-topics.sh --create --broker-list localhost:9092 --replication-factor 3 --partitions 3 --topic test**  
   **Incorrect**.

3. ❌ **C. bin/kafka-topics-create.sh --zookeeper localhost:9092 --replication-factor 3 --partitions 3 --topic test**  
   **Incorrect**.

4. ❌ **D. bin/kafka-topics.sh --create --bootstrap-server localhost:2181 --replication-factor 3 --partitions 3 --topic test**  
   **Incorrect**.

</details>

## Question 11 (Kafka Setup and Operations):
There are 3 brokers in the cluster. You want to create a topic with a single partition that is resilient to one broker failure and one broker maintenance. What is the replication factor will you specify while creating the topic?

- A. 2
- B. 1
- C. 3
- D. 6

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

1 is not possible as it doesn‘t provide resilience to failure, 2 is not enough as if we take a broker down for maintenance, we cannot tolerate a broker failure, and 6 is impossible as we only have 3 brokers (RF cannot be greater than the number of brokers). Here the correct answer is 3

**Detailed explanation of each option:**

1. ❌ **A. 2**  
   **Incorrect**.

2. ❌ **B. 1**  
   **Incorrect**.

3. ✅ **C. 3**  
   **Correct**.

4. ❌ **D. 6**  
   **Incorrect**.

</details>

## Question 12 (Kafka Consumers):
To allow consumers in a group to resume at the previously committed offset, I need to set the proper value for…

- A. `auto.offset.resets`
- B. `enable.auto.commit`
- C. `value.deserializer`
- D. `group.id`

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Setting a group.id that‘s consistent across restarts will allow your consumers part of the same group to resume reading from where offsets were last committed for that group

**Detailed explanation of each option:**

1. ❌ **A. auto.offset.resets**  
   **Incorrect**.

2. ❌ **B. enable.auto.commit**  
   **Incorrect**.

3. ❌ **C. value.deserializer**  
   **Incorrect**.

4. ✅ **D. group.id**  
   **Correct**.

</details>

## Question 13 (Kafka Consumers):
You are building a consumer application that processes events from a Kafka topic. What is the most important metric to monitor to ensure real-time processing?

- A. UnderReplicatedPartitions
- B. BytesInPerSec
- C. MessagesInPerSec
- D. records-lag-max

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

This metric shows the current lag (number of messages behind the broker)

**Detailed explanation of each option:**

1. ❌ **A. UnderReplicatedPartitions**  
   **Incorrect**.

2. ❌ **B. BytesInPerSec**  
   **Incorrect**.

3. ❌ **C. MessagesInPerSec**  
   **Incorrect**.

4. ✅ **D. records-lag-max**  
   **Correct**.

</details>

## Question 14 (Programming & Serialization):
In Avro, removing a field that does not have a default is a __ schema evolution

- A. backward
- B. breaking
- C. full
- D. forward

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. backward**  
   **Incorrect**.

2. ✅ **B. breaking**  
   **Correct**.

3. ❌ **C. full**  
   **Incorrect**.

4. ❌ **D. forward**  
   **Incorrect**.

</details>

## Question 15 (Reliable Data Delivery):
If I want to have an extremely high confidence that leaders and replicas have my data, I should use

- A. acks=all, replication factor=2, min.insync.replicas=1
- B. acks=all, replication factor=3, min.insync.replicas=1
- C. acks=1, replication factor=3, min.insync.replicas=2
- D. acks=all, replication factor=3, min.insync.replicas=2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

acks=all means the leader will wait for all in-sync replicas to acknowledge the record. Also the min in-sync replica setting specifies the minimum number of replicas that need to be in-sync for the partition to remain available for writes.

**Detailed explanation of each option:**

1. ❌ **A. acks=all, replication factor=2, min.insync.replicas=1**  
   **Incorrect**.

2. ❌ **B. acks=all, replication factor=3, min.insync.replicas=1**  
   **Incorrect**.

3. ❌ **C. acks=1, replication factor=3, min.insync.replicas=2**  
   **Incorrect**.

4. ✅ **D. acks=all, replication factor=3, min.insync.replicas=2**  
   **Correct**.

</details>

## Question 16 (Stream Processing):
A Snowflake account can be hosted on any of the following cloud platforms: Amazon Web Services (AWS) Google Cloud Platform (GCP), and Microsoft Azure (Azure) You want to perform table lookups against a KTable everytime a new record is received from the KStream. What is the output of KStream-KTable join? You choose between KStream or KTable

- A. KTable
- B. Kstream
- C. GlobalKTable

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. KTable**  
   **Incorrect**.

2. ✅ **B. Kstream**  
   **Correct**.

3. ❌ **C. GlobalKTable**  
   **Incorrect**.

</details>

## Question 17 (Kafka Consumers):
Which actions will trigger partition rebalance for a consumer group?

- A. Add a broker to the cluster
- B. Increase partitions of a topic
- C. Add a new consumer to consumer group
- D. Remove a broker from the cluster
- E. A consumer in a consumer group shuts down

Choose the correct answers (select 3).

<details>
<summary>Response:</summary>

**Answer:** B, C, E

**Explanation:**

Rebalance occurs when a new consumer is added, removed or consumer dies or paritions increased.

**Detailed explanation of each option:**

1. ❌ **A. Add a broker to the cluster**  
   **Incorrect**.

2. ✅ **B. Increase partitions of a topic**  
   **Correct**.

3. ✅ **C. Add a new consumer to consumer group**  
   **Correct**.

4. ❌ **D. Remove a broker from the cluster**  
   **Incorrect**.

5. ✅ **E. A consumer in a consumer group shuts down**  
   **Correct**.

</details>

## Question 18 (Kafka Core Concepts):
Once sent to a topic, a message can be modified

- A. Yes
- B. No

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka logs are append-only and the data is immutable

**Detailed explanation of each option:**

1. ❌ **A. Yes**  
   **Incorrect**.

2. ✅ **B. No**  
   **Correct**.

</details>

## Question 19 (Kafka Consumers):
Select all the way for one consumer to subscribe simultaneously to the following topics – topic.history, topic.sports, topic.politics? (select two)

- A. ```consumer.subscribe(Arrays.asList(“topic.history“, “topic.sports“, “topic.politics“));```
- B. ```consumer.subscribe(Pattern.compile(“topic\..*“));```
- C. ```consumer.subscribe(“topic.history“); consumer.subscribe(“topic.sports“); consumer.subscribe(“topic.politics“);```
- D. ```consumer.subscribePrefix(“topic.“);```

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** A, B

**Explanation:**

Multiple topics can be passed as a list or regex pattern.

**Detailed explanation of each option:**

1. ✅ **A. consumer.subscribe(Arrays.asList(“topic.history“, “topic.sports“, “topic.politics“));**  
   **Correct**.

2. ✅ **B. consumer.subscribe(Pattern.compile(“topic\..*“));**  
   **Correct**.

3. ❌ **C. consumer.subscribe(“topic.history“); consumer.subscribe(“topic.sports“); consumer.subscribe(“topic.politics“);**  
   **Incorrect**.

4. ❌ **D. consumer.subscribePrefix(“topic.“);**  
   **Incorrect**.

</details>

## Question 20 (Reliable Data Delivery):
A bank uses a Kafka cluster for credit card payments. What should be the value of the property `unclean.leader.election.enable`?

- A. TRUE
- B. FALSE

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Setting unclean.leader.election.enable to true means we allow out-of-sync replicas to become leaders, we will lose messages when this occurs, effectively losing credit card payments and making our customers very angry.

**Detailed explanation of each option:**

1. ❌ **A. TRUE**  
   **Incorrect**.

2. ✅ **B. FALSE**  
   **Correct**.

</details>

## Question 21 (Kafka Setup and Operations):
If I produce to a topic that does not exist, and the broker setting `auto.create.topic.enable=true`, what will happen?

- A. Kafka will automatically create the topic with 1 partition and 1 replication factor
- B. Kafka will automatically create the topic with the indicated producer settings num.partitions and default.replication.factor
- C. Kafka will automatically create the topic with num.partitions=#of brokers and replication.factor=3
- D. Kafka will automatically create the topic with the broker settings num.partitions and default.replication.factor

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Kafka will automatically create the topic with 1 partition and 1 replication factor**  
   **Incorrect**.

2. ❌ **B. Kafka will automatically create the topic with the indicated producer settings num.partitions and default.replication.factor**  
   **Incorrect**.

3. ❌ **C. Kafka will automatically create the topic with num.partitions=#of brokers and replication.factor=3**  
   **Incorrect**.

4. ✅ **D. Kafka will automatically create the topic with the broker settings num.partitions and default.replication.factor**  
   **Correct**.

</details>

## Question 22 (Kafka Core Concepts):
A customer has many consumer applications that process messages from a Kafka topic. Each consumer application can only process 50 MB/s. Your customer wants to achieve a target throughput of 1 GB/s. What is the minimum number of partitions will you suggest to the customer for that particular topic?

- A. 10
- B. 50
- C. 20
- D. 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

each consumer can process only 50 MB/s, so we need at least 20 consumers consuming one partition so that 50 * 20 = 1000 MB target is achieved.

**Detailed explanation of each option:**

1. ❌ **A. 10**  
   **Incorrect**.

2. ❌ **B. 50**  
   **Incorrect**.

3. ✅ **C. 20**  
   **Correct**.

4. ❌ **D. 1**  
   **Incorrect**.

</details>

## Question 23 (Programming & Serialization):
Which is an optional field in an Avro record?

- A. namespace
- B. name
- C. fields
- D. doc

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. namespace**  
   **Incorrect**.

2. ❌ **B. name**  
   **Incorrect**.

3. ❌ **C. fields**  
   **Incorrect**.

4. ✅ **D. doc**  
   **Correct**.

</details>

## Question 24 (Kafka Internals):
A producer just sent a message to the leader broker for a topic partition. The producer used acks=1 and therefore the data has not yet been replicated to followers. Under which conditions will the consumer see the message?

- A. When the high watermark has advanced
- B. When the message has been fully replicated to all replicas
- C. Right away
- D. Never, the produce request will fail

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Correct:

**Detailed explanation of each option:**

1. ✅ **A. When the high watermark has advanced**  
   **Correct**.

2. ❌ **B. When the message has been fully replicated to all replicas**  
   **Incorrect**.

3. ❌ **C. Right away**  
   **Incorrect**.

4. ❌ **D. Never, the produce request will fail**  
   **Incorrect**.

</details>

## Question 25 (Programming & Serialization):
A consumer application is using KafkaAvroDeserializer to deserialize Avro messages. What happens if message schema is not present in AvroDeserializer local cache?

- A. Fetches schema from Schema Registry
- B. Throws DeserializationException
- C. Throws SerializationException
- D. Fails silently

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

First local cache is checked for the message schema. In case of cache miss, schema is pulled from the schema registry. An exception will be thrown in the Schema Registry does not have the schema (which should never happen if you set it up properly)

**Detailed explanation of each option:**

1. ✅ **A. Fetches schema from Schema Registry**  
   **Correct**.

2. ❌ **B. Throws DeserializationException**  
   **Incorrect**.

3. ❌ **C. Throws SerializationException**  
   **Incorrect**.

4. ❌ **D. Fails silently**  
   **Incorrect**.

</details>

## Question 26 (Kafka Internals):
Your topic is log compacted and you are sending a message with the key K and value null. What will happen?

- A. The producer will throw a Runtime exception
- B. The message will get ignored by the Kafka broker
- C. The broker will delete all messages with the key K upon cleanup
- D. The broker will delete the message with the key K and null value only upon cleanup

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Sending a message with the null value is called a tombstone in Kafka and will ensure the log compacted topic does not contain any messages with the key K upon compaction

**Detailed explanation of each option:**

1. ❌ **A. The producer will throw a Runtime exception**  
   **Incorrect**.

2. ❌ **B. The message will get ignored by the Kafka broker**  
   **Incorrect**.

3. ✅ **C. The broker will delete all messages with the key K upon cleanup**  
   **Correct**.

4. ❌ **D. The broker will delete the message with the key K and null value only upon cleanup**  
   **Incorrect**.

</details>

## Question 27 (Kafka Consumers):
A consumer starts and has `auto.offset.reset=latest`, and the topic partition currently has data for offsets going from 45 to 2311. The consumer group has committed the offset 643 for the topic before. Where will the consumer read from?

- A. it will crash
- B. offset 643
- C. offset 45
- D. offset 2311

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

The offsets are already committed for this consumer group and topic partition, so the property auto.offset.reset is ignored

**Detailed explanation of each option:**

1. ❌ **A. it will crash**  
   **Incorrect**.

2. ✅ **B. offset 643**  
   **Correct**.

3. ❌ **C. offset 45**  
   **Incorrect**.

4. ❌ **D. offset 2311**  
   **Incorrect**.

</details>

## Question 28 (Kafka Consumers):
A consumer wants to read messages from a specific partition of a topic. How can this be achieved?

- A. Call subscribe(String topic, int partition) passing the topic and partition number as the arguments
- B. Call subscribe() passing TopicPartition as the argument
- C. Call assign() passing a Collection of TopicPartitions as the argument

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

assign() can be used for manual assignment of a partition to a consumer, in which case subscribe() must not be used. Assign() takes a collection of TopicPartition object as an argument

**Detailed explanation of each option:**

1. ❌ **A. Call subscribe(String topic, int partition) passing the topic and partition number as the arguments**  
   **Incorrect**.

2. ❌ **B. Call subscribe() passing TopicPartition as the argument**  
   **Incorrect**.

3. ✅ **C. Call assign() passing a Collection of TopicPartitions as the argument**  
   **Correct**.

</details>

## Question 29 (Kafka Connect):
To import data from external databases, I should use

- A. Kafka Connect Source
- B. Kafka Streams
- C. Confluent REST Proxy
- D. Kafka Connect Sink

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka Connect Sink is used to export data from Kafka to external databases and Kafka Connect Source is used to import from external databases into Kafka.

**Detailed explanation of each option:**

1. ✅ **A. Kafka Connect Source**  
   **Correct**.

2. ❌ **B. Kafka Streams**  
   **Incorrect**.

3. ❌ **C. Confluent REST Proxy**  
   **Incorrect**.

4. ❌ **D. Kafka Connect Sink**  
   **Incorrect**.

</details>

## Question 30 (Stream Processing):
Which of the following event processing application is stateless? (select two)

- A. Publish the top 10 stocks each day
- B. Find the minimum and maximum stock prices for each day of trading
- C. Read log messages from a stream and writes ERROR events into a high-priority stream and the rest of the events into a low-priority stream
- D. Read events from a stream and modifies them from JSON to Avro

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** C, D

**Explanation:**

Stateless means processing of each message depends only on the message, so converting from JSON to Avro or filtering a stream are both stateless operations

**Detailed explanation of each option:**

1. ❌ **A. Publish the top 10 stocks each day**  
   **Incorrect**.

2. ❌ **B. Find the minimum and maximum stock prices for each day of trading**  
   **Incorrect**.

3. ✅ **C. Read log messages from a stream and writes ERROR events into a high-priority stream and the rest of the events into a low-priority stream**  
   **Correct**.

4. ✅ **D. Read events from a stream and modifies them from JSON to Avro**  
   **Correct**.

</details>

## Question 31 (Kafka Consumers):
We would like to be in an at-most once consuming scenario. Which offset commit strategy would you recommend?

- A. Commit the offsets in Kafka, after processing the data
- B. Do not commit any offsets and read from beginning
- C. Commit the offsets on disk, after processing the data
- D. Commit the offsets in Kafka, before processing the data

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Here, we must commit the offsets right after receiving a batch from a call to .poll()

**Detailed explanation of each option:**

1. ❌ **A. Commit the offsets in Kafka, after processing the data**  
   **Incorrect**.

2. ❌ **B. Do not commit any offsets and read from beginning**  
   **Incorrect**.

3. ❌ **C. Commit the offsets on disk, after processing the data**  
   **Incorrect**.

4. ✅ **D. Commit the offsets in Kafka, before processing the data**  
   **Correct**.

</details>

## Question 32 (Reliable Data Delivery):
The exactly once guarantee in the Kafka Streams is for which flow of data?

- A. Kafka => External
- B. Kafka => Kafka
- C. External => Kafka

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Kafka Streams can only guarantee exactly once processing if you have a Kafka to Kafka topology.

**Detailed explanation of each option:**

1. ❌ **A. Kafka => External**  
   **Incorrect**.

2. ✅ **B. Kafka => Kafka**  
   **Correct**.

3. ❌ **C. External => Kafka**  
   **Incorrect**.

</details>

## Question 33 (Programming & Serialization):
What isn‘t a feature of the Confluent schema registry?

- A. Store avro data
- B. Store schemas
- C. Enforce compatibility rules

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Data is stored on brokers.

**Detailed explanation of each option:**

1. ✅ **A. Store avro data**  
   **Correct**.

2. ❌ **B. Store schemas**  
   **Incorrect**.

3. ❌ **C. Enforce compatibility rules**  
   **Incorrect**.

</details>

## Question 34 (Kafka Producers):
Producing with a key allows to…

- A. Add more information to my message
- B. Allow a Kafka Consumer to subscribe to a (topic,key) pair and only receive that data
- C. Influence partitioning of the producer messages
- D. Ensure per-record level security

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

Keys are necessary if you require strong ordering or grouping for messages that share the same key. If you require that messages with the same key are always seen in the correct order, attaching a key to messages will ensure messages with the same key always go to the same partition in a topic. Kafka guarantees order within a partition, but not across partitions in a topic, so alternatively not providing a key – which will result in round-robin distribution across partitions – will not maintain such order.

**Detailed explanation of each option:**

1. ❌ **A. Add more information to my message**  
   **Incorrect**.

2. ❌ **B. Allow a Kafka Consumer to subscribe to a (topic,key) pair and only receive that data**  
   **Incorrect**.

3. ✅ **C. Influence partitioning of the producer messages**  
   **Correct**.

4. ❌ **D. Ensure per-record level security**  
   **Incorrect**.

</details>

## Question 35 (Programming & Serialization):
What client protocol is supported for the schema registry? (select two)

- A. SASL
- B. HTTPS
- C. HTTP
- D. Websocket
- E. JDBC

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, C

**Explanation:**

clients can interact with the schema registry using the HTTP or HTTPS interface

**Detailed explanation of each option:**

1. ❌ **A. SASL**  
   **Incorrect**.

2. ✅ **B. HTTPS**  
   **Correct**.

3. ✅ **C. HTTP**  
   **Correct**.

4. ❌ **D. Websocket**  
   **Incorrect**.

5. ❌ **E. JDBC**  
   **Incorrect**.

</details>

## Question 36 (Kafka Internals):
There are 3 producers writing to a topic with 5 partitions. There are 5 consumers consuming from the topic. How many Controllers will be present in the cluster?

- A. 5
- B. 2
- C. 3
- D. 1

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

There is only one controller in a cluster at all times.

**Detailed explanation of each option:**

1. ❌ **A. 5**  
   **Incorrect**.

2. ❌ **B. 2**  
   **Incorrect**.

3. ❌ **C. 3**  
   **Incorrect**.

4. ✅ **D. 1**  
   **Correct**.

</details>

## Question 37 (Kafka Internals):
You have a Kafka cluster and all the topics have a replication factor of 3. One intern at your company stopped a broker, and accidentally deleted all the data of that broker on the disk. What will happen if the broker is restarted?

- A. The broker will start, and won‘t be online until all the data it needs to have is replicated from other leaders
- B. The broker will crash
- C. The broker will start, and other topics will also be deleted as the broker data on the disk got deleted
- D. The broker will start, and won‘t have any data. If the broker comes leader, we have a data loss

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka replication mechanism makes it resilient to the scenarios where the broker lose data on disk, but can recover from replicating from other brokers. This makes Kafka amazing!

**Detailed explanation of each option:**

1. ✅ **A. The broker will start, and won‘t be online until all the data it needs to have is replicated from other leaders**  
   **Correct**.

2. ❌ **B. The broker will crash**  
   **Incorrect**.

3. ❌ **C. The broker will start, and other topics will also be deleted as the broker data on the disk got deleted**  
   **Incorrect**.

4. ❌ **D. The broker will start, and won‘t have any data. If the broker comes leader, we have a data loss**  
   **Incorrect**.

</details>

## Question 38 (Kafka Internals):
A client connects to a broker in the cluster and sends a fetch request for a partition in a topic. It gets an exception NotLeaderForPartitionException in the response. How does client handle this situation?

- A. Send fetch request to each Broker in the cluster
- B. Send metadata request to the same broker for the topic and select the broker hosting the leader replica
- C. Send metadata request to Zookeeper for the topic and select the broker hosting the leader replica
- D. Get the Broker id from Zookeeper that is hosting the leader replica and send request to it

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

In case the consumer has the wrong leader of a partition, it will issue a metadata request. The Metadata request can be handled by any node, so clients know afterwards which broker are the designated leader for the topic partitions. Produce and consume requests can only be sent to the node hosting partition leader.

**Detailed explanation of each option:**

1. ❌ **A. Send fetch request to each Broker in the cluster**  
   **Incorrect**.

2. ✅ **B. Send metadata request to the same broker for the topic and select the broker hosting the leader replica**  
   **Correct**.

3. ❌ **C. Send metadata request to Zookeeper for the topic and select the broker hosting the leader replica**  
   **Incorrect**.

4. ❌ **D. Get the Broker id from Zookeeper that is hosting the leader replica and send request to it**  
   **Incorrect**.

</details>

## Question 39 (Kafka Producers):
To get acknowledgement of writes to only the leader partition, we need to use the config…

- A. acks=1
- B. acks=0
- C. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Producers can set acks=1 to get acknowledgement from partition leader only.

**Detailed explanation of each option:**

1. ✅ **A. acks=1**  
   **Correct**.

2. ❌ **B. acks=0**  
   **Incorrect**.

3. ❌ **C. acks=all**  
   **Incorrect**.

</details>

## Question 40 (Kafka Internals):
Compaction is enabled for a topic in Kafka by setting `log.cleanup.policy=compact`. What is true about log compaction?

- A. After cleanup, only one message per key is retained with the first value
- B. After cleanup, only one message per key is retained with the latest value
- C. Compaction changes the offset of messages
- D. Each message stored in the topic is compressed
- E. Kafka automatically de-duplicates incoming messages based on key hashes

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

Log compaction retains at least the last known value for each record key for a single topic partition. All compacted log offsets remain valid, even if record at offset has been compacted away as a consumer will get the next highest offset.

**Detailed explanation of each option:**

1. ❌ **A. After cleanup, only one message per key is retained with the first value**  
   **Incorrect**.

2. ✅ **B. After cleanup, only one message per key is retained with the latest value**  
   **Correct**.

3. ❌ **C. Compaction changes the offset of messages**  
   **Incorrect**.

4. ❌ **D. Each message stored in the topic is compressed**  
   **Incorrect**.

5. ❌ **E. Kafka automatically de-duplicates incoming messages based on key hashes**  
   **Incorrect**.

</details>

## Question 41 (Kafka Producers):
To enhance compression, I can increase the chances of batching by using

- A. batch.size=65536
- B. max.message.size=10MB
- C. linger.ms=20
- D. acks=all

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

linger.ms forces the producer to wait before sending messages, hence increasing the chance of creating batches that can be heavily compressed.

**Detailed explanation of each option:**

1. ❌ **A. batch.size=65536**  
   **Incorrect**.

2. ❌ **B. max.message.size=10MB**  
   **Incorrect**.

3. ✅ **C. linger.ms=20**  
   **Correct**.

4. ❌ **D. acks=all**  
   **Incorrect**.

</details>

## Question 42 (Kafka Consumers):
There are two consumers C1 and C2 belonging to the same group G subscribed to topics T1 and T2. Each of the topics has 3 partitions. How will the partitions be assigned to consumers with PartitionAssignor being RoundRobinAssignor?

- A. Two consumers cannot read from two topics at the same time
- B. C1 will be assigned partitions 0 and 2 from T1 and partition 1 from T2. C2 will have partition 1 from T1 and partitions 0 and 2 from T2.
- C. All consumers will read from all partitions
- D. C1 will be assigned partitions 0 and 1 from T1 and T2, C2 will be assigned partition 2 from T1 and T2.

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** B

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ❌ **A. Two consumers cannot read from two topics at the same time**  
   **Incorrect**.

2. ✅ **B. C1 will be assigned partitions 0 and 2 from T1 and partition 1 from T2. C2 will have partition 1 from T1 and partitions 0 and 2 from T2.**  
   **Correct**.

3. ❌ **C. All consumers will read from all partitions**  
   **Incorrect**.

4. ❌ **D. C1 will be assigned partitions 0 and 1 from T1 and T2, C2 will be assigned partition 2 from T1 and T2.**  
   **Incorrect**.

</details>

## Question 43 (Kafka Internals):
How do Kafka brokers ensure great performance between the producers and consumers?

- A. It buffers the messages on disk, and sends messages from the disk reads
- B. It does not transform the messages
- C. It transforms the messages into a binary format
- D. It compresses the messages as it writes to the disk
- E. It leverages zero-copy optimisations to send data straight from the page-cache

Choose the correct answers (select 2).

<details>
<summary>Response:</summary>

**Answer:** B, E

**Explanation:**

Kafka transfers data with zero-copy and sends the raw bytes it receives from the producer straight to the consumer, leveraging the RAM available as page cache

**Detailed explanation of each option:**

1. ❌ **A. It buffers the messages on disk, and sends messages from the disk reads**  
   **Incorrect**.

2. ✅ **B. It does not transform the messages**  
   **Correct**.

3. ❌ **C. It transforms the messages into a binary format**  
   **Incorrect**.

4. ❌ **D. It compresses the messages as it writes to the disk**  
   **Incorrect**.

5. ✅ **E. It leverages zero-copy optimisations to send data straight from the page-cache**  
   **Correct**.

</details>

## Question 44 (Kafka Internals):
What‘s a Kafka partition made of?

- A. One file and two indexes per segment
- B. One file and two indexes
- C. One file and one index
- D. One file

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Kafka partitions are made of segments (usually each segment is 1GB), and each segment has two corresponding indexes (offset index and time index)

**Detailed explanation of each option:**

1. ✅ **A. One file and two indexes per segment**  
   **Correct**.

2. ❌ **B. One file and two indexes**  
   **Incorrect**.

3. ❌ **C. One file and one index**  
   **Incorrect**.

4. ❌ **D. One file**  
   **Incorrect**.

</details>

## Question 45 (Programming & Serialization):
When using the Confluent Kafka Distribution, where does the schema registry reside?

- A. As an in-memory plugin on your Zookeeper cluster
- B. As an in-memory plugin on your Kafka Brokers
- C. As an in-memory plugin on your Kafka Connect Workers
- D. As a separate JVM component

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Schema registry is a separate application that provides RESTful interface for storing and retrieving Avro schemas.

**Detailed explanation of each option:**

1. ❌ **A. As an in-memory plugin on your Zookeeper cluster**  
   **Incorrect**.

2. ❌ **B. As an in-memory plugin on your Kafka Brokers**  
   **Incorrect**.

3. ❌ **C. As an in-memory plugin on your Kafka Connect Workers**  
   **Incorrect**.

4. ✅ **D. As a separate JVM component**  
   **Correct**.

</details>

## Question 46 (Kafka Setup and Operations):
Which Kafka CLI should you use to consume from a topic?

- A. kafka-console-consumer
- B. kafka-consumer-groups
- C. kafka-console
- D. kafka-topics

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

Example: kafka-console-consumer –bootstrap-server 127.0.0.1:9092 –topic test –from-beginning

**Detailed explanation of each option:**

1. ✅ **A. kafka-console-consumer**  
   **Correct**.

2. ❌ **B. kafka-consumer-groups**  
   **Incorrect**.

3. ❌ **C. kafka-console**  
   **Incorrect**.

4. ❌ **D. kafka-topics**  
   **Incorrect**.

</details>

## Question 47 (Kafka Consumers):
You are doing complex calculations using a machine learning framework on records fetched from a Kafka topic. It takes more about 6 minutes to process a record batch, and the consumer enters rebalances even though it‘s still running. How can you improve this scenario?

- A. Increase session.timeout.ms to 600000
- B. Add consumers to the consumer group and kill them right away
- C. Increase heartbeat.interval.ms to 600000
- D. Increase max.poll.interval.ms to 600000

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** D

**Explanation:**

Here, we need to change the setting max.poll.interval.ms (default 300000) to its double in order to tell Kafka a consumer should be considered dead if the consumer only if it hasn‘t called the .poll() method in 10 minutes instead of 5.

**Detailed explanation of each option:**

1. ❌ **A. Increase session.timeout.ms to 600000**  
   **Incorrect**.

2. ❌ **B. Add consumers to the consumer group and kill them right away**  
   **Incorrect**.

3. ❌ **C. Increase heartbeat.interval.ms to 600000**  
   **Incorrect**.

4. ✅ **D. Increase max.poll.interval.ms to 600000**  
   **Correct**.

</details>

## Question 48 (Reliable Data Delivery):
A Kafka topic has a replication factor of 3 and a min.insync.replicas setting of 2. How many brokers can go down before a producer with acks=all can’t produce?

- A. 1
- B. 3
- C. 2

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** A

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. 1**  
   **Correct**.

2. ❌ **B. 3**  
   **Incorrect**.

3. ❌ **C. 2**  
   **Incorrect**.

</details>

## Question 49 (Stream Processing):
Which of the following Kafka Streams operators are stateful? (select all that apply)

- A. count
- B. reduce
- C. peek
- D. aggregate
- E. flatmap
- F. joining

Choose the correct answers (select 4).

<details>
<summary>Response:</summary>

**Answer:** A, B, D, F

**Explanation:**

(No explanation provided in source.)

**Detailed explanation of each option:**

1. ✅ **A. count**  
   **Correct**.

2. ✅ **B. reduce**  
   **Correct**.

3. ❌ **C. peek**  
   **Incorrect**.

4. ✅ **D. aggregate**  
   **Correct**.

5. ❌ **E. flatmap**  
   **Incorrect**.

6. ✅ **F. joining**  
   **Correct**.

</details>

## Question 50 (Kafka Internals):
How often is log compaction evaluated?

- A. Every time a new partition is created
- B. Every time a message is sent to Kafka
- C. Every time a segment is closed
- D. Every time a message is flushed to disk

Choose the correct answer.

<details>
<summary>Response:</summary>

**Answer:** C

**Explanation:**

A. Every time a new partition is created (Incorrect) Partition creation is a metadata operation handled by the controller. Compaction is a data-level cleanup process that happens within existing partitions based on their contents, not their creation.

**Detailed explanation of each option:**

1. ❌ **A. Every time a new partition is created**  
   **Incorrect**.

2. ❌ **B. Every time a message is sent to Kafka**  
   **Incorrect**.

3. ✅ **C. Every time a segment is closed**  
   **Correct**.

4. ❌ **D. Every time a message is flushed to disk**  
   **Incorrect**.

</details>
