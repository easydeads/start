import urllib.request

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = False
#opts.set_headless()
#assert opts.headless

linux_driver_path = ""
win_driver_path = "geckodriver-v0.24.0-win64/geckodriver.exe"

driver = webdriver.Firefox(executable_path=win_driver_path)

def go_to(addr, title="Not have"):
    driver.get(addr)
    print("url: " + str(addr) + " title: " + str(driver.title))
    if title == "Not have":
        print("Title not have")
    elif title != "Not have":
        list_title = title.split()
        print(list_title[0])
        assert list_title[0] in driver.title
    else:
        assert title.split() in driver.title

def find_copy(where_is):
    elem = driver.find_element_by_xpath(where_is)
    elem_data = elem.text
    #add to verification by RegExp
    print("Finded email now: " + str(elem_data))
    return elem_data

def get_image(from_url, title, pict_xpath, file_name):
    go_to(from_url, title)
    # get image source
    img = driver.find_element_by_xpath(pict_xpath)
    src = img.get_attribute('src')
    if type(src) != 'str':
        src = img.get_attribute('url')
        print("url: " + str(src))
    else:
        print("src: " + str(src))

    # download the image
    #urllib.urlretrieve(src, title)

    # take screenshot
    driver.save_screenshot(img.get_attribute('src').split("/")[-1], )
    print("Saved screen: " + str(img.get_attribute('src').split("/")[-1]))

    return src


"""
написать функцию для открытия новой вкладки с 'ёпмейл'
написать письмо с полоченным ссылками и отправить на адрес в гетнада

обновить страницу гетнада (при необходимости) и проверить что ссылки соответствубт отправленным

кликом в ссылки открыть пикчи и сделать скрины открытых страниц/вкладок
"""

#------ VARIABLES start---------
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
cat_title = "random.cat"
cat_xpath = "//img[@id='cat']"

    #dog resources
dog_url = "https://random.dog/"
dog_title = "random.dog"
dog_xpath = "//img[@id='dog-img']"

    #fox resources
fox_url = "https://randomfox.ca/"
fox_title = "RandomFox"
fox_xpath = "//img[@id='fox_img_link']"

cat = get_image(cat_url, cat_title, cat_xpath, "cat_pict")
dog = get_image(dog_url, dog_title, dog_xpath, "dog_pict")
fox = get_image(fox_url, fox_title, fox_xpath, "fox_pict")
#------ VARIABLES finish---------

#run start here
#get cat image, linck for sending
try:
    print(cat, dog, fox)

    #get email for sending and ferification
    go_to(url_nada, title_nada)
    find_copy(element)

    driver.close()
except:
    driver.close()