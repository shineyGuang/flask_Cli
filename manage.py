# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 15:31
# @Author  : 20019236
# @File    : manage.py
# @Software: flaskReview

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models.base.base import db
from server import create_app
from server.config.base_url import host, port

app = create_app("dev")
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    print(f"""
                ------Zcg_Server启动成功-----
                * Running on http://{host}:{port}/
                """)
    manager.run()
