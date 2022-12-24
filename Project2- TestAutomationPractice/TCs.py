import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

import Utils
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def chr_setup():
    serv_obj = Service("J:\SQA Concepts\Drivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.headless = True    # declare headless mode
    driver = webdriver.Chrome(service=serv_obj, options=options)
    driver.implicitly_wait(10)
    return driver


driver = chr_setup()

# Launch URL in browser
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

try:
    search_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
    search_box.clear()
    search_box.send_keys("python")

    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    totalEle = len(driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/child::div"))

    if totalEle == Utils.total_result:
        print("TestCase-1 Passed")
    else:
        print("TestCase-1 Failed")

    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']/child::div[2]").click()

    windowIDs = driver.window_handles

    for windowId in windowIDs:
        driver.switch_to.window(windowId)

    if driver.title == Utils.py_page_tite:
        print("TestCase-2 Passed")
        driver.close()
    else:
        print("TestCase-2 Failed")
        driver.close()

    driver.switch_to.window(windowIDs[0])

except:
    print("Doesn't perform test case -1 or 2")


try:
    driver.find_element(By.XPATH, "//button[normalize-space()='Click Me']").click()

    load_alt_win = driver.switch_to.alert   # capture the confirm alert window
    load_alt_win.accept()        # close alert window by clicking on OK button

    conformation = driver.find_element(By.ID, "demo").text
    if conformation == Utils.confirm:
        print("TestCase-3 passed")
    else:
        print("TestCase-3 Failed")

except:
    print("Doesn't perform test case -3")

try:
    driver.find_element(By.ID, "datepicker").click()    # click on date picker box

    while True:
        datePicker_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        datepicker_month =  driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        if datepicker_month == Utils.month and datePicker_year == Utils.year:
            break
        else:
            driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


    # Select Date
    datePicker_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
    for ele in datePicker_dates:
        if ele.text == Utils.date:
            ele.click()
            break

    m_d_y = driver.find_element(By.ID, "datepicker").get_attribute('value')

    if m_d_y == Utils.FDatePicker:
        print("TestCase-4 Passed")
    else:
        print("TestCase-4 Failed")

except:
    print("Doesn't perform test case 4")

try:
    # Select Menu
    speed = driver.find_element(By.ID, "speed")
    speedMenu = Select(speed)
    speedMenu.select_by_visible_text("Medium")

    if speed.get_attribute('value') == Utils.speedCapture:
        print("TestCase-5 passed")
    else:
        print("TestCase-5 Failed")

    file = driver.find_element(By.ID, "files")
    fileDD = Select(file)
    # fileDD.select_by_index(1)
    fileDD.select_by_visible_text("PDF file")

    # for f in file.text:
    #     if f == Utils.fileCapture:
    #         print("TestCase-6 passed")
    #         break
    if file.get_attribute('value') == Utils.fileCapture:
        print("TestCase-6 Passed")
    else:
        print("TestCase-6 Failed")

    animal = driver.find_element(By.ID, "animals")
    animalDD = Select(animal)
    animalDD.select_by_value("avatar")

    if animal.get_attribute('value') == Utils.captureAnimal:
        print("TestCase-7 Passed")
    else:
        print("TestCase-7 Failed")

except:
    print("Doesn't perform test case 5, 6 and 7")

try:
    total_labels = driver.find_elements(By.XPATH,"//div[@id='Text1']//div[@class='widget-content']/div/span")
    totalLabels = len(total_labels)
    if totalLabels == Utils.Labels:
        print("TestCase-8 Passed")
    else:
        print("TestCase-8 Failed", total_labels)

    if total_labels[1].text == Utils.secondLabel:
        print("TestCase-9 Passed")
    else:
        print("TestCase-9 Failed")

except:
    print("Doesn't perform test case 8 or 9")


try:
    act = ActionChains(driver)
    dbl_btn = driver.find_element(By.CSS_SELECTOR, "button[ondblclick='myFunction1()']")
    act.double_click(dbl_btn).perform()
    field1 = driver.find_element(By.ID, "field1").get_attribute('value')
    field2 = driver.find_element(By.ID, "field2").get_attribute('value')

    if field1 == field2:
        print("TestCase-10 Passed")
    else:
        print("TestCase-10 Failed")

except:
    print("Doesn't perform test case 10")


try:
    # Drag and Drop
    act = ActionChains(driver)
    source_ele = driver.find_element(By.ID, "draggable")
    destination_ele = driver.find_element(By.ID, "droppable")
    act.drag_and_drop(source_ele, destination_ele).perform()
    dropped = driver.find_element(By.XPATH, "//div[@id='droppable']/p").text

    if dropped == Utils.drp_text:
        print("TestCase-11 Passed")
    else:
        print("TestCase-11 Failed")


except:
    print("Doesn't perform test case 11")

driver.quit()
