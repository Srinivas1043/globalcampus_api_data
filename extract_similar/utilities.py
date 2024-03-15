import requests
from . import TOKEN_SECRET, MAIN_URL

class Utilities: 

    def __init__(self):
        self.token =  TOKEN_SECRET
        self.main_url = MAIN_URL
        self.headers = {
    'Authorization': f'Token {TOKEN_SECRET}',
    'Content-Type': 'application/json'
}
        self.payload = {
  "search_module": 1,
  "limit": 5,
  "query_text": "Cancer and AI cure"
}
    
    def check_post_request(self):
        response = requests.post(self.main_url, json=self.payload, headers=self.headers)
        if response.status_code == 200:
            return response.status_code
        else:
            print('Error:', response.status_code)
            return response.status_code
    
    
        

