from jd.base.locate_element import LocateElement
from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self,driver,url):
        self.driver = driver
        self.locate_element = LocateElement(self.driver,url)

    def login_function(self,linklogin,login,name,password,login_btn,name_value,password_value):
        # self.locate_element.open_url()
        # self.locate_element.find_element(By.CLASS_NAME, 'link-login').click()
        # self.locate_element.find_element(By.LINK_TEXT, '账户登录').click()
        # self.locate_element.find_element(By.ID, 'loginname').send_keys('17721386744')
        # self.locate_element.find_element(By.ID, 'nloginpwd').send_keys('meng15803408440')
        # self.locate_element.find_element(By.ID, 'loginsubmit').click()
        # time.sleep(4)

        self.locate_element.open_url()
        self.locate_element.find_element(By.CLASS_NAME, linklogin).click()
        self.locate_element.find_element(By.LINK_TEXT, login).click()
        self.locate_element.find_element(By.ID, name).send_keys(name_value)
        self.locate_element.find_element(By.ID, password).send_keys(password_value)
        self.locate_element.find_element(By.ID, login_btn).click()
        time.sleep(4)








