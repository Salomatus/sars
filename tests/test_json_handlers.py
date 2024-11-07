import pytest

from src.json_handlers import HandlerHH


# Фикстура JSON данных hh.ru (урезанная)
@pytest.fixture
def hh_json() -> list[dict]:
    return [
        {
            "id": "001",
            "name": "Наименование",
            "area": {"id": "002", "name": "Город", "url": "https://api.hh.ru/area/"},
            "salary": {"from": 50000, "to": 90000, "currency": "RUR"},
            "alternate_url": "https://hh.ru/vacancy/",
            "employer": {"id": "003", "name": "Работодатель", "url": "https://api.hh.ru/employers/"},
            "snippet": {"requirement": "Требования", "responsibility": "Обязанности"},
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
        },
    ]


# Фикстура унифицированных  JSON данных
@pytest.fixture
def converted_json() -> list[dict]:
    return [
        {
            "name": "Наименование",
            "employer": "Работодатель",
            "area": "Город",
            "requirement": "Требования",
            "responsibility": "Обязанности",
            "experience": "От 3 до 6 лет",
            "schedule": "Полный день",
            "employment": "Полная занятость",
            "url": "https://hh.ru/vacancy/",
            "salary": {"from": 50000, "to": 90000, "currency": "RUR"},
        },
    ]


# Тест конвертера структуры JSON
def test_converter(hh_json: list[dict], converted_json: list[dict]) -> None:
    json_handler = HandlerHH()
    assert json_handler.converter(hh_json) == converted_json
