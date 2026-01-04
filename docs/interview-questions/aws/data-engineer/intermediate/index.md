---
title: "AWS Data Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Data Engineer interview questions covering S3 Optimization, Partitioning, and Redshift Distribution Styles."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. How do you optimize S3 performance for high request rates (thousands of PUT/GET per second)?"
    **Use multiple prefixes (folder paths) to parallelize the requests, as S3 scaling is partition-based per prefix**.
    
    S3 scales automatically, but using distinct prefixes allows it to scale partitions horizontally for massive throughput.

??? question "2. What is the "Small File Problem" in Hadoop/Spark/Athena?"
    **Performance degradation caused by excessive metadata overhead when processing thousands of tiny files (KB size)**.
    
    Query engines spend more time listing files and opening connections than reading data. Solution: Compact files into larger chunks (e.g., 128MB).

??? question "3. When should you choose Amazon EMR over AWS Glue?"
    **When you need massive, long-running, complex jobs where you require full control over the cluster configuration and software tuning**.
    
    EMR gives you "root" access to the cluster, ideal for specific Hadoop/Spark tuning or custom binaries.

??? question "4. What is "Partitioning" in the context of Athena/S3?"
    **Organizing data into folders (e.g., `year=2024/month=01`) so queries scan only relevant data subsets**.
    
    Partitioning dramatically reduces cost and improves speed by preventing full table scans.

??? question "5. Which distribution style in Redshift optimizes for joins between two large tables?"
    **KEY (Distribute based on the Join column)**.
    
    Colocating rows with matching keys on the same node minimizes network shuffle during the join operation.

??? question "6. How do you handle schema evolution (e.g., adding a new column) in a Parquet-based data lake?"
    **Parquet supports schema evolution; you can add the column and use Glue Schema Registry to validate compatibility**.
    
    Columnar formats like Parquet and Avro are designed to handle schema add/remove gracefully.

??? question "7. What is the main difference between Amazon QuickSight and Tableau on EC2?"
    **QuickSight is serverless and auto-scaling; Tableau on EC2 requires infrastructure management**.
    
    QuickSight is native to AWS and charges per session/user without server admin overhead.

??? question "8. How do you securely connect QuickSight to a private RDS instance?"
    **Connect QuickSight to the VPC; it creates an ENI to access private subnets**.
    
    Attaching QuickSight to the VPC allows it to route traffic to internal IPs securely.

??? question "9. Which service is used to orchestrate complex data workflows involving dependencies (e.g., Lambda -> Glue -> Redshift)?"
    **AWS Step Functions (or MWAA)**.
    
    Step Functions provides a state machine to manage retries, parallel branches, and error handling for critical pipelines.

??? question "10. What is the role of the "Sort Key" in Redshift?"
    **It determines the order in which data is stored on disk, optimizing range queries and filtering**.
    
    Zone maps allow Redshift to skip blocks that don't fall within the requested Sort Key range, speeding up queries.

??? question "11. If you need to query logs in S3 but only care about records with "ERROR", how can you avoid scanning the whole file?"
    **Use S3 Select (or convert to Parquet and filter)**.
    
    S3 Select allows you to retrieve only a subset of data from an object by using simple SQL expressions.

??? question "12. What is key difference between "Stream Processing" and "Batch Processing"?"
    **Stream processing deals with continuous data in real-time; Batch processing deals with usage of large datasets at scheduled intervals**.
    
    Stream processing is for low-latency insights; Batch is for comprehensive, high-volume analysis.

??? question "13. How can you ensure PII data is not stored in your clean data lake?"
    **Use Glue ETL or Lambda to hash/mask PII columns during ingestion before writing to S3**.
    
    Proactive masking/hashing during the ETL phase is the best practice for data privacy.

??? question "14. Which Redshift feature allows you to manage concurrent query execution queues?"
    **Workload Management (WLM)**.
    
    WLM allows you to define queues (e.g., "ETL", "Dashboard") and assign memory/concurrency limits to prevent one from starving the other.

??? question "15. What is the benefit of "Columnar Storage" (like Parquet) over Row-based (like CSV)?"
    **It allows reading only the specific columns required by the query, reducing I/O**.
    
    For analytics where you often select only 3-4 columns out of 50, columnar storage is vastly more efficient.

??? question "16. How do you monitor the "lag" in a Kinesis Data Stream consumer?"
    **Use the `GetRecords.IteratorAgeMilliseconds` metric in CloudWatch**.
    
    Iterator Age tells you how far behind (in time) your consumer application is from the tip of the stream.

??? question "17. Which service would you use to catalog metadata from an on-premise JDBC database?"
    **AWS Glue Crawler (via JDBC connection)**.
    
    Glue Crawlers can connect to JDBC targets to extract schema information.

??? question "18. What is a common use case for DynamoDB in a data engineering pipeline?"
    **Storing high-velocity state/metadata or deduplication caches (e.g., "Seen IDs")**.
    
    DynamoDB provides fast, predictable read/write performance for state tracking or looking up individual records during processing.

??? question "19. How does Kinesis Data Firehose handle data transformation before loading to S3?"
    **It can invoke a Lambda function to transform the records (e.g., JSON to CSV) in flight**.
    
    Firehose supports inline Lambda transformation for simple modifications (like parsing logs) before delivery.

??? question "20. What is the purpose of "Lifecycle Policies" in S3 for a Data Lake?"
    **To automatically move old raw data to cheaper storage tiers (Glacier) to save costs**.
    
    Data Lakes grow indefinitely; lifecycle policies ensure you don't pay "Standard" prices for data from 3 years ago.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Data Engineer Intermediate Quiz](../../../../quiz/aws/data-engineer/intermediate/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}
