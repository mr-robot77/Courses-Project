# define static method for class
class Sample:
    goal_money = 3000   

    @staticmethod 
    def increase_goal_money(value):
        Sample.goal_money += value

sample = Sample()
print(Sample.goal_money)
Sample.increase_goal_money(100)
print(sample.goal_money)