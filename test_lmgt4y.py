# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_lmgt4y(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_lmgt4y(self):
        success = True
        wd = self.wd
        wd.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
        wd.find_element_by_id("searchInput").click()
        wd.find_element_by_id("searchInput").clear()
        wd.find_element_by_id("searchInput").send_keys("олененок")
        wd.find_element_by_id("searchButton").click()
        wd.find_element_by_link_text("Оленёнок Рудольф").click()
        wd.find_element_by_link_text("3 Примечания").click()
        wd.find_element_by_link_text("Вячеслав Баранов").click()
        wd.find_element_by_link_text("5.1 Роли в кино").click()
        wd.find_element_by_link_text("Ранетки").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
