from src.hh_api_client import HHAPIClient

def test_load_vacancies_success(mock_requests):
    client = HHAPIClient()
    mock_requests.get(HHAPIClient.BASE_URL, json={
        'items': [{'id': 1, 'name': 'Python Developer'}],
        'pages': 1
    })
    client.load_vacancies('Python developer')
    assert len(client.vacancies) == 1
    assert client.vacancies[0]['name'] == 'Python Developer'

def test_load_vacancies_error(mock_requests):
    client = HHAPIClient()
    mock_requests.get(HHAPIClient.BASE_URL, status_code=500)
    client.load_vacancies('Python developer')
    assert len(client.vacancies) == 0

def test_get_info(mock_requests):
    client = HHAPIClient()
    mock_requests.get(HHAPIClient.BASE_URL, json={
        'items': [{'id': 1, 'name': 'Python Developer'}],
        'pages': 1
    })
    client.load_vacancies('Python developer')
    info = client.get_info()
    assert len(info) == 1
    assert info[0]['name'] == 'Python Developer'
