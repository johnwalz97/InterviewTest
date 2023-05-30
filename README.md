# NYC Bike Trips Pipeline

## Overview

This code is used as a data pipeline to ingest, process and deliver NYC bike trips data.

### 1. Ingestion

The first step is written in Python and is run with the command:

```commandline
python download.py
```

The script logs into an SFTP server and downloads the `trips.csv.gz` and `stations.csv.gz` files
from the `/data/` directory to `/tmp/` on the local filesystem.<br><br>
**TODO:** Script needs to have checks built in to verify that the files exist and download correctly

### 2. Processing

The processing step is written as a PySpark script and is run with the command:

```commandline
spark-submit process.py
```

This script loads the csv files that have been downloaded and joins the stations data frame
twice to the trips data frame to pull in the station name for the start and end stations. It then
selects the relevant columns and renames them based on the schema in the requirements then saves the
results as a csv file in tmp.<br><br>
**TODO:** Data quality checks need to be added in to log and potentially fix bad records (see code TODOs)

### 3. Delivery

The final step is another Python script that takes the result file from the processing step and uploads
it with the appropriate name to the SFTP server's `upload` directory. It is run with the command:

```commandline
python upload.py
```

**TODO:** Script could have some checks built in to verify that results file exists and has the right data

## Data Quality

Did some initial analysis into the data and found that they were few and that issue that first needs to be addressed
is the fact that some records did not have a proper start or end station id and because of this, they were left out of the
inner join. Apart from this, some basic data quality checks should be built in to ensure that the data in the columns
is the correct type and is not corrupted or missing where applicable.

## Production, Orchestration and Automation

To make this pipeline production-ready, some changes would need to be made depending on the size of the data
in production as well as the systems used.<br>
Currently, the code downloads the data to the local file system and
uses Spark local mode to transform the data. This should be changed so that the data is downloaded and moved into
AWS S3 and then processed using AWS EMR. From there the results data can be saved back into S3, downloaded to a server
and then uploaded into the SFTP server.<br>
One way to automate this pipeline for a production system would be to use Apache Airflow and write
a DAG to run the different steps and start up any resources that might be needed (servers or clusters).
