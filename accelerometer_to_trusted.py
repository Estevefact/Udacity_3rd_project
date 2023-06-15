import re
import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node customer_trusted
customer_trusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://project-stedi-eva/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="customer_trusted_node1",
)

# Script generated for node accelerometer
accelerometer_node1686846065036 = (
    glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": False},
        connection_type="s3",
        format="json",
        connection_options={
            "paths": ["s3://project-stedi-eva/accelerometer/landing/"],
            "recurse": True,
        },
        transformation_ctx="accelerometer_node1686846065036",
    )
)

# Script generated for node Join
Join_node1686846041513 = Join.apply(
    frame1=customer_trusted_node1,
    frame2=accelerometer_node1686846065036,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="Join_node1686846041513",
)

# Script generated for node Filter
Filter_node1686846631780 = Filter.apply(
    frame=Join_node1686846041513,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="Filter_node1686846631780",
)

# Script generated for nodce S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=Filter_node1686846631780,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://project-stedi-eva/accelerator/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
