from src.currency_converters import ConstantsCurrency
from src.json_handlers import HandlerHH
from src.salary import Salary
from src.services_api import HeadHunterAPI
from src.services_file import JSONWorker
from src.utils import filter_vacancies, get_salary_range, get_top_n
from src.vacancies import Vacancy

FAVOURITES = "Favourites"  # Имя файла для сохранения/чтения
CURRENCY = "RUR"  # Валюта пользователя

# Создание экземпляра класса конвертера валют
currency_converter = ConstantsCurrency(CURRENCY)
# Добавление конвертера к классу зарплаты
Salary.converter = currency_converter
# Создание экземпляра класса файлового обработчика
file_worker = JSONWorker(FAVOURITES)
# Создание экземпляра класса JSON обработчика
json_handler = HandlerHH()
# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI(json_handler)


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    print("Добро пожаловать в программу поиска работы.")
    search_query = input("Введите поисковый запрос: ")
    top_n = get_top_n()
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = get_salary_range()

    print(f"Загрузка вакансий по запросу «{search_query}»...")
    hh_vacancies = hh_api.load_vacancies(search_query)
    print(f"Загружено вакансий: {len(hh_vacancies)}")
    # Преобразование набора данных из JSON в список объектов
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    print("Фильтрация по ключевым словам и зарплате...")
    filtered_vacancies = filter_vacancies(vacancies, filter_words, salary_range)
    print(f"Соответствует критериям: {len(filtered_vacancies)}")
    print("Сортировка по зарплате...")
    filtered_vacancies.sort(reverse=True)
    top_vacancies = filtered_vacancies[:top_n]
    # Добавление первых топ N вакансий в файл
    for vacancy in top_vacancies:
        file_worker.add_vacancy(vacancy)
    print(f"Первые {len(top_vacancies)} добавлены в файл {FAVOURITES}.json")

    if input("Открыть файл для просмотра? (да/нет): ").lower() in ("да", "д", "yes", "y"):
        vacancies_file = file_worker.vacancies
        show_vacancy(vacancies_file)
    print("\nКонец программы")


def show_vacancy(vacancies: list[Vacancy]) -> None:
    """Функция вывода вакансий в консоль и выбора действий"""
    print(f"Всего вакансий: {len(vacancies)}\n")
    counter = 1
    for vacancy in vacancies:
        print(str(counter) + ")", vacancy)
        counter += 1
        action = input("1: Удалить, 2: Выйти, Enter: Дальше >>")
        if action == "1":
            print(file_worker.delete_vacancy(vacancy), "\n")
        elif action == "2":
            break
        else:
            print("Пропущено\n")


if __name__ == "__main__":
    user_interaction()
