# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


def project_api():
    return [
        {
            "id": 1,
            "name": "Fahrräder für Flüchtlinge",
            "necessities": [
                {
                    "name": "Fahrräder",
                    "description": "Wir brauchen gebrauchte Fahrräder.",
                    "quantity_required": 10,
                    "quantity_pledged": 3,
                    "unit": "items",
                    "id": 1,
                },
                {
                    "name": "Werkstatt",
                    "description": "Wir brauchen Zugriff auf eine Werkstatt.",
                    "quantity_required": 7,
                    "quantity_pledged": 3,
                    "unit": "hours",
                    "id": 2,
                }
            ]
        }
    ]


@app.route('/')
def home_view():
    return render_template("base.html")


@app.route("/project")
def project_view():
    projects = project_api()
    return render_template("project.html", projects=projects)
