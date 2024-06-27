from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/inc_exp')
def incomes_expenses():
    return render_template('inc_exp.html')

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')
