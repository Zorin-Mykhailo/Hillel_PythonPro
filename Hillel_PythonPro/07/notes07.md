# Used sources
1. [ABC — Abstract Base Classes](https://docs.python.org/3.10/library/abc.html#module-abc) #python.org
1. [Абстрактные классы и интерфейсы в Питоне](https://habr.com/ru/articles/72757/) #Habr


# Тезиси

1. Абстрактні класи не включені в ядро мови, а реалізовані окремо в стандартному модулі `abc`

```python
from abc import ABC, abstractmethod
```

2. За домомогою абстрактних базових класів (далі ABC) можна визначити клас, вказавши які методи чи властивості повинні бути обов'язково визначені в класах-наслідниках

```python
class Movable(ABC):

    @abstractmethod
    def move():
    """Переместить объект"""

    @abstractproperty
    def speed():
    """Скорость объекта"""
```

В такому випадку клас, що наслідується від `Movable` повинен в обов'язковому порядку перевизначити члени класу помічені атрибутом `@abstract...`

```python
class Car(Movable):
    def __init__:
        self.speed = 10
        self.x = 0

    def move(self):
        self.c += self.speed
        def speed(self):
        return self.speed
    
assert issubclass(Car, Movable)
assert ininstance(Car(), Movable)
```