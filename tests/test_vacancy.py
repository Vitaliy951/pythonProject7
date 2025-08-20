from src.vacancy import Vacancy

def test_vacancy_creation():
    vac = Vacancy(
        title="Python Developer",
        url="https://example.com",
        salary_from=100000,
        salary_to=150000,
        description="Test requirements"
    )
    assert vac.title == "Python Developer"
    assert vac.salary_from == 100000