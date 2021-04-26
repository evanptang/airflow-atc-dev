import boto3

def query_aws_last_modifed(bucket, prefix):
    """
    function that fetches the last_modified key for objects with a prefix
    """
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    last_modifed_dict = dict()
    for s3file in my_bucket.objects.filter(Prefix=prefix).limit(1000):
        last_modifed_dict[s3file.key] = s3file.last_modified
    return last_modifed_dict