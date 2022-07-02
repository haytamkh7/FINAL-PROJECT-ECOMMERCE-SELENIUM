import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("sajobi3111@meidir.com")
    time.sleep(4)
    # Password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("testing_909$")
    time.sleep(4)
    # Repeat-password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("testing_909$")
    time.sleep(4)
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    time.sleep(4)
    # Check authentication page
    assert driver.title == "Authentication required"


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
    first_product_name = driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/h2/a/span").text
    # Search for first_product_name in the search field
    driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys(first_product_name)
    time.sleep(3)
    # Click the search button
    driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button").click()
    time.sleep(3)
    # Get the name of the first product name after the search
    new_first_product_name = driver.find_element(By.CSS_SELECTOR,
                                                 "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > div > div > div > div > div > div.a-section.a-spacing-small.s-padding-left-small.s-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2 > a > span").text
    # Compare first product name before the search with the one after the search
    assert first_product_name == new_first_product_name


def test_end_to_end_buy_product(driver):
    # Email: tomeutube@gmail.com
    # Password: testing_909$

    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
    time.sleep(4)
    # Fill the email input with email address
    driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("tomeutube@gmail.com")
    time.sleep(4)
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    time.sleep(4)
    # Fill the password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("testing_909$")
    time.sleep(4)
    # Click the 'Sign-in' button
    driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()
    time.sleep(4)
    #  Bypass adding mobile number
    # driver.find_element(By.CSS_SELECTOR, "#ap-account-fixup-phone-skip-link").click()
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
    # Click on the second product from the second row
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div[2]/span/a/div").click()
    time.sleep(4)
    # Choosing custom color
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[1]/div[12]/div[1]/div/form/div/ul/li[1]").click()
    time.sleep(4)
    # Change quantity to 2
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/form/div/div/div/div/div[8]/div/div/span/div/div/span/span/span/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/ul/li[2]/a").click()
    time.sleep(2)
    # Click 'Add to Cart' button
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/form/div/div/div/div/div[10]/div[1]/span/span/span/input").click()
    time.sleep(2)
    # Click 'Proceed to checkout' button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div/form/span/span/input").click()
    time.sleep(2)
    # Filling the address data
    # Country/Region
    driver.find_element(By.XPATH,
                        "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[2]/span/span/span/span").click()
    driver.find_element(By.XPATH, "/html/body/div[8]/div/div/ul/li[108]/a").click()
    time.sleep(2)
    # Full Name
    full_name = driver.find_element(By.XPATH,
                                    "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[4]/input")
    full_name.send_keys("Jeff Smith")
    time.sleep(2)
    # Address
    address = driver.find_element(By.XPATH,
                                  "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[6]/input")
    address.send_keys("Ibillin, Main Street, 3001200")
    time.sleep(2)
    # City
    city = driver.find_element(By.XPATH,
                               "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[10]/input")
    city.send_keys("Ibillin")
    time.sleep(2)
    # State
    state = driver.find_element(By.XPATH,
                                "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[12]/input")
    state.send_keys("IL")
    time.sleep(2)
    # Zip Code
    zip_code = driver.find_element(By.XPATH,
                                   "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[14]/input")
    zip_code.send_keys("3001200")
    time.sleep(2)
    # Phone number
    phone_num = driver.find_element(By.XPATH,
                                    "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div[16]/input")
    phone_num.send_keys("0506501245")
    time.sleep(2)
    # Click 'Use this address' button
    driver.find_element(By.XPATH,
                        "/html/body/div[5]/div[2]/div[2]/div[1]/div/div[1]/form/div/span[3]/span/span/input").click()
    time.sleep(2)


def test_add_to_wishlist_signed_out(driver):
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
    # Click on the second product from the second row
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div[2]/span/a/div").click()
    time.sleep(4)
    # Click 'Add to List' button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/form/div/div/div/div/div[20]/div[1]/div[1]/span/span/a").click()
    time.sleep(4)
    # Verify that the current page is the sign-in page
    assert driver.title == "Amazon Sign-In"


def test_change_quantity_price(driver):
    # Email: tomeutube@gmail.com
    # Password: testing_909$

    # Open the web page
    driver.get('https://www.amazon.com/')
    time.sleep(4)
    # Click sign in button
    driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
    time.sleep(4)
    # Fill the email input with email address
    driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("tomeutube@gmail.com")
    time.sleep(4)
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    time.sleep(4)
    # Fill the password input
    driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("testing_909$")
    time.sleep(4)
    # Click the 'Sign-in' button
    driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()
    time.sleep(4)
    #  Bypass adding mobile number
    # driver.find_element(By.CSS_SELECTOR, "#ap-account-fixup-phone-skip-link").click()
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
    # Click on the second product from the second row
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div[2]/span/a/div").click()
    time.sleep(4)
    # Choose quantity 1
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/form/div/div/div/div/div[8]/div/div/span/div/div/span/span/span/span/span[1]").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/ul/li[1]/a").click()
    time.sleep(4)
    # Choosing custom color
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[1]/div[12]/div[1]/div/form/div/ul/li[1]").click()
    time.sleep(4)
    # Click 'Add to Cart' button
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div[1]/div[9]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/form/div/div/div/div/div[10]/div[1]/span/span/span/input").click()
    time.sleep(4)
    # Click 'Go to Cart' button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div/span/span/a").click()
    time.sleep(4)
    # Save the old price, before changing quantity
    old_price = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[2]/div/form/div/div/div[1]/span[2]/span").text
    # Choose quantity 2
    driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/span[1]/span/span/span/span").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[5]/div/div/ul/li[3]/a").click()
    time.sleep(4)
    # Save the new price, after changing quantity
    new_price = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[2]/div/form/div/div/div[1]/span[2]/span").text
    assert float(new_price[1:]) > float(old_price[1:])  # Use[1:]  to skip the dollar sign
