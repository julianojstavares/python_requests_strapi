import requests
import json

def get(apiUrl, endPoint, contentType):
    response = requests.get(url=f'{apiUrl}/{endPoint}', headers=contentType)
    print(response.json())

def post(apiUrl, endPoint,postData):
    response = requests.post(url=f'{apiUrl}/{endPoint}', data=postData)
    print(response.status_code)
    if response.status_code == 200:
        print('Post succeded')

def put(apiUrl, endPoint, idNumber, postData):
    response = requests.put(url=f'{apiUrl}/{endPoint}/{idNumber}', data=postData)
    print(response.status_code)
    if response.status_code == 200:
        print('Put succeded')

def delete(apiUrl, endPoint, idNumber):
    response = requests.delete(url=f'{apiUrl}/{endPoint}/{idNumber}')
    print(response.status_code)
    if response.status_code == 200:
        print('Delete succeded')
    
    