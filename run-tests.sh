#!/bin/sh
set -ex

flake8 --exclude bottle.py src test
nosetests --with-coverage test
