import json

from db import db
from flask import Flask
from db import User
from db import Task

from flask import Flask
from flask import request

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({'error': message},). code

@app.route('/api/users/', methods=['GET'])
def get_users():
    return success_response(
        {'users': [u.serialize() for u in User.query.all()]}
    )

@app.route('/api/task/', methods=['POST'])
def make_task():
    body= json.loads(request.data)
    new_task= Task(name=body.get('name'), description= body.get('description', priority = body.get('priority')))
    db.session.add(new_task)
    db.session.commit()
    return success_response(new_task.serialize(), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
