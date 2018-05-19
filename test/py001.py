#! /usr/bin/env python
# coding = utf-8
#变量
name = 'yummy'
#单变量赋值
a = 123
b = 12.3
d = 1+2j
#多变量赋值
e = f = 1
#交换赋值
a,b = b,a
print('my name is %s' % name)
print(type(name)) #type()查看数据类型
#计算婓波那契数列（前两个数的和是第三个数）

f = [0,1]
for i in range(8):
    f.append(f[-2]+f[-1])
print(f)

f1 = [0,1]
num = int(input('how many nums do you want?'))
for i in range(num):
    f1.append(f1[-1]+f1[-2])
print(f1)
print(num)
print(len(f1))



