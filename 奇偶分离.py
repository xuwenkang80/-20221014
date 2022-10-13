import random as r
list = []
list1 = []
for i in range (10):
    n = r.randint(0,100)
    if n%2 == 0:
        list.append(n)
    else:
        list1.append(n)
print("偶数有",list)
print("奇数有",list1)
