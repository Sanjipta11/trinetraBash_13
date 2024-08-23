from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check_boxes = driver.find_elements(By.XPATH,"//input[starts-with(@name,'checkBoxOption')]")
print(check_boxes)
print(len(check_boxes))
for check_box in check_boxes:
    # if check_boxes.index(check_box)+1<3:
    if check_boxes.index(check_box) + 1 !=2:
      check_box.click()