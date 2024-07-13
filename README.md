# wazuh
Wazuh Automatic Reporting with Selenium

# Installing selenium and chromium for macOS

brew update
brew install python
brew install --cask google-chrome
brew install chromedriver
pip install selenium
python3 -m venv myenv
source myenv/bin/activate
pip install selenium

#After installation, configure the empty sections in the Python files according to your wazuh settings and system settings.

#Specify the directory to download from
download_dir = "" 

#enter wazuh url
wazuhUrl = ""

#enter username
loginUsername.send_keys("")

#enter password 
loginPassword.send_keys("")

#If you want to change the duration of automatic reporting, change the value of the sleep function under the run_script.sh file.
sleep 1800 default

#After doing this for each python file authorize the bash file and run
chmod +x run_script.sh
./run_script.sh