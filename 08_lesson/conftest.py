import pytest
from api_client import YougileAPI

BASE_URL = "https://yougile.com"
TOKEN = ""



@pytest.fixture(scope="session")
def api():
    return YougileAPI(BASE_URL, TOKEN)
