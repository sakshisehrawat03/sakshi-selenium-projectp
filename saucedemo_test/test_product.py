from selenium import webdriver
import pytest
@pytest.mark.set1
def test_product_01():
  driver_path= "chromedriver.exe"
  driver= webdriver.Chrome (executable_path=driver_path)
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/")
  driver.find_element_by_id("user-name"). send_keys("standard_user")
  driver.find_element_by_id("password"). send_keys("secret_sauce")
  driver.find_element_by_id("login-button"). click()
  driver.find_element_by_id("add-to-cart-sauce-labs-bike-light"). click()
  driver.find_element_by_id("add-to-cart-test.allthethings()-t-shirt-(red)").click()
  driver.quit()

def test_product_02():
  driver_path= "chromedriver.exe"
  driver= webdriver.Chrome (executable_path=driver_path)
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/")
  driver.find_element_by_id("user-name"). send_keys("standard_user")
  driver.find_element_by_id("password"). send_keys("secret_sauce")
  driver.find_element_by_id("login-button"). click()
  driver.find_element_by_id("add-to-cart-sauce-labs-bike-light"). click()
  driver.quit()