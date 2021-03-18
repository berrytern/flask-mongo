import pytest
def login(api,password):
    token=api.post('/login',json={"username":"joao","password":password})
    return token.get_data(True).split('"')[1]

@pytest.mark.parametrize("status",[201,409])
def test_register(api,status):
    response = api.post('/register',json={"username":"joao","password":"right"})
    assert response.status_code == status

@pytest.mark.parametrize("cases",[("right",200),("false",401)])
def test_login(api,cases):
    response = api.post('/login',json={"username":"joao","password":cases[0]})
    assert response.status_code==cases[1]

@pytest.mark.parametrize("cases",[("right","right","new_pass",200),("new_pass","right","right",401)])
def test_update(api,cases):
    token=login(api, cases[0])
    response = api.put('/login',json={"password":cases[1],"new_password":cases[2]},headers={"Authorization":"Bearer "+token})
    assert response.status_code==cases[3]

def test_delete_user(api):
    token=login(api, "new_pass")
    response = api.delete('/login',json={"password":"right"},headers={"Authorization":"Bearer "+token})
    assert response.status_code==200