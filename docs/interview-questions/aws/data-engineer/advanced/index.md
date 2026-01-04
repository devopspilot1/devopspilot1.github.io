---
title: "AWS Data Engineer Interview Questions - Advanced"
description: "Top 20 Advanced AWS Data Engineer interview questions covering CDC, Lake Formation, Kinesis Processing, and Redshift Optimization."
---

# Advanced Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-advanced.md" %}

??? question "1. Explain the AWS "Lake House" architecture benefit."
    **It enables you to query data across your Data Warehouse, Data Lake, and Operational Databases seamlessly without data movement**.
    
    The pattern removes silos, allowing Redshift to query S3 (Spectrum) and RDS (Federated Query) in a unified manner.

??? question "2. How do you implement Change Data Capture (CDC) from an on-premise Oracle database to an S3 Data Lake?"
    **Use AWS Database Migration Service (DMS) with a replication instance**.
    
    DMS reads the source database transaction logs to capture and replicate changes in near real-time.

??? question "3. You need to deduplicate a high-velocity stream of 1 million events per second with minimal latency. Which probabilistic data structure is most efficient?"
    **Bloom Filter (implemented in Redis or Flink)**.
    
    Bloom filters offer O(1) checking with very small memory footprint, accepting a tiny false positive rate for massive speed.

??? question "4. What is the most secure way to grant Redshift access to S3 data for Spectrum queries?"
    **Associate an IAM Role with the Redshift Cluster that has specific S3 read permissions**.
    
    Redshift assumes the IAM Role to access external catalogs and S3 data on your behalf.

??? question "5. How can you provide column-level access control for sensitive PII data in your Data Lake?"
    **Use AWS Lake Formation**.
    
    Lake Formation allows you to define granular permissions (hide "SSN" column) for different users accessing the same Glue table.

??? question "6. You are designing a real-time dashboard. Aggregations must be calculated every minute. Which tool is best for the processing layer?"
    **Amazon Kinesis Data Analytics (Flink or SQL)**.
    
    Kinesis Data Analytics can process streaming data with windowed aggregations (e.g., "Tumbling Window") in real-time.

??? question "7. How do you optimize Redshift performance for a table heavily used in joins with another large table?"
    **Use the same Distribution Key (DistStyle KEY) on the join columns for both tables**.
    
    Colocating join keys on the same node eliminates the network overhead of shuffling data between nodes during the join.

??? question "8. What is the "Vacuum" operation in Redshift and why is it critical?"
    **It reclaims space from deleted rows and resorts the data to restore performance**.
    
    Deleted rows in Redshift are only marked for deletion. Vacuum actually frees the disk space and re-sorts data for optimal scanning.

??? question "9. Which file format supports "Predicate Pushdown" in Athena?"
    **Parquet**.
    
    Parquet stores min/max statistics for each column block, allowing Athena/Spectrum to skip entire blocks that don't match the query filter.

??? question "10. How do you securely share a Glue Data Catalog with another AWS account?"
    **Use Glue Resource Policies or Lake Formation cross-account sharing**.
    
    Resource policies allow you to grant cross-account permissions to the metadata store without duplicating data.

??? question "11. Your EMR cluster is running slow due to "skewed data" (one key has 90% of data). How do you handle this?"
    **"Salting" the key (adding a random suffix) to distribute it across more reducers**.
    
    Data skew causes one node to work while others wait. Salting breaks the large key into smaller sub-keys to balance the load.

??? question "12. What is "Backpressure" in a streaming pipeline?"
    **When the consumer cannot keep up with the producer, causing buffers to fill up and potentially slow down the source**.
    
    Handling backpressure (e.g., throttling source, scaling consumer) is critical to prevent system collapse.

??? question "13. How do you implement "Exactly-Once" processing semantics in Kinesis?"
    **It is difficult; typically requires checking a unique ID against a state store (deduplication) or using a framework like Flink with checkpointing**.
    
    Standard streaming often guarantees "At Least Once". achieving "Exactly Once" requires application-level logic or advanced frameworks.

??? question "14. Which option minimizes the cost of storing petabytes of historical logs that effectively never need to be read unless there is a legal audit?"
    **S3 Glacier Deep Archive**.
    
    Deep Archive is the absolute lowest cost storage class, with retrieval times of 12-48 hours.

??? question "15. How can you speed up a complex Glue ETL job that is running out of memory (OOM)?"
    **Scale out (add more workers) or switch to a worker type with more memory (G.1X to G.2X)**.
    
    Glue allows you to select "Worker Type" to allocate more memory and CPU to each executor.

??? question "16. What is a "Materialized View" in Redshift?"
    **A precomputed result set of a query stored physically, which is much faster to query than the complex base view**.
    
    Materialized views are ideal for speeding up dashboards that run the same complex aggregation query repeatedly.

??? question "17. How do you integrate on-premise Active Directory users with Amazon QuickSight?"
    **Use AWS IAM Identity Center (Single Sign-On) or AD Connector**.
    
    Federating identity allows users to login with their corporate credentials.

??? question "18. What mechanism allows Kinesis Data Firehose to convert JSON data to Parquet before writing to S3?"
    **Turn on "Record Format Conversion" in the Firehose configuration (using a Glue table for schema)**.
    
    Firehose has native support for format conversion (JSON -> Parquet/ORC) which is more efficient than Lambda.

??? question "19. You need to list billions of objects in an S3 bucket daily for auditing. `ListObjects` API is too slow and expensive. What is the solution?"
    **Enable S3 Inventory to generate a daily CSV/Parquet report**.
    
    S3 Inventory provides a flat file listing of your objects, which you can then query with Athena essentially for free (compared to API costs).

??? question "20. Which scenario warrants using Redshift RA3 nodes (Managed Storage)?"
    **When you need to scale compute and storage independently (e.g., tons of data but low query volume)**.
    
    RA3 nodes decouple storage from compute, allowing you to store petabytes of data on S3-backed managed storage without paying for thousands of CPU nodes.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Data Engineer Advanced Quiz](../../../../quiz/aws/data-engineer/advanced/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}
