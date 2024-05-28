import requests
import settings
from endpoints.base_object import BaseObject
import allure


class CreateUser(BaseObject):
    @allure.step('Создание пользователя')
    def user_creation(self, data):
        self.response = requests.post(settings.URL_USER_CREATION, json = data)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code
        self.token = self.response_json.get('accessToken')