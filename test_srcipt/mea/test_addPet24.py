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

class TestAddPet24():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addPet24(self):
    self.driver.get("http://mea/")
    # self.driver.set_window_size(1550, 830)
    self.driver.find_element(By.ID, "identifiant_connexion").send_keys("admin")
    self.driver.find_element(By.ID, "password_connexion").send_keys("admin")
    self.driver.find_element(By.ID, "bouton_connexion").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".arrow-middle-r").click()#24
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, "#lien_animaux > td:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
    self.driver.find_element(By.ID, "nom").send_keys("test")
    self.driver.find_element(By.ID, "race").send_keys("test")
    self.driver.find_element(By.ID, "date_naissance").send_keys("1")
    self.driver.find_element(By.ID, "bouton_animal_fermer").click()
    ##$##
    self.driver.find_element(By.ID, "lien_deconnexion").click()
    self.driver.close()
  
