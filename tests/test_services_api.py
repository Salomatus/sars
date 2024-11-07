from typing import Any
from unittest.mock import Mock, patch

import pytest

from src.json_handlers import HandlerHH
from src.services_api import HeadHunterAPI


# Фикстура JSON данных hh.ru (урезанная)
@pytest.fixture
def responce_json() -> dict[str, Any]:
    return {
        "items": [
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
        ],
        "found": 1,
        "pages": 1,
        "page": 0,
        "per_page": 100,
    }


# Фикстура унифицированных  JSON данных
@pytest.fixture
def vacancies() -> list[dict]:
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


# Тест метода load_vacancies
@patch("requests.get")
def test_load_vacancies(mock_get: Mock, responce_json: dict[str, Any], vacancies: list[dict]) -> None:
    mock_get.return_value.json.return_value = responce_json
    json_handler = HandlerHH()
    hh_vacancies = HeadHunterAPI(json_handler)
    assert hh_vacancies.load_vacancies("text") == vacancies
    mock_get.assert_called_once()
