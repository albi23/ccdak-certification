> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1

What happens when you set `max.in.flight.requests.per.connection` to a value greater than 1 in a Kafka producer?

- A. It increases the throughput of the producer
- B. It increases the latency of the producer
- C. It can lead to out-of-order delivery of messages
- D. It has no effect on the producer's behavior

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Setting `max.in.flight.requests.per.connection` to a value greater than 1 in a Kafka producer allows multiple requests to be sent to the broker in parallel, without waiting for the previous requests to be acknowledged. While this can improve throughput, it also means that if a request fails and needs to be retried, the subsequent requests may have already been processed, leading to out-of-order delivery.

- A is incorrect because while it can improve throughput, it's not the only effect.
- B is incorrect. In fact, it can potentially decrease latency by allowing more requests in flight.

Note: since Kafka 3.0 `enable.idempotence=true` is the default, and with idempotence the broker keeps ordering per partition for up to 5 in-flight requests even with retries. Reordering risk applies when idempotence is disabled (retries with more than 1 in-flight request).
- D is incorrect because it does have a significant effect on the producer's behavior.

</details>

## Question 2

What is the effect of setting `acks=0` in a Kafka producer?

- A. The producer will wait for the broker to acknowledge the message before sending the next one
- B. The producer will wait for the leader and all replicas to acknowledge the message
- C. The producer will not wait for any acknowledgement from the broker
- D. The producer will throw an exception if the broker does not acknowledge the message

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When `acks` is set to 0 in a Kafka producer, the producer will not wait for any acknowledgement from the broker before considering the send operation successful. This means the producer will fire and forget the message, providing no guarantees about whether the broker has received it.

- A and B are incorrect because they describe the behaviors of `acks=1` and `acks=all` respectively.
- D is incorrect because no exception is thrown in this case. The producer simply continues sending messages without waiting for acknowledgement.

</details>

## Question 3

What is the relationship between `request.timeout.ms` and `delivery.timeout.ms` in a Kafka producer?

- A. `request.timeout.ms` should always be greater than `delivery.timeout.ms`
- B. `delivery.timeout.ms` should always be greater than `request.timeout.ms`
- C. They should always be set to the same value
- D. They are independent and can be set to any value

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In a Kafka producer, `request.timeout.ms` configures the maximum amount of time the client will wait for a response from the server when sending a request, while `delivery.timeout.ms` sets an upper bound on the time to report success or failure to the application after a call to `send()`.

If `delivery.timeout.ms` is smaller than `request.timeout.ms`, the client can time out and report a failure to the application before the request timeout even occurs. Therefore, `delivery.timeout.ms` should always be greater than `request.timeout.ms` to allow the full request timeout to elapse before reporting a timeout failure to the application. The producer enforces `delivery.timeout.ms >= linger.ms + request.timeout.ms` (defaults: 120000 ms >= 5 ms + 30000 ms).

- A is incorrect because it's the other way around.
- C is incorrect because they serve different purposes and can have different values.
- D is incorrect because there is a recommended relationship between the two settings.

```
delivery.timeout.ms  > request.timeout.ms

┌─────────────────────────────────────────────────────┐
│              delivery.timeout.ms                    │
│  ┌─────────────────────────────────────────────┐    │
│  │  linger.ms  │  request.timeout.ms  │ retry  │    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘

delivery.timeout.ms covers the ENTIRE lifecycle of a record:
→ Time spent in the buffer (linger.ms)
→ Time to send the request to the broker
→ Time waiting for an ACK (request.timeout.ms)
→ Retry time in case of an error
→ Resend time (linger.ms + request.timeout.ms)

```

</details>

## Question 4

A Kafka producer application needs to send messages to a topic. The messages do not require any particular order. Which of the following properties are mandatory in the producer configuration? (Select three)

- A. `compression.type`
- B. `partitioner.class`
- C. `bootstrap.servers`
- D. `key.serializer`
- E. `value.serializer`
- F. `client.id`

<details>
<summary>Response:</summary> 

**Answer:** C, D, E

**Explanation:**
For the Java Kafka producer to be created, it must know how to connect to the Kafka cluster and how to serialize both keys and values (the constructor throws a `ConfigException` if a serializer is missing, even if you send records with null keys). Therefore, the mandatory properties are:

- `bootstrap.servers`: This specifies the list of Kafka brokers the producer should contact to bootstrap initial cluster metadata.
- `key.serializer`: This specifies the serializer class for message keys.
- `value.serializer`: This specifies the serializer class for message values.

The other options are not strictly mandatory:

- A: `compression.type` is optional. If not set, the producer will send uncompressed messages.
- B: `partitioner.class` is optional. If not set, the default partitioner will be used, which is sufficient for messages that don't require a particular order.
- F: `client.id` is optional. It's used to identify the producer application, but the producer will work without it.

</details>

## Question 5

What is the purpose of setting `compression.type` in a Kafka producer configuration?

- A. To specify the compression algorithm used when sending data to Kafka
- B. To specify the compression algorithm used when storing data on Kafka brokers
- C. To enable or disable compression for the producer
- D. To set the compression level for the producer

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `compression.type` setting in a Kafka producer configuration is used to specify the compression algorithm that the producer will use when sending data to Kafka. The available options are:

- `none`: No compression (default)
- `gzip`: GZIP compression
- `snappy`: Snappy compression
- `lz4`: LZ4 compression
- `zstd`: ZStandard compression

The compression is applied by the producer before sending the data, and the broker will store the compressed data as is. The consumer will decompress the data when it receives it.

