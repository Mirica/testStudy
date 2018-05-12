#! /usr/bin/env python
# coding = utf-8
l = ['a',99,[1,'r'],9834,'a',1,3,1]
print(l)
#列表操作
l.append('bye') #添加一个元素
print(l)
l.remove(99) #移除一个元素
print(l)
print(l.count('a')) #计算摸个元素在列表中出现的次数
p = l.pop(2)   #把列表中的第x个元素取出，并赋值给p,可以直接赋值使用
print(p)
print(l)