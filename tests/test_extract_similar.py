from extract_similar.extract_similar import ExtractSimilar
import unittest

class TestExtractSimilar(unittest.TestCase):

    def test_read_query_text(self):
        extractsim_obj = ExtractSimilar("Soething random to test")
        query_text_ = extractsim_obj.read_query_text()
        print(query_text_)
        assert len(query_text_)