class Student(Account):
    def __init__(self, full_name, username, password, rank_in_college):
        super().__init__(full_name, username, password)
        self.rank_in_college = rank_in_college

    def get_rank(self):
        return f'Student {self.full_name} rank in the college is {self.rank_in_college}!' 

class Professor(Account):
    def __init__(self, full_name, username, password, h_index_rank):
        super().__init__(full_name, username, password)
        self.h_index_rank = h_index_rank   

    def get_rank(self):
        return f'Professor {self.full_name} H-Index rank is {self.h_index_rank}!' 

>>> ali = Student('Ali Safinal', 'safinal', '@Li2001', 13)
>>> seyed = Professor('Seyed Ali Babaei', 'SalibeBaSalabat1234', '786ff912', 80)
>>> ali.get_rank()
'Student Ali Safinal rank in the college is 13!'
>>> seyed.get_rank()
'Professor Seyed Ali Babaei H-Index rank is 80!'