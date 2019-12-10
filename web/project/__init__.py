#################
#### imports ####
#################

from os.path import join, isfile
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
if isfile(join('instance', 'flask_full.cfg')):
    app.config.from_pyfile('flask_full.cfg')
else:
    app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)


@app.route('/get/<n>')
def index():
    sol = app.query.filter_by(n=n).all()
    return sol





