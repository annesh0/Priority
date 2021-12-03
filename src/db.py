from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)
    tasks = db.relationship("Task", order_by="Task.priority", cascade="delete")

    def __init__(self, **kwargs):
        self.category = kwargs.get('category')

    def serialize(self):

        return {
            'id': self.id,
            'category': self.category,
            'tasks': [t.serialize() for t in self.tasks]
        }

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    priority = db.Column(db.Boolean, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.priority = kwargs.get('priority')
        self.category_id= kwargs.get('category_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'priority': self.priority,
            'category_id': self.category_id
        }
