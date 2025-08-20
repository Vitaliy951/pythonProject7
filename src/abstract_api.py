from abc import ABC, abstractmethod

class JobAPI(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list:
        pass