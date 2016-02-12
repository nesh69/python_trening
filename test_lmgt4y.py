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

class (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("https://www.google.ru/?gfe_rd=cr&ei=FMG9VpzXLY3DNLCqpaAE&gws_rd=ssl")
        wd.find_element_by_id("lst-ib").click()
        wd.find_element_by_id("lst-ib").clear()
        wd.find_element_by_id("lst-ib").send_keys("let me google that")
        wd.find_element_by_css_selector("b").click()
        wd.find_element_by_name("btnG").click()
        wd.find_element_by_name("btnG").click()
        wd.find_element_by_link_text("Let me google that for you").click()
        wd.find_element_by_link_text("×").click()
        wd.find_element_by_id("rcnt").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
