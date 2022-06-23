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

    def test_error_message_incorrect_values(driver):
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
        # Fill the full name input with wrong/invalid value (for instance: a number)
        driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys("9098987")
        time.sleep(4)
        # Fill the email input with incorrect email address
        driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("imaginaryemail- 9@emailliar")
        time.sleep(4)
        # Fill the password input with wrong/invalid password
        driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("short")
        time.sleep(4)
        # Repeat-password input with the same wrong/invalid password
        driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("short")
        time.sleep(4)
        # Click the continue button
        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        time.sleep(4)
        # Verify error messages for entering incorrect values in fields are displayed
        # Checking the incorrect email/mobile error message
        assert driver.find_element(By.CSS_SELECTOR, "#auth-email-invalid-claim-alert > div > div").is_displayed()
        # Checking the invalid password error message
        assert driver.find_element(By.CSS_SELECTOR, "#auth-password-invalid-password-alert > div > div").is_displayed()

    def test_search_product(driver):
        # Open the web page
        driver.get('https://www.amazon.com/')
        time.sleep(4)
        # Click 'All' button
        driver.find_element(By.CSS_SELECTOR, "#nav-hamburger-menu").click()
        time.sleep(4)
        # Click 'See All' button
        driver.find_element(By.CSS_SELECTOR,
                            "#hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(12) > a.hmenu-item.hmenu-compressed-btn").click()
        time.sleep(4)
        # Click 'Women's Fashion' button
        driver.find_element(By.CSS_SELECTOR,
                            "#hmenu-content > ul.hmenu.hmenu-visible > ul:nth-child(11) > li:nth-child(5) > a").click()
        time.sleep(4)
        # Click 'Handbags' button
        driver.find_element(By.CSS_SELECTOR,
                            "#hmenu-content > ul.hmenu.hmenu-visible.hmenu-translateX > li:nth-child(7) > a").click()
        time.sleep(4)
        # Get the name of the first product displayed on page
        first_product_name = driver.find_element(By.CSS_SELECTOR,
                                                 "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > div > div > div > div.a-section.a-spacing-small.s-padding-left-small.s-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2 > a > span").text
        # Search for first_product_name in the search field
        driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys(first_product_name)
        time.sleep(3)
        # Click the search button
        driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button").click()
        time.sleep(3)
        # Get the name of the first product name after the search
        new_first_product_name = driver.find_element(By.CSS_SELECTOR,
                                                     "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > div > div > div > div.a-section.a-spacing-small.s-padding-left-small.s-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2 > a > span").text
        # Compare first product name before the search with the one after the search
        assert first_product_name == new_first_product_name
