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

def get_page(url, title):
  driver.get(url)
  assert title


def log_in(name, passkey):
  mail_form = driver.find_element_by_id('identity')
  mail_form.send_keys(name)
  passkey_form = driver.find_element_by_id('password')
  passkey_form.send_keys(passkey)

def searh_check(responce_text):
  search_field = driver.find_element_by_xpath("//div[@class='search-container']")
  search_field.click()
  search_field.send_keys(responce_text)


"""
driver.find_element_by_xpath('id("projectsDropzone10261")/a[@class="btn btn-green create"]')
driver.get('https://frondage.com/logout')
driver.close()
driver.quit()
"""

frondage = 'https://frondage.com/login'
frondage_title = "Frondage  - Sign In"
frondage_name = 'alpha_draw@yopmail.com'
frondage_passkey = '!Test123'

getnada = "https://getnada.com"
getnada_title = ""



get_page(frondage, frondage_title)
log_in(frondage_name, frondage_passkey)
