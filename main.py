from src.config import config
from src.constants import DB_NAME, EMPLOYER_IDS, FILE_CONFIG, TABLES
from src.db_manager import DBManager
from src.db_saver import DataBaseSaver
from src.services_api import HeadHunterAPI

print("Получение данных о компаниях и их вакансиях...")
hh_parser = HeadHunterAPI()
hh_parser.load_data(EMPLOYER_IDS)
print("Создание базы данных и таблиц в ней...")
params = config(FILE_CONFIG)
db_saver = DataBaseSaver(DB_NAME, **params)
db_saver.create_tables(TABLES)
print("Сохранение данных о компаниях и их вакансиях в базу...")
db_saver.insert_data("employers", hh_parser.employers)
db_saver.insert_data("vacancies", hh_parser.vacancies)
db_saver.insert_data("industries", hh_parser.industries)
db_saver.insert_data("employer_industry", hh_parser.employer_industry)
print(f"Данные сохранены в БД {DB_NAME}\n")


def show_vacancies(vacancies: list[tuple]) -> None:
    """Функция выводит в консоль список вакансий"""
    if vacancies:
        for vacancy in vacancies:
            print(
                f"{vacancy[0]}. Зарплата: {str(vacancy[1]) + ' ' + vacancy[2] if vacancy[1] else 'Не указана'}.\n"
                f"Компания: {vacancy[3]}. ({vacancy[4]})\n"
            )
    else:
        print("Нет результатов!\n")


def main() -> None:
    """Основная логика программы"""
    db_manager = DBManager(DB_NAME, **params)
    while True:
        print(
            "Выберите действие:\n"
            "1. Вывести список всех компаний и количество вакансий у каждой\n"
            "2. Вывести информацию по всем вакансиям\n"
            "3. Показать среднюю зарплату по всем вакансиям\n"
            "4. Вывести список всех вакансий, у которых зарплата выше средней\n"
            "5. Поиск вакансий по ключевому слову в названии"
        )
        answer = input(">>")
        if answer == "1":
            result = db_manager.get_companies_and_vacancies_count()
            print("Список всех компаний:")
            for company in result:
                print(f"{company[0]}. Вакансий: {company[1]}")
            print()
        elif answer == "2":
            result = db_manager.get_all_vacancies()
            print("Список всех вакансий:")
            show_vacancies(result)
        elif answer == "3":
            avg_salary = db_manager.get_avg_salary()
            print(f"Средняя зарплата по вакансиям: {avg_salary}\n")
        elif answer == "4":
            result = db_manager.get_vacancies_with_higher_salary()
            print("Список вакансий с зарплатой выше средней:")
            show_vacancies(result)
        elif answer == "5":
            question = input("Введите запрос: ")
            result = db_manager.get_vacancies_with_keyword(question)
            print(f"Список вакансий со словом «{question.title()}» в названии:")
            show_vacancies(result)
        else:
            print("Нет такого пункта!\n")
            continue
        if input("Продолжить (да/нет)?\n>>").lower() in ("y", "yes", "д", "да", ""):
            continue
        else:
            print("Конец программы")
            break


if __name__ == "__main__":
    main()
