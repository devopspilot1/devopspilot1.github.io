---
title: "AWS Data Engineer Interview Questions"
date: 2024-07-01
---

# AWS Data Engineer Interview Questions

## Storage & Data Lakes

### 1. Explain the "Lake House" architecture on AWS.
It combines the flexibility and low cost of a Data Lake (S3) with the performance and ACID transactions of a Data Warehouse (Redshift).
Key components:
*   **S3**: Storage layer (Parquet/ORC).
*   **Glue**: Data Catalog/Metadata.
*   **Redshift Spectrum**: Query S3 data directly from Redshift without loading it.
*   **Athena**: Serverless SQL analysis on S3.

### 2. How do you optimize S3 performance for high request rates?
*   **Prefix Randomization**: Historically needed, but S3 now scales automatically to 3,500 PUT/COPY/POST/DELETE per second and 5,500 GET/HEAD requests per second per prefix.
*   **Parallel Requests**: Use multipart uploads for large files and range fetches for downloads.
*   **Retry Logic**: Implement exponential backoff.

### 3. What is the difference between Parquet and CSV?
*   **Parquet**: Columnar storage. Optimized for read-heavy analytical queries (OLAP). Compresses well. Supports schema evolution. Better for Athena/Redshift Spectrum.
*   **CSV**: Row-based. Simple, human-readable, but inefficient for querying specific columns (must read whole row/file).

## ETL & Processing

### 4. What is AWS Glue and what are its components?
A serverless ETL service.
*   **Data Catalog**: Central repository of metadata.
*   **Crawlers**: Discover schema and populate Catalog.
*   **ETL Jobs**: PySpark or Scala scripts to transform data.
*   **Triggers**: Schedule jobs.

### 5. When would you use EMR over Glue?
*   **EMR (Elastic MapReduce)**: Managed Hadoop/Spark cluster. You have full control over the infrastructure (EC2 type, cluster size). Best for massive, long-running, complex jobs where you need fine-tuned tuning or custom JARs/software.
*   **Glue**: Serverless. Best for standard ETL, ease of use, and when you don't want to manage clusters.

### 6. Explain Kinesis Data Streams vs Kinesis Firehose.
*   **Data Streams**: Real-time streaming. Custom consumers (Lambda, KCL). You manage shards (scale). Low latency (sub-second).
*   **Firehose**: Near real-time delivery service. Loads data into S3, Redshift, Elasticsearch, Splunk. Managed scaling. Higher latency (60s buffer).

### 7. How do you handle "Small File Problem" in Hadoop/Spark on S3?
Lots of small files kill performance (too much metadata overhead).
*   **Compaction**: Run a job to merge small files into larger ones (e.g., 128MB - 1GB).
*   **Glue**: Enable "Group" option in S3 source.
*   **Firehose**: Configure buffering hints (size/time) to aggregate data before writing.

## Data Warehousing (Redshift)

### 8. Explain Distribution Styles in Redshift.
*   **KEY**: Rows with same distribution key values go to same node. Good for joins.
*   **EVEN**: Round-robin distribution. Good for keeping node loads balanced if no joins.
*   **ALL**: Copy of full table on every node. Good for small dimension tables.
*   **AUTO**: Redshift decides.

### 9. What is Redshift Spectrum?
Allows you to run SQL queries against exabytes of unstructured data in Amazon S3. No loading required. It scales compute separately from storage.

### 10. How do you optimize a Redshift query?
*   **Sort Keys**: Store data in sorted order for range filtering.
*   **Dist Keys**: Serialize joins by colocating data.
*   **Compression**: Use ANALYZE command.
*   **WLM (Workload Management)**: Prioritize queues.
*   **VACUUM**: Reclaim space and resort rows after deletes.

## Analytics & Visualization

### 11. What is Athena and how is it priced?
Serverless interactive query service based on Presto. Queries data in S3 using standard SQL.
**Pricing**: $5 per TB of data *scanned*.
**Optimization**: Compress data (Snappy/Gzip), use Columnar formats (Parquet), Partition data (Scan only relevant folders).

### 12. How does QuickSight connect to private RDS?
QuickSight must be attached to the VPC. It creates an ENI in the VPC subnet to reach the private RDS instance. Security Groups must allow traffic.

## Data Pipelines & Orchestration

### 13. Compare AWS Data Pipeline vs Step Functions vs Airflow (MWAA).
*   **Data Pipeline**: Legacy, specific to moving data between AWS services.
*   **Step Functions**: General purpose orchestration (state machine). Good for event-driven workflows involving Lambda/Glue.
*   **MWAA (Airflow)**: Industry standard open-source platform. Python-based DAGs. Best for complex dependencies, backfilling, and hybrid cloud workflows.

### 14. How do you handle schema evolution?
*   **Glue Schema Registry**: Validates data against schema.
*   **Parquet/Avro**: Support appending columns.
*   **Versioning**: Create new table versions if breaking changes occur.

## Advanced & Scenarios

### 15. Real-time Dashboard Scenario: You need to ingest clickstream logs, process them to find top URLs every minute, and display on a dashboard. Architecture?
1.  **Ingest**: Kinesis Data Streams.
2.  **Process**: Kinesis Data Analytics (SQL or Flink app) to aggregate windowed counts.
3.  **Store/Deliver**: Kinesis Firehose -> OpenSearch Service (or Timestream).
4.  **Visualize**: OpenSearch Dashboards (or Grafana).

### 16. Explain Change Data Capture (CDC) with DMS.
AWS **DMS (Database Migration Service)** can replicate ongoing changes from a source DB (e.g., Oracle, MySQL) to a target (e.g., S3, Redshift) using the source transaction logs. It allows near-zero downtime migration or continuous replication for analytics.

### 17. How do you secure PII data in a Data Lake?
*   **Encryption**: SSE-S3 or SSE-KMS.
*   **Access Control**: Lake Formation (Column-level access control).
*   **Anonymization**: Use Glue ETL to hash/mask PII columns before writing to the "Clean" zone.
*   **Discovery**: Use Macie to find exposed PII.

### 18. What is the difference between Kinesis Data Streams and SQS?
*   **SQS**: Message Queue. Job distribution. Delete after process. No ordering guarantee (unless FIFO). One consumer per message.
*   **Kinesis**: Streaming Log. Real-time analytics. Replayable (retention period). Ordered by shard. Multiple consumers can read same data.

### 19. How do you handle checking for duplicates in a stream?
*   **Bloom Filter**: probabilistic structure to check existence.
*   **Stateful Processing**: Use Flink/Kinesis Analytics with a state store (e.g., RocksDB) to track seen IDs within a window.
*   **DynamoDB**: Check/Write valid IDs (slower).

### 20. Optimize "Listing" objects in S3 with billions of files.
Don't use `ListObjects`. It's slow and expensive.
Use **S3 Inventory**. It delivers a daily or weekly CSV/Parquet file listing all objects to a destination bucket. Query that file with Athena.
