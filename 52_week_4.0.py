"""
    作者：sunshine
    功能：52周存钱法
    版本：4.0
    日期：04/22/2019
    4.0 灵活设置每周存款数，增加的存款数及存款周数
"""
import math

def saving_money(total_week, money_value,increase_value):
    """
        计算存款金额
    """
    saving_value = 0

    money_list = []  # 记录每周存款数的列表

    for i in range(total_week):

        money_list.append(money_value)

        saving_value = math.fsum(money_list)

        money_value += increase_value

    return saving_value

def main():
    """
        主函数
    :return:
    """
    total_week = int(input("请输入存款周数："))
    money_value = float(input("请输入每周存款金额："))  # 第一周存钱金额
    increase_value = float(input("请输入每周递增金额："))  # 每周递增金额

    saving_value = saving_money(total_week, money_value,increase_value)

    print(saving_value)
    
if __name__ == '__main__':
    main()