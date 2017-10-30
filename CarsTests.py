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

driver = webdriver.Chrome()

url = driver.get('http://la.carsstage.org/cars5/secure/main.jsf')

loginElement = driver.find_element_by_id('loginForm:usernameInput')
passwordElement = driver.find_element_by_id('loginForm:passwordInput')
loginElement.send_keys('rkavanaugh')
passwordElement.send_keys('test')
passwordElement.send_keys(Keys.ENTER)



driver.find_element_by_id('navMenu').click()

time.sleep(3)

driver.find_element_by_xpath("//*[contains(text(), 'Events List')]").click()

time.sleep(3)

todaysDate = str(time.strftime("%m/%d") + "/17")

#listXpath = "//*[contains(text()," +  " '" + todaysDate + "' "  + ")]"

listXpath = '//*[@title=' + '"' + todaysDate + '"' + ']'

eventInEventsList = driver.find_element_by_xpath(listXpath)


cars4IDWithText = eventInEventsList.get_attribute('onclick')
print cars4IDWithText
cars4ID = cars4IDWithText[33:-3]
print cars4ID

deleteXpath1 = "'attemptEventDeletion('" + cars4ID + "');'"
deleteXpath2 = '//*[@onclick=' + deleteXpath1 + ']'


# "//*[@onclick="'attemptEventDeletion('CARS4-1394');'"]"

# attemptEventDeletion('CARS4-1394.1');

#xpathRite = "''//*[contains(text(), '" + cars4ID + "'')]'"

idList = driver.find_elements_by_xpath("//*[contains(text(), '{0}')]".format(cars4ID))

deleteList = driver.find_elements_by_xpath("//*[@title='Delete this event']")

num = 0
for item in idList:
    print item.text
    #print item.get_attribute('title')
    print num
    num += 1

for item in deleteList:
    if cars4ID in item.get_attribute('onclick'):
        print item.get_attribute('title')
        print item.get_attribute('onclick')
        item.click()
        time.sleep(2)
        driver.switch_to_alert().accept()

#driver.find_element_by_xpath("//*[@onclick='attemptEventDeletion('CARS4-1394.1');']").click()
eventInEventsList.click()

time.sleep(3)

testElem = driver.find_element_by_xpath("//*[contains(text(), 'LA 1 at Texas State Line (2 miles north of the Rodessa area). Traffic is heavy. Look out for an abandoned vehicle.')]")

#print testElem.get_attribute('OuterHTML')

driver.close()