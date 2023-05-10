# [Homework 10 • Async IO](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/6450182004d8ea2db78b5e5b)

We had an example with exchange rates on [Lesson6](https://github.com/parfeniukink/hillel_04_2022/blob/main/lesson_6/exchange_rates.py):

```python
from pprint import pprint as print

import requests


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        self.data: dict = self._fetch_from_api()

        ExchangeRates._initialized = True

    @staticmethod
    def _fetch_from_api() -> dict:
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=PASTE_YOUR_API_KEY"
        response = requests.get(url)
        return response.json()

    # @staticmethod
    # def get_rate(source: str, target: str) -> float:
    #     url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={target}&apikey=PASTE_YOUR_API_KEY"
    #     response = requests.get(url)
    #     return response.json()["5. Exchange rate"]


er = ExchangeRates()
# er = object.__new__(ExchangeRates)
# er <= ExchangeRages.__init__() <= ExchangeRates.__new__()


print(er.data)
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# print(er2.data)
```


**Acceptance criteria:**
- [ ] Now all requests to the external API are making async calls.
- [ ] The httpx library is used ([DOCUMENTATION](https://www.python-httpx.org/async/))