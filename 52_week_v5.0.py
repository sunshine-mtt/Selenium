"""
    作者：sunshine
    功能：52周存钱法
    版本：4.0
    日期：04/22/2019
    4.0 灵活设置每周存款数，增加的存款数及存款周数
    5.0 根据用户输入的日期，判断是一年的第几周，然后输出相应的金额
"""
import math
import datetime

def saving_money(total_week, money_value, increase_value):
    """
        计算存款金额
    """
    money_list = []  # 记录每周存款数的列表
    saved_value = []  #截止到第几周的存款数

    for i in range(total_week):
        money_list.append(money_value)

        saving_value = math.fsum(money_list)

        saved_value.append(saving_value)

        money_value += increase_value

    return saved_value


def main():
    """
        主函数
    :return:
    """
    total_week = int(input("请输入存款周数："))
    money_value = float(input("请输入每周存款金额："))  # 第一周存钱金额
    increase_value = float(input("请输入每周递增金额："))  # 每周递增金额
    #调用函数
    saved_value = saving_money(total_week, money_value, increase_value)

    #输入查询日期
    input_str_value = input("请输入您要查询的日期：")
    #转换字符串为datetime.datetime类型
    input_value = datetime.datetime.strptime(input_str_value, '%Y/%m/%d')
    #获取第几周(isocalendar()输出三个结果：年，全年第多少周，周几)
    week_num = input_value.isocalendar()[1]

    print("您要查询的是第{}周的金额是{}元".format(week_num,saved_value[week_num - 1]))


if __name__ == '__main__':
    main()