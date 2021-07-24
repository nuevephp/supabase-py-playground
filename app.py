import os
from flask import (
    Flask, render_template, request, redirect, session, url_for, flash
)
from supabase_py import create_client, Client
from forms import AuthForm

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"dedjefijefuhhu]/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AuthForm()
    if form.validate_on_submit():
        error = None
        email = form.email.data
        password = form.password.data
        
        app.logger.debug('debugging now...')
        user = supabase.auth.sign_in(email=email, password=password)
        app.logger.debug(user)
        if (user['status_code'] == 400):
            error = user['error_description']
        else:
            return redirect(url_for('home'))
        
        flash(error)
    
    return render_template("auth/login.html", form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def register():
    form = AuthForm()
    if form.validate_on_submit():
        error = None
        email = form.email.data
        password = form.password.data
        
        user = supabase.auth.sign_up(email=email, password=password)
        if (user['status_code'] == 400):
            error = user['error_description']
        else:
            return redirect(url_for('home'))
        
        flash(error)
    
    return render_template("auth/sign_up.html", form=form)
