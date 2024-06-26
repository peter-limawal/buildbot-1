# Using the Test Log Parser app
## Disclaimer
This project was developed on macOS and most of the scripts & Makefiles uses PATHs that are macOS and Linux compatible. To use this project on Windows, you need to change all occurences `*/bin/*` into `*/Scripts/*` in `buildbot-1/Makefile` and `buildbot-1/bb-testing/installDeps.sh`
## Step 1: Set up virtual environment & install dependencies
Run the following commands in the root directory of the repository (`/buildbot-1`)
```
./bb-testing/installDeps.sh

. .venv/bin/activate (or . .venv/Scripts/activate for Windows)
```
## Step 2: Move into the `buildbot-1/bb-testing` directory
```
cd bb-testing
```
## Step 3: Run unit tests using `runTrial.sh` script
Make sure you are in the buildbot-1/bb-testing` directory
```
./runTrial.sh
```
This will generate a JUnit XML test log in the `buildbot-1/bb-testing/junit-reports` directory (the output on the command line will be garbage due to the piping).  
Note that the logs are named in the format `TEST-YYYY-MM-DD-HH-MM-SS.xml` (prefixed with `TEST-`, suffixed with `DATE-TIME.xml`).
## Step 4: Open the test log using the Test Log Parser app
Run the Test Log Parser app using Python with a relative path to the log file as an argument. You can
```
python3 bb-testing.py junit-reports/TEST-YYYY-MM-DD-HH-MM-SS.xml
```
Don't forget to change the suffix of the *relative path* argument to a valid log file.
## Step 5: Explore the Test Log Parser app
The six panels on the top of the app shows a summary of the test log.  
<img width="600" alt="Screenshot 2024-03-27 at 09 48 00" src="https://github.com/peter-limawal/buildbot-1/assets/59006829/3a69707d-3c53-4d73-88b6-584a8379c38b">  
The three different tables shows the details of the Failed, Skipped, and Passed test cases.  
You can use your mouse or arrow keys to scroll up and down from the table, and you can click or press ENTER to seen more details for each test case.  
<img width="600" alt="Screenshot 2024-03-27 at 09 49 05" src="https://github.com/peter-limawal/buildbot-1/assets/59006829/eed7e331-d54d-487a-8679-93e5f6614f6c">
