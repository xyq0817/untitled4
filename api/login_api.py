import requests
import app


class LoginApi():
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login(self, mobile, ps):
        data = {"mobile": mobile, 'password': ps}
        response = requests.post(self.login_url, json=data, headers=self.headers)
        return response
