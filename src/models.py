from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50),unique=True)
    name = db.Column(db.String(50), nullable=False)
    last = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(5000), nullable=True)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(15), nullable=False)
    admin = db.Column(db.Boolean) 
    todos = db.relationship('Todo', backref='user', lazy=True)
    def serialize(self):
        return {
            "name": self.name,
            "last": self.last,
            "password": self.password,
            "email": self.email,
            "phone": self.phone,
            "admin": self.admin,
            "todos": list(map(lambda x: x.serialize(), self.todos)),
            "id": self.id,
            "public_id":self.public_id,
        }


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    createdDate = db.Column(db.String(12))
    dueDate = db.Column(db.String(12))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def serialize(self):
        return {
            "text": self.text,
            "complete": self.complete,
            "createdDate" : self.createdDate,
            "dueDate" : self.dueDate,
            "user_id": self.user_id,
            "id": self.id,
        }



# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }