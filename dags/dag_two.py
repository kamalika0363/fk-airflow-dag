from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, Airflow!")

with DAG(
    dag_id="simple_hello_dag",
    start_date=datetime(2024, 2, 14),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    task_hello = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )

    task_hello
