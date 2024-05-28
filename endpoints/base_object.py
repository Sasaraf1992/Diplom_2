import requests
import settings
import allure

class BaseObject:
    response = None
    response_json = None
    response_status_code = None
    token = None
    response_status = None
    response_text = None

    def __init__(self):
        self.response_headers = None

    @allure.step('Проверка статуса и кода')
    def check_status_code_and_text(self, code, name, text):
        assert self.response_status_code == code and self.response_json[name] == text

    @allure.step('Проверка статуса и ключа')
    def check_order_status_code(self, code, name, text):
        assert self.response_status_code == code and name in self.response_json[text]

    @allure.step('Проверка отсутствия ключа')
    def check_order_status_code_not_in(self, code, name, text):
        assert self.response_status_code == code and name not in self.response_json[text]

    def check_status_code(self, code):
        assert self.response_status_code == code

    def check_response_text(self, text):
        assert text in self.response_text

    def check_headers(self, header, text):
        assert self.response_headers.get(header).startswith(text)

    @allure.step('Удаление пользователя')
    def delete_user(self, data):
        self.response = requests.delete(settings.URL_USER_DELETE, json=data)
