from data import StellarBurgerTestData as SD
from endpoints.login_user_object import LoginUser
from endpoints.create_order_object import CreateOrder
import allure


class TestGetOrder:
    @allure.title('Проверка получения заказа авторизованным пользователем')
    def test_get_order_user_auth_successful(self, fake_user, get_token):
        lu = LoginUser()
        co = CreateOrder()
        lu.user_login(data=SD.FAKE_USER)
        co.create_order(data=SD.ORDER_DATA, headers=get_token)
        co.get_user_order(headers=get_token)
        co.check_status_code_and_text(200, 'success', True)

    @allure.title('Проверка получения заказа неавторизованным пользователем')
    def test_get_order_user_not_auth_failed(self, fake_user, get_token):
        lu = LoginUser()
        co = CreateOrder()
        lu.user_login(data=SD.FAKE_USER)
        co.create_order(data=SD.ORDER_DATA, headers=get_token)
        co.get_user_order(headers=None)
        co.check_status_code_and_text(401, 'message', 'You should be authorised')
