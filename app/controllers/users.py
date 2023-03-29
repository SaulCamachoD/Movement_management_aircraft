from flask import render_template,redirect,session,request, flash
from app import app
from datetime import datetime
from app.models.user import User
from app.models import svc
from app.controllers import svcs
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/new/register', methods=["POST"])
def new_register():
    if not User.validate_register(request.form):
        return redirect('/register')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/hangar')

@app.route('/login')
def login_in():
    return render_template('login.html')

@app.route('/login/in', methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email/Password","login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect('/login')
    
    session['user_id'] = user.id
    return redirect('/hangar')

@app.route('/hangar')
def hangar():
    if 'user_id' not in session:
        return redirect('/logout')
    hora_actual = datetime.now()
    svc_info = svc.Svc.get_all()
    svc_en_mantenimiento = []
    for svc_data in svc_info:
        if svc.Svc.check_time(svc_data.movement_time):
            svc_en_mantenimiento.append(svc_data)
    return render_template('hangar.html', hora_actual=hora_actual, svc_info= svc_info, svc_en_mantenimiento = svc_en_mantenimiento)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


