import http
import json
from pprint import pprint as print
import requests
import asyncio
import httpx
from time import perf_counter, sleep


async def main():
    api_key = '06EXQ0JZFVLO6RZA'
    courses = [
        ('USD', 'UAH'),
        ('EUR', 'UAH'),        
        ('GBP', 'UAH'),
    ]

    async with httpx.AsyncClient() as httpClient:
        tasks = []
        for course in courses:
            request = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={course[0]}&to_currency={course[1]}&apikey={api_key}"
            tasks.append(httpClient.get(request))
        responses = await asyncio.gather(*tasks)
        
        for response in responses:            
            json = response.json()
            if 'Realtime Currency Exchange Rate' not in json:
                continue
            res = response.json()['Realtime Currency Exchange Rate']
            result = (res['1. From_Currency Code'], res['3. To_Currency Code'], res['5. Exchange Rate'])
            print(f'1 {result[0]} = {result[2]} {result[1]}')

            

    

if __name__ == '__main__':
    
    start_time = perf_counter()    
    asyncio.run(main())    
    print(f"\nElapsed time: {(perf_counter() - start_time):00.2f}")
     