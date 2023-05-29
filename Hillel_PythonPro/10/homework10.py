import asyncio
from pprint import pprint as print

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
        self.data = []
        asyncio.run(self._obtain_rates(api_key, courses))
        ExchangeRates._initialized = True

    async def _obtain_rates(self, api_key: str, courses: list[tuple[str, str]]) -> None:
        async with httpx.AsyncClient() as httpClient:
            tasks = []
            for course in courses:
                request = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={course[0]}&to_currency={course[1]}&apikey={api_key}"
                tasks.append(httpClient.get(request))
            responses = await asyncio.gather(*tasks)

            for response in responses:
                json = response.json()
                if "Realtime Currency Exchange Rate" not in json:
                    continue
                res = response.json()["Realtime Currency Exchange Rate"]
                result = (
                    res["1. From_Currency Code"],
                    res["3. To_Currency Code"],
                    res["5. Exchange Rate"],
                )
                self.data.append(result)
                print(f"1 {result[0]} = {result[2]} {result[1]}")


def main(api_key: str, courses: list[tuple[str, str]]):
    ExchangeRates(api_key, courses)


if __name__ == "__main__":
    api_key = "06EXQ0JZFVLO6RZA"
    courses = [("USD", "UAH"), ("EUR", "UAH"), ("GBP", "UAH")]
    main(api_key, courses)
