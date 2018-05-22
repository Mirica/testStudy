#! /usr/bin/env python
# coding = utf-8
import  requests
# url和参数写一行
'''
url = 'http://zzk.cnblogs.com/s/blogpost?Keywords=bb'
# 请求头部
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Cookie": "_ga=GA1.2.865342035.1503842097; __utma=226521935.865342035.1503842097.1511965730.1512395827.3; __utmz=226521935.1506156701.1.1.utmcsr=mamicode.com|utmccn=(referral)|utmcmd=referral|utmcct=/info-detail-1728757.html; __gads=ID=b4fc842c685a9b8f:T=1509190884:S=ALNI_MbEMu-56DkVeTQtVHtlZFnLlLWpcA; __utma=59123430.865342035.1503842097.1520166296.1526129027.6; __utmz=59123430.1519560648.3.2.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; UM_distinctid=162de1f7e2b35-0733f99c938b448-13656f4a-15f900-162de1f7e2c653; .CNBlogsCookie=01AEE72FA3C50C32A4E3B4F2A4F9A32601E828D9FC34E0AD96E6C12E688402A0C7E06B1440045AA7B62CA2FF84A91E5715A060A5395508425526FC6E99DD86865153FD33318BDFD6E72D93D9D44F382ADE22ADE5; .Cnblogs.AspNetCore.Cookies=CfDJ8Gf3jjv4cttDnEy2UYRcGZ3Pi9OM4skIIYVBcrbhroStjsMtGr_EU9_WEVVJVdmE-g2f0dxTt46cJJDhXy68jvw6faypAo9ZVoj1c6EQF8ITGmDxhqQXzmMaUjZkawLpoeBuOvHL7LYI_-G7Cf-tMsl6WQFF91xu5m4RhHb3WNZWm0nEJxCDJ9uCPvY6_hT7gYDhZaKq6z5KX7evbdcwpq1UopsGpuCr3GmvDbmClc8hwufK2OoHk54uwcna9EbzgFPrgF-GDTBrpBS2Nv-684HgicO6V0Cb4qSK90BcL68ValeAY4bqnF7rChHNuh-awA; _gid=GA1.2.573385483.1525956638; __utmb=59123430.1.10.1526129027; __utmc=59123430; __utmt=1"
    }
r3 = requests.get(url, headers=h)  # headers=h
print(r3.text)
'''
url1 = 'http://zzk.cnblogs.com/s/blogpost'
pa = {
    'Keywords':'bb'
}
he ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Cookie": "_ga=GA1.2.865342035.1503842097; __utma=226521935.865342035.1503842097.1511965730.1512395827.3; __utmz=226521935.1506156701.1.1.utmcsr=mamicode.com|utmccn=(referral)|utmcmd=referral|utmcct=/info-detail-1728757.html; __gads=ID=b4fc842c685a9b8f:T=1509190884:S=ALNI_MbEMu-56DkVeTQtVHtlZFnLlLWpcA; __utma=59123430.865342035.1503842097.1520166296.1526129027.6; __utmz=59123430.1519560648.3.2.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; UM_distinctid=162de1f7e2b35-0733f99c938b448-13656f4a-15f900-162de1f7e2c653; .CNBlogsCookie=01AEE72FA3C50C32A4E3B4F2A4F9A32601E828D9FC34E0AD96E6C12E688402A0C7E06B1440045AA7B62CA2FF84A91E5715A060A5395508425526FC6E99DD86865153FD33318BDFD6E72D93D9D44F382ADE22ADE5; .Cnblogs.AspNetCore.Cookies=CfDJ8Gf3jjv4cttDnEy2UYRcGZ3Pi9OM4skIIYVBcrbhroStjsMtGr_EU9_WEVVJVdmE-g2f0dxTt46cJJDhXy68jvw6faypAo9ZVoj1c6EQF8ITGmDxhqQXzmMaUjZkawLpoeBuOvHL7LYI_-G7Cf-tMsl6WQFF91xu5m4RhHb3WNZWm0nEJxCDJ9uCPvY6_hT7gYDhZaKq6z5KX7evbdcwpq1UopsGpuCr3GmvDbmClc8hwufK2OoHk54uwcna9EbzgFPrgF-GDTBrpBS2Nv-684HgicO6V0Cb4qSK90BcL68ValeAY4bqnF7rChHNuh-awA; _gid=GA1.2.573385483.1525956638; __utmb=59123430.1.10.1526129027; __utmc=59123430; __utmt=1"
}
r = requests.get(url1,params= pa,headers = he)
print(r.text)