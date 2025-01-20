import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"В городе {city_name} сейчас {description}, температура {temperature}°C")
    else:
        print("Не удалось получить данные о погоде. Проверьте правильность названия города.")

if __name__ == "__main__":
    api_key = "ВАШ_API_КЛЮЧ"  # Замените ВАШ_API_КЛЮЧ на ваш реальный API-ключ
    city_name = input("Введите название города: ")
    get_weather(city_name, api_key)
