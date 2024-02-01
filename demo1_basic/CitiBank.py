import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.online.citibank.co.in/")
#wait= WebDriverWait(driver,10)
#wait.until(expected_conditions.alert_is_present())
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='newclose']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[@class='newclose2']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[@class='lockSign']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(text(),'Forgot User ID?')]").click()
driver.find_element(By.XPATH,"//a[@class='sbSelector']").click()

driver.find_element(By.XPATH,"//a[@rel='Credit Card']").click()
driver.find_element(By.XPATH,"//input[@id='citiCard1']").send_keys(5656)
driver.find_element(By.XPATH,"//input[@id='citiCard2']").send_keys(8887)
driver.find_element(By.XPATH,"//input[@id='citiCard3']").send_keys(9998)
driver.find_element(By.XPATH,"//input[@id='citiCard4']").send_keys(9998)
driver.find_element(By.XPATH,"//input[@id='cvvnumber']").send_keys(234)
driver.find_element(By.XPATH,"//input[@id='bill-date-long']").click()


selectYear = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
selectYear.select_by_visible_text("2022")
selectMonth = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
selectMonth.select_by_visible_text("Dec")

driver.find_element(By.XPATH,"//a[text()='25']").click()
driver.find_element(By.XPATH,"//input[@id='agree']").click()
driver.find_element(By.XPATH,"//input[@value='PROCEED']").click()
result = driver.find_element(By.XPATH,"//p[@class='err-cont']")
print(result.text)

time.sleep(10)

