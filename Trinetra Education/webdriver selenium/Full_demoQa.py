from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Navigate to https://demoqa.com

driver.get("https://demoqa.com/")
driver.maximize_window()

#Click to the Elements

driver.find_element(By.XPATH, "//h5[text()='Elements']").click()
time.sleep(5)

# Get List of Items under Elements

List_of_elements = driver.find_elements(By.CLASS_NAME, "header-wrapper")
print(" print all Elements name")
for i in List_of_elements:
    print(i.text)

# select text box

driver.find_element(By.CLASS_NAME, "text").click()
time.sleep(4)
print(" text box click successfully")

# Auto_suggestion = driver.find_elements(By.CLASS_NAME,"text")
# Select = select(Auto_suggestion)
# Select.index(0)
# time.sleep(5)

# Enter details and submit the form

driver.find_element(By.ID, "userName").send_keys(" I love my india ")
driver.find_element(By.ID, "userEmail").send_keys("sanjiptk@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys(" odisha")
driver.find_element(By.ID, "permanentAddress").send_keys("Bangalore")
driver.find_element(By.XPATH,"//button[@id ='submit']").click()
time.sleep(5)

#Fetch the output generated post submission and verify

output_Username = driver.find_element(By.ID, "userName").text
output_email =driver.find_element(By.ID, "userEmail").text
output_current_adress = driver.find_element(By.ID, "currentAddress").text
output_permanet_adress = driver.find_element(By.ID, "permanentAddress").text

print(" submitted all credetial document")
print(output_Username)
print(output_email)
print(output_current_adress)
print(output_permanet_adress)

# return back to the freeform page
driver.back()

time.sleep(6)


# Click on alert , frames and windows
driver.find_element(By.XPATH,"//h5[text()='Alerts, Frame & Windows']").click()






