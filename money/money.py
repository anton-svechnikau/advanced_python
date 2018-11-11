    """
HW -- 7.

Implement money object.
"""

from . import RATES
from decimal import Decimal


STANDART_CURRENCY = 'USD'


class Money:
    """Money object."""

    def __init__(self, amount, currency=STANDART_CURRENCY):
        """Init of the object."""
        try:
            self.amount = Decimal(str(amount))
        except Exception as exp:
            raise ValueError(exp)

        self.currency = currency.upper()
        self.currency_rates = RATES

    def __repr__(self):
        """Printable representation of the object."""
        return 'Money: {amount} {curr}'.format(
            amount=self.amount,
            curr=self.currency,
        )

    def __str__(self):
        """Printable representation of the object."""
        return '{amount} {curr}'.format(
            amount=round(self.amount, 2),
            curr=self.currency,
        )

    def __add__(self, other):
        """Add operation for the object."""
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount + other.amount, self.currency)
            else:
                try:
                    if other.currency == 'USD':
                        currency_pair = other.currency + self.currency
                    else:
                        currency_pair = STANDART_CURRENCY + other.currency
                    other_currency_rate = Decimal(str(RATES.get(currency_pair)))
                except Exception as exp:
                    raise ValueError(exp)
                else:
                    if other.currency == 'USD':
                        return Money(
                            self.amount + other.amount * other_currency_rate,
                            self.currency
                        )
                    else:
                        return Money(
                            self.amount + other.amount / other_currency_rate,
                            self.currency
                        )
        else:
            raise TypeError

    def __sub__(self, other):
        """Subtraction operation for the object."""
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount - other.amount, self.currency)
            else:
                try:
                    if other.currency == 'USD':
                        currency_pair = other.currency + self.currency
                    else:
                        currency_pair = STANDART_CURRENCY + other.currency
                    other_currency_rate = Decimal(str(RATES.get(currency_pair)))
                except Exception as exp:
                    raise ValueError(exp)
                else:
                    if other.currency == 'USD':
                        return Money(
                            self.amount - other.amount * other_currency_rate,
                            self.currency
                        )
                    else:
                        return Money(
                            self.amount - other.amount / other_currency_rate,
                            self.currency
                        )
        else:
            raise TypeError

    def __mul__(self, other):
        """Multiply operation for the object."""
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount * Decimal(str(other)), self.currency)
        elif isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount * other.amount, self.currency)
            else:
                try:
                    if other.currency == 'USD':
                        currency_pair = other.currency + self.currency
                    else:
                        currency_pair = STANDART_CURRENCY + other.currency
                    other_currency_rate = Decimal(str(RATES.get(currency_pair)))
                except Exception as exp:
                    raise ValueError(exp)
                else:
                    if other.currency == 'USD':
                        return Money(
                            self.amount * (other.amount * other_currency_rate),
                            self.currency
                        )
                    else:
                        return Money(
                            self.amount * (other.amount / other_currency_rate),
                            self.currency
                        )
        else:
            raise TypeError

    def __rmul__(self, other):
        """Multiply operation for the object."""
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount * Decimal(other), self.currency)
        else:
            raise TypeError

    def __truediv__(self, other):
        """Division operation for the object."""
        if isinstance(other, int) or isinstance(other, float):
            return Money(self.amount / Decimal(str(other)), self.currency)

        if not isinstance(other, Money):
            raise TypeError

        if self.currency == other.currency:
            return Money(self.amount / other.amount, self.currency)
        else:
            try:
                if other.currency == 'USD':
                    currency_pair = other.currency + self.currency
                else:
                    currency_pair = STANDART_CURRENCY + other.currency
                other_currency_rate = Decimal(str(RATES.get(currency_pair)))
            except Exception as exp:
                raise ValueError(exp)
            else:
                if other.currency == 'USD':
                    return Money(
                        self.amount / (other.amount * other_currency_rate),
                        self.currency
                    )
                else:
                    return Money(
                        self.amount / (other.amount / other_currency_rate),
                        self.currency
                    )

    def __rtruediv__(self, other):
        """Division operation for the object."""
        if isinstance(other, int) or isinstance(other, float):
            return Money(Decimal(other) / self.amount, self.currency)
        else:
            raise TypeError
