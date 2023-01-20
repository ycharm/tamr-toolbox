"""
An example script to demonstrate the use of the gcs_upload function to upload file.
"""

import tamr_toolbox as tbox
from google.cloud import storage

gcs_client = storage.Client()

# uploads file to gcs
# upload a local file "my_local_directory/my_file.txt" to "gs://my-bucket/path-to-file"
tbox.filesystem.cloud.gcs_upload(
    cloud_client=gcs_client,
    source_filepath="my_local_directory/my_file.txt",
    destination_filepath="path-to-file",
    bucket_name="my-bucket",
)
