from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
#opts.set_headless()
assert opts.headless

# vithout UI
#driver = webdriver.Firefox(executable_path="D:\\Frondage\\start\\geckodriver-v0.24.0-win64\\geckodriver.exe", options=opts)
# with UI
driver = webdriver.Firefox(executable_path="D:\\Frondage\\start\\geckodriver-v0.24.0-win64\\geckodriver.exe")

driver.get('https://frondage.com/login')

search_form = driver.find_element_by_id('identity')
search_form.send_keys('alpha_draw@yopmail.com')
search_form = driver.find_element_by_id('password')
search_form.send_keys('!Test123')
search_form = driver.find_element_by_xpath("//input[@name='submit']")
search_form.click()

"""
driver.find_element_by_xpath('id("projectsDropzone10261")/a[@class="btn btn-green create"]')

driver.get('https://frondage.com/logout')
driver.close()
driver.quit()
"""