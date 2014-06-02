#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models import Todo

app = Flask(__name__)
api = Api(app)

from sqlalchemy import create_engine
from settings import DB_URI

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI))
session = scoped_session(Session)

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class TodoResource(Resource):
    def get(self, todo_id):
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        return todo

    def delete(self, todo_id):
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        session.delete(todo)
        session.commit()
        return '', 204

    def put(self, todo_id):
        parsed_args = parser.parse_args()
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        todo.task = parsed_args['task']
        session.add(todo)
        session.commit()
        return todo, 201


class TodoListResource(Resource):
    def get(self):
        todos = session.query(Todo).all()
        return [todo.serialize for todo in todos]

    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(task=parsed_args['task'])
        session.add(todo)
        session.commit()
        return todo.serialize, 201

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
