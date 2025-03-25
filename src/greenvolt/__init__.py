from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5881f26bae925d752a97795'

from greenvolt import routes