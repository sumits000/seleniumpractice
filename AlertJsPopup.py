from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)
alert = driver.switch_to.alert

print(alert.text)
alert.accept()  # Accept it or click on
# alert.dismiss() # cancel the popup
driver.switch_to.default_content()
time.sleep(3)
driver.quit()