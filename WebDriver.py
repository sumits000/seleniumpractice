from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path= "/home/appventurez/Documents/Selenium_jar/chromedriver_linux64/chromedriver")
driver.implicitly_wait(5)
driver.get("https://google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
time.sleep(3)
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/div[1]').click()
optionlist = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print(len(optionlist))
for ele in optionlist:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break
time.sleep(5)
driver.quit()