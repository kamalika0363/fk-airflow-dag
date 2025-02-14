from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator


default_args = {
    'owner'                 : 'Kamalika',
    'description'           : 'Use of the GitSync',
    'depend_on_past'        : False,
    'start_date'            : datetime(2025, 2, 2),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}
# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo_dag", start_date=datetime(2025, 1, 1), schedule="0 0 * * *") as dag:
 # Tasks are represented as operators
 hello = BashOperator(task_id="hello", bash_command="echo hello")

 @task()
 def airflow():
  print("airflow")

 # Set dependencies between tasks
 hello >> airflow()
