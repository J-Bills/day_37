import requests
import json

WEIGHT_KG = 81.6466
HEIGHT_CM = 182.88
AGE = 26

API_KEY = '788989e8dee1415a11f5b8a518bf7da9'
APP_ID = 'ddb5c6f6'

headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

parameters ={
    'query':"",
    'age':AGE,
    'weight':WEIGHT_KG,
    'height':HEIGHT_CM
}


usr_input = input("input what exercise you did:\n")

parameters.update({'query':usr_input})
print(parameters)


response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',json=parameters, headers=headers)
response.raise_for_status()

data = response.json()
print(data)