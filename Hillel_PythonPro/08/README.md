﻿# [Homework 08 • OOP. Dunder methods ](https://lms.ithillel.ua/groups/63c0179f2482232c29371552/homeworks/6446dfc21c978946f0f8398c)

- [ ] Create a class Price
```python
class Price:
   def __init__(self, amount: int, currency: str) -> None:
      self.amount: int = amount
      self.currency: str = currency
```

**Acceptance criteria:**

If I create 2 instances of a `Price` class I want to do operations between them:
- [ ] `add` prices with the same currency
- [ ] do a `subtraction` of prices with the same currency
- [ ] *Additional: operations between prices with different currencies:
- [ ] If price instances currencies are different I want to do a double conversion
- [ ] USD is used as an intermediate currency (to convert `UAH` to `GBP` you have to do next: `UAH` -> `USD` -> `GBP` )
- [ ] If the right price is `USD` - the regular conversion (not double) is happening
- [ ] If prices' currencies are the same - conversion is not happening
- [ ] Result currency after the operation is a `❓cur`