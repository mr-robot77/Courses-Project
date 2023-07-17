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

class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    
    instances = []

    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1 
        return self.calc_capacity()

    def hire(self, person: Person):
        if len(self.employees)>=self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        total_financial_status = 0 
        for instance in WorkPlace.instances:
            total_financial_status += instance.calc()
        return total_financial_status
