# =============================
# Домашняя работа: ООП на Python
# TeachMeSkills.by
# =============================

# Задание 1. Класс «Товар» и «Склад».
#
# Класс «Товар» содержит закрытые поля:
# - название товара
# - название магазина
# - стоимость в рублях
#
# Класс «Склад» содержит массив товаров.
#
# Обеспечить возможности:
# ✅ Вывод информации о товаре со склада по индексу
# ✅ Вывод информации о товаре со склада по имени
# ✅ Сортировка товаров по названию, по магазину и по цене
# ✅ Перегрузка сложения товаров по цене


# === TODO: реализовать класс Product ===
class Product:
    def __init__(self, name, shop, price):
        # TODO: сохранить значения в закрытые поля
        self.__name = name
        self.__shop = shop
        self.__price = price

    def __str__(self):
        # TODO: вернуть читаемую строку с данными товара
        return f"Товар: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price}"

    # TODO: перегрузить оператор сложения (__add__), чтобы возвращалась сумма цен двух товаров
    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        raise TypeError("Можно складывать только объекты Product")

    @property
    def name(self):
        return self.__name

    @property
    def shop(self):
        return self.__shop

    @property
    def price(self):
        return self.__price

# === TODO: реализовать класс Warehouse ===
class Warehouse:
    def __init__(self):
        # TODO: создать список товаров
        self.products = [] #Создаем пустой список

    def add_product(self, product):
        # TODO: добавить товар на склад
        self.products.append(product)

    def get_by_index(self, index):
        # TODO: вернуть информацию о товаре по индексу
        if 0 <= index < len(self.products):
            return str(self.products[index])
        return "Товар не найден"

    def get_by_name(self, name):
        # TODO: вернуть информацию о товаре по имени
        for product in self.products:
            if product.name == name:
                return str(product)
        return "Товар не найден"

    def sort_by_name(self):
        # TODO: отсортировать по названию
        self.products.sort(key=lambda p: p.name)

    def sort_by_shop(self):
        # TODO: отсортировать по магазину
        self.products.sort(key=lambda p: p.shop)

    def sort_by_price(self):
        # TODO: отсортировать по цене
        self.products.sort(key=lambda p: p.price)


# === Тесты для задачи 1 ===
print("=== Задача 1: Склад ===")
w = Warehouse()
p1 = Product("Молоко", "Пятерочка", 70)
p2 = Product("Хлеб", "Магнит", 40)
p3 = Product("Сыр", "Пятерочка", 300)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.get_by_index(1))
print(w.get_by_name("Сыр"))

# TODO: протестировать сортировку и сложение p1 + p2

print("Сортировка по названию:")
w.sort_by_name()
for p in w.products:
    print(p)

print("Сортировка по магазину:")
w.sort_by_shop()
for p in w.products:
    print(p)

print("Сортировка по цене:")
w.sort_by_price()
for p in w.products:
    print(p)

print("Сложение p1 + p2:")
print(p1 + p2)


# =============================
# Задание 2. Класс «ПчёлоСлон».
#
# Инициализируется двумя числами:
# - часть пчелы
# - часть слона
#
# Методы:
# ✅ Fly() – True, если часть пчелы >= части слона
# ✅ Trumpet() – "tu-tu-doo-doo", если часть слона >= пчелы, иначе "wzzzz"
# ✅ Eat(meal, value) – meal только "nectar" или "grass".
#   - если nectar: у слона уменьшается, у пчелы увеличивается
#   - если grass: наоборот
#   - нельзя выйти за пределы 0–100


# === TODO: реализовать класс BeeElephant ===
class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        # TODO: сохранить bee_part и elephant_part
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        # TODO: реализовать логику Fly
        return self.bee_part >= self.elephant_part


    def trumpet(self):
        # TODO: реализовать логику Trumpet
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        # TODO: реализовать логику Eat
        if meal == "nectar":
            self.bee_part = min(100, self.bee_part + value)
            self.elephant_part = max(0, self.elephant_part - value)
        elif meal == "grass":
            self.elephant_part = min(100, self.elephant_part + value)
            self.bee_part = max(0, self.bee_part - value)



# === Тесты для задачи 2 ===
print("\n=== Задача 2: ПчёлоСлон ===")
be = BeeElephant(30, 70)
print(be.fly())            # False
print(be.trumpet())        # tu-tu-doo-doo
be.eat("nectar", 20)       # должно изменить пропорции
print(be.fly())            # возможно True


# =============================
# Задание 3. Класс «Автобус».
#
# Свойства:
# ✅ скорость
# ✅ макс. кол-во мест
# ✅ макс. скорость
# ✅ список фамилий пассажиров
# ✅ флаг наличия свободных мест
# ✅ словарь мест (номер: фамилия)
#
# Методы:
# ✅ посадка/высадка одного или нескольких пассажиров
# ✅ увеличение/уменьшение скорости на заданное значение
# ✅ операции:
#   - `in` проверяет фамилию в списке
#   - `+=` посадка
#   - `-=` высадка


# === TODO: реализовать класс Bus ===
class Bus:
    def __init__(self, max_seats, max_speed):
        # TODO: инициализировать поля
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.speed = 0 #начальная скорость
        self.passengers = {}
        self.free_seats = True

    #Обновляем значение свободных мест
    def _update_free_seats(self):
        self.free_seats = len(self.passengers) < self.max_seats

    def board(self, *passengers):
        # TODO: посадка пассажиров
        for surname in passengers:
            if len(self.passengers) < self.max_seats:
                #перебираем номера мест от 1 до максимального
                for seat_number in range(1, self.max_seats + 1):
                    #проверяем занято ли место в словаре
                    if seat_number not in self.passengers:
                        self.passengers[seat_number] = surname
                        break
            else:
                print(f"Нет свободных мест для {surname}")
        self._update_free_seats()

    def unboard(self, *passengers):
        # TODO: высадка пассажиров
        for surname in passengers:
            seat_number = None
            for seat, passenger in self.passengers.items():
                if passenger == surname:
                    seat_number = seat
                    break
            if seat_number is not None:
                del self.passengers[seat_number]
            else:
                print(f"{surname} не найден")
        self._update_free_seats()

    def change_speed(self, delta):
        # TODO: изменить скорость на delta
        new_speed = self.speed + delta
        if new_speed > self.max_speed:
            self.speed = self.max_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def __contains__(self, surname):
        # TODO: проверить фамилию пассажира
        return surname in self.passengers.values()

    def __iadd__(self, surname):
        # TODO: += посадка
        self.board(surname)
        return self

    def __isub__(self, surname):
        # TODO: -= высадка
        self.unboard(surname)
        return self


# === Тесты для задачи 3 ===
print("\n=== Задача 3: Автобус ===")
bus = Bus(max_seats=3, max_speed=100)
bus.board("Иванов", "Петров")
print("Иванов" in bus)     # True
bus += "Сидоров"
print("Сидоров" in bus)    # True
bus -= "Петров"
print("Петров" in bus)     # False
bus.change_speed(20)