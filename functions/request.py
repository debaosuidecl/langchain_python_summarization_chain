import requests

def customRequest(url,params={}, payload={},method = "GET"):
    # Make a GET request
    response = requests.get(url,params) if method =="GET" else requests.post(url, payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
 
        return response.text
    else:
        
        print(f"Request failed with status code {response.status_code}")
        return False
