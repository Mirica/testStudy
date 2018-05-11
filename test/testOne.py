#! /usr/bin/env python
# coding : utf-8

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
