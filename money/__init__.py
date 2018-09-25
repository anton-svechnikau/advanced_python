"""Init file."""

import requests
import datetime


CURRENCY_API = 'http://www.apilayer.net/api/live?access_key={token}&format=1'


def _get_rates(token):
    """Get rates."""
    if not token:
        raise ValueError('Invalid token for apilayer')

    rates = {}
    try:
        request = requests.get(CURRENCY_API.format(token=token))
    except Exception:
        print("Can't update currency rates.")
    else:
        rates = request.json().get('quotes', {})
        rates['update_time'] = datetime.datetime.now()
    return rates


def _get_token():
    """Get token."""
    token = ''
    try:
        with open('token', 'rb') as file:
            lines = [l for l in file]
            token = lines[0][:-1].decode('utf-8')
    except Exception:
        print("Can't find token.")

    return token


RATES = _get_rates(_get_token())
