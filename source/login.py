from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('login', type=str)
parser.add_argument('password', type=str)
parser.add_argument('-t', type=int, help="Czas oczekiwania na zaladowanie strony", default=5)

args = parser.parse_args()
timeout = args.t

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
driver.get("https://portal.librus.pl/rodzina")

try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'dropdown-toggle'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Strona nie zdazyla sie zaladowac")

dropdown = driver.find_element_by_class_name('dropdown-toggle')
dropdown.click()

menu_button = driver.find_element_by_xpath('//a[@href="'+'/rodzina/synergia/loguj'+'"]')
menu_button.click()

assert "Zaloguj do Synergii" in driver.title
try:
    element_present = EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Strona nie zdazyla sie zaladowac")

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

try:
    element_present = EC.presence_of_element_located((By.ID, 'Login'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Strona nie zdazyla sie zaladowac")

login_input = driver.find_element_by_id("Login")
login_input.clear()
login_input.send_keys(args.login)

password_input = driver.find_element_by_id("Pass")
password_input.clear()
password_input.send_keys(args.password)
password_input.send_keys(Keys.RETURN)

sleep(timeout)
driver.close()
