from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_saver import JSONSaver


def user_interaction():
    hh_api = HeadHunterAPI()
    hh_api.connect()

    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query)
    vacancy_objects = Vacancy.cast_to_object_list(vacancies)

    saver = JSONSaver()
    for vac in vacancy_objects:
        saver.add_vacancy(vac)

    # Фильтрация и вывод
    top_n = int(input("Введите количество вакансий для вывода: "))
    filtered = sorted(vacancy_objects, reverse=True)[:top_n]

    for vac in filtered:
        print(f"{vac.title}: {vac.salary_from}-{vac.salary_to} руб.")
