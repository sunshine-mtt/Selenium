from jd.base.locate_element import LocateElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class IndexSearch:
    def __init__(self,driver,url):
        self.driver = driver
        self.locate_element = LocateElement(self.driver,url)

    def index_search_function(self):
        #self.locate_element.open_url()
        self.locate_element.find_element(By.XPATH, '//*[@id="key"]').send_keys('笔记本')
        self.locate_element.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()
        time.sleep(4)








