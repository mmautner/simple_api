Demo RESTful HTTP API using [Flask](https://github.com/pallets/flask), [Flask-Restful](https://github.com/flask-restful/flask-restful) and [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
===================

1. Install requisite packages:
```shell
$ pip install -r requirements.txt
```
2. Create tables:
```shell
$ ./models.py
```
3. Run service:
```
$ python app.py
```
4. Give it a try:
```shell
>> import requests, json
>> requests.get('http://localhost:5000/todos').json()
[]
>> requests.post('http://localhost:5000/todos',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({'task': 'go outside!'})).json()
{u'id': 1, u'task': u'go outside!', u'uri': u'http://localhost:5000/todos/1'}
>> requests.get('http://localhost:5000/todos/1').json()
{u'id': 1, u'task': u'go outside!', u'uri': u'http://localhost:5000/todos/1'}
>> requests.put('http://localhost:5000/todos/1',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({'task': 'go to the gym'})).json()
{u'id': 1, u'task': u'go to the gym', u'uri': u'http://localhost:5000/todos/1'}
>> requests.delete('http://localhost:5000/todos/1')
>> requests.get('http://localhost:5000/todos').json()
[]
```

Don't forget that you must pass a "Content-Type: application/json" header along with your request!
