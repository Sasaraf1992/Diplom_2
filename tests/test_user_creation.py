from data import StellarBurgerTestData as SD
from faker import Faker
import pytest
from endpoints.create_user_object import CreateUser
import allure
fake = Faker()


class TestUserCreation:

    @allure.title('Проверка создания пользователя')
    def test_user_successful_creation(self, fake_user):
        fake_user.check_status_code_and_text(200, 'success', True)

    @allure.title('Проверка ошибки создания уже существующего пользователя')
    def test_user_already_existing_error(self, fake_user):
        cu = CreateUser()
        cu.user_creation(data=SD.FAKE_USER)
        cu.check_status_code_and_text(403, 'success', False)

    @allure.title('Проверка ошибки создания пользователя с одним пустым полем')
    @pytest.mark.parametrize('email, password, name', [
        (fake.email(), fake.password(), None),
        (fake.email(), None, fake.user_name()),
        (None, fake.password(), fake.user_name())
    ])
    def test_user_creation_one_missed_field(self, email, password, name):
        cu = CreateUser()
        cu.user_creation(data={'email': email, 'password': password, 'name': name})
        cu.check_status_code_and_text(403, 'message', 'Email, password and name are required fields')