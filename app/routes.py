from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/hello')
def index():
    user = {'username': 'ttimms'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
 # get is used to request information from the server
 # post is used to send information to the server
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # returns true if post
        flash('Login requested for user {}, remember_me={}'.format( # shows up above next thing that is displayed
            form.username.data, form.remember_me.data)) # flash provides temporary values for form elements
        #redirects if form submission    
        return redirect(url_for('index')) # redirect returns to another page

    # redirects if get request
    return render_template('login.html', title='Sign In', form=form) # often have variables with names matching parameters in python
