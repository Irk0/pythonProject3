from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import warnings


class TestWeb(unittest.TestCase):
    def test_ok(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[@required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[@required]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[@required]")
        input3.send_keys("Ivanov@ii.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_neok(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[@required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[@required]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[@required]")
        input3.send_keys("Ivanov@ii.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()  # Строка запуска программы
