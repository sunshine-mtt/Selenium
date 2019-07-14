"""
    作者: sunshine
    功能: 模拟随机掷骰子
    版本: 5.0
    2.0新增功能: 模拟随机投掷两个骰子，并输出结果
    3.0新增功能: 可视化投掷两个骰子的结果（散点图）
    4.0新增功能: 对结果进行简单的数据统计和分析（直方图）
    5.0新增功能: 使用科学计算库Numpy简化程序，并实现可视化效果
    日期: 2010/4/28
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import _rebuild

_rebuild()

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']   #可显示中文，字体改成黑体
plt.rcParams['axes.unicode_minus'] = False     #解决负号问题

def main():
    """
        主函数
    """
    total_times = 10000      #投掷次数

    #记录骰子的结果，7不取，取到6
    roll1_arr = np.random.randint(1, 7, size=total_times)
    print(roll1_arr)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    print(roll2_arr)
    roll3_arr = np.random.randint(1, 7, size=total_times)
    print(roll3_arr)
    result_arr = roll1_arr + roll2_arr + roll3_arr
    print(result_arr)
    hist, bins = np.histogram(result_arr, bins=range(3,20))
    print(hist)    #次数
    print(bins)    #点数

    #数据可视化
    plt.hist(result_arr, bins=range(3,20), density=1, edgecolor='black', linewidth=1, rwidth=0.8)
    #设置x轴坐标点显示
    tick_labels = ['3点','4点','5点','6点','7点',
                   '8点','9点','10点','11点','12点',
                   '13点','14点','15点','16点','17点',
                   '18点']
    tick_pos = np.arange(3,20) + 0.5
    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('次数')
    plt.show()

if __name__ == '__main__':
    main()