# Demo 06 - Using RStudio from within OpenShift AI

## Introduction
...
...also mention S3 storage...

## Requirements
...

## Configure RStudio in OpenShift AI
Import RStudio notebook image, see https://github.com/opendatahub-io-contrib/workbench-images.

If no S3-compatible storage is available, for testing purposes (no production use!) a simple option for including object storage in the OpenShift cluster is to install minio following https://ai-on-openshift.io/tools-and-applications/minio/minio.

Afterwars create new workbench using the previously created rstudio notebook image.

## Using RStudio in OpenShift AI
Start the RStudio-enabled workbench.

Notes:
- env vars
- region

Use the following code to play around with storing to / loading from S3 buckets:
```R
################################################################################
# NOTE: This is just a collection of commands that can be useful to interact
#       with S3 storage from within RStudio inside OpenShift AI
################################################################################

# Environment variables are directly injected from OpenShift into the container, 
# but they can't be seen by the rstudio terminal. 
# Hence, setting env vars manually as quick hack
Sys.setenv("AWS_ACCESS_KEY_ID" = "YOUR_ACCESS_KEY_ID",
           "AWS_SECRET_ACCESS_KEY" = "YOUR_SECRET_ACCESS_KEY",
           "AWS_DEFAULT_REGION" = "YOUR_DEFAULT_REGION",
           "AWS_S3_ENDPOINT" = "YOUR_S3_ENDPOINT")

# Including library to read S3 buckets (https://github.com/cloudyr/aws.s3)
library("aws.s3")

# Get listing of all object inside a bucket
# NOTE: Setting region as '' is a quick hack needed due to not using AWS S3, but minio
get_bucket(bucket = 'mybucket', region = '')

# Put local file into S3
# NOTE: Setting region as '' is a quick hack needed due to not using AWS S3, but minio
put_object(file = "test_file.txt", object = "test_file", bucket = "mybucket", region = '')

# Save file from S3 to local
# NOTE: Setting region as '' is a quick hack needed due to not using AWS S3, but minio
save_object("test_file", file = "test_file.txt", bucket = "mybucket", region = '')
```


Example to list buckets from VS Code:
```python
# Include AWS boto3 library and os
import boto3
import os

# Create connection to local object storage
s3_client = boto3.client(
    service_name='s3',
    endpoint_url=os.environ['AWS_S3_ENDPOINT']
)

# Obtain buckets
response = s3_client.list_buckets()

# Output bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```



# S3 Browser
Simple S3 browser from https://github.com/cloudlena/s3manager.


Important: Endpoint without `https://`! Set properly in secret!
