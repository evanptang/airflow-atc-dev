import requests

url = "https://rapidapi.p.rapidapi.com/country/code"

def get_covid_data(country_code, api_token, **kwargs):
    querystring = {"code": country_code}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': api_token
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.content