def assert_common(self, response, success):
    self.assertEqual(success, response.json().get("success"))
