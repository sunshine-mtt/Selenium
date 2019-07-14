"""
    作者: sunshine
    版本: 3.0
    功能: 将密码和密码强度写入文件
    1.0 判断密码强弱
    2.0 新增限制密码输入次数，终止循环
"""

def has_number(password_str):
    is_has_number = False
    for i in password_str:
        if i.isnumeric():
            is_has_number = True
            break
    return is_has_number

def has_letter(password_str):
    is_has_letter = False
    for i in password_str:
        if i.isalpha():
            is_has_letter = True
            break
    return is_has_letter

def main():
    """
        主函数
    """
    try_time = 5  # 尝试密码次数初始值

    while try_time > 0:

        password = input('请输入密码：')
        strength = 0  # 密码强度初始值

        #规则1－－长度大于8
        if len(password) >= 8:
            strength += 1
        else:
            print('密码长度不够！')
        #规则2－－包含数字
        if has_number(password):
            strength += 1
        else:
            print('密码需要包含数字！')
        #规则3－－包含字母
        if has_letter(password):
            strength += 1
        else:
            print('密码需要包含字母！')

        # 打开文件，'a'表示没有文件会生成文件，写入的文件会追加进去
        f = open('password_strength_v3.0.txt', 'a')
        f.write('密码{},强度{}\n'.format(password, strength))
        f.close()

        #密码强度合格判断
        if strength == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_time -= 1

    if try_time == 0:
        print('输入次数太多，已退出程序！')

if __name__ == '__main__':
    main()