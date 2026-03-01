from datetime import datetime, timedelta

from airflow.decorators import dag
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
)
from tasks import show_path   # importe ta task

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="retail",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    default_args=default_args,
    catchup=False,
)
def retail():
    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_retail_dataset",
        dataset_id="retail",
        gcp_conn_id="gcp",
        exists_ok=True,
    )

    path_task = show_path()

    create_retail_dataset >> path_task

retail()
