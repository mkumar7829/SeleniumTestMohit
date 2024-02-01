from collections.abc import Set
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.medibuddy.in/")
time.sleep(1)
driver.implicitly_wait(10)
#driver.find_element(By.XPATH,"//*[@class='popsubform']").click()

#driver.find_element(By.XPATH,"//a[@class='wzrkClose']").click()
#driver._switch_to.window(driver.find_element(By.ID,"wiz-iframe"))

driver.switch_to.frame("wiz-iframe")
driver.find_element(By.XPATH,"//a[@class='wzrkClose']").click()
time.sleep(1)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[@ng-if='!OneClickFlowLogin']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@ng-click='linkAccount()']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@ng-click='openLearnMoreSection()']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@ng-click='skipCorpUserPhone()']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@ng-click='openUsernameScreen()']").click()
driver.find_element(By.ID,"username").send_keys("john")
driver.find_element(By.XPATH,"//button[@ng-disabled='disableLoginButton']").click()
driver.find_element(By.ID,"password").send_keys("john123")

time.sleep(1)
driver.find_element(By.XPATH,"//img[@ng-if='!showPassword']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='btn btn-primary verifyBtn']").click()
time.sleep(1)
result = driver.find_element(By.XPATH,"//div[@ng-if='isPasswordWrong']")
print(result.text)
time.sleep(3)
driver.quit()