import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.db4free.net/")
#driver.find_element(By.XPATH,"//b[normalize-space()='phpMyAdmin »']").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"input_username").send_keys("admin")
driver.find_element(By.ID,"input_password").send_keys("123")
driver.find_element(By.ID,"input_go").click()
print(driver.find_element(By.XPATH,"//div[@id='pma_errors']").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.title)