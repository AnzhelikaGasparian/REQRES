import pytest
import requests
import allure
from test_3_reqres_post import my_id


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres')
@allure.suite('Delete User Suite')
@allure.title('Validate Deletion of User via Reqres API')
@allure.description('This test case verifies the deletion of a user via the Reqres API and validates the response status code is 204.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_delete():
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send DELETE request to delete user'):
        response = requests.delete(
            f'https://reqres.in/api/users/{my_id}',
            headers=headers
        )

    with allure.step('Verify the response status code is 204'):
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
