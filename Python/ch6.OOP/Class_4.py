# define function for object (method) for change properties
>>> class Game:
...     def set_money(self, money):
...         self.money = money
...     def get_money(self):
...         return self.money
...
>>> game = Game()
>>> Game.set_money(game, 5)
>>> Game.get_money(game)
5
>>> game.set_money(4)
>>> game.get_money()
4