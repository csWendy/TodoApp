from app import app,db,login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):#The id that Flask-Login passes to the function as an argument is going to be a string,
    return User.query.get(int(id))#so databases that use numeric IDs need to convert the string to integer as above.

# @login_manager.request_loader
# def load_user_from_request(request):
#     # first, try to login using the api_key url arg
#     api_key = request.args.get('api_key')
#     if api_key:
#         user=User.query.filter_by(api_key=api_key).first()
#         if user:
#             return user
#
#     # next, try to login using Basic Auth
#     api_key = request.headers.get('Authorization')
#     if api_key:
#         api_key = api_key.replace('Basic ', '', 1)
#         try:
#             api_key = base64.b64decode(api_key)
#         except TypeError:
#             pass
#         user = User.query.filter_by(api_key=api_key).first()
#         if user:
#             return user
#     # finally, return None if both methods did not login the user
#     return None

class User(UserMixin,db.Model):
    __tablename__ = "user"
    id = db.Column('id',db.Integer,primary_key = True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    todo_item = db.relationship('Todo_item',backref='user',lazy=True)

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username

class Todo_item(db.Model):
    __tablename__ = "todo_items"
    id = db.Column('todo_id',db.Integer, primary_key=True)
    items = db.Column(db.String(100),nullable=False)
    completed = db.Column(db.Boolean,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return '<Todos %r>' % self.items

    # def __init__(self,items):
    #     self.items = items

    # def add_item(self):
    #   db.session.add(self)
    #   db.session.commit()
    #   print("item added:", self.item)
