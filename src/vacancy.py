from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    title: str
    url: str
    salary_from: int
    salary_to: int
    description: str

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'description': self.description
        }

    def __post_init__(self):
        self._validate_salary()

    def _validate_salary(self):
        self.salary_from = self.salary_from or 0
        self.salary_to = self.salary_to or 0
        if self.salary_to < self.salary_from:
            self.salary_to, self.salary_from = self.salary_from, self.salary_to

    @classmethod
    def cast_to_object_list(cls, data: list) -> list:
        return [
            cls(
                title=item.get('name', 'Без названия'),
                url=item.get('alternate_url', '#'),
                salary_from=item.get('salary', {}).get('from', 0),
                salary_to=item.get('salary', {}).get('to', 0),
                description='\n'.join(filter(None, [
                    item.get('snippet', {}).get('requirement', ''),
                    item.get('snippet', {}).get('responsibility', '')
                ]))
            )
            for item in data
            if item.get('name') and item.get('alternate_url')
        ]
