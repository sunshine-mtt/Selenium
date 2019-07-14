"""
    作者：sunshine
    功能：52周存钱法
    版本：2.0
    日期：04/22/2019
    记录每周存款数
"""
import math

def main():
    """
        主函数
    :return:
    """
    i = 1               #第一周
    total_week = 52     #总周数
    money_value = 10    #第一周存钱金额
    increase_value = 10 #每周递增金额
    saving_value = 0    #存入总金额

    money_list = []     #记录每周存款数的列表

    while i <= total_week:

        money_list.append(money_value)     #把每周的存款数加到列表中

        saving_value = math.fsum(money_list)    #math.fsum() 对集合内的元素求合
        print('第{}周存入{}，总金额{}'.format(i, money_value, saving_value))

        i += 1
        money_value += increase_value

    print(money_list)
if __name__ == '__main__':
    main()