import pytest
import requests
import allure


@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Get Reqres Suite')
@allure.title('Test Reqres Delayed Response')
@allure.description('This test verifies that the Reqres API handles a delayed response correctly.')
@allure.severity(allure.severity_level.NORMAL)
def test_reqres_delayed():
    with allure.step('Send GET request to Reqres with a delay'):
        response = requests.get('https://reqres.in/api/users?delay=6')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code should be 200, but god{response.status_code}'

    response_data = response.json()


    with allure.step('Verify the response contains "page" key'):
        assert 'page' in response_data, 'Expected "page" key in the response'
        assert isinstance(response_data['page'], (int, float)), "The 'page' should be a number"


    with allure.step('Verify the response contains "per_page" key'):
        assert 'per_page' in response_data, 'Expected "per_page" key in the response'
        assert isinstance(response_data['per_page'], (int, float)), "The 'per_page' should be a number"

    with allure.step('Verify the response contains "total" key'):
        assert 'total' in response_data, 'Expected "total" key in the response'
        assert isinstance(response_data['total'], (int, float)), "The 'total' should be a number"

    with allure.step('Verify the response contains "total_pages" key'):
        assert 'total_pages' in response_data, 'Expected "total_pages" key in the response'
        assert isinstance(response_data['total_pages'], (int, float)), "The 'total_pages' should be a number"

    with allure.step('Verify the response contains "data" key and has items'):
        assert 'data' in response_data, 'Expected "data" key in the response'
        assert len(response_data['data']) > 0, 'Expected "data" to have items'

    with allure.step('Verify the response contains "support" key and has items'):
        assert 'support' in response_data, 'Expected "support" key in the response'
        assert len(response_data['support']) > 0, 'Expected "support" to have items'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)



@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Get Reqres Suite')
@allure.title('Validate Response Structure of Reqres List Users API')
@allure.description('This test case validates the structure and key elements of the response for the List Users API from Reqres.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_list_user():
    with allure.step('Send GET request to retrieve list of users'):
        response = requests.get('https://reqres.in/api/users?page=2')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code to be 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "page" key'):
        assert 'page' in response_data, 'Expected "page" key in the response'
        assert isinstance(response_data['page'], (int, float)), "The 'page' should be a number"

    with allure.step('Verify the response contains "per_page" key'):
        assert 'per_page' in response_data, 'Expected "per_page" key in the response'
        assert isinstance(response_data['per_page'], (int, float)), "The 'per_page' should be a number"

    with allure.step('Verify the response contains "total" key'):
        assert 'total' in response_data, 'Expected "total" key in the response'
        assert isinstance(response_data['total'], (int, float)), "The 'total' should be a number"

    with allure.step('Verify the response contains "total_pages" key'):
        assert 'total_pages' in response_data, 'Expected "total_pages" key in the response'
        assert isinstance(response_data['total_pages'], (int, float)), "The 'total_pages' should be a number"

    with allure.step('Verify the response contains "data" key and has items'):
        assert 'data' in response_data, 'Expected "data" key in the response'
        assert len(response_data['data']) > 0, 'Expected "data" to have items'

    with allure.step('Verify the response contains "support" key and has items'):
        assert 'support' in response_data, 'Expected "support" key in the response'
        assert len(response_data['support']) > 0, 'Expected "support" to have items'

    with allure.step('Attach the response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)



@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Get Reqres Suite')
@allure.title('Validate Single User Retrieval from Reqres')
@allure.description('This test case verifies the retrieval of a single user from the Reqres API and validates the response structure.')
@allure.severity(allure.severity_level.NORMAL)
def test_reqres_single_user():
    with allure.step('Send GET request to retrieve a single user'):
        response = requests.get('https://reqres.in/api/users/2')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code to be 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "data" key and has items'):
        assert 'data' in response_data, 'Expected "data" key in the response'
        assert len(response_data['data']) > 0, 'Expected "data" to have items'

    with allure.step('Verify the response contains "support" key and has items'):
        assert 'support' in response_data, 'Expected "support" key in the response'
        assert len(response_data['support']) > 0, 'Expected "support" to have items'

    with allure.step('Attach the response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

