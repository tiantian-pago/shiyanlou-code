from flask import Flask, request
from flask import flash, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = b'\x83\x02\x13\xef9Y\xfa:)\xa0\x879p\x92\xf9\xcc'

@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'shiyanlou' or request.form['password'] != 'shiyanlou':
            flash('username or password invalid')
            return redirect(url_for('index', name='world'))
        else:
            session['username'] = request.form['username']
            name = request.form['username']
            flash('you were logged in')
            return redirect(url_for('index', name=name))
    return render_template('login.html')