from diamond_mod import write_df
from prefect import flow, task


@task
def diamond_pipeline():
    write_df()


@flow
def diamond_api():
    print("Pipeline is running")
    diamond_pipeline()


if __name__ == "__main__":
    diamond_api()
