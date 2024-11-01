from src.abstract_container import Container
from src.vacancy import Vacancy

class VacancyContainer(Container):
    """ Contains vacancies, can be used to manipulate them"""
    __slots__ = ()

    def __init__(self, vacancies: list[Vacancy] | None=None):
        """ Constructor """
        if not vacancies:
            self._items = []
        elif all(isinstance(vacancy, Vacancy) for vacancy in vacancies):
            self._items = vacancies
        else:
            raise TypeError('All items in list must be Vacancy objects')

    def add_item(self, item):
        """ Adds an item to the container """
        if isinstance(item, Vacancy):
            self._items.append(item)
        else:
            raise TypeError('This container is only for Vacancies')

    def remove_item(self, item):
        """ Removes an item from the container """
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f'Item {repr(item)} not found in the container')

    # MAGIC METHODS
    def __eq__(self, other):
        """ Compare two VacancyContainer objects for equality """
        if not isinstance(other, VacancyContainer):
            return False
        return self._items == other._items

    def __iter__(self):
        """ Returns iterator from items """
        return iter(self._items)

    def __len__(self):
        """ Returns length of contained items"""
        return len(self._items)

    def __contains__(self, item):
        """ Check if an item is in a container """
        return item in self._items

    def __str__(self):
        """ Returns a string representation of an object """
        return f'{self.__class__.__name__}: contains {len(self)} vacancies'

    def __repr__(self):
        """ Returns an official string representation of an object """
        return str(self)

    def from_list(self, vacancies: list[Vacancy]):
        """ Construct container from list of objects """
        if all(isinstance(vacancy, Vacancy) for vacancy in vacancies):
            for vacancy in vacancies:
                self.add_item(vacancy)
        else:
            raise TypeError()

    def filtered_by(self, keyword: str):
        """ Filters data by keyword"""
        filtered_items = [item for item in self._items if
                          any(keyword in str(getattr(item, attr)) for attr in item.__slots__)]
        print(f"Filtered items: {filtered_items}")
        return VacancyContainer(filtered_items)

    def ranged(self):
        """ Sort data by salary"""
        def sort_by_salary(vacancy):
            """ Returns avg for salary range """
            return (vacancy.salary_from + vacancy.salary_to) / 2
        sorted_items = sorted(self._items, key=sort_by_salary)
        return VacancyContainer(sorted_items)

    def get_top_n(self, n: int):
        """ Return first n values """
        return VacancyContainer(self._items[:n])
