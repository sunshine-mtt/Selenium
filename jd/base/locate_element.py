from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from jd.config import basic_config

class LocateElement(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open_url(self):
        self.driver.get(self.url)
        return self.driver

    def find_element(self,
                     *locator,
                     element=None,
                     timeout=None,
                     wait_type='visibility',
                     when_failed_close_browser=True):
        try:
            if element == None:
                if wait_type == 'visibility':
                    return self.init_wait(timeout).until(EC.visibility_of_element_located(locator))
                else:
                    return self.init_wait(timeout).until(EC.presence_of_element_located(locator))
            else:
                #判断元素是否可见，如果可见就返回这个元素
                return self.init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))
        except NoSuchElementException:
            if when_failed_close_browser:
                self.driver.quit()
            raise NoSuchElementException(msg='定位元素失败，定位方式是{}'.format(locator))
        except TimeoutException:
            if when_failed_close_browser:
                self.driver.quit()
            raise TimeoutException(msg='定位元素失败，定位方式是{}'.format(locator))

    def find_elements(self,
                     *locator,
                     element=None,
                     timeout=None,
                     wait_type='visibility',
                     when_failed_close_browser=True):
        try:
            if element == None:
                if wait_type == 'visibility':
                    return self.init_wait(timeout).until(EC.visibility_of_all_elements_located(locator))
                else:
                    return self.init_wait(timeout).until(EC.presence_of_all_elements_located(locator))
            else:
                # 判断元素是否可见，如果可见就返回这个元素
                return self.init_wait(timeout).until(EC.visibility_of(element.find_elements(*locator)))
        except NoSuchElementException:
            if when_failed_close_browser:
                self.driver.quit()
            raise NoSuchElementException(msg='定位元素失败，定位方式是{}'.format(locator))
        except TimeoutException:
            if when_failed_close_browser:
                self.driver.quit()
            raise TimeoutException(msg='定位元素失败，定位方式是{}'.format(locator))


    def init_wait(self,timeout):
        if timeout == None:
            return WebDriverWait(self.driver,basic_config.UI_WAIT_TIME)
        else:
            return WebDriverWait(self.driver,timeout)