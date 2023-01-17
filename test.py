# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:25:35 2023

@author: P102MNPH1
"""
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote("http://172.17.0.2:4444/wd/hub", DesiredCapabilities.CHROME)

#options = selenium.webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#driver = selenium.webdriver.Chrome(chrome_options=options)

driver.get("http://omegle.com")