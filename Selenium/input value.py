from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"checkBoxOption1").click()
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sanjipt")
# driver.find_element(By.XPATH,"//input[@id='name']").clear()
# driver.find_element(By.XPATH,"//input[@id='name']").send_keys("addi")
# 2nd method
input_field =driver.find_element(By.XPATH,"//input[@id='name']")
input_field.send_keys("sanjipt")
input_field.clear()
input_field.send_keys("addi")
driver.find_element(By.XPATH,"//legend[text()='Switch To Alert Example']")
alert_example_text = alert_example.text
print(alert_example_text)