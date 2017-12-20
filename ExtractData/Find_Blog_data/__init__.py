# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from pytz import timezone

app = Flask(__name__)
app.config.from_pyfile('../config.cfg')
db = SQLAlchemy(app)
ma = Marshmallow(app)
tdg_tz = timezone(app.config.get('SERVER_TIMEZONE', 'Etc/UTC'))
from Find_Blog_data.models import BlogTable 
db.create_all()
