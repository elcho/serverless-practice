from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('APIXU_WEATHER_API_KEY')


def get_forecast():

    response = requests.get(f'http://api.apixu.com/v1/forecast.json?key={api_key}&q=08701&days=1')
    status = response.status_code
    print(response.json())
    return response.json()



