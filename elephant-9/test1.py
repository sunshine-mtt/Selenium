import requests
from bs4 import BeautifulSoup

def get_hero_list(url):
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    li_list = soup.find('div',{'class':'herolist-content'})
    print(li_list)
    hero_list = []

    for li in li_list:
        hero_name = li_list[li].find('a').text().strip()
        hero_img = li_list[li].find('img').text().strip()
        hero_list.append(hero_name,hero_img)

    return hero_list

def main():
    url = "https://pvp.qq.com/web201605/herolist.shtml"
    hero_list = get_hero_list(url)
    print(hero_list)

if __name__ == '__main__':
    main()