from typing import Any

import requests


class HeadHunterAPI:
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Инициализация экземпляра класса"""
        self.employers: list[dict] = []  # Компании
        self.vacancies: list[dict] = []  # Вакансии
        self.__industries: dict[str, str] = {}  # Отрасли
        self.employer_industry: list[dict] = []  # Связи КОМПАНИЯ-ОТРАСЛЬ

    def load_data(self, employer_ids: list[str]) -> None:
        """Загрузка данных для заполнения таблиц в Data Base"""
        for employer_id in employer_ids:
            employer_info = self.get_employer_info(employer_id)
            if employer_info:
                self.employers.append(employer_info)
            employer_vacancies_info = self.get_employer_vacancies_info(employer_id)
            self.vacancies.extend(employer_vacancies_info)

    def get_employer_info(self, employer_id: str) -> dict[str, str]:
        """Получение информации о компании по id"""
        employer = self.api_request(f"https://api.hh.ru/employers/{employer_id}")
        if employer:
            self._industries_update(employer["id"], employer["industries"])  # Обновление отраслей
            return {
                "employer_id": employer["id"],
                "type": employer["type"],
                "name": employer["name"],
                "area": employer["area"]["name"],
                "site_url": employer["site_url"],
            }
        return {}

    def get_employer_vacancies_info(self, employer_id: str) -> list[dict]:
        """Получение информации о вакансиях по id компании"""
        employer_vacancies = []
        page = 0
        pages = 1
        while page < pages:
            page_with_vacancies = self.api_request(
                "https://api.hh.ru/vacancies",
                params={"employer_id": employer_id, "page": str(page), "per_page": "100"},
            )
            page += 1
            pages = page_with_vacancies.get("pages", 1)
            # Обработка и добавление вакансий в список компании
            for vacancy in page_with_vacancies.get("items", []):
                employer_vacancies.append(
                    {
                        "vacancy_id": vacancy["id"],
                        "employer_id": vacancy["employer"]["id"],
                        "name": vacancy["name"],
                        "url": vacancy["alternate_url"],
                        "schedule": vacancy["schedule"]["name"],
                        "employment": vacancy["employment"]["name"],
                        "salary_from": vacancy["salary"]["from"] if vacancy["salary"] else None,
                        "salary_to": vacancy["salary"]["to"] if vacancy["salary"] else None,
                        "currency": vacancy["salary"]["currency"] if vacancy["salary"] else None,
                    }
                )
        return employer_vacancies

    @staticmethod
    def api_request(url: str, params: dict[str, str] | None = None) -> Any:
        """Функция делает API запросы на указанный URL с заданными параметрами,
        и возвращает сущность с результатом запроса"""
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException:
            return {}
        if response.status_code != 200:
            return {}
        return response.json()

    def _industries_update(self, employer_id: str, industries_list: list[dict]) -> None:
        """Обновление словаря отраслей и сохранение связей: КОМПАНИЯ-ОТРАСЛЬ"""
        for industry in industries_list:
            self.__industries[industry["id"]] = industry["name"]
            self.employer_industry.append({"employer_id": employer_id, "industry_id": industry["id"]})

    @property
    def industries(self) -> list[dict]:
        """Геттер атрибута __industries"""
        return [dict(industry_id=industry_id, name=name) for industry_id, name in self.__industries.items()]
