from abc import ABC, abstractmethod

class VacancyBase(ABC):
    """ Represents a Vacancy """
    __slots__ = ('name', 'url', 'salary_from', 'salary_to', 'salary_currency')
    # MAGIC METHODS
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    # CLASSMETHODS
    @classmethod
    @abstractmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list[object]:
        pass
