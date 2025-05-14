from storages.backends.s3boto3 import S3Boto3Storage
import os

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = False

class PublicMediaStorage(S3Boto3Storage):
    location = os.path.join('media', 'public')
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = 'media/private'
    default_acl = 'private'
    file_overwrite = False
