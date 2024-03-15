from globalcampus.extract_similar import ExtractSimilar
import unittest

MAIN_URL = 'https://globalcampus.ai/api/find_similar/'
TOKEN_SECRET= '67b1537b7e8f82c8e1af580f06e89a524efab8b7'

class TestExtractSimilar(unittest.TestCase):
    
    def test_find_similar(self):
        
        extractsim_obj = ExtractSimilar(secret_token=TOKEN_SECRET, main_url=MAIN_URL)
        data_extracted = extractsim_obj.find_similar(query_text="Cancer and AI")
        assert len(data_extracted) > 0