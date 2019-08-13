import httplib2
import requests
import re
from urllib.parse import urlencode


def ip_check(ip):

     params = urlencode({'ip':ip,'datatype':'jsonp','callback':'find'})
     url = 'http://api.ip138.com/query/?'+params
     headers = {"token":"966cb6635a4e657d6252807b769d9a3d"}
     http = httplib2.Http()
     response, content = http.request(url,'GET',headers=headers)

     location=str(content.decode("utf-8")).split(':')
     b= location[3].replace('"',"").replace('[',"").replace(']',"").replace('}',"").replace(')',"").replace(',',' ')
     return(b)
     
a="139.224.39.0"
print(ip_check(a))



# {oid=24732,mid=87246}