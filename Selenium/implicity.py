from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait()
driver.get("https://www.flipkart.com/")
login_popup_close_button = driver.find_element()

