# ================================
# TeachMeSkills.by — Домашнее задание
# ================================
"""
Здесь задания на генераторы и паттерны проектирования:
- Строитель
- Фабричный метод
- Стратегия

Заполняйте TODO, читайте комментарии и запускайте тесты.
"""

# ================================
# ЗАДАНИЕ 1: Генератор чисел Фибоначчи
# ================================

def fibonacci_generator(n: int):
    """Генераторная функция, возвращает n чисел Фибоначчи."""
    # TODO: напишите генератор
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Тест:
print("\n--- Задание 1 ---")
n = int(input("Сколько чисел Фибоначчи вывести? "))
for num in fibonacci_generator(n):
    print(num, end=' ')
print()


# ================================
# ЗАДАНИЕ 2: Бесконечная циклическая последовательность
# ================================

def cycle_123():
    """Генераторная функция, бесконечно выдаёт 1-2-3"""
    # TODO: напишите генератор
    list = [1, 2, 3]
    while True:
        for number in list:
            yield number

# Тест:
print("\n--- Задание 2 ---")
count = int(input("Сколько чисел вывести из бесконечного цикла? "))
gen = cycle_123()
for _ in range(count):
    print(next(gen), end=' ')
print()


# ================================
# ЗАДАНИЕ 3: Паттерн «Строитель»
# ================================

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        # TODO: реализуйте метод
        self.pizza.size = size
        return self

    def add_cheese(self):
        # TODO: реализуйте метод
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    # TODO: реализуйте остальные add_… методы и метод build()
    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        # TODO: используйте методы builder, чтобы собрать пиццу
        return (self.builder
                .set_size("Small")
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .add_onions()
                .add_bacon()
                .build()
        )


# Тест:
print("\n--- Задание 3 ---")
builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)


# ================================
# ЗАДАНИЕ 4: Паттерн «Фабричный метод»
# ================================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        # TODO: реализуйте метод
        print("woof-woof")


class Cat(Animal):
    def speak(self):
        # TODO: реализуйте метод
        print("meow-meow")


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        # TODO: возвращайте Dog или Cat в зависимости от animal_type
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Животное {animal_type} не найдено")


# Тест:
print("\n--- Задание 4 ---")
factory = AnimalFactory()
animal = factory.create_animal("dog")
animal.speak()
animal = factory.create_animal("cat")
animal.speak()


# ================================
# ЗАДАНИЕ 5: Паттерн «Стратегия»
# ================================

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a * b


class Division(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a, b):
        # TODO: выполните операцию через текущую стратегию
        if not self.strategy:
            return "Ошибка: стратегия не определена"
        return self.strategy.execute(a, b)


# Тест:
print("\n--- Задание 5 ---")
calc = Calculator()
calc.set_strategy(Addition())
print("5 + 3 =", calc.calculate(5, 3))
calc.set_strategy(Subtraction())
print("5 - 3 =", calc.calculate(5, 3))
calc.set_strategy(Multiplication())
print("5 * 3 =", calc.calculate(5, 3))
calc.set_strategy(Division())
print("5 / 3 =", calc.calculate(5, 3))


# ================================
# УДАЧИ! 🚀
# ================================