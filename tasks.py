from invoke import task


@task
def docker_build(c):
    c.run("docker build -f Dockerfile -t streamlit-app:latest .", pty=True)


@task
def docker_run(c, clean=False):
    c.run("docker run -p 8501:8501 streamlit-app:latest", pty=True)
