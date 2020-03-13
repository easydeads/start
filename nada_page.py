import urllib, json, requests
from email.mime.multipart import MIMEMultipart
from vars import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
#opts.set_headless()
#assert opts.headless

linux_driver_path = ""
win_driver_path = "geckodriver-v0.24.0-win64/geckodriver.exe"

driver = webdriver.Firefox(executable_path=win_driver_path)

def go_to(addr, title="Not have"):
  driver.get(addr)
  #print("url: " + str(addr) + " title: " + str(driver.title))
  if title == "Not have":
    print("Title not have")
  elif title != "Not have" and type(title) != 'list':
    list_title = title.split()
    assert list_title[0] in driver.title
  else:
    assert title.split() in driver.title

def find_copy(where_url, title, what):
  """
  :param where_is:
  :return:
  """
  go_to(where_url, title)
  elem = driver.find_element_by_xpath(what)
  elem_data = elem.text
  #add to verification by RegExp
  print("Finded email now: " + str(elem_data))
  return elem_data

def get_image_src(from_url, title, x_path):
  """x_path take as input string or list max from two elements if x_path not static"""
  """
  :param from_url:
  :param title:
  :param pict_xpath:
  :return:
  """
  go_to(from_url, title)
  # get image source
  if type(x_path) == list:
    try:
      img = driver.find_element_by_xpath(x_path[0])
      src = str(img.get_attribute('src'))
    except:
      img = driver.find_element_by_xpath(x_path[1])
      src = str(img.get_attribute('src'))
  elif type(x_path) == str:
    img = driver.find_element_by_xpath(x_path)
    src = str(img.get_attribute('src'))
  else:
    print("Unknown type")

  """if type(src) != 'str':
      src = img.get_attribute('url')
      print("Picture url: " + str(src))
  else:
      print("Picture src: " + str(src))
  """
  print("src is: " + str(src))
  return src

def src_from_api(url):
  """
  :param url:
  :return: as example
{'image': 'http://randomfox.ca/images/32.jpg', 'link': 'http://randomfox.ca/?i=32'}
{'fileSizeBytes': 1199392, 'url': 'https://random.dog/cb06ca7a-b464-426f-ba51-e4014f537cb0.mp4'}
{'file': 'https://purr.objects-us-east-1.dream.io/i/4FXOM.jpg'}
  """
  responce = requests.get(url)
  data = responce.json()
  for i in data:
    for n in key_names:
      if n == i:
        print("Link:", data[i])
        return data[i]
      else:
        print("Not have")
"""
def save_screen():
  driver.save_screenshot(img.get_attribute('src').split("/")[-1], )
  print("Saved screen: " + str(img.get_attribute('src').split("/")[-1]))

"""
def open_mailbox(url, title, login, input_text, button):
  go_to(url, title)
  mail_form = driver.find_element_by_id(login).send_keys(input_text)
  print("Text: " + input_text)
  next_button = driver.find_element_by_xpath(button).click()
  print("Button pressed")

def write_mail():
  write = driver.find_element_by_xpath("//a[@id='wrmail']").click()
  to = driver.find_element_by_xpath("//input[@id='mailto']").click()

# google api
import base64
from email.mime.text import MIMEText

from apiclient import errors

def SendMessage(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def CreateMessage(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}

def create_message_without_attachment (sender, to, subject, msgHtml, msgPlain):
  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = to
  msg.attach(MIMEText(msgPlain, 'plain'))
  msg.attach(MIMEText(msgHtml, 'html'))

  raw = base64.urlsafe_b64encode(msg.as_bytes())
  raw = raw.decode()
  body = {'raw': raw}
  return body

def send_email(subject, msg, to):
  import smtplib
  import config
  try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    message = 'Subhect: {}\n\n{}'.format(subject, msg)
    server.sendmail(config.EMAIL_ADDRESS, to, message)
    server.quit()
    print("Success: Email sent!")
  except:
    print("Email failed to send")