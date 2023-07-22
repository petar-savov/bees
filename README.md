Tool for data labelling and ML model output review.

## Database Setup

This project uses PostgreSQL as its primary data store. We recommend running PostgreSQL with Docker for the easiest setup.

1. **Install Docker**: If you don't have Docker installed, you can download it from [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop). Follow the instructions for your operating system.

2. **Pull the PostgreSQL Docker image**: This will download the PostgreSQL image which can be used to run a PostgreSQL container. Run the following command in your terminal:

    ```bash
    docker pull postgres
    ```

3. **Run the PostgreSQL container**: This will start a new PostgreSQL instance. The `-p` option maps your machine's port 5432 to the container's port 5432, which is the default port for PostgreSQL.

    ```bash
    docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
    ```

    In this command:
    - `--name some-postgres` gives the name "some-postgres" to the new Docker container.
    - `-e POSTGRES_PASSWORD=mysecretpassword` sets an environment variable in the container which sets the Postgres password to "mysecretpassword".
    - `-p 5432:5432` maps port 5432 on your host machine to port 5432 in the Docker container.
    - `-d` runs the container in the background.
    - `postgres` is the Docker image to use.

4. **Check your Docker containers**: You can check that the container is running using:

    ```bash
    docker ps
    ```

    You should see "some-postgres" in the output list.

5. **Connect to your database**: At this point, you should be able to connect to your database at `localhost:5432` with the username `postgres` and password `mysecretpassword`.


6. To populate the database:

       docker cp backend/fastapi/app/populate_db.sql some-postgres:/tmp/populate_db.sql
       
       docker exec -it some-postgres psql -U postgres -d postgres -f /tmp/populate_db.sql