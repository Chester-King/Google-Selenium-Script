import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("D:/Work/VOLSBB-Selenium-Script/chromedriver.exe")
# driver.get("https://www.google.com")
driver.get("http://gstatic.com/generate_204")

try:
    time.sleep(2)
    elem=driver.find_element_by_name('userId')
    print('Found reg entery')
    elem.send_keys("<Reg. Number>")
    time.sleep(2)
    elem=driver.find_element_by_name('password')
    time.sleep(2)
    elem.send_keys("<Password>")
    elem.send_keys(Keys.ENTER)
except Exception as e:
    pass



print(driver.title)
time.sleep(8)
driver.quit