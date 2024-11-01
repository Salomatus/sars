import json
from src.json_saver import JSONSaver

from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer
from tests.conftest import temp_file


def test_add_vacancy(json_saver, vacancy, temp_file):
    json_saver.add_vacancy(vacancy)

    with open(temp_file.name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    vacancy_dict = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
    assert vacancy_dict in data


def test_get_vacancies(vacancy_1, vacancy_2, json_saver):
    json_saver.add_vacancy(vacancy_1)
    json_saver.add_vacancy(vacancy_2)

    expected_container = VacancyContainer([vacancy_1, vacancy_2])

    assert json_saver.get_vacancies() == expected_container
