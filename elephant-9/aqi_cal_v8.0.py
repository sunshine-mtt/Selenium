class Person:
    name = []

p1 = Person()
p2 = Person()
p1.name.append('小明')
print(p1.name)
print(p2.name)
print(Person.name)