import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.ID, "realbox").send_keys("Mohit")
time.sleep(5)
driver.quit()