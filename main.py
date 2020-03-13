from nada_page import *
from vars import *

# Variables

cat_pict = src_from_api(cat_api)
dog_pict = src_from_api(dog_api)
fox_pict = src_from_api(fox_api)

to_mail = find_copy(url_nada, title_nada, element)
msg = str(cat_pict) + "\n" + str(dog_pict) + "\n" + str(fox_pict)

# Variables


send_email("Take this pictures", msg, to_mail)

#get email for sending and ferification