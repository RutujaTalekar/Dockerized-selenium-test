#!/usr/bin/python3

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# passing the selenium endpoint and chrome options 
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

# a simple test
driver.get("https://www.uga.edu/")
time.sleep(1)
print(driver.title)


driver.quit()
