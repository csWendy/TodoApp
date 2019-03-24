from flask import render_template,flash,redirect,url_for,request
from werkzeug.urls import url_parse
from app import app,db
from flask_login import UserMixin,current_user,login_user,logout_user,login_required
from app.form import LoginForm,RegistrationForm,AddItemForm
from app.models import User, Todo_item

#The function here is executed right before the view function.
@app.before_first_request
def create_tables():
  db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid username.Please register first.')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('home')
        # flash('Login requested for user {}'.format(form.username.data))
        return redirect(next_page)
    return render_template('login.html',title='Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    todos= Todo_item.query.filter_by(user_id=user.id).all()
    return render_template('user.html',user=user,todos=todos)

@app.route('/add-items',methods=['GET', 'POST'])
@login_required
def add_items():
    form = AddItemForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        todo=Todo_item(items=form.items.data)
        db.session.add(todo)
        db.session.commit()
        flash('Your Todo Items have been saved.')
        return redirect(url_for('add-items'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.todo_item = current_user.todo_items
    return render_template('add-items.html', title='Add items',form=form)

#     if request.method == 'POST':
#             todo = Todo_item(request.form['items'])
#             db.session.add(todo)
#             db.session.commit()
#             flash('Todo item was successfully created')
#             return redirect(url_for('todo-items/<username>'))
#     return render_template('new-item.html')
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
#
#     #retrieved info from cookies
#     val = request.cookies.get('sillyauth')
#     jary = requests.cookies.RequestsCookieJar()
#     jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")
#
#     r = requests.delete('https://hunter-todo-api.herokuapp.com/todo-item/' + id,data=json.dumps({'delete':True}),cookies=jary)
#     return redirect('/todo-item')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
