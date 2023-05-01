# Used sources
1. [ABC � Abstract Base Classes](https://docs.python.org/3.10/library/abc.html#module-abc) #python.org
1. [����������� ������ � ���������� � ������](https://habr.com/ru/articles/72757/) #Habr


# ������

1. ��������� ����� �� ������� � ���� ����, � ��������� ������ � ������������ ����� `abc`

```python
from abc import ABC, abstractmethod
```

2. �� ��������� ����������� ������� ����� (��� ABC) ����� ��������� ����, �������� �� ������ �� ���������� ������ ���� ����'������ �������� � ������-����������

```python
class Movable(ABC):

    @abstractmethod
    def move():
    """����������� ������"""

    @abstractproperty
    def speed():
    """�������� �������"""
```

� ������ ������� ����, �� ���������� �� `Movable` ������� � ����'�������� ������� ������������� ����� ����� ������ ��������� `@abstract...`

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