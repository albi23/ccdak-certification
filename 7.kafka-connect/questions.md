> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## Question 1:
For a system designed to read data from an external database, perform some transformations, and then store the results in a Kafka topic, which approach is most suitable?

1. Consumer + Producer
2. Kafka Connect Source
3. Kafka Connect Sink
4. Kafka Streams

<details>
<summary>Response:</summary> 

The correct answer is **2. Kafka Connect Source.**

**Explanation:**
Kafka Connect Source is designed for importing data from external systems into Kafka topics. It can easily read from an external database, and with the appropriate connectors and transformations configured, it can modify the data as required before making it available in a Kafka topic.

</details>

## Question 2:
When needing to aggregate real-time data from a Kafka topic, compute running totals, and then publish those totals back to another Kafka topic for further analysis, which tool should you use?

1. Consumer + Producer
2. Kafka Connect Source
3. Kafka Connect Sink
4. Kafka Streams

<details>
<summary>Response:</summary> 

The correct answer is **4. Kafka Streams.**

**Explanation:**
Kafka Streams is specifically designed for building real-time streaming data pipelines and applications that transform or react to the streams of data. For tasks like aggregating data and computing running totals, Kafka Streams provides the necessary stateful operations and can directly publish the results back to another Kafka topic.

</details>

## Question 3:
If the objective is to periodically export data from a Kafka topic to a relational database for long-term storage and analysis, which Kafka component would best fulfill this requirement?

1. Consumer + Producer
2. Kafka Connect Source
3. Kafka Connect Sink
4. Kafka Streams

<details>
<summary>Response:</summary> 

The correct answer is **3. Kafka Connect Sink.**

**Explanation:**
Kafka Connect Sink is designed to export data from Kafka topics into external systems such as databases, key-value stores, search indexes, and file systems. For scenarios where the goal is to move data from Kafka to a relational database, a Kafka Connect Sink connector can be configured to handle this task efficiently and with minimal coding effort.

</details>

## Question 4:
A financial institution wants to analyze transaction data in real-time to detect fraudulent activities. The transaction data, which includes sensitive information, is initially stored in a mainframe system. Which approach ensures secure, real-time analysis of this data by a Kafka Streams application while complying with data privacy regulations?

1. Utilize a mainframe connector with Kafka Connect to ingest the transaction data into a Kafka topic. Apply a Kafka Streams application to anonymize sensitive information in the stream before conducting fraud analysis.
2.  Directly connect the mainframe system to the Kafka Streams application using a custom API, ensuring sensitive data is filtered out during the streaming process.
3.  Employ ksqlDB to directly query the mainframe system, apply data anonymization functions to filter out sensitive information, and then write the sanitized data to a Kafka topic for stream processing.
4.  Implement a batch process to extract transaction data periodically from the mainframe, cleanse the data of sensitive information, and then load the sanitized data into Kafka topics for streaming analysis.

<details>
<summary>Response:</summary> 

The correct answer is **1. Utilize a mainframe connector with Kafka Connect to ingest the transaction data into a Kafka topic. Apply a Kafka Streams application to anonymize sensitive information in the stream before conducting fraud analysis.**

</details>

## Question 5:
Your organization aims to implement a real-time recommendation engine for e-commerce users based on their browsing behavior. User session data is considered sensitive and must be anonymized before processing. How can the Kafka ecosystem be leveraged to meet these requirements?

1. Deploy a Kafka Connect Source Connector to capture session data directly into Kafka, using Stream Processing to anonymize user identifiers before aggregating sessions for recommendation analysis.
2.  Use a custom Kafka Producer application to publish session data to a topic, applying a Stream Processor to anonymize and then process the data for generating recommendations.
3.  Implement a Kafka Connect Sink Connector to store session data into a NoSQL database, with a pre-processor to remove sensitive information before ingestion. Use Kafka Streams to read from the database for analysis.
4.  Create a ksqlDB process to pull session data from source systems, apply anonymization functions within ksqlDB, and output the clean data to a Kafka topic for further processing by the Kafka Streams application.

<details>
<summary>Response:</summary> 

The correct answer is **1. Deploy a Kafka Connect Source Connector to capture session data directly into Kafka, using Stream Processing to anonymize user identifiers before aggregating sessions for recommendation analysis.**

</details>

## Question 6:
An organization is implementing a system to monitor and alert on infrastructure health status in real-time. The system collects metrics from various sources, including some that contain proprietary information. Which approach ensures that only non-proprietary, critical health metrics are analyzed and alerted on?

1. Use Kafka Connect with appropriate Source Connectors for each metric source, configuring the connectors to filter out proprietary information. Process the filtered metrics stream with Kafka Streams for alerting.
2.  Directly stream all metrics into Kafka using custom Producers, then employ a Kafka Streams application to separate proprietary data from non-proprietary data, and analyze the latter for alerting.
3.  Implement a series of ksqlDB statements to ingest metrics into Kafka, applying filtering logic within ksqlDB to remove proprietary information before streaming processing and alerting.
4.  Configure a Kafka Connect Sink Connector to aggregate all metrics into a centralized database, followed by batch processing to remove proprietary information before streaming the data into Kafka for real-time analysis.

<details>
<summary>Response:</summary> 

The correct answer is **1. Use Kafka Connect with appropriate Source Connectors for each metric source, configuring the connectors to filter out proprietary information. Process the filtered metrics stream with Kafka Streams for alerting.**

</details>

## Question 7:
A multinational corporation is looking to aggregate sales data from multiple regional systems into a centralized Kafka topic for real-time analysis and reporting. The regional systems vary in technology, including SQL databases and cloud-based storage solutions. Which solution enables the efficient and unified ingestion of these diverse data sources into Kafka?

1. Deploy Kafka Streams applications near each regional system to collect and forward data to the centralized Kafka topic.
2.  Use Kafka Connect with a mix of Source Connectors suitable for each regional system's technology to ingest data directly into Kafka.
3.  Implement custom Kafka Producers embedded within each regional system to push data to the centralized Kafka topic.
4.  Configure a Kafka Connect Sink Connector for each regional system to replicate data into the centralized Kafka topic.

