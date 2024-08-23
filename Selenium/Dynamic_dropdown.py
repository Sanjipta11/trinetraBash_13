
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Initialize options and set detach option
options = Options()
options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to Flipkart
driver.get("https://www.flipkart.com/")
# Find the input elements by XPath
search_boxes = driver.find_elements(By.XPATH, "//input[@type='text']")

# Assuming you want to interact with the first text input box
if search_boxes:
    search_box = search_boxes[0]
    # You can now interact with the search_box element, e.g., send keys to it
    search_box.send_keys(" i phone ")


