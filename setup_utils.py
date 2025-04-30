import os

# Create the renamed folder and common.py module
new_folder = "dataspaces_utils"
os.makedirs(new_folder, exist_ok=True)

common_code = """import os
import uuid
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from io import BytesIO
from fitparse import FitFile
from dotenv import load_dotenv
import boto3

# Load environment variables
load_dotenv()

# Setup S3 client
def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=os.getenv("SUPABASE_S3_ENDPOINT"),
        aws_access_key_id=os.getenv("SUPABASE_S3_KEY_ID"),
        aws_secret_access_key=os.getenv("SUPABASE_S3_SECRET")
    )

# Get bucket name from env
bucket = os.getenv("SUPABASE_BUCKET")
"""

# Write the files
with open(f"{new_folder}/common.py", "w") as f:
    f.write(common_code)

with open(f"{new_folder}/__init__.py", "w") as f:
    f.write("# Init file for dataspaces_utils package")