<details>
<summary>Response:</summary> 

The correct answer is **2.  Use Kafka Connect with a mix of Source Connectors suitable for each regional system's technology to ingest data directly into Kafka.**

</details>

## Question 8:
An online media platform wishes to analyze user interactions (clicks, views, and comments) in real-time to dynamically adjust content recommendations. The platform generates a high volume of interaction data, necessitating scalable and real-time processing. What architecture best suits this requirement?

1. Utilize a Kafka Connect Source Connector to ingest interaction data into Kafka, then process this data with Kafka Streams to update content recommendations in real-time.
2. Directly stream interaction data into Kafka using a custom API, then use ksqlDB to perform real-time analysis and generate content recommendations.
3. Implement batch processing jobs to periodically analyze interaction data stored in an external database, and then use Kafka to distribute batch analysis results for content recommendation updates.
4. Configure Kafka Connect Sink Connectors to collect interaction data into a big data platform first, then process the data using external stream processing tools before updating content recommendations.

<details>
<summary>Response:</summary> 

The correct answer is **1. Utilize a Kafka Connect Source Connector to ingest interaction data into Kafka, then process this data with Kafka Streams to update content recommendations in real-time.**

</details>

## Question 9:
A utility company monitors a network of IoT devices deployed across an energy grid. The devices send telemetry data (e.g., power usage, system health) every minute. The company wants to aggregate this data for near-real-time monitoring and anomaly detection. Which Kafka-based solution efficiently achieves this goal?

1. Configure Kafka Connect Sink Connectors to collect telemetry data from the IoT devices into Kafka, followed by a Kafka Streams application to aggregate and analyze the data.
2. Use Kafka Connect Source Connectors appropriate for the IoT devices' communication protocols to ingest telemetry data into Kafka, then employ Kafka Streams for data aggregation and anomaly detection.
3. Develop custom Kafka Producers within the IoT devices to send data directly to Kafka topics, then use external tools to pull and analyze the data from Kafka.
4. Implement a centralized database to collect IoT telemetry data first, then use Kafka Connect Source Connectors to ingest the data from the database into Kafka for further processing.

<details>
<summary>Response:</summary> 

The correct answer is **2.  Use Kafka Connect Source Connectors appropriate for the IoT devices' communication protocols to ingest telemetry data into Kafka, then employ Kafka Streams for data aggregation and anomaly detection.**

</details>

## Question 10:
A digital marketing platform analyzes user activities to send personalized marketing emails. The platform streams activity data into a Kafka topic and processes it with a Kafka Streams application (the data is already in Kafka; the processing application is the bottleneck). Data volume fluctuates throughout the day. Which strategy best lets processing keep up with the load during peaks?

1. Dynamically adjust the number of partitions in the user activities topic based on incoming data volume.
2.  Scale the Kafka Streams application instances up or down in response to the processing load.
3.  Increase or decrease the number of Kafka Connect Source Connector tasks to match the rate of incoming user activity data.
4.  Modify the replication factor of the user activities topic during high load periods to improve data durability and availability.

<details>
<summary>Response:</summary> 

The correct answer is **2.  Scale the Kafka Streams application instances up or down in response to the processing load.**

Explanation: Streams instances with the same `application.id` form a consumer group and share the input partitions, so adding/removing instances scales processing (up to the number of partitions/tasks). 1 is wrong: partitions can only be increased (never decreased) and changing them breaks key-to-partition mapping. 3 is wrong: source connector tasks only affect ingestion from an external system, not processing of data already in Kafka. 4 is wrong: replication factor affects durability, not throughput.
Source: Kafka docs, Streams "Architecture" (parallelism model) https://kafka.apache.org/43/documentation/streams/architecture

</details>

## 🚫 Question 11:
An e-commerce company uses Kafka to process customer orders. During sales events, the order volume spikes significantly. Which approach ensures the system scales efficiently to handle these spikes in order volume?

1. Automatically adjust the number of topics to spread the increased order messages across more Kafka topics during sales events.
2. Use Kafka Connect with scalable Source Connectors to adjust the throughput based on order volume.
3. Scale out the Kafka broker cluster by adding more brokers during high-volume periods and scale in when the volume decreases.
4. Configure the Kafka producer to dynamically adjust batch size and linger time based on the current throughput of order messages.

<details>
<summary>Response:</summary> 

The correct answer is **3. Scale out the Kafka broker cluster by adding more brokers during high-volume periods and scale in when the volume decreases.**

(Note: adding brokers does not move existing partitions automatically; a partition reassignment is required. This broker-administration topic is outside the exam scope.)

</details>

## Question 12:

A streaming media company uses Kafka to ingest viewer watch history for real-time recommendation updates. Viewer engagement varies greatly, with peak times during new content releases. To handle variable ingestion rates, which configuration should be optimized?

1. Adjust the replication factor of the watch history topic in real-time to handle the increased data volume.
2. Increase and decrease the number of Kafka Connect Sink Connector tasks to efficiently write watch history data into Kafka.
3. Scale the number of Kafka Streams applications processing the watch history data according to the ingestion rate.
4. Dynamically modify the number of partitions in the watch history topic to manage the load during peak engagement times.

<details>
<summary>Response:</summary> 

**Correct Answer:** 3. Scale the number of Kafka Streams applications processing the watch history data according to the ingestion rate.

**Explanation:**

Kafka Streams applications are responsible for processing data from Kafka topics in real-time. By scaling the number of Kafka Streams application instances, the company can adjust the processing capacity to match the variable ingestion rates, especially during peak times.

Key benefits of this approach:
- Scaling up during high engagement ensures that the system can handle increased data volumes without latency.
- Scaling down during low engagement periods optimizes resource utilization and reduces costs.
- This method allows for dynamic adjustment based on processing load rather than modifying Kafka's underlying configurations, which can be more complex and less responsive to real-time fluctuations.

**Why other options are less suitable:**

