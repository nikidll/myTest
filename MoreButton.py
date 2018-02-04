# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MoreButton(unittest.TestCase):

    
    def test_more_button(self):
        driver = self.driver
        driver.get("https://demo.kantox.com/en/secure/api_docs#/companies")
        driver.find_element_by_link_text("More").click()
        driver.find_element_by_id("client_settings").click()
        driver.find_element_by_link_text("More").click()
        driver.find_element_by_id("profiles_settings").click()
        driver.find_element_by_link_text("More").click()
        driver.find_element_by_id("profile_switch").click()
    
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
