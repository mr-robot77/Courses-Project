class Account:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.courses = []   

    def add_course(self, new_course):
        self.courses.append(new_course)