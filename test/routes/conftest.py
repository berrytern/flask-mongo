import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/test')]
import pytest
from src.config.db import db
from src.app import app


@pytest.fixture()
def api():
    yield app.test_client()
@pytest.fixture(scope="session", autouse=True)
def clean_db():
    print("cleaning db")
    db.drop_collection("users")
    yield
    print("cleaning db")
    db.drop_collection("users")
