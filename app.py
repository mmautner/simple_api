#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

from resources import TodoListResource, TodoResource

app = Flask(__name__)
api = Api(app)


api.add_resource(TodoListResource, "/todos", endpoint="todos")
api.add_resource(TodoResource, "/todos/<string:id>", endpoint="todo")

if __name__ == "__main__":
    app.run(debug=True)
