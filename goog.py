import time
from selenium import webdriver

driver = webdriver.Chrome("D:/Work/Browser Automation/chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
time.sleep(8)
driver.quit