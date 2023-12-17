# Python API

This project is simple Python API template.

### Back End: `api`
- Python
- Postgres
- Poetry

### Basic Python Packages
- fastapi
- uvicorn
- pydantic
- sqlalchemy
- pytest

### Containerization
- Docker
- Docker Compose

## Prerequisites

To run this project, you need to have Docker, Pyenv, and Poetry installed on your machine. If you don't have it
installed, you can follow this guide:

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
- [Install Poetry](https://python-poetry.org/docs/)

## Simple Setup

1. Clone the repo:
    ```shell
    git clone git@github.com:eduardoagarcia/python-template.git
    ```
2. Navigate to the project directory:
    ```shell
    cd python-template
    ```
3. Initialize and start the app:
    ```shell
    make init
    ```

## App Links
Once your app is up and running, these are two helpful links to get started:
- [Health Check](http://localhost:8000/health-check)
- [Hello World](http://localhost:8000/api/v1/hello/world)

## Installing Python and Poetry for Local Development

Install Python `3.12.0b2` (or most recent version)
```shell
env CONFIGURE_OPTS='--enable-optimizations' pyenv install 3.12.0b2
```
Note: if you run into issues, [this openssl thread](https://stackoverflow.com/questions/77237751/3-12-install-fails-on-intel-macbook-pro) might help.

Set `3.12.0b2` as the default version
```shell
pyenv global 3.12.0b2
```

Determine where the `3.12.0b2` version is located on your machine
```shell
pyenv which python
```

Update Poetry to use the correct Python version:
```shell
poetry env use {example: <your path>/.pyenv/versions/3.12.0b2/bin/python}
```

Install Poetry project via make:
```shell
make poetry-install
```

After installing Poetry on your machine, if you need to configure your IDE (like IntelliJ) with the Python interpreter, it will be located here:
```text
python-template/api/.venv/bin/python
```

## Running Python API Tests

Run all Python API tests via make:
```shell
make run-tests
```

## View API Logs

View logs via make:
```shell
make logs
```

## Additional `Makefile` Usage

The project provides a `Makefile` with several additional commands to manage the project:

- **init**: Initializes and boots the api
    ```shell
    make init
    ```

- **build**: Builds the Docker images for the project
    ```shell
    make build
    ```

- **destroy**: Stops and removes containers, networks, images, and volumes
    ```shell
    make destroy
    ```

- **start**: Starts the containers
    ```shell
    make start
    ```

- **stop**: Stops the running containers
    ```shell
    make stop
    ```

- **shell-api**: Opens a shell in the API (backend) container
    ```shell
    make shell
    ```

- **all**: Default: calls the `init` command
    ```shell
    make all
    ```

## License

This project is licensed under the terms of the MIT license.