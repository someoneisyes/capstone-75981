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
            'authorization': "{}".format(os.environ.get('ASSISTANT'))
            }

        self.casting_director_token = {
            'authorization': "{}".format(os.environ.get('DIRECTOR'))
            }

        self.executive_producer_token = {
            'authorization': "{}".format(os.environ.get('PRODUCER'))
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