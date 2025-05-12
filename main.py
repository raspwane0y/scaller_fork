import requests
from bs4 import BeautifulSoup

# URL сайта, который будем парсить
url = 'https://example.com '

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Извлекаем и выводим заголовки h1, h2
    h1 = soup.find('h1')
    print("H1:", h1.text if h1 else "Не найден")

    h2_list = soup.find_all('h2')
    print("\nH2 заголовки:")
    for h2 in h2_list:
        print('-', h2.text)
else:
    print(f"Ошибка загрузки страницы: {response.status_code}")
