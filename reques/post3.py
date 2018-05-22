# coding:utf-8
import requests
import time
import urllib3
urllib3.disable_warnings()
#通过接口添加文章，先手动添加，通过抓包获取需要的cookies
#title = "aa_%s"%str(int(time.time()))
t = time.strftime('%Y_%m_%d_%H_%M_%S')
title = "aa_%s"%t
zhengwen = "bb%s"%str(int(time.time()))#格式转换
url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$Advanced$chkComments":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkMainSyndication":"on",
    "Editor$Edit$Advanced$ckbPublished": "on",
    "Editor$Edit$Advanced$tbEnryPassword": "",
    "Editor$Edit$Advanced$txbEntryName": "",
    "Editor$Edit$Advanced$txbExcerpt": "",
    "Editor$Edit$Advanced$txbTag": "",
    "Editor$Edit$EditorBody": zhengwen,  # 参数不能重复
    "Editor$Edit$lkbDraft": "sdsd",
    "Editor$Edit$txbTitle": title,    # 参数不能重复
}

s = requests.session()
# 验证是否登录成功，访问一个登录之后的页面
print("更新之前的cookies:")
print(s.cookies)
# 加cookies
c = requests.cookies.RequestsCookieJar()
#将手动添加，抓包获得的cookis加入
c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8Gf3jjv4cttDnEy2UYRcGZ1Qc-cenrkc4n4nD4LpTpy3HJ2PU_K756UapFqzVYp6rwR5E6hBjoQTmMcU63r83VQBHHA_s65S62DzpByXsWlK8h_LTrG2dySk3ovEL2HJr8oVawqdNbX29klu83IxF3x1rPmAUWpdWNq6k_5rsmXDpeHCw29fKEJsxQ1V48lKvPDV2HFX2dgRYw3d12L34Wf67mka9Iqon8rp7eauwIvU803knGvzcGe9aXhKm27E5bRx9gA3ndIo2xPInFLMDfXW4XC3b2lWJ3Dphez7F7w9")
c.set(".CNBlogsCookie","920CA8C3DCA17918DFB08D7E6285CA123BCD6F845E99CE21E75C81AA26A72D1893D2E8D8C757E4C2A7BCFE3BEDF1B41FC368792441D3E7A5D1610614F172034FBF6664FA0EC3491D09D0187AAE6EA24BD307C5B7")

# 更新s上的cookies
s.cookies.update(c)
print("更新之后的cookies")
print(s.cookies)

#r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",verify=False)
#print(r1.text)

# 登录成功之后，提交post请求
r2 = s.post(url,data=body)
print(r2.url)
# print(r2.text)
