# Nittfest-Server

Server-Application for NITTFEST.

<p align="center" > <img src="https://user-images.githubusercontent.com/63253383/146638088-96d83626-f121-46fc-9f7d-208b0f9fe725.png"></p>

# FastAPI
---
# Requirements

- [Pipenv](https://pipenv.pypa.io/en/latest/install/)
- [Docker](https://www.docker.com/get-started)

# Setup

- Fork and Clone the Repo
  ```sh
  git clone <YOUR_FORK_URL>
  ```
- Add remote upstream
  ```sh
  git remote add upstream <MAIN_REPO_URL>
  ```
- cd into the folder
  ```sh
   git config core.hooksPath .githooks
  ```
- copy content of .env.example to .env
  ```sh
   cp .env.example .env
  ```  
- Setup the virtualenv
  - Create a virtualenv for this project.
    ```sh
     pipenv install
    ```
  - Activate virtualenv for this project.
    ```sh
     pipenv shell
    ```
  - Install dev dependencies
    ```sh
     pipenv install --dev
    ```
- Docker
  - Build and Up the Docker Container.
    ```sh
    docker-compose -f docker-compose.dev.yml up --build
    ```
- To Run Migrations
  - To make Migrations
    ```sh
    docker exec nittfest_server alembic revision --autogenerate -m <COMMIT_MESSAGE>
    ```
  - To run Migrations
    ```sh
    docker exec nittfest_server alembic upgrade head
    ```
