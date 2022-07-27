from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

# У кого-то не работала без ниже. у меня ок
   # browser.switch_to.window(browser.window_handles[0])

    x_element = browser.find_element(By.ID, "input_value").text

    def calc(x_element):
        return str(math.log(abs(12 * math.sin(int(x_element)))))
    input1 = browser.find_element(By.ID, "answer").send_keys(calc(x_element))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()