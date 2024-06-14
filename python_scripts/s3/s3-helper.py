import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Create a new S3 bucket
def create_bucket(bucket_name):
    """
    Create a new S3 bucket.
    
    Args:
        bucket_name (str): The name of the bucket to create.
    """
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")

# Upload a file to an S3 bucket
def upload_file(bucket_name, file_path, object_key):
    """
    Upload a file to an S3 bucket.
    
    Args:
        bucket_name (str): The name of the bucket to upload the file to.
        file_path (str): The local path of the file to upload.
        object_key (str): The key of the object in the bucket.
    """
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"File '{file_path}' uploaded to '{bucket_name}' with key '{object_key}'.")

# Download a file from an S3 bucket
def download_file(bucket_name, object_key, file_path):
    """
    Download a file from an S3 bucket.
    
    Args:
        bucket_name (str): The name of the bucket to download the file from.
        object_key (str): The key of the object in the bucket.
        file_path (str): The local path to save the downloaded file.
    """
    s3_client.download_file(bucket_name, object_key, file_path)
    print(f"File '{object_key}' downloaded from '{bucket_name}' and saved to '{file_path}'.")

# List all objects in an S3 bucket
def list_objects(bucket_name):
    """
    List all objects in an S3 bucket.
    
    Args:
        bucket_name (str): The name of the bucket to list objects from.
    """
    response = s3_client.list_objects(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"Object: {obj['Key']}")
    else:
        print(f"No objects found in bucket '{bucket_name}'.")

# Delete an object from an S3 bucket
def delete_object(bucket_name, object_key):
    """
    Delete an object from an S3 bucket.
    
    Args:
        bucket_name (str): The name of the bucket to delete the object from.
        object_key (str): The key of the object to delete.
    """
    s3_client.delete_object(Bucket=bucket_name, Key=object_key)
    print(f"Object '{object_key}' deleted from '{bucket_name}'.")

# Delete a bucket and all its objects
def delete_bucket(bucket_name):
    """
    Delete a bucket and all its objects.
    
    Args:
        bucket_name (str): The name of the bucket to delete.
    """
    response = s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")

# Example usage
if __name__ == "__main__":
    # Create a new bucket
    create_bucket("my-bucket")
    
    # Upload a file to the bucket
    upload_file("my-bucket", "/path/to/file.txt", "file.txt")
    
    # Download a file from the bucket
    download_file("my-bucket", "file.txt", "/path/to/save/file.txt")
    
    # List all objects in the bucket
    list_objects("my-bucket")
    
    # Delete an object from the bucket
    delete_object("my-bucket", "file.txt")
    
    # Delete the bucket
    delete_bucket("my-bucket")