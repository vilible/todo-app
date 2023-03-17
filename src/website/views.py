from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def index():
    pass

@views.route("/add", methods=["POST"])
def add():
    pass

@views.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    pass

@views.route("/delete/<int:id>")
def delete(id: int):
    pass