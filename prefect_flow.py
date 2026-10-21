from prefect import flow, task

@task
def run_pipeline_step():
    print("Executing hourly data fetch and quality checks...")
    return True

@flow(name="Hourly HackInsight Pipeline", schedule="5 * * * *")
def hourly_flow():
    run_pipeline_step()

if __name__ == "__main__":
    hourly_flow()
