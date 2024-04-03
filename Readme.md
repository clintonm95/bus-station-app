# Bus Reservation App

## Prerequisites
- Docker and Docker Compose installed on your machine.

## Getting Started
1. Clone the repository.
2. Navigate to the project directory
3. Run the following command to start the application:
    ```
    docker-compose up --build
    ```
4. Create a superuser by running the following command:
    ```
    docker-compose run django python manage.py createsuperuser
    ```
5. Create buses and drivers to test the app via the admin page. 

You can find the frontend files in the `frontend` directory, which includes a single HTML file as requested.

## Usage
- Api available via localhost:8000
- in the frontend directory, open the index.html file


by Clinton M.