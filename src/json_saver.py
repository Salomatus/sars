import json

from src.vacancy import Vacancy
from src.vacancy_container import VacancyContainer
from src.vacancy_saver import VacancySaver


class JSONSaver(VacancySaver):
    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """ Добавляет вакансию в файл """
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # using getattr bc Vacancy described with __slots__
        vacancy_dict = {attr: getattr(vacancy, attr) for attr in vacancy.__slots__}
        data.append(vacancy_dict)

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        vacancy_list = Vacancy.cast_to_object_list(data)

        return VacancyContainer(vacancy_list)

    def delete_vacancy(self, vacancy: Vacancy):
        pass
