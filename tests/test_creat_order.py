from data import StellarBurgerTestData as SD
from faker import Faker
from endpoints.login_user_object import LoginUser
from endpoints.create_order_object import CreateOrder
import allure

fake = Faker()


class TestOrderCreation:
    @allure.title('Проверка, создания заказа авторизованным пользователем')
    def test_order_creation_with_auth(self, fake_user, get_token):
        lu = LoginUser()
        co = CreateOrder()
        lu.user_login(data=SD.FAKE_USER)
        co.create_order(data=SD.ORDER_DATA, headers=get_token)
        co.check_order_status_code(200, 'owner', 'order')

    @allure.title('Проверка, cоздания заказа неавторизованным пользователем')
    def test_order_creation_without_auth(self):
        co = CreateOrder()
        co.create_order(data=SD.ORDER_DATA, headers=None)
        co.check_order_status_code_not_in(200, 'owner', 'order')

    @allure.title('Проверка, создания заказа без ингредиентов')
    def test_order_creation_without_ingridients(self, fake_user, get_token):
        co = CreateOrder()
        lu = LoginUser()
        lu.user_login(data=SD.FAKE_USER)
        co.create_order(data=SD.ORDER_DATA_WITHOUT_ING, headers=get_token)
        co.check_status_code_and_text(400, 'message', "Ingredient ids must be provided")

    @allure.title('Проверка, создания заказа с неверным хэшем ингредиентов')
    def test_order_creation_with_wrong_hash(self, fake_user, get_token):
        co = CreateOrder()
        lu = LoginUser()
        lu.user_login(data=SD.FAKE_USER)
        co.get_user_order_html(data=SD.ORDER_DATA_WITH_WRONG_HASH, headers=get_token)
        co.check_status_code(500)

