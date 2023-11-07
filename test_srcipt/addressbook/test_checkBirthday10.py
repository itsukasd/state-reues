# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCheckBirthday():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_checkBirthday(self):
    self.driver.get("http://1addressbook/")
    self.driver.set_window_size(1175, 629)
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.NAME, "searchform").click()
    self.driver.find_element(By.LINK_TEXT, "next birthdays").click()
    ##$##
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()