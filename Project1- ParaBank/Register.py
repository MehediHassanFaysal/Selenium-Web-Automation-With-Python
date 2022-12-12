import time
import Utilities

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service("C:\Drivers\chromedriver_win32_2\chromedriver.exe")    # setup chrome webdriver
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()   # maximize the window size
driver.implicitly_wait(10)  # set 10 sec for implicit wait

driver.get("https://parabank.parasoft.com/")

reg_link = driver.find_element(By.LINK_TEXT, "Register")
reg_link.click()

reg_title = driver.title
expected_title = Utilities.exp_reg_title

if(reg_title == expected_title):
    print("--------------- We are now in Registration page --------------- ")

    try:
        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register

        # capture xpath's of required message's
        firstName = driver.find_element(By.XPATH, Utilities.first_name_xpath)
        lastName = driver.find_element(By.XPATH, Utilities.last_name_xpath)
        address = driver.find_element(By.XPATH, Utilities.addr_xpath)
        city = driver.find_element(By.XPATH, Utilities.city_xpath)
        state = driver.find_element(By.XPATH, Utilities.state_xpath)
        zipCode = driver.find_element(By.XPATH, Utilities.zipCode_xpath)
        ssn = driver.find_element(By.XPATH, Utilities.ssn_xpath)
        userName = driver.find_element(By.XPATH, Utilities.userName_xpath)
        password = driver.find_element(By.XPATH, Utilities.pass_xpath)
        confirmPass = driver.find_element(By.XPATH, Utilities.confirmPass_xpath)

        # capture required message's
        firstName_req_text = firstName.text
        lastName_req_text = lastName.text
        addr_req_text = address.text
        city_req_text = city.text
        state_req_text = state.text
        zip_req_text = zipCode.text
        ssn_req_text = ssn.text
        userName_req_text = userName.text
        pass_req_text = password.text
        confirm_req_text = confirmPass.text


        if(firstName_req_text == Utilities.firstName_RMS and lastName_req_text == Utilities.lastName_RMS and addr_req_text == Utilities.addr_RMS and city_req_text == Utilities.city_RMS and state_req_text == Utilities.state_RMS and zip_req_text == Utilities.zipCode_RMS and ssn_req_text == Utilities.ssn_RMS and userName_req_text == Utilities.userName_RMS and pass_req_text == Utilities.pass_RMS and confirm_req_text == Utilities.confirmPass_RMS):
            print("Test Case-1:", Utilities.success_status)
    except:
        print("Test Case-1:", Utilities.failure_status)

    try:
        time.sleep(3)

        lastNameField = driver.find_element(By.XPATH, Utilities.last_name).send_keys("Sarker")
        addressField = driver.find_element(By.XPATH,Utilities.addr).send_keys("Mirpur-12")
        cityField = driver.find_element(By.XPATH,Utilities.city).send_keys("Dhaka")
        stateField = driver.find_element(By.XPATH,Utilities.state).send_keys("Dhaka")
        zipField = driver.find_element(By.XPATH,Utilities.zip).send_keys("1300")
        phoneNoField = driver.find_element(By.XPATH,Utilities.phn).send_keys("0125678910")
        ssnField = driver.find_element(By.XPATH,Utilities.ssn).send_keys("1234")
        userNameField = driver.find_element(By.XPATH,Utilities.userName).send_keys("Test")
        passwordField = driver.find_element(By.XPATH,Utilities.password).send_keys("Testtest12@#")
        confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass).send_keys("Testtest12@#")


        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register

        firstName_req_text = driver.find_element(By.XPATH, Utilities.first_name_xpath).text

        if(firstName_req_text == Utilities.firstName_RMS):
            print("Test Case-2:", Utilities.success_status)
    except:
        print("Test Case-2:", Utilities.failure_status)


    try:
        time.sleep(3)
        firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
        lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
        addressField = driver.find_element(By.XPATH,Utilities.addr)
        cityField = driver.find_element(By.XPATH,Utilities.city)
        stateField = driver.find_element(By.XPATH,Utilities.state)
        zipField = driver.find_element(By.XPATH,Utilities.zip)
        phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
        ssnField = driver.find_element(By.XPATH,Utilities.ssn)
        userNameField = driver.find_element(By.XPATH,Utilities.userName)
        passwordField = driver.find_element(By.XPATH,Utilities.password)
        confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)

        firstNameField.clear()
        firstNameField.send_keys("Test")
        lastNameField.clear()
        addressField.clear()
        addressField.send_keys("Mirpur-12")
        cityField.clear()
        cityField.send_keys("Dhaka")
        stateField.clear()
        stateField.send_keys("Dhaka")
        zipField.clear()
        zipField.send_keys("1300")
        phoneNoField.clear()
        phoneNoField.send_keys("0125678910")
        ssnField.clear()
        ssnField.send_keys("1234")
        userNameField.clear()
        userNameField.send_keys("Test")
        passwordField.clear()
        passwordField.send_keys("Testtest12@#")
        confirmPassField.clear()
        confirmPassField.send_keys("Testtest12@#")



        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register

        lastName_req_text = driver.find_element(By.XPATH, Utilities.last_name_xpath).text

        if(lastName_req_text == Utilities.lastName_RMS):
            print("Test Case-3:", Utilities.success_status)
    except:
        print("Test Case-3:", Utilities.failure_status)


    try:
        time.sleep(3)
        firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
        lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
        addressField = driver.find_element(By.XPATH,Utilities.addr)
        cityField = driver.find_element(By.XPATH,Utilities.city)
        stateField = driver.find_element(By.XPATH,Utilities.state)
        zipField = driver.find_element(By.XPATH,Utilities.zip)
        phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
        ssnField = driver.find_element(By.XPATH,Utilities.ssn)
        userNameField = driver.find_element(By.XPATH,Utilities.userName)
        passwordField = driver.find_element(By.XPATH,Utilities.password)
        confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)

        firstNameField.clear()
        firstNameField.send_keys(0000)
        lastNameField.clear()
        lastNameField.send_keys(1111)
        addressField.clear()
        addressField.send_keys("Mirpur-12")
        cityField.clear()
        cityField.send_keys("Dhaka")
        stateField.clear()
        stateField.send_keys("Dhaka")
        zipField.clear()
        zipField.send_keys("1300")
        phoneNoField.clear()
        phoneNoField.send_keys("0125678910")
        ssnField.clear()
        ssnField.send_keys("1234")
        userNameField.clear()
        userNameField.send_keys("Test12")
        passwordField.clear()
        passwordField.send_keys("Testtest12@#")
        confirmPassField.clear()
        confirmPassField.send_keys("Testtest12@#")



        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register


        firstName_req_text = driver.find_element(By.XPATH, Utilities.first_name_xpath).text
        lastName_req_text = driver.find_element(By.XPATH, Utilities.last_name_xpath).text

        if(firstName_req_text == Utilities.firstName_RMS and lastName_req_text == Utilities.lastName_RMS):
            print("Test Case-4:", Utilities.success_status)
    except:
        print("Test Case-4:", Utilities.failure_status)


    try:
        time.sleep(3)
        firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
        lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
        addressField = driver.find_element(By.XPATH,Utilities.addr)
        cityField = driver.find_element(By.XPATH,Utilities.city)
        stateField = driver.find_element(By.XPATH,Utilities.state)
        zipField = driver.find_element(By.XPATH,Utilities.zip)
        phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
        ssnField = driver.find_element(By.XPATH,Utilities.ssn)
        userNameField = driver.find_element(By.XPATH,Utilities.userName)
        passwordField = driver.find_element(By.XPATH,Utilities.password)
        confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)

        firstNameField.clear()
        firstNameField.send_keys("Test")
        lastNameField.clear()
        lastNameField.send_keys("test")
        addressField.clear()
        addressField.send_keys("Mirpur-12")
        cityField.clear()
        cityField.send_keys("Dhaka")
        stateField.clear()
        stateField.send_keys("Dhaka")
        zipField.clear()
        zipField.send_keys("1300")
        phoneNoField.clear()
        # phoneNoField.send_keys("abc0125678")
        ssnField.clear()
        ssnField.send_keys("abc123")
        userNameField.clear()
        userNameField.send_keys("Test124")
        passwordField.clear()
        passwordField.send_keys("Testtest12@#")
        confirmPassField.clear()
        confirmPassField.send_keys("Testtest12@#")



        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register


        ssn_req_text = driver.find_element(By.XPATH, Utilities.first_name_xpath).text

        if(ssn_req_text == Utilities.ssn_RMS):
            print("Test Case-5:", Utilities.success_status)
        else:
            print("Test Case-5:", Utilities.failure_status)

    except:
        print("Failed to perform test case 5")


    try:
        time.sleep(3)
        firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
        lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
        addressField = driver.find_element(By.XPATH,Utilities.addr)
        cityField = driver.find_element(By.XPATH,Utilities.city)
        stateField = driver.find_element(By.XPATH,Utilities.state)
        zipField = driver.find_element(By.XPATH,Utilities.zip)
        phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
        ssnField = driver.find_element(By.XPATH,Utilities.ssn)
        userNameField = driver.find_element(By.XPATH,Utilities.userName)
        passwordField = driver.find_element(By.XPATH,Utilities.password)
        confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)

        firstNameField.clear()
        firstNameField.send_keys("Test")
        lastNameField.clear()
        lastNameField.send_keys("test")
        addressField.clear()
        addressField.send_keys("Mirpur-12")
        cityField.clear()
        cityField.send_keys("Dhaka")
        stateField.clear()
        stateField.send_keys("Dhaka")
        zipField.clear()
        zipField.send_keys("1300")
        phoneNoField.clear()
        phoneNoField.send_keys("abc0125678")
        ssnField.clear()
        ssnField.send_keys("123")
        userNameField.clear()
        userNameField.send_keys("Test127")
        passwordField.clear()
        passwordField.send_keys("Testtest12@#")
        confirmPassField.clear()
        confirmPassField.send_keys("Testtest12@#")



        reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
        reg_button.click()  # Click on register

        time.sleep(3)

        if(driver.title == "ParaBank | Register for Free Online Account Access"):
            print("Test Case-6:", Utilities.success_status)
        else:
            print("Test Case-6: ", Utilities.failure_status)
    except:
        print("Failed to perform test case 6")


    try:
         time.sleep(3)
         firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
         lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
         addressField = driver.find_element(By.XPATH,Utilities.addr)
         cityField = driver.find_element(By.XPATH,Utilities.city)
         stateField = driver.find_element(By.XPATH,Utilities.state)
         zipField = driver.find_element(By.XPATH,Utilities.zip)
         phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
         ssnField = driver.find_element(By.XPATH,Utilities.ssn)
         userNameField = driver.find_element(By.XPATH,Utilities.userName)
         passwordField = driver.find_element(By.XPATH,Utilities.password)
         confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)
         firstNameField.clear()
         firstNameField.send_keys("Test")
         lastNameField.clear()
         lastNameField.send_keys("test")
         addressField.clear()
         addressField.send_keys("Mirpur-12")
         cityField.clear()
         cityField.send_keys("Dhaka")
         stateField.clear()
         stateField.send_keys("Dhaka")
         zipField.clear()
         zipField.send_keys("1300")
         phoneNoField.clear()
         phoneNoField.send_keys("0125678910")
         ssnField.clear()
         ssnField.send_keys("123")
         userNameField.clear()
         userNameField.send_keys("Test128")
         passwordField.clear()
         passwordField.send_keys(0)
         confirmPassField.clear()
         confirmPassField.send_keys(0)

         reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
         reg_button.click()  # Click on register
         # time.sleep(3)

         if(driver.title == "ParaBank | Register for Free Online Account Access"):
              print("Test Case-7:", Utilities.success_status)
         else:
              print("Test Case-7: ", Utilities.failure_status)
    except:
         print("Failed to perform test case 7")

    try:
         time.sleep(3)
         firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
         lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
         addressField = driver.find_element(By.XPATH,Utilities.addr)
         cityField = driver.find_element(By.XPATH,Utilities.city)
         stateField = driver.find_element(By.XPATH,Utilities.state)
         zipField = driver.find_element(By.XPATH,Utilities.zip)
         phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
         ssnField = driver.find_element(By.XPATH,Utilities.ssn)
         userNameField = driver.find_element(By.XPATH,Utilities.userName)
         passwordField = driver.find_element(By.XPATH,Utilities.password)
         confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)
         firstNameField.clear()
         firstNameField.send_keys("Test")
         lastNameField.clear()
         lastNameField.send_keys("test")
         addressField.clear()
         addressField.send_keys("Mirpur-12")
         cityField.clear()
         cityField.send_keys("Dhaka")
         stateField.clear()
         stateField.send_keys("Dhaka")
         zipField.clear()
         zipField.send_keys("1300")
         phoneNoField.clear()
         phoneNoField.send_keys("0125678910")
         ssnField.clear()
         ssnField.send_keys("123")
         userNameField.clear()
         userNameField.send_keys("Test128")
         passwordField.clear()
         passwordField.send_keys("Testtest123###")
         confirmPassField.clear()
         confirmPassField.send_keys("Testtest123")

         reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
         reg_button.click()  # Click on register
         # time.sleep(3)

         confirm_req_text = driver.find_element(By.XPATH, Utilities.confirmPass_xpath).text

         if(confirm_req_text == Utilities.confMatchingPass_RMS):
              print("Test Case-8:", Utilities.success_status)
         else:
              print("Test Case-8: ", Utilities.failure_status)
    except:
         print("Failed to perform test case 8")

    try:
         time.sleep(3)

         sen = driver.find_element(By.XPATH, "//h1[normalize-space()='Signing up is easy!']")
         sentence = sen.text

         if(sen.is_displayed() and sentence  == "Signing up is easy!"):
              print("Test Case-9:", Utilities.success_status)
         else:
              print("Test Case-9: ", Utilities.failure_status)
    except:
         print("Failed to perform test case 9")

    try:
         time.sleep(3)
         firstNameField = driver.find_element(By.XPATH, Utilities.first_name)
         lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
         addressField = driver.find_element(By.XPATH,Utilities.addr)
         cityField = driver.find_element(By.XPATH,Utilities.city)
         stateField = driver.find_element(By.XPATH,Utilities.state)
         zipField = driver.find_element(By.XPATH,Utilities.zip)
         phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
         ssnField = driver.find_element(By.XPATH,Utilities.ssn)
         userNameField = driver.find_element(By.XPATH,Utilities.userName)
         passwordField = driver.find_element(By.XPATH,Utilities.password)
         confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)
         firstNameField.clear()
         firstNameField.send_keys("Test")
         lastNameField.clear()
         lastNameField.send_keys("test")
         addressField.clear()
         addressField.send_keys("Mirpur-12")
         cityField.clear()
         cityField.send_keys("Dhaka")
         stateField.clear()
         stateField.send_keys("Dhaka")
         zipField.clear()
         zipField.send_keys("1300")
         phoneNoField.clear()
         phoneNoField.send_keys("0125678910")
         ssnField.clear()
         ssnField.send_keys("123")
         userNameField.clear()
         userNameField.send_keys("Test135")
         passwordField.clear()
         passwordField.send_keys("Testtest123###")
         confirmPassField.clear()
         confirmPassField.send_keys("Testtest123###")

         enterUserName = userNameField.get_attribute("value")

         reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
         reg_button.click()  # Click on register

         userNameText = driver.find_element(By.XPATH, Utilities.userName_aft_Xpath).text
         headerline = "Welcome "+enterUserName

         if(userNameText == headerline and driver.title=="ParaBank | Customer Created"):
              print("Test Case-10:", Utilities.success_status)
              driver.find_element(By.XPATH, Utilities.logout).click()

         else:
              print("Test Case-10: ", Utilities.failure_status)
    except:
         print("Failed to perform test case 10")


else:
    print("Didn't redirect to registration page")
driver.quit()





