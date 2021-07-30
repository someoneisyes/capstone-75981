import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Movies, Actors, Link, db, db_drop_and_create_all

class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

        self.database_name = "capstone_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.casting_assistant_token = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZDA4ZGYyYjcyYTlmMDA2YTI5NmY5MiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTI2NywiZXhwIjoxNjI3NjQ4NDY3LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.M8LWKFSrmOnaiQnrN66QFSQB_diasdbTiDCd-R0ysjEl5M7u1IhZhBwJ3pqGhHswxHMaTkoTtjaBV0bdvKlLYDneCO-b6pjmFD3poyPEMPGTfZczgj3T0OAzkwToKeiC1shFLOow3-fcl0m-9MJcAPtam3KzidIzjef18EhcWVAOZYsLghd3nWsBu90_In_sTdeUh8_4CMJmmPKsrS_UQc35Na1niPye1mer9xGcp9bKDl6AZ54pDKPQRlvosMv2PfE8ZRJ0yAveR4UsP099jBsuGkby7BeYSPqXyvKzrhc4NEAAVTVwx7GNmtKCfjav8OeJukS7Oqx5eIJADqzN9w'
        }

        self.casting_director_token = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMDI1Mzk3ODU0MWE2MDA3MWJlOTZmYyIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTIxOSwiZXhwIjoxNjI3NjQ4NDE5LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.WfJMjGfkLDsnpI2lUryr6pSfYnOvHIskzpnCjyFqh-A8cy845f_kF324pLorE-qblPtPtd4fZv_AzjE1QpOJkiKabkaYaUv9ofIWPYo-b0EHmgp8VjIVb4d0cBHhNyBw2wAt3K0D0oS4W-HFB9ZiBADhSehMDM29AeT8UW4B7AP_lMydNSic4QhaJqVvZymB64h7SBsPAk0BR7cgpNzJT_0TnHLmUPmCZTjWuhm4JaEud3o_Gfs2kxXkyNQYl8dFNWyfhBursuwpWCwHt1OcEG6KqTLfvph-vQY78z25wXIoYsq4nKNmNYnQp86Pl0lghGem8pqJ-Cf5nraoI9ctCg'
        }

        self.executive_producer_token = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjRiNjE5ZDFjNzUzMDA3MDkwMmExMiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzY0MTAzOSwiZXhwIjoxNjI3NjQ4MjM5LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.UgbvAYJ2LYHREOpt8GI1MP3jBcA2p1NKBnOEmjK_vR6wWFN1vvZcVYDjdVIHLJdxNEjAitmGYIFfovlLtbKMlzgOZCB3TRQqXTbBDfVQIh3-Z8ZtvCNbPpM01xNRssiPEhqpcPRzAmbaGox8WcO-vSshsMxR8i0cotc0D3DbilUZCK1-uSn_zz0e0hOormAluaJWs-ymQYb1BKnOjeYoi6qB7dfb4Ng-J6c9-M0vN6_0zTlRhGjugXBtcxoB3HHKpiuhByw7oefXGGmoLcrHcXCtxrlsb87RZtNogjb20KTIvewWfRg7xfJ0mI7e_iluG4GrWjmewRn8M3N5Ni9s9w'
        }

        self.test_movie = {
            'title': 'Very Good Movie 2',
            'release_date': '2021-01-29',
            'actor':2
        }

        self.update_movie = {
            'title': 'Excellent Movie',
            'rating':'5.0'
        }

        self.test_actor = {
            'name': 'John Doe',
            'age': '38',
            'gender': 'male',
            'movie': 3
        }

        self.update_actor = {
            'age': '40',
            'gender': 'non-binary'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()

        actor1 = Actors(
            name="Jane Doe",
            age="32",
            gender="female"
        )
        actor2 = Actors(
            name="Jane Doe",
            age="32",
            gender="female"
        )
        actor3 = Actors(
            name="Jane Doe",
            age="32",
            gender="female"
        )
        movie1 = Movies(
            title="Very Good Movie",
            release_date="2021-02-02",
            rating=5.0,
        )
        movie2 = Movies(
            title="Very Good Movie",
            release_date="2021-02-02",
            rating=5.0,
        )
        movie3 = Movies(
            title="Very Good Movie",
            release_date="2021-02-02",
            rating=5.0,
        )
        db.session.add_all([actor1, actor2, actor3, movie1, movie2, movie3])
        db.session.commit()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # actors and movies POST endpoint tests

    def test_post_actors_success(self):
        res = self.client().post('/actors', headers=self.casting_director_token, json=self.test_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_actors_fail(self):
        res = self.client().post('/actors', headers=self.casting_assistant_token, json=self.test_actor)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_post_movies_success(self):
        res = self.client().post('/movies', headers=self.executive_producer_token, json=self.test_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movies_fail(self):
        res = self.client().post('/movies', headers=self.casting_assistant_token, json=self.test_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    #   movies and actors GET endpoint tests

    def test_get_movies_success(self):
        res = self.client().get('/movies', headers=self.casting_assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_fail(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
    
    def test_get_movies_by_id_success(self):
        res = self.client().get('/movies/2', headers=self.casting_assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        print()

    def test_get_movies_by_id_fail(self):
        res = self.client().get('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        print()

    def test_get_actors_success(self):
        res = self.client().get('/actors', headers=self.casting_assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        print()

    def test_get_actors_fail(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_get_actors_by_id_success(self):
        res = self.client().get('/actors/2', headers=self.casting_assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        print()

    def test_get_actors_by_id_fail(self):
        res = self.client().get('/actors/100', headers=self.casting_assistant_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        print()


    #   actors and movies PATCH endpoint tests

    def test_patch_actors_success(self):
        res = self.client().patch('/actors/2', headers=self.executive_producer_token, json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_patch_actors_fail(self):
        res = self.client().patch('/actors/2', headers=self.casting_assistant_token, json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_patch_movies_success(self):
        res = self.client().patch('/movies/2', headers=self.executive_producer_token, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_fail(self):
        res = self.client().patch('/movies/2', headers=self.casting_assistant_token, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    #   actors and movies DELETE endpoint tests

    def test_delete_actors_success(self):
        res = self.client().delete('/actors/1', headers=self.casting_director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_fail(self):
        res = self.client().delete('/actors/999', headers=self.casting_director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movies_success(self):
        res = self.client().delete('/movies/1', headers=self.executive_producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movies_fail(self):
        res = self.client().delete('/movies/999', headers=self.executive_producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

if __name__ == '__main__':
    unittest.main()