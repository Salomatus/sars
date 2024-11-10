from typing import Any

import psycopg2
import pytest

from src.config import config
from src.constants import FILE_CONFIG
from src.db_saver import DataBaseSaver


@pytest.fixture
def params() -> dict[str, Any]:
    """Фикстура параметров подключения к БД"""
    return config(FILE_CONFIG)


@pytest.fixture
def tables() -> dict[str, tuple]:
    """Фикстура тестовой таблицы"""
    return {"test_table": ("test_column1 INT PRIMARY KEY", "test_column2 VARCHAR(10)")}


@pytest.fixture
def data() -> list[dict]:
    """Фикстура тестовых данных"""
    return [{"test_column1": 10, "test_column2": "TEXT"}]


def test_db_create(params: dict[str, Any]) -> None:
    """Тест создания базы данных"""
    DataBaseSaver("test_db", **params)
    with psycopg2.connect(dbname="test_db", **params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT datname FROM pg_database WHERE datname='test_db'")
            result = cur.fetchone()
    conn.close()
    assert result[0] == "test_db"


def test_create_tables(tables: dict[str, tuple], params: dict[str, Any]) -> None:
    """Тест создания таблиц"""
    db_saver = DataBaseSaver("test_db", **params)
    db_saver.create_tables(tables)
    with psycopg2.connect(dbname="test_db", **params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
            result = cur.fetchone()
    conn.close()
    assert result[0] == "test_table"


def test_insert_data(data: list[dict], params: dict[str, Any]) -> None:
    """Тест заполнения таблиц"""
    db_saver = DataBaseSaver("test_db", **params)
    db_saver.insert_data("test_table", data)
    db_saver.insert_data("test_table", data)  # Проверка исключения дублирования
    with psycopg2.connect(dbname="test_db", **params) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test_table")
            result = cur.fetchone()
    conn.close()
    assert result == (10, "TEXT")


def test_drop_test_db(params: dict[str, Any]) -> None:
    """Удаление тестовой базы данных"""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("DROP DATABASE test_db")
    cur.close()
    conn.close()
