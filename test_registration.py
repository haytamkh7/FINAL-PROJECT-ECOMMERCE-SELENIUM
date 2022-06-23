import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture()
def driver():
    # chrome_driver_binary = "chromedriver.exe"
    # ser_chrome = ChromeService(chrome_driver_binary)

    # driver = webdriver.Chrome(service=ser_chrome)
    dc = {
        "browserName": "chrome",
        "platformName": "Windows 11"

    }
    # Selenium grid standAlone
    driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)
    yield driver
    driver.close()


def test_register(driver):
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
    time.sleep(4)
    # Click create account button
    driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
    time.sleep(4)
    # Full name input
    driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys("Jeff Smith")
    time.sleep(4)
    # Mobile/Email input
    driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("tomeutube@gmail.com")
    time.sleep(4)
    # Password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("sawiv777")
    time.sleep(4)
    # Repeat-password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("sawiv777")
    time.sleep(4)
    # Click the continue button
    # driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def test_invalid_email_login(driver):
        # Open the web page
        driver.get('https://www.amazon.com/')
        time.sleep(4)
        # Click sign in button
        driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
        time.sleep(4)
        # Fill the email input with invalid email address
        driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("imaginaryemail@email.liar")
        time.sleep(4)
        # Click the continue button
        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        time.sleep(4)
        # Validate that the error message is displayed
        assert driver.find_element(By.CSS_SELECTOR,
                                   "#auth-error-message-box > div > div > ul > li > span").is_displayed()
        time.sleep(4)

    def test_error_message_mandatory_fields(driver):
        # Open the web page
        driver.get('https://www.amazon.com/')
        time.sleep(4)
        # Click sign in button
        driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
        time.sleep(4)
        # Fill the email input with email address
        driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("imaginaryemail@email.liar")
        time.sleep(4)
        # Click create account button
        driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
        time.sleep(4)
        # Leave the mandatory fields empty and click the continue button
        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        time.sleep(4)
        # Verifying error messages has been displayed
        # Checking the full name field (error message)
        assert driver.find_element(By.CSS_SELECTOR, "#auth-customerName-missing-alert > div > div").is_displayed()
        # Checking the email/mobile field (error message)
        assert driver.find_element(By.CSS_SELECTOR, "#auth-email-missing-alert > div > div").is_displayed()
        # Checking the password field (error message)
        assert driver.find_element(By.CSS_SELECTOR, "#ap_password").is_displayed()
