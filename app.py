#!/usr/bin/env python

from resources import TodoResource
from resources import TodoListResource
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

if __name__ == '__main__':
    app.run(debug=True)
