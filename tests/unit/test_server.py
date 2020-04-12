
from unittest.mock import patch, Mock


class TestServer():
    @staticmethod
    def test_home(test_client):
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Hello Ram' in response.data


