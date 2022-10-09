# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time


class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                timing = time.time()
                while time.time() - timing < 7.0:
                    print("red")
                else:
                    self.__color = "yellow"
            if self.__color == "yellow":
                timing = time.time()
                while time.time() - timing < 2.0:
                    print("yellow")
                else:
                    self.__color = "green"
            if self.__color == "green":
                timing = time.time()
                while time.time() - timing < 10.0:
                    print("green")
                else:
                    self.__color = "red"


t = TrafficLight()
t.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self, m, th):
        print(str(self.__length * self.__width * m * th))


r = Road(10, 5)
r.mass(2, 2)

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии \
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    @property
    def income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


p = Position("Иван", "Антонов", "менеджер", {"wage": 34000, "bonus": 12000})

print(p.get_full_name())
print(str(p.get_total_income()))

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print("машина повернула " + direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("превышение скорости")


class PoliceCar(Car):
    pass


tc = TownCar(70, "белый", "TC", False)
sc = SportCar(60, "желтый", "SC", False)
wc = WorkCar(170, "зеленый", "WC", False)
pc = PoliceCar(30, "синий", "PC", True)

print(tc.color)
print(sc.name)
print(str(wc.speed))
print(str(pc.is_police))

tc.show_speed()
sc.show_speed()
wc.show_speed()
pc.show_speed()

tc.go()
sc.stop()
wc.turn("налеао")

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


pen = Pen("Pen")
pencil = Pencil("Pencil")
handle = Handle("Handle")
pen.draw()
pencil.draw()
handle.draw()
