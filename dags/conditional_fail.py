"""
# Conditional Fail DAG

A DAG which looks for an Airflow Variable - if it finds it, the DAG raises a runtime error

This DAG takes in the following Airflow variables 

- conditional_failure (default_var: None)

"""

import os
from airflow import DAG
from airflow.operators import PythonOperator
from airflow.models import Variable
from local_operators.conditional_fail import check_conditional_fail
from datetime import datetime
args = {
    'owner': 'evan_tang',
    'start_date': datetime(2020, 10, 31),
    'provide_context': True
}

dag = DAG(
    'conditional_fail',
    schedule_interval='0 * * * *', 
    default_args=args
)

dag.doc_md = __doc__ 


with dag:
    fail_on_condition = PythonOperator(
        task_id='fail_on_condition',
        python_callable=check_conditional_fail,
        op_kwargs={
            'conditional_value': Variable.get("conditional_fail", default_var=None)
        }
    )