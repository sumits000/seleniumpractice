from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.find_element(By.NAME, "upfile").send_keys('/home/appventurez/Desktop/cat.jpeg')
driver.find_element(By.XPATH, "//input[@type='submit']").click()