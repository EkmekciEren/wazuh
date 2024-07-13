from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import time
 
# Specify the file path to download
download_dir = ""
# Configure Chrome options
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option("prefs", prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
#enter wazuh url
wazuhUrl = ""

def login():
    driver.get(wazuhUrl)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "details-button"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "proceed-link"))
    ).click()

    loginUsername = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='username_input']"))
    )

    #enter username
    loginUsername.send_keys("")

    loginPassword = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@aria-label='password_input']"))
    )
    #enter password
    loginPassword.send_keys("")
    loginPassword.send_keys(Keys.ENTER)
    time.sleep(5)  

def mainMenu():
    mainMenu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "header__homeLoaderNavButton"))
    )
    mainMenu.click()
    print("Main menu opened")
    time.sleep(5)

def generateReport():
    try:
        generateReport = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="euiButtonEmpty__text" and text()="Generate report"]'))
        )
        print("report button information received")
        generateReport.click()
        print("report created..")
    except StaleElementReferenceException:
        print("The item has gone stale and is being found again...")
        generateReport = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="euiButtonEmpty__text" and text()="Generate report"]'))
        )
        generateReport.click()
        print("The report has been recreated.")
    time.sleep(3)

def yanMenu():    
    yanMenu = driver.find_element(By.CSS_SELECTOR, 'svg[viewBox="0 0 16 16"] path[d="M0 2h16v2H0V2Zm0 5h16v2H0V7Zm16 5H0v2h16v-2Z"]')
    print("side menu selected")
    yanMenu.click()
    print("side menu opened")
    time.sleep(3)

def reportDownload():
    dashboardManagement = driver.find_element(By.XPATH, '//h3[contains(text(), "Dashboard management")]')
    print("dashboard received")
    dashboardManagement.click()
    print("dashboard management clicked.")
    time.sleep(3)
    reporting = driver.find_element(By.XPATH, '//a[@class="euiListGroupItem__button" and @href="https://51.136.2.204/app/reporting"]')
    print("reporting received")
    reporting.click()
    print("reporting clicked")
    time.sleep(3)
    downloadReport = driver.find_element(By.XPATH, "//button[@aria-label='Dowload report']")
    print("Report received")
    downloadReport.click()
    print("Report downloaded..")
    time.sleep(5)

def PCIDSSReport():
    login()
    mainMenu()
    time.sleep(3)
    PCIDSSButton = driver.find_element(By.CSS_SELECTOR, '[data-test-subj="overviewWelcomePci-dss"]')
    print("PCIDSSButton information retrieved")
    PCIDSSButton.click()
    print("Switched to PCI DSS menu")
    generateReport()
    yanMenu()
    reportDownload()
    time.sleep(5)

PCIDSSReport()
driver.quit()