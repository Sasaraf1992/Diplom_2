from data import StellarBurgerTestData as SD
from faker import Faker
import pytest
from endpoints.login_user_object import LoginUser
from endpoints.change_data_user_object import ChangeDataUser
import allure
fake = Faker()


class TestUserDataChange:
    @allure.title('Проверка успешной смены данных авторизованного пользователя')
    @pytest.mark.parametrize('data_change', [
        {'email': fake.email()},
        {'password': fake.password()},
        {'name': fake.first_name()}
    ])
    def test_auth_user_successful_data_change(self, fake_user, get_token, data_change):
        cd = ChangeDataUser()
        lu = LoginUser()
        lu.user_login(data=SD.FAKE_USER)
        cd.user_data_change(data=data_change, headers=get_token)
        cd.check_status_code_and_text(200, 'success', True)

    @allure.title('Проверка ошибки при смены данных неавторизованного пользователя')
    @pytest.mark.parametrize('data_change', [
        {'email': fake.email()},
        {'password': fake.password()},
        {'name': fake.first_name()}
    ])
    def test_not_auth_user_fail_data_change(self, fake_user, data_change):
        cd = ChangeDataUser()
        cd.user_data_change(data=data_change, headers = None)
        cd.check_status_code_and_text(401, 'message', 'You should be authorised')



