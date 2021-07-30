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
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZDA4ZGYyYjcyYTlmMDA2YTI5NmY5MiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzYzMTYxOSwiZXhwIjoxNjI3NjM4ODE5LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.lv15SHBy7oxBhQ3kbRjCnmYVCm_ZGSGoUOL0YP5tXMHfuvL0u9yvqMPN7x1YkavIBInB9__fd9oasx4tRZWPooljLjT0qpcOyi4PEf2gyaCB_aHQKza_0uZEK3RtLdruiZVBfF6XYfVj9IyW1lGvf4k9Zzftr2QUaiKyxBYbxYEYWhDL6pex5nhCq1IilqX9GCJ3uhp1qDn3a-MoLgwKAhiVxlMSI4_cbBISGBsM5AE58d-MT7dtOwYZV22O18WgvG0ZNGOfYNoqM6hl9wWlNSLT0EZze4ib9RW2dQyqStN5lJKpMh95pB0qxXVBzBEdWfWr0rR-PjFd3WS0bTe2Ng'
        }

        self.casting_director_token = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMDI1Mzk3ODU0MWE2MDA3MWJlOTZmYyIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzYzMTQ0OCwiZXhwIjoxNjI3NjM4NjQ4LCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.nCiMxliiMxM_Oj1bpGeNgEytSfAdaLzE22g_Wnz405wTwwbS56q5fNOAQqWXiiQBXpvjzECA5tI5Q0pEGViBK4IUxYbcY217E_9QbJcaFqX_f-wAtfYHv58TacWPB0ng1wht3sI1QAep7msf0xHZQ3-1S9qsiXzlG5FWpyIFz_7G4IqM5moIUbgwEYrwC_MaeibNa6WBwJXALAiYM9mKAH8ctBxNmQ4k5OME-eDwIMkkB0ki_H8Gm2XXWsRffIi1VVA6Wafl0bPLa59UId0O8KLdnOeOEAknf65uO7P9RTj8p_GesQYzMmh3AUb8M1ck8T-CkjKcm8QggE59JeOclA'
        }

        self.executive_producer_token = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ5SjJLZTA5dVMyaWZWZjZYUGNzaiJ9.eyJpc3MiOiJodHRwczovL25hcmF0LWF1dGguZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwYjRiNjE5ZDFjNzUzMDA3MDkwMmExMiIsImF1ZCI6ImNhcHN0b25lLWFwaSIsImlhdCI6MTYyNzYzMTE5MCwiZXhwIjoxNjI3NjM4MzkwLCJhenAiOiJTSFJUb01DWGhYZGF6eXN6anpWMUtMVVlkaGFxOEUxNyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.CD_f6zt4iyif3Hb9h6k73xzLbJ4OUHgJBt82WkeqwyH_FaloBhGJH4xGjnAoQCgsAWoPVyxZwbAc9TjfGB7nmpySvTwJX5U47sYQMOIHBOAWkPzK99yt2Nm785a6NiVZoAd8Biuop1bgz8Y5-zCTAhnvNkWgOZoVrY5BQnFagkjom5kXX6jAMmyKet-J2Jv-CGTAKttG5f6FRJkGvJor0gwiQJeWI80wzmoxwIQv88QMi2NZIAo2Du1I4VH14ULbuvYJvh9uFFqrY3LVnAmLXPu7Pnz7qwMKjGDeNV9bMAp6TlQHTsXsYiZqKncmspasZRWIUfqDEc08nzFPDovFrA'
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