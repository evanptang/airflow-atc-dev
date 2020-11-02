"""
# Quotes

A scheduled DAG which fetches data from a rapid api endpoint
and then writes it to S3

This DAG takes in the following Airflow variables 

- aws_quote_bucket (default_var: air-traffic-control)

Additionally this DAG utilizes the environmental variable RAPID_API_KEY for authenticating into the API 
"""

import os
from airflow import DAG
from airflow.operators import PythonOperator
from airflow.models import Variable
from local_operators.fetch_quotes import get_quotes_data
from local_operators.s3_upload import write_to_s3
from datetime import datetime
args = {
    'owner': 'evan_tang',
    'start_date': datetime(2020, 10, 31),
    'provide_context': True
}

dag = DAG(
    'quotes_api',
    schedule_interval='0 */4 * * *', 
    default_args=args
)

dag.doc_md = __doc__ 

with dag:
    fetch_from_quotes_api = PythonOperator(
        task_id='quotes_data_api_call',
        python_callable=get_quotes_data,
        op_kwargs={
            'api_token': os.environ.get('RAPID_API_KEY')
        }
    )

    s3_uploader = PythonOperator(
        task_id='s3_upload',
        python_callable=write_to_s3,
        op_kwargs={
            'bucket':  Variable.get("aws_quotes_bucket", default_var='air-traffic-control'),
            'key': 'quotes_data/data/{}_data.json'.format(
                datetime.now().strftime('%Y%m%d_%H:%M:%S')
            ),
            'task_id': 'quotes_data_api_call'
        }
    )

    fetch_from_quotes_api >> s3_uploader
