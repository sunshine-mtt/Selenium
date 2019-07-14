x=1
def change():
    global x
    x=5
    print('inside',x)
print(x)
print(change())
print(x)

y = 3
def new():
    y = 4
    print('inside',y)

print(y)
print(new())
print(y)

# smallest = 0
# inputStr = input('enter a value:')
# while inputStr != "":
#     value = int(inputStr)
#     if value < smallest:
#         smallest = value
#     inputStr = input('enter a value:')
# print(smallest)

from random import randint
mystery=randint(1,10)
print(mystery)



for i in range(10):
    if i%2:
        print(i)



def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

input_str = input('是否退出程序？')

while input_str != 'yes':

    num1 = eval(input('first number:'))
    num2 = eval(input('second number:'))
    choice = input('enter choice(1/2/3/4):' )

    if choice == '1':
        print(add(num1,num2))
    elif choice == '2':
        print(substract(num1,num2))
    elif choice == '3':
        print(multiply(num1,num2))
    elif choice == '4':
        print(divide(num1,num2))
    else:
        print('invalid input')
    input_str = input('是否退出程序？')
    