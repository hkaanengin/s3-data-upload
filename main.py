from save_csv_to_s3 import Hot_AWS
from config.config import *


Hot_AWS(profile).upload_to_s3(bucket_name, csv_file_path, object_name)
