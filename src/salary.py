from typing import Any

from src.currency_converters import ConstantsCurrency
from src.errors import ConversionError


class Salary:
    """Класс для работы с зарплатой"""

    converter = ConstantsCurrency()

    def __init__(self, salary: dict[str, Any]) -> None:
        """Инициализация экземпляра класса"""
        self.s_from = salary["from"] if salary.get("from") else 0
        self.s_to = salary["to"] if salary.get("to") else 0
        self.currency = salary["currency"] if salary.get("currency") else "RUR"
        self.converted = True  # Флаг удачной конвертации

    def __str__(self) -> str:
        """Строковое представление зарплаты"""
        # Оригинальные параметры
        salary_from = f"от {self.s_from} " if self.s_from else ""
        salary_to = f"до {self.s_to} " if self.s_to else ""
        ending = f"{self.currency}" if self.s_from or self.s_to else "Не указана"
        # Конвертированные параметры
        salary_from_ = f"от {self.s_from_converted} " if self.s_from else ""
        salary_to_ = f"до {self.s_to_converted} " if self.s_to else ""
        ending_ = f"{self.converter.currency_base}" if self.s_from or self.s_to else ""
        # На случай не удачной конвертации
        if self.converted:
            if self.currency == self.converter.currency_base:
                converted_string = ""  # Прячем расшифровку(дублирование)
            else:
                converted_string = f"({salary_from_}{salary_to_}{ending_})"
        else:
            converted_string = "(Не удалось конвертировать)"
        return f"{salary_from}{salary_to}{ending} {converted_string}"

    @property
    def s_from_converted(self) -> float:
        """Геттер нижней границы зарплаты с учетом валюты"""
        try:
            return self.converter.conversion(self.s_from, self.currency)
        except ConversionError:
            self.converted = False
            return float(self.s_from)

    @property
    def s_to_converted(self) -> float:
        """Геттер верхней границы зарплаты с учетом валюты"""
        try:
            return self.converter.conversion(self.s_to, self.currency)
        except ConversionError:
            self.converted = False
            return float(self.s_to)

    @property
    def salary_value(self) -> float:
        """Геттер размера зарплаты для сравнений с учетом валюты"""
        # В приоритете нижняя граница
        return self.s_from_converted if self.s_from else self.s_to_converted

    def to_dict(self) -> dict[str, Any]:
        """Возвращает свои атрибуты в виде словаря"""
        self_dict = {}
        self_dict["from"] = self.s_from
        self_dict["to"] = self.s_to
        self_dict["currency"] = self.currency
        return self_dict
