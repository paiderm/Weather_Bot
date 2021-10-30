import requests

API_KEY = "4591a3b4cce03fe385a69d62957bc3cf"

API_URL = "api.openweathermap.org/data/2.5/weather?"

api_url = API_URL + "q=" + "Platteville" + "," +"WI"+"&appid="+API_KEY
response = requests.get("api_url")

print(response.status_code)