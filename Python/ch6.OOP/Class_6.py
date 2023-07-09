# define static variable in class
>>> class Game:
...     goal_money = 3000
...
...     def set_money(self, x):
...         self.money = x
...
...     def get_money(self):
...         return self.money
...
>>> Game.goal_money
3000
>>> Game.max_people_count = 20
>>> Game.max_people_count
20
>>> game = Game()
>>> game.goal_money
3000
>>> game.goal_money = 2000
>>> game.goal_money
2000
>>> Game.goal_money
3000
>>> del game.goal_money
>>> game.goal_money
3000