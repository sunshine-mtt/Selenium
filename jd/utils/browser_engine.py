from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from jd.config import basic_config

class BrowserEngine:
    @staticmethod
    def init_local_driver(browser):
        if browser == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=option,
                                      executable_path=basic_config.CHROME_EXECUTABLE_PATH)
        elif browser == 'firefox':
            option = webdriver.FirefoxOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Firefox(firefox_options=option,
                                       executable_path=basic_config.FIREFOX_EXECUTABLE_PATH)
        else:
            return None

        return driver

    @staticmethod
    def init_remote_driver():
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        result_dict = {}
        for item in remote_browser_dict.items():
            for name,url in item.items():
                if name == 'linux':
                    option = webdriver.ChromeOptions()
                    option.add_argument('disable-infobars')
                    driver = webdriver.Remote(
                        options=option,
                        command_executor=url,
                        desired_capabilities=DesiredCapabilities.CHROME
                    )
                    result_dict[name] = driver
                else:
                    option = webdriver.FirefoxOptions()
                    option.add_argument('disable-infobars')
                    driver = webdriver.Remote(
                        options=option,
                        command_executor=url,
                        desired_capabilities=DesiredCapabilities.FIREFOX
                    )
                    result_dict[name] = driver
                return result_dict