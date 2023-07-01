from functions import request
import json

class KeywordScaleSerp:
    def __init__(self, keyword, api_key):
        self.keyword = keyword
        self.api_key = api_key

    def get_keyword_scaleserp(self):
        print("fetching")
        api_result = request.customRequest(url= "https://api.scaleserp.com/search", method="GET", params={
            'q': self.keyword,
            'api_key': self.api_key
        })
        if api_result != False: 
            return json.loads(api_result)['organic_results'][:5]