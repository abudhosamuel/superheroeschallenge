
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)Python Application

# Superheroes and Powers API

This project is a Flask-based RESTful API for managing superheroes and their superpowers. It allows you to view all superheroes, see detailed information about individual heroes and their powers, and update power descriptions. The API also allows assigning strengths to superheroes for a given power, and includes all necessary validations and error handling.

This project was developed to demonstrate building and managing relational data using Flask and SQLAlchemy with correct relationships and validations. The relationships between models are:

A Hero has many Powers through HeroPower.
A Power has many Heroes through HeroPower.
A HeroPower connects a Hero and a Power with an associated strength.
The API follows RESTful principles, making it easy to manage the resources using standard HTTP verbs.


## Features


List all heroes: GET /heroes
View details of a specific hero: GET /heroes/:id
List all powers: GET /powers
View details of a specific power: GET /powers/:id
Update a power's description: PATCH /powers/:id
Assign a strength to a hero for a specific power: POST /hero_powers

## Installation
Installation Requirements
Before you run this project, ensure you have the following installed:

Python 3.7 or higher
Flask: A micro web framework for building web applications in Python.
Flask-SQLAlchemy: SQLAlchemy integration for Flask to interact with the database.
Flask-Migrate: A Flask extension for handling SQLAlchemy database migrations.

##Installation and Setup Instructions
Clone the Repository:

First, clone the repository to your local machine:

git clone https://github.com/abudhosamuel/superheroeschallenge
cd superheroeschallenge

Create a Virtual Environment:
pipenv install

Create and activate a virtual environment for the project:
pipenv shell

Install Required Packages:

pip install Flask Flask-SQLAlchemy Flask-Migrate

Create a Database:

Initialize the SQLite database for the project. Run the following commands:

flask db init       # Create the migrations folder
flask db migrate    # Generate migration files
flask db upgrade    # Apply migrations and create the Database

Seed the Database:

python seed.py


Run the Flask Application:

python app.py
The app will run on http://127.0.0.1:5000 by default.
## Running Tests


How to Test the API
You can use tools like Postman or curl to test the various endpoints of the API. Here are some sample requests:

1. List All Heroes
Endpoint: GET /heroes
Request: http://127.0.0.1:5000/heroes


2. View Details of a Specific Hero
Endpoint: GET /heroes/:id
Request: http://127.0.0.1:5000/heroes/1

3. List All Powers
Endpoint: GET /powers
Request: http://127.0.0.1:5000/powers


4. Update a Power's Description
Endpoint: PATCH /powers/:id
Request: http://127.0.0.1:5000/powers/1


5. Assign a Strength to a Hero for a Specific Power
Endpoint: POST /hero_powers
Request: http://127.0.0.1:5000/hero_powers

## Authors

- [@abudhosamuel](https://www.github.com/abudhosamuel)




## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

Acknowledgements

Font Awesome
Feel free to contribute to the project by submitting a pull request or opening an issue.

