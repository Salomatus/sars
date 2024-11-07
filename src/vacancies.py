from typing import Any

from src.salary import Salary


class Vacancy:
    """Класс объектов вакансий"""

    def __init__(self, vacancy: dict[str, Any]) -> None:
        """Инициализация экземпляра класса вакансий"""
        self.name: str = vacancy["name"]  # Название
        self.employer: str = vacancy["employer"]  # Работодатель
        self.area: str = vacancy["area"]  # Область
        self.requirement: str = str(vacancy["requirement"])  # Требования
        self.responsibility: str = str(vacancy["responsibility"])  # Обязанности
        self.experience: str = vacancy["experience"]  # Опыт
        self.schedule: str = vacancy["schedule"]  # График
        self.employment: str = vacancy["employment"]  # Трудоустройство
        self.url: str = vacancy["url"]  # Ссылка
        self.salary: Salary = Salary(vacancy["salary"])  # Зарплата

    def __str__(self) -> str:
        """Строковое представление экземпляра класса"""
        return (
            f"{self.name}. Зарплата: {self.salary}\n"
            f"График: {self.schedule}, Занятость: {self.employment}, Опыт: {self.experience}\n"
            f"Работодатель: {self.employer} ({self.area})\n"
            f"URL: {self.url}\n"
            f"Требования:\n{self.requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')}\n"
            f"Обязанности:\n{self.responsibility.replace('<highlighttext>', '').replace('</highlighttext>', '')}"
        )

    def __lt__(self, other: Any) -> bool:
        """Метод сравнения зарплат «меньше»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value < other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value < other
        else:
            raise TypeError("Невозможно сравнить")

    def __le__(self, other: Any) -> bool:
        """Метод сравнения зарплат «меньше или равно»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value <= other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value <= other
        else:
            raise TypeError("Невозможно сравнить")

    def __gt__(self, other: Any) -> bool:
        """Метод сравнения зарплат «больше»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value > other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value > other
        else:
            raise TypeError("Невозможно сравнить")

    def __ge__(self, other: Any) -> bool:
        """Метод сравнения зарплат «больше или равно»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value >= other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value >= other
        else:
            raise TypeError("Невозможно сравнить")

    def __eq__(self, other: Any) -> bool:
        """Метод сравнения зарплат «равно»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value == other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value == other
        else:
            raise TypeError("Невозможно сравнить")

    def __ne__(self, other: Any) -> bool:
        """Метод сравнения зарплат «неравно»"""
        if isinstance(other, self.__class__):
            return self.salary.salary_value != other.salary.salary_value
        elif isinstance(other, (int, float)):
            return self.salary.salary_value != other
        else:
            raise TypeError("Невозможно сравнить")

    def is_there_a_words(self, *args: str) -> bool:
        """Метод проверки наличия ключевых слов в описании"""
        return any(
            [arg.lower() in self.requirement.lower() or arg.lower() in self.responsibility.lower() for arg in args]
        )

    def to_dict(self) -> dict[str, Any]:
        """Возвращает свои атрибуты в виде словаря"""
        self_dict = self.__dict__.copy()
        self_dict["salary"] = self.salary.to_dict()
        return self_dict

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list[Any]:
        """Классметод для получения списка объектов вакансий из JSON"""
        objects_list = []
        for vacancy in vacancies:
            objects_list.append(cls(vacancy))
        return objects_list
