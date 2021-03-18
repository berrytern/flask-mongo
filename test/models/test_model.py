from bson.objectid import ObjectId
import pytest

@pytest.mark.parametrize("password",["Sa2421"])
@pytest.mark.parametrize("username",["joao","maria"])
def test_create_user(usermodel,username,password):
    print(usermodel.collection)
    response=usermodel.create(username,password)
    assert isinstance(response.inserted_id,ObjectId)

@pytest.mark.parametrize("username",["joao","maria"])
def test_find_user(usermodel,username):
    response=usermodel.find_all(username)
    assert response.count()==1

@pytest.mark.parametrize("username",["joao","maria"])
def test_find_one_user(usermodel,username):
    response=usermodel.find_one(username)
    assert  isinstance(response['_id'],ObjectId)

@pytest.mark.parametrize("password",["Sa2421"])
@pytest.mark.parametrize("username",["joao","maria"])
def test_update_user(usermodel,username,password):
    response=usermodel.update(username,password)
    assert response.raw_result['updatedExisting']

@pytest.mark.parametrize("username",["joao","maria"])
def test_delete_user(usermodel,username):
    response=usermodel.delete(username)
    assert response.deleted_count == 1