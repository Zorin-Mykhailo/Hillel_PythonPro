# [Homework 08 • OOP. Dunder methods ](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/6446dfc21c978946f0f8398c)

- [x] Create a class Price
```python
class Price:
   def __init__(self, amount: int, currency: str) -> None:
      self.amount: int = amount
      self.currency: str = currency
```

**Acceptance criteria:**

- [x] If I create 2 instances of a `Price` class I want to do operations between them:
    - [x] `add` prices with the same currency
    - [x] do a `subtraction` of prices with the same currency

- [x] __Additional__: operations between prices with different currencies:
    - [x] If price instances currencies are different I want to do a double conversion
    - [x] USD is used as an intermediate currency (to convert `UAH` to `GBP` you have to do next: `UAH` -> `USD` -> `GBP` )
    - [x] If the right price is `USD` - the regular conversion (not double) is happening
    - [x] If prices' currencies are the same - conversion is not happening
    - [x] Result currency after the operation is a `❓cur` 