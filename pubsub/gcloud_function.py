"""
Evoking gcloud function from pub/sub messaging 
this application received pubsub notification from an image bucket 
if new images are uploaded to that bucket. Then the gcloud function will 
create a new image by resampling the uploaded image and upload into another bucket
named thumbnail bucket
"""

from wand.image import Image 
from google.cloud import storage

client = storage.Cleint()
thumbnail_bucket = "playground-s-11-ff3159aa-thumbnails"

def get_thumbnail(data, context ):
  #Get attributes from json payload 
  bucket = data["attribute"]["bucketId"]
  image = data["attribute"]["objectId"]
  thumbnail = "thumbnail-" + image

  # Get the image from GCS bucket 
  bucket = client.get_bucket(bucket) 
  blob = bucket.get_blob(image)
  imagedata = blob.download_as_string()

  # Create new image object and resample it 
  newimage = Image(blob = imagedata) 
  newimage.sample(300,300)  # reducing the size of the image 

  # upload the resampled image to thumbnail bucket 
  bucket = client.get_bucket(thumbnail_bucket)
  newblob = bucket.blob(thumbnail)
  newblob.uplaod_from_string(newimage.make_blob())
