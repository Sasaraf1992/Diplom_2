import requests
import settings
from endpoints.base_object import BaseObject
import allure

class LoginUser(BaseObject):
    @allure.step('Логин пользователя')
    def user_login(self, data):
        self.response = requests.post(settings.URL_USER_LOGIN, json=data)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code