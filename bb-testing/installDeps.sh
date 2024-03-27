#!/bin/bash

# https://docs.buildbot.net/current/developer/quickstart.html
# Move to root directory (buildbot-1/)
python3 -m venv .venv

# run a helper script which creates the virtualenv for development.
# Virtualenv allows to install python packages without affecting
# other parts of the system.
# This script does not support Windows: you should create the virtualenv and install
# requirements-ci.txt manually.
make virtualenv

# activate the virtualenv
. .venv/bin/activate

# install dependencies for bb-testing
pip3 install junitxml==0.7
pip3 install python-subunit==1.4.4
pip3 install textual==0.53.1