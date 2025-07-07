from invoke import task 

@task
def updb(c):
    c.run("docker compose up -d postgres")

@task
def buildapp(c):
    c.run("docker compose build app")

@task(pre=[updb, buildapp])
def upapp(c):
    c.run("docker compose up -d app")

@task
def makerevision(c, message):
    c.run(f'alembic revision -m {message}')

@task
def migrate(c):
    result = c.run("docker compose exec app alembic upgrade head", warn=True)
    if result.failed:
        print("Migration failed")
        exit(1)
    else:
        print("Migration successful")

@task
def down(c):
    print("Stopping and removing containers...")
    c.run("docker compose down -v")
