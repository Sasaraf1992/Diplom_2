import pytest
from faker import Faker
import allure
from endpoints.create_user_object import CreateUser
from data import StellarBurgerTestData as SD

fake = Faker()


@allure.step("Создание фейкового пользователя")
@pytest.fixture(scope='package')
def fake_user():
    cu = CreateUser()
    cu.user_creation(data=SD.FAKE_USER)

    yield cu

    cu.delete_user(data=SD.FAKE_USER)


@allure.step("Создание фейкового пользователя отдельно пароль и email")
@pytest.fixture(scope='package')
def fake_user_required_login_password():
    cu = CreateUser()
    email = fake.email()
    password = fake.password()
    cu.user_creation(data={'email': email, 'password': password, 'name': 'Dmitry'})

    yield email, password

    cu.delete_user(data={'email': email, 'password': password, 'name': 'Dmitry'})


@allure.step("Получение токена пользователя")
@pytest.fixture(scope='package')
def get_token(fake_user):
    token = fake_user.token
    header_token = {'Authorization': f'{token}'}
    return header_token
