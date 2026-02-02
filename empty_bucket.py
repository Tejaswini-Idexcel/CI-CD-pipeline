import json
import boto3
import sys

bucket_name = ""
try:
    with open('bucket_name.txt', 'r') as f:
        bucket_name = f.read().strip()
except:
    print("No bucket found")
    sys.exit(1)

if not bucket_name:
    print("Empty bucket name")
    sys.exit(1)

print(f"Emptying bucket: {bucket_name}")
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.object_versions.delete()
print("Versions deleted")
