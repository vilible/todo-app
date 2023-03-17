from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "todo.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    db.init_app(app)

    from .models import Tasks
    with app.app_context():
        db.create_all()

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
