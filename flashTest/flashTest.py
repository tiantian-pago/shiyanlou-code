from flask import Flask, flash, redirect, render_template, \
                request, url_for

app = Flask(__name__)
app.secret_key = b'K\x06\x8d(\xfcm\x1dQ\x1b\xf1\xa3_\xccd,\x14'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or\
            request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)