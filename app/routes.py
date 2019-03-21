from flask import render_template
from app import app,db
from flask_login import UserMixin,current_user,login_user,logout_user,login_required
from app.form import LoginForm,RegistrationForm
from app.models import User, Todo_item

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('todo-items'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect("/login")
        login_user(user)
        flask.flash('Logged in successfully.')
        return redirect("/todo-items")
    return render_template('login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flask.flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/todo-item/<user_id>')
@login_required
def user_todo_item(user_id):
    user = User.query.filter_by(user_id=user_id).first_or_404()
    return render_template('todo_item<user_id>',todos=Todo_item.query.filter_by(user_id).all())

@app.route('/new-item', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
            todo = Todo_item(request.form['items'])
            db.session.add(todo)
            db.session.commit()
            flash('Todo item was successfully created')
            return redirect(url_for('todo-items/<username>'))
    return render_template('new-item.html')

@app.route('/completed-item/<id>')
def completed_item(id):
    #retrieved info from cookies
    val = request.cookies.get('sillyauth')
    jary = requests.cookies.RequestsCookieJar()
    jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")

    r = requests.put('https://hunter-todo-api.herokuapp.com/todo-item/' + id,data=json.dumps({'completed':True}),cookies=jary)
    return redirect('/todo-item')

@app.route('/delete-item/<id>')
def delete_item(id):
    #retrieved info from cookies
    val = request.cookies.get('sillyauth')
    jary = requests.cookies.RequestsCookieJar()
    jary.set('sillyauth', val, domain="hunter-todo-api.herokuapp.com")

    r = requests.delete('https://hunter-todo-api.herokuapp.com/todo-item/' + id,data=json.dumps({'delete':True}),cookies=jary)
    return redirect('/todo-item')
