Project name:
Test work SVIT IT

Project description:

This project is an API application for saving logs. The application allows authorized users to upload logs in "csv" format, as well as in the form of RAR, ZIP, 7z archives. The ability to view logs and work with filters is also implemented. It uses Django REST Framework (DRF) as its API.

Development Tools:

    Python >= 3.10
    
    Django == 4.2.4
    Django REST Framework 3.14.0
    
    PostgreSQL

    Docker 20.10.2

Installation and running the project:

1) Clone the repository

       https://github.com/Costello90/test_work_svit_it.git
2) Create a virtual environment

       cd test_work_svit_it
       python -m venv venv

3) Activate virtual environment

   Linux

       source venv/bin/activate

   Windows

       ./venv/Scripts/activate
4) Install dependencies:

       pip install -r requrements.txt
5) Set up PostgreSQL DB with your credentials or use default Django DB (SQLite3).
6) Since this is a test task, the '.env' file is uploaded to the repository.
7) Create migrations and apply them to the database

       python manage.py makemigrations
       python manage.py migrate
8) Create superuser

       python manage.py createsuperuser
9) Run server

       python manage.py runserver
10) Links

    DRF API 

        http://127.0.0.1:8000/

    Django admin interface 

        http://127.0.0.1:8000/admin

    API documentation 

        http://127.0.0.1:8000/swagger


Deploying the application using Docker:

1) Ensure that Docker and Docker Compose are installed on your system.

2) Since this is a test task, the '.env' file is uploaded to the repository.

3) Build the Docker images:

       docker-compose build
4) Start the containers:

       docker-compose up
5) You can now open a web browser and see the application in action at the following address.
       
       http://127.0.0.1:8000

License:

Copyright (c) 2023-present, Kostiantyn Kondratenko