import json
import requests

def request_get(url):
    """Esta funcion hace un request tipo GET a la url recibida
    Parameters
    ----------
    url: [str]
        URL de la API a utilizar
    Returns
    ----------
    [list]
        Retorna un listado con los datos recibidos
    """
    return json.loads(requests.get(url).text)

def unpack_response(response_text):
    """Esta funcion desempaca y selecciona los datos recibidos de la API
    Parameters
    ----------
    url: [list]
        Listado que contiene la respuesta de la API
    Returns
    ----------
    [list]
        Retorna un listado de diccionarios con los datos filtrados
    """
    data = [{"uid":response["uid"], "name":response["name"], "images":response["images"]} for response in response_text]
    return data