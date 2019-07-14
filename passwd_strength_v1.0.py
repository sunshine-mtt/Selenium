"""
    作者: sunshine
    版本: 1.0
    功能: 判断密码强弱
"""
def check_number_exist(password_str):
    for i in password_str:
        if i.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    for i in password_str:
        if i.isalpha():
            return True
    return False

def main():
    """
        主函数
    """
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
        print('您的密码是强密码！')
    else:
        print('您的密码是弱密码！')
if __name__ == '__main__':
    main()