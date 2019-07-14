"""
    作者: sunshine
    功能: AQI计算
    版本: 6.0
    6.0新增功能: 网络爬虫
    日期: 2019/4/28
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(url):
    """
        返回url的文本
    """
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div',{'class':'span1'})
    print(div_list)

    city_aqi = []
    for i in range(8):
        caption = div_list[i].find('div',{'class':'caption'}).text.strip()
        value = div_list[i].find('div',{'class':'value'}).text.strip()
        city_aqi.append((value,caption))
    return city_aqi

def main():
    """
        主函数
    """
    input_str = input('是否退出程序(y/n?): ')
    while input_str != 'y':
        city_pinyin = input('请输入您要查询的城市： ')
        url = 'http://pm25.in/' + city_pinyin
        city_aqi = get_city_aqi(url)
        print(city_aqi)

        print()
        input_str = input('是否退出程序(y/n?): ')

    print('您已退出程序！')

if __name__ == '__main__':
    main()
