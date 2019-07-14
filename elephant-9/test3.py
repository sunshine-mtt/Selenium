s = {'ab','cb'}
print(dict(s))
print(s)

#zip
s1 = 'adc'
s2 = 'dce'
d = list(zip(s1,s2))
print(d)
#unzip
s3,s4 = zip(*d)
print(list(s3))
print(list(s4))

day = [1,2,3,4,5]
for index, key in enumerate(day,2):
    print(index,key)


dict = {'mon':1,'tue':2,'wed':3}
for key,value in dict.items():
    print(key,':',value)

for k in dict.keys():
    print(k)

for value in dict.values():
    print(value)

import math
num_list = [i * i for i in range(0,int(math.sqrt(500))) if i%3 == 2]
print(num_list)

import random
num_list = random.sample(range(10),10)
print(num_list)

l1 = [i for i in num_list if i < 5]
print(l1)

container = ['acd','ded','ddd']
s="".join([str(data) for data in container])
print(s)

for i in range(10):
    print(i)
    if i == 15:
        break
else:
    print('over')

for i in range(5):
    for j in range(i+1):
        print("x",end=" ")
    print("-")

for m in range(1,10):
    for n in range(1,m+1):
        print('{}*{}={}'.format(n,m,m*n),end=" ")
    print("")

for x in range(7):
    for y in range(x+1):
        print(1,end=" ")
    print("")

print([[0 for x in range(5)] for x in range(5)])

str = 'abbcdefbccb'
cnt = {b: str.count(b) for b in set(str)}
print(cnt)

def print_all_args(req1,req2,*args,**kwargs):
    print(req1)
    print(req2)
    print('args:', args)
    print('kwargs', kwargs)

print_all_args(1,2,3,4,5,day='mon',month=2)

def print_time():
    print('now is 3')

def run_func(func):
    func()

run_func(print_time)

def exp(n):
    def tmp(m):
        return m*n
    return tmp

print(exp(2)(3))

from time import clock
def timer(func):
    def test(*args):
        t0 = clock()
        func(*args)
        return clock() - t0
    return test

def add(x,y):
    return x+y

def binary(func,*args):
    return func(*args)

print(timer(binary)(add,1,2))