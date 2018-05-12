#! /usr/bin/env python
# coding = utf-8
'''
列表常用
'''
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
l1 = [1,5,33,2,0]
l1.sort() #将原列表排序
print(l1)
print(len(l1)) #计算列表的长度，一共有多少个元素
'''
元祖常用
1.元祖为括号
2.列表、元祖单独去某个值，和字符串一样[],[:][::]
3.用[]取值，原本的字符串、列表、元祖，都是不变的
'''
a = (1,2,3,4)
print(a[1:-1])
print(a[2])
'''
字典
1.字典是无序的
'''
d = {'name':'aa','h':'sd'}
print(d)
print(d.keys()) #只打印keys
print(d.values()) #只打印值
print(d['name'])  #打印某个key的值
d1 = {'age':{'ss','dd','as'}} #嵌套
print(d1['age'])



