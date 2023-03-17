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
    is_done = False
    date = datetime.now().strftime("%d.%m.%Y %H:%M")

    db.session.add(Tasks(description=description, is_done=is_done, date=date))
    db.session.commit()

    return redirect(url_for("views.index"))

@views.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    pass

@views.route("/delete/<int:id>")
def delete(id: int):
    pass