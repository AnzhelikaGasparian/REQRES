import pytest
import requests
import allure
from datetime import datetime
from test_3_reqres_post import my_id

@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Partial Update User Suite')
@allure.title('Validate Partial Update of User via Reqres API')
@allure.description('This test case verifies the partial update of a user via the Reqres API and validates the response structure including the "updatedAt" field.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_partial_update():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send PATCH request to partially update user'):
        response = requests.patch(
            f'https://reqres.in/api/users/{my_id}',
            json=data,
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code to be 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "name" key and matches the input data'):
        assert 'name' in response_data, 'Expected "name" key in the response'
        assert len(response_data['name']) > 0, 'Expected "name" to have a value'
        assert data['name'] == response_data['name'], f'Expected name to be {data["name"]}, but got {response_data["name"]}'

    with allure.step('Verify the response contains "job" key and matches the input data'):
        assert 'job' in response_data, 'Expected "job" key in the response'
        assert len(response_data['job']) > 0, 'Expected "job" to have a value'
        assert data['job'] == response_data['job'], f'Expected job to be {data["job"]}, but got {response_data["job"]}'

    with allure.step('Verify the response contains "updatedAt" key and has a valid timestamp'):
        assert 'updatedAt' in response_data, 'Expected "updatedAt" key in the response'
        assert len(response_data['updatedAt']) > 0, 'Expected "updatedAt" to have a value'
        try:
            datetime.fromisoformat(response_data['updatedAt'].replace('Z', '+00:00'))
        except ValueError:
            assert False, f'"updatedAt" is not in a valid ISO 8601 format: {response_data["updatedAt"]}'

    with allure.step('Attach the response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)