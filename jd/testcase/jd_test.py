import unittest
from jd.config.logging_setting import get_logger
from jd.utils.browser_engine import BrowserEngine
from jd.page.login_page import LoginPage
from jd.page.index_search import IndexSearch
from jd.page.left_nav import LeftNav
from jd.config import basic_config
import time
import os
import HTMLTestRunner
import ddt
from jd.utils.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class JdTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BrowserEngine.init_local_driver('chrome')
        cls.url = basic_config.START_URL
        cls.logger = get_logger()
        cls.logger.info('测试开始')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.logger.info('测试结束')

    def setUp(self) -> None:
        self.logger.info('单个测试开始')
        self.driver.get('https://www.jd.com')

    def tearDown(self) -> None:
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                print(file_path)
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @ddt.data(*data)
    def test_login(self,data):
        linklogin, login, name, password, login_btn, name_value, password_value = data
        login_page = LoginPage(self.driver,self.url)
        login_page.login_function(linklogin, login, name, password, login_btn, name_value, password_value)
        title = self.driver.title
        self.assertNotIn('登录',title)
        self.logger.info('登录用例执行--pass!')

    @unittest.skip('test_index_search')
    def test_index_search(self):
        index_search = IndexSearch(self.driver,self.url)
        index_search.index_search_function()
        title = self.driver.title
        self.assertIn('笔记本',title)
        self.logger.info('首页搜索用例执行--pass!')

    @unittest.skip('test_left_nav')
    def test_left_nav(self):
        left_nav = LeftNav(self.driver,self.url)
        left_nav.left_nav_function()

if __name__ == '__main__':
    report_file = os.path.join(os.path.dirname(os.getcwd()),'report','login_report.html')
    with open(report_file,'wb') as f:
        suite = unittest.TestLoader().loadTestsFromTestCase(JdTest)
        run = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=0,title='login_report')
        run.run(suite)