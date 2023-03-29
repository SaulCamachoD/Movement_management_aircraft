from flask import render_template,redirect,session,request, flash
from app import app
from app.controllers import users
from app.models import svc,user

@app.route('/hangar/new_svc')
def new_svc():
    if "user_id" not in session:
        return redirect("/")
    return render_template('new_svc.html')

@app.route('/hangar/new_svc/input', methods=['GET','POST'])
def in_svc():
    if request.method == "POST":
        data ={ 
            "matricule": request.form['matricule'],
            "model": request.form['model'],
            "engine": request.form['engine'],
            "init_date": request.form['init_date'],
            "end_date": request.form['end_date'],
            "tat": request.form['tat'],
            "movement_time": request.form['movement_time'],
            "description": request.form['description'],
            "location": request.form['location'],
            "user_id": request.form['user_id']
        }
        svc.Svc.save(data)
        return redirect('/hangar')
    
    if "user_id" not in session:
        return redirect('/')


@app.route('/hangar/all_info')
def new_info():
    if 'user_id' not in session:
        return redirect('/')
    svc_info = svc.Svc.get_all()
    return render_template('all_info.html',svc_info = svc_info)

@app.route('/hangar/lasa')
def lasa():
    if 'user_id' not in session:
        return redirect('/')
    svc_info = svc.Svc.get_all()
    return render_template('svc_en_mantenimiento.html',svc_info = svc_info)


@app.route('/hangar/delete_svc/<int:id>')
def delete_svc(id):
    svc.Svc.destroy({'id': id})
    return redirect('/hangar/all_info')
