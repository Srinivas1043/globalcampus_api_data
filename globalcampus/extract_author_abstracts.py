import pandas as pd
import requests
from . import TOKEN_SECRET, MAIN_URL


class ExtractAuthorAbstracts: 

    def __init__(self, secret_token, main_url):
        self.token =  secret_token
        self.main_url = main_url
        self.headers = {
    'Authorization': f'Token {TOKEN_SECRET}',
    'Content-Type': 'application/json'
}

    
    def get_author_abstracts(self, author_id="A5037750063", search_module=1):
        params = {"search_module": search_module,
                   "author_id": author_id,
                   }
        try:
            response = requests.get(self.main_url, params=params, headers=self.headers)
            if response.status_code == 200:
                data= response.json()
                return data
            else: 
                return None
        
        except:
            print("An error occurred:", e)
            return None 