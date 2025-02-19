import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from chromeOptions import options
import inquirer


# Load webdriver based on OS
if 'linux' in sys.platform:
    service = Service(executable_path='/usr/bin/chromedriver')
else:
    service = Service()

history_file = open('../scripts/history.txt', 'r')
site_selection_options = []
for line in history_file:
    site_selection_options.append(line.replace('\n', ''))
site_selection_options.append('New Site')
print(site_selection_options)
site_select = [
    inquirer.List('site',
                  message="Which site would you like to load?",
                  choices=site_selection_options,
                  ),
]
selection = inquirer.prompt(site_select)
if selection['site'] == 'New Site':
    destination = input('Where would you like to go?: \n')
    file = open('../scripts/history.txt', 'a')
    file.write(f'\n{destination}')
    file.close()
else:
    destination = selection['site']

# Define driver shorthand
driver = webdriver.Chrome(service=service,
                          options=options)
# Define timeout
wait = WebDriverWait(driver, 10)

# Initial website pull
driver.get(destination)
