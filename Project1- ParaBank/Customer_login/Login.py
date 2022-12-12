import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

serv_obj = Service("C:\Drivers\chromedriver_win32_2\chromedriver.exe")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=options)

driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()
driver.implicitly_wait(10)

import XLUtils
file = "J:\SQA Concepts\Selenium with python\Projects\Para Bank\ParaBank-selenium automation with python.xlsx"
rows = XLUtils.getRowCount(file, "Login")

try:

    for row in range(2, rows + 1):
        # read data from Excel sheet
        user = XLUtils.readData(file, "Login", row, 1)  # row->2 and column->1
        pwd = XLUtils.readData(file, "Login", row, 2)  # row->2 and column->2
        exp_err = XLUtils.readData(file, "Login", row, 3)

        # passing data to the application
        userName = driver.find_element(By.XPATH, "//input[@name='username']")
        userName.clear()
        userName.send_keys(user)

        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.click()
        password.send_keys(pwd)

        driver.find_element(By.XPATH, "//input[@value='Log In']").click()  # click on login button

        actual_error = driver.find_element(By.XPATH, "//h1[normalize-space()='Accounts Overview']").text

        # validation
        if exp_err == actual_error:
            print("Test passed")
            XLUtils.writeData(file, "Login", row, 5, "Passed")
            XLUtils.fillGreenColor(file, "Login", row, 5)
        else:
            print("Test failed")
            XLUtils.writeData(file, "Login", row, 5, "Failed")
            XLUtils.fillRedColor(file, "Login", row, 5)

        driver.find_element(By.LINK_TEXT, "Log Out").click()
        time.sleep(3)
except:
    print("Something worng")




driver.quit()


