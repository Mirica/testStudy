#! /usr/bin/env python
# coding : utf-8
##一些算法练习，总结在这里
#打印一颗圣诞树
height = 5
starts = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * starts))
    starts += 2
print((' '*height) + '|')

def b():
    b =1
    def bchange():
        nonlocal b
        b += 1
    bchange()
    print(b)

#数学练习四个数字，分别是：1、2、3、4,组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range (1,5):
            if (i != k) and (i != j) and (k != j):
                print(i,j,k)
print(i)
a = int(input('净利润'))
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if a > arr[idx]:
        r += (a - arr[idx]) * rat[idx]
       # print((i - arr[idx]) * rat[idx])
        #i = arr[idx]
print(r)

i = 'ss'




