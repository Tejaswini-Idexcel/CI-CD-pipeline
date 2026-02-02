import boto3

bucket_name = "mylambdapipelinestack-pipelineartifactbucket-btkf1w8skp1p"
s3 = boto3.client('s3')

# Delete all versions
versions = s3.list_object_versions(Bucket=bucket_name)
for version in versions.get('Versions', []):
    s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
    print(f"Deleted {version['Key']} version {version['VersionId']}")

# Delete all delete markers
for marker in versions.get('DeleteMarkers', []):
    s3.delete_object(Bucket=bucket_name, Key=marker['Key'], VersionId=marker['VersionId'])
    print(f"Deleted marker {marker['Key']} version {marker['VersionId']}")

print("Bucket emptied successfully")
