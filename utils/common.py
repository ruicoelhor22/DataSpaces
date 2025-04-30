
import os
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
