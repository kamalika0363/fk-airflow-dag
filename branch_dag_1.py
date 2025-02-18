from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define default_args for DAG execution
default_args = {
    'owner': 'Kamalika',
    'start_date': datetime(2023, 2, 7),
    'retries': 1,
}

# Create the DAG object
dag = DAG(
    'dag_branch_1',  # DAG ID
    default_args=default_args,
    description='A simple custom DAG',
    schedule_interval='@daily',  # This will run once a day
)

# Define the tasks (these are the individual jobs)
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set the task dependencies (order of execution)
start_task >> end_task
