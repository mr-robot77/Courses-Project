class Student(Account):
    def __init__(self, full_name, username, password, rank_in_college):
        super().__init__(full_name, username, password)
        '''
        super()
        --------------------------
        self.full_name = full_name
		self.username = username
		self.password = password
		self.courses = []
        '''
        self.rank_in_college = rank_in_college 

class Professor(Account):
    def __init__(self, full_name, username, password, h_index_rank):
        super().__init__(full_name, username, password)
        self.h_index_rank = h_index_rank   