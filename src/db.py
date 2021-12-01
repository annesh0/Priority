from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Columns(db.String, nullable=False)
    tasks = db.Column(db.Integer, db.ForeignKey('task.id'))

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'tasks': [s.serialize() for s in self.tasks]
        }

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    priority = db.Column(db.Integer, nullable=False)
    username_id= db.relationship('User', cascade = 'delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.priority = kwargs.get('priority')
        self.username_id= kwargs.get('username_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'priority': self.priority,
            'username_id': self.username_id
        }
