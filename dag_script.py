from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from Zipco_Foods_Extraction import run_extraction
from Zipco_Foods_Transformation import run_transformation
from Zipco_Foods_loading import run_loading

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 7),
    'email': "nelxzxi@gmail.com",
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'zipco_foods_pipeline',
    default_args=default_args,
    description='This represents Zipco Foods Data Management pipeline',
    schedule_interval='@daily',
)

extraction_task = PythonOperator(
    task_id='Zipco_Foods_Extraction_layer',
    python_callable=run_extraction,
    dag=dag,
)

transformation_task = PythonOperator(
    task_id='Zipco_Foods_Transformation_layer',
    python_callable=run_transformation,
    dag=dag,
)

loading_task = PythonOperator(
    task_id='Zipco_Foods_loading_layer',
    python_callable=run_loading,
    dag=dag,
)

extraction_task >> transformation_task >> loading_task