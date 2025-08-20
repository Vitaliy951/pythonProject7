import os
import json
import pytest
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


class TestJSONSaver:
    @pytest.fixture
    def temp_file(self, tmp_path):
        return tmp_path / "test_vacancies.json"

    def test_add_vacancy(self, temp_file):
        saver = JSONSaver(str(temp_file))
        vac = Vacancy(
            title="Python Developer",
            url="https://example.com/vacancy/1",  # Добавлен корректный URL
            salary_from=100000,
            salary_to=150000,
            description="Test description"
        )
        saver.add_vacancy(vac)
