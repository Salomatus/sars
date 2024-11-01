from abc import ABC, abstractmethod

class Container(ABC):
    """ Abstract container """
    __slots__ = '_items'

    @abstractmethod
    def filtered_by(self, keyword: str):
        """ Filters data by keyword"""
        pass

    @abstractmethod
    def ranged(self):
        """ Sorts vacancies by salary """
        pass

    @abstractmethod
    def __init__(self):
        """ Constructor """
        pass

    @abstractmethod
    def get_top_n(self, n: int):
        """ Return first n values """
        pass

    @abstractmethod
    def add_item(self, item):
        """ Adds an element to the container """
        pass

    @abstractmethod
    def remove_item(self, item):
        """ Removes an element from the container """
        pass

    @abstractmethod
    def __iter__(self):
        """ Method to support iteration over a container """
        pass

    @abstractmethod
    def __len__(self):
        """ Returns a quantity of items in container """
        pass

    @abstractmethod
    def __contains__(self, item):
        """ Check if item in container """
        pass

    @abstractmethod
    def __str__(self):
        """ Print data in clear format """
        pass
