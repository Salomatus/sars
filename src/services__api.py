from abc import ABC, abstractmethod
from typing import Any

import requests

from src.json_handlers import JsonHandler


class ParserAPI(ABC):
    """Шаблон для работы с API сервиса с вакансиями"""

    @abstractmethod
    def __init__(self, json_handler: JsonHandler) -> None:
        """Конструктор экземпляра класса"""
        pass

    @abstractmethod
    def load_vacancies(self, search_query: str) -> list[dict[str, Any]]:
        """API запрос для получения списка вакансий по ключевой фразе"""
        pass


class HeadHunterAPI(ParserAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self, json_handler: JsonHandler) -> None:
        """Инициализация экземпляра класса"""
        self.json_handler = json_handler
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": "0", "per_page": "100"}
        self.vacancies: list[dict] = []

    def load_vacancies(self, search_query: str) -> list[dict]:
        """API запрос для получения списка вакансий по ключевой фразе"""
        self.params["text"] = search_query
        while True:
            request_result = requests.get(self.url, headers=self.headers, params=self.params).json()
            self.vacancies.extend(request_result["items"])
            if int(self.params["page"]) == request_result["pages"] - 1:
                self.params["page"] = "0"
                break
            self.params["page"] = str(int(self.params["page"]) + 1)
        return self.json_handler.converter(self.vacancies)
