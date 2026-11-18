> 🚫 = outside the CCDAK exam scope (see exam blueprint)

## 🚫 Question 1

Where are the ACLs stored in a Kafka cluster by default at Zookeeper mode cluster?

- A. In the Kafka topic `_acls`
- B. Inside the broker's data directory  
- C. In Zookeeper node `/kafka-acl/`
- D. In a separate ACL server

<details>
<summary>Response:</summary> 

**Answer:** C

**Explanation:**
ACLs are stored in Zookeeper by default under the `/kafka-acl/` znode. This allows all brokers to access the ACL information in a consistent manner.

- A is incorrect because there is no `_acls` topic used for storing ACLs.
- B is incorrect as ACLs are not stored on the broker's data directories.
- D is incorrect because there is no separate ACL server. ACLs are managed within the Kafka cluster itself.

Note: 
ZooKeeper mode is removed in Kafka 4.0 (KIP-500). In KRaft clusters, ACLs are stored in the cluster metadata log (the `__cluster_metadata` internal topic, managed by the controllers) and enforced by `StandardAuthorizer`. See Question 5.

</details>

## 🚫 Question 2

What Kafka CLI command can be used to add new ACL rules to a running Kafka cluster?

- A. `kafka-acls.sh`
- B. `kafka-configs.sh`
- C. `kafka-topics.sh`
- D. `kafka-console-producer.sh`

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `kafka-acls.sh` CLI tool is used to manage ACLs in Kafka. It allows adding, removing or listing ACL rules in a running cluster.

- B is used for altering configs, not ACLs.
- C is used for managing topics, not ACLs.
- D is used for producing messages, not managing ACLs.

</details>

## Question 3

Which of the following is NOT a valid resource type when defining ACLs in Kafka?

- A. Topic
- B. Consumer Group
- C. Cluster
- D. Partition

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
In Kafka, ACLs can be defined for resource types like Topic, Consumer Group, Cluster, and others. However, Partition is not a valid resource type for defining ACLs.

- A, B, C are all valid resource types for ACLs.
- D is invalid because ACLs are defined at the topic level, not individual partition level. The topic resource type covers all its partitions. (Other valid resource types: TransactionalId, DelegationToken, User.)


</details>

## Question 4

What is the purpose of ACLs (Access Control Lists) in Kafka?

- A. To encrypt messages for secure communication between clients and brokers
- B. To authorize their access to Kafka resources
- C. To compress messages for efficient storage and transmission
- D. To validate the schema of messages produced to Kafka topics

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
ACLs (Access Control Lists) in Kafka are used to authorize (not authenticate) the access of authenticated principals to
Kafka resources. Authentication itself is done by SSL/mTLS or SASL; the resulting principal is then checked against the ACLs.
Option B. They provide a mechanism to control and restrict the actions that clients can
perform on Kafka brokers, topics, and other resources. ACLs allow you to define permissions for specific users or groups, 
specifying which operations they are allowed to perform on particular resources. By configuring ACLs, you can enforce security
policies and ensure that clients have the appropriate privileges to access and interact with Kafka. ACLs help in securing Kafka 
clusters by preventing unauthorized access and protecting sensitive data. They are a key component of Kafka's security model, 
along with other features like authentication and encryption.



</details>

## 🚫 Question 5

How are ACLs stored and managed in Kafka for KRaft mode?

