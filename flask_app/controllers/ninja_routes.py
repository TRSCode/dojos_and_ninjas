from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo_model, ninja_model


@app.route('/ninjas')
def ninjas():
    # dojos = dojo_model.Dojo.get_all()
    return render_template("add_ninja.html", dojos=dojo_model.Dojo.get_all())

@app.route('/ninja/create_ninja', methods=['POST'])
def create_ninja():
    ninja_model.Ninja.save(request.form)
    return redirect('/')