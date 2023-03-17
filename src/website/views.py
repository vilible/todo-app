from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from .models import Tasks
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html", tasks=Tasks.query.all())

@views.route("/add", methods=["POST"])
def add():
    description = request.form.get("task")

    if description != "":
        is_done = False
        date = datetime.now().strftime("%d.%m.%Y %H:%M")

        db.session.add(Tasks(description=description, is_done=is_done, date=date))
        db.session.commit()

    return redirect(url_for("views.index"))

@views.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    task = Tasks.query.filter_by(id=id).first()

    if task == None:
        return redirect(url_for("views.index"))

    if request.method == "POST":
        task.description = request.form.get("task")
        task.is_done = True if request.form.get("is_done") == "on" else False
        db.session.commit()

        return redirect(url_for("views.index"))
    else:
        return render_template("edit.html", id=id, description=task.description, is_done=task.is_done)

@views.route("/delete/<int:id>", methods=["GET"])
def delete(id: int):
    db.session.delete(Tasks.query.filter_by(id=id).first())
    db.session.commit()

    return redirect(url_for("views.index"))