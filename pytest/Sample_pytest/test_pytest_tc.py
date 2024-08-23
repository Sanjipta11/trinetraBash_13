def test_pytest_tc_one():
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

def test_pytest_tc_two():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.ID, "checkBoxOption1").click()
    # driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sanjipt")
    # driver.find_element(By.XPATH,"//input[@id='name']").clear()
    # driver.find_element(By.XPATH,"//input[@id='name']").send_keys("addi")
    # 2nd method
    input_field = driver.find_element(By.XPATH, "//input[@id='name']")
    input_field.send_keys("sanjipt")
    input_field.clear()
    input_field.send_keys("addi")
    driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']")
    alert_example_text = alert_example.text
    print(alert_example_text)

def test_pytest_tc_three():
    print("all are redy to fight boys ")


