#!/bin/sh
set -ex

flake8 src test
nosetests --with-coverage tests
