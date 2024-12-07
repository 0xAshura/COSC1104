import boto3
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS credentials and region
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = 'us-east-1'  # Replace with your AWS region

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

def backup_data(source_bucket, destination_bucket):
    try:
        # Validate source bucket
        s3.head_bucket(Bucket=source_bucket)
        logger.info(f"Validated source bucket: {source_bucket}")

        # List objects in the source bucket
        response = s3.list_objects_v2(Bucket=source_bucket)
        if 'Contents' not in response:
            logger.warning(f"No objects found in the source bucket: {source_bucket}")
            return

        # Copy objects to destination bucket
        for obj in response['Contents']:
            copy_source = {'Bucket': source_bucket, 'Key': obj['Key']}
            try:
                s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=obj['Key'])
                logger.info(f"Copied {obj['Key']} to {destination_bucket}")
            except Exception as copy_error:
                logger.error(f"Failed to copy {obj['Key']}: {str(copy_error)}")

        logger.info(f"Data backup completed from {source_bucket} to {destination_bucket}")
    except Exception as e:
        logger.error(f"Error during data backup: {str(e)}")

# Example usage
backup_data('source_bucket', 'backup_bucket')  # Replace with actual bucket names
