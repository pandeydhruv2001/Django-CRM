from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# Start a new browser session
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)  # Waits up to 10 seconds

try:
    # Open the CRM login page
    driver.get("http://127.0.0.1:8000/")
    print("Navigating to CRM login page")

    # Fill in the login form
    wait.until(EC.presence_of_element_located((By.NAME, "first_name"))).send_keys("admin")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("tiger")
    print("Login credentials entered")

    # Submit the form
    wait.until(EC.element_to_be_clickable((By.NAME, "submit_button"))).click()
    print("Login form submitted")

except TimeoutException as e:
    print("A timeout occurred: ", str(e))
finally:
    # Close the browser
    driver.quit()
    print("Browser closed")
