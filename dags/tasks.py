from airflow.decorators import task

@task
def show_path():
    path = "gs://dbt_online_retails/raw/online_retail.csv"
    print(path)
    return path