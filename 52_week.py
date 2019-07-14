"""
    作者：sunshine
    功能：52周存钱法
    版本：1.0
    日期：04/22/2019
"""

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

    while i <= total_week:
        saving_value += money_value
        print('第{}周存入{}，总金额{}'.format(i, money_value, saving_value))

        i += 1
        money_value += increase_value

if __name__ == '__main__':
    main()