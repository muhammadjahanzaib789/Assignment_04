import requests

city_name="Karachi"
API_key='f921a898bcee89f6c7bada7c87ece6b4'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['weather'])