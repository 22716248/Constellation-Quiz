from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, DataRequired, EqualTo
from app.models import User, Score

# Used for existing users into their account
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Used to register an existing user
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

# Used to submit a Quiz Attempt, by a user.
class QuizForm(FlaskForm):
    question1 = StringField("Question 1: For the above image, identify the constellation.", validators=[DataRequired()])
    question2 = StringField("Question 2: For the above image, identify the constellation.", validators=[DataRequired()])
    question3 = StringField("Question 3: For the above image, identify the constellation.", validators=[DataRequired()])
    question4 = StringField("Question 4: For the above image, identify the constellation.", validators=[DataRequired()])
    question5 = StringField("Question 5: For the above image, identify the constellation.", validators=[DataRequired()])
    question6 = StringField("Question 6: Within what constellation did the brightest stellar event in recorded history occur?", validators=[DataRequired()])
    question7 = StringField("Question 7: Which constellation is also known as the poop deck?", validators=[DataRequired()])
    question8 = StringField("Question 8: Which constellation is also known as the sails?", validators=[DataRequired()])
    question9 = StringField("Question 9: Which constellation contains the star system Alpha Centauri?", validators=[DataRequired()])
    question10 = StringField("Question 10: Which constellation depicts a superhuman giant hunter?", validators=[DataRequired()])
    submit = SubmitField('Submit Answers.')

# This form is used for users to reset their password
class ResetForm(FlaskForm):
    password_o = PasswordField('Old Password',validators=[DataRequired()])
    password_n = PasswordField('New Password',validators=[DataRequired()])
    password_n2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password_n')])
    submit = SubmitField('Change Password')

