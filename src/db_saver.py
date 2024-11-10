from typing import Any

import psycopg2


class DataBaseSaver:
    """Класс для создания базы данных и таблиц в ней"""

    def __init__(self, db_name: str, **params: Any) -> None:
        """Инициализация экземпляра класса"""
        self.db_name = db_name
        self.__params = params
        self.create_db()

    def create_db(self) -> None:
        """Создание базы данных, если она не существует"""
        conn = psycopg2.connect(dbname="postgres", **self.__params)
        conn.autocommit = True
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE DATABASE {self.db_name}")
        except psycopg2.errors.DuplicateDatabase:
            pass
        finally:
            cur.close()
            conn.close()

    def create_tables(self, tables: dict[str, tuple]) -> None:
        """Создание таблиц в базе данных"""
        conn = psycopg2.connect(dbname=self.db_name, **self.__params)
        with conn.cursor() as cur:
            # Удаление
            for table_name in list(tables.keys())[::-1]:
                cur.execute(f"DROP TABLE IF EXISTS {table_name}")
            # Создание
            for table_name, table_columns in tables.items():
                cur.execute(f"CREATE TABLE {table_name}({', '.join(table_columns)})")
        conn.commit()
        conn.close()

    def insert_data(self, table_name: str, data: list[dict]) -> None:
        """Заполнение таблиц данными"""
        conn = psycopg2.connect(dbname=self.db_name, **self.__params)
        conn.autocommit = True

        for record in data:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        f"INSERT INTO {table_name} ({', '.join([key for key in record.keys() if record.get(key)])}) "
                        f"VALUES {tuple(value for value in record.values() if value)}"
                    )
                except psycopg2.errors.UniqueViolation:
                    continue

        conn.close()
