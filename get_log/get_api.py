
# coding=utf-8
import requests

task = {'task': 'my task'}
# 请求该接口
response = requests.get('http://172.16.20.95/loginError')

# 获取响应数据，并解析JSON，转化为python字典
result = response.json()

# 打印响应状态码
print(response.status_code)

# 打印result
print(result)

# 打印结果中的 ‘todo1’ 任务
print(result['todo1'])