- B is incorrect because the producer setting only controls compression on the producer side. The broker (with the default topic/broker `compression.type=producer`) stores the batches as received; the on-disk codec is governed by the broker/topic `compression.type`, not by this producer setting.
- C is incorrect because `compression.type` does not enable/disable compression, it specifies the algorithm. Compression is enabled by default if an algorithm is specified.
- D is incorrect because `compression.type` sets the algorithm, not the compression level. Compression levels have separate settings (`compression.gzip.level`, `compression.lz4.level`, `compression.zstd.level`, available since Kafka 3.8).

</details>

## Question 6

What is the main benefit of enabling compression on the producer side in Kafka?

- A. Reduced producer memory usage
- B. Increased consumer CPU usage
- C. Reduced network bandwidth usage
- D. Increased end-to-end latency

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Enabling compression on the producer side in Kafka can significantly reduce the amount of network bandwidth used when sending data from the producer to the Kafka brokers. The compressed data takes up less space on the wire, thus reducing network I/O.

However, there are trade-offs:

- A is incorrect because compression actually increases memory usage on the producer side, as the data needs to be held in memory during the compression process.
- B is a trade-off, not a benefit: the consumer needs CPU cycles to decompress the data.
- D is a possible trade-off, not a benefit: compression adds some processing time (although smaller batches often reduce overall latency when the network is the bottleneck).

So enabling producer compression is a trade-off between network bandwidth and CPU/memory usage. It's most beneficial when network bandwidth is the bottleneck.

</details>

## Question 7

What is the relationship between `batch.size` and `linger.ms` in the Kafka producer configuration?

- A. They are mutually exclusive settings
- B. `linger.ms` is only relevant if `batch.size` is set to 0
- C. `batch.size` is only relevant if `linger.ms` is set to 0
- D. They work together to control when a batch is considered ready to send

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In the Kafka producer, `batch.size` and `linger.ms` work together to control when a batch of messages is considered ready to send to the broker:

- `batch.size` sets the maximum amount of data that will be included in a single batch.
- `linger.ms` sets the maximum amount of time a batch will wait before being sent to the broker.

A batch will be sent when either `batch.size` is reached or `linger.ms` has passed, whichever comes first.

- A is incorrect because the settings are not mutually exclusive, they work together.
- B and C are incorrect because both settings are always relevant, regardless of the value of the other setting. If `batch.size` is 0, batching is effectively disabled. If `linger.ms` is 0, the producer will not wait at all and will send batches as soon as the sender thread can send them. (The default `linger.ms` is 5 ms since Kafka 4.0; it was 0 before.) `batch.size` is the per-partition batch limit.

Tuning these settings can have a significant impact on producer performance and throughput.

</details>

## Question 8

What is the effect of increasing `batch.size` in a Kafka producer configuration?

- A. It increases the maximum size of each individual message
- B. It increases the maximum number of bytes (memory) the producer uses for a single batch of records for one partition
- C. It increases the maximum time a batch will wait before being sent
- D. It increases the total memory the producer uses for buffering all unsent records

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
`batch.size` is the amount of memory in **bytes** (not number of messages) used for each batch; the producer batches records sent to the same partition. A larger value lets more records fit in one batch, which usually improves throughput and compression at the cost of more memory per batch. Because the producer does not wait for a batch to fill (it sends half-full batches too, governed by `linger.ms`), a larger `batch.size` alone does not add latency.

- A is incorrect: the maximum size of a single record/request is limited by `max.request.size` (and broker `message.max.bytes`).
- C is incorrect: the wait time is controlled by `linger.ms`.
- D is incorrect: the total buffer is `buffer.memory`.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3, p. 59 ("batch.size ... amount of memory in bytes (not messages!) that will be used for each batch"); https://kafka.apache.org/documentation/#producerconfigs_batch.size

</details>

## Question 9

What is the relationship between `linger.ms` and `request.timeout.ms` in the Kafka producer configuration?

- A. They are redundant settings that control the same thing
- B. `linger.ms` should always be set higher than `request.timeout.ms`
- C. `request.timeout.ms` should always be set higher than `linger.ms`
- D. They control independent aspects of the producer behavior

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
`linger.ms` and `request.timeout.ms` both relate to timing, but they control independent aspects of the producer:

- `linger.ms` controls the maximum amount of time a batch will wait before being sent to the broker. A higher value can increase batching and thus throughput, at the cost of some latency.
- `request.timeout.ms` controls the maximum amount of time the producer will wait for a response from the broker before considering the request failed.

The `request.timeout.ms` clock only starts when a request has been sent to the broker, so it does not include the time a batch spends lingering in the accumulator. There is therefore no required ordering between the two settings. The related constraint is on `delivery.timeout.ms`, which must be greater than or equal to `linger.ms + request.timeout.ms` (see Question 3).

- A is incorrect because the settings control different things.
- B and C are incorrect because no ordering between these two settings is required; the linger time is not part of the request timeout.

</details>

## Question 10

What happens if `linger.ms` is set to 0 in the Kafka producer configuration?

- A. The producer will never send any messages
- B. The producer will wait indefinitely for each batch to fill up before sending
- C. The producer will send each message as soon as it is received, without batching
- D. The producer will use the default linger time

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Setting `linger.ms` to 0 in the Kafka producer configuration means that the producer will not wait at all before sending a batch of messages. In effect, the producer sends as soon as the sender thread is free, without deliberately waiting for more records (records that arrive while a request is already in flight can still end up in the same batch).

This can be useful in scenarios where minimizing latency is more important than maximizing throughput. With `linger.ms=0`, each message is sent immediately, minimizing the time between when a message is produced and when it is available to be consumed.

However, disabling batching can significantly reduce throughput, as the producer will make many more requests to the broker, each carrying fewer messages. This increases the overhead of the request-response cycle.

