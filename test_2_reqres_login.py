import pytest
import requests
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Login test')
@allure.title('Successful user login')
@allure.description('This test verifies that a user can successfully log in to the Reqres platform using valid credentials.')
@allure.severity(allure.severity_level.BLOCKER)
def test_login():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send login request'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=data,
            headers=headers
        )
    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Validate response contains token'):
        assert 'token' in response_data, 'Response should contain token'

    with allure.step('Verify token is not empty'):
        assert len(response_data['token']) > 0, 'Token should not be empty'


@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Login test')
@allure.title('User login without password')
@allure.description('This test verifies that login without a password fails with an appropriate error message.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_login():
    data = {
        "email": "peter@klaven"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send login request without password'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=data,
            headers=headers
        )
    with allure.step('Verify response status code is 400'):
        assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Validate response contains error message'):
        assert 'error' in response_data, 'Response should contain error message'
        assert len(response_data['error']) > 0, 'Error message should not be empty'
