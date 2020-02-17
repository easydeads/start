from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import urllib.request

driver = webdriver.Firefox(executable_path="/home/john/PycharmProjects/AbSoft/venv/lib/python3.6/site-packages/geckodriver")

def go_to(addr, title):
    driver.get(addr)
    assert title in driver.title

def find_copy(where_is):
    elem = driver.find_element_by_xpath(where_is)
    elem_data = elem.text
    #add to verification by RegExp
    print(str(elem_data))
    return elem_data

def get_image(from_url, file_path, file_name):
    full_path = file_path + file_name + ".jpg"
    urllib.request.urlretrieve(from_url, full_path)

    go_to(from_url+str(random.randint(1, 122))+".jpg")
    file_name = input("foximage")
    print()
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



#run start here
go_to(url_nada, title_nada)
find_copy(element)

driver.close()