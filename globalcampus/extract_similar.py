import pandas as pd
import requests
from . import TOKEN_SECRET, MAIN_URL


class ExtractSimilar: 

    def __init__(self, secret_token, main_url):
        self.token =  secret_token
        self.main_url = main_url
        self.headers = {
    'Authorization': f'Token {TOKEN_SECRET}',
    'Content-Type': 'application/json'
}

    
    def find_similar(self, query_text, limit=5, search_module=1):
        payload = {"search_module": search_module,
                   "limit": limit,
                   "query_text": query_text}
        try:
            response = requests.post(self.main_url, json=payload, headers=self.headers)
            if response.status_code == 200:
                data= response.json()
                return data
            else: 
                return response.status_code
        
        except:
            print("An error occurred:", e)
            return None 