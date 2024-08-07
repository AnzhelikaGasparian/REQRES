import pytest
import requests
import allure

my_reg_id = 0
my_reg_token = 0

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Register test')
@allure.title('Successful user registration')
@allure.description('This test verifies that a user can successfully register on the Reqres platform using valid credentials.')
@allure.severity(allure.severity_level.BLOCKER)
def test_create_register():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send registration request'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    with allure.step('Validate response contains user ID'):
        response_data = response.json()
        assert "id" in response_data, 'Response should contain user ID'

    with allure.step('Validate response contains token'):
        assert "token" in response_data, 'Response should contain token'

    global my_reg_id
    my_reg_id = response_data['id']

    global my_reg_token
    my_reg_token = response_data['token']

@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Register test')
@allure.title('User registration without password')
@allure.description('This test verifies that registration without a password fails with an appropriate error message.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_create_register_without_password():
    data = {
        "email": "sydney@fife"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send registration request without password'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 400'):
        assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Validate response contains error message'):
        assert 'error' in response_data, 'Response should contain error message'

    with allure.step('Verify error message is "Missing password"'):
        assert response_data['error'] == "Missing password", 'Error message should be "Missing password"'