# Используйте последнюю версию Python в качестве основного образа
FROM python:latest

# Установите рабочую директорию для приложения
WORKDIR /home/user_bot/bot

# Копируйте файлы в приложение
COPY . .

# Установите все необходимые зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Установите команду, которая будет запускать бота
CMD ["python", "Index.py"]

#POWERED CHATGPT