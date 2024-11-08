from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, l):
        l_car = self.fuel / self.fuel_consumption
        if l <= l_car:
            self.fuel -= l * self.fuel_consumption
        else:
            raise NotEnoughFuel
