from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to https://demoqa.com
driver.get("https://demoqa.com/")
driver.maximize_window()

# Click on the "Elements" section
driver.find_element(By.XPATH, "//h5[text()='Elements']").click()
time.sleep(5)

# Get List of Items under Elements
list_of_elements = driver.find_elements(By.CLASS_NAME, "header-wrapper")
print("Print all Elements names:")
for element in list_of_elements:
    print(element.text)

# Select the Text Box option
driver.find_element(By.XPATH, "//span[text()='Text Box']").click()
time.sleep(4)
print("Text box clicked successfully")

# Enter details and submit the form
driver.find_element(By.ID, "userName").send_keys("I love my India")
driver.find_element(By.ID, "userEmail").send_keys("sanjiptk@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Odisha")
driver.find_element(By.ID, "permanentAddress").send_keys("Bangalore")
driver.find_element(By.ID, "submit").click()
time.sleep(5)

# Fetch the output generated post submission and verify
output_username = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text
output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

print("Submitted all credentials:")
print(output_username)
print(output_email)
print(output_current_address)
print(output_permanent_address)

# Return back to the homepage
driver.get("https://demoqa.com/")
time.sleep(6)

# Click on "Alerts, Frame & Windows"
driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']").click()

# Close the browser
time.sleep(5)
driver.quit()


