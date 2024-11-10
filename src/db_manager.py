from typing import Any

import psycopg2


class DBManager:
    """Класс для работы с базами данных PostgresSQL"""

    def __init__(self, db_name: str, **params: Any) -> None:
        """Инициализация экземпляра класса"""
        self.db_name = db_name
        self.__params = params

    def get_companies_and_vacancies_count(self) -> Any:
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with psycopg2.connect(dbname=self.db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT employers.name, COUNT(vacancies.vacancy_id) FROM
                        employers INNER JOIN vacancies USING (employer_id)
                        GROUP BY employer_id
                        ORDER BY COUNT(*) DESC"""
                )
                result = cur.fetchall()
        return result

    def get_all_vacancies(self) -> Any:
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        with psycopg2.connect(dbname=self.db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT vacancies.name, salary_from, currency, employers.name, url
                        FROM employers INNER JOIN vacancies USING(employer_id)
                        ORDER BY salary_from DESC"""
                )
                result = cur.fetchall()
        return result

    def get_avg_salary(self) -> int:
        """Получает среднюю зарплату по вакансиям"""
        with psycopg2.connect(dbname=self.db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT AVG(salary_to) FROM vacancies""")
                result = cur.fetchall()
        return int(result[0][0])

    def get_vacancies_with_higher_salary(self) -> Any:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(dbname=self.db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT vacancies.name, salary_from, currency, employers.name, url
                        FROM employers INNER JOIN vacancies USING(employer_id)
                        WHERE salary_from > (SELECT AVG(salary_to) FROM vacancies)
                        ORDER BY salary_from DESC"""
                )
                result = cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, key_word: str) -> Any:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        with psycopg2.connect(dbname=self.db_name, **self.__params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT vacancies.name, salary_from, currency, employers.name, url
                    FROM employers INNER JOIN vacancies USING(employer_id)"""
                    f"WHERE LOWER(vacancies.name) LIKE '%{key_word.lower()}%'"
                    "ORDER BY salary_from DESC"
                )
                result = cur.fetchall()
        return result
