---
title: "AWS Data Engineer - Advanced Quiz (20 Questions)"
---

# AWS Data Engineer - Advanced Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/data-engineer.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz challenges your ability to design complex data pipelines, secure PII, and optimize high-scale analytical workloads.

---

<quiz>
Explain the AWS "Lake House" architecture benefit.
- [x] It enables you to query data across your Data Warehouse, Data Lake, and Operational Databases seamlessly without data movement.
- [ ] It puts a house on a lake.
- [ ] It is for structured data only.
- [ ] It replaces S3 with EBS.

The pattern removes silos, allowing Redshift to query S3 (Spectrum) and RDS (Federated Query) in a unified manner.
</quiz>

<quiz>
How do you implement Change Data Capture (CDC) from an on-premise Oracle database to an S3 Data Lake?
- [x] Use AWS Database Migration Service (DMS) with a replication instance.
- [ ] Use AWS Snowball.
- [ ] Use a nightly dump script.
- [ ] Use Kinesis Data Streams directly.

DMS reads the source database transaction logs to capture and replicate changes in near real-time.
</quiz>

<quiz>
You need to deduplicate a high-velocity stream of 1 million events per second with minimal latency. Which probabilistic data structure is most efficient?
- [x] Bloom Filter (implemented in Redis or Flink).
- [ ] Storing every ID in DynamoDB.
- [ ] Using a SQL JOIN.
- [ ] Using S3 ListObjects.

Bloom filters offer O(1) checking with very small memory footprint, accepting a tiny false positive rate for massive speed.
</quiz>

<quiz>
What is the most secure way to grant Redshift access to S3 data for Spectrum queries?
- [x] Associate an IAM Role with the Redshift Cluster that has specific S3 read permissions.
- [ ] Store Access Keys in Redshift.
- [ ] Make the S3 bucket public.
- [ ] Use a Bucket Policy allowing 0.0.0.0/0.

Redshift assumes the IAM Role to access external catalogs and S3 data on your behalf.
</quiz>

<quiz>
How can you provide column-level access control for sensitive PII data in your Data Lake?
- [x] Use AWS Lake Formation.
- [ ] Use S3 Bucket Policies.
- [ ] Use IAM User Policies.
- [ ] Use Security Groups.

Lake Formation allows you to define granular permissions (hide "SSN" column) for different users accessing the same Glue table.
</quiz>

<quiz>
You are designing a real-time dashboard. Aggregations must be calculated every minute. Which tool is best for the processing layer?
- [x] Amazon Kinesis Data Analytics (Flink or SQL).
- [ ] Amazon Athena.
- [ ] AWS Glue.
- [ ] AWS Batch.

Kinesis Data Analytics can process streaming data with windowed aggregations (e.g., "Tumbling Window") in real-time.
</quiz>

<quiz>
How do you optimize Redshift performance for a table heavily used in joins with another large table?
- [x] Use the same Distribution Key (DistStyle KEY) on the join columns for both tables.
- [ ] Use DistStyle ALL.
- [ ] Use DistStyle EVEN.
- [ ] Increase node count.

Colocating join keys on the same node eliminates the network overhead of shuffling data between nodes during the join.
</quiz>

<quiz>
What is the "Vacuum" operation in Redshift and why is it critical?
- [x] It reclaims space from deleted rows and resorts the data to restore performance.
- [ ] It cleans the logs.
- [ ] It deletes old tables.
- [ ] It backs up the cluster.

Deleted rows in Redshift are only marked for deletion. Vacuum actually frees the disk space and re-sorts data for optimal scanning.
</quiz>

<quiz>
Which file format supports "Predicate Pushdown" in Athena?
- [x] Parquet.
- [ ] CSV.
- [ ] JSON.
- [ ] Text.

Parquet stores min/max statistics for each column block, allowing Athena/Spectrum to skip entire blocks that don't match the query filter.
</quiz>

<quiz>
How do you securely share a Glue Data Catalog with another AWS account?
- [x] Use Glue Resource Policies or Lake Formation cross-account sharing.
- [ ] Copy the data to the other account.
- [ ] Share the IAM user credentials.
- [ ] It is not possible.

Resource policies allow you to grant cross-account permissions to the metadata store without duplicating data.
</quiz>

