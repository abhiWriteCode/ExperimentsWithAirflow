from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from connect import downloading, uploading
from client_1 import transformer_A, transformer_B
from client_2 import transformer_C, transformer_D
import finish



with DAG(
	dag_id="Complex_ETL_pipeline",
	default_args={
        "owner": "airflow",
        "start_date": datetime(2022, 1, 1),
        'depends_on_past': False,
    },
    schedule_interval="2 * * * *",
    catchup=False,
    tags=['ETL']
) as dag:

	download_files = PythonOperator(
	    task_id="download_files",
	    python_callable=downloading.download,
	)

	transformer_a = PythonOperator(
	    task_id="transformer_a",
	    python_callable=transformer_A.data_transform,
	)

	transformer_b = PythonOperator(
	    task_id="transformer_b",
	    python_callable=transformer_B.data_transform,
	)

	transformer_c = PythonOperator(
	    task_id="transformer_c",
	    python_callable=transformer_C.data_transform,
	)

	transformer_d = PythonOperator(
	    task_id="transformer_d",
	    python_callable=transformer_D.data_transform,
	)

	upload_files = PythonOperator(
	    task_id="upload_files",
	    python_callable=uploading.upload,
	)

	exit_msg = PythonOperator(
	    task_id="exit_msg",
	    python_callable=finish.exit,
	)

	download_files >> [transformer_a, transformer_b, transformer_c, transformer_d] >> exit_msg

print('SUCESSFULLY EXECUTED')
