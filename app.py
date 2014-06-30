#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__)
api = Api(app)

from resources import TodoListResource
from resources import TodoResource

api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

if __name__ == '__main__':
    app.run(debug=True)
