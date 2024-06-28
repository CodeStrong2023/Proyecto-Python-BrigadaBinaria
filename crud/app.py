from flask import Flask, render_template

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
        cur = conn.cursor(cursor_factory=RealDictCursor)
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
