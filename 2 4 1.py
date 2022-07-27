from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)

    element = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    x_element = browser.find_element(By.ID, "input_value").text

    def calc(x_element):
        return str(math.log(abs(12 * math.sin(int(x_element)))))
    input1 = browser.find_element(By.ID, "answer").send_keys(calc(x_element))
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()