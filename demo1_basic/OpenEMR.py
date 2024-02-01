import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://demo.openemr.io/b/openemr/")
driver.find_element(By.XPATH,"//input[@id='authUser']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@id='clearPass']").send_keys("pass")
selectLang = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
selectLang.select_by_visible_text("English (Indian)")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='login-button']").click()