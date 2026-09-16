def load_to_bigquery(df, project_id, dataset_id, table_id):
    """Load the processed DataFrame into BigQuery."""
    from google.cloud import bigquery

    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()
    return table_ref
