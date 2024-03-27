#!/bin/bash

# we use the subunit (version 1) reporter to create machine-readable log output
TRIALFLAGS="--reporter=subunit"
TESTDIR="buildbot"
TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)

if [ $# -eq 1 && $1 == "--parallel" ]; then
    TRIALFLAGS="-j16 --reporter=subunit"
fi

cd ..

# run the trial unit test
# we pipe the machine-readable log output to a subunitv1 to subunitv2 converter,
#       and then we pipe it to a subunitv2 to junitxml converter
trial ${TRIALFLAGS} ${TESTDIR} | subunit-1to2 | subunit2junitxml --forward -o bb-testing/junit-reports/TEST-${TIMESTAMP}.xml

exit 0