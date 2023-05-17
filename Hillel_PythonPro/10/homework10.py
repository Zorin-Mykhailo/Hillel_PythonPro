import http
import json
from pprint import pprint as print
import requests
import asyncio
import httpx


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, api_key: str, courses: list[tuple[str, str]]) -> None:
        if ExchangeRates._initialized:
            return
        self.data = {}
        #self.data: dict = self._fetch_from_api()

        asyncio.run(self.get_rates())

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

    @staticmethod
    async def get_rates(api_key: str, courses: list[tuple[str, str]]) -> None:
        async with httpx.AsyncClient() as httpClient:
            tasks = []
            for course in courses:
                request = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={course[0]}&to_currency={course[1]}&apikey={api_key}"
                tasks.append(httpClient.get(request))
            responses = await asyncio.gather(*tasks)
            for response in responses:

            self.data = [response.json() for response in responses]

er = ExchangeRates('06EXQ0JZFVLO6RZA', None)
# er = object.__new__(ExchangeRates)
# er <= ExchangeRages.__init__() <= ExchangeRates.__new__()


print(er.data)
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# er2 = ExchangeRates()
# print(er2.data)

async def main(api_key: str, courses: list[tuple[str, str]]):
    print(f'{api_key=}')
    print(f'{courses=}')
    return
    async with asyncio.TaskGroup() as tg:
        
        task1 = tg.create_task(...)
        task2 = tg.create_task(...)
    print("all tasks have completed now.")

if __name__ == '__main__':
    api_key = '06EXQ0JZFVLO6RZA'
    courses = [
        ('USD', 'UAH'),
        ('EUR', 'UAH'),
        ('UAH', 'UAH'),
        ('PLN', 'UAH'),
        ('GBP', 'UAH')
    ]


    asyncio.run(main(api_key, courses))