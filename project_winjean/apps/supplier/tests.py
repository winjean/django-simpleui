# from django.test import TestCase
#
# # Create your tests here.
import requests
import datetime

# 新增pi
# url = 'http://127.0.0.1:8000/supplier/'
# data = {
#     'id': "1012",
#     'name': "1012",
#     'gender': 1,
#     'status': 1,
#     'create_time': "2022-04-08 14:16:00",
#     'create_user': "zhang",
#     'update_user': "zhang",
# }
# h = requests.post(url, data=data)
# print(h.text)

# 删除
# url = 'http://127.0.0.1:8000/supplier/1010'
# h = requests.delete(url)
# print(h.text)

# 修改
# url = 'http://127.0.0.1:8000/supplier/1011/'
# data = {
#     "id": "1011",
#     "name": "1011",
#     "gender": "0",
#     "status": "1",
#     "create_time": "2022-04-08 14:16:00",
#     "create_user": "333",
#     "update_user": "333"
# }
# h = requests.put(url, data=data)
# print(h.text)

# 获取详情
url = 'http://127.0.0.1:8000/supplier/111'
h = requests.get(url)
print(h.text)

# 获取列表
# url = 'http://127.0.0.1:8000/supplier/?page=2'
# h = requests.get(url)
# print(h.text)

# url = 'http://127.0.0.1:8000/supplier/print'
# h = requests.get(url)
# print(h.text)

