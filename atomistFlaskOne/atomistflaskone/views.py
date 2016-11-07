# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['atomistflaskone_app']

atomistflaskone_app = Blueprint('atomistflaskone_app', __name__)


@atomistflaskone_app.route('/')
def index():
    return "Hello World!"
