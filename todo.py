#a shell context that adds the database instance and models to the shell session
# export FLASK_APP=todo.py in terminal
from app import app, db
from app.models import User, Todo_item

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Todo_item': Todo_item}
