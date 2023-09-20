class Health:
    __health = 100
    __max_health = 100

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if health > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health = health

    def __init__(self, max_health=100):
        self.__max_health = max_health
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0


import random


class Name:
    __name = "default"

    def get_name(self):
        return self.__name

    def __init__(self, id=random.randint(0, 100), name="plane"):
        if name == "plane":
            if id <= 40:
                name = f"Pu$$y Destroyer [{id}]"
            elif 40 < id <= 80:
                name = f"Bomber [{id}]"
            elif id > 80:
                name = f"Scouter [{id}]"
            else:
                name = f"Unknown plane [{id}]"
        self.__name = name


class Position:
    __position = [0, 0]
    __move_speed = 1

    def get_position(self):
        return self.__position

    def move(self, x, y):
        if x > 1:
            x = 1
        elif x < -1:
            x = -1
        if y > 1:
            y = 1
        elif y < -1:
            y = -1

        self.__position[0] += x * self.__move_speed
        self.__position[1] += y * self.__move_speed

    def __init__(self, x=0, y=0, move_speed=1):
        self.__position = [x, y]
        self.__move_speed = move_speed


class Plane(Health, Name, Position):
    print("xui")
