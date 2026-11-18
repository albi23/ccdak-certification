> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 21

How can you convert a stream into a table in KSQL?

- A. CREATE TABLE table_name AS SELECT key_col, COUNT(*) FROM stream_name GROUP BY key_col;
- B. INSERT INTO table_name SELECT * FROM stream_name;
- C. CREATE TABLE table_name FROM stream_name;
- D. CONVERT STREAM stream_name TO TABLE table_name;

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
A stream cannot be selected into a table as-is; a table is created from a stream by aggregating it, e.g. `CREATE TABLE table_name AS SELECT key_col, COUNT(*) FROM stream_name GROUP BY key_col;`.

- B, C, and D are incorrect because they are not valid syntaxes for this operation in KSQL.

</details>

## 🚫 Question 22

What is the purpose of the `AVRO` format in KSQL?

- A. To provide a human-readable format for data
- B. To enable complex data types and schema evolution
- C. To ensure data is stored as plain text
- D. To simplify data parsing

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The `AVRO` format in KSQL is used to enable complex data types and schema evolution. It is a binary serialization format that supports rich data structures and efficient data encoding.

- A, C, and D are incorrect because they do not accurately describe the purpose and capabilities of the AVRO format.

</details>

## 🚫 Question 23

Which KSQL function is used to extract the year from a timestamp?

- A. EXTRACTYEAR()
- B. GETYEAR()
- C. YEAR()
- D. EXTRACT(YEAR FROM timestamp)

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
The `EXTRACT(YEAR FROM timestamp)` function in KSQL is used to extract the year from a timestamp.

- A, B, and C are incorrect because they are not valid KSQL functions for this operation.

</details>

## 🚫 Question 24

How do you handle null values in KSQL?

- A. Use the `IS NULL` and `IS NOT NULL` predicates
- B. Use the `NULLIFY()` function
- C. Replace null values with default values using `COALESCE()`
- D. Both A and C

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In KSQL, you can handle null values using the `IS NULL` and `IS NOT NULL` predicates to filter records, and the `COALESCE()` function to replace null values with default values.

- B is incorrect because `NULLIFY()` is not a valid KSQL function. Combining A and C provides comprehensive handling of null values.

</details>

## 🚫 Question 25

Which KSQL function calculates the total sum of a column's values?

- A. SUM()
- B. TOTAL()
- C. ADD()
- D. AGGREGATE()

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `SUM()` function in KSQL calculates the total sum of a column's values.

- B, C, and D are incorrect because they are not valid KSQL functions for this operation.

</details>

## 🚫 Question 26

What is the default retention period for KSQL streams?

- A. 7 days
- B. 1 day
- C. 30 days
- D. 2 days

<details>
<summary>Response:</summary> 

**Answer:** A. 7 days

### Explanation:

In KSQL, streams are abstractions over Kafka topics. By default, the retention period for Kafka topics—and therefore KSQL streams—is **7 days**. This means that the data in a KSQL stream is retained for 7 days before it is eligible for deletion, unless you alter the topic settings (`retention.ms`).

**Key Points:**

- **Default Retention Period**: 7 days.
- **Inheritance from Kafka**: KSQL streams inherit the retention settings from the underlying Kafka topics.
- **Configuration**: You can adjust the retention period by changing the topic's `retention.ms` configuration (or creating the topic beforehand with the desired retention); there is no per-stream `RETENTION` property in `CREATE STREAM`.

**Example (retention is not set here; it stays the topic default):**

```sql
CREATE STREAM my_stream (
  ...
) WITH (
  kafka_topic='my_topic',
  value_format='JSON',
  partitions=1  -- retention is a topic config (retention.ms, default 604800000 = 7 days)
);
```

**Other Options Explained:**

- **B. 1 day**: Not the default retention period but can be set manually.
- **C. 30 days**: Not the default retention period.
- **D. 2 days**: Not the default retention period but can be configured if needed.

</details>

## 🚫 Question 27

How can you filter records in a KSQL stream?

- A. By using the `FILTER` clause
- B. By using the `WHERE` clause
- C. By using the `HAVING` clause
- D. By using the `LIMIT` clause

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
Records in a KSQL stream can be filtered using the `WHERE` clause, which allows you to specify conditions that records must meet to be included in the query results.

- A, C, and D are incorrect because they are not valid clauses for filtering records in a KSQL stream.

</details>

## 🚫 Question 28

Which KSQL function can be used to format timestamps?

- A. FORMAT_TIMESTAMP()
- B. TO_TIMESTAMP()
- C. DATE_FORMAT()
- D. TIMESTAMP_FORMAT()

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `FORMAT_TIMESTAMP()` function (and the older `TIMESTAMPTOSTRING()`) in ksqlDB formats a timestamp using a given pattern.

- B is incorrect because `TO_TIMESTAMP()` is not a ksqlDB function (parsing is `PARSE_TIMESTAMP()`). C and D are not ksqlDB functions.


</details>
