# Wazuh Automatic Reporting with Selenium

This guide explains how to set up and use Selenium with Chromium on macOS to automate reporting for Wazuh.

## Installation Instructions

### Step 1: Update Homebrew and Install Dependencies
Open your terminal and run the following commands:

```bash
brew update
brew install python
brew install --cask google-chrome
brew install chromedriver
 ```
 ### Step 2: Install Python Packages
 Create a virtual environment and install Selenium:

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install selenium
 ```
### Step 3: Configure Python Files
Open the Python files and fill in the necessary settings according to your Wazuh setup:

Download Directory: Specify the directory where you want to download files:
```bash
download_dir = "path/to/download/directory"
```
Wazuh URL: Enter the URL for your Wazuh instance:
```bash
wazuhUrl = "http://your-wazuh-url"
```
Login Credentials: Enter your Wazuh login username and password:

```bash
loginUsername.send_keys("your-username")
loginPassword.send_keys("your-password")
```

### Step 4: Adjust Reporting Interval
If you want to change the duration of automatic reporting, modify the value of the sleep function in the run_script.sh file. The default is set to 1800 seconds (30 minutes):

```bash
sleep 1800
```
# Running the Script

### Step 5: Authorize and Execute the Bash Script
Make the bash script executable and run it:

```bash
chmod +x run_script.sh
./run_script.sh
```
By following these steps, you should be able to set up and run the Selenium scripts for automated reporting with Wazuh on macOS.