"""
    作者: sunshine
    功能: 模拟随机掷骰子
    版本: 4.0
    2.0新增功能: 模拟随机投掷两个骰子，并输出结果
    3.0新增功能: 可视化投掷两个骰子的结果（散点图）
    4.0新增功能: 对结果进行简单的数据统计和分析（直方图）
    日期: 2010/4/28
"""
import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import _rebuild

_rebuild()

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']   #可显示中文，字体改成黑体
plt.rcParams['axes.unicode_minus'] = False     #解决负号问题

def roll_dice():
    """
        随机投掷骰子函数
    """
    roll = random.randint(1,6)
    return roll

def main():
    """
        主函数
    """
    total_times = 1000       #投掷次数

    #记录骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll_list.append(roll1 + roll2)

    print(roll_list)

    #数据可视化
    plt.hist(roll_list, bins=range(2,14), density=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('次数')
    plt.show()

if __name__ == '__main__':
    main()