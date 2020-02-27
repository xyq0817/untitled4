import unittest

from api.login_api import LoginApi
import logging
from utils import assert_common
import app


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def test_login(self):
        response = self.login_api.login('13800000002', '123456')
        json_data = response.json()
        logging.info(json_data)
        assert_common(self, response, True)
        token = json_data.get("data")
        app.HEADERS['Authorization'] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.HEADERS))
