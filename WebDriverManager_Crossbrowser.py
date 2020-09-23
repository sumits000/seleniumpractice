from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "firefox"

if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())

if browserName == 'firefox':
    driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())

else:
    print("please pass the correct browser name: " + browserName)
    raise Exception('Driver is not found')
driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, 'password').send_keys('Test@12345')
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)
driver.get_screenshot_as_file("test.png");
time.sleep(4)
driver.quit()