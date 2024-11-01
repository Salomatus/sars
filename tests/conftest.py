from tempfile import NamedTemporaryFile
from tkinter.ttk import Label

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer


# VACANCY TEST
@pytest.fixture
def vacancy_1():
    return  Vacancy(
        'Software Developer',
        'https://example.com/job/1',
        5000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/2',
        5000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_3():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/3',
        6000,
        10000,
        'USD'
    )


@pytest.fixture
def vacancy_4():
    return Vacancy(
        'Software Developer',
        'https://example.com/job/4',
        7000,
        11000,
        'USD'
    )

@pytest.fixture
def vacancy_5():
    return Vacancy(
        'Web Designer',
        'https://example.com/job/5',
        5000,
        11000,
        'EUR'
    )

# VACANCY CONTAINER
@pytest.fixture
def vacancy_list():
    return [
        Vacancy("Developer", "http://example.com/1", 50000, 70000, "USD"),
        Vacancy("Designer", "http://example.com/2", 40000, 60000, "USD"),
        Vacancy("Manager", "http://example.com/3", 60000, 80000, "USD")
    ]

@pytest.fixture
def vacancy_container(vacancy_list):
    return VacancyContainer(vacancy_list)


# HH API CLIENT

import pytest
import requests_mock

@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m


# JSONSaver TESTS

@pytest.fixture
def temp_file():
    temp_file = NamedTemporaryFile(delete=False, mode='w+t', encoding='utf-8')
    temp_file.write('[]')
    temp_file.seek(0)
    yield temp_file
    temp_file.close()


@pytest.fixture
def json_saver(temp_file):
    return JSONSaver(temp_file.name)


@pytest.fixture
def vacancy():
    return Vacancy(
        name="Python Developer",
        url="http://example.com/job/1",
        salary_from=5000,
        salary_to=6000,
        salary_currency="USD"
    )