<quiz>
Your EMR cluster is running slow due to "skewed data" (one key has 90% of data). How do you handle this?
- [x] "Salting" the key (adding a random suffix) to distribute it across more reducers.
- [ ] Increase cluster size.
- [ ] Use a larger instance type.
- [ ] Ignore it.

Data skew causes one node to work while others wait. Salting breaks the large key into smaller sub-keys to balance the load.
</quiz>

<quiz>
What is "Backpressure" in a streaming pipeline?
- [x] When the consumer cannot keep up with the producer, causing buffers to fill up and potentially slow down the source.
- [ ] When data flows backwards.
- [ ] When S3 is full.
- [ ] When Redshift is offline.

Handling backpressure (e.g., throttling source, scaling consumer) is critical to prevent system collapse.
</quiz>

<quiz>
How do you implement "Exactly-Once" processing semantics in Kinesis?
- [x] It is difficult; typically requires checking a unique ID against a state store (deduplication) or using a framework like Flink with checkpointing.
- [ ] Kinesis supports it out of the box.
- [ ] Use SQS FIFO.
- [ ] Use Standard SQS.

Standard streaming often guarantees "At Least Once". achieving "Exactly Once" requires application-level logic or advanced frameworks.
</quiz>

<quiz>
Which option minimizes the cost of storing petabytes of historical logs that effectively never need to be read unless there is a legal audit?
- [x] S3 Glacier Deep Archive.
- [ ] S3 Glacier Flexible Retrieval.
- [ ] S3 Standard-IA.
- [ ] EBS Cold HDD.

Deep Archive is the absolute lowest cost storage class, with retrieval times of 12-48 hours.
</quiz>

<quiz>
How can you speed up a complex Glue ETL job that is running out of memory (OOM)?
- [x] Scale out (add more workers) or switch to a worker type with more memory (G.1X to G.2X).
- [ ] Increase the timeout.
- [ ] Write the data to a local file.
- [ ] Disable logging.

Glue allows you to select "Worker Type" to allocate more memory and CPU to each executor.
</quiz>

<quiz>
What is a "Materialized View" in Redshift?
- [x] A precomputed result set of a query stored physically, which is much faster to query than the complex base view.
- [ ] A logical view.
- [ ] A backup.
- [ ] A temporary table.

Materialized views are ideal for speeding up dashboards that run the same complex aggregation query repeatedly.
</quiz>

<quiz>
How do you integrate on-premise Active Directory users with Amazon QuickSight?
- [x] Use AWS IAM Identity Center (Single Sign-On) or AD Connector.
- [ ] Create IAM users for everyone.
- [ ] Share a generic login.
- [ ] Use a CSV file.

Federating identity allows users to login with their corporate credentials.
</quiz>

<quiz>
What mechanism allows Kinesis Data Firehose to convert JSON data to Parquet before writing to S3?
- [x] Turn on "Record Format Conversion" in the Firehose configuration (using a Glue table for schema).
- [ ] It cannot do this.
- [ ] Use a Lambda.
- [ ] Use EMR.

Firehose has native support for format conversion (JSON -> Parquet/ORC) which is more efficient than Lambda.
</quiz>

<quiz>
You need to list billions of objects in an S3 bucket daily for auditing. `ListObjects` API is too slow and expensive. What is the solution?
- [x] Enable S3 Inventory to generate a daily CSV/Parquet report.
- [ ] Run a Lambda function.
- [ ] Use multiple threads.
- [ ] Use DynamoDB.

S3 Inventory provides a flat file listing of your objects, which you can then query with Athena essentially for free (compared to API costs).
</quiz>

<quiz>
Which scenario warrants using Redshift RA3 nodes (Managed Storage)?
- [x] When you need to scale compute and storage independently (e.g., tons of data but low query volume).
- [ ] When you have small data.
- [ ] When you need the lowest cost.
- [ ] When you use only standard SQL.

RA3 nodes decouple storage from compute, allowing you to store petabytes of data on S3-backed managed storage without paying for thousands of CPU nodes.
</quiz>

---

### 📚 Study Guides
- [AWS Data Engineer Interview Questions](../../../../interview-questions/aws/data-engineer.md)

---

{% include-markdown "_partials/subscribe.md" %}
