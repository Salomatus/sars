from abc import ABC, abstractmethod
import json
import os.path


class JSONVacancy(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        pass


class HHVacancy(JSONVacancy):
    """Класс для создания и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self):
        """Инициализатор класса"""
        self.file_name_save = 'data/suitable_vacancies.json'

    def safe_vacancy(self, stock_list):
        """Метод для сохранения данных о вакансиях в файл"""
        if stock_list is None:
            print("Вакансий с такими критериями не найдено")
        elif stock_list is not None:
            if os.path.exists(self.file_name_save):
                with open(self.file_name_save, 'r', encoding="utf-8") as file:
                    data = json.load(file)
                for i in stock_list:
                    if i not in data:
                        data.append(i)
                with open(self.file_name_save, 'w', encoding="utf-8") as file:
                    json.dump(data, file, indent=4,
                              ensure_ascii=False)
            else:
                with open(self.file_name_save, 'w', encoding="utf-8") as file:
                    json.dump(stock_list, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        """Метод для удаления не нужного файла"""
        pass
