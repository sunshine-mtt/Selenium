"""
    作者：sunshine
    功能：输入日期，显示其是一年中第几天
    版本：2.0
    1.0 输入日期，显示其是一年中第几天
    2.0 将元组改为列表
    3.0 将列表改为set无序集合
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

    #定义一个无序集合，存储每月天数
    _30_month_days_set = {4,6,9,11}
    _31_month_days_set = {1,3,5,7,8,10,12}

    #初始化天数
    days = 0
    days += day

    #range(1,1)就是从1到1但不包括1，所以输出是[],所以循环不对1月生效
    for i in range(1,month):
        if i in _30_month_days_set:
            days += 30
        elif i in _31_month_days_set:
            days += 31
        else:
            days += 28

    if month > 2 and leap_year(year):
        days += 1

    print('您查询的是{}年的第{}天'.format(year, days))

if __name__ == '__main__':
    main()