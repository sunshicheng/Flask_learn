#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
from werkzeug.exceptions import HTTPException
from flask import Flask, current_app
from flask import jsonify
from API import api
from LoggerSetting import  FileLogger
from flask import request

def handle_error_exception(e):
    if current_app.debug:
        pass
    FileLogger.error("{0} exception {1}".format(request.full_path, e))
    return jsonify(errormsg=str(e)), 500


def handle_http_error_exception(e):
    if current_app.debug:
        pass
    FileLogger.error("{0} exception {1}".format(request.full_path,e))
    res = jsonify(errormsg=e.description)
    return res, e.code


def create_flask_app():
    app = Flask(__name__)
    app.config.from_pyfile('./ServiceConfig.py')
    app.register_blueprint(api)
    DB.init_app(app)
    app.register_error_handler(HTTPException, handle_http_error_exception)
    app.register_error_handler(Exception, handle_error_exception)
    return app
