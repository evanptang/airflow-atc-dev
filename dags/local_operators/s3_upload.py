import boto3 
import os

def write_to_s3(bucket, key, task_id, **kwargs):
    ti = kwargs['ti']
    weather_data = ti.xcom_pull(task_ids=task_id)
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

    client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    aws_response = client.put_object(
        Body=weather_data,
        Bucket=bucket,
        Key=key
    )

    return aws_response