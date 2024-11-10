from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.services_api import HeadHunterAPI


@pytest.fixture
def requests_get_return_value() -> dict[str, Any]:
    """Фикстура значения, возвращаемого запросом requests.get"""
    return {
        "id": "001",
        "type": "company",
        "name": "HeadHunter",
        "area": {"name": "City"},
        "site_url": "http://hh.ru",
        "industries": [{"id": "1", "name": "industry"}],
        "items": [
            {
                "id": "002",
                "employer": {"id": "001", "name": "HeadHunter"},
                "name": "Python developer",
                "alternate_url": "http://hh.ru/vacancies/002",
                "schedule": {"name": "График"},
                "employment": {"name": "Полная занятость"},
                "salary": {"from": 50000, "to": 100000, "currency": "RUR"},
            }
        ],
        "pages": 1,
    }


def test_init_head_hunter_class() -> None:
    """Тест инициализации экземпляра класса HeadHunterAPI"""
    hh_parser = HeadHunterAPI()
    assert hh_parser.employers == []
    assert hh_parser.vacancies == []
    assert hh_parser.industries == []
    assert hh_parser.employer_industry == []


@patch("requests.get")
def test_load_data(get_mock: Mock, requests_get_return_value: dict[str, Any]) -> None:
    """Тест загрузки данных для заполнения таблиц"""
    get_mock.return_value.status_code = 200
    get_mock.return_value.json.return_value = requests_get_return_value
    hh_parser = HeadHunterAPI()
    hh_parser.load_data(["001"])
    assert hh_parser.employers == [
        {"employer_id": "001", "type": "company", "name": "HeadHunter", "area": "City", "site_url": "http://hh.ru"}
    ]
    assert hh_parser.vacancies == [
        {
            "vacancy_id": "002",
            "employer_id": "001",
            "name": "Python developer",
            "url": "http://hh.ru/vacancies/002",
            "schedule": "График",
            "employment": "Полная занятость",
            "salary_from": 50000,
            "salary_to": 100000,
            "currency": "RUR",
        }
    ]
    assert hh_parser.industries == [{"industry_id": "1", "name": "industry"}]
    assert hh_parser.employer_industry == [{"employer_id": "001", "industry_id": "1"}]


@patch("requests.get")
def test_load_data_not_found(get_mock: Mock) -> None:
    """Тест загрузки пустых данных (данные не найдены или неверный запрос)"""
    get_mock.return_value.status_code = 400
    hh_parser = HeadHunterAPI()
    hh_parser.load_data(["001"])
    assert hh_parser.employers == []
    assert hh_parser.vacancies == []
    assert hh_parser.industries == []
    assert hh_parser.employer_industry == []


@patch("requests.get")
def test_load_data_error(get_mock: Mock) -> None:
    """Тест ошибки загрузки данных (например нет интернета)"""
    get_mock.side_effect = requests.exceptions.RequestException
    hh_parser = HeadHunterAPI()
    hh_parser.load_data(["001"])
    assert hh_parser.employers == []
    assert hh_parser.vacancies == []
    assert hh_parser.industries == []
    assert hh_parser.employer_industry == []
