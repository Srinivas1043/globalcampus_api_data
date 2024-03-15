from extract_similar.utilities import Utilities
import unittest

class TestUtilities(unittest.TestCase):

    def test_check_post_request(self):
        utilitiy_obj = Utilities()
        actual_response = utilitiy_obj.check_post_request()
        expected_response = 200
        assert expected_response == actual_response