'''
    作者：sunshine
    功能：处理bmr程序的异常机制
    版本：3.0
'''


def main():

    '''
        主函数
    '''

    yes_or_no = input("是否退出程序?(y/n):")

    while yes_or_no != 'y':

        print("请输入以下信息，以空格分割")

        input_str = input("性别：，体重(kg)：，身高(cm)：，年龄：")
        # 使用split函数之后，字符串转换为list类型，需赋值于一个新的变量
        str_list = input_str.split(' ')

        dmr_process(str_list)

        yes_or_no = input("是否退出程序?(y/n):")

    print("您已退出程序！")

def dmr_process(str_list):
    '''
        执行步骤函数
    :param str_list:
    :return:
    '''
    try:
        sex = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if sex == '女':
            bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
        elif sex == '男':
            bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
        else:
            bmr = -1

        if bmr != -1:
            print("您的身体BMR指数为:{}大卡".format(bmr))
        else:
            print("程序暂不支持您输入的性别！")

    except ValueError:
        print('请输入正确的数值！')
    except IndexError:
        print('您输入的值太少！')
    except:
        print('程序错误！')

if __name__ == '__main__':
    main()