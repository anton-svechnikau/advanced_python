
import requests
import datetime


CURRENCY_API = 'http://www.apilayer.net/api/live?access_key={token}&format=1'


def _get_rates(token):
    if not token:
        raise ValueError('Invalid token for apilayer')

    rates = {}
    try:
        request = requests.get(CURRENCY_API.format(token=token))
    except Exception as exp:
        pass
    else:
        rates = request.json().get('quotes', {})
        rates['update_time'] = datetime.datetime.now()
    return rates

def _get_token():
    token = ''
    try:
        with open('token', 'rb') as file:
            lines = [l for l in file]
            token = lines[0][:-1].decode('utf-8')
    except Exception as exp:
        raise FileExistsError

    return token


RATES = _get_rates(_get_token())
