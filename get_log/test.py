import urllib.request

url="https://eufy-security-grafana.eufylife.com/d/EFrVYyfnz/chan-pin-chi-xian-ji-lu-cha-xun?orgId=1&var-env=All&var-device_model=T8210"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)