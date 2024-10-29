import pytest

from src.vacancy import Vacancy

def test_vacancy_initialization(vacancy_1):
    assert vacancy_1.name == "Software Developer"
    assert vacancy_1.url == "https://example.com/job/1"
    assert vacancy_1.salary_from == 5000
    assert vacancy_1.salary_to == 10000
    assert vacancy_1.salary_currency == "USD"

def test_vacancy_equality(vacancy_1, vacancy_2, vacancy_3, vacancy_4):
    assert vacancy_1 == vacancy_1
    assert vacancy_1 != vacancy_2


def test_vacancy_comparison(vacancy_1, vacancy_2, vacancy_3, vacancy_4):

    assert vacancy_1 < vacancy_4
    assert vacancy_1 <= vacancy_2
    assert vacancy_4 > vacancy_1
    assert vacancy_2 >= vacancy_1
    assert not vacancy_4 < vacancy_1
    assert not vacancy_3 <= vacancy_1
    assert not vacancy_3 > vacancy_4
    assert not vacancy_1 >= vacancy_3

def test_cast_to_object_list():
    vacancies_data = [
        {
            "name": "Software Developer",
            "url": "https://example.com/job/1",
            "salary":
                {
                    "from": 5000,
                    "to": 10000,
                    "currency": "USD"
                }
        },
        {
            "name": "Data Scientist",
            "url": "https://example.com/job/2",
            "salary":
                {
                    "from": 6000,
                    "to": 12000,
                    "currency": "USD"
                }
        },
    ]
    vacancies = Vacancy.cast_to_object_list(vacancies_data)

    assert len(vacancies) == 2
    assert vacancies[0].name == "Software Developer"
    assert vacancies[0].url == "https://example.com/job/1"
    assert vacancies[0].salary_from == 5000
    assert vacancies[0].salary_to == 10000
    assert vacancies[0].salary_currency == "USD"
    assert vacancies[1].name == "Data Scientist"
    assert vacancies[1].url == "https://example.com/job/2"
    assert vacancies[1].salary_from == 6000
    assert vacancies[1].salary_to == 12000
    assert vacancies[1].salary_currency == "USD"

def test_valid_str():
    assert Vacancy.valid_str("Test") == "Test"
    assert Vacancy.valid_str("") == "Data not found"
    assert Vacancy.valid_str(None) == "Data not found"

def test_valid_value():
    assert Vacancy.valid_value(100) == 100
    assert Vacancy.valid_value(0) == 0
    assert Vacancy.valid_value(None) == 0
    assert Vacancy.valid_value("100") == 0
