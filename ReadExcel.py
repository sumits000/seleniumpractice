import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

Url = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_subdomain']")
First_Name = driver.find_element(By.ID, "Form_submitForm_FirstName")
Last_Name = driver.find_element(By.ID, "Form_submitForm_LastName")
Email = driver.find_element(By.ID, "Form_submitForm_Email")
Job_Title = driver.find_element(By.ID, "Form_submitForm_JobTitle")
Company = driver.find_element(By.ID, "Form_submitForm_CompanyName")
Phone_no = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_Contact']")
total_emp =  driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
Industry =  driver.find_element(By.ID, "Form_submitForm_Industry")
Country =  driver.find_element(By.ID, "Form_submitForm_Country")


workbook = xlrd.open_workbook("/home/appventurez/testdata.xlsx")
sheet = workbook.sheet_by_name("registration")

#get total no of rows:
rowcount = sheet.nrows
colcount = sheet.ncols
print("Total rows are:", rowcount)
print("Total cols are:", colcount)

for curr_row in range(1, rowcount):
    url = sheet.cell_value(curr_row, 0)
    firstname = sheet.cell_value(curr_row, 1)
    LastName = sheet.cell_value(curr_row, 2)
    Emailid = sheet.cell_value(curr_row, 3)
    JobTitle = sheet.cell_value(curr_row, 4)
    Companyname = sheet.cell_value(curr_row, 5)
    Phoneno = int(sheet.cell_value(curr_row, 6))
    totalemp = sheet.cell_value(curr_row, 7)
    Industryname = sheet.cell_value(curr_row, 8)
    Countryname = sheet.cell_value(curr_row, 9)
    print(url , " " , firstname, " ", LastName , " " , Emailid , " " , JobTitle , " " , Companyname , " " , Phoneno , " " , totalemp , " " , Industryname , " " , Companyname)


    Url.send_keys(url)
    First_Name.send_keys(firstname)
    Last_Name.send_keys(LastName)
    Email.send_keys(Emailid)
    Job_Title.send_keys(JobTitle)
    Company.send_keys(Companyname)
    Phone_no.send_keys(Phoneno)
    # total_emp.send_keys(totalemp)
    # Industry.send_keys(Industryname)
    # Country.send_keys(Countryname)

    time.sleep(4)