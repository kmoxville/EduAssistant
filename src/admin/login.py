from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Simple hardcoded check for demonstration purposes
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            flash('Login successful', 'success')
            return redirect(url_for("index"))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return decorated_function
