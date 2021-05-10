from app import app
from flask import render_template
from app.forms import LoginForm
@app.route('/')
@app.route('/index')

def index():
	return render_template('index.html')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html',title='Profile Page', form=form)