In most cases, it's recommended to set `linger.ms` to a small but non-zero value, like 5-100ms, to strike a balance between latency and throughput (the default is 5 ms since Kafka 4.0; before that it was 0).

- A is incorrect because a linger time of 0 does not prevent the producer from sending messages, it just sends them immediately.
- B is incorrect because a linger time of 0 means the producer won't wait at all, not that it will wait indefinitely.
- D is incorrect because 0 is a valid setting for `linger.ms`, not a signal to use the default.

</details>

## Question 11

A producer is configured with `acks=1`. The leader writes the record to its local log and acknowledges it, then crashes before any follower has fetched the record, and a follower becomes the new leader. What is the outcome?

- A. The producer receives an error, because the record was not replicated to all in-sync replicas
- B. The record is lost although the producer already received a successful acknowledgment
- C. The new leader fetches the record from the old leader once it restarts, so nothing is lost
- D. The producer automatically resends the record, because it detects the leader change

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
With `acks=1` the leader responds as soon as it has written the record to its own log, without waiting for followers. If the leader fails before replication, the new leader (a follower) does not have the record and, when the old leader rejoins, its unreplicated tail is truncated. The producer already got a success, so it will not retry and the message is lost. To avoid this use `acks=all` together with `min.insync.replicas` >= 2.

- A is incorrect: the ack was already returned before the failure.
- C is incorrect: the old leader's uncommitted records are truncated when it becomes a follower.
- D is incorrect: retries only happen when the request fails or times out, which did not happen here.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3 ("acks" section, p. 55-56); https://kafka.apache.org/documentation/#producerconfigs_acks

</details>

## Question 12

How does the `min.insync.replicas` broker configuration interact with the `acks` producer configuration?

- A. They are completely independent settings
- B. `min.insync.replicas` is enforced for every value of `acks`
- C. `min.insync.replicas` is only relevant if `acks` is set to `1` or `all`
- D. If `acks` is set to `all`, writes will only succeed if the number of in-sync replicas is at least `min.insync.replicas`

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
The `min.insync.replicas` broker configuration and the `acks` producer configuration work together to control the durability of writes in Kafka:

- `min.insync.replicas` specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful.
- `acks` specifies the number of acknowledgments the producer requires the leader to have received before considering a request complete.

When `acks` is set to `all`, the leader will wait for the full set of in-sync replicas to acknowledge the write before responding to the producer. However, if the number of in-sync replicas is less than `min.insync.replicas`, the write will fail even if `acks=all`. 

This ensures that a minimum number of replicas have the data, providing a stronger durability guarantee.

- A is incorrect because the settings are not independent, they interact.
- B is incorrect because `min.insync.replicas` is enforced by the broker only for producers using `acks=all`.
- C is incorrect because `min.insync.replicas` is not relevant to `acks=1`, only to `acks=all`.

</details>

## Question 13 [x]

What happens if a Kafka producer sends a message with `acks=all` to a topic partition with 3 replicas, but only 2 replicas are currently in-sync?

- A. The write will succeed and the producer will receive an acknowledgment
- B. The write will succeed but the producer will not receive an acknowledgment
- C. The write will be queued until the third replica comes back in-sync
- D. The write will fail and the producer will receive an error

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In this scenario, the producer is configured with `acks=all`, meaning the leader waits for all replicas currently in the in-sync replica set (ISR) before acknowledging. The ISR contains 2 replicas (the leader and one follower); the replica that is out of sync is not waited for.

The write is rejected only if the ISR size is smaller than `min.insync.replicas`. The question does not change `min.insync.replicas` from its default of 1 (and even a value of 2 would be satisfied), so the write succeeds and the producer receives an acknowledgment. (If `min.insync.replicas=3` were configured, the write would fail with `NotEnoughReplicasException`.)

- B is incorrect because a successful write is always acknowledged.
- C is incorrect because the broker never queues a write waiting for an out-of-sync replica to catch up.
- D is incorrect because the failure only happens when ISR size < `min.insync.replicas`.

</details>

## Question 14 [x]

Can a producer configured with `acks=all` and `retries=Integer.MAX_VALUE` ever lose data that was already acknowledged to it?

- A. No, this configuration guarantees no data loss under all circumstances
- B. Yes, if the number of in-sync replicas for a partition drops below `min.insync.replicas`
- C. Yes, if `unclean.leader.election.enable=true` and all in-sync replicas fail
- D. Yes, if the producer crashes after the broker acknowledges the write but before the producer records the acknowledgment

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
A producer configured with `acks=all` and `retries=Integer.MAX_VALUE` provides a very strong durability guarantee, but acknowledged data can still be lost in some broker-side edge cases:

(Only C loses already acknowledged data; B and D are explained below.)

1. (Option B, not acknowledged data loss) If the ISR size drops below `min.insync.replicas`, the broker rejects writes to that partition with `NotEnoughReplicasException`. The producer retries only until `delivery.timeout.ms` (default 2 minutes, which bounds `retries`) and then reports a failure to the application. The record was never acknowledged, so the application must handle the error; nothing acknowledged is lost.

2. (Option C) If `unclean.leader.election.enable=true` and all in-sync replicas for a partition fail, an out-of-sync replica can be elected as the new leader. This replica may be missing some of the latest messages, causing data loss.

3. (Option D) If the producer crashes or loses connectivity after the broker has committed a write but before the acknowledgment arrives, the record is stored on the broker, so it is not lost. A retry can produce a duplicate (unless idempotence is enabled, which is the default since Kafka 3.0).

So `acks=all` with retries cannot completely eliminate data loss in all failure scenarios.

- A is incorrect because, as explained above, there are edge cases where data loss can still occur even with this configuration.

