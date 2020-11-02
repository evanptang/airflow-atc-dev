import requests

url = "https://rapidapi.p.rapidapi.com/quotes/random/"

def get_quotes_data(api_token, **kwargs):

    headers = {
            'x-rapidapi-host': "quotes15.p.rapidapi.com",
            'x-rapidapi-key': api_token
        }

    response = requests.request("GET", url, headers=headers)

    return response.content