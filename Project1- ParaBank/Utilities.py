exp_reg_title = "ParaBank | Register for Free Online Account Access"

success_status = "Pass"
failure_status = "Failed"

first_name_xpath = "//span[@id='customer.firstName.errors']"
last_name_xpath = "//span[@id='customer.lastName.errors']"
addr_xpath = "//span[@id='customer.address.street.errors']"
city_xpath = "//span[@id='customer.address.city.errors']"
state_xpath = "//span[@id='customer.address.state.errors']"
zipCode_xpath = "//span[@id='customer.address.zipCode.errors']"
ssn_xpath = "//span[@id='customer.ssn.errors']"
userName_xpath = "//span[@id='customer.username.errors']"
pass_xpath = "//span[@id='customer.password.errors']"
confirmPass_xpath = "//span[@id='repeatedPassword.errors']"

firstName_RMS = "First name is required."
lastName_RMS = "Last name is required."
addr_RMS = "Address is required."
city_RMS = "City is required."
state_RMS = "State is required."
zipCode_RMS = "Zip Code is required."
ssn_RMS = "Social Security Number is required."
userName_RMS = "Username is required."
pass_RMS = "Password is required."
confirmPass_RMS = "Password confirmation is required."
confMatchingPass_RMS = "Passwords did not match."

# input fields
first_name = "//input[@id='customer.firstName']"
last_name = "//input[@id='customer.lastName']"
addr = "//input[@id='customer.address.street']"
city = "//input[@id='customer.address.city']"
state = "//input[@id='customer.address.state']"
zip = "//input[@id='customer.address.zipCode']"
phn = "//input[@id='customer.phoneNumber']"
ssn = "//input[@id='customer.ssn']"
userName = "//input[@id='customer.username']"
password = "//input[@id='customer.password']"
confimPass = "//input[@id='repeatedPassword']"

#after registration

userName_aft_Xpath = "//div[@id='rightPanel']/h1"
logout = "//a[normalize-space()='Log Out']"





























# # capture xpath's of required fields
# firstNameField = driver.find_element(By.XPATH,Utilities.first_name)
# lastNameField = driver.find_element(By.XPATH, Utilities.last_name)
# addressField = driver.find_element(By.XPATH,Utilities.addr)
# cityField = driver.find_element(By.XPATH,Utilities.city)
# stateField = driver.find_element(By.XPATH,Utilities.state)
# zipField = driver.find_element(By.XPATH,Utilities.zip)
# phoneNoField = driver.find_element(By.XPATH,Utilities.phn)
# ssnField = driver.find_element(By.XPATH,Utilities.ssn)
# userNameField = driver.find_element(By.XPATH,Utilities.userName)
# passwordField = driver.find_element(By.XPATH,Utilities.password)
# confirmPassField = driver.find_element(By.XPATH,Utilities.confimPass)

# lastNameField.send_keys("Sarker")
# addressField.send_keys("Mirpur-12")
# cityField.send_keys("Dhaka")
# stateField.send_keys("Dhaka")
# zipField.send_keys("1300")
# phoneNoField.send_keys("0125678910")
# ssnField.send_keys("1234")
# userNameField.send_keys("Test")
# passwordField.send_keys("Testtest12@#")
# confirmPassField.send_keys("Testtest12@#")

# reg_button = driver.find_element(By.XPATH, "//input[@value='Register']")
# reg_button.click()  # Click on register


# # capture xpath's of required message's
# firstName = driver.find_element(By.XPATH, Utilities.first_name_xpath)
# lastName = driver.find_element(By.XPATH, Utilities.last_name_xpath)
# address = driver.find_element(By.XPATH, Utilities.addr_xpath)
# city = driver.find_element(By.XPATH, Utilities.city_xpath)
# state = driver.find_element(By.XPATH, Utilities.state_xpath)
# zipCode = driver.find_element(By.XPATH, Utilities.zipCode_xpath)
# ssn = driver.find_element(By.XPATH, Utilities.ssn_xpath)
# userName = driver.find_element(By.XPATH, Utilities.userName_xpath)
# password = driver.find_element(By.XPATH, Utilities.pass_xpath)
# confirmPass = driver.find_element(By.XPATH, Utilities.confirmPass_xpath)
#
# # capture required message's
# firstName_req_text = firstName.text
# lastName_req_text = lastName.text
# addr_req_text= address.text
# city_req_text= city.text
# state_req_text= state.text
# zip_req_text = zipCode.text
# ssn_req_text= ssn.text
# userName_req_text = userName.text
# pass_req_text = password.text
# confirm_req_text = confirmPass.text


