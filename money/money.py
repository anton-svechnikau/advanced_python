
from . import RATES
from decimal import Decimal


STANDART_CURRENCY = 'USD'


class Money:
    def __init__(self, amount, currency=STANDART_CURRENCY):
        try:
            self.amount = Decimal(str(amount))
        except Exception as exp:
            raise ValueError

        self.currency = currency.upper()

    def __repr__(self):
        return 'Money: {amount} {curr}'.format(
            amount=self.amount,
            curr=self.currency,
            )

    def __str__(self):
        return '{amount} {curr}'.format(
            amount=round(self.amount, 2),
            curr=self.currency,
            )

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount
        else:
            currency_pair = STANDART_CURRENCY + other.currency
            try:
                other_currency_rate = Decimal(str(RATES.get(currency_pair)))
            except Exception as exp:
                raise ValueError('Invalid currency')
            else:
                return Money(self.amount + other.amount / other_currency_rate, self.currency)

    def __mul__(self, other):
        if self.currency == other.currency:
            return self.amount * other.amount
        else:
            currency_pair = STANDART_CURRENCY + other.currency
            try:
                other_currency_rate = Decimal(str(RATES.get(currency_pair)))
            except Exception as exp:
                raise ValueError('Invalid currency')
            else:
                return Money(self.amount * (other.amount / other_currency_rate, self.currency))

    def __truediv__(self, other):
        if self.currency == other.currency:
            return self.amount / other.amount
        else:
            currency_pair = STANDART_CURRENCY + other.currency
            try:
                other_currency_rate = Decimal(str(RATES.get(currency_pair)))
            except Exception as exp:
                raise ValueError('Invalid currency')
            else:
                return Money(self.amount / (other.amount / other_currency_rate, self.currency))
