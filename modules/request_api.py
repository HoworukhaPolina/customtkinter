import requests
#імпортуємо модулі, які будемо використовувати у коді;
from .read_json import read_json
#із файла read.json імпортуємо json,який допоможе читати файли цього типу
import json
#ще раз імпортуємо модулі, а на цей раз сам json
data_api = read_json(name_file= 'config_api.json')
#змінна data_api, яка допоможе записати усі данні
API_KEY = data_api['api_key']
#сам ключ api, який дає змогу записувати дані ключа
CITY_NAME = data_api['city_name']
#названня міста у якому ви знаходитесь, для того щоб передавати дані погоди
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#дані які передаются з допомогою юрл силки
response = requests.get(URL)
#змінна, яка відповідає на запроси інформації к другим сайтам
if response.status_code == 200:
    #умова, якщо статус відповіді на максимум
    data_dict = json.loads(response.content)
    #завантажування даних з відповіди
    print(json.dumps(data_dict, indent= 4))
    #виведення усього на єкран