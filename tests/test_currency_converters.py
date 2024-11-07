import pytest

from src.currency_converters import ConstantsCurrency
from src.errors import ConversionError


# Тест инициализации класса
@pytest.mark.parametrize("currency", [("USD"), ("EUR"), ("RUR"), ("KZT")])
def test_constants_currency_init(currency: str) -> None:
    object = ConstantsCurrency(currency)
    assert object.currency_base == currency


# Тест метода конвертации
@pytest.mark.parametrize("currency, result", [("USD", 87.85), ("EUR", 95.68), ("RUR", 1)])
def test_constants_currency_conversion(currency: str, result: float) -> None:
    object = ConstantsCurrency()
    assert object.currency_base == "RUR"
    assert object.conversion(1, currency) == result


# Тест ошибки конвертации
def test_constants_currency_error() -> None:
    object = ConstantsCurrency()
    with pytest.raises(ConversionError, match="Неизвестная валюта"):
        object.conversion(1, "No currency")
