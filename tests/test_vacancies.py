import pytest

from src.vacancies import Vacancy


# Фикстура списка объектов вакансий
@pytest.fixture
def vacancies() -> list[Vacancy]:
    return Vacancy.cast_to_object_list(
        [
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
                "salary": {"from": 60000, "to": 90000, "currency": "RUR"},
            },
        ]
    )


# Тест методов сранения вакансий по зарплате
def test_cast_to_object_list(vacancies: list[Vacancy]) -> None:
    vacancy_1 = vacancies[0]
    vacancy_2 = vacancies[1]

    assert vacancy_1 < vacancy_2
    assert vacancy_1 < 60000
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_1 < "string"

    assert vacancy_1 <= vacancy_2
    assert vacancy_1 <= 50000.0
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_1 <= "string"

    assert vacancy_2 > vacancy_1
    assert vacancy_2 > 50000
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_2 > "string"

    assert vacancy_2 >= vacancy_1
    assert vacancy_2 >= 60000.0
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_2 >= "string"

    assert vacancy_1 != vacancy_2
    assert vacancy_1 != 60000
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_1 != "string"

    assert not vacancy_1 == vacancy_2
    assert vacancy_1 == 50000.0
    with pytest.raises(TypeError, match="Невозможно сравнить"):
        vacancy_1 == "string"


# Тест метода to_dict
def test_vacancy_to_dict(vacancies: list[Vacancy]) -> None:
    assert vacancies[0].to_dict() == {
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
    }


# Тест метода is_there_a_words
def test_vacancy_is_there_a_words(vacancies: list[Vacancy]) -> None:
    assert vacancies[0].is_there_a_words("требования")
    assert vacancies[1].is_there_a_words("обязанности")
    assert not vacancies[0].is_there_a_words("строка которой нет")
    assert vacancies[1].is_there_a_words("обязанности", "другое слово")


# Тест строкового представления вакансии
def test_vacancy_str(vacancies: list[Vacancy]) -> None:
    assert str(vacancies[1]) == (
        "Наименование. Зарплата: от 60000 до 90000 RUR \n"
        "График: Полный день, Занятость: Полная занятость, Опыт: От 3 до 6 лет\n"
        "Работодатель: Работодатель (Город)\n"
        "URL: https://hh.ru/vacancy/\n"
        "Требования:\n"
        "Требования\n"
        "Обязанности:\n"
        "Обязанности"
    )
