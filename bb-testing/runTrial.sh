#!/bin/bash

TRIALFLAGS="--reporter=subunit"
TESTDIR="buildbot"
TIMESTAMP=$(date +%Y-%m-%d-%H:%M:%S)

if [ $# -eq 1 && $1 == "--parallel" ]; then
    TRIALFLAGS="-j16 --reporter=subunit"
fi

# https://docs.buildbot.net/current/developer/quickstart.html
# Move to root directory (buildbot-1/)
cd ..

# run a helper script which creates the virtualenv for development.
# Virtualenv allows to install python packages without affecting
# other parts of the system.
# This script does not support Windows: you should create the virtualenv and install
# requirements-ci.txt manually.
make virtualenv

# activate the virtualenv (you should now see (.venv) in your shell prompt)
. .venv/bin/activate

# install dependencies for bb-testing
pip3 install junitxml
pip3 install python-subunit
pip3 install textual==0.53.1

# run the trial unit test
trial ${TRIALFLAGS} ${TESTDIR} | subunit-1to2 | subunit2junitxml --forward -o bb-testing/junit-reports/TEST-${TIMESTAMP}.xml

exit 0