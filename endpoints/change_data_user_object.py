import requests
import settings
from endpoints.base_object import BaseObject
import allure


class ChangeDataUser(BaseObject):
    @allure.step('Изменение данных пользователя')
    def user_data_change(self, data, headers):
        self.response = requests.patch(settings.URL_USER_DATA_CHANGE, json=data, headers=headers)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code
