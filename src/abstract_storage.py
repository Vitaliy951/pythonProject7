from abc import ABC, abstractmethod
from typing import List, Optional
from src.vacancy import Vacancy


class Storage(ABC):
    """Абстрактный класс для работы с хранилищами данных"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавление вакансии в хранилище"""
        raise NotImplementedError("Метод add_vacancy должен быть реализован в дочернем классе")

    @abstractmethod
    def get_vacancies(self, criteria: Optional[dict] = None) -> List[Vacancy]:
        """
        Получение вакансий по критериям
        :param criteria: Словарь с критериями фильтрации
        Пример: {'salary_from': 100000, 'salary_to': 150000}
        """
        raise NotImplementedError("Метод get_vacancies должен быть реализован в дочернем классе")

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии из хранилища"""
        raise NotImplementedError("Метод delete_vacancy должен быть реализован в дочернем классе")

    def _validate_vacancy(self, vacancy: Vacancy) -> bool:
        """Валидация объекта вакансии (дополнительная проверка)"""
        return isinstance(vacancy, Vacancy) and all([
            vacancy.title,
            vacancy.url,
            isinstance(vacancy.salary_from, (int, float)),
            isinstance(vacancy.salary_to, (int, float))
        ])
