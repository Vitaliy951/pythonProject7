import pytest
from unittest.mock import patch, Mock
from src.hh_api import HeadHunterAPI


class TestHeadHunterAPI:
    @patch('requests.get')
    def test_connect_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        assert api.connect() is True

    @patch('requests.get')
    def test_get_vacancies(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'items': [{'name': 'Python Developer'}]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        result = api.get_vacancies('Python')
        assert len(result) == 1
        assert 'Python Developer' in result[0]['name']
