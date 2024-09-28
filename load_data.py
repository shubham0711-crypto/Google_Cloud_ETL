from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the GCS bucket."""
    
    # Initialize a client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a blob (object) in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file to the blob
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

# File details
bucket_name = 'bkt-employee-data-07'  # Replace with your bucket name
source_file_name = 'employee_data.csv'  # Replace with your local file name
destination_blob_name = 'employee_data'  # Replace with the object name in GCS

# Upload the file to GCS
upload_to_gcs(bucket_name, source_file_name, destination_blob_name)