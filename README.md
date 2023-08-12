# todo-flask-app
This repository contains a todo flask app that is deployed via docker compose. The main purpose of this repository is to demonstrate docker volume, networks, and docker compose.

**Prerequisites:**
- Docker
- Docker Compose

## Steps:
1. Open your terminal and navigate to the project directory.
2. Create an empty directory `data` in the project folder, this folder will store MySQL database data. docker containers are ephemeral and any data created inside the container will be lost when the container is removed. Thats why, we will use docker volumes to persist the database even when containers are destroyed.
3. Set the MySQL database passwords in `api.env` and `mysql.env` files. These passwords have been set as PLACEHOLDER by default.
![image](https://github.com/kunal-gohrani/todo-flask-app/assets/47574597/717a1664-b9fa-40df-aa5f-dd4f4503b155)
4. Deploy the containers using the command `docker-compose up -d`, this will build the docker image and start the containers.

## Docker Compose Configuration Explanation

This Docker Compose configuration file is designed to facilitate the deployment and orchestration of a multi-container application. It defines two services, api and mysql, and sets up their interactions, network communication, and environment variables.

### api Service
The api service represents the main application component. It is built from the Dockerfile present in the current directory and exposes its functionality on port 5001, mapped to the host's port 5000. This service relies on environment variables specified in the api.env file, enabling dynamic configuration of the application.

The networks section indicates that the api service should be part of both the public and private networks. The public network is a bridge network, likely intended for external access, while the private network serves internal communication between containers.

The restart: always directive ensures that the api service automatically restarts in case of failure. Additionally, the depends_on field lists mysql as a dependency, meaning the api service will wait until the mysql service is up and running before starting.

### mysql Service
The mysql service utilizes the latest MySQL Docker image available. Environment variables from the mysql.env file configure this containerized MySQL instance. The service exposes its MySQL port (3306) to the host machine, enabling external connections.

The networks section connects the mysql service to the private network, allowing internal communication with other containers on the same network. The volumes field ensures that data in the /var/lib/mysql directory of the mysql container is persisted on the host machine within the ./data directory.

### Networks
The two networks, public and private, are defined in the networks section. The public network is a bridge network, which can be accessed externally. On the other hand, the private network is utilized for internal communication between the containers. This separation ensures a clear distinction between external and internal connections.

By utilizing this Docker Compose configuration, you can easily deploy and manage a multi-container application consisting of an API service and a MySQL database, all with the defined network connections, environment variables, and restart behaviors.