1. Adjusting the replication factor in real-time is not practical and does not directly address the issue of variable ingestion rates. Replication factor affects data redundancy and fault tolerance, not processing capacity.
2. Kafka Connect Sink Connectors are used to export data from Kafka to external systems, not for ingesting data into Kafka. This option is not relevant for the given scenario of ingesting viewer watch history.
4. Dynamically modifying the number of partitions is operationally complex (it changes key-to-partition mapping and triggers rebalances). It's not recommended to change partition counts frequently in response to fluctuating loads.

</details>

## 🚫 Question 13:
A logistics company tracks shipping containers across the globe in real-time. This tracking information is stored in various formats across different databases. The company aims to centralize this data into Kafka for real-time visibility and to enable reactive logistics management. The IT team is proficient in SQL but new to Kafka. Which approach should they take to integrate this diverse data into Kafka efficiently?

1. Use JDBC Source Connectors to ingest container tracking data into Kafka. Transform this data into a unified format using Kafka Streams for real-time logistics management.
2. Streamline data into Kafka using custom scripts that extract data from databases and publish to Kafka, relying on Kafka Streams for necessary transformations.
3. Consolidate data in the RDBMS using SQL procedures to match the target schema required by Kafka, then use JDBC Source Connectors to stream this unified data into Kafka.
4. Ingest raw data into Kafka using JDBC Source Connectors, then employ ksqlDB to perform SQL-like transformations and route the data to various microservices.

<details>
<summary>Response:</summary> 

The correct answer is **4. Ingest raw data into Kafka using JDBC Source Connectors, then employ ksqlDB to perform SQL-like transformations and route the data to various microservices.**

</details>

## 🚫 Question 14:
A retail company wishes to analyze customer transactions in real-time to personalize marketing efforts. Transaction data, including purchases and returns, is captured in a legacy system. The marketing team requires this data in a format that can be easily queried and joined with other customer data. Given the team's familiarity with SQL, what is the most effective way to achieve this?

1. Use JDBC Source Connectors to ingest transaction data into Kafka, followed by Kafka Streams for data transformation and enrichment.
2. Directly export transaction data to CSV files, use custom producers to send these files to Kafka, and then apply Kafka Streams for transformation.
3. Ingest transaction data into Kafka using JDBC Source Connectors and leverage ksqlDB for transforming and querying the data in a SQL-like manner.
4. Transform data within the legacy system using SQL stored procedures, then use JDBC Source Connectors to ingest the pre-transformed data into Kafka.

<details>
<summary>Response:</summary> 

The correct answer is **3. Ingest transaction data into Kafka using JDBC Source Connectors and leverage ksqlDB for transforming and querying the data in a SQL-like manner.**

</details>

## 🚫 Question 15:
An automotive manufacturer aims to optimize its supply chain by analyzing sensor data from its manufacturing equipment in real-time. The sensor data is currently logged in a proprietary format in a traditional database. The operations team, skilled in SQL, seeks to convert this data into actionable insights. Considering their expertise and requirements, which solution would best suit their needs?

1. Utilize JDBC Source Connectors to stream sensor data into Kafka, transforming the data into a more accessible format using Kafka Streams.
2. Export sensor data to a common format like JSON, use Kafka Connect to ingest this data, and then apply ksqlDB to analyze and visualize the data in real-time.
3. Stream sensor data directly into Kafka using custom producers, followed by data transformation through SQL procedures embedded within the Kafka ecosystem.
4. Ingest sensor data into Kafka using JDBC Source Connectors, then use ksqlDB to perform real-time analytics and transform the data for downstream processing.

<details>
<summary>Response:</summary> 

The correct answer is **4. Ingest sensor data into Kafka using JDBC Source Connectors, then use ksqlDB to perform real-time analytics and transform the data for downstream processing.**

</details>

## 🚫 Question 16:
A company plans to synchronize data between a PostgreSQL database and a Kafka cluster to enable real-time analytics. Which connector should be used to efficiently import data from PostgreSQL into Kafka?

1. JDBC Source Connector
2. S3 Sink Connector
3. Elasticsearch Sink Connector
4. HDFS Sink Connector

<details>
<summary>Response:</summary> 

The correct answer is **1. JDBC Source Connector.**

**Explanation:**
- **1. JDBC Source Connector**: Correct choice. The JDBC Source Connector is designed to pull data from relational databases like PostgreSQL into Kafka topics, making it suitable for real-time data synchronization and analytics.
- **2. S3 Sink Connector**: Incorrect for this use case. This connector is used to export data from Kafka topics into AWS S3, not for importing data from databases into Kafka.
- **3. Elasticsearch Sink Connector**: Also incorrect for the scenario. While useful for exporting data from Kafka to Elasticsearch for search and analytics, it does not facilitate data import from PostgreSQL to Kafka.
- **4. HDFS Sink Connector**: Not applicable here. This connector exports data from Kafka to HDFS (Hadoop Distributed File System), and does not support importing data from PostgreSQL into Kafka.

</details>

## 🚫 Question 17:
Your organization requires real-time text search capabilities on data streamed through Kafka. Which connector best facilitates exporting data from Kafka topics into Elasticsearch to meet this requirement?

1. JDBC Sink Connector
2. Elasticsearch Sink Connector
3. MongoDB Sink Connector
4. Kafka Connect File Sink Connector

<details>
<summary>Response:</summary> 

The correct answer is **2. Elasticsearch Sink Connector.**

**Explanation:**
- **1. JDBC Sink Connector**: Incorrect for this requirement. Primarily used for moving data from Kafka to relational databases, not suitable for integration with Elasticsearch for text search.
- **2. Elasticsearch Sink Connector**: Perfect fit. This connector is specifically designed to export data from Kafka topics directly into Elasticsearch, enabling powerful search and analytics capabilities on the streamed data.
- **3. MongoDB Sink Connector**: Incorrect. While MongoDB offers text search capabilities, this connector focuses on exporting data to MongoDB, not Elasticsearch.
- **4. Kafka Connect File Sink Connector**: Incorrect. This connector writes data from Kafka topics to the file system and does not integrate with Elasticsearch or support text search functionalities directly.

</details>

