# FizzBuzz REST Server using Python Flask

The REST server is built using python Flask framework, and the API endpoints have been documented using SwaggerUI and API is hosted on Render.<br><br>
This project is a submission for the Roche Hackathon conducted by DoSelect.

Production URL (documented API) - https://fizzbuzz-rest-server.onrender.com/api/docs

## Table of Contents

- [Objective](#objective)
- [Installation](#installation)
- [Unit Testing](#unittesting)
- [Running the API](#runningtheapi)
- [API Documentation](#apidocumentation)
- [Python packages used](#pythonpackagesused)
- [Production Server](#productionserver)
- [Conclusion](#conclusion)

## Objective

To Implement a robust and production-ready Fizz-Buzz REST Server that follows the classic Fizz-Buzz logic.<br>
The server should expose a REST API endpoint, with the additional feature of a statistical endpoint.

- REST API Endpoint
  - Accept five parameters: three integers (int1, int2, and limit) and two strings (str1 and str2).
  Return a list of strings containing numbers from 1 to limit.
  Replace multiples of int1 with str1, multiples of int2 with str2, and multiples of both int1 and int2 with str1str2

- Production Ready
  - Ensure that the server is ready for production use.
  - Prioritize clean and maintainable code to facilitate future development by other developers.
 
- Statistics Endpoint
  - Add a statistics endpoint that accepts no parameters.
  - Return the parameters corresponding to the most used request.
  - Include the number of hits for the most frequent request.
 
- Unit Tests
  - Develop comprehensive unit tests to validate the functionality of your server.

## Installation(local environment)

- Ensure Python 3.10.x version is installed on your system.
- Download and extract the zip file for the project OR git clone the project in your local directory.
- Navigate to the root folder of the project.
- Activate python virtual environment using command: **python venv\Scripts\activate**
- Install the neccessary packages from requirements.txt file using command: **pip -m install requirements.txt**

## Unit Testing

- Comprehensive unit tests have been created for the API
- Once the project has ben installed the unit tests can be executed by running the following steps
  - Navigate to the root folder of the project
  - run command on terminal: python -m unittest
  - This command will run all the tests listed in tests/tests.py file

## Running the API

- Once the installation is completed, run the api using command: **flask run**
- The app will start running on the localhost server (http://localhost:5000/api/hello-world)
- Access API endpoints as per the API documentation using Postman/Swagger (http://localhost:5000/api/docs)

## API Documentation

- API documentation is provided using Swagger UI
- Navigate the Swagger documentation (http://localhost:5000/api/docs)
- Select the localhost server from the dropdown (http://localhost:5000)
- The REST API sever has 3 endpoints defined
  - Get the FizzBuzz logic implemented strings as per the query parameters
  - Get the count of the highest requests
  - Get the count of the highest requests for a given query parameter
- Access the endpoints from the swagger UI provding the relevant parameters

## Python packages used

- flask 3.0.0
- flask-swagger-ui 4.11.1
- Werkzeug 3.0.1
- python-dotenv 1.0.0
- gunicorn 21.2.0

## Production Server

- The API is hosted on a Render server
- Production endpoints
  - SwaggerUI - https://fizzbuzz-rest-server.onrender.com/api/docs
  - API - https://fizzbuzz-rest-server.onrender.com/api/hello-world
 
## Conclusion

- The project is a simple demonstration of implementing a REST server using flask, a lightweight web framework of python
- All the objectives of the problem statement have been implemented in the project

## Credits

- This project is solely developed by Ritwik Gupta (ritwikgupta98@gmail.com), as a part of the submission for the Roche Hackathon conducted by DoSelect.
- Some refernces have been taken from the below articles
  - Deployment: https://shorturl.at/gmwDH
  - Unit Testing: https://www.dataquest.io/blog/unit-tests-python/




