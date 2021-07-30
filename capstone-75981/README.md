# Capstone project

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py
export
```

To run the server, execute:

```bash
flask run
```

## Introdution

- The capstone project follows RESTful principles, including naming of endpoints, use of HTTP methods GET, POST, PATCH and DELETE. The project handles errors using unittest library to test each endpoint for expected behaviour and error handling if applicable.

- The purpose of this project is for the completion of the Udacity fullstack developer course.

## Getting Started

- Base URL: At present this app can be run locally and also on heroku. The backend app is hosted at the default, http://127.0.0.1:5000/ or by visiting https://capstone-75981.herokuapp.com/ , which set as a proxy in the frontend configuration.

- Authentication:
```
        casting_assistant_token :
            Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZDA4ZGYyYjcyYTlmMDA2YTI5NmY5MiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTI2NywiZXhwIjoxNjI3NjQ4NDY3LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.M8LWKFSrmOnaiQnrN66QFSQB_diasdbTiDCd-R0ysjEl5M7u1IhZhBwJ3pqGhHswxHMaTkoTtjaBV0bdvKlLYDneCO-b6pjmFD3poyPEMPGTfZczgj3T0OAzkwToKeiC1shFLOow3-fcl0m-9MJcAPtam3KzidIzjef18EhcWVAOZYsLghd3nWsBu90_In_sTdeUh8_4CMJmmPKsrS_UQc35Na1niPye1mer9xGcp9bKDl6AZ54pDKPQRlvosMv2PfE8ZRJ0yAveR4UsP099jBsuGkby7BeYSPqXyvKzrhc4NEAAVTVwx7GNmtKCfjav8OeJukS7Oqx5eIJADqzN9w
        

        casting_director_token :
            Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMDI1Mzk3ODU0MWE2MDA3MWJlOTZmYyIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTIxOSwiZXhwIjoxNjI3NjQ4NDE5LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.WfJMjGfkLDsnpI2lUryr6pSfYnOvHIskzpnCjyFqh-A8cy845f_kF324pLorE-qblPtPtd4fZv_AzjE1QpOJkiKabkaYaUv9ofIWPYo-b0EHmgp8VjIVb4d0cBHhNyBw2wAt3K0D0oS4W-HFB9ZiBADhSehMDM29AeT8UW4B7AP_lMydNSic4QhaJqVvZymB64h7SBsPAk0BR7cgpNzJT_0TnHLmUPmCZTjWuhm4JaEud3o_Gfs2kxXkyNQYl8dFNWyfhBursuwpWCwHt1OcEG6KqTLfvph-vQY78z25wXIoYsq4nKNmNYnQp86Pl0lghGem8pqJ-Cf5nraoI9ctCg
        

        executive_producer_token :
            Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjRiNjE5ZDFjNzUzMDA3MDkwMmExMiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTAzOSwiZXhwIjoxNjI3NjQ4MjM5LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UgbvAYJ2LYHREOpt8GI1MP3jBcA2p1NKBnOEmjK_vR6wWFN1vvZcVYDjdVIHLJdxNEjAitmGYIFfovlLtbKMlzgOZCB3TRQqXTbBDfVQIh3-Z8ZtvCNbPpM01xNRssiPEhqpcPRzAmbaGox8WcO-vSshsMxR8i0cotc0D3DbilUZCK1-uSn_zz0e0hOormAluaJWs-ymQYb1BKnOjeYoi6qB7dfb4Ng-J6c9-M0vN6_0zTlRhGjugXBtcxoB3HHKpiuhByw7oefXGGmoLcrHcXCtxrlsb87RZtNogjb20KTIvewWfRg7xfJ0mI7e_iluG4GrWjmewRn8M3N5Ni9s9w
        
```

## Error Handling

- Errors are returned as JSON objects in the following format:
```
{
    "code": "unauthorized",
    "description": "Permission not found."
}
```

The API will return four error types when requests fail:

- 404: Resource Not Found
- 422: Unprocessable
- 400: Bad Request
- 401: Permission not found
- 405: Method Not Allowed
- 403: Forbidden
- 500: Internal Server Error

## API Endpoints

- API samples can be test with the postman collection provide.

### GET /actors
- General:

  - Returns actors object, success value, and total number of actors

```
{
    "actors": [
        {
            "age": 35,
            "gender": null,
            "id": 1,
            "name": "Jane Doe"
        },
        {
            "age": 32,
            "gender": null,
            "id": 2,
            "name": "Jane Doe"
        }
    ],
    "success": true,
    "total_actors": 2
}
```

### GET /actors/{actor_id}
- General:

  - Returns actors object, title of movies associate with this actor, and success value

```
{
    "details": {
        "age": 35,
        "gender": null,
        "id": 1,
        "name": "Jane Doe"
    },
    "movies": [
        "Very Good Movie 3"
    ],
    "success": true
}
```

### GET /movies
- General:

  - Returns movies object, success value, and total number of movies

```
{
    "movies": [
        {
            "id": 1,
            "rating": 4.5,
            "release_date": "Fri, 29 Jan 2021 00:00:00 GMT",
            "title": "Very Good Movie 3"
        },
    ],
    "success": true,
    "total_movies": 1
}
```

### GET /movies/{movie_id}
- General:

  - Returns movies object, actors associate with this movie, and success value

```
{
    "actors": [
        "Jane Doe"
    ],
    "details": {
        "id": 1,
        "rating": 4.5,
        "release_date": "Fri, 29 Jan 2021 00:00:00 GMT",
        "title": "Very Good Movie 3"
    },
    "success": true
}
```

### POST /actors
- General:

    - Creates a new actor using the data from JSON and returns success value.

```
{
    "success": true
}
``` 

### POST /movies
- General:

    - Creates a new movies using the data from JSON and returns success value.

```
{
    "success": true
}
``` 

### PATCH /actors/{actor_id}
- General:

    - Updates the actor corresponding with actor_id's information using the data from JSON and returns success value.

```
{
    "success": true
}
``` 

### PATCH /movies/{movie_id}
- General:

    - Updates the movie corresponding with movie_id's information using the data from JSON and returns success value.

```
{
    "success": true
}
``` 

### DELETE /actors/{actors_id}
- General:

    - Delete the actor corresponding with actor_id's from database and returns success value.

```
{
    "success": true
}
``` 

### DELETE /movies/{movie_id}
- General:

    - Delete the movie corresponding with movie_id's from database and returns success value.

```
{
    "success": true
}
``` 

## Roles and permissions

- The app use Auth0 to generate jwt tokens which has permissions for each of the three roles. These roles include :

### Casting Assistant

- Can view actors and movies

### Casting Director

- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies

### Executive Producer

- All permissions a Casting Director has and…
- Add or delete a movie from the database
