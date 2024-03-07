import json
import requests

def request_get(url, data = None):
    response = requests.get(url, data=data)
    print(response)
    return json.loads(response.text)

def request_post(url, data):
    response = requests.get(url, data=data)
    print(response)
    return json.loads(response.text)

def request_put(url, data):
    response = requests.get(url, data=data)
    print(response)
    return json.loads(response.text)

def request_delete(url, data = None):
    return requests.delete(url = url, data = data)

url = 'https://reqres.in/api/users'

#1.- Obtencion de usuarios
users_data = request_get(url)
print(users_data)
print('\n\n')

#2.- Creacion de nuevo usuario
new_user = """first_name: Ignacio,
            last_name: Profesor""" # El api ya no tiene trabajo
created_user = request_post(url, new_user)
print(created_user)
print('\n\n')

#3.- Actualizacion de un usuario
new_user = """first_name: morpheus,
            residence: zion""" # El api ya no tiene trabajo
updated_user = request_put(url + "/2", new_user)
print(updated_user)
print('\n\n')

#4.- Eliminacion de un usuario
new_user = """first_name : Tracey"""
response = request_delete(url, new_user) #Alternativamente se puede buscar el id con un get y luego hacer el delete con el id
print(response)
print('\n\n')

#4.- Eliminacion de un usuario Alternativo
datos = request_get(url, new_user)
data_tracey_id = [data for data in datos['data'] if data['first_name'] == "Tracey"][0]['id']
response = request_delete(url + str(data_tracey_id))
print(response)
