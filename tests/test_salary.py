from typing import Any

import pytest

from src.salary import Salary

init_data = [
    ({"from": 1000, "to": 2000, "currency": "USD"}, 1000, 2000, "USD"),
    ({"from": 50000, "to": None, "currency": "RUR"}, 50000, 0, "RUR"),
    ({"to": 5000000, "currency": "KZT"}, 0, 5000000, "KZT"),
    ({}, 0, 0, "RUR"),
]

conversion_data = [
    ({"from": 1000, "to": 2000, "currency": "USD"}, 87850.0, 175700.0, 87850.0, True),
    ({"from": 50000, "to": None, "currency": "RUR"}, 50000.0, 0, 50000.0, True),
    ({"to": 300000, "currency": "Unicown"}, 0, 300000.0, 300000.0, False),
]

string_data = [
    ({"from": 1000, "to": 2000, "currency": "USD"}, "от 1000 до 2000 USD (от 87850.0 до 175700.0 RUR)"),
    ({"from": 50000, "to": None, "currency": "RUR"}, "от 50000 RUR "),
    ({"to": 300000, "currency": "Unicown"}, "до 300000 Unicown (Не удалось конвертировать)"),
    ({}, "Не указана "),
]

dict_data = [
    ({"from": 1000, "to": 2000, "currency": "USD"}, {"from": 1000, "to": 2000, "currency": "USD"}),
    ({"from": 50000, "to": None, "currency": "RUR"}, {"from": 50000, "to": 0, "currency": "RUR"}),
    ({"to": 300000, "currency": "Unicown"}, {"from": 0, "to": 300000, "currency": "Unicown"}),
    ({}, {"from": 0, "to": 0, "currency": "RUR"}),
]


# Тест инициализации класса
@pytest.mark.parametrize("salary_dict, from_, to_, currency", init_data)
def test_salary_init(salary_dict: dict[str, Any], from_: int, to_: int, currency: str) -> None:
    salary: Salary = Salary(salary_dict)
    assert salary.s_from == from_
    assert salary.s_to == to_
    assert salary.currency == currency
    assert salary.converted


# Тест использования конвертера валют
@pytest.mark.parametrize("salary_dict, from_converted, to_converted, value, converted", conversion_data)
def test_salary_conversion(
    salary_dict: dict[str, Any], from_converted: float, to_converted: float, value: float, converted: bool
) -> None:
    salary: Salary = Salary(salary_dict)
    assert salary.s_from_converted == from_converted
    assert salary.s_to_converted == to_converted
    assert salary.salary_value == value
    assert salary.converted == converted


# Тест строкового представления
@pytest.mark.parametrize("salary_dict, string", string_data)
def test_salary_string(salary_dict: dict[str, Any], string: str) -> None:
    salary: Salary = Salary(salary_dict)
    assert str(salary) == string


# Тест метода to_dict
@pytest.mark.parametrize("salary_dict, result", dict_data)
def test_salary_to_dict(salary_dict: dict[str, Any], result: dict[str, Any]) -> None:
    salary: Salary = Salary(salary_dict)
    assert salary.to_dict() == result
