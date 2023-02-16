import os
from os import walk
import json
import helper as Helper

file_processing_location = 'doc_processor_location/' if os.environ['LOCAL'] == 'true' else '/tmp/'

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            processing_file_list = []
            s3_bucket = record['s3']['bucket']['name']
            s3_file_key = record['s3']['object']['key']
            base_image_file_name = os.path.basename(s3_file_key)
            file_tmp_storage_path = file_processing_location + base_image_file_name
            print(f'Processing file {base_image_file_name}')
            Helper.s3_download(s3_bucket,s3_file_key,file_tmp_storage_path)
            processing_file_list.append(file_tmp_storage_path)
            thumbnail_path = file_processing_location + os.path.splitext(base_image_file_name)[0] + "_tmb.jpg"
            Helper.genarate_thumbnail(file_tmp_storage_path,thumbnail_path)
            processing_file_list.append(thumbnail_path)
            s3_thumbnail_path = "thumbnail/" + os.path.splitext(base_image_file_name)[0] + "_tmb.jpg"
            Helper.s3_upload(s3_bucket,thumbnail_path,s3_thumbnail_path)
            print("Thumbnail genrated and uploaded successfully")
            for file in processing_file_list:
                if os.path.exists(file):
                    os.remove(file)
            print("Process Completed Successfully")

    except Exception as error:
        raise error

