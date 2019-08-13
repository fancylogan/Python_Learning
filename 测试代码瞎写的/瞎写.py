def ip_check(ip):
    url1 ='http://m.ip138.com/ip.asp?ip='+ip
     html1 = requests.get(url1)
     #time.sleep(0.2)
     html1.raise_for_status()
     html1.encoding = html1.apparent_encoding
     p = html1.text[-312:-220]
     zhengze_temp = "本站主数据：(.*?)</p>"
     temp = re.findall(zhengze_temp,p,re.S)
     d=temp[0]
     return(d)

