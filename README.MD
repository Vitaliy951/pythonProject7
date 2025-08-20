# **Курсовая работа: Парсер вакансий с HH.ru**

Описание
Программа для сбора, анализа и управления вакансиями с платформы HeadHunter через API.
Реализованы функции фильтрации, сортировки и сравнения вакансий с сохранением данных в JSON.

## Особенности реализации

### Архитектура проекта

Абстрактные классы для API и хранилища данных
Наследование и полиморфизм для расширения функционала
Реализация принципов SOLID (SRP, OCP)
Инкапсуляция данных вакансий
Ключевые функции
Получение вакансий через HH API (REST)
Валидация данных при создании объектов
Сравнение вакансий по зарплате
Фильтрация по ключевым словам
Топ-N вакансий по зарплате
Сохранение/загрузка в JSON
Консольный интерфейс
Требования
Python 3.10+
Зависимости:
Копировать
[tool.poetry.dependencies]
requests = "^2.32.0"
pydantic = "^2.7.0"
Установка
Копировать
poetry install  # через poetry
# или
pip install -r requirements.txt
Использование
Копировать
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver

# Инициализация компонентов
hh_api = HeadHunterAPI()
json_saver = JSONSaver('vacancies.json')

# Получение и сохранение вакансий
vacancies_data = hh_api.get_vacancies("Python Developer")
vacancies = Vacancy.cast_to_object_list(vacancies_data)
json_saver.add_vacancies(vacancies)

# Фильтрация и сортировка
filtered = json_saver.filter_vacancies(salary_from=100000, keywords=["Django"])
top_5 = sorted(filtered, reverse=True)[:5]
Структура проекта
Копировать
.

├── src/

│   ├── abstract_api.py    # Абстрактный класс API

│   ├── hh_api.py         # Реализация HH.ru API

│   ├── vacancy.py         # Класс вакансии

│   └── json_saver.py      # Работа с JSON-хранилищем

├── tests/

│   ├── test_api.py

│   └── test_vacancy.py

├── main.py               # Точка входа

└── pyproject.toml


##### Документация API


Официальная документация HH.ru API
Поддерживаемые методы:
GET /vacancies (поиск по тексту)
Параметры: text, area=113 (Россия), per_page=100
Лицензия
MIT License



**Ключевые улучшения:**
1. Добавлена структура проекта с явным указанием модулей
2. Приведены примеры использования основных компонентов
3. Указаны требования к версии Python и зависимостям
4. Добавлена секция с документацией API
5. Упрощена навигация по разделам
6. Указаны поддерживаемые методы API HH.ru
7. Добавлена информация о лицензии

Для тестирования: `pytest tests/ -v`