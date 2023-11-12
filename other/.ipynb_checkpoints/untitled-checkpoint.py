import requests
from bs4 import BeautifulSoup
import os

# URL-адрес страницы с PDF-файлами
url = "https://the-eye.eu/public/Books/rpg.rem.uz/7th%20Sea%20Guides/01%20For%20The%20Player%20And%20GM/"

# Папка для сохранения файлов
download_folder = "C:/Users/YourUsername/Downloads"

# Создаем папку, если она не существует
os.makedirs(download_folder, exist_ok=True)

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Разбираем HTML-контент страницы с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все ссылки на PDF-файлы
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]
    
    for pdf_url in pdf_links:
        # Получаем имя файла из URL
        pdf_filename = os.path.join(download_folder, pdf_url.split('/')[-1])
        
        # Скачиваем и сохраняем PDF-файл
        pdf_response = requests.get(pdf_url)
        
        if pdf_response.status_code == 200:
            with open(pdf_filename, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
            print(f"Скачан файл: {pdf_filename}")
        else:
            print(f"Не удалось скачать PDF-файл: {pdf_url}")
else:
    print(f"Не удалось получить доступ к странице: {url}")
