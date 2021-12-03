import json
import os

from db import db
from flask import Flask
from db import Category
from db import Task

from flask import Flask
from flask import request

app = Flask(__name__)
db_filename = "tasks.db"

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

@app.route("/", methods=["GET"])
def default():
    return success_response("default")

@app.route('/api/categories/', methods=['GET'])
def get_categories():
    return success_response({"categories": [c.serialize() for c in Category.query.all()]})

@app.route('/api/category/<int:category_id>/', methods=['GET'])
def get_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if not category:
        return failure_response("category does not exist", 400)

    return success_response(category.serialize(), 200)


@app.route('/api/<int:category_id>/tasks/', methods=['POST'])
def create_task(category_id):
    body= json.loads(request.data)
    category = Category.query.filter_by(id=category_id).first()
    #new_task= Task(name=body.get('name'), description= body.get('description', priority = body.get('priority')))
    if not body.get("name") or not body.get("description") or not body.get("priority"):
        return failure_response("arguments not specified", 400)
    if not category:
        return failure_response("Category not found", 404)

    new_task = Task(name=body.get("name"), description=body.get("description"), priority = body.get("priority"), category_id=category_id)
    db.session.add(new_task)
    db.session.commit()
    return success_response(new_task.serialize(), 201)

@app.route("/api/category/", methods=["POST"])
def create_category():
    body = json.loads(request.data)
    if body is None or body.get("category") is None:
        return failure_response("arguments not specified", 400)
    new_category = Category(category=body.get("category"))
    db.session.add(new_category)
    db.session.commit()
    return success_response(new_category.serialize(), 201)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
