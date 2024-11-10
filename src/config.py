import os
from configparser import ConfigParser

ROOT = os.path.join(os.path.dirname(__file__), "..")


def config(file_name: str = "database.ini", section: str = "postgresql") -> dict[str, str]:
    """Чтение файла конфигурации с параметрами подключения к Data Base"""
    parser = ConfigParser()
    parser.read(os.path.join(ROOT, file_name))
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f"Секция {section} не содержится в файле {file_name}.")
    return db_config
