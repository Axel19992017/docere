from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'docere-ni'
    location = 'assets-root/media'

class StaticStorage(S3Boto3Storage):
    bucket_name = 'docere-ni'
    location = 'assets-root/static'
