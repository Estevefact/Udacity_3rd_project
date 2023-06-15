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

# Script generated for node Customer_trusted
Customer_trusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://project-stedi-eva/accelerator/trusted/"],
        "recurse": True,
    },
    transformation_ctx="Customer_trusted_node1",
)

# Script generated for node Step_trainer
Step_trainer_node1686847346908 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://project-stedi-eva/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="Step_trainer_node1686847346908",
)

# Script generated for node Join
Join_node1686847342372 = Join.apply(
    frame1=Customer_trusted_node1,
    frame2=Step_trainer_node1686847346908,
    keys1=["serialNumber"],
    keys2=["serialNumber"],
    transformation_ctx="Join_node1686847342372",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=Join_node1686847342372,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://project-stedi-eva/step_trainer/curated/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
