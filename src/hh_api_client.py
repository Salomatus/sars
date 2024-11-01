import requests

from src.api_client import APIClient


class HHAPIClient(APIClient):
    """ Represents client to fetch data from hh.ru """
    BASE_URL = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str):
        self.params['text'] = keyword
        while True:
            try:
                response = requests.get(self.BASE_URL, headers=self.headers, params=self.params)
                response.raise_for_status()  # Raise an error for bad status codes
                data = response.json()
                vacancies = data['items']
                self.vacancies.extend(vacancies)
                if self.params['page'] >= data['pages'] - 1:
                    break
                self.params['page'] += 1
            except requests.RequestException as e:
                print(f"Error fetching page {self.params['page']}: {e}")
                break  # Exit the loop on error

    def get_info(self):
        return self.vacancies
