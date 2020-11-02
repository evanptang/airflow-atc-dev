import requests

def get_weather_by_zip(zip_code, api_token, **kwargs):
    """
    zip_code: a five digit integer
    api_token: the api token for open weather api
    """
    api_endpoint = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}'.format(
        str(zip_code),
        api_token
    )
    response = requests.get(api_endpoint)
    return response.content
