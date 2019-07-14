"""
    作者：sunshine
    功能：输入日期，显示其是一年中第几天
    版本：2.0
    1.0 输入日期，显示其是一年中第几天
    2.0 将元组改为列表
"""
from datetime import datetime

def leap_year(year):
    # 判断是平年还是闰年
    is_leap_year = False

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        is_leap_year = True

    return is_leap_year

def main():
    """
        主函数

    """
    input_value_str = input('请输入您要查询的日期(yyyy/mm/dd): ')
    #把字符串转换为datetime类型
    input_value = datetime.strptime(input_value_str,'%Y/%m/%d')
    #获取年、月、日
    year = input_value.year
    month = input_value.month
    day = input_value.day

    #定义一个元组，存储每月天数
    month_days = [ 31,28,31,30,31,30,31,31,30,31,30,31 ]

    if month > 2 and leap_year(year):
        month_days[1] = 29

    # 获取查询日期在一年中的第几天
    days = sum(month_days[:month - 1]) + day

    print('您查询的是{}年的第{}天'.format(year, days))

if __name__ == '__main__':
    main()