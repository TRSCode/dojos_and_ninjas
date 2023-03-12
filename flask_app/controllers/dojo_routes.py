from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model


@app.route('/')
def home():
    return redirect('/dojos')
    
@app.route('/dojos')
def dojos():
    dojos = dojo_model.Dojo.get_all()
    return render_template("dojo.html", all_dojos = dojos) # could user dojo.get_all() instead of all_dojos = dojos

@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():
    dojo_model.Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def dojo_show(id):
    data = {
        "id": id
    }
    return render_template("dojo_show.html", dojo=dojo_model.Dojo.get_one_and_ninjas(data))