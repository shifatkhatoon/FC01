# -*- coding: utf-8 -*-
from Find_Blog_data import app, db
from Find_Blog_data.crons import cron
from flask_script import Manager, Command, Option, Server
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(use_debugger=app.config['DEBUG'], use_reloader=app.config['RELOAD'], host=app.config['HOST'], port=int(app.config['PORT'])))
manager.add_command('cron', cron)

if __name__ == "__main__":
    manager.run()
