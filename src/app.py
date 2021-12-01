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
    return json.dumps({'error': message}), code

@app.route('/api/users/', methods=['GET'])
def get_users():
    return success_response(
        {'users': [u.serialize() for u in User.query.all()]}
    )

@app.route('/api/user/<int:user_id>/', methods=['GET'])
def get_users(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return failure_response("user does not exist", 400)

    return success_response(user.serialize(), 200)

@app.route('/api/task/', methods=['POST'])
def make_task():
    body= json.loads(request.data)
    new_task= Task(name=body.get('name'), description= body.get('description', priority = body.get('priority')))
    db.session.add(new_task)
    db.session.commit()
    return success_response(new_task.serialize(), 201)

@app.route('/api/<int:user_id>/tasks/', methods=['POST'])
def create_task(user_id):
    body= json.loads(request.data)
    user = User.query.filter_by(id=user_id).first()
    #new_task= Task(name=body.get('name'), description= body.get('description', priority = body.get('priority')))
    if not body.get("name") or not body.get("description") or not body.get("priority"):
        return failure_response("arguments not specified", 400)
    if not user:
        return failure_response("user not found", 404)

    new_task = Task(name=body.get("name"), description=body.get("description"), priority = body.get("priority"), username_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return success_response(new_task.serialize(), 201)

@app.route("/api/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    if body is None or body.get("username") is None:
        return failure_response("arguments not specified", 400)
    new_user = User(username=body.get("username"))
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/api/<user_id>/tasks/", methods=["GET"])
def get_users_tasks(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("user not found")

    return success_response(user.serialize())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
