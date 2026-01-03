---
title: "AWS Data Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS Data Engineer interview questions covering S3 Data Lakes, Glue, Redshift, and Athena."
---

# Basics Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-basics.md" %}

??? question "1. What is a "Data Lake" on AWS typically built upon?"
    **Amazon S3**.
    
    S3 provides the scalable, durable, cost-effective storage foundation for a Data Lake.

??? question "2. Which AWS service is a serverless ETL (Extract, Transform, Load) service?"
    **AWS Glue**.
    
    Glue classifies, cleans, enriches, and moves data reliably between data stores.

??? question "3. What is the purpose of the AWS Glue Data Catalog?"
    **To act as a central repository for metadata (table definitions, schemas) across your data assets**.
    
    The Data Catalog is a persistent metadata store that integrates with Athena, Redshift, and EMR.

??? question "4. Which service allows you to run standard SQL queries directly against data in S3 without loading it?"
    **Amazon Athena**.
    
    Athena is an interactive query service that makes it easy to analyze data in S3 using standard SQL.

??? question "5. What is Amazon Redshift?"
    **A fully managed, petabyte-scale data warehouse service**.
    
    Redshift is optimized for OLAP (Online Analytical Processing) workloads.

??? question "6. Which file format is column-oriented and optimized for analytics queries?"
    **Parquet**.
    
    Parquet stores data by column, making it faster and cheaper to query subsets of columns compared to row-based formats like CSV.

??? question "7. What is an AWS Glue Crawler used for?"
    **To discover the schema of your data and populate the Data Catalog**.
    
    Crawlers browse your data sources, deduce the schema, and create table definitions in the Glue Data Catalog.

??? question "8. Which service is best suited for real-time streaming data ingestion?"
    **Amazon Kinesis Data Streams**.
    
    Kinesis Data Streams creates a channel for capturing and storing terabytes of data per hour from hundreds of thousands of sources.

??? question "9. What is the difference between Kinesis Data Streams and Kinesis Data Firehose?"
    **Streams is for custom real-time processing; Firehose is for loading data into destinations (S3, Redshift) with zero code**.
    
    Firehose is the "easiest way to load streaming data" into data stores.

??? question "10. How is Amazon Athena priced?"
    **Per Terabyte of data scanned by your queries**.
    
    You pay only for the queries that you run. Compressing and partitioning data reduces costs significantly.

??? question "11. Which Redshift distribution style distributes rows in a round-robin fashion?"
    **EVEN**.
    
    EVEN distribution is useful when the table does not participate in joins or when there is no clear choice for a distribution key.

??? question "12. What is Redshift Spectrum?"
    **A feature that allows Redshift to query data in S3 without loading it**.
    
    Spectrum extends analytics to your data lake, allowing you to query open file formats in S3 using Redshift SQL.

??? question "13. What is Amazon EMR (Elastic MapReduce)?"
    **A managed cluster platform that simplifies running big data frameworks like Hadoop and Spark**.
    
    EMR provides a managed environment for processing vast amounts of data using open-source tools.

??? question "14. Which component is responsible for organizing and scheduling Glue ETL jobs?"
    **Triggers and Workflows**.
    
    Triggers can start jobs on a schedule or based on events (like a previous job finishing).

??? question "15. What helps you visualize and analyze data using interactive dashboards?"
    **Amazon QuickSight**.
    
    QuickSight is AWS’s fast, cloud-powered business intelligence service.

??? question "16. Which S3 feature helps unauthorized users from accessing your data lake?"
    **S3 Bucket Policies and Block Public Access**.
    
    Securing the bucket permissions is the first line of defense for a Data Lake.

??? question "17. What is an "OLAP" workload?"
    **Online Analytical Processing - complex queries on large historical datasets**.
    
    OLAP queries often involve aggregations and joins over millions of rows (e.g., "Total sales by region last year").

??? question "18. Which Redshift command reclaims space from deleted rows and resorts tables?"
    **VACUUM**.
    
    Because Redshift does not reclaim space immediately on delete, you must run VACUUM periodically (or rely on auto-vacuum).

??? question "19. How do you compress data in S3 to save Athena query costs?"
    **Convert data to Gzip or Snappy compressed formats (e.g., Parquet/Snappy)**.
    
    Athena scans fewer bytes if the data is compressed, directly lowering your bill.

??? question "20. What is the "Lake House" architecture?"
    **A combined approach using a Data Lake (S3) for scale/flexibility and a Data Warehouse (Redshift) for performance/structure**.
    
    Migration of data between the lake and the warehouse is seamless in this architecture.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Data Engineer Basics Quiz](../../../../quiz/aws/data-engineer/basics/index.md)**

{% include-markdown "../../../../_partials/subscribe-guides.md" %}
