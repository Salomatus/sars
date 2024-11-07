import json
import os
from abc import ABC, abstractmethod
from typing import Any

from src.vacancies import Vacancy


class FileWorker(ABC):
    """Шаблон классов для работы с файлами данных о вакансиях"""

    @abstractmethod
    def __init__(self, *args: str) -> None:
        """Конструктор экземпляра класса"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> str:
        """Метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> str:
        """Метод для удаления вакансии из файла"""
        pass


class JSONWorker(FileWorker):
    """Класс для работы с файлами данных о вакансиях JSON"""

    ROOT = os.path.join(os.path.dirname(__file__), "..")

    def __init__(self, file_name: str = "vacancies_found") -> None:
        """Инициализация экземпляра класса"""
        os.makedirs(os.path.join(self.ROOT, "data", "JSON"), exist_ok=True)
        self.file_name = os.path.join(self.ROOT, "data", "JSON", file_name + ".json")
        self.__vacancies = Vacancy.cast_to_object_list(self.__read_data())
        self.__write_data()  # Создаст файл если его нет

    def __read_data(self) -> Any:
        """Чтение JSON файла"""
        try:
            with open(self.file_name, "rt") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __write_data(self) -> None:
        """Запись JSON файла"""
        data = [vacancy.to_dict() for vacancy in self.__vacancies]
        with open(self.file_name, "wt") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @property
    def vacancies(self) -> list[Vacancy]:
        """Геттер атрибута вакансий"""
        return self.__vacancies.copy()

    def add_vacancy(self, vacancy: Vacancy) -> str:
        """Добавление вакансии в файл"""
        self.__vacancies.append(vacancy)
        self.__write_data()
        return f"Сохранено. Вакансий в избранном: {len(self.__vacancies)}"

    def delete_vacancy(self, vacancy: Vacancy) -> str:
        """Удаление вакансии из файла"""
        if vacancy in self.__vacancies:
            self.__vacancies.remove(vacancy)
            self.__write_data()
            return f"Удалено. Вакансий в избранном: {len(self.__vacancies)}"
        return f"Не содержится. Вакансий в избранном: {len(self.__vacancies)}"
