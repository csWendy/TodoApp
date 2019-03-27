from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,TextAreaField,SubmitField
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
    items = TextAreaField('Todo Items',validators=[Length(min=0,max=140)])
    submit = SubmitField('Add')

class DeleteItemForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    items = TextAreaField('Todo Items',validators=[Length(min=0,max=140)])
    submit = SubmitField('Delete')
    
class CompletedItemForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    items = TextAreaField('Todo Items',validators=[Length(min=0,max=140)])
    submit = SubmitField('Completed')
