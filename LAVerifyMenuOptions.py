# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
import time
import unittest
import xlrd
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-


def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

workbook = xlrd.open_workbook('DataLA.xlsx')
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == 1:
    AdjustResolution()

class Verify_LA_Menu_Options(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
       # self.driver.get('http://idwebtg.carsstage.org/#roadReports?timeFrame=TODAY&layers=roadReports%2CwinterDriving%2CweatherWarnings%2CotherStates')
        self.driver.get(url)


    def test_idaho_menu(self):

        driver = self.driver

        # Login To The System
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'sign-in-link')))
        driver.find_element_by_id('sign-in-link').click()
        driver.find_element_by_id('userAccountEmail').send_keys(username)
        driver.find_element_by_id('userAccountPassword').send_keys(password)
        driver.find_element_by_id('userAccountPassword').submit()

        # Check that the menu items are all present
        left_Panel_Wait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Ryan’s Favorites"]')))
        # Favorites
        assert (driver.find_element_by_xpath('//*[@title="Ryan’s Favorites"]').is_enabled()) == True, "Favorites Is Faulty"
        # All Reports
        assert driver.find_element_by_xpath("//*[contains(text(), 'All Reports')]").is_enabled(), "All Reports Is Faulty"
        # Flooding/Ice
        assert driver.find_element_by_xpath('//*[@title="See all flooding and ice reports"]').is_enabled(), "Flooding/Ice Is Faulty"
        # Road Reports
        assert driver.find_element_by_xpath('//*[@title="See all road reports"]').is_enabled(), "Road Reports Are Faulty"
        # Cameras
        assert driver.find_element_by_xpath('//*[@title="See maps and lists of cameras and view camera images"]').is_enabled(), "Cameras Are Faulty"
        # Google Speeds and Incidents
        assert driver.find_element_by_xpath('//*[@title="See up-to-date traffic conditions"]').is_enabled(), "Google Speeds And Incidents Are Faulty"
        # Ferry Status
        assert driver.find_element_by_xpath("//*[contains(text(), 'Ferry Status')]").is_enabled(), "Metro Traffic Map not present"


    def tearDown(self):
         self.driver.quit()


if __name__ == '__main__':
    unittest.main()
