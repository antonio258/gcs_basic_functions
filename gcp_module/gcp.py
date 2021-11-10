from google.cloud import storage


def download(bucket_name, blob_path, down_path, project=''):
    """
    Download file from google storage
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        down_path: local download path
        project: project name

    Returns:
    """
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.download_to_filename(down_path)


def upload(bucket_name, blob_path, file_path, project=''):
    """
    Upload file to google storage
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        file_path: local file path
        project: project name

    Returns:
    """
    storage_client = storage.Client(project=project)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)


def list_blobs(bucket_name, blob_path, project=''):
    """
    List blobs of google storage bucket
    Args:
        bucket_name: name of bucket
        blob_path: path of blob
        project: project nome

    Returns:
    """
    storage_client = storage.Client(project=project)
    for blob in storage_client.list_blobs(bucket_name, prefix=blob_path):
        print(blob.name)
