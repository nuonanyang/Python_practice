import requests as req
r = req.get('http://www.yiibai.com/python/')
print(r.text)[0:300]


import urllib3
http = urllib3.PoolManager()

resp = http.request('GET', 'http://yiibai.com/robots.txt')
print (resp.data)

# get the status of the response
print (resp.status)


