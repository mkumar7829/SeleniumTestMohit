import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))
driver.find_element(By.XPATH,"//input[@name='fldLoginUserId']").send_keys("Jack123")
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"CONTINUE").click
time.sleep(3)
#driver.switch_to.default_content()

#enter userid as jack123