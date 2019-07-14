"""
    作者: sunshine
    功能: 模拟随机掷骰子
    版本: 2.0
    日期: 2010/4/28
    2.0新增模拟随机投掷两个骰子，并输出结果
"""
import random
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
    total_times = 10          #投掷次数
    roll_count_list = [0] * 11      #初始化次数列表，0
    roll_dice_list = list(range(2,13))    #初始化点数列表，2－12
    dice_dict = dict(zip(roll_dice_list,roll_count_list))   #生成字典

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll = roll1 + roll2
        for j in range(2,13):
            if roll == j:
                dice_dict[j] += 1    #dict[key]返回的是dict的value值
    for i, result in dice_dict.items():
        print('点数:{},次数:{},频率:{}'.format(i, result, result / total_times))

if __name__ == '__main__':
    main()