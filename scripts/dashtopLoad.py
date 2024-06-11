import os
import sys
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from chromeOptions import options

# Load destinatoin
load_dotenv()
destination = os.getenv("DESTINATION")

# Define targets
emailForm = "/html/body/div[1]/div/div/div[3]/form/div[1]/input"
baySelect = "/html/body/div[1]/div/div[4]/div/div[2]/i[1]"
baySelectConfirm = "/html/body/div[1]/div/div[4]/div/div[7]/div/div[2]/div[1]/div[6]/button"

# Load webdriver
if 'linux' in sys.platform:
    service = Service(executable_path='/usr/bin/chromedriver')
else:
    service = Service()

# Define driver
driver = webdriver.Chrome(service=service,
                          options=options)
# Define timeout
wait = WebDriverWait(driver, 10)

# Initial website pull
driver.get("https://droptop-app.com")