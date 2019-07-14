'''
    作者：sunshine
    功能：绘制五角星
'''

import turtle

#汇制步骤
def draw():
    count = 0
    while count < 5:
        turtle.forward(100)
        turtle.right(144)
        count += 1
#主函数
def main():
    #抬起画笔
    turtle.penup()
    #设置画笔的初始位置，默认位置是0，0，位于画部正中央
    turtle.setpos(-50,-50)
    #放下画笔
    turtle.pendown()
    #设置画笔的颜色和笔的尺寸
    turtle.color('yellow')
    turtle.pensize(2)
    #调用绘制步骤函数
    draw()
    #绘制结束
    turtle.exitonclick()

if __name__ == '__main__':
    main()