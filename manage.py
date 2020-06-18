from app import create_app
import os
from flask_script import Manager
from app import db

app = create_app(os.environ['CONFIG_TYPE'])
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def db_init():
    db.create_all()


if __name__ == '__main__':
    manager.run()
