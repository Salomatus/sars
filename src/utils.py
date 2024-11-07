from src.vacancies import Vacancy


def get_top_n() -> int:
    """Функция получает у пользователя число топ N"""
    while True:
        try:
            return int(input("Введите количество вакансий для вывода в топ N: "))
        except TypeError:
            pass


def get_salary_range() -> tuple[int, int]:
    """Функция получает у пользователя диапазон зарплат"""
    while True:
        salary_range = input("Введите через пробел диапазон зарплат: ").split()
        try:
            return int(salary_range[0]), int(salary_range[1])
        except Exception:
            pass


def filter_vacancies(
    vacancies: list[Vacancy], filter_words: list[str], salary_range: tuple[int, int]
) -> list[Vacancy]:
    """Функция фильтрует список вакансий по ключевым словам и диапазону зарплат"""
    filtered_vacancies = []
    for vacancy in vacancies:
        if salary_range[0] <= vacancy <= salary_range[1] and vacancy.is_there_a_words(*filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies
