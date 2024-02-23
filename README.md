## Commands


* ```bash
	python3 -m venv venv
	source venv/bin/activate
	pip3 install apache-airflow
	```

* `airflow -h`

* `airflow db -h`

* `airflow webserver -h`

* Edit `~/airflow/airflow.cfg`. Add `dags_folder = path/to/ExperimentWithAirflow`

* `airflow db init`

* `airflow users  create --role Admin --username admin --email admin --first name admin --lastname admin --password admin`

* `airflow scheduler`

* `airflow webserver --port 8080`

* `airflow db reset`
