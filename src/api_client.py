from abc import ABC, abstractmethod

from requests import Response


class APIClient(ABC):
    """ Abstract API client """
    @abstractmethod
    def get_info(self):
        pass
