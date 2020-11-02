"""
# Weather Data by ZIP Code

A scheduled DAG which fetches data from a OpenWeather api endpoint
and then writes it to S3

This DAG takes in the following Airflow variables 

- zip_code (default_var: 90210)
- aws_weather_bucket (default_var: air-traffic-control)

Additionally this DAG utilizes the environmental variable OPEN_WEATHER_API_KEY for authenticating into the API 
"""
import os
from airflow import DAG
from airflow.operators import PythonOperator
from airflow.models import Variable
from local_operators.fetch_weather import get_weather_by_zip
from local_operators.s3_upload import write_to_s3
from datetime import datetime
args = {
    'owner': 'evan_tang',
    'start_date': datetime(2020, 10, 31),
    'provide_context': True
}

dag = DAG(
    'weather_by_zip', 
    schedule_interval='0 4 * * *',
    default_args=args
) 

dag.doc_md = __doc__

with dag:
    fetch_from_weather_api = PythonOperator(
        task_id='weather_api_call',
        python_callable=get_weather_by_zip,
        op_kwargs={
            'zip_code':  Variable.get("zip_code", default_var=90210),
            'api_token': os.environ.get('OPEN_WEATHER_API_KEY')
        }
    )

    s3_uploader = PythonOperator(
        task_id='s3_upload',
        python_callable=write_to_s3,
        op_kwargs={
            'bucket':  Variable.get("aws_weather_bucket", default_var='air-traffic-control'),
            'key': 'weather_by_zip/data/{}_{}_weather_data.json'.format(
                str(Variable.get("zip_code", default_var=90210)),
                datetime.now().strftime('%Y%m%d_%H:%M:%S')
            ),
            'task_id': 'weather_api_call'
        }
    )

    fetch_from_weather_api >> s3_uploader