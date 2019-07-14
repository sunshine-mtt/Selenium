'''
    作者：sunshine
    功能：身体BMR指数,实现循环输入，直到用户退出
    版本：1.0

'''

def main():

    yes_or_no = input("是否退出程序？请输入y/n:")

    while yes_or_no != 'y':

        sex = input("请输入您的性别：")
        weight = float(input("请输入您的体重："))
        height = float(input("请输入您的身高："))
        age = int(input("请输入您的年龄："))

        if sex == '女':
            bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
        elif sex == '男':
            bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
        else:
            bmr = -1

        if bmr != -1:
            print('身体BMR指数为' + str(bmr) + '大卡')
        else:
            print("程序暂不支持该种性别查询")

        print()
        yes_or_no = input("是否退出程序？请输入y/n:")

    print("您已退出程序！")

if __name__ == '__main__':
    main()