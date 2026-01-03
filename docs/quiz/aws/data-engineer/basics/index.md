---
title: "AWS Data Engineer - Basics Quiz (20 Questions)"
---

# AWS Data Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers fundamental data engineering concepts on AWS, including S3 storage, Glue ETL components, and Redshift basics.

---

<quiz>
What is a "Data Lake" on AWS typically built upon?
- [x] Amazon S3.
- [ ] Amazon RDS.
- [ ] Amazon DynamoDB.
- [ ] Amazon EBS.

S3 provides the scalable, durable, cost-effective storage foundation for a Data Lake.
</quiz>

<quiz>
Which AWS service is a serverless ETL (Extract, Transform, Load) service?
- [x] AWS Glue.
- [ ] AWS Data Pipeline.
- [ ] Amazon EMR.
- [ ] Amazon Athena.

Glue classifies, cleans, enriches, and moves data reliably between data stores.
</quiz>

<quiz>
What is the purpose of the AWS Glue Data Catalog?
- [x] To act as a central repository for metadata (table definitions, schemas) across your data assets.
- [ ] To store the actual data.
- [ ] To visualize data.
- [ ] To run SQL queries.

The Data Catalog is a persistent metadata store that integrates with Athena, Redshift, and EMR.
</quiz>

<quiz>
Which service allows you to run standard SQL queries directly against data in S3 without loading it?
- [x] Amazon Athena.
- [ ] Amazon RDS.
- [ ] Amazon Kinesis.
- [ ] AWS Glue.

Athena is an interactive query service that makes it easy to analyze data in S3 using standard SQL.
</quiz>

<quiz>
What is Amazon Redshift?
- [x] A fully managed, petabyte-scale data warehouse service.
- [ ] A NoSQL database.
- [ ] A caching service.
- [ ] A graph database.

Redshift is optimized for OLAP (Online Analytical Processing) workloads.
</quiz>

<quiz>
Which file format is column-oriented and optimized for analytics queries?
- [x] Parquet.
- [ ] CSV.
- [ ] JSON.
- [ ] XML.

Parquet stores data by column, making it faster and cheaper to query subsets of columns compared to row-based formats like CSV.
</quiz>

<quiz>
What is an AWS Glue Crawler used for?
- [x] To discover the schema of your data and populate the Data Catalog.
- [ ] To move data.
- [ ] To visualize data.
- [ ] To delete data.

Crawlers browse your data sources, deduce the schema, and create table definitions in the Glue Data Catalog.
</quiz>

<quiz>
Which service is best suited for real-time streaming data ingestion?
- [x] Amazon Kinesis Data Streams.
- [ ] Amazon S3.
- [ ] Amazon Glacier.
- [ ] AWS Batch.

Kinesis Data Streams creates a channel for capturing and storing terabytes of data per hour from hundreds of thousands of sources.
</quiz>

<quiz>
What is the difference between Kinesis Data Streams and Kinesis Data Firehose?
- [x] Streams is for custom real-time processing; Firehose is for loading data into destinations (S3, Redshift) with zero code.
- [ ] Streams is slower.
- [ ] Firehose is for video.
- [ ] They are identical.

Firehose is the "easiest way to load streaming data" into data stores.
</quiz>

<quiz>
How is Amazon Athena priced?
- [x] Per Terabyte of data scanned by your queries.
- [ ] Per hour of instance usage.
- [ ] Per user.
- [ ] Flat monthly fee.

You pay only for the queries that you run. Compressing and partitioning data reduces costs significantly.
</quiz>

<quiz>
Which Redshift distribution style distributes rows in a round-robin fashion?
- [x] EVEN.
- [ ] KEY.
- [ ] ALL.
- [ ] AUTO.

EVEN distribution is useful when the table does not participate in joins or when there is no clear choice for a distribution key.
</quiz>

<quiz>
What is Redshift Spectrum?
- [x] A feature that allows Redshift to query data in S3 without loading it.
- [ ] A visualization tool.
- [ ] A migration tool.
- [ ] A type of node.

Spectrum extends analytics to your data lake, allowing you to query open file formats in S3 using Redshift SQL.
</quiz>

<quiz>
What is Amazon EMR (Elastic MapReduce)?
- [x] A managed cluster platform that simplifies running big data frameworks like Hadoop and Spark.
- [ ] A serverless Query engine.
- [ ] A Data Warehouse.
- [ ] A message queue.

EMR provides a managed environment for processing vast amounts of data using open-source tools.
</quiz>

<quiz>
Which component is responsible for organizing and scheduling Glue ETL jobs?
- [x] Triggers and Workflows.
- [ ] Crawlers.
- [ ] Endpoints.
- [ ] Notebooks.

Triggers can start jobs on a schedule or based on events (like a previous job finishing).
</quiz>

<quiz>
What helps you visualize and analyze data using interactive dashboards?
- [x] Amazon QuickSight.
- [ ] Amazon CloudWatch.
- [ ] AWS CloudTrail.
- [ ] Amazon Macie.

QuickSight is AWS’s fast, cloud-powered business intelligence service.
</quiz>

<quiz>
Which S3 feature helps unauthorized users from accessing your data lake?
- [x] S3 Bucket Policies and Block Public Access.
- [ ] S3 Versioning.
- [ ] S3 Transfer Acceleration.
- [ ] S3 Analytics.

Securing the bucket permissions is the first line of defense for a Data Lake.
</quiz>

<quiz>
What is an "OLAP" workload?
- [x] Online Analytical Processing - complex queries on large historical datasets.
- [ ] Online Transaction Processing (OLTP) - simple inserts/updates.
- [ ] Real-time streaming.
- [ ] Key-value lookups.

OLAP queries often involve aggregations and joins over millions of rows (e.g., "Total sales by region last year").
</quiz>

<quiz>
Which Redshift command reclaims space from deleted rows and resorts tables?
- [x] VACUUM.
- [ ] CLEAN.
- [ ] OPTIMIZE.
- [ ] COMPACT.

Because Redshift does not reclaim space immediately on delete, you must run VACUUM periodically (or rely on auto-vacuum).
</quiz>

<quiz>
How do you compress data in S3 to save Athena query costs?
- [x] Convert data to Gzip or Snappy compressed formats (e.g., Parquet/Snappy).
- [ ] Zip the files manually.
- [ ] Use S3 Intelligent Tiering.
- [ ] You cannot compress data for Athena.

Athena scans fewer bytes if the data is compressed, directly lowering your bill.
</quiz>

<quiz>
What is the "Lake House" architecture?
- [x] A combined approach using a Data Lake (S3) for scale/flexibility and a Data Warehouse (Redshift) for performance/structure.
- [ ] Using only S3.
- [ ] Using only Redshift.
- [ ] A house built on a lake.

Migration of data between the lake and the warehouse is seamless in this architecture.
</quiz>

---

### 📚 Study Guides
- [AWS Data Engineer Interview Questions](../../../../interview-questions/aws/data-engineer.md)

---

{% include-markdown "_partials/subscribe.md" %}
