# Buildbot Bug Hunt Challenge

## Step 1: Run test suites & store JUnit XML log
Enter the following command in your terminal. Ensure that you are in the `buildbot-1/` directory
```
./bb-testing/runTrial.sh
```

## Step 2: Open the Test Log Parser application (timer starts here!)
The JUnit XML log file should be in the directory `buildbot-1/bb-testing/junit-reports/`, and it will have the filename `TEST-${timestamp}.xml`
Enter the following commands in your terminal to open the Test Log Parser application, your time will begin as soon as you open the application
```
cd bb-testing
python3 bb-testing.py junit-reports/TEST-${timestamp}.xml
```

Remember to change ${timestamp} to the correct timestamp

## Step 3: Find the bug
There is a failing test case in the Failed Tests table. Identify the bug and fix it!
Your time will stop when you notify the examiner (Peter) regarding your completion

## Step 4: Re-run test suites & store JUnit XML log
Enter the following command in your terminal again. Ensure that you are in the `buildbot-1/` directory
```
./bb-testing/runTrial.sh
```

## Step 5: Check if all tests are passing
Open the Test Log Parser application again with the latest JUnit XML log file (ensure you have the latest timestamp for the filename `TEST-${timestamp}.xml`)
If there are 0 failing tests, you've completed the challenge!
Otherwise, the timer will be continued and you will have to go back to step 3