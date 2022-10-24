from benzinpreise import get_location
from airflow import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022,9,25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'Benzinpreise',
    default_args=default_args,
    description='',
    schedule_interval=timedelta(minutes=15),
)

load = DockerOperator(
    task_id='docker_command',
    image='benzinpreis_image',
    api_version='auto',
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag
)

load
