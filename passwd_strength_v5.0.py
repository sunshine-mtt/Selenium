"""
    作者: sunshine
    版本: 5.0
    功能: 判断密码强弱
    2.0 新增限制密码输入次数，终止循环
    3.0 将密码和密码强度写入文件
    4.0 读取保存的文件
    5.0 定义一个password工具类
    日期: 2019/4/26
"""
class PasswordTool:
    """
        密码工具类
    """

    def __init__(self, password):   #password是外部程序要调用这个类时要求传进来的数据
        # 类的属性
        self.password = password    #把password传到类里，当成类的一个属性
        self.strength_level = 0

    #类的方法
    def process_password(self):  #在类里定义的函数，默认的第一个参数是self，这是规范

        # 规则1
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度不合格！')

        # 规则2
        if self.has_number():   #调用类本身的方法时也需要加self.，参数里则不需要再传属性
            self.strength_level += 1
        else:
            print('密码要包含数字！')

        # 规则3
        if self.has_letter():
            self.strength_level += 1
        else:
            print('密码要包含数字！')

    # 类的方法
    def has_number(self):
        is_has_number = False
        for i in self.password:
            if i.isnumeric():
                is_has_number = True
                break
        return is_has_number

    # 类的方法
    def has_letter(self):
        is_has_letter = False
        for i in self.password:
            if i.isalpha():
                is_has_letter = True
                break
        return is_has_letter

def main():
    """
       主函数
    """

    try_time = 5
    while try_time > 0:
        password = input('请输入密码：')
        #实例化密码工具对象
        password_tool = PasswordTool(password)  #调用类
        password_tool.process_password()     #调用类的方法

        f = open('password.txt','a')
        f.write('密码{},强度{}\n'.format(password,password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_time -= 1

    if try_time == 0:
        print('输入次数过多，退出程序！')


if __name__ == '__main__':
    main()