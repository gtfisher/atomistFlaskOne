# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from atomistFlaskOne import __version__


setup(
    name="atomistFlaskOne",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["atomistFlaskOne", "atomistFlaskOne.atomistflaskone"],
    platforms=["any"]
)
