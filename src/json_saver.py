import json
from pathlib import Path
from typing import List, Optional
from .abstract_storage import Storage
from .vacancy import Vacancy


class JSONSaver(Storage):
    def __init__(self, filename: str = 'vacancies.json'):
        self._filename = Path(filename)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Создает файл с пустым списком, если не существует"""
        if not self._filename.exists():
            self._filename.write_text('[]', encoding='utf-8')

    def add_vacancy(self, vacancy: Vacancy) -> None:
        if not self._validate_vacancy(vacancy):
            raise ValueError("Некорректный объект вакансии")

        data = [v.to_dict() for v in self.get_vacancies()]
        data.append(vacancy.to_dict())
        self._save(data)

    def get_vacancies(
            self, criteria: Optional[dict] = None
    ) -> List[Vacancy]:
        """Получение вакансий с возможностью фильтрации"""

        with self._filename.open(encoding='utf-8') as f:
            data = json.load(f)

        vacancies = [Vacancy(**item) for item in data]

        return self._filter_vacancies(vacancies, criteria) if criteria else vacancies

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаление вакансии по URL"""
        data = self.get_vacancies()
        updated = [v for v in data if v.url != vacancy.url]
        self._save([v.to_dict() for v in updated])

    def clear_file(self) -> None:
        """Полная очистка файла"""
        self._filename.write_text('[]', encoding='utf-8')

    def _save(self, data: list) -> None:
        """Внутренний метод сохранения данных"""
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _validate_vacancy(self, vacancy: Vacancy) -> bool:
        """Расширенная валидация вакансии"""
        return all([
            isinstance(vacancy.title, str) and len(vacancy.title) > 2,
            isinstance(vacancy.url, str) and vacancy.url.startswith('http'),
            vacancy.salary_from >= 0,
            vacancy.salary_to >= vacancy.salary_from,
            isinstance(vacancy.description, str)
        ])

    def _filter_vacancies(self, vacancies: List[Vacancy], criteria: dict) -> List[Vacancy]:
        """Приватный метод для фильтрации по критериям"""
        filtered = []
        for vac in vacancies:
            match = True
            for key, value in criteria.items():
                if getattr(vac, key, None) != value:
                    match = False
                    break
            if match:
                filtered.append(vac)
        return filtered