from datetime import datetime, timedelta
import time
from airflow import DAG
from airflow.operators.python import PythonOperator


def first_function_execute(**kwargs):
    print("func: first_function_execute")
    time.sleep(3)
    return 'first_function_execute return'


def second_function_execute(**kwargs):
    print("func: second_function_execute")
    time.sleep(3)
    third_function_execute()
    time.sleep(2)
    return 'second_function_execute return'


def third_function_execute(**kwargs):
    print("func: third_function_execute")
    time.sleep(3)
    return 'third_function_execute return'


with DAG(
        dag_id="first_dag",
        default_args={
            "owner": "airflow",
            "start_date": datetime(2021, 1, 1),
        },
        schedule_interval="@daily",
        catchup=False,
        tags=['ETL']) as dag:

    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
    )

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
    )


first_function_execute >> second_function_execute
