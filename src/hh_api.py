import requests
from src.abstract_api import JobAPI


class HeadHunterAPI(JobAPI):
    __slots__ = ('_base_url',)

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"

    def connect(self):
        response = requests.get(self._base_url)
        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к API")
        return True

    def get_vacancies(self, search_query: str, per_page: int = 100) -> list:
        params = {
            "text": search_query,
            "per_page": per_page,
            "area": 113  # Россия
        }
        response = requests.get(self._base_url, params=params)
        # БЫЛО
        #return response.json().get('items', [])
        #СТАЛО
        return response.json()['items']
