import random
offices = [[],[],[]]
names = ["余涛","迅哥","闰土","施瓦辛格","王晨栋","杨二嫂","初音未来","胡善岷"]
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
while i <= 3:
 for office in offices:
      print("班级%d的人数为%d"%(i,len(office)))
      i +=1
      for name in office:
          print("%s"%name,end="\t")
      print("\n")
      print("-"*30)

