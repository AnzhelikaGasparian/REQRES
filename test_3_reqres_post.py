import pytest
import requests
import allure
from datetime import datetime

my_id = 0

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Create Suite')
@allure.title('Validate Reqres Create User API')
@allure.description('This test case verifies the creation of a user via the Reqres Create User API and validates the response structure.')
@allure.severity(allure.severity_level.BLOCKER)
def test_reqres_create():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a user'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 201'):
        assert response.status_code == 201, f'Expected status code to be 201, but got {response.status_code}'

    res_data = response.json()

    with allure.step('Verify the response contains "name" key and matches the input data'):
        assert 'name' in res_data, 'Expected "name" key in the response'
        assert len(res_data['name']) > 0, 'Expected "name" to have a value'
        assert data['name'] == res_data['name'], f'Expected name to be {data["name"]}, but got {res_data["name"]}'

    with allure.step('Verify the response contains "job" key and matches the input data'):
        assert 'job' in res_data, 'Expected "job" key in the response'
        assert len(res_data['job']) > 0, 'Expected "job" to have a value'
        assert data['job'] == res_data['job'], f'Expected job to be {data["job"]}, but got {res_data["job"]}'

    with allure.step('Verify the response contains "id" key'):
        assert 'id' in res_data, 'Expected "id" key in the response'

    with allure.step('Verify the response contains "createdAt" key and has a valid timestamp'):
        assert 'createdAt' in res_data, 'Expected "createdAt" key in the response'
        assert len(res_data['createdAt']) > 0, 'Expected "createdAt" to have a value'
        try:
            datetime.fromisoformat(res_data['createdAt'].replace('Z', '+00:00'))
        except ValueError:
            assert False, f'"createdAt" is not in a valid ISO 8601 format: {res_data["createdAt"]}'

    with allure.step('Attach the response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

    global my_id
    my_id = res_data['id']