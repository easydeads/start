from selenium import webdriver
from test_cases.variables import *

driver = webdriver.Firefox(executable_path="D:\Frondage\start\geckodriver-v0.24.0-win64\geckodriver.exe")

driver.get(login_page)
print(str(driver.title))
assert login_title in driver.title

driver.find_element_by_xpath(login_email).send_keys("alpha_draw@yopmail.com")
driver.find_element_by_xpath(login_password).send_keys("!Test123")
driver.find_element_by_xpath(login_button).click()
print(str(driver.title))
assert my_workspace_title in driver.title

driver.find_element_by_xpath(my_workspace_menu).click()
driver.find_element_by_xpath(sign_out)
print(str(driver.title))
assert login_title in driver.title
