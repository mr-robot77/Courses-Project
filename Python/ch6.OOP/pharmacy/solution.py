class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        employee_info = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }
        self.employees.append(employee_info)

    def total_value(self) -> int:
        total_price = 0
        for drug in self.drugs:
            drug_total_price = drug.amount * drug.price
            total_price += drug_total_price
        return total_price

    def employees_summary(self) -> str:
        summary = "Employees:\n"
        for i,employee in enumerate (self.employees,start=1):
            first_name = employee ["first_name"]
            last_name = employee ["last_name"]
            age = str(employee["age"])
            line = f"The employee number {i} is {first_name} {last_name} who is {age} years old.\n"
            
            summary += line
        return summary

