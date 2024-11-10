# Файл с данными для  подключения к БД
FILE_CONFIG = "database.ini"

# Имя БД для сохранения полученных данных
DB_NAME = "head_hunter_data"

# Список таблиц с описанием колонок
TABLES = {
    "employers": (
        "employer_id VARCHAR(20) PRIMARY KEY",
        "type VARCHAR(20) NOT NULL",
        "name VARCHAR(100) NOT NULL",
        "area VARCHAR(50) NOT NULL",
        "site_url TEXT",
    ),
    "vacancies": (
        "vacancy_id VARCHAR(20) PRIMARY KEY",
        "employer_id VARCHAR(20) REFERENCES employers(employer_id)",
        "name VARCHAR(100) NOT NULL",
        "url VARCHAR(100) NOT NULL",
        "schedule VARCHAR(20) NOT NULL",
        "employment VARCHAR(20) NOT NULL",
        "salary_from INT",
        "salary_to INT",
        "currency VARCHAR(3)",
    ),
    "industries": ("industry_id VARCHAR(20) PRIMARY KEY", "name VARCHAR(255) NOT NULL"),
    "employer_industry": (
        "employer_id VARCHAR(20) REFERENCES employers(employer_id)",
        "industry_id VARCHAR(20) REFERENCES industries(industry_id)",
    ),
}

# Список id компаний для запросов
EMPLOYER_IDS = [
    "1918903",  # Decart IT-production
    "1054992",  # I Like IT
    "5591530",  # IT-hunters
    "2716772",  # Internet Media Gid
    "1289095",  # Агентство Интернет-рекламы Контраст
    "779741",  # Интернет Логистика
    "572985",  # Online Market Intelligence (OMI)
    "2036165",  # Камаз Центр
    "3663900",  # МАГНИТ
    "852361",  # Ростелеком - Центры обработки данных
]
