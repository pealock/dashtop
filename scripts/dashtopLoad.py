import os
import sys
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from chromeOptions import options

# Load .env
load_dotenv()
destination = os.getenv("DESTINATION")

# Load webdriver based on OS
if 'linux' in sys.platform:
    service = Service(executable_path='/usr/bin/chromedriver')
else:
    service = Service()

# Define driver shorthand
driver = webdriver.Chrome(service=service,
                          options=options)
# Define timeout
wait = WebDriverWait(driver, 10)

# Initial website pull
driver.get(destination)