## 🚫 Question 18:
A streaming application is designed to process events in real-time and then store processed events in an Amazon S3 bucket for long-term analysis. Which connector configuration is most appropriate for this use case?

1. JDBC Source Connector
2. S3 Sink Connector
3. MQTT Source Connector
4. File Source Connector

<details>
<summary>Response:</summary> 

The correct answer is **2. S3 Sink Connector.**

**Explanation:**
- **1. JDBC Source Connector**: Incorrect. This connector is used for importing data from relational databases into Kafka, not for storing data into S3.
- **2. S3 Sink Connector**: Correct. Specifically designed for exporting data from Kafka topics into Amazon S3, this connector supports both the requirement for long-term storage and efficient data analysis.
- **3. MQTT Source Connector**: Incorrect. This connector is utilized for ingesting data from MQTT-enabled devices into Kafka and does not facilitate data export to S3.
- **4. File Source Connector**: Incorrect. It's used for reading data from files into Kafka topics, not for writing or storing data into Amazon S3 from Kafka.

</details>

## Question 19:
An IoT company collects temperature and humidity data from sensors deployed in various locations. The goal is to correlate this environmental data with location-specific weather forecasts retrieved from an external API. Which approach best facilitates this integration and processing within the Kafka ecosystem?

1. Ingest sensor data into a Kafka topic using MQTT connectors. Separately, use an external service to fetch weather forecasts, storing this data in a Kafka topic via the HTTP Source Connector. Utilize Kafka Streams to join sensor data with weather forecasts based on location and timestamp, outputting enriched data to another topic.
2. Directly stream sensor data and weather forecasts into Kafka using custom Kafka Producers implemented in Python. These producers perform API calls to retrieve forecasts, merge this data with sensor readings, and produce the combined records into a single Kafka topic.
3. Use the MQTT Source Connector to ingest sensor data into Kafka. Write a Kafka Streams application that performs REST API calls to the weather forecast service for each sensor data record processed, enriching and producing enriched records to a new topic.
4. Implement an MQTT proxy to capture sensor data into Kafka. Concurrently, utilize Kafka Connect with the JDBC Sink Connector to store sensor data in a relational database, from which an external cron job fetches weather forecasts, merges them with sensor data, and re-ingests the enriched data back into Kafka via JDBC Source Connector.

<details>
<summary>Response:</summary> 

The correct answer is **1. Ingest sensor data into a Kafka topic using MQTT connectors. Separately, use an external service to fetch weather forecasts, storing this data in a Kafka topic via the HTTP Source Connector. Utilize Kafka Streams to join sensor data with weather forecasts based on location and timestamp, outputting enriched data to another topic.**

**Explanation:**
- **1.** Correct. This approach leverages the strengths of Kafka's ecosystem for real-time data integration and processing. MQTT connectors efficiently ingest sensor data, while the HTTP Source Connector handles external API data. Kafka Streams then enables complex processing, such as joining data streams based on key attributes like location and time.
- **2.** While using custom producers allows for flexible data ingestion and preprocessing, it bypasses Kafka's robust and scalable data integration capabilities, such as fault tolerance and parallel processing provided by connectors and Kafka Streams.
- **3.** Integrating external API calls directly within a Kafka Streams application for each record can introduce significant latency and potential rate limit issues with the weather API, making it less efficient for enriching streaming data at scale.
- **4.** This method introduces unnecessary complexity and latency by cycling data through external systems and back into Kafka. It also fails to utilize Kafka's real-time streaming capabilities efficiently, such as stream processing for data enrichment without the need for intermediate storage.

</details>

## Question 20:
A retail chain wants to integrate sales data from their Point of Sale (POS) systems across multiple stores into Kafka for real-time analysis and inventory management. Each store's POS system dumps sales records into a local SQL database. The integration needs to account for network bandwidth limitations. Which strategy optimally addresses these requirements?

1. Deploy Kafka Connect with the JDBC Source Connector at each store to ingest sales data into Kafka, using Single Message Transforms (SMTs) to filter and reduce the size of the data on the fly. Aggregate this data centrally using a Kafka Streams application for inventory analysis.
2. Utilize log-based Change Data Capture (CDC) connectors to monitor changes in each store's SQL database, streaming only new or changed sales records into Kafka. This minimizes network usage and enables real-time central processing with Kafka Streams.
3. Implement custom Kafka Producers within the POS systems to directly publish sales data to Kafka, compressing messages to mitigate network bandwidth issues. Use Kafka Streams for processing and inventory management centrally.
4. Set up a central database to aggregate sales data from all stores nightly. Use the JDBC Sink Connector to transfer this aggregated data into Kafka for next-day inventory analysis, relying on batch processing rather than real-time analysis.

<details>
<summary>Response:</summary> 

The correct answer is **2. Utilize log-based Change Data Capture (CDC) connectors to monitor changes in each store's SQL database, streaming only new or changed sales records into Kafka. This minimizes network usage and enables real-time central processing with Kafka Streams.**

**Explanation:**
- **1.** While JDBC Source Connectors are capable of ingesting data into Kafka, using them without consideration for data volume and network bandwidth can lead to inefficiencies, especially in bandwidth-limited environments.
- **2.** Correct. CDC connectors are designed to efficiently capture and stream only the incremental changes (new or updated sales records), significantly reducing network bandwidth requirements and enabling effective real-time data integration and processing.
- **3.** Custom producers offer flexibility but require additional development and maintenance effort. Compressing messages addresses bandwidth concerns but doesn't reduce the volume of data sent as effectively as streaming only changes.
- **4.** This approach shifts towards batch processing, which does not meet the requirement for real-time analysis and fails to leverage Kafka's real-time streaming capabilities.

</details>


## 🚫 Question 21:
A media company streams live video content, which generates logs of viewer interactions (e.g., play, pause, stop) in real-time. To enhance viewer experience through personalized content and advertisements, they need to analyze these logs in real-time. The logs are stored in NoSQL databases across different geographical locations. Considering the need for low-latency analysis, which setup is most appropriate?

