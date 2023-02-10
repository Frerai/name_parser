README.md
# Introduction

The "Name Parser" is a coding assignment. It's a tool designed to take an input string of a full name in various formats, and parse them in parts consisting of a first name and last name, regardless of the input format.

The assignment is written as a REST service with FastAPI framework. 

## Setup

In order to use this service, follow the steps below:

1. Clone the remote repository: `$ git clone <git@github.com:Frerai/name_parser.git>`

2. Build the Docker image: `$ docker build -t my-name-parser-app .`

   _Note: "my-name-parser-app" is the image name; choose whatever desired._

3. Run the Docker container: `$ docker run -d -p 8200:8200 --name name-parser`
    
    _Note: name-parser is the container name; choose whatever desired._

## Usage
### Healthcheck
A healthcheck can be made using a tool such as Postman by reaching the following URL: `http://127.0.0.1:8000/health/live`

Or alternatively, using a curl command from the terminal: `$ curl --location --request GET 'http://127.0.0.1:8000/health/live'`


### Endpoint

After the container is up and running, access the FastAPI endpoint at: `http://localhost:8200/docs`

_Follow the intuitive instructions of FastAPIs Swagger UI and test it out_

    Or alternatively, an input string can be given with a curl command from the terminal: 
    $ curl --location --request GET 'http://127.0.0.1:8000/api/v1/parse?full_name=full-name%20with-a-space'

## Tests
To run tests inside the Docker container, use the following command: `$ docker exec name-parser python -m pytest tests/ -vv`

_Note: name-parser is the container name, set earlier when running the docker run command._