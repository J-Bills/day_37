import requests


API_KEY = '788989e8dee1415a11f5b8a518bf7da9'
APP_ID = 'ddb5c6f6'

parameters = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}

response = requests.get('https://trackapi.nutritionix.com/www.v2/natural/exercise')