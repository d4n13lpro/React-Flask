# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/api/users')
def get_users():
    return {
        'users': [
            {
                'id': 1,
                'name': 'Alice',
                'last_name': 'Perez'
            },
            {
                'id': 2,
                'name': 'Bob',
                'last_name': 'Patiño'
            },
            {
                'id': 3,
                'name': 'Carlos',
                'last_name': 'Acuña'
            }
        ]
    }

@app.route('/api/fruits')
def get_fruits():
    return {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }

if __name__ == '__main__':
    app.run(debug=True)
