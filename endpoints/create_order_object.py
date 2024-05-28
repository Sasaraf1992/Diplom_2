import requests
import settings
from endpoints.base_object import BaseObject
import allure


class CreateOrder(BaseObject):
    @allure.step('Создание заказа')
    def create_order(self, data, headers):
        self.response = requests.post(settings.URL_ORDER_CREATION, json=data, headers=headers)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code

    @allure.step('Получение заказов пользователя')
    def get_user_order(self, headers):
        self.response = requests.get(settings.URL_ORDER_CREATION, headers=headers)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code

    @allure.step('Получение заказов пользователя под ошибку 500')
    def get_user_order_html(self, data, headers):
        self.response = requests.post(settings.URL_ORDER_CREATION, json=data, headers=headers)
        self.response_status_code = self.response.status_code
