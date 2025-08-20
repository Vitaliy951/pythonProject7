from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
from src.filters import VacancyFilter

def user_interaction():
    hh_api = HeadHunterAPI()
    saver = JSONSaver()

    try:
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода: "))
        filter_words = input("Введите ключевые слова для фильтрации (через запятую): ").split(',')
        salary_range = input("Введите диапазон зарплат (например 100000-150000): ")

        # Получение данных
        hh_api.connect()
        raw_vacancies = hh_api.get_vacancies(search_query)
        vacancies = Vacancy.cast_to_object_list(raw_vacancies)

        # Фильтрация
        filtered = VacancyFilter.filter_by_keyword(vacancies, filter_words)
        ranged = VacancyFilter.filter_by_salary(filtered, salary_range)
        sorted_vacancies = VacancyFilter.sort_vacancies(ranged)
        top_vacancies = VacancyFilter.get_top_vacancies(sorted_vacancies, top_n)

        # Сохранение и вывод
        for vac in top_vacancies:
            saver.add_vacancy(vac)
            print(f"""
            Вакансия: {vac.title}
            Зарплата: {vac.salary_from}-{vac.salary_to}
            Ссылка: {vac.url}
            Требования: {vac.description[:100]}...
            """)

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    user_interaction()