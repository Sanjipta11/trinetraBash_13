from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
static_dropdown = driver.find_element(By.id,"dropdown-class-example")
select = Select(static_dropdown)
select.select_by_index(2)
time.sleep(3)
select.select_by_visible_text("Option1")
time.sleep(4)
select.select_by_value("option3")
time.sleep(6)
driver.close()
