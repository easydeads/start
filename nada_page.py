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
    elif title != "Not have" and type(title) != 'list':
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
    try:
        img = driver.find_element_by_xpath(pict_xpath)
        src = img.get_attribute('src')
        if type(src) != 'str':
            src = img.get_attribute('url')
            print("url: " + str(src))
        else:
            print("src: " + str(src))
        driver.save_screenshot(img.get_attribute('src').split("/")[-1], )
        print("Saved screen: " + str(img.get_attribute('src').split("/")[-1]))

        return src
    except:
        driver.refresh()


    # download the image
    #urllib.urlretrieve(src, title)

    # take screenshot


def open_mailbox(url, title, login, input_text, button):
    go_to(url, title)
    mail_form = driver.find_element_by_id(login).send_keys(input_text)
    print("Text: " + input_text)
    next_button = driver.find_element_by_xpath(button).click()
    print("Button pressed")

def write_mail():
    write = driver.find_element_by_xpath("//a[@id='wrmail']").click()
    to = driver.find_element_by_xpath("//input[@id='mailto']").click()




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

    #cat resources
cat_url = "https://random.cat/"
cat_title = "random.cat"
cat_xpath = "//img[@id='cat']"

    #dog resources
dog_url = "https://random.dog/"
dog_title = "random.dog"
dog_xpath = ["//img[@id='dog-img']", "//video[@id='dog-img']//source"]

    #fox resources
fox_url = "https://randomfox.ca/"
fox_title = "RandomFox"
fox_xpath = "//img[@id='fox_img_link']"

    #yopmail data
url_yop = "http://www.yopmail.com/en/"
title_start_yop = "YOPmail - Disposable Email Address"
# если есть несколько тайтлов можно попробовать массив, но допилив go_to() "YOPmail - Одноразовые, Анонимные  и Бесплатные адреса электронной почты"
mail_field = "login"
mail_addr_yop = "send_image"
mail_get_button = "//input[@class='sbut']"
"""
cat = get_image(cat_url, cat_title, cat_xpath, "cat_pict")
dog = get_image(dog_url, dog_title, dog_xpath, "dog_pict")
fox = get_image(fox_url, fox_title, fox_xpath, "fox_pict")
"""
#------ VARIABLES finish---------

#run start here
#get cat image, linck for sending
try:
    open_mailbox(url_yop, title_start_yop, mail_field, mail_addr_yop, mail_get_button)

    """
    print(cat, dog, fox)
    go_to(url_yop, title_start_yop)

    #get email for sending and ferification
    go_to(url_nada, title_nada)
    find_copy(element)
    """

    #driver.close()
except:
    print("Complete")
    #driver.close()