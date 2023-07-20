from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy 
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "tutoring.db")
db.init_app(app)

import app.models as models


@app.route('/')
def home():
    return render_template('home.html', page_title='The Website')


@app.route('/level/<int:level>')
def show_level(level):
    if level < 1 or level > 3:
        abort(404)
    results = models.Subject.query.filter_by(level=level).first()
    print(results.name)
    return render_template('levels.html', page_title='LEVEL')
  

#@app.route('/subjects/<int:id>')
#def subjects(id): 
    subject = models.Subject.query.filter_by(id=id).first()
    print(subject.name, subject.level)
    return render_template("subjects.html", subject=subject)


@app.route('/all_tutors')
def all_tutors():
    results = models.Tutor.query.all()
    print(results.name)
    return render_template('all_tutors.html', page_title='ALL_TUTORS')

@app.route('/tutor/<int:id>')
def tutors(id):
    tutor = models.Tutor.query.filter_by(id=id).first_or_404()
    print(tutor.name, tutor.description)
    return render_template("all_tutors.html", tutor=tutor)

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='CONTACTS')


if __name__ == "__main__":
    app.run(debug=True)