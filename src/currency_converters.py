from abc import ABC, abstractmethod

from src.errors import ConversionError
from src.rates import RATES


class CurrencyConverter(ABC):
    """Шаблон для классов конвертации валюты"""

    @abstractmethod
    def __init__(self, currency_base: str) -> None:
        """Констуктор сущности класса конвертации валюты"""
        self.currency_base = currency_base

    @abstractmethod
    def conversion(self, amount: int, currency: str) -> float:
        """Конвертация переданной суммы в базовую валюту"""
        pass


class ConstantsCurrency(CurrencyConverter):
    """Класс конвертации вылюты по константным значениям
    Можно заменить на (или добавить) класс с логикой API запросов"""

    def __init__(self, currency_base: str = "RUR") -> None:
        """Констуктор сущности класса конвертации валюты"""
        super().__init__(currency_base)

    def conversion(self, amount: int, currency: str) -> float:
        """Конвертация переданной суммы в базовую валюту"""
        try:
            return round(amount * RATES[currency] / RATES[self.currency_base], 2)
        except KeyError:
            raise ConversionError("Неизвестная валюта")
