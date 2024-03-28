# Buildbot Bug Hunt Challenge

## Step 1: Run test suites & store output log
Enter the following command in your terminal. Ensure that you are in the `buildbot-1/` directory
```
trial --reporter=subunit buildbot > bb-testing/trial-reports/TEST-$(date +%Y-%m-%d-%H-%M-%S).log
```

## Step 2: Open the output log file (timer starts here!)
The output log file should be in the directory `buildbot-1/bb-testing/trial-reports/`, and it will have the filename `TEST-${timestamp}.log`
Use the VSCode file explorer to open this file, your time will start as soon as you open the file

## Step 3: Find the bug
There is a failing test case in the output log file. Identify the bug and fix it!
Your time will stop when you notify the examiner (Peter) regarding your completion

## Step 4: Re-run test suites & store output log
Enter the following command in your terminal again. Ensure that you are in the `buildbot-1/` directory
```
trial --reporter=subunit buildbot > bb-testing/trial-reports/TEST-$(date +%Y-%m-%d-%H-%M-%S).log
```

## Step 5: Check if all tests are passing
Open the latest output log file in the `buildbot-1/bb-testing/trial-reports/` directory
If there are 0 failing tests, you've completed the challenge!
Otherwise, the timer will be continued and you will have to go back to step 3