import time

import Utils

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
serv_obj = Service("C:\Drivers\chromedriver_win32_2\chromedriver.exe")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv_obj)

driver.implicitly_wait(10)

driver.get("https://parabank.parasoft.com/parabank/index.htm")   # Launch URL
driver.maximize_window()   # maximize the window

# click on service menu item
services = driver.find_element(By.XPATH, "//ul[@class='leftmenu']//li[3]/a")
services.click()

try:
    noOfRows = len(driver.find_elements(By.XPATH, "//body[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr"))
    noOfColumns = len(driver.find_elements(By.XPATH, "//body[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td"))
    #print("Number of rows:", noOfRows, "\n","Number of columns", noOfColumns)
    if noOfRows == Utils.totalRows and noOfColumns == Utils.totalColumns and driver.title == Utils.pageTitle:
        print("TestCase -1: Passed")
    else:
        print("TestCase -1: Failed")
except:
    print("Doesn't perform TestCase 1")

# Indentify the position of the sentence (WS-Security Signature)

try:
    noOfRows = len(driver.find_elements(By.XPATH, "//body[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr"))
    noOfColumns = len(driver.find_elements(By.XPATH, "//body[1]/div[1]/div[3]/div[2]/table[1]/tbody[1]/tr[1]/td"))

    if(driver.title == Utils.pageTitle):
        for r in range(1, noOfRows + 1):
            bookStoreWS = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[2]/span[3]").text
            reteatation = r
            if bookStoreWS == "WSDL :" and reteatation == Utils.rpdTime:
                print("TestCase -2: Passed")
        print("Total repeated time:", reteatation)
    else:
        print("Services page not found.")

except:
    print("Doesn't perform TestCase 2")


# Count number of rows are available in Bookstore services table
try:
    noOfRows = len(driver.find_elements(By.XPATH, "//table[2]/tbody/tr"))
    if(noOfRows == Utils.bsRows):
        print("TestCase -3: Passed")
    else:
        print("TestCase -3: Failed")
except:
    print("Doesn't perform TestCase-3")


# Identify the number of "int" parameter are available in Parameters column of Bookstore services table

try:
    noOfRows = len(driver.find_elements(By.XPATH, "//table[2]/tbody/tr"))
    for r in range(2, noOfRows + 1):
        captureInt = driver.find_element(By.XPATH, "//table[2]/tbody[1]/tr[" + str(r) + "]/td[2]").text
        if captureInt == "int" or captureInt == "int, int, int":
            for i in range(1, 6):
                if r == r:
                    num = 0
                    num =num+i
                    intFound = "int found"
        #
        # else:
        #     print("Doesn't found int parameter")
    #print(intFound, num)
    if(num == Utils.intfound):
        print("TestCase -4: Passed")
    else:
        print("TestCase -4: Failed")

except:
    print("Doesn't perform TestCase -4")


# Identify the position of "submitOrder" method in Bookstore services
try:
    noOfRows = len(driver.find_elements(By.XPATH, "//table[2]/tbody/tr"))
    col = 1
    for r in range(2, noOfRows+1):
        submit_Order = driver.find_element(By.XPATH, "//table[2]/tbody/tr["+str(r)+"]/td["+str(col)+"]").text
        if(submit_Order == Utils.subMethod):
            print("TestCase -5: Passed.", "Position", "(",r,",",col,")")
except:
    print("Doesn't perform TestCase -5")

driver.quit()

