from selenium import webdriver 
from time import sleep 
from getpass import getpass
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

usr=input('Enter Email Id:') 
pwd=getpass('Enter Password:') 

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path="/home/fuzzy/Downloads/firefox/geckodriver")
driver.get('https://www.facebook.com/') 
sleep(3) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(5) 

password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
sleep(5) 
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

