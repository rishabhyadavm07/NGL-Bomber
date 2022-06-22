#Importing Libraries
from time import sleep
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# PATH = "/home/user/PythonProjects/NGLAutomation/chromedriver"
nglLink = str(input("Enter the NGL Link: "))
msgSend = str(input("Enter the message you want to BOMB: "))
numberOfMsgs = int(input("Number of messages you want to send: "))

from selenium.webdriver import Chrome
driver = Chrome()
driver.get(nglLink)

i =0

try:
    while(i < 20):
        question = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME,"question"))
        )
        question.clear()
        question.send_keys(msgSend)
        sleep(4)
        submit = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME,"submit"))
        )
        submit.click()
        sleep(3)
        another = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME,"another"))
        )
        another.click()

        sleep(10)
        i = i + 1

except:
    print("Error encountered")