import requests
import json
from config import api_url, end_point, content_type

class Clientes:
    def __init__(self):
        self.url = api_url

    def getAll(self):
        response = requests.get(self.url + "/" + end_point)
        print(response.status_code)
        if response.status_code == 200:
            print(response.json())

    def post(self, postData):
        response = requests.post(self.url + "/" + end_point,
        json=postData,
        headers=content_type)
        print(response.status_code)
        if response.status_code == 200:
            print("Post succeded")
    
    def put(self, idNumber, postData):
        response = requests.put(self.url + "/" + end_point + "/" + f'{idNumber}',
        json=postData,
        headers=content_type)
        print(response.status_code)
        if response.status_code == 200:
            print("Put succeded")

    def delete(self, idNumber):
        response = requests.delete(self.url+ "/" + end_point + "/" + f'{idNumber}')
        print(response.status_code)
        if response.status_code == 200:
            print("Delete succeded")