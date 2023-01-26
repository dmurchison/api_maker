import pytest



async def test_delete_user_success(testing_app, valid_user_delete_id):
    response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert response.status_code == 200


def test_delete_user_failure(testing_app, valid_user_delete_id):
    response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert response.status_code == 200

    second_response = testing_app.delete(f"/user/{valid_user_delete_id}")
    assert second_response.status_code == 404
    assert second_response.json() == {'message': "User ain't real"}
    

