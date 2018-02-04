# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Trade1(unittest.TestCase):

    
    def test_trade1(self):
        driver = self.driver
        driver.get("https://demo.kantox.com/en/secure/hedges/new")
        driver.find_element_by_link_text("Trade").click()
        driver.find_element_by_id("remain_amount").click()
        driver.find_element_by_id("remain_amount").clear()
        driver.find_element_by_id("remain_amount").send_keys("1.000,00")
        driver.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        driver.find_element_by_link_text("8").click()
        driver.find_element_by_css_selector("textarea.notes").click()
        driver.find_element_by_css_selector("textarea.notes").clear()
        driver.find_element_by_css_selector("textarea.notes").send_keys("abc")
        driver.find_element_by_id("update").click()
        driver.find_element_by_name("signing_key").click()
        driver.find_element_by_name("signing_key").clear()
        driver.find_element_by_name("signing_key").send_keys("IHKQKYZ")
        driver.find_element_by_css_selector("div.row > #update").click()
        driver.find_element_by_id("continue").click()
    
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
