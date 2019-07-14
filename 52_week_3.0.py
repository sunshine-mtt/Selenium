"""
    作者：sunshine
    功能：52周存钱法
    版本：3.0
    日期：04/22/2019
    使用for循环
"""
import math

def main():
    """
        主函数
    :return:
    """
    total_week = 52
    money_value = 10  # 第一周存钱金额
    increase_value = 10  # 每周递增金额

    money_list = []  # 记录每周存款数的列表

    for i in range(total_week):

        money_list.append(money_value)

        saving_value = math.fsum(money_list)

        print('第{}周存入{}，总金额{}'.format(i + 1, money_value, saving_value))

        money_value += increase_value

if __name__ == '__main__':
    main()