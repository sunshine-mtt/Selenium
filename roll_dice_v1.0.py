"""
    作者: sunshine
    功能: 随机掷骰子
    版本: 1.0
    日期: 2019/4/26
"""
import random
#获取随机掷骰子数
def roll_dice():
    roll = random.randint(1,6)
    return roll

def main():
    """
        主函数
    """
    total_times = 10000   #掷骰子次数
    roll_list = [0] * 6   #存储点数出现次数列表
    #统计每次掷骰子的点数，和该点数出现的次数
    for i in range(total_times):
        roll = roll_dice()
        #j为索引＋1
        for j in range(1,7):
            if roll == j:
                roll_list[j - 1] += 1

    for i, roll in enumerate(roll_list):
        print('点数:{},次数:{},频率:{}'.format(i + 1, roll, roll/total_times))

if __name__ == '__main__':
    main()