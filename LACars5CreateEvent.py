# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest
import xlrd
from selenium.webdriver.support.ui import Select
import datetime
import time
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-

# /Users/ryankavanaugh/Desktop/AmazonLA/

# Required Function For Working With Jenkins Virtual Machine
def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

# Pull link and user credentials from excel spreadsheet
workbook = xlrd.open_workbook('LA CARS 5 Links.xlsx')
worksheet = workbook.sheet_by_index(0)
url = worksheet.cell(1, 0).value
username = worksheet.cell(1, 1).value
password = worksheet.cell(1, 2).value
adjustResolution = worksheet.cell(1, 3).value

if adjustResolution == 1:
    AdjustResolution()

def Run_Script(driver):

    testFails = 0

    # try:
    # Login
    loginElement = driver.find_element_by_id('loginForm:usernameInput')
    passwordElement = driver.find_element_by_id('loginForm:passwordInput')
    loginElement.send_keys(username)
    passwordElement.send_keys(password)
    passwordElement.send_keys(Keys.ENTER)

    # Head To The Create An Event
    mainPageWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'topbar-create-event')))
    createEventButton = driver.find_element_by_id('topbar-create-event')
    createEventButton.click()

    time.sleep(4)

    # Fill in the from/at and to
    createEventWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'eventEditingScreenForm:routePointFromGrid')))

    # item = driver.find_element_by_class_name('gm-style-pbc')

    item = driver.find_element_by_id('mapToolbarDiv')

    #item = driver.find_element_by_class_name('lm_center')

    hover = ActionChains(driver).move_to_element(item).context_click(item)

    hover.perform()

    time.sleep(2)


    # Select first category and descriptor
    selectCategory1 = Select(driver.find_element_by_id('eventEditingScreenForm:categorySelect'))
    selectCategory1.select_by_visible_text('traffic conditions')
    descriptorsWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'phraseEntry')))
    #descriptors1 = driver.find_element_by_id('phraseEntry').send_keys('test')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@title="Select descriptor"]').send_keys('Heavy traffic')
    time.sleep(2)
    add_Button = driver.find_element_by_id('eventEditingScreenForm:addPhrase')
    add_Button.click()

    time.sleep(3)

    # Select second cateogry
    selectCategory1 = Select(driver.find_element_by_id('eventEditingScreenForm:categorySelect'))
    selectCategory1.select_by_visible_text('incident')
    descriptorsWait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'phraseEntry')))
    descriptors2 = driver.find_element_by_id('phraseEntry').send_keys('test')
    descriptors20 = driver.find_element_by_xpath('//*[@title="Select descriptor"]').send_keys('Abandoned vehicle')
    #driver.find_element_by_xpath('//*[@title="Select descriptor"]').send_keys(Keys.RETURN)
    time.sleep(2)
    add_Button2 = driver.find_element_by_id('eventEditingScreenForm:addPhrase')
    add_Button2.click()

    time.sleep(3)
    # Calendar
    calElem = driver.find_element_by_id('eventEditingScreenForm:startTimeCalendarInputDate')

    calElem.click()

    time.sleep(2)

    driver.find_element_by_id('eventEditingScreenForm:startTimeCalendarDayCell0').click()

    time.sleep(3)

    # Start time
    timeElem = driver.find_element_by_id('eventEditingScreenForm:startTimeCalendar_time')

    timeElem.click()

    selectHour = Select(driver.find_element_by_id('eventEditingScreenForm:startTimeCalendar_hour'))
    selectHour.select_by_visible_text('04')

    selectMinute = Select(driver.find_element_by_id('eventEditingScreenForm:startTimeCalendar_minute'))
    selectMinute.select_by_visible_text('30')

    selectAMorPM = Select(driver.find_element_by_id('eventEditingScreenForm:startTimeCalendar_ampm'))
    selectAMorPM.select_by_visible_text('PM')
    driver.find_element_by_xpath('//*[@value="Apply"]').click()

    driver.find_element_by_id('eventEditingScreenForm:createEvent').click()

    time.sleep(3)

    # Events list stuff

    driver.find_element_by_id('navMenu').click()

    time.sleep(3)

    driver.find_element_by_xpath("//*[contains(text(), 'Events List')]").click()

    time.sleep(3)

    todaysDate = str(time.strftime("%m/%d"))

    listXpath = "//*[contains(text()," +  " '" + todaysDate + "' "  + ")]"

    eventInEventsList = driver.find_element_by_xpath(listXpath)

    print eventInEventsList

    print eventInEventsList.text

    print eventInEventsList.get_attribute('InnerHTML')

    print eventInEventsList.get_attribute('onclick')


    eventInEventsList.click()

    time.sleep(3)

    testElem = driver.find_element_by_xpath("//*[contains(text(), 'LA 1 at Texas State Line (2 miles north of the Rodessa area). Traffic is heavy. Look out for an abandoned vehicle.')]")

    print testElem.get_attribute('OuterHTML')

    time.sleep(20)

class Verify_LA_Cars_5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_Login(self):
        driver = self.driver
        driver.maximize_window()

        print time.strftime("%m/%d")

       # todaysDate = time.strftime("%m/%d/%Y")
        try:
            Run_Script(driver)
        except:
            print "okayy"


if __name__ == '__main__':
    unittest.main()


            # login to CARS 5
# try to grab an icon
# 1. create an event (try moving mouse to middle of the page and then clicking on it)
# 2. assert event exist
# 3. Also, think about checking buttons are enabled and that security settings work, think of little nuances to grow test coverage...











