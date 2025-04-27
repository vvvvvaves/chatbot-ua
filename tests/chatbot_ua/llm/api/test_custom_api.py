import unittest
import config


class TestCustomAPI(unittest.TestCase):

    def test_completion(self):
        api = config.get_api(run="test")

        messages = [{
            "role": "user",
            "content": "Hi! How are you?"
        }]

        response = api.completion(messages=messages,
                                  stream=False,
                                  max_tokens=50,
                                  temperature=1.,
                                  presence_penalty=0.,
                                  frequency_penalty=0.)

        self.assertEqual(response.status_code, 200, "Response status code is not 200.")

        self.assertIsNotNone(response.json(), "response.json() is None.")

        self.assertIsInstance(response.json(), dict, "response.json() is not a dictionary.")


if __name__ == '__main__':
    unittest.main()
