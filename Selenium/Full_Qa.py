from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (you can specify the path to your WebDriver executable)
driver = webdriver.Chrome()

# 1. Navigate to https://demoqa.com
driver.get("https://demoqa.com")

# 2. Click on Elements
elements_section = driver.find_element(By.XPATH, "//h5[text()='Elements']")
elements_section.click()

# 3. Get List of Items under Elements
list_of_items = driver.find_elements(By.CSS_SELECTOR, ".element-group .btn-light")
print("List of Items under Elements:")
for item in list_of_items:
    print(item.text)

# 4. Select Text Box
textbox_item = driver.find_element(By.XPATH, "//span[text()='Text Box']")
textbox_item.click()

# 5. Enter details and submit the form
driver.find_element(By.ID, "userName").send_keys("John Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Main Street")
driver.find_element(By.ID, "submit").click()

# 6. Fetch the output generated post submission and verify
output = driver.find_element(By.ID, "output")
print("Form Output:")
print(output.text)

# 7. Click on Alerts, Frames & Windows
alerts_frames_windows = driver.find_element(By.CLASS_NAME, "//h5[text()='Alerts, Frame & Windows']")
alerts_frames_windows.click()

# 8. Click Frames
frames_item = driver.find_element(By.XPATH, "//span[text()='Frames']")
frames_item.click()

# 9. Get details from both the text boxes
driver.switch_to.frame("frame1")
frame1_text = driver.find_element(By.ID, "sampleHeading").text
driver.switch_to.default_content()

driver.switch_to.frame("frame2")
frame2_text = driver.find_element(By.ID, "sampleHeading").text
driver.switch_to.default_content()

print("Frame 1 Text:", frame1_text)
print("Frame 2 Text:", frame2_text)

# 10. Click Alerts
alerts_item = driver.find_element(By.XPATH, "//span[text()='Alerts']")
alerts_item.click()

# 11. Click on 'Click me' next to the On button click, confirm box will appear
click_me_button = driver.find_element(By.ID, "confirmButton")
click_me_button.click()

# Wait for the alert and accept it
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# 12. Click Browser Windows
browser_windows_item = driver.find_element(By.XPATH, "//span[text()='Browser Windows']")
browser_windows_item.click()

# 13. Click on New Tab and get text from it
new_tab_button = driver.find_element(By.ID, "tabButton")
new_tab_button.click()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
new_tab_text = driver.find_element(By.ID, "sampleHeading").text
print("New Tab Text:", new_tab_text)

# Close the new tab and switch back to the main window
driver.close()
driver.switch_to.window(driver.window_handles[0])

# 14. Has context menu
context_menu_item = driver.find_element(By.XPATH, "//span[text()='Buttons']")
context_menu_item.click()

# Perform a right-click (context click) action
right_click_button = driver.find_element(By.ID, "rightClickBtn")
ActionChains(driver).context_click(right_click_button).perform()

# Wait and close the browser
driver.quit()
