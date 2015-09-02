# -*- coding: utf-8 -*-
from collections import OrderedDict

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wkih.sqlite"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)

    contact_id = db.Column(
        db.Integer, db.ForeignKey('contact.id'), nullable=False)
    contact = db.relationship(
        'Contact',
        backref=db.backref('projects', lazy='dynamic')
    )


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Text)


db.create_all()


@app.route('/')
def home_view():
    return render_template("base.html")


@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")


@app.route("/project", methods=["GET", "POST"])
def project_view():
    if request.method == "POST":
        contact = Contact(
            email=request.form["email"],
            phone_number=request.form["phone_number"],
        )
        db.session.add(Project(
            name=request.form["name"],
            description=request.form["description"],
            contact=contact,
        ))
        db.session.commit()

    # maps the forms' name to its label
    form_fields = OrderedDict(
        (
            ("name", "Name"),
            ("email", "Email"),
            ("phone_number", "Telefon"),
            ("description", "Beschreibung"),
        )
    )
    projects = Project.query.all()
    return render_template(
        "project.html",
        projects=projects,
        form_fields=form_fields
    )
