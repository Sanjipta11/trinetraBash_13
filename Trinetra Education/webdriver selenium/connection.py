import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# service_obj= service("path")
driver = webdriver.Chrome()
# driver = webdriver.firefox()
driver.get("https://www.facebook.com/")
# print(driver.title)
# # for checking the nav url or current url
# print(driver.current_url)
# time.sleep(5)
driver.find_element(By.id,value:"email").send_keys("vjgj")
driver.find_element(By.id)