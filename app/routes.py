from app import app

from flask import render_template

from flask_sqlalchemy import SQLAlchemy 

import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir,"Tutoring.db")
db.init_app(app)

import app.models as models

@app.route('/all_pizzas')
def all_pizzas():
    results = models.Pizza.query.all()
    print(results)
    return "done"


@app.route('/')
def home():
    return render_template('home.html', page_title = 'The Website')

@app.route('/level/<int:level>')
def show_level(level):
    results = models.Subject.query.all()
    return render_template('level.html', page_title = 'LEVEL')
    if level<1 or level>3:
        abort(404)



@app.route('/<Subjects>')
def Subjects (id):
    Subjects = models.Subjects.query.filter_by(id=id).first()
    return render_template("Subjects.html", Subjects = Subjects)


@app.route('/contact')
def contact ():
    return render_template('contact.html', page_title = 'CONTACTS')

if __name__ == "__main__":
    app.run(debug=True)

