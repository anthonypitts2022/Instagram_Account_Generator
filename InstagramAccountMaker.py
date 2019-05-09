# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:57:03 2019

@author: Anthony Pitts

This uses selenium to automate the account creation process on instagram

"""


import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
import random
import string



def __main__():
    #tells the browser to wait up to 10 sec for an element to appear b/4 throwing a NotFoundException
    browser.implicitly_wait(10)
    
    browser.get("https://10minutemail.com/10MinuteMail/index.html")
    copy_email_action = ActionChains(browser)
    copy_email_action.key_down(Keys.CONTROL).key_down('c').key_up('c').key_up(Keys.CONTROL)
    copy_email_action.perform()
    
    browser.get("https://www.instagram.com/")
    action = ActionChains(browser) 
    for _ in range(2):
        action = action.send_keys(Keys.TAB)
    #paste email
    action= action.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).key_up('v')

    #inputs name
    action = action.send_keys(Keys.TAB)
    action=action.send_keys(get_name())
 
    #inputs username
    username = generate_random_user_pass()[0]
    action = action.send_keys(Keys.TAB)
    action = action.send_keys(username)
    action = action.pause(1)
    
    #inputs password
    password = generate_random_user_pass()[1]
    action = action.send_keys(Keys.TAB)
    action = action.send_keys(Keys.TAB)
    action = action.send_keys(password)
    
    action = action.send_keys(Keys.ENTER)
    action.perform()

    print("Your secure username is: " + username)
    print("Your secure password is: " + password)
    
    #clicks off of the "Do you want notifications on" button
    browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
    

def get_name():
    name=""
    for i in range(8):
        name =  name + random.choice(string.ascii_lowercase)
    return name




def generate_random_user_pass():
    
    username=""
    #capital letter
    username = username + random.choice(string.ascii_uppercase)
    #number
    username = username + random.choice(string.digits)
    #loop for rest of characters
    for i in range(9):
        username = username + random.choice(string.ascii_lowercase)
    #shuffles username
    password = ''.join(random.sample(username,len(username)))

    password=""
    #capital letter
    password = password + random.choice(string.ascii_uppercase)
    #number
    password = password + random.choice(string.digits)
    #special character
    password = password + random.choice("!@#$%*")
    #loop for rest of characters
    for i in range(8):
        password = password + random.choice(string.ascii_lowercase)
    #shuffles password
    password = ''.join(random.sample(password,len(password)))
    
    return [username,password]



browser = webdriver.Chrome("C:\\Users\\Downloads\\chromedriver_win32\\chromedriver.exe")
__main__()
