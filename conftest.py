import pytest
from faker import Faker
import allure
from endpoints.create_user_object import CreateUser
from data import StellarBurgerTestData as SD

fake = Faker()


@allure.step("Создание фейкового пользователя")
@pytest.fixture(scope='function')
def fake_user():
    cu = CreateUser()
    email = SD.FAKE_USER['email']
    password = SD.FAKE_USER['password']
    name = SD.FAKE_USER['name']
    cu.user_creation(data={'email': email, 'password': password, 'name': name})
    token = cu.token
    yield cu

    cu.delete_user(data={'email': email, 'password': password, 'name': name}, token = token)


@allure.step("Получение токена пользователя")
@pytest.fixture(scope='function')
def get_token(fake_user):
    token = fake_user.token
    header_token = {'Authorization': f'{token}'}
    return header_token


@allure.step("Создание фейкового пользователя отдельно пароль и email")
@pytest.fixture(scope='function')
def fake_user_required_login_password(fake_user):
    email = SD.FAKE_USER['email']
    password = SD.FAKE_USER['password']

    yield email, password
