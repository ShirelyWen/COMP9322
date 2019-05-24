# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v6


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v6.bp,
        url_prefix='/v6')
    return app

if __name__ == '__main__':
    create_app().run("0.0.0.0",debug=True)
