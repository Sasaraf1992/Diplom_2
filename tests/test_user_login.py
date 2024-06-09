from faker import Faker
from endpoints.login_user_object import LoginUser
import allure
from data import StellarBurgerTestData as SD

fake = Faker()



class TestUserLogin:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_user_successful_auth(self, fake_user):
        lu = LoginUser()
        lu.user_login(data=SD.FAKE_USER)
        lu.check_status_code_and_text(200, 'success', True)

    @allure.title('Проверка ошибки авторизации пользователя при неверном логине')
    def test_user_auth_with_wrong_login(self, fake_user):
        lu = LoginUser()
        lu.user_login(data={'email': fake.email(), 'password': SD.FAKE_USER['password']})
        lu.check_status_code_and_text(401, 'success', False)

    @allure.title('Проверка ошибки авторизации пользователя при неверном пароле')
    def test_user_auth_with_wrong_password(self, fake_user):
        lu = LoginUser()
        lu.user_login(data={'email': SD.FAKE_USER['email'], 'password': '23322'})
        lu.check_status_code_and_text(401, 'success', False)