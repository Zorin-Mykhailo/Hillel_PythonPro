﻿from enum import IntEnum


class Cur(IntEnum):
    USD = 1
    EUR = 2
    UAH = 3
    PLN = 4
    GBP = 5

    def __str__(self):
        return self.name


exchange_rates = {
    Cur.USD: 1.0000,
    Cur.EUR: 0.9114,
    Cur.UAH: 37.9374,
    Cur.PLN: 4.1985,
    Cur.GBP: 0.8299,
}


class Price:
    def __init__(self, amount: float, currency: Cur) -> None:
        self.__amount: float = amount
        self.__currency: Cur = currency

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float) -> None:
        self.__amount = value

    @property
    def currency(self) -> Cur:
        return self.__currency

    def convert(self, second_currency: Cur) -> "Price":
        price_in_usd = (
            self
            if Cur.USD == self.currency
            else Price(self.amount / exchange_rates[self.currency], Cur.USD)
        )
        return (
            price_in_usd
            if second_currency == price_in_usd.currency
            else Price(
                price_in_usd.amount * exchange_rates[second_currency], second_currency
            )
        )

    def __add__(self, other):
        if self is None and other is None:
            return None
        if other is None:
            return self
        another = other
        if self.currency != other.currency:
            another = other.convert(self.currency)
        return Price(self.amount + another.amount, self.currency)

    def __sub__(self, other):
        if self is None and other is None:
            return None
        if other is None:
            return self
        another = other
        if self.currency != other.currency:
            another = other.convert(self.currency)
        return Price(self.amount - another.amount, self.currency)

    def __str__(self):
        return f"{self.__amount:0.2f} {self.currency}"


def main() -> None:
    print(f"{Price(1.00, Cur.USD) + Price(37.9374, Cur.UAH)}")
    print(f"{Price(379.374, Cur.UAH) - Price(9.0, Cur.USD)}")


if __name__ == "__main__":
    main()
