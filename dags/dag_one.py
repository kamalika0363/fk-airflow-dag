from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator


default_args = {
    'owner'                 : 'Kamalika',
    'description'           : 'Use of the GitSync',
    'depend_on_past'        : False,
    'start_date'            : datetime(2025, 1, 1),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}

with DAG('docker_dag_sample', default_args=default_args, schedule_interval="5 10 * * *", catchup=False) as dag:
    t1 = BashOperator(
        task_id='from_git_sync',
        bash_command='echo "hello world"'
    )

t1

