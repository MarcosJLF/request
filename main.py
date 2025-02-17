import requests

ID = 2

URL = {
    'get':'http://127.0.0.1:5000/get',
    'get_id': f'http://127.0.0.1:5000/get/{ID}',
    'post':'http://127.0.0.1:5000/api',
    'put':f'http://127.0.0.1:5000/put/{ID}',
    'delete':f'http://127.0.0.1:5000/delete/{ID}'
}

send = {
    'name':'John',
    'age': 25
}
carros = [
    {   
        "modelo": "911",
        "marca": "Porsche",
        "ano": 2020,
        "cor": "azul",
        "km": 2000,
        "preco": 20
    },
    {
        "modelo": "Civic",
        "marca": "Honda",
        "ano": 2022,
        "cor": "prata",
        "km": 5000,
        "preco": 25
    },
    {
        "modelo": "Corolla",
        "marca": "Toyota",
        "ano": 2021,
        "cor": "branco",
        "km": 7000,
        "preco": 27
    },
    {
        "modelo": "Mustang",
        "marca": "Ford",
        "ano": 2023,
        "cor": "vermelho",
        "km": 3000,
        "preco": 50
    },
    {
        "modelo": "Model S",
        "marca": "Tesla",
        "ano": 2022,
        "cor": "preto",
        "km": 1000,
        "preco": 80
    },
    {
        "modelo": "A4",
        "marca": "Audi",
        "ano": 2021,
        "cor": "azul",
        "km": 4000,
        "preco": 35
    },
    {
        "modelo": "X5",
        "marca": "BMW",
        "ano": 2020,
        "cor": "cinza",
        "km": 6000,
        "preco": 60
    },
    {
        "modelo": "Cayenne",
        "marca": "Porsche",
        "ano": 2019,
        "cor": "verde",
        "km": 8000,
        "preco": 90
    },
    {
        "modelo": "Cherokee",
        "marca": "Jeep",
        "ano": 2022,
        "cor": "marrom",
        "km": 2000,
        "preco": 45
    },
    {
        "modelo": "Cruze",
        "marca": "Chevrolet",
        "ano": 2020,
        "cor": "branco",
        "km": 9000,
        "preco": 28
    },
    {
        "modelo": "Fiesta",
        "marca": "Ford",
        "ano": 2018,
        "cor": "azul",
        "km": 12000,
        "preco": 18
    },
    {
        "modelo": "Tiguan",
        "marca": "Volkswagen",
        "ano": 2021,
        "cor": "preto",
        "km": 5000,
        "preco": 42
    },
    {
        "modelo": "Seltos",
        "marca": "Kia",
        "ano": 2022,
        "cor": "vermelho",
        "km": 3000,
        "preco": 33
    },
    {
        "modelo": "Q7",
        "marca": "Audi",
        "ano": 2019,
        "cor": "cinza",
        "km": 7000,
        "preco": 70
    },
    {
        "modelo": "Accord",
        "marca": "Honda",
        "ano": 2020,
        "cor": "prata",
        "km": 4000,
        "preco": 38
    },
    {
        "modelo": "Sentra",
        "marca": "Nissan",
        "ano": 2021,
        "cor": "branco",
        "km": 6000,
        "preco": 29
    },
    {
        "modelo": "Macan",
        "marca": "Porsche",
        "ano": 2022,
        "cor": "preto",
        "km": 2000,
        "preco": 85
    },
    {
        "modelo": "HR-V",
        "marca": "Honda",
        "ano": 2023,
        "cor": "azul",
        "km": 1500,
        "preco": 40
    },
    {
        "modelo": "Ranger",
        "marca": "Ford",
        "ano": 2020,
        "cor": "vermelho",
        "km": 10000,
        "preco": 55
    },
    {
        "modelo": "Outlander",
        "marca": "Mitsubishi",
        "ano": 2021,
        "cor": "verde",
        "km": 5000,
        "preco": 50
    }
]


def get(URL):
    response = requests.get(URL['get'])
    print(response.json())


def get_id(URL):
    response = requests.get(URL['get_id'])
    print(response.json())

def post(carros):

    size = len(carros)

    for i in range(size):
        reponse = requests.post(URL['post'], json=carros[i])
        print(reponse.json())

def put(send):
    response = requests.put(URL['put'], json=send)
    print(response.json())

def delete(URL):
    response = requests.delete(URL['delete'])
    print(response.json())

post(carros)