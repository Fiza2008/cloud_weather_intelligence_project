from pathlib import Path

def upload_to_gcs(local_file, bucket_name, object_name):
    """Upload a file to Google Cloud Storage.

    Requires:
        pip install google-cloud-storage
        gcloud auth application-default login
    """
    from google.cloud import storage

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(str(local_file))
    return f"gs://{bucket_name}/{object_name}"
