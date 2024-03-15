from globalcampus.extract_author_abstracts import ExtractAuthorAbstracts
import unittest

MAIN_URL = 'https://globalcampus.ai/api/get_author_abstracts/'
TOKEN_SECRET= '67b1537b7e8f82c8e1af580f06e89a524efab8b7'

class TestExtractAuthorAbstracts(unittest.TestCase):
    
    def test_get_author_abstracts(self):
        
        extractsim_obj = ExtractAuthorAbstracts(secret_token=TOKEN_SECRET, main_url=MAIN_URL)
        data_extracted = extractsim_obj.get_author_abstracts()
        assert len(data_extracted) > 0