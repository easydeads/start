#------ VARIABLES start---------
#get nada data
url_nada = "https://getnada.com"
title_nada = "Nada - temp mail - fast and free"
element = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/h1[1]/span[2]"
fox_image = ("https://randomfox.ca/images/")

#cat resources
cat_url = "https://random.cat/"
cat_api = "http://aws.random.cat/meow"
cat_title = "random.cat"
cat_xpath = "//img[@id='cat']"

#dog resources
dog_url = "https://random.dog/"
dog_api = "https://random.dog/woof.json"
dog_title = "random.dog"
dog_xpath = ["//img[@id='dog-img']", '/html/body/div/div/div/video/source']

#fox resources
fox_url = "https://randomfox.ca/"
fox_api = "https://randomfox.ca/floof/"
fox_title = "RandomFox"
fox_xpath = "//img[@id='fox_img_link']"

#yopmail data
url_yop = "http://www.yopmail.com/en/"
title_start_yop = "YOPmail - Disposable Email Address"
# если есть несколько тайтлов можно попробовать массив, но допилив go_to() "YOPmail - Одноразовые, Анонимные  и Бесплатные адреса электронной почты"
mail_field = "login"
mail_addr_yop = "send_image"
mail_get_button = "//input[@class='sbut']"
new_mail = "//a[@id='wrmail']"
mailto = "//input[@id='mailto']"
mail_title = "//input[@id='mailsu']"

to = ""
sender = "mail address"
subject = "subject test1"
msgHtml = r'Hi<br/>Html <b>hello</b>'
msgPlain = "Hi\nPlain Email"
message_text = "this is message text"

all_data = [fox_api, dog_api, cat_api]
key_names = ["image", "url", "file"]
#------ VARIABLES finish---------