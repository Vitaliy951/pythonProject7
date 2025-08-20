from typing import List
from src.vacancy import Vacancy


class VacancyFilter:
    @staticmethod
    def filter_by_keyword(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
        """Фильтрация вакансий по ключевым словам в описании"""
        if not keywords:
            return vacancies

        return [vac for vac in vacancies
                if any(kw.lower() in vac.description.lower() for kw in keywords)]

    @staticmethod
    def filter_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
        """Фильтрация по диапазону зарплат"""
        if not salary_range:
            return vacancies

        try:
            min_salary, max_salary = map(int, salary_range.split('-'))
            return [vac for vac in vacancies
                    if vac.salary_from >= min_salary and vac.salary_to <= max_salary]
        except (ValueError, AttributeError):
            return vacancies

    @staticmethod
    def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
        """Сортировка вакансий по убыванию зарплаты"""
        return sorted(vacancies, reverse=True)

    @staticmethod
    def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
        """Получение топ N вакансий"""
        return vacancies[:top_n]
