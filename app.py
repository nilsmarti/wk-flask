from flask import Flask, request, render_template, redirect, url_for, session
import requests
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.eniron.get('SECRET_KEY')

DATABASE = 'wanikani.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

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
    app.run(host='0.0.0.0')

