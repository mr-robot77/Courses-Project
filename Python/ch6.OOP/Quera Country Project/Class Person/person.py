import math


class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1 
        self.job = ""
        self.work_place = None 
        Person.instances.append(self)

    def do_level(self, income):
        if self.work_place is not None:
            return income * math.sqrt(self.level*self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        
        return self.do_level(income) - cost 

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1 

    @staticmethod
    def calc_all():
        total_calculation = 0
        for person in Person.instances:
            total_calculation += person.calc()
        return total_calculation
