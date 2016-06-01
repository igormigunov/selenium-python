# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginAndlogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stellus.devicepros.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_andlogout(self): 
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        #driver.find_element_by_id(By.id("dropdownMenu1").click()
        #driver.find_element_by_link_text("Logout").click()
        #driver.get("http://stellus.devicepros.net/")
        print("name=username")
        print("name=password")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("dropdownMenu1").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