1. Use Kafka Connect with a custom NoSQL Source Connector for each geographical location to ingest logs into Kafka, then utilize Kafka Streams for real-time analysis and dynamic content delivery.
2. Directly stream logs from NoSQL databases to Kafka using log-based Change Data Capture (CDC) connectors specific to each NoSQL database type, followed by processing with ksqlDB to generate viewer insights and personalized content recommendations.
3. Configure a network of MQTT brokers to collect logs from each location, and then use an MQTT Source Connector to consolidate logs into Kafka. Apply a Kafka Streams application to analyze viewer interactions and adjust content recommendations.
4. Implement a batch ETL process to extract logs from NoSQL databases nightly, load them into Kafka for next-day processing with Kafka Streams, and update content recommendations based on the analysis.

<details>
<summary>Response:</summary> 

The correct answer is **2. Directly stream logs from NoSQL databases to Kafka using log-based Change Data Capture (CDC) connectors specific to each NoSQL database type, followed by processing with ksqlDB to generate viewer insights and personalized content recommendations.**

**Explanation:**
- **1.** Custom connectors for each location could work but might not offer the low-latency needed for real-time analysis and personalized content delivery compared to CDC connectors that capture changes as they happen.
- **2.** Correct. CDC connectors are designed to capture and stream real-time changes (including viewer interactions) from databases to Kafka, facilitating immediate analysis. Using ksqlDB allows for leveraging SQL-like queries for real-time data processing, ideal for generating insights and recommendations with minimal latency.
- **3.** While MQTT is suitable for IoT data, using it for log data from NoSQL databases introduces unnecessary complexity and may not provide the direct integration or the efficiency of CDC connectors.
- **4.** Batch ETL processes cannot meet the requirements for real-time analysis and dynamic content personalization due to the inherent delay in processing.

</details>

## 🚫 Question 22:
An online retailer integrates user reviews from their website into Kafka to perform sentiment analysis and adjust product rankings accordingly. Reviews are initially posted to a MongoDB database. To ensure the analysis reflects recent feedback, which configuration ensures the most efficient and timely data flow into Kafka?

1. Configure MongoDB Source Connector to capture new and updated reviews into Kafka, then use Kafka Streams for sentiment analysis and to adjust product rankings in near-real-time.
2. Utilize a cron job to export reviews from MongoDB to CSV files at regular intervals, then use File Source Connectors to ingest these files into Kafka, followed by processing with Kafka Streams.
3. Deploy log-based CDC connectors to stream only the changes (new and updated reviews) from MongoDB into Kafka, leveraging ksqlDB for continuous sentiment analysis and product ranking adjustments.
4. Directly access the MongoDB API from Kafka Streams applications to fetch new and updated reviews, perform sentiment analysis, and update product rankings without storing reviews in Kafka.

<details>
<summary>Response:</summary> 

The correct answer is **3. Deploy log-based CDC connectors to stream only the changes (new and updated reviews) from MongoDB into Kafka, leveraging ksqlDB for continuous sentiment analysis and product ranking adjustments.**

**Explanation:**
- **1.** MongoDB Source Connector can efficiently ingest data into Kafka, but this option doesn't specify the efficiency of capturing only new or updated reviews like CDC would.
- **2.** Exporting to CSV and using File Source Connectors introduces delays, making it unsuitable for reflecting recent feedback in near-real-time.
- **3.** Correct. CDC connectors are specifically designed for efficient, real-time data synchronization by capturing only new and modified data. Using ksqlDB for sentiment analysis allows for real-time processing and immediate action on the insights.
- **4.** Fetching data directly via the MongoDB API bypasses Kafka's benefits of decoupling data producers and consumers, scalability, and fault tolerance, making it less efficient for real-time analysis and adjustment of product rankings.

</details>

## 🚫 Question 23:
A financial institution aims to merge transaction data from legacy systems with real-time fraud detection models running on Kafka Streams. The transaction data resides in various legacy databases and must be enriched with real-time fraud signals before being presented on a dashboard. What's the most effective architecture for this use case?

1. Use JDBC Source Connectors to ingest transaction data from legacy databases into Kafka. Enrich the data using Kafka Streams by joining it with real-time fraud detection signals. Utilize a Kafka Connect Sink Connector to publish the enriched data to the dashboard.
2. Implement custom Kafka Producers to extract transaction data from legacy systems, enriching the data in-flight with fraud detection signals before producing it to a Kafka topic for dashboard consumption.
3. Directly connect the legacy databases to Kafka Streams applications using custom database clients. Perform the enrichment with real-time fraud detection signals in the application, then produce the enriched data to a Kafka topic for dashboard visualization.
4. Leverage Change Data Capture (CDC) connectors to stream transaction data from legacy databases into Kafka. Use Kafka Streams for real-time enrichment with fraud detection signals and ksqlDB to further process and prepare the data for dashboard presentation.

<details>
<summary>Response:</summary> 

The correct answer is **4. Leverage Change Data Capture (CDC) connectors to stream transaction data from legacy databases into Kafka. Use Kafka Streams for real-time enrichment with fraud detection signals and ksqlDB to further process and prepare the data for dashboard presentation.**

**Explanation:**
- **1.** While using JDBC Source Connectors to ingest transaction data into Kafka is a viable option, it may not provide the low-latency required for real-time fraud detection compared to the efficiency of CDC connectors.
- **2.** Implementing custom Kafka Producers requires significant development effort and might not be as efficient or scalable as using built-in Kafka Connect connectors. Additionally, enriching data in-flight before it reaches Kafka can complicate the architecture.
- **3.** Connecting legacy databases directly to Kafka Streams applications complicates the architecture and increases the coupling between data sources and processing logic, making the system less resilient and scalable.
- **4.** Correct. CDC connectors are ideal for capturing changes from legacy databases in real-time, minimizing latency. Kafka Streams enables sophisticated stream processing capabilities for enrichment with fraud detection signals. Using ksqlDB allows for additional processing and preparation of the enriched data in a more accessible SQL-like language, making it suitable for dynamic dashboard presentation. This option efficiently combines real-time data integration, processing, and presentation while leveraging the strengths of the Kafka ecosystem.

