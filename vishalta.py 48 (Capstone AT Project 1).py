from selenium import webdriver
   import pytest

   @pytest.fixture
   def browser():
       driver = webdriver.Chrome()
       yield driver
       driver.quit()

   def test_login_successful(browser):
       browser.get('URL_OF_ORANGE_HRM_LOGIN_PAGE')
       username = browser.find_element_by_id('txtUsername')
       password = browser.find_element_by_id('txtPassword')

       username.send_keys("Admin")
       password.send_keys("admin123")

       login_button = browser.find_element_by_id('btnLogin')
       login_button.click()

       assert browser.current_url == 'URL_AFTER_SUCCESSFUL_LOGIN'

   def test_login_invalid(browser):
       browser.get('URL_OF_ORANGE_HRM_LOGIN_PAGE')
       username = browser.find_element_by_id('txtUsername')
       password = browser.find_element_by_id('txtPassword')

       username.send_keys("Admin")
       password.send_keys("InvalidPassword")

       login_button = browser.find_element_by_id('btnLogin')
       login_button.click()

       error_message = browser.find_element_by_xpath('//div[@class="error-message"]').text
       assert "Invalid credentials" in error_message