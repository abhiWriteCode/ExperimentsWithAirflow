## Apache [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

* For database -

  &nbsp;&nbsp;&nbsp;&nbsp;Sqlite3: `sudo apt-get install sqlite3`
  
  &nbsp;&nbsp;&nbsp;&nbsp;[Postgresql](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-up-database.html#setting-up-a-postgresql-database):
  ```bash
  >>> sudo apt-get install postgresql postgresql-contrib
  >>> sudo systemctl start postgresql.service
  >>> sudo -u postgres createuser --interactive
  Enter name of role to add: pg_db_super_usr
  Shall the new role be a superuser? (y/n) y
  >>> sudo -u postgres psql
  postgres=# CREATE DATABASE airflow_pg_db;
  postgres=# CREATE USER af_usr WITH PASSWORD 'af_pass'
  postgres=# GRANT ALL PRIVILEGES ON DATABASE airflow_pg_db TO af_usr;
  postgres=# \l
  postgres=# \c airflow_pg_db
  airflow_pg_db=# GRANT ALL ON SCHEMA public TO af_usr;
  ```


* ```bash
	python3 -m venv venv
	source venv/bin/activate
	pip3 install apache-airflow
	```

* ```bash
  airflow -h
  airflow webserver -h
  airflow db -h
  ```

* Edit `~/airflow/airflow.cfg`. Add `dags_folder = path/to/ExperimentsWithAirflow`

* ```bash
  airflow db migrate
  airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
  airflow webserver --port 8080
  airflow scheduler
  ```
  or simply `airflow standalone`

* `airflow db reset`
