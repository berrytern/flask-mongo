import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/test')]
import pytest
from src.config.db import db
from src.models.user import UserModel as User


@pytest.fixture(scope='session', autouse=True)
def db_connection():
    db.drop_collection("users")
    yield 
    db.drop_collection("users")
@pytest.fixture()
def usermodel():
    yield User()