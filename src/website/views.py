from flask import Blueprint, render_template
from .models import Tasks

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html", tasks=Tasks.query.all())

@views.route("/add", methods=["POST"])
def add():
    pass

@views.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    pass

@views.route("/delete/<int:id>")
def delete(id: int):
    pass