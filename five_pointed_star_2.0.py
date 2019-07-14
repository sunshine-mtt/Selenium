'''
    作者：sunshine
    功能：绘制五角星2.0
'''
import turtle

#汇制步骤
def draw(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    if size < 100:
        draw(size + 15)

#主函数
def main():
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()
    #设置画笔的颜色和笔的尺寸
    turtle.color('yellow')
    turtle.pensize(2)
    #调用绘制步骤函数
    draw(40)
    #绘制结束
    turtle.exitonclick()

if __name__ == '__main__':
    main()