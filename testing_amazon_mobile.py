import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    Firefox_driver_binary = "./geckodriver"
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=360")
    fire_fox_options.add_argument("--height=800")
    fire_fox_options.set_preference("general.useragent.override",
                                    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver
    driver.close()


def test_register(driver):
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.XPATH, '//*[@id="nav-logobar-greeting"]').click()
    time.sleep(4)
    # Click create account button
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/a/i').click()
    time.sleep(4)
    # Full name input
    driver.find_element(By.XPATH, '//*[@id="ap_customer_name"]').send_keys("Jeff Smith")
    time.sleep(4)
    # Mobile/Email input
    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys("tomeutube@gmail.com")
    time.sleep(4)
    # Password input
    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys("testing_909$")
    time.sleep(4)
    # Click the continue button
    # driver.find_element(By.XPATH, '//*[@id="continue"]').click()


def test_invalid_email_login(driver):
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.XPATH, '//*[@id="nav-logobar-greeting"]').click()
    time.sleep(4)
    # Fill the email input with invalid email address
    driver.find_element(By.XPATH, '//*[@id="ap_email_login"]').send_keys("imaginaryemail@email.liar")
    time.sleep(4)
    # Click the continue button
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.a-button-stack > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)')))
    driver.find_element(By.CSS_SELECTOR,
                        '.a-button-stack > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)').click()
    time.sleep(4)
    # Verify error message is displayed
    error_msg = driver.find_element(By.CSS_SELECTOR,
                                    "#auth-warning-message-box > div:nth-child(1) > h4:nth-child(1)").text
    assert error_msg == "No account found with email address"


def test_error_message_mandatory_fields(driver):
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.XPATH, '//*[@id="nav-logobar-greeting"]').click()
    time.sleep(4)
    # Click create account button
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/a/i').click()
    time.sleep(4)
    # Leave the mandatory fields empty and click the continue button
    driver.find_element(By.CSS_SELECTOR, "#auth-continue > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(10)
    # Verifying error messages has been displayed
    # Checking the full name field (error message)
    assert driver.find_element(By.CSS_SELECTOR,
                               '.auth-error-messages > li:nth-child(1) > span:nth-child(1)').text == "Enter your name"
    time.sleep(2)
    # Checking the email/mobile field (error message)
    assert driver.find_element(By.CSS_SELECTOR,
                               '.auth-error-messages > li:nth-child(5) > span:nth-child(1)').text == "Enter your email or mobile phone number"
    time.sleep(2)
    # Checking the password field (error message)
    assert driver.find_element(By.CSS_SELECTOR,
                               '.auth-error-messages > li:nth-child(6) > span:nth-child(1)').text == "Enter your password"


def test_error_message_incorrect_values(driver):  # come back check this test case
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.XPATH, '//*[@id="nav-logobar-greeting"]').click()
    time.sleep(4)
    # Click create account button
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/a/i').click()
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
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR, "#auth-continue > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(30)
    # Verify error messages box for entering incorrect values in fields are displayed
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-alert-heading")))
    assert driver.find_element(By.CSS_SELECTOR, ".a-alert-heading").text == "There was a problem"


def test_search_product(driver):
    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click the menu button
    driver.find_element(By.CSS_SELECTOR, "#nav-hamburger-menu > i:nth-child(1)").click()
    time.sleep(3)
    # Click 'All' button
    driver.find_element(By.CSS_SELECTOR, ".hmenu-compressed-btn").click()
    time.sleep(4)
    # Click the clothes section
    driver.find_element(By.CSS_SELECTOR,
                        ".hmenu-compress-section > li:nth-child(10) > a:nth-child(1)").click()
    time.sleep(4)
    # Click 'Women's Fashion' button
    driver.find_element(By.CSS_SELECTOR,
                        "ul.hmenu:nth-child(11) > li:nth-child(4) > a:nth-child(1)").click()
    time.sleep(4)
    # Click 'Handbags' button
    driver.find_element(By.CSS_SELECTOR,
                        "#sobe_m_b_2_3 > a:nth-child(1)").click()
    time.sleep(4)
    # Go to the first category
    driver.find_element(By.CSS_SELECTOR,
                        ".a-cardui-teaser > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
    time.sleep(4)
    # Get the name of the first product
    first_product_name = driver.find_element(By.CSS_SELECTOR,
                                             ".widgetId\=search-results_1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > a:nth-child(1) > div:nth-child(1) > h2:nth-child(2)").text
    # Search for first_product_name in the search field
    driver.find_element(By.CSS_SELECTOR, "#nav-search-keywords").send_keys(first_product_name)
    time.sleep(3)
    # Click the search button
    driver.find_element(By.CSS_SELECTOR, ".nav-search-submit > input:nth-child(1)").click()
    time.sleep(3)
    # Get the name of the first product name after the search
    new_first_product_name = driver.find_element(By.CSS_SELECTOR,
                                                 ".widgetId\=search-results_3 > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > a:nth-child(1) > div:nth-child(1) > h2:nth-child(1)").text
    # Compare first product name before the search with the one after the search
    assert first_product_name == new_first_product_name


def test_end_to_end_buy_product(driver):
    # Email: tomeutube@gmail.com
    # Password: testing_909$

    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.XPATH, '//*[@id="nav-logobar-greeting"]').click()
    time.sleep(4)
    # Fill the email input with email address
    driver.find_element(By.CSS_SELECTOR, "#ap_email_login").send_keys("tomeutube@gmail.com")
    time.sleep(4)
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR,
                        ".a-button-stack > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(4)
    # Hide password
    driver.find_element(By.CSS_SELECTOR,
                        "#auth-show-password-checkbox-container > label:nth-child(1) > i:nth-child(2)").click()
    time.sleep(4)
    # Fill the password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("testing_909$")
    time.sleep(4)
    # Click the 'Sign-in' button
    driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()
    time.sleep(4)
    #  Bypass adding mobile number
    # driver.find_element(By.CSS_SELECTOR, "#ap-account-fixup-phone-skip-link").click()
    # Click the menu button
    # driver.find_element(By.CSS_SELECTOR, "#nav-hamburger-menu > i:nth-child(1)").click()
    # time.sleep(4)
    # Click 'See All' button
    # driver.find_element(By.CSS_SELECTOR,
    #                     ".hmenu-compressed-btn").click()
    # time.sleep(4)
    # # Click on the clothes section
    # driver.find_element(By.CSS_SELECTOR, ".hmenu-compress-section > li:nth-child(10) > a:nth-child(1)").click()
    # time.sleep(4)
    # # Click 'Women's Fashion' button
    # driver.find_element(By.CSS_SELECTOR,
    #                     "ul.hmenu:nth-child(11) > li:nth-child(4) > a:nth-child(1)").click()
    # time.sleep(4)
    # # Click 'Handbags' button
    # driver.find_element(By.CSS_SELECTOR,
    #                     "#sobe_m_b_2_3 > a:nth-child(1)").click()
    # time.sleep(4)
    # # Click on the second type of handbags
    # driver.find_element(By.CSS_SELECTOR,
    #                     ".a-cardui-teaser > ul:nth-child(1) > li:nth-child(2) > span:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
    # time.sleep(4)
    # # Click on the second product from the second row
    # driver.find_element(By.CSS_SELECTOR,
    #                     ".widgetId\=search-results_4 > div:nth-child(1) > div:nth-child(3) > span:nth-child(1) > a:nth-child(1) > div:nth-child(1) > h2:nth-child(1)").click()
    # time.sleep(4)
    # # Choosing custom color
    # driver.find_element(By.CSS_SELECTOR,
    #                     "#color_name_1 > span:nth-child(1) > input:nth-child(1)").click()
    # time.sleep(4)
    # # Change quantity to 2
    # driver.find_element(By.CSS_SELECTOR,
    #                     "#a-autoid-39-announce").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#mobileQuantityDropDown_1").click()
    # time.sleep(2)
    driver.get("https://www.amazon.com/Timberland-Leather-Wallet-Clutch-Organizer/dp/B07T2F1VFJ/ref=mp_s_a_1_4?c=ts&keywords=Women%27s+Wallets&qid=1656369437&s=apparel&sr=1-4&ts_id=2475898011")
    time.sleep(4)
    # change color
    driver.find_element(By.CSS_SELECTOR, "#color_name_4 > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(4)
    # change quantity to 2
    driver.find_element(By.CSS_SELECTOR, ".a-dropdown-label").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#mobileQuantityDropDown_1").click()
    time.sleep(4)
    # Click 'Add to Cart' button
    driver.find_element(By.CSS_SELECTOR,
                        "#add-to-cart-button").click()
    time.sleep(4)
    # Click 'Proceed to checkout' button
    driver.find_element(By.CSS_SELECTOR, "#a-autoid-0 > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(4)
    # Filling the address data
    # Country/Region
    driver.find_element(By.CSS_SELECTOR, "div.a-spacing-base:nth-child(2) > span:nth-child(1)").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#address-ui-widgets-countryCode-dropdown-nativeId_107").click()
    time.sleep(4)
    # Full Name
    full_name = driver.find_element(By.CSS_SELECTOR,
                                    "#address-ui-widgets-enterAddressFullName")
    full_name.send_keys("Jeff Smith")
    time.sleep(4)
    # Address
    address = driver.find_element(By.CSS_SELECTOR,
                                  "#address-ui-widgets-enterAddressLine1")
    address.send_keys("Ibillin, Main Street, 3001200")
    time.sleep(4)
    # City
    city = driver.find_element(By.CSS_SELECTOR,
                               "#address-ui-widgets-enterAddressCity")
    city.send_keys("Ibillin")
    time.sleep(4)
    # State
    state = driver.find_element(By.CSS_SELECTOR,
                                "#address-ui-widgets-enterAddressStateOrRegion")
    state.send_keys("IL")
    time.sleep(4)
    # Zip Code
    zip_code = driver.find_element(By.CSS_SELECTOR,
                                   "#address-ui-widgets-enterAddressPostalCode")
    zip_code.send_keys("3001200")
    time.sleep(4)
    # Phone number
    phone_num = driver.find_element(By.CSS_SELECTOR,
                                    "#address-ui-widgets-enterAddressPhoneNumber")
    phone_num.send_keys("0506501245")
    time.sleep(4)
    # Click 'Use this address' button
    driver.find_element(By.CSS_SELECTOR,
                        "#address-ui-widgets-form-submit-button > span:nth-child(1) > input:nth-child(1)").click()
    time.sleep(4)
