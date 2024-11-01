from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """ Adds vacancy to storage """
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Returns vacancies from storage """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """ Delete Vacancy from storage """
        pass
