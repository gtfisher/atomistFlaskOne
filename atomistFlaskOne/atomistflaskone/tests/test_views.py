# -*- coding: utf-8 -*-
from flask import url_for


def test_atomistflaskone_index(client):
    res = client.get(url_for('atomistflaskone_app.index'))
    assert res.data == b'Hello World!'
