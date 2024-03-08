import json
import requests

def request_get(url):
    return json.loads(requests.get(url).text)

def unpack_response(response_text):
    dictionary = [{"uid":response["uid"], "name":response["name"], "images":response["images"]} for response in response_text]
    return dictionary