#页面最长等待时间
UI_WAIT_TIME = 4
#本地driver路径
CHROME_EXECUTABLE_PATH = '/Users/mengtingting/PycharmProjects/review/chromedriver'
FIREFOX_EXECUTABLE_PATH = '/Users/mengtingting/PycharmProjects/review/geckodriver'

#初始url
START_URL = 'https://www.jd.com/'
#远程driver服务地址
REMOTE_DRIVER_DICT = {
    'linux':'http://192.168.1.35:4444/wd/hub',
    'windows':'http://192.168.1.35:4444/wd/hub'
}