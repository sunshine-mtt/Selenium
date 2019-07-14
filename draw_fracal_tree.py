'''
    作者：sunshine
    功能：绘制分型树
    日期： 20/4/2019
'''

import turtle

def draw_branch(branch_length):

    if branch_length > 5:

        # 绘制右侧树枝
        turtle.forward(branch_length)
        print("向前", branch_length)
        turtle.right(20)
        print("右转", 20)
        draw_branch(branch_length - 15)


        # 绘制左侧树枝
        turtle.left(40)
        print("左转", 40)
        draw_branch(branch_length - 15)

        # 返回主节点
        turtle.right(20)
        print("右转", 20)
        turtle.backward(branch_length)
        print("向后", branch_length)

def main():
    '''
        主函数
    '''
    # 向左旋转90度
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()

    draw_branch(100)

    turtle.exitonclick()


if __name__ == '__main__':
    main()