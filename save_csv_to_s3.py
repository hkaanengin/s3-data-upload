import boto3
import os

class Hot_AWS:
    def __init__(self, prof_name) -> None:
        self.session = boto3.Session(profile_name=prof_name)        
        print(self.session)
    
    def create_s3_bucket(self, bucket):
        s3_resource = self.session.resource("s3",verify=False)          #verification needs to be implemented
        s3_resource.create_bucket(Bucket=bucket)

    def upload_to_s3(self, bucket, filepath, filename=None):
        s3_filename = os.path.basename(filepath) if filename is None else filename
        s3_resource = self.session.client("s3",verify=False)            #verification needs to be implemented
        s3_resource.upload_file(filepath, bucket, s3_filename)
        
    def create_glue_database(self):
        client = self.session.client("glue")

