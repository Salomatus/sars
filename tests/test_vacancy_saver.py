import pytest

from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer

def test_add_item(vacancy_container):
    new_vacancy = Vacancy("Tester", "http://example.com/4", 55000, 75000, "USD")
    vacancy_container.add_item(new_vacancy)
    assert new_vacancy in vacancy_container

def test_remove_item(vacancy_list, vacancy_container):
    vacancy_to_remove = vacancy_list[0]
    vacancy_container.remove_item(vacancy_to_remove)
    assert vacancy_to_remove not in vacancy_container

def test_filtered_by(vacancy_container, vacancy_list):
    filtered_container = vacancy_container.filtered_by("Dev")
    assert len(filtered_container) == 1
    assert filtered_container._items[0].name == "Developer"

def test_ranged(vacancy_container):
    ranged_container = vacancy_container.ranged()
    assert ranged_container._items[0].salary_from == 40000
    assert ranged_container._items[-1].salary_from == 60000

def test_get_top_n(vacancy_container):
    top_n_container = vacancy_container.get_top_n(2)
    assert len(top_n_container) == 2
    assert top_n_container._items[0].name == "Developer"
    assert top_n_container._items[1].name == "Designer"

def test_from_list():
    new_vacancies = [
        Vacancy("Tester", "http://example.com/4", 55000, 75000, "USD"),
        Vacancy("Analyst", "http://example.com/5", 65000, 85000, "USD")
    ]
    new_container = VacancyContainer()
    new_container.from_list(new_vacancies)
    assert len(new_container) == 2
    assert new_container._items[0].name == "Tester"
    assert new_container._items[1].name == "Analyst"


def test_vacancy_container_eq(vacancy_container, vacancy_list):
    equal_container = VacancyContainer(vacancy_list)
    non_equal_container = VacancyContainer(vacancy_list[::-1])
    assert vacancy_container == equal_container
    assert vacancy_container != non_equal_container
