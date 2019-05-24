# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import v7
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)
    app.register_blueprint(
        v7.bp,
        url_prefix='/v7')
    return app

if __name__ == '__main__':
    create_app().run(port=5002,debug=True)