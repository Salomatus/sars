from abc import ABC, abstractmethod


class JsonHandler(ABC):
    """ "Шаблон классов для приведения JSON данных к единому интерфейсу"""

    @abstractmethod
    def converter(self, vacancies: list[dict]) -> list[dict]:
        """Изменение структуры JSON данных"""
        pass


class HandlerHH(JsonHandler):
    """ "Класс обработки JSON данных HeadHunter"""

    def converter(self, vacancies: list[dict]) -> list[dict]:
        """Изменение структуры JSON данных"""
        vacancies_converted = []
        for vacancy in vacancies:
            alt_vacancy = {}
            alt_vacancy["name"] = vacancy["name"]  # Название
            alt_vacancy["employer"] = vacancy["employer"]["name"]  # Работодатель
            alt_vacancy["area"] = vacancy["area"]["name"]  # Область
            alt_vacancy["requirement"] = vacancy["snippet"]["requirement"]  # Требования
            alt_vacancy["responsibility"] = vacancy["snippet"]["responsibility"]  # Обязанности
            alt_vacancy["experience"] = vacancy["experience"]["name"]  # Опыт
            alt_vacancy["schedule"] = vacancy["schedule"]["name"]  # График
            alt_vacancy["employment"] = vacancy["employment"]["name"]  # Трудоустройство
            alt_vacancy["url"] = vacancy["alternate_url"]  # Ссылка
            alt_vacancy["salary"] = vacancy["salary"] if vacancy["salary"] else {}  # Зарплата
            vacancies_converted.append(alt_vacancy)
        return vacancies_converted
