# Nittfest-Server
Server Application for NITTFEST.

<p align="center" > <img src="https://user-images.githubusercontent.com/63253383/146638088-96d83626-f121-46fc-9f7d-208b0f9fe725.png"></p>

# FastAPI
---
# Requirements
* [Pipenv](https://pipenv.pypa.io/en/latest/install/)
* [Docker](https://www.docker.com/get-started)

# Setup
 * Fork and Clone the Repo
    ```sh
    git clone < YOUR_FORK_URL >
    ```
 * Add remote upstream
    ```sh
    git remote add upstream < MAIN_REPO_URL>
    ```
 * cd into the folder
    ```sh
     git config core.hooksPath .githooks
    ```    
* Setup the virtualenv
   * Create a virtualenv for this project.
       ```sh
        pipenv install
        ```
    * Activate virtualenv for this project.
       ```sh
        pipenv shell
        ```
* Docker
    * Build docker Image.
        ```sh
        docker-compose -f docker-compose.dev build 
        ```
    *  Run docker Container.
        ```sh
        docker-compose -f docker-compose.dev up
        ```
* To Run Migrations
    * To run migrations
        ```sh
        pipenv run migrations
        ```
    * To auto-generate alembic migration scripts
        ```sh
        alembic revision --autogenerate -m <MIGRATION_MESSAGE>
        ```
