from flask import Flask
from flask_sqlalchemy import SQLAlchemy


nome_css_file = 'bootstrap.css'
nome_css_file_app = 'app.css'

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views_games import *
from views_user import *

if __name__ == '__main__':
    app.run(debug = True)
    