- A. ACLs are stored in a Controller node's local file system and managed using Kafka command-line tools
- B. ACLs are stored in the `__cluster_metadata` topic and managed using Kafka command-line tools
- C. ACLs are stored in a dedicated ACL server and managed through a REST API
- D. ACLs are stored in the Kafka broker's local file system and managed using configuration files

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
The default authorizer (for ZooKeeper Kafka) is `AclAuthorizer`, which you specify in each broker's configuration: ``authorizer.class.name=kafka.security.authorizer.AclAuthorizer``.
However, if you are using Kafka's native consensus implementation based on KRaft then you'll use a new built-in ``StandardAuthorizer`` (``authorizer.class.name=org.apache.kafka.metadata.authorizer.StandardAuthorizer``) that doesn't depend on ZooKeeper. ZooKeeper and ``AclAuthorizer`` are removed in Kafka 4.0.
``StandardAuthorizer`` accomplishes all of the same things that ``AclAuthorizer`` does for ZooKeeper-dependent clusters, and it stores its ACLs in the ``__cluster_metadata`` metadata topic.
See [Confluent course on authorization](https://developer.confluent.io/courses/security/authorization/#:~:text=it%20stores%20its%20ACLs%20in%20the%20__cluster_metadata%20metadata%20topic)

</details>

## Question 6

What happens when a client tries to perform an operation that is not allowed by the configured ACLs?

- A. The operation is performed, but a warning is logged in the Kafka broker logs
- B. The operation is rejected, and the client receives an authorization error
- C. The operation is performed, but the message is flagged as unauthorized
- D. The operation is delayed until the necessary ACLs are added

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
When a client tries to perform an operation that is not allowed by the configured ACLs, the operation is rejected, and the client receives an authorization error. Kafka brokers enforce the ACLs by checking the permissions of the client against the requested operation and resource. If the client does not have the necessary privileges, the broker denies the operation and returns an authorization error to the client. The client can then handle the error accordingly, such as logging the failure, retrying with different credentials, or propagating the error to the application. The unauthorized operation is not performed, and no data is processed or modified. This behavior ensures that Kafka maintains the integrity and security of the system by strictly enforcing the defined access control rules.

</details>

## Question 7

What is the purpose of the `CreateTopics` ACL operation in Kafka?

- A. To allow a client to create new topics in a Kafka cluster
- B. To permit a client to produce messages to a specific topic
- C. To grant a client permission to delete topics from a Kafka cluster
- D. To enable a client to modify the configuration of existing topics

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
The `CreateTopics` ACL operation in Kafka is used to allow a client to create new topics in a Kafka cluster. When a client has been granted the `CreateTopics` permission, it is authorized to send requests to the Kafka brokers to create new topics. This ACL operation is typically assigned to administrative clients or applications responsible for managing the topic lifecycle in a Kafka cluster. When an authorizer is configured, brokers require the `Create` permission (on the Cluster, or on matching Topic resources) for any client creating a topic (the `CreateTopics` API; in ACL terms the operation is named `Create`). This ensures that only authorized clients can create topics and helps maintain control over the topic management process in the cluster.

</details>

## Question 8

What is the difference between `Read` and `Write` ACL operations in Kafka?

- A. `Read` allows consuming messages, while `Write` allows producing messages
- B. `Read` allows producing messages, while `Write` allows consuming messages
- C. `Read` allows modifying topic configurations, while `Write` allows deleting topics
- D. `Read` and `Write` are equivalent and can be used interchangeably

<details>
<summary>Response:</summary> 

**Answer:** A

**Explanation:**
In Kafka, the `Read` ACL operation allows a client to consume messages from a specific topic, while the `Write` ACL operation allows a client to produce messages to a specific topic. The `Read` permission grants the client the ability to read and fetch messages from the topic, including the metadata required for consumption. On the other hand, the `Write` permission authorizes the client to send messages to the topic and update its content. It's important to note that `Read` and `Write` operations are distinct and serve different purposes. A client with `Read` permission cannot produce messages, and a client with `Write` permission cannot consume messages. The permissions are specific to the respective operations and should be granted based on the client's intended actions.

</details>

## Question 9

How can you grant a client permission to describe topics and consumer groups in a Kafka cluster?

- A. Assign the `DescribeConfigs` ACL operation to the client
- B. Grant the `Describe` ACL operation to the client
- C. Provide the `AlterConfigs` ACL operation to the client
- D. Give the `IdempotentWrite` ACL operation to the client

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
To grant a client permission to describe topics and consumer groups in a Kafka cluster, you need to assign the `Describe` ACL operation to the client. The `Describe` permission allows a client to view the metadata and details of topics and consumer groups without the ability to modify or delete them. With the `Describe` ACL, a client can send requests to the Kafka brokers to retrieve information such as the list of partitions and replica assignments for topics (reading topic configuration values requires `DescribeConfigs`). It can also query the state and membership of consumer groups. The `Describe` ACL is commonly used by monitoring and administrative tools to gather information about the Kafka cluster's state without making any changes to the topics or consumer groups.

</details>

## Question 10 [x]

What is the purpose of the `ssl.keystore.location` and `ssl.keystore.password` configurations in Kafka?

- A. To specify the location and password of the truststore for verifying client certificates
- B. To specify the location and password of the keystore for broker authentication
- C. To specify the location and password of the keystore for client authentication
- D. To specify the location and password of the truststore for broker authentication

<details>
<summary>Response:</summary> 

**Answer:** B

**Explanation:**
In Kafka, the `ssl.keystore.location` and `ssl.keystore.password` configurations are used to specify the location and password of the keystore for broker authentication. When SSL/TLS is enabled for inter-broker communication or client-broker communication, each Kafka broker needs to have a keystore that contains its private key and certificate. The `ssl.keystore.location` configuration points to the file path of the keystore on the broker's file system, while the `ssl.keystore.password` configuration provides the password required to access the keystore. These configurations are essential for setting up SSL/TLS authentication on the broker side, allowing the broker to securely authenticate itself to clients and other brokers.

</details>

## Question 11

What is the role of the `ssl.truststore.location` and `ssl.truststore.password` configurations in Kafka?

- A. To specify the location and password of the keystore for storing the broker's private key
- B. To specify the location and password of the truststore for storing trusted client certificates
- C. To specify the location and password of the keystore for storing trusted broker certificates
- D. To specify the location and password of the truststore for verifying broker certificates

<details>
<summary>Response:</summary> 

**Explanation:**

The `ssl.truststore.location` and `ssl.truststore.password` configurations in Kafka are used to specify the location and password of the truststore for verifying broker certificates. In an SSL/TLS setup, the truststore contains the trusted CA (or broker) certificates. On a broker with mutual TLS it likewise holds the CAs that sign client certificates. When a client or another broker establishes a secure connection to a Kafka broker, it uses the certificates in the truststore to verify the identity of the broker. The `ssl.truststore.location` configuration specifies the file path of the truststore on the client or broker's file system, and the `ssl.truststore.password` configuration provides the password needed to access the truststore. These configurations are crucial for enabling trust verification and ensuring secure communication between clients and brokers.

**Answer:** D

</details>

##  Question 12

How can you enable SSL/TLS encryption for communication between Kafka brokers?

- A. Set `ssl.enabled.protocols` to `SSL` in the broker configuration
- B. Set `security.inter.broker.protocol` to `SSL` in the broker configuration
- C. Set `ssl.client.auth` to `required` in the broker configuration
- D. Set `ssl.endpoint.identification.algorithm` to `HTTPS` in the broker configuration

<details>
<summary>Response:</summary> 

**Explanation:**

To enable SSL/TLS encryption for communication between Kafka brokers, you need to set the `security.inter.broker.protocol` configuration to `SSL` in the broker configuration. By default, Kafka brokers communicate with each other using plaintext. By setting `security.inter.broker.protocol` to `SSL`, you instruct the brokers to use SSL/TLS encryption for inter-broker communication. This ensures that all data exchanged between brokers, including replication traffic, is encrypted. (In KRaft mode, controller traffic uses the separate listener named in `controller.listener.names`, whose protocol is mapped in `listener.security.protocol.map`.) When enabling SSL/TLS for inter-broker communication, you also need to configure the appropriate SSL/TLS settings, such as the keystore and truststore locations and passwords, to establish secure connections between the brokers.

**Answer:** B

</details>

## Question 13 [x]

What is the purpose of the `ssl.client.auth` configuration in Kafka?

- A. To specify the SSL/TLS protocol version to be used for client authentication
- B. To enable or disable SSL/TLS encryption for client connections
- C. To configure the client authentication mode (none, requested, or required)
- D. To set the location of the client certificate for authentication

<details>
<summary>Response:</summary> 

**Explanation:**

The `ssl.client.auth` configuration in Kafka is used to configure the client authentication mode when SSL/TLS is enabled. It determines how the Kafka broker handles client authentication during the SSL/TLS handshake process. The `ssl.client.auth` configuration can be set to one of three values:

- `none`: Client authentication is not required. The broker does not request or verify client certificates.
- `requested`: Client authentication is optional. The broker requests client certificates but does not require them. If a client provides a certificate, it will be verified.
- `required`: Client authentication is mandatory. The broker requires clients to provide a valid certificate for authentication.

By configuring `ssl.client.auth`, you can enforce the desired level of client authentication security (mutual TLS) in your Kafka cluster.

```
ssl.client.auth         → authentication mode (none/required/mandatory)
ssl.enabled.protocols   → TLS versions (TLSv1.2, TLSv1.3)
ssl.keystore.location   → path to the keystore
ssl.truststore.location → path to the truststore
ssl.key.password        → private key password
security.protocol       → Enable/disable SSL encryption (PLAINTEXT / SSL / SASL_PLAINTEXT / SASL_SSLL)
```

**Answer:** C

**Area:** Security

</details>

## Question 14

What happens when `ssl.client.auth` is set to `required` in the Kafka broker configuration?

- A. Clients are required to provide a valid certificate for authentication
- B. Clients can choose to provide a certificate optionally
- C. Client authentication is disabled, and no certificates are requested
- D. The broker uses the default SSL/TLS protocol version for client authentication

<details>
<summary>Response:</summary> 

**Explanation:**

When the `ssl.client.auth` configuration is set to `required` in the Kafka broker configuration, clients are required to provide a valid certificate for authentication. In this mode, the Kafka broker enforces mandatory client authentication during the SSL/TLS handshake process. When a client establishes a connection to the broker, the broker requests the client's certificate and verifies its validity against the trusted certificates stored in the broker's truststore. Only clients with a valid and trusted certificate are allowed to proceed with the connection. If a client fails to provide a certificate or provides an invalid certificate, the connection is rejected. Setting `ssl.client.auth` to `required` ensures that all clients connecting to the Kafka cluster are authenticated and trusted.

**Answer:** A

</details>

## 🚫\ Question 15

What is the default value of the `ssl.client.auth` configuration in Kafka?

- A. `none`
- B. `requested`
- C. `required`
- D. `optional`

<details>
<summary>Response:</summary> 

**Explanation:**

The default value of the `ssl.client.auth` configuration in Kafka is `none`. When `ssl.client.auth` is not explicitly set in the Kafka broker configuration, it assumes the default value of `none`. In this mode, client authentication is not required, and the Kafka broker does not request or verify client certificates during the SSL/TLS handshake process. Clients can establish connections to the broker without providing any authentication credentials. This default behavior prioritizes simplicity and ease of use but does not enforce client authentication. If you need to enable client authentication, you must explicitly set `ssl.client.auth` to `requested` or `required` in the broker configuration.

**Answer:** A

</details>

## Question 16

What is the purpose of the `sasl.kerberos.service.name` configuration in Kafka?

- A. To specify the Kerberos principal name for the Kafka broker
- B. To set the Kerberos realm for SASL authentication
- C. To configure the Kerberos key distribution center (KDC) hostname
- D. To define the service name used by Kafka brokers for SASL authentication

<details>
<summary>Response:</summary> 

**Explanation:**

The `sasl.kerberos.service.name` configuration in Kafka is used to define the service name used by Kafka brokers for SASL authentication when Kerberos is enabled. In a Kerberos-based SASL authentication setup, Kafka clients and brokers use Kerberos tickets to authenticate with each other. The `sasl.kerberos.service.name` configuration specifies the Kerberos principal name (the service part of `kafka/host@REALM`) that Kafka runs as. Clients set it to know which service principal to request a ticket for; brokers set it to their own service name. This service name is typically set to `kafka` but can be customized based on your Kerberos setup. It is important to ensure that the service name configured in Kafka matches the service name used in the Kerberos principal and keytab files for the Kafka brokers.

**Answer:** D

</details>

## Question 17

What is the role of the `sasl.jaas.config` configuration in Kafka SASL authentication?

- A. To specify the JAAS login module and its options inline in the Kafka configuration, instead of a separate JAAS file
- B. To set the SASL mechanism to be used for authentication (e.g., PLAIN, SCRAM)
- C. To configure the SASL client and server callbacks for authentication
- D. To enable or disable SASL authentication in Kafka

<details>
<summary>Response:</summary> 

**Explanation:**

The `sasl.jaas.config` configuration in Kafka is used to specify the JAAS (Java Authentication and Authorization Service) configuration for SASL authentication. JAAS is a pluggable authentication framework used by Kafka to configure and handle authentication mechanisms. The `sasl.jaas.config` configuration allows you to provide the necessary authentication details, such as the login module, principal, and credentials, directly in the Kafka configuration. It eliminates the need for a separate JAAS configuration file. The value of `sasl.jaas.config` is a string that represents the JAAS configuration, including the login module class, principal, and any additional options required for authentication. It is a convenient way to configure SASL authentication settings directly in the Kafka broker or client configuration (per listener/mechanism on brokers). B is `sasl.mechanism`, C is `sasl.login.callback.handler.class` / `sasl.client.callback.handler.class`, and D is controlled by the listener's security protocol.

**Answer:** A

</details>

## Question 18

What is the purpose of the `sasl.mechanism` configuration in Kafka SASL authentication?

- A. To specify the SASL mechanism to be used for authentication (e.g., PLAIN, SCRAM)
- B. To configure the SASL client and server callbacks for authentication
- C. To set the path to the JAAS configuration file for SASL authentication
- D. To enable or disable SASL authentication in Kafka

<details>
<summary>Response:</summary> 

**Explanation:**

The `sasl.mechanism` configuration in Kafka is used to specify the SASL mechanism to be used for authentication. SASL (Simple Authentication and Security Layer) is a framework that provides authentication and optional encryption for network protocols. Kafka supports multiple SASL mechanisms, such as PLAIN, SCRAM (Salted Challenge Response Authentication Mechanism), and GSSAPI (Kerberos). The `sasl.mechanism` configuration allows you to choose the specific SASL mechanism that Kafka should use for authentication. For example, setting `sasl.mechanism=PLAIN` configures Kafka to use the PLAIN mechanism, which transmits credentials in plaintext. Setting `sasl.mechanism=SCRAM-SHA-256` configures Kafka to use the SCRAM mechanism with SHA-256 hashing for secure password-based authentication. The available SASL mechanisms depend on the Kafka version and the security libraries installed.

**Answer:** A

</details>

## Question 19

What security protocol does Kafka use by default for communication between clients and brokers?

- A. SSL/TLS
- B. SASL_PLAINTEXT
- C. PLAINTEXT
- D. SASL_SSL

<details>
<summary>Response:</summary> 

**Explanation:**

By default, Kafka uses the PLAINTEXT security protocol for communication between clients and brokers. The PLAINTEXT protocol does not provide any encryption or authentication and sends data in plain text over the network. It is the simplest and most basic security protocol in Kafka, offering no security measures out of the box. While PLAINTEXT is the default protocol, it is not recommended for production environments or sensitive data transmission. Instead, it is strongly advised to use more secure protocols like SSL/TLS (SSL) or SASL (SASL_PLAINTEXT or SASL_SSL) to ensure data confidentiality, integrity, and authentication between clients and brokers.

**Answer:** C

</details>

## Question 20 [x]

Which security protocol in Kafka provides encryption for data in transit but does not offer authentication?

- A. PLAINTEXT
- B. SASL_PLAINTEXT
- C. SSL
- D. SASL_SSL


<details>
<summary>Response:</summary> 

**Explanation:**

In Kafka, the SSL security protocol provides encryption for data in transit between clients and brokers; by default (`ssl.client.auth=none`) it does not authenticate clients (the client only verifies the broker certificate). When the SSL protocol is used, all the data exchanged between clients and brokers is encrypted using SSL/TLS, ensuring confidentiality and integrity of the data. However, SSL alone does not handle authentication of the clients or brokers. It focuses solely on encrypting the communication channel. To add client authentication you can either set `ssl.client.auth=required` (mutual TLS with client certificates) or use the SASL_SSL protocol, which combines SSL encryption with SASL authentication (PLAIN, SCRAM, GSSAPI/Kerberos, OAUTHBEARER). Of the options, SSL is the expected answer.

**Answer:** C

## Question 21

Which security protocol in Kafka provides both encryption and authentication for client-broker communication?

- A. PLAINTEXT
- B. SASL_PLAINTEXT
- C. SSL
- D. SASL_SSL

<details>
<summary>Response:</summary> 

**Answer:** D

**Explanation:**
The SASL_SSL security protocol in Kafka provides both encryption and authentication for client-broker communication. SASL_SSL combines the benefits of SSL/TLS encryption with SASL authentication mechanisms. When SASL_SSL is used, the data exchanged between clients and brokers is encrypted using SSL/TLS, ensuring confidentiality and integrity. Additionally, SASL authentication is employed to authenticate the clients and brokers. SASL (Simple Authentication and Security Layer) supports various authentication mechanisms, such as PLAIN, SCRAM, and GSSAPI (Kerberos). By using SASL_SSL, you can achieve both encryption and authentication in a single protocol, providing a high level of security for your Kafka cluster.

</details>
