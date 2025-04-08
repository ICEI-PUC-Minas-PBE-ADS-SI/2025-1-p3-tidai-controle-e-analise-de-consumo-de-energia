from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import psycopg2

app = Flask(__name__)
db = SQLAlchemy()
## login_manager = LoginManager()
app.config['SECRET_KEY'] = 'a5881f26bae925d752a97795'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PML1RRjpQ8foE5y1@proudly-unbiased-spadefish.data-1.use1.tembo.io:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db.init_app(app)
bcrypt = Bcrypt(app)
## login_manager.init_app(app)

from greenvolt import routes