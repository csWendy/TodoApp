from app import app
import os

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, threaded=True,debug=True)

# from flask import Flask, request, render_template, redirect, url_for, make_response
# from flask_sqlalchemy import SQLAlchemy
# import os
# import requests, json
#
# app = Flask(__name__)
#
# # setting up db config
# #'mysql://{master username}:{db password}@{endpoint}/{db instance name}'
# # app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://{}:{}@{}:3306/{}'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://todoapp:todoapp123@todoapp.cgya4a2lrtxt.us-east-1.rds.amazonaws.com:3306/todoapp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column('id',db.Integer,primary_key = True)
#     username = db.Column(db.String(50),unique=True,nullable=False)
#     todo_item = db.relationship('Todo_item',backref='user',order_by="Todo_item.id",lazy=True)
#
#     def save_user(self):
#         db.session.add(self)
#         db.session.commit()
#         print("User added:", self.username)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
#     def __init__(self,username):
#         self.username = username
#
# class Todo_item(db.Model):
#     __tablename__ = "todo_items"
#     id = db.Column(db.Integer, primary_key=True)
#     items = db.Column(db.String(100), nullable=False)
#     completed = db.Column(db.Boolean, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#
#     def __repr__(self):
#         return '<Todos %r>' % self.items
#
#     def __init__(self,items):
#         self.items = items
#
#     def add_item(self):
#       db.session.add(self)
#       db.session.commit()
#       print("item added:", self.item)
#
# @app.before_first_request
# def create_tables():
#   db.create_all()

#
# @app.route('/user')
# def user():
#     r = requests.get('https://hunter-todo-api.herokuapp.com/user')
#     return r.text
#
# @app.route('/create_user', methods=['post'])
# def create_user():
#     username = request.form['username']
#     r = requests.get('https://hunter-todo-api.herokuapp.com/user')
#     exist_users = json.loads(r.text)
#     for u in exist_users:
#         if u['username'] == username:
#             return 'user exists'
#     r = requests.post('https://hunter-todo-api.herokuapp.com/user', data=json.dumps({'username': username}))
#     return render_template('login.html')
#
# @app.route('/login_user', methods=['post'])
# def login_user():
#     username = request.form['username']
#     r = requests.post('https://hunter-todo-api.herokuapp.com/auth', data=json.dumps({'username': username}))
#     jar = r.cookies
#
#     #store info in a cookie
#     response = make_response(redirect("/todo-item"))
#     response.set_cookie('sillyauth', jar['sillyauth'])
#     response.set_cookie('username', username)
#
#     return response
#
#
# @app.route('/todo-item',methods = ['GET','POST'])
# def todo_item():
#     #retrieved info from cookies
#     val = request.cookies.get('sillyauth')
#     jary = requests.cookies.RequestsCookieJar()
#     jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")
#
#     r = requests.get('https://hunter-todo-api.herokuapp.com/todo-item', cookies=jary)
#     return render_template('todo-item.html', todo_item = r.json())
#
# @app.route('/new-item')
# def new_item():
#     return render_template('new-item.html')
#
# @app.route('/create-item', methods=['post'])
# def create_item():
#     #retrieved info from cookies
#     val = request.cookies.get('sillyauth')
#     jary1 = requests.cookies.RequestsCookieJar()
#     jary1.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")
#
#     content = request.form['content']
#     r = requests.post('https://hunter-todo-api.herokuapp.com/todo-item', data=json.dumps({'content': content}), cookies=jary1)
#     return redirect('/todo-item')
#
# @app.route('/completed-item/<id>')
# def completed_item(id):
#     #retrieved info from cookies
#     val = request.cookies.get('sillyauth')
#     jary = requests.cookies.RequestsCookieJar()
#     jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")
#
#     r = requests.put('https://hunter-todo-api.herokuapp.com/todo-item/' + id,data=json.dumps({'completed':True}),cookies=jary)
#     return redirect('/todo-item')
#
# @app.route('/delete-item/<id>')
# def delete_item(id):
#     #retrieved info from cookies
#     val = request.cookies.get('sillyauth')
#     jary = requests.cookies.RequestsCookieJar()
#     jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")
#
#     r = requests.delete('https://hunter-todo-api.herokuapp.com/todo-item/' + id,data=json.dumps({'delete':True}),cookies=jary)
#     return redirect('/todo-item')
