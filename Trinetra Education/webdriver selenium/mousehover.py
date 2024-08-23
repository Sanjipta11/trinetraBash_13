from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID"")