# from selenium.webdriver.chrome import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import pytest
#
#
# @pytest.fixture()
# def driver():
#     chrome_options = ChromeOptions()
#     chrome_driver_binary = "chromedriver.exe"
#     chrome_options.add_argument("--width=390")
#     chrome_options.add_argument("--height=844")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
#                                 "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
#     ser_chrome = ChromeService(chrome_driver_binary)
#     driver = webdriver.Chrome(service=ser_chrome, options=chrome_options)
#     yield driver
#     driver.close()
#
#
# def test_google(driver):
#     driver.get("https://www.google.com/")
#     title = driver.title
#     assert title == str.title("google")
