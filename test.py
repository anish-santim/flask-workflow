import unittest
from flask import Flask
from flask_testing import TestCase
from decouple import config


from app import app  # Assuming your Flask app code is in a separate file named 'app.py'

class TodoAppTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app
    
    def test_port(self):
        self.assertEqual(int(config('PORT')), 8000)

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertTemplateUsed('index.html')

if __name__ == '__main__':
    unittest.main()