import requests

ID = 2

URL = {
    'get':'http://127.0.0.1:5000/get',
    'get_id': f'http://127.0.0.1:5000/get/{ID}',
    'post':'http://127.0.0.1:5000/post',
    'put':f'http://127.0.0.1:5000/put/{ID}',
    'delete':f'http://127.0.0.1:5000/delete/{ID}'
}

send = {
    'name':'John',
    'age': 25
}

def get(URL):
    response = requests.get(URL['get'])
    print(response.json())


def get_id(URL):
    response = requests.get(URL['get_id'])
    print(response.json())

def post(send):

    reponse = requests.post(URL['post'], json=send)
    print(reponse.json())

def put(send):
    response = requests.put(URL['put'], json=send)
    print(response.json())

def delete(URL):
    response = requests.delete(URL['delete'])
    print(response.json())
