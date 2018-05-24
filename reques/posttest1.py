#! /usr/bin/env python
# coding = utf-8
import requests
import json
#登录
login_url = 'https://www.ketangpai.com/UserApi/login'
login_par = {'email':'386150953@qq.com',
           'password':'***',
           'remember':0}
login_r = requests.session()
login=login_r.post(login_url,login_par)
print(login.text)
print(login.cookies)
print(login.json())
#课程首页
index_url = 'https://www.ketangpai.com/Main/index.html'
index_cookie = login.cookies
index = requests.get(index_url,cookies=index_cookie)
print(index.status_code)
#homework
homework_url = 'https://www.ketangpai.com/HomeworkApi/listsHomework'
homework_par = {'courseid':'MDAwMDAwMDAwMLOGsZeG36tr'}
homework = requests.get(homework_url,params=homework_par,cookies =index_cookie)
#print(homework.json())
a = homework.json()
print(a)
print(type(a))
b = a['lists'][0]['title']
if '简历' in b:
    print('最后一课啦')
elif '其他' in b:
    print('plz come on')
else:
    print('first  you need time ')
c = json.dumps(a)
print(type(c))
print(c)