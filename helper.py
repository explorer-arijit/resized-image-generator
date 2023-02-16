import boto3
import botocore
from botocore.exceptions import ClientError
from botocore.config import Config
from PIL import Image

def s3_download(bucket,key,path):
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket,key,path)
        return "Success"
    except ClientError as error:
        print(f"An error occured while downloading file from S3: {error}")
        raise error
    except botocore.exceptions.ParamValidationError as error:
        print(f"Parameters provided are invalid: {error}")
        raise error

def genarate_thumbnail(file_path,thumbnail_path):
    try:
        image = Image.open(file_path)
        image.thumbnail((90,90))
        image.save(thumbnail_path)
    except Exception as error:
        raise error

def s3_upload(bucket,file_source,destination):
    try:
        s3 = boto3.client('s3')
        s3.upload_file(file_source,bucket,destination)
        return "Success"
    except ClientError as error:
        print(f"An error occured while uploading file to S3: {error}")
        raise error
    except botocore.exceptions.ParamValidationError as error:
        print(f"Parameters provided are invalid: {error}")
        raise error