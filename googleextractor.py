import time
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.opera.options import Options

driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
# driver = webdriver.Opera("C:\webdrivers\operadriver.exe")
driver.get("http://www.google.com")
print(driver.title)
inputElement = driver.find_element_by_name("q")
inputElement.send_keys(input(str('what is your search?\n')))
inputElement.submit()

link = []
while True:
    for a in driver.find_elements_by_xpath('.//a'):
        if a.get_attribute('href'):
            val = a.get_attribute('href')
            if val.startswith("https://www.google.com/") or val.startswith("https://consent.yahoo.com/") or val.startswith("https://support.google.com/") or val.startswith("https://policies.google.com/") or val.startswith("https://myactivity.google.com/") or val.startswith("https://accounts.google.com/") or val.startswith("https://webcache.googleusercontent.com/") or val.startswith("https://en.wikipedia.org/") or val.startswith("https://www.youtube.com") or val.startswith("https://en.m.wikipedia.org") or val.startswith("https://telegram.me") or val.startswith("http://webcache.googleusercontent.com/") or val.startswith("https://translate.google.com") or val.startswith("https://www.indeed.com") or val.startswith("https://www.googleadservices.com") or val.startswith("https://www.glassdoor.com") or val.startswith("https://www.googleadservices.com/") or val.startswith("javascript:void(0)") or val.startswith("mailto:?body") or val.startswith("https://mail.google.com/") or val.startswith('https://www.bbc.com/') or val.startswith("https://instagram.com") or val.startswith("https://github.com"):
                continue
            link.append(val)
            with open("Urls/ExtactUrlRiceKerman.txt", "w") as w:
                w.write('\n'.join(set(link)))
        print('its not link')
    # print("there are not link siyamak")

    element = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, 'pnnext')))
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    element.click()