</details>

## Question 15

You want to produce messages to a Kafka topic using a Java client. Which of the following is NOT a required configuration for the producer?

- A. `bootstrap.servers`
- B. `key.serializer`
- C. `value.serializer`
- D. `partitioner.class`

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
When creating a Kafka producer in Java, there are several required configurations:

- `bootstrap.servers`: This specifies the list of broker addresses the producer should contact to bootstrap initial cluster metadata. It is required for the producer to know where to send requests.
- `key.serializer`: This specifies the serializer class for keys. It is required because Kafka needs to know how to serialize the key object to bytes.
- `value.serializer`: This specifies the serializer class for values. It is required because Kafka needs to know how to serialize the value object to bytes.

The `partitioner.class` configuration is optional. It specifies the partitioner class that should be used to determine which partition to send each message to. If not specified, the default partitioner will be used, which is sufficient for most use cases.

</details>

## Question 16 [x]

Which of the following is true about the relationship between producers and consumers in Kafka?

- A. Producers and consumers must use the same serialization format
- B. Producers and consumers must be written in the same programming language
- C. Producers and consumers are decoupled by the Kafka topic
- D. Producers must know about the consumers to send messages to them

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
One of the key design principles of Kafka is the decoupling of producers and consumers:

- Producers write messages to a Kafka topic, without needing to know about the consumers that will read those messages.
- Consumers read messages from a Kafka topic, without needing to know about the producers that wrote those messages.

This decoupling is achieved through the Kafka topic, which acts as a buffer between producers and consumers. Producers write to the topic and consumers read from the topic, but they don't need to be aware of each other.

This decoupling allows for several benefits:

- Producers and consumers can be scaled independently, as they are not directly dependent on each other.
- Producers and consumers can be written in different programming languages and use different serialization formats, as long as they agree on the data format of the messages in the topic.
- New consumers can be added to read from the topic without affecting the producers.

Therefore, statements A, B, and D are incorrect. Producers and consumers do not need to use the same serialization format, be written in the same language, or know about each other. They are decoupled by the Kafka topic.

</details>

## Question 17

What happens if a Kafka producer sends a message to a topic partition and does not receive an acknowledgment from the broker?

- A. The producer will consider the message as successfully sent
- B. The producer will wait indefinitely for the acknowledgment
- C. The producer will retry sending the message based on its retry configuration
- D. The producer will immediately send the next message in the queue

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When a Kafka producer sends a message, it waits for an acknowledgment from the broker before considering the send operation complete. If the acknowledgment is not received within the configured `request.timeout.ms`, the send operation is considered failed.

In case of a failure, the producer's behavior depends on its `retries` configuration:

- If `retries` is set to 0, the producer will not retry the send operation. It will consider the message as failed and will either throw an exception or invoke the callback function with an error, depending on how the send operation was invoked.
- If `retries` is set to a value greater than 0 (the default is 2147483647), the producer will retry sending the message until the retries are exhausted or `delivery.timeout.ms` (default 120000 ms) expires, whichever comes first. It will wait for `retry.backoff.ms` before each retry attempt.

If the producer exhausts all retry attempts without receiving an acknowledgment, it will consider the message as failed.

Therefore, statement C is correct. The producer will retry sending the message based on its retry configuration.

- A is incorrect because the producer will not consider the message as successfully sent until it receives an acknowledgment.
- B is incorrect because the producer will not wait indefinitely. It will timeout after `request.timeout.ms`.
- D is incorrect because the producer will not immediately send the next message. It will attempt to retry the failed message first.

</details>

## Question 18

What is the purpose of the `acks` parameter in Kafka producer configuration?

- A. To specify the number of partitions the producer should write to
- B. To specify the number of replicas that must acknowledge a write for it to be considered successful
- C. To specify the number of times the producer should retry sending a message
- D. To specify the maximum size of a batch of messages

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The `acks` parameter in Kafka producer configuration controls how many partition replicas must receive the record before the producer considers the write successful (the book's wording). It controls the durability and reliability of message writes.

The `acks` parameter can have the following values:

- `0`: The producer does not wait for any acknowledgment from the server. The message is considered sent as soon as it is written to the network. This provides the lowest latency but also the lowest durability guarantee.
- `1`: The leader writes the message to its local log and responds without waiting for acknowledgment from the followers. This provides better durability than `acks=0` but still has the risk of message loss if the leader fails before the followers have replicated the message.
- `all` or `-1`: The leader waits for the full set of in-sync replicas (ISR) to acknowledge the message before responding. Combined with `min.insync.replicas` this gives the highest durability.

- A, C and D describe unrelated settings (partitioner, `retries`/`delivery.timeout.ms`, `batch.size`).

The choice of the `acks` value depends on the specific requirements of your application regarding durability, latency, and throughput.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3, p. 55; https://kafka.apache.org/documentation/#producerconfigs_acks

</details>

## Question 19

What happens if the `acks` parameter is set to `all` and the minimum in-sync replicas (`min.insync.replicas`) setting is not satisfied?

- A. The producer will retry sending the message until the `min.insync.replicas` requirement is met
- B. The producer will write the message successfully, ignoring the `min.insync.replicas` setting
- C. The producer will receive an error indicating that the `min.insync.replicas` requirement is not met
- D. The producer will wait indefinitely until the `min.insync.replicas` requirement is met

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
When the `acks` parameter is set to `all` in the Kafka producer configuration, the producer requires acknowledgment from all in-sync replicas (ISR) before considering a write successful. The `min.insync.replicas` setting specifies the minimum number of replicas that must be in-sync for a partition to accept writes with `acks=all`.

If the `min.insync.replicas` requirement is not met, meaning there are fewer in-sync replicas than the specified minimum, the broker rejects the write with `NotEnoughReplicasException`. This error is retriable, so the producer retries until `delivery.timeout.ms` expires and then reports the error to the application (via the callback/future). The application must then handle the error and decide on the appropriate action, such as retrying the write or logging.

- A is incorrect because retries are bounded by `delivery.timeout.ms`; the producer does not retry until the requirement is met forever.
- D is incorrect for the same reason; the producer does not wait indefinitely.

Setting `min.insync.replicas` to a value greater than 1 in combination with `acks=all` ensures that writes are only considered successful if a minimum number of replicas have acknowledged the message. This provides additional durability guarantees by preventing writes from succeeding if the specified number of replicas is not available.

It's important to note that setting `min.insync.replicas` too high can impact the availability of the system, as writes will fail if the required number of replicas is not available. It's recommended to find a balance between durability and availability based on the specific requirements of your application.

</details>

## Question 20

What is the relationship between the `acks` parameter and the `request.required.acks` parameter in Kafka?

- A. They are the same parameter, just with different names
- B. `acks` is used in the producer configuration, while `request.required.acks` is used in the consumer configuration
- C. `acks` is used in the new producer API, while `request.required.acks` is used in the old producer API
- D. They are completely unrelated parameters

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
The `acks` parameter and the `request.required.acks` parameter in Kafka are related to the acknowledgment mechanism for producer writes, but they are used in different versions of the producer API.

In the new producer API (introduced in Kafka 0.8.2 and later), the `acks` parameter is used to specify the number of acknowledgments the producer requires the leader to have received before considering a write request complete. It is part of the producer configuration.

On the other hand, `request.required.acks` is a parameter used in the old producer API (prior to Kafka 0.8.2). It serves a similar purpose as `acks` but with a slightly different syntax and behavior.

The `request.required.acks` parameter can have the following values:

- `0`: The producer does not wait for any acknowledgment from the server.
- `1`: The leader writes the message to its local log and responds without waiting for acknowledgment from the followers.
- `-1`: The leader waits for the full set of in-sync replicas (ISR) to acknowledge the message before responding to the producer.

In the old producer API, `request.required.acks` is used in the producer configuration to specify the acknowledgment level.

It's important to note that the old producer API and the `request.required.acks` parameter are deprecated and have been replaced by the new producer API and the `acks` parameter. The old Scala producer was removed in Kafka 2.0; use the Java producer and the `acks` parameter.

When migrating from the old producer API to the new producer API, you should replace `request.required.acks` with the equivalent `acks` configuration.

</details>

## Question 21

How does Kafka's zero-copy optimization handle data transformation or modification?

- A. It automatically applies data transformations during the zero-copy process.
- B. It allows custom data transformations to be plugged into the zero-copy mechanism.
- C. It does not support data transformations and sends data as-is.
- D. It performs data transformations after the data is copied into the application's memory.

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
Kafka's zero-copy optimization (the `sendfile` system call used by brokers) is designed to efficiently transfer data from the broker's page cache to the network socket when serving consumers, without any data transformation or modification. (It is not used when TLS encryption is enabled.) When using zero-copy, Kafka sends the data as-is, exactly as it was received from the producer, without applying any transformations.

Here's how Kafka handles data transformation with zero-copy:

1. Producer-side serialization:
   - Before sending data to Kafka, the producer application serializes the data into a format suitable for transmission, such as byte arrays or specific serialization formats like Avro or Protobuf.
   - The producer is responsible for any necessary data transformations or modifications before serialization.

2. Zero-copy data transfer:
   - When the producer sends the serialized data to Kafka, Kafka uses zero-copy optimization to transfer the data directly from the file system cache to the network buffer.
   - During this zero-copy process, Kafka does not perform any data transformations or modifications.
   - The data is sent as-is, exactly as it was received from the producer.

3. Consumer-side deserialization:
   - When the consumer receives the data from Kafka, it needs to deserialize the data back into the application's format.
   - The consumer is responsible for any necessary data transformations or modifications after deserialization.

Kafka's zero-copy optimization focuses on efficient data transfer and does not include built-in mechanisms for data transformation (option A). It also does not provide a pluggable framework for custom data transformations during the zero-copy process (option B).

If data transformations are required, they should be performed by the producer before sending the data to Kafka and by the consumer after receiving the data from Kafka. Option D is incorrect because the broker never loads record data into application memory for transformation. This allows the zero-copy optimization to work efficiently by transferring data as-is, without any modifications.

</details>

## Question 22

What is the purpose of the `linger.ms` setting in the Kafka producer configuration?

- A. To specify the maximum time to wait for a response from the Kafka broker
- B. To specify the maximum time to wait before sending a batch of messages
- C. To specify the maximum time to wait for a message to be acknowledged by the Kafka broker
- D. To specify the maximum time to wait for a message to be written to the Kafka topic

<details>
<summary>Response:</summary> 

**Explanation:**
The `linger.ms` setting in the Kafka producer configuration is used to specify the maximum time to wait before sending a batch of messages. By default (`linger.ms=5` since Kafka 4.0, `0` before), the producer waits only a very short time. Setting `linger.ms` to a larger value allows the producer to wait for a short period of time to accumulate more messages into a batch before sending them to the Kafka broker. This can help improve throughput by reducing the number of requests sent to the broker.

**Answer:** B

</details>

## Question 23

How does the `batch.size` setting affect the behavior of the Kafka producer?

- A. It specifies the maximum number of messages that can be sent in a single batch
- B. It specifies the maximum size (in bytes) of a batch of messages
- C. It specifies the minimum number of messages required to form a batch
- D. It specifies the minimum size (in bytes) of a message to be included in a batch

<details>
<summary>Response:</summary> 

**Explanation:**
The `batch.size` setting in the Kafka producer configuration specifies the maximum size (in bytes) of a batch of messages. When the producer has accumulated messages up to the specified batch size or the `linger.ms` time has elapsed, it sends the batch of messages to the Kafka broker. Increasing the `batch.size` allows the producer to accumulate more messages into a single batch, potentially improving throughput. However, it also increases the memory usage of the producer and may introduce additional latency.

**Answer:** B

</details>

## Question 24

What happens if the Kafka producer exhausts its buffer memory while sending messages?

- A. The producer will block and wait until buffer memory becomes available
- B. The producer will start discarding the oldest messages to free up buffer memory
- C. The producer will start discarding the newest messages to free up buffer memory
- D. The producer will throw an exception and stop sending messages

<details>
<summary>Response:</summary> 

**Explanation:**
If the Kafka producer exhausts its buffer memory while sending messages, it will block and wait until buffer memory becomes available, for up to `max.block.ms` (default 60000 ms); after that `send()` throws a `TimeoutException`. The producer maintains a buffer of messages waiting to be sent to the Kafka broker. If the rate of message production exceeds the rate at which the producer can send messages to the broker, the buffer will start filling up. Once the buffer (`buffer.memory`, default 32 MB) is full, the producer will block in `send()` until some buffer memory becomes available. The producer never silently discards messages. However, it can also introduce latency if the producer remains blocked for an extended period.

**Answer:** A

</details>

## Question 25 [x]

What is the default value for the `acks` parameter in the Kafka producer configuration?

- A. 0
- B. 1
- C. all
- D. none

<details>
<summary>Response:</summary> 

**Explanation:**
The default value for the `acks` parameter in the Kafka producer configuration is `all` (equivalent to `-1`) since Kafka 3.0 (KIP-679, together with `enable.idempotence=true`). It was `1` in Kafka 2.x and earlier. With `acks=all` the leader waits for all in-sync replicas (subject to `min.insync.replicas`) before acknowledging, which is the strongest durability guarantee.

- A (`0`) and B (`1`) are the weaker settings and are no longer the default; D (`none`) is not a valid value.

**Answer:** C

</details>

## Question 26

What happens when the `acks` parameter is set to "all" in the Kafka producer configuration?

- A. The producer does not wait for any acknowledgment and considers the write successful immediately
- B. The producer waits for the leader replica to acknowledge the write before considering it successful
- C. The producer waits for all in-sync replicas to acknowledge the write before considering it successful
- D. The producer waits for a minimum number of replicas to acknowledge the write before considering it successful

<details>
<summary>Response:</summary> 

**Explanation:**
When the `acks` parameter is set to "all" in the Kafka producer configuration, the producer will wait for all in-sync replicas (ISRs) to acknowledge the write before considering it successful. This means that the producer will receive an acknowledgment only after the message has been successfully written to the leader replica and replicated to all the follower replicas that are currently in-sync. Setting `acks=all` provides the highest level of durability, as it ensures that the message is persisted on multiple replicas before the producer receives an acknowledgment. However, it also introduces additional latency since the producer has to wait for all ISRs to respond. The `min.insync.replicas` setting (option D is only partially right) additionally sets the minimum ISR size required for the write to be accepted.

**Answer:** C

</details>

## Question 27 [x]

How does the `max.in.flight.requests.per.connection` setting affect the behavior of the Kafka producer when `acks=1`?

- A. It specifies the maximum number of unacknowledged requests allowed per broker connection
- B. It specifies the maximum number of requests that can be sent to the broker concurrently
- C. It specifies the maximum number of messages that can be buffered in the producer's memory
- D. It has no effect when `acks=1`

<details>
<summary>Response:</summary> 

**Explanation:**
The `max.in.flight.requests.per.connection` setting in the Kafka producer configuration specifies the maximum number of unacknowledged requests allowed per broker connection. When `acks=1`, this setting determines how many requests the producer can send to the broker before waiting for an acknowledgment. By default, `max.in.flight.requests.per.connection` is set to 5, meaning the producer can send up to 5 requests to the broker without waiting for an acknowledgment. Increasing this value can potentially improve throughput by allowing more requests to be sent concurrently. However, it also increases the risk of out-of-order delivery if a request fails and needs to be retried, as the subsequent requests may have already been processed. (With idempotence, the default since Kafka 3.0, ordering is preserved for up to 5 in-flight requests.)

**Answer:** A

</details>

## Question 28

What is the purpose of the `enable.idempotence` setting in the Kafka producer configuration?

- A. To ensure that messages are delivered exactly once to the Kafka broker
- B. To enable compression of messages sent by the producer
- C. To specify the maximum size of a batch of messages
- D. To control the acknowledgment behavior of the producer

<details>
<summary>Response:</summary> 

**Explanation:**
The `enable.idempotence` setting in the Kafka producer configuration is used to ensure that messages are delivered exactly once to the Kafka broker, even in the presence of network or broker failures. When idempotence is enabled, the producer is assigned a producer ID (PID) and attaches a sequence number per partition to each batch. This allows the broker to detect and discard duplicates caused by retries, so each message is written exactly once per partition within the producer's session. Idempotence is enabled by default since Kafka 3.0 and requires `acks=all`, `retries>0` and `max.in.flight.requests.per.connection<=5`. Enabling idempotence provides a higher level of message delivery reliability, but it may slightly impact the performance of the producer due to the additional bookkeeping and coordination required.

**Answer:** A

</details>

## Question 29

What happens when `max.in.flight.requests.per.connection` is set to 1 and `enable.idempotence` is set to true in the Kafka producer configuration?

- A. The producer will send messages in batches to improve throughput
- B. The producer will wait for each request to be acknowledged before sending the next request
- C. The producer will retry failed requests automatically
- D. The producer will disable message compression

<details>
<summary>Response:</summary> 

**Explanation:**
When `max.in.flight.requests.per.connection` is set to 1 and `enable.idempotence` is set to true in the Kafka producer configuration, the producer will wait for each request to be acknowledged by the broker before sending the next request. This maintains the order of messages within each partition. Note that idempotence alone already preserves ordering with up to 5 in-flight requests, so setting the value to 1 is not necessary for ordering; it only reduces throughput, because the producer can send only one request at a time per broker connection. Option C is also a general producer behavior but is not what this setting changes. This configuration may limit the throughput of the producer, as it can only send one request at a time per broker connection.

**Answer:** B

</details>

## Question 30

How does enabling idempotence affect the performance of the Kafka producer?

- A. It significantly improves the producer's throughput
- B. It has no impact on the producer's performance
- C. It may slightly reduce the producer's throughput
- D. It increases the producer's memory usage

<details>
<summary>Response:</summary> 

**Explanation:**
Enabling idempotence in the Kafka producer configuration may slightly reduce the producer's throughput compared to a non-idempotent producer. When idempotence is enabled, the producer needs to perform additional bookkeeping and coordination with the Kafka broker to avoid duplicates on retry. This includes maintaining sequence numbers per partition and handling acknowledgments and retries. The additional overhead introduced by idempotence can result in a slight decrease in the producer's throughput. However, the impact on performance is generally minimal and is often outweighed by the benefit of no duplicates or reordering from retries (it is enabled by default since Kafka 3.0), especially in scenarios where message reliability is critical.

**Answer:** C

</details>

## Question 31

What does the `acks=all` setting in the Kafka producer configuration ensure?

- A. The producer will receive an acknowledgment only after the message is written to all replicas
- B. The producer will receive an acknowledgment only after the message is written to the leader replica
- C. The producer will receive an acknowledgment only after the message is written to all in-sync replicas
- D. The producer will not wait for any acknowledgment and will consider the write successful immediately

<details>
<summary>Response:</summary> 

**Explanation:**
When the `acks` parameter is set to "all" in the Kafka producer configuration, the producer will receive an acknowledgment only after the message is written to all in-sync replicas (ISRs). In-sync replicas are the replicas that are currently up-to-date with the leader and are considered to have the latest data. Setting `acks=all` ensures the highest level of durability, as the producer will wait for the message to be persisted on multiple replicas before considering the write successful. However, this setting also introduces additional latency, as the producer needs to wait for acknowledgments from all ISRs before proceeding.

**Answer:** C

</details>

## Question 32

What is the purpose of the `client.id` setting in the Kafka producer and consumer configurations?

- A. To specify a unique identifier for the client within a Kafka cluster
- B. To set the maximum number of requests the client can send or receive
- C. To determine the compression type used for message production or consumption
- D. To control the maximum amount of memory the client can use for buffering

<details>
<summary>Response:</summary> 

**Explanation:**
The `client.id` setting in the Kafka producer and consumer configurations is used to specify a unique identifier for the client within a Kafka cluster. It is an optional setting that helps in identifying and tracking the client's activity in the cluster. When set, the `client.id` is included in the metadata of requests sent by the client, making it easier to correlate and monitor client behavior. It can be useful for debugging purposes, as it allows you to identify specific clients in the logs and metrics. It is also usable as the identity for client quotas. The `client.id` does not change the functional behavior of the client, such as the number of requests, compression type, or memory usage.

**Answer:** A

</details>

## Question 33

What is the documented purpose of `client.id`, and what happens when multiple Kafka clients use the same value?

- A. The clients share the same configuration and connection pool
- B. The brokers treat them as one logical client, and consumer group membership is merged
- C. Kafka does not enforce uniqueness; brokers account them under one logical client name (shared quotas, merged metrics/log attribution), which makes troubleshooting harder
- D. The brokers reject the connection of the second client

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
`client.id` is a logical identifier of the client/application, used by the brokers for logging, metrics and quotas. It is not required to be unique: brokers do not reject duplicates and clients stay separate connections (and, in consumer groups, separate members identified by `member.id`). However, requests from all clients sharing a `client.id` are attributed to the same name, so client-id quotas are shared between them and metrics/logs cannot be told apart (client JMX MBeans may also collide). Use a unique, meaningful `client.id` per client instance.

- A and B are incorrect: configuration, connections and group membership are not shared.
- D is incorrect: there is no uniqueness check.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3, p. 54 ("client.id ... used in logging and metrics and for quotas"); https://kafka.apache.org/documentation/#producerconfigs_client.id

</details>

## Question 34

If a producer sends a message with a key to a topic with 5 partitions, which partition will the message be written to?

- A. The partition is randomly selected
- B. The partition is determined based on the hash of the message key
- C. The partition is always the first partition (partition 0)
- D. The partition is determined by the broker

<details>
<summary>Response:</summary> 

**Explanation:**
When a producer sends a message with a key to a topic, the partition to which the message is written is determined based on the hash of the message key. Kafka's default partitioner uses the murmur2 hash function to compute the hash of the key and then maps it to a specific partition.

The process works as follows:
1. The producer calculates the hash of the message key using the murmur2 hash function.
2. The hash value is then modulo'd by the number of partitions in the topic to determine the partition index.
3. The message is sent to the corresponding partition based on the calculated partition index.

This means that messages with the same key will always be sent to the same partition (as long as the number of partitions does not change), ensuring that they are stored in the order they were sent.

The partition is not randomly selected, nor is it always the first partition. The broker does not determine the partition for keyed messages; it is determined by the producer based on the hash of the message key.

**Answer:** B

</details>

## Question 35

What happens if a producer sends a message without a key to a topic with 3 partitions?

- A. The message is discarded
- B. The message is sent to a randomly selected partition
- C. The message is sent to all partitions
- D. The message is sent to the partition with the least amount of data

<details>
<summary>Response:</summary> 

**Explanation:**
When a producer sends a message without a key to a topic, the default partitioner chooses the partition itself, spreading records across partitions without any key-based mapping. Since Kafka 2.4 this uses "sticky" partitioning: the producer sticks to one partition until the current batch is full (or `linger.ms` elapses), then switches to another, so over time the load is spread roughly evenly (older versions used strict round-robin per record, as described in the book). Since Kafka 3.3 (KIP-794) adaptive partitioning can additionally favor partitions on faster brokers, and in Kafka 4.0 this logic is built into the producer (`partitioner.class` is unset by default).

The key point for the exam is that there is no key-based ordering or placement: the message goes to one partition chosen by the producer's partitioner.

The message is not discarded, sent to all partitions, or sent to the partition with the least amount of data. The partition for keyless messages is chosen by the producer's partitioner (sticky/round-robin style) to achieve a balanced distribution over time.

**Answer:** B

</details>

## Question 36

A single producer sends records with different keys that all hash to the same partition. With default settings of a modern client (Kafka 3.0+, `enable.idempotence=true`, `acks=all`, `max.in.flight.requests.per.connection=5`), what ordering does Kafka guarantee for these records within that partition?

- A. They are written in the order they were sent, even when retries occur
- B. They may be written in a different order, because ordering is guaranteed only among records with the same key
- C. Ordering is guaranteed only if `max.in.flight.requests.per.connection=1`
- D. Ordering is guaranteed only if the topic has `min.insync.replicas=1`

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
Kafka guarantees order per partition, not per key: records sent by one producer to the same partition are appended in send order regardless of their keys. The idempotent producer attaches sequence numbers, so even with retries and up to 5 in-flight requests the broker preserves order (it rejects out-of-order/duplicate batches). Without idempotence, `retries` > 0 with `max.in.flight.requests.per.connection` > 1 can reorder batches, and then only `max.in.flight=1` preserves order (C is therefore not required with idempotence). Records in different partitions or from different producers have no relative order. `min.insync.replicas` does not affect ordering.

Source: Kafka: The Definitive Guide 2nd ed., ch. 3, "Ordering Guarantees" (p. 59-60; idempotence works with max.in.flight <= 5); https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence

</details>

## Question 37

What happens when a producer tries to send a message to a partition whose leader replica is not in-sync?

- A. The producer receives a `NotLeaderOrFollowerException` and retries sending the message
- B. The producer waits until the leader replica becomes in-sync before sending the message
- C. The message is automatically routed to another in-sync replica
- D. The producer receives a `LeaderNotAvailableException` and the message is discarded

<details>
<summary>Response:</summary> 

**Explanation:**
When a producer tries to send a message to a partition whose leader replica is not in-sync, the producer will receive a `NotLeaderOrFollowerException`. This exception indicates that the broker the producer is connected to is not (or no longer) the leader for the partition and cannot accept writes, typically because leadership moved and the producer's metadata is stale. (A partition leader is always itself a member of the ISR, so the real-world case is a leadership change.)

In this situation, the producer typically retries sending the message after a short backoff period. The producer will attempt to refresh its metadata to obtain the current leader information for the partition. Once the producer has the updated leader information, it will retry sending the message to the new leader.

The producer does not wait indefinitely for the leader replica to become in-sync. It proactively refreshes its metadata and retries sending the message to the updated leader.

The message is not automatically routed to another in-sync replica. The producer specifically sends the message to the partition leader, and it is the leader's responsibility to replicate the message to the followers.

If the producer is unable to send the message after multiple retries, it may eventually timeout or return an error to the application, depending on its configuration. The message is not automatically discarded; it is the application's responsibility to handle the failure and decide whether to retry or discard the message.

**Answer:** A

</details>

## Question 38

In a topic with a replication factor of 3 and `min.insync.replicas` set to 2, what happens when a producer sends a message with `acks=all` and two replicas are not in-sync?

- A. The producer receives an acknowledgment and the message is successfully written
- B. The producer receives a `NotEnoughReplicasException` and the message is not written
- C. The producer waits indefinitely until at least two replicas become in-sync
- D. The message is written to the leader replica and the producer receives an acknowledgment

<details>
<summary>Response:</summary> 

**Explanation:**
When a topic has a replication factor of 3 and `min.insync.replicas` is set to 2, it means that at least 2 replicas (including the leader) must be in-sync for a write to be considered successful when `acks=all`.

In the scenario where a producer sends a message with `acks=all` and two replicas are not in-sync, the producer will receive a `NotEnoughReplicasException`, and the message will not be written to the topic. The `acks=all` configuration requires acknowledgment from all in-sync replicas before considering a write successful.

Since the topic has `min.insync.replicas` set to 2, the leader replica alone is not sufficient to meet the acknowledgment requirement. The producer will not receive an acknowledgment, and the message will not be written to the topic.

The broker checks the ISR size before appending, so the record is not written to the log. `NotEnoughReplicasException` is retriable: the producer keeps retrying until `delivery.timeout.ms` (default 2 minutes) expires and then reports the error to the application. It does not wait indefinitely.

The leader alone does not satisfy `min.insync.replicas=2`, so the write is rejected rather than acknowledged.

**Answer:** B

</details>