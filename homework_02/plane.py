"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_history = self.cargo
        self.cargo = 0
        return cargo_history