</details>

## Question 24

Where are the Kafka Connect connector configurations stored?

- 1. In a separate config file on each Kafka Connect worker
- 2. In the Kafka broker's config directory
- 3. In Zookeeper under the `/kafka-connect` znode
- 4. In a special Kafka topic named `connect-configs`

<details>
<summary>Response:</summary>  4

**Explanation:**
In distributed mode, Kafka Connect stores connector and task configurations in a compacted Kafka topic set by `config.storage.topic` (conventionally named `connect-configs`). When a connector is created or updated, the configuration is persisted in this topic.

- 1 is incorrect because connector configs are not stored in separate files on the worker nodes.
- 2 is incorrect as connector configs are not stored in the Kafka broker's config directory.
- 3 is incorrect because Kafka Connect does not use ZooKeeper at all (it coordinates through Kafka's group protocol and internal topics; ZooKeeper is removed entirely in Kafka 4.x).

</details>

## Question 25

You want to use Kafka Connect to export data from a Kafka topic to a relational database. Which type of connector should you use?

- 1. Source Connector
- 2. Sink Connector
- 3. Transformation Connector
- 4. Import Connector

<details>
<summary>Response:</summary> 

**Answer:** 2

**Explanation:**
In Kafka Connect, a Sink Connector is used to consume data from Kafka topics and deliver it to an external system, such as a relational database, a search index, or a file system.

- 1 Source Connector is used to import data from an external system into Kafka topics, which is the opposite of what's needed here.
- 3 is incorrect because Transformation Connectors are not a real type in Kafka Connect. Transformations can be applied to a connector configuration, but they are not a separate connector type.
- 4 is incorrect because "Import Connector" is not a real term in Kafka Connect.

</details>

## Question 26

You need to stream data from a Twitter feed into a Kafka topic for real-time processing. Which Kafka Connect connector type is most appropriate?

- 1. Sink Connector
- 2. Source Connector
- 3. Transformation Connector
- 4. Export Connector

<details>
<summary>Response:</summary> 

**Answer:** 2

**Explanation:**
A Kafka Connect Source Connector is used to import data from an external source, such as a database, a Twitter feed, or a messaging system, and publish that data to Kafka topics.

- 1 Sink Connector is used to export data from Kafka topics to an external system, which is the opposite of what's needed here.
- 3 is incorrect because Transformation Connectors are not a real type in Kafka Connect. Transformations can be applied to a connector configuration, but they are not a separate connector type.
- 4 is incorrect because "Export Connector" is not a real term in Kafka Connect.

</details>

## Question 27

You are using Kafka Connect to move data from a source system into Kafka for real-time processing with Kafka Streams. After processing, the results need to be stored in HDFS for batch analysis. Which combination of connector types will you need?

- 1. Source Connector -> Sink Connector
- 2. Sink Connector -> Source Connector
- 3. Source Connector -> Source Connector
- 4. Sink Connector -> Sink Connector

<details>
<summary>Response:</summary> 

**Answer:** 1

**Explanation:**
This scenario requires a combination of a Source Connector and a Sink Connector:

1. A Source Connector is needed to import data from the source system into Kafka topics.
2. Kafka Streams can then process this data in real-time.
3. Finally, a Sink Connector is needed to export the processed results from Kafka topics to HDFS.

The other options are incorrect:

- 2 would be importing from Kafka to the source system and then from HDFS to Kafka, which is the wrong direction.
- 3 and 4 use the same connector type twice, which doesn't make sense for moving data from a source to Kafka to a sink.

</details>

## 🚫 Question 28

You are using a JDBC source connector to copy data from a database table to a Kafka topic. The table has 5 columns. How many tasks will be created by the connector?

- 1. 1
- 2. 5
- 3. It depends on the `tasks.max` configuration of the connector
- 4. It depends on the number of partitions in the Kafka topic

<details>
<summary>Response:</summary> 

**Answer:** 1

**Explanation:**
The JDBC source connector parallelizes by table: each table is assigned to one task, so a single table is always copied by exactly one task, regardless of the number of columns or of `tasks.max`.

- 2 is incorrect because the number of tasks is not determined by the number of columns in the table.
- 3 is incorrect for a single table: `tasks.max` is only an upper limit, and the connector creates at most one task per table (the connector may create fewer tasks than `tasks.max`).
- 4 is incorrect because the number of tasks is not related to the number of partitions in the Kafka topic.

</details>

## Question 29

What happens if the `tasks.max` configuration is set to a value less than the number of tables being copied by a JDBC source connector?

1. The connector will create one task per table, ignoring the `tasks.max` setting
2. The connector will create tasks up to the `tasks.max` limit, potentially leaving some tables without dedicated tasks
3. The connector will distribute the tables evenly among the available tasks
4. The connector will fail with an error due to the insufficient number of tasks

<details>
<summary>Response:</summary> 

**Answer:** 3

**Explanation:**
When the `tasks.max` configuration is set to a value less than the number of tables being copied by a JDBC source connector, the connector will distribute the tables evenly among the available tasks.

Key points:
- The connector respects the `tasks.max` setting and creates up to that number of tasks.
- All tables are processed; no tables are left without tasks.
- Tables are assigned to tasks in a way that balances the load.
- Each task will handle multiple tables, processing them sequentially.

Example:
If there are 10 tables and `tasks.max` is set to 5:
- The connector creates 5 tasks.
- Each task is assigned 2 tables.
- All tables are processed, and the workload is distributed evenly among the tasks.

This approach ensures that all data is ingested into Kafka, maintaining data integrity and completeness while respecting the `tasks.max` limit.

</details>

##  Question 30

How can you increase the parallelism of a JDBC source connector to improve the performance of copying data from a database to Kafka?

1. Increase the `tasks.max` configuration of the connector
2. Increase the number of partitions in the target Kafka topic
3. Increase the `tasks.max` configuration of the Kafka Connect workers (workers have no such setting)
4. Use multiple instances of the JDBC connector, each copying a different subset of tables

<details>
<summary>Response:</summary> 

**Answer:** 1 and 4

**Explanation:**
To increase the parallelism of a JDBC source connector and improve performance, you can use a combination of approaches:

1. Increase the `tasks.max` configuration of the connector:
   - This allows the connector to create more tasks within a single instance, but only up to one task per table (it does not help when copying a single table).
   - Each task can process data independently, increasing parallelism.

4. Use multiple instances of the JDBC connector, each copying a different subset of tables:
   - Distributes the workload across multiple connector instances.
   - Each instance can run tasks in parallel, further enhancing performance.

Combining both options can maximize parallelism and performance, although it's important to manage the complexity that comes with multiple connector instances.

Additional notes:
- Option 2 (increasing partitions) can help with downstream consumer parallelism but doesn't directly affect the connector's parallelism.
- Option 3 is incorrect: `tasks.max` is a connector-level setting, not a worker setting. Adding more workers only spreads existing tasks across more machines.
</details>

## Question 31

What information about Kafka Connect tasks is NOT stored in the `connect-status` topic?

- 1. The connector and task configurations
- 2. The current status of each connector and task (running, failed, paused, etc.)
- 3. The offsets processed by each connector
- 4. The worker node each task is assigned to


<details>
<summary>Response:</summary> 

**Answer:** 1 and 3

**Explanation:**
The `connect-status` topic in Kafka is used by Kafka Connect to store status information about connectors and tasks. However, it does not store the actual configurations of the connectors and tasks.

- 1: Connector and task configurations are stored in the `connect-configs` topic, not in `connect-status`.
- 2, 4: The current status (and the worker ID) of each connector and task for each connector and task is indeed stored in `connect-status`.
- 3: Offsets are not stored in `connect-status` either. Source connector offsets are stored in the `connect-offsets` topic (`offset.storage.topic`), and sink connector offsets are stored as regular consumer group offsets.

</details>

## Question 32

You have a Kafka cluster with 5 brokers and a topic with 10 partitions. You want to consume messages from this topic using a consumer group with 3 consumers. What is the maximum number of partitions that can be assigned to a single consumer?

- 1. 3
- 2. 4
- 3. 5
- 4. 10

<details>
<summary>Response:</summary> 

**Answer:** 2

**Explanation:**
In a Kafka consumer group, the partitions of a topic are distributed among the available consumers to achieve parallel consumption. The maximum number of partitions that can be assigned to a single consumer depends on the total number of partitions and the number of consumers in the group.

When there are more partitions than consumers, Kafka will distribute the partitions as evenly as possible among the consumers. In this case, with 10 partitions and 3 consumers, the distribution will be as follows:

- Consumer 1: 4 partitions
- Consumer 2: 3 partitions
- Consumer 3: 3 partitions

Therefore, the maximum number of partitions that can be assigned to a single consumer is 4.

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (partition assignment, Range/RoundRobin assignors); this is generic consumer-group behaviour (also applies to Connect sink tasks, which form a consumer group `connect-<name>`).

If there were fewer partitions than consumers, some consumers would be idle and not receive any partitions. For example, if there were 5 consumers and 10 partitions, each consumer would be assigned 2 partitions, and no consumer would have more than 2 partitions.

It's important to note that the actual partition assignment may vary based on factors such as the partition assignment strategy and the current state of the consumer group. However, in general, Kafka aims to distribute the partitions evenly among the available consumers to ensure balanced consumption.

</details>

## Question 33

You have a Kafka cluster with 3 brokers and a topic with 12 partitions. You want to create a consumer group with 4 consumers to consume messages from this topic. How many consumers will be actively consuming messages?

- 1. 1
- 2. 3
- 3. 4
- 4. 12

<details>
<summary>Response:</summary> 

**Answer:** 3

**Explanation:**
In a Kafka consumer group, the number of active consumers depends on the number of partitions in the topic and the number of consumers in the group. Kafka assigns partitions to consumers in a way that ensures each partition is consumed by exactly one consumer in the group.

Consumers beyond the number of partitions would be idle. In this case, with 12 partitions and 4 consumers, all 4 consumers will be actively consuming messages.

Here's how the partition assignment will work:

- Consumer 1: Assigned 3 partitions
- Consumer 2: Assigned 3 partitions
- Consumer 3: Assigned 3 partitions
- Consumer 4: Assigned 3 partitions

Source: Kafka: The Definitive Guide 2nd ed., ch. 4 (consumers beyond the partition count sit idle); https://kafka.apache.org/43/documentation/#intro_consumers

Each consumer will be responsible for consuming messages from its assigned partitions. Since there are more partitions than consumers, each consumer will have an equal share of the partitions and will be actively consuming messages.

If there were fewer partitions than consumers, some consumers would be idle. For example, if there were 3 partitions and 4 consumers, only 3 consumers would be actively consuming messages, and 1 consumer would be idle.

It's important to note that the actual partition assignment may vary based on factors such as the partition assignment strategy and the current state of the consumer group. However, in general, Kafka aims to distribute the partitions evenly among the available consumers to ensure balanced consumption.

</details>

## Question 34

What is the purpose of the `connect-offsets` topic in Kafka Connect?

- 1. It stores the configuration of the connectors.
- 2. It stores the status of the connector tasks.
- 3. It stores the offsets of the source connectors.
- 4. It stores the offsets of the sink connectors.

<details>
<summary>Response:</summary> 

**Answer:** 3

**Explanation:**
In Kafka Connect, the `connect-offsets` topic is used to store the offsets of the source connectors. It plays a crucial role in enabling fault tolerance and recovery of connector tasks.

Here's how the `connect-offsets` topic is used:

1. Offset Tracking:
   - When a source connector reads data from an external system, it keeps track of the offsets or positions of the data it has processed.
   - The connector periodically writes these offsets to the `connect-offsets` topic.
   - Each record in the `connect-offsets` topic represents an offset for a specific partition or data source.

2. Fault Tolerance:
   - If a connector task fails or is restarted, Kafka Connect uses the offsets stored in the `connect-offsets` topic to resume data processing from the last committed offset.
   - By default this gives at-least-once delivery (a few records may be re-delivered after a failure); exactly-once for source connectors requires `exactly.once.source.support` on the workers (Kafka 3.3+) and connector support.

3. Connector Recovery:
   - When a connector is restarted or a new connector task is created, it reads the offsets from the `connect-offsets` topic to determine the starting position for data processing.
   - By using the stored offsets, the connector can pick up from where it left off and continue processing data without starting from scratch.

The offsets topic (named by `offset.storage.topic`, conventionally `connect-offsets`) is used in distributed mode (standalone mode uses a file, `offset.storage.file.filename`) and is created by the worker on startup if it does not exist (manual creation is recommended to control partitions and replication). It is an internal topic managed by Kafka Connect and should not be modified or consumed by external applications.

It's important to note that the `connect-offsets` topic is specific to source connectors. Sink connectors, which write data to external systems, do not use this topic; they track progress with regular consumer group offsets (option 4).

The `connect-configs` topic (option 1) is used to store the configuration of the connectors, while the `connect-status` topic (option 2) stores the status of the connector tasks. These are separate topics from `connect-offsets`.

</details>

## Question 35

How does Kafka Connect handle the scalability of connectors?

- 1. By automatically creating multiple instances of a connector based on the load.
- 2. By allowing manual configuration of the number of tasks for each connector.
- 3. By dynamically adjusting the number of tasks based on the connector's performance.
- 4. By requiring a separate Kafka Connect cluster for each connector.

<details>
<summary>Response:</summary> 

**Answer:** 2

**Explanation:**
Kafka Connect provides scalability for connectors by allowing manual configuration of the number of tasks for each connector. This enables you to scale the processing of a connector based on your specific requirements and the characteristics of the data being processed.

Here's how Kafka Connect handles connector scalability:

1. Connector Configuration:
   - When deploying a connector, you can specify the `tasks.max` parameter in the connector configuration.
   - The `tasks.max` parameter determines the maximum number of tasks that can be created for the connector.

2. Task Allocation:
   - Kafka Connect distributes the work of a connector across multiple tasks.
   - Each task is responsible for processing a subset of the data handled by the connector.
   - The number of tasks created for a connector is determined by the `tasks.max` configuration and the partitioning of the data.

3. Scalability:
   - By increasing the `tasks.max` value, you can scale the processing of a connector to handle higher throughput or process data from multiple partitions in parallel.
   - Kafka Connect automatically distributes the tasks across the available Kafka Connect worker nodes in the cluster.
   - Each task runs independently and processes its assigned subset of data, allowing for parallel processing and increased overall throughput.

4. Resource Utilization:
   - The number of tasks for a connector should be chosen based on the available resources (CPU, memory) in the Kafka Connect cluster.
   - Each task consumes resources on the worker node where it is running.
   - It's important to balance the number of tasks with the available resources to avoid overloading the Kafka Connect cluster.

Kafka Connect does not automatically create multiple instances of a connector based on the load (option 1) or dynamically adjust the number of tasks based on the connector's performance (option 3). The number of tasks is manually configured using the `tasks.max` parameter.

Additionally, Kafka Connect does not require a separate cluster for each connector (option 4). Multiple connectors can run within the same Kafka Connect cluster, and the tasks of different connectors can be distributed across the available worker nodes.

</details>

## Question 36

What happens when a Kafka Connect worker node fails in a distributed Kafka Connect cluster?

- 1. All the connectors and tasks running on the failed worker node are permanently lost.
- 2. The connectors and tasks are automatically redistributed to the remaining worker nodes.
- 3. The failed worker node is replaced with a new worker node, and the tasks are reassigned.
- 4. The entire Kafka Connect cluster goes down until the failed worker node is restored.

<details>
<summary>Response:</summary> 

**Answer:** 2

**Explanation:**
In a distributed Kafka Connect cluster, when a worker node fails, Kafka Connect automatically redistributes the connectors and tasks running on the failed node to the remaining active worker nodes in the cluster. This ensures fault tolerance and continued operation of the connectors and tasks.

Here's what happens when a Kafka Connect worker node fails:

1. Worker Node Failure Detection:
   - Kafka Connect uses a heartbeat mechanism to detect worker node failures.
   - Each worker node periodically sends heartbeats to the Kafka Connect cluster to indicate its health and availability.
   - If a worker node fails to send heartbeats within `session.timeout.ms`, it is considered dead.

2. Task Rebalancing:
   - When a worker node failure is detected, Kafka Connect triggers a rebalancing process.
   - The connectors and tasks that were running on the failed worker node are redistributed among the remaining active worker nodes in the cluster (with incremental cooperative rebalancing, reassignment may be delayed up to `scheduled.rebalance.max.delay.ms`, default 5 minutes, to allow the worker to return).
   - Source tasks resume from the offsets in the `connect-offsets` topic, and sink tasks resume from their committed consumer group offsets.

3. Connector and Task Reassignment:
   - The redistributed connectors and tasks are assigned to the available worker nodes based on the current load and capacity of each node.
   - Kafka Connect aims to evenly distribute the workload across the cluster to ensure optimal performance and resource utilization.
   - The reassignment process is transparent to the connectors and tasks, and they continue processing data from where they left off.

4. Continuous Operation:
   - After the rebalancing and reassignment process is complete, the Kafka Connect cluster continues operating with the remaining worker nodes.
   - The connectors and tasks that were previously running on the failed worker node are now running on the active worker nodes.
   - Kafka Connect ensures that data processing continues without interruption, maintaining the overall functionality and reliability of the system.

It's important to note that the connectors and tasks are not permanently lost when a worker node fails (option 1). Kafka Connect's fault tolerance mechanisms ensure that they are redistributed and continue running on the available worker nodes.

The failed worker node is not automatically replaced with a new worker node (option 3). Instead, the workload is redistributed among the existing worker nodes in the cluster.

The failure of a single worker node does not bring down the entire Kafka Connect cluster (option 4). The cluster remains operational, and the workload is redistributed to maintain continuous operation.

</details>

