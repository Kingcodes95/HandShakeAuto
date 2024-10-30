import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import Alert

# TODO: Fix the pop up alert, after user login

user_email = ""
user_password = ""
school_name = "University of North Texas"

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://app.joinhandshake.com/login"
driver.get(url)

try:
    school_drop_down = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "s2id_school-login-select"))
    )
except TimeoutException:
    print("Could not find drop down box, Try again.")
school_drop_down.click()

try:
    click_search = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-input"))
    )
except TimeoutException:
    print("Could not find the drop down search, Try again.")
click_search.send_keys(school_name)

try:
    find_school = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{school_name}')]"))
    )
except TimeoutException:
    print("Could not find school name, Try again.")
find_school.click()

try:
    click_sso = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'sso-button'))
    )
except TimeoutException:
    print("Could not find sso button")
click_sso.click()

try:
    click_user = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
except TimeoutException:
    print("Could not find username box, Try again.")
click_user.click()
click_user.send_keys(user_email)

try:
    click_password = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
except TimeoutException:
    print("Could not find password box, Try again.")
click_password.click()
click_password.send_keys(user_password)
time.sleep(2)
click_password.send_keys(Keys.RETURN)

# Need to find a way to exit out the initial pop up on login
'''
    alert = WebDriverWait(driver, 5).until(
        EC.alert_is_present()
    )
except TimeoutException:
    print("Alert not found, ERROR big gay no alerty")
    
alert.accept()
'''

time.sleep(5)
driver.quit()