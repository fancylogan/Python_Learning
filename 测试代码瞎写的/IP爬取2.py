import requests
import re
import time

def ip_check(ip):
     url ='http://m.ip138.com/ip.asp?ip='+ip
     html = requests.get(url)
     time.sleep(0.2)
     html.raise_for_status()
     html.encoding = html.apparent_encoding
     a = html.text[-400:-220]
     zhengze = "本站主数据：(.*?)</p>"
     temp = re.findall(zhengze,a,re.S)
     print(a)
     return(temp[0])
     
ip = "139.224.39.0"
print(ip_check(ip))



# {oid=24732,mid=87246}