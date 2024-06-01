from flask import Flask, request, render_template, redirect, url_for, session, g
import requests
import sqlite3
import os
import logging

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

DATABASE_DIR = '/app/data'
DATABASE = os.path.join(DATABASE_DIR, 'wanikani.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            api_key TEXT NOT NULL
        )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        api_key = request.form['api_key']
        session['api_key'] = api_key

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (api_key) VALUES (?)", (api_key,))
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    api_key = session.get('api_key')
    if not api_key:
        return redirect(url_for('login'))
    
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get('https://api.wanikani.com/v2/user', headers=headers)
    data = response.json()

    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    os.makedirs(DATABASE_DIR, exist_ok=True)  # Ensure the directory exists
    if not os.path.exists(DATABASE):
        open(DATABASE, 'w').close()
        os.chmod(DATABASE, 0o666)  # Ensure the file is writable
    with app.app_context():
        init_db()
    app.run(host='0.0.0.0')
