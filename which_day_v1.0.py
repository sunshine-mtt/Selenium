"""
    作者：sunshine
    功能：输入日期，显示其是一年中第几天
    版本：1.0
"""
from datetime import datetime

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
    month_days = (31,28,31,30,31,30,31,31,30,31,30,31)

    #获取查询日期在一年中的第几天
    days = sum(month_days[:month - 1]) + day

    #判断是平年还是闰年
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        #判断是否大于2月，大于加1
        if month > 2:
            days += 1

    print('您查询的日期是在1年中的第{}天'.format(days))

if __name__ == '__main__':
    main()