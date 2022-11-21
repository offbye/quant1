#!/usr/bin/python3

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
a = list4
a.pop()
print(a)
print(list4)
print(list4.clear())
print('white' in list4)
for color in list4:
    print(color)
