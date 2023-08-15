import os

from flask import Flask
import logging
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy

from config import AppConfig

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfig)
app.secret_key = os.getenv("SECRET_KEY")
db.init_app(app)

from views import *
from models import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=4200,
            debug=app.config.get("DEBUG"))
