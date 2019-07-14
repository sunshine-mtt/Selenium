"""
    作者: sunshine
    版本: 2.0
    功能: 限制密码输入次数，终止循环
    1.0 判断密码强弱

"""
def check_number_exist(password_str):
    has_number = False
    for i in password_str:
        if i.isnumeric():
            has_number = True
            break
    return has_number

def check_letter_exist(password_str):
    has_letter = False
    for i in password_str:
        if i.isalpha():
            has_letter = True
            break
    return has_letter

def main():
    """
        主函数
    """
    try_time = 5    #密码输入次数

    while try_time > 0:

        password = input('请输入密码：')
        strength = 0    #密码强度初始值

        #密码长度大于等于8
        if len(password) >= 8:
            strength += 1
        else:
            print('请输入8位及8位以上的密码！')

        #密码包含数字
        if check_number_exist(password):
            strength += 1
        else:
            print('请输入包含数字的密码！')

        # 密码包含字母
        if check_letter_exist(password):
            strength += 1
        else:
            print('请输入包含字母的密码！')

        if strength == 3:
            print('恭喜，您输入的密码是强密码！')
            break
        else:
            print('您输入的密码是弱密码！')
            try_time -= 1

    if try_time == 0:
        print('您输入的次数过多，终止查询！')
if __name__ == '__main__':
    main()