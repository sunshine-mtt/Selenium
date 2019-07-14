from jd.base.locate_element import LocateElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class LeftNav:
    def __init__(self,driver,url):
        self.driver = driver
        self.locate_element = LocateElement(self.driver,url)

    def left_nav_function(self):
       # self.locate_element.open_url()
        element = self.locate_element.find_element(By.LINK_TEXT, '手机')
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(4)








