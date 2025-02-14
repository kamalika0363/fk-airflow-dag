from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, Airflow!")

# Define the DAG
default_args = {
    'owner': 'Kamalika',
    'start_date': datetime(2024, 2, 15),
    'retries': 1,
}

dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple DAG that prints Hello, Airflow!',
    schedule_interval='@daily',
    catchup=False,
)

# Define the task
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

hello_task
