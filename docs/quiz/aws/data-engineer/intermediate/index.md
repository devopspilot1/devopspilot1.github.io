---
title: "AWS Data Engineer Quiz – Intermediate"
---

# AWS Data Engineer - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers performance optimization in S3 and Redshift, streaming architectures, and handling schema changes.

---

<quiz>
How do you optimize S3 performance for high request rates (thousands of PUT/GET per second)?
- [x] Use multiple prefixes (folder paths) to parallelize the requests, as S3 scaling is partition-based per prefix.
- [ ] Use a single folder for everything.
- [ ] Use Standard-IA storage class.
- [ ] Disable versioning.

S3 scales automatically, but using distinct prefixes allows it to scale partitions horizontally for massive throughput.
</quiz>

<quiz>
What is the "Small File Problem" in Hadoop/Spark/Athena?
- [x] Performance degradation caused by excessive metadata overhead when processing thousands of tiny files (KB size).
- [ ] Files being too small to read.
- [ ] Files being lost.
- [ ] S3 running out of inodes.

Query engines spend more time listing files and opening connections than reading data. Solution: Compact files into larger chunks (e.g., 128MB).
</quiz>

<quiz>
When should you choose Amazon EMR over AWS Glue?
- [x] When you need massive, long-running, complex jobs where you require full control over the cluster configuration and software tuning.
- [ ] For simple ETL jobs.
- [ ] When you want serverless.
- [ ] When you have no budget.

EMR gives you "root" access to the cluster, ideal for specific Hadoop/Spark tuning or custom binaries.
</quiz>

<quiz>
What is "Partitioning" in the context of Athena/S3?
- [x] Organizing data into folders (e.g., `year=2024/month=01`) so queries scan only relevant data subsets.
- [ ] Cutting a hard drive in half.
- [ ] Splitting a CSV file by rows.
- [ ] Using RAID.

Partitioning dramatically reduces cost and improves speed by preventing full table scans.
</quiz>

<quiz>
Which distribution style in Redshift optimizes for joins between two large tables?
- [x] KEY (Distribute based on the Join column).
- [ ] ALL.
- [ ] EVEN.
- [ ] RANDOM.

colocating rows with matching keys on the same node minimizes network shuffle during the join operation.
</quiz>

<quiz>
How do you handle schema evolution (e.g., adding a new column) in a Parquet-based data lake?
- [x] Parquet supports schema evolution; you can add the column and use Glue Schema Registry to validate compatibility.
- [ ] You must rewrite all historical data.
- [ ] You cannot change the schema.
- [ ] Use a CSV file instead.

Columnar formats like Parquet and Avro are designed to handle schema add/remove gracefully.
</quiz>

<quiz>
What is the main difference between Amazon QuickSight and Tableau on EC2?
- [x] QuickSight is serverless and auto-scaling; Tableau on EC2 requires infrastructure management.
- [ ] QuickSight is harder to use.
- [ ] Tableau cannot connect to Redshift.
- [ ] QuickSight is free.

QuickSight is native to AWS and charges per session/user without server admin overhead.
</quiz>

<quiz>
How do you securely connect QuickSight to a private RDS instance?
- [x] Connect QuickSight to the VPC; it creates an ENI to access private subnets.
- [ ] Make the RDS public.
- [ ] Use a bastion host.
- [ ] Use a VPN.

Attaching QuickSight to the VPC allows it to route traffic to internal IPs securely.
</quiz>

<quiz>
Which service is used to orchestrate complex data workflows involving dependencies (e.g., Lambda -> Glue -> Redshift)?
- [x] AWS Step Functions (or MWAA).
- [ ] S3 Event Notifications.
- [ ] CloudWatch Alarms.
- [ ] SNS.

Step Functions provides a state machine to manage retries, parallel branches, and error handling for critical pipelines.
</quiz>

<quiz>
What is the role of the "Sort Key" in Redshift?
- [x] It determines the order in which data is stored on disk, optimizing range queries and filtering.
- [ ] It sorts the output of a SELECT query.
- [ ] It encrypts the data.
- [ ] It distributes data across nodes.

Zone maps allow Redshift to skip blocks that don't fall within the requested Sort Key range, speeding up queries.
</quiz>

<quiz>
If you need to query logs in S3 but only care about records with "ERROR", how can you avoid scanning the whole file?
- [x] Use S3 Select (or convert to Parquet and filter).
- [ ] Download the file and grep it.
- [ ] Use Glacier.
- [ ] Use CloudFront.

S3 Select allows you to retrieve only a subset of data from an object by using simple SQL expressions.
</quiz>

<quiz>
What is key difference between "Stream Processing" and "Batch Processing"?
- [x] Stream processing deals with continuous data in real-time; Batch processing deals with usage of large datasets at scheduled intervals.
- [ ] Stream is slower.
- [ ] Batch is real-time.
- [ ] There is no difference.

Stream processing is for low-latency insights; Batch is for comprehensive, high-volume analysis.
</quiz>

<quiz>
How can you ensure PII data is not stored in your clean data lake?
- [x] Use Glue ETL or Lambda to hash/mask PII columns during ingestion before writing to S3.
- [ ] Delete the PII manually later.
- [ ] Hide the column in QuickSight.
- [ ] Trust the users.

Proactive masking/hashing during the ETL phase is the best practice for data privacy.
</quiz>

<quiz>
Which Redshift feature allows you to manage concurrent query execution queues?
- [x] Workload Management (WLM).
- [ ] Concurrency Scaling.
- [ ] AQUA.
- [ ] RA3 nodes.

WLM allows you to define queues (e.g., "ETL", "Dashboard") and assign memory/concurrency limits to prevent one from starving the other.
</quiz>

<quiz>
What is the benefit of "Columnar Storage" (like Parquet) over Row-based (like CSV)?
- [x] It allows reading only the specific columns required by the query, reducing I/O.
- [ ] It is easier to read for humans.
- [ ] It writes faster.
- [ ] It uses more space.

For analytics where you often select only 3-4 columns out of 50, columnar storage is vastly more efficient.
</quiz>

<quiz>
How do you monitor the "lag" in a Kinesis Data Stream consumer?
- [x] Use the `GetRecords.IteratorAgeMilliseconds` metric in CloudWatch.
- [ ] Check CPU usage.
- [ ] Count the shards.
- [ ] Check S3 bucket size.

Iterator Age tells you how far behind (in time) your consumer application is from the tip of the stream.
</quiz>

<quiz>
Which service would you use to catalog metadata from an on-premise JDBC database?
- [x] AWS Glue Crawler (via JDBC connection).
- [ ] AWS Snowball.
- [ ] AWS Schema Conversion Tool.
- [ ] AWS Config.

Glue Crawlers can connect to JDBC targets to extract schema information.
</quiz>

<quiz>
What is a common use case for DynamoDB in a data engineering pipeline?
- [x] Storing high-velocity state/metadata or deduplication caches (e.g., "Seen IDs").
- [ ] Data Warehousing.
- [ ] Storing large video files.
- [ ] Running complex JOIN queries.

DynamoDB provides fast, predictable read/write performance for state tracking or looking up individual records during processing.
</quiz>

<quiz>
How does Kinesis Data Firehose handle data transformation before loading to S3?
- [x] It can invoke a Lambda function to transform the records (e.g., JSON to CSV) in flight.
- [ ] It uses Glue.
- [ ] It requires an EC2 instance.
- [ ] It cannot transform data.

Firehose supports inline Lambda transformation for simple modifications (like parsing logs) before delivery.
</quiz>

<quiz>
What is the purpose of "Lifecycle Policies" in S3 for a Data Lake?
- [x] To automatically move old raw data to cheaper storage tiers (Glacier) to save costs.
- [ ] To delete data immediately.
- [ ] To encrypt data.
- [ ] To indexing data.

Data Lakes grow indefinitely; lifecycle policies ensure you don't pay "Standard" prices for data from 3 years ago.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Data Engineer Interview Questions](../../../../interview-questions/aws/data-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}
