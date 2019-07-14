#获取href和title
def extract_page(current_page):
    # 获取第一个页面http和tile信息
    start_href = current_page.find('<a href=')
    start_quote = current_page.find('"', start_href)
    end_quote = current_page.find('"', start_quote + 1)
    end_stract = current_page.find('>', end_quote)
    start_stract = current_page.find('<', end_stract + 1)
    href = current_page[start_quote + 1:end_quote]
    title = current_page[end_stract + 1:start_stract]

    if href.startswith('/'):
        print(href, title)
        return start_stract
    else:
        return -1

def main():
    page_hero = """<ul class="sub-nav-inner">
            	<li class="down-nav"> &nbsp; </li>
            	<li class="down-nav"> <a href="/cp/a20170829bbgxsm/index.html" target="_blank" title="版本介绍" onclick="PTTSendClick('headNav','data_ver','版本介绍');">版本介绍</a> <a href="/web201605/introduce.shtml" target="_blank" title="游戏介绍" onclick="PTTSendClick('headNav','data_moba','游戏介绍');">游戏介绍</a> <a href="/web201605/herolist.shtml" target="_blank" title="英雄资料" onclick="PTTSendClick('headNav','data_hero','英雄资料');">英雄资料</a> 
    """
    while True: #如果不设break条件，while True就是死循环
        last_index = extract_page(page_hero)
        page_hero = page_hero[last_index:]
        if last_index == -1:
            break




    # 获取第一个页面http和tile信息


if __name__ == '__main__':
    main()



# second = 60
# minute = 60
# seconds_per_hour = second * minute
# seconds_per_day = seconds_per_hour * 24
# print(seconds_per_day)
# dive1 = seconds_per_day // seconds_per_hour
# dive2 = float(seconds_per_day / seconds_per_hour)
# print(dive1)
# print(dive2)
#
# #b * (1 + r /100)**n
# import math
# a = 2
# b = 3
# c = 4
# print(math.sqrt((a**2+c**2)/b))
#
# def menu(wine,entree,dessert=0):
#     return "wine:{},entree:{},dessert:{}".format(wine,entree,dessert)
#
# s = menu(entree=1,wine=2,dessert=3)
# print(s)