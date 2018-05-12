#! /usr/bin/env python
# coding = utf-8
#运算
a = 1 + 2
b = 5 - 2
c = 3 * 6
d = 8 / 3
e = 20 // 3  #取整
f = 20 % 3
g = 2 ** 5   #乘方
print(a,b,c,d,e,f,g)
#连接
x = 'hello'
y = 'world'
z = 3
t = 5
print(x+y) #helloworld
print((z+t)) # 8
#切片
s = '-hello world-'
print(s[7:3:-1]) #w ol
print(s.split('o')) #按照某个符号或字符，切割字符串，返回的是list['-hell', ' w', 'rld-']
print(s.strip('-'))#去掉前后的某个符号，返回字符串hello world
c = '[sjkhdla]'
print(c)  #列表[sjkhdla]
print(c.strip('[]'))#字符串sjkhdla
