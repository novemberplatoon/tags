import os
from os.path import join
from flask import Flask
from config import load_config
from peewee import SqliteDatabase

FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'

app = Flask(__name__)

app.config['config'] = load_config(join(app.root_path, '../shared/config.yml'))

dbname = load_config('config/database.yml')[FLASK_ENV]['database']
db = SqliteDatabase(dbname)
