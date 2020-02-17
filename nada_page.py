from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import urllib.request

linux_driver_path = ""
win_driver_path = "geckodriver-v0.24.0-win64/geckodriver.exe"

driver = webdriver.Firefox(executable_path=win_driver_path)

def go_to(addr, title):
    driver.get(addr)
    print("url: " + str(addr) + "\n" +
          str(driver.title))
    assert title in driver.title

def find_copy(where_is):
    elem = driver.find_element_by_xpath(where_is)
    elem_data = elem.text
    #add to verification by RegExp
    print("Finded email now: " + str(elem_data))
    return elem_data

def get_image(from_url, title, pict_xpath, file_name):
    go_to(from_url, title)
    img = driver.find_element_by_xpath(pict_xpath)
    src = img.get_attribute('src')
    urllib.urlretrieve(src, "name.extention")



"""
написать функцию для открытия новой вкладки с 'ёпмейл'
написать письмо с полоченным ссылками и отправить на адрес в гетнада

обновить страницу гетнада (при необходимости) и проверить что ссылки соответствубт отправленным

кликом в ссылки открыть пикци и сделать скрины открытых страниц/вкладок
"""
#get nada data
url_nada = "https://getnada.com"
title_nada = "Nada - temp mail - fast and free"
element = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/h1[1]/span[2]"
fox_image = ("https://randomfox.ca/images/")

#yopmail data
url_yop = "http://www.yopmail.com/en/"
title_start_yop = "YOPmail - Disposable Email Address"
title_start_yop_ru = "YOPmail - Одноразовые, Анонимные  и Бесплатные адреса электронной почты"

mail_field = "/html[1]/body[1]/center[1]/div[1]/div[1]/div[3]/table[3]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[2]"
mail_addr_yop = "send_image"
mail_get_button = "/html[1]/body[1]/center[1]/div[1]/div[1]/div[3]/table[3]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/input[1]"

#cat resources
cat_url = "https://random.cat/"
cat_title = "random.cat -- meeeeeeeeoooooooow"
cat_xpath = "//img[@id='cat']"

#dog resources
dog_url = "https://random.dog/"
dog_title = "random.dog"
dog_xpath = "//img[@id='dog-img']"


#fox resources
fox_url = "https://randomfox.ca/"
fox_title = "RandomFox"
fox_xpath = "//a[@id='fox_full_link']"


#run start here
#get cat image, linck for sending
go_to(cat_url, cat_title)

go_to(dog_url, dog_title)

go_to(fox_url, fox_title)

#get email for sending and ferification
go_to(url_nada, title_nada)
find_copy(element)

driver.close()