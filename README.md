# Scan Service
Проект для сбора данных о Wi-Fi точках доступа и клиентских станциях с нескольких RaspberryPi. 
Каждое устройство сканирует сеть (airmon-ng) и отправляет результаты на сервер. 
Также реализован примитивный pub/sub паттерн для взаимодействия с RabbitMQ.

## Оглавление

1. [Технологии](#Технологии)
2. [Структура проекта](#Структура-проекта)
3. [Установка и запуск](#Установка-и-запуск)
4. [Маршруты (API)](#Маршруты-api)
5. [Схема БД (UML)](#Схема-бд-uml)
6. [Работа с RabbitMQ](#Работа-с-rabbitmq)
7. [Тестирование](#Тестирование)
8. [Дополнительно](#Дополнительно)

---

## Технологии

- **Python 3.11**
- **FastAPI** (REST‐сервер)
- **SQLAlchemy** 
- **RabbitMQ** (pub/sub) +
- **pytest** (для автотестов)

---

## Структура проекта

my_project/
├── app/
│   ├── init.py
│   ├── main.py         # Точка входа FastAPI
│   ├── routes/
│   │   ├── devices.py
│   │   └── scans.py
│   ├── rabbitmq.py     # Логика pub/sub 
│   ├── db.py           # Подключение к БД
│   └── …
├── tests/
│   ├── test_devices.py
│   ├── test_main.py
│   └── test_scans.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md

---

## Установка и запуск

### 1. Клонировать репозиторий и перейти в папку

```bash
git clone https://github.com/PlaguesW/Mihalich_test.git 
cd Mihalich_test
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
### Запуск приложения через докер

```bash
docker-compose up --build
```