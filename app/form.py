from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo,Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Please register.')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class AddItemForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    items = StringField('Todo Items',validators=[DataRequired()])
    submit = SubmitField('Add')

class DeleteTodoForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    todo_item = StringField('Todo Items',validators=[DataRequired()])
    submit = SubmitField('Delete')
