import pandas as pd
import requests

class ExtractSimilar: 

    def __init__(self, query_text):
        self.query_text = query_text

    
    def read_query_text(self):
        return self.query_text