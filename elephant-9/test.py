class Person:
    x = 5
    y = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y

person = Person(10,20)
person.z = 7
print(person.x)
print(person.y)
print(Person.x)
print(Person.y)
print(person.add())
print(person.add())
print(person.z)


list = [1,2,3,4,5,6]
list[0]=10
list.insert(0,11)
del list[-1]
del list[6:]
list.remove(5)
list.append(8)
print(list)
list2 = ['num1','num2']
print(list+list2)
print(list.pop())   #最后一位被清除
print(list.pop(2))
print(list.pop(0))

for i in range(1,10):
    for j in range(1,i+1):
        print(u'{}*{}={}\t'.format(j,i,i*j),end='')

    print()


def dele_elem(x,index):
    del x[index]

x = [5] * 100
dele_elem(x,-1)
print(len(x))


liste = [4,1,3,9,0]
liste.sort(reverse=True)
print(liste)

liste2 = [4,1,3,9,0]
sorted_list = sorted(liste2)
print(sorted_list)
print(liste2)

y = ' '.join(sorted('abcde'))
print(y)

dict = {
    'size':'medium',
    'height':'163cm'
}
print(dict['size'])
dict['age'] = 19
print(dict)
del dict['age']
print(dict)
dict.clear()
print(dict)