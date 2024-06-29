from flask import Flask, render_template, request, flash, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from conexiondb import get_db_connection
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
        user = cur.fetchone()
        cur.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            conn.close()
            return redirect(url_for('incomes_expenses'))
        else:
            conn.close()
            flash('Email o contraseña incorrectos')
        return render_template('login.html')

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE usuarios SET nombre = %s, apellido = %s, email = %s, password = %s WHERE id = %s',
                    (nombre, apellido, email, password, user_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('profile'))
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

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE usuarios SET nombre = %s, apellido = %s, email = %s, password = %s WHERE id = %s',
                    (nombre, apellido, email, password, user_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('profile'))
    return render_template("profile.html", user=user)

@app.route("/inc_exp")
def incomes_expenses():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    # Obtener ingresos
    cur.execute('SELECT * FROM ingresos WHERE usuario_id = %s', (user_id,))
    incomes = cur.fetchall()
    print("Ingresos obtenidos:", incomes)  # Log para verificar ingresos
    
    # Obtener gastos
    cur.execute('SELECT * FROM gastos WHERE usuario_id = %s', (user_id,))
    expenses = cur.fetchall()
    print("Gastos obtenidos:", expenses)  # Log para verificar gastos
    
    cur.close()
    conn.close()
    return render_template("inc_exp.html", incomes=incomes, expenses=expenses)



