import pandas as pd


class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    '''Representation username & votes'''
    def __init__(self, name):
        self.name = name
        self.upvotes = 0
    def receive_upvote(self):
        self.upvotes += 1
    def is_popular(self):
        return self.upvotes > 100

class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type
    def run(self):
        return 'Vroom!'
    def eat(self, food):
        return food + ' is delicious, yum!'
class Tiger(Animal):
    pass


class Tiger(Animal):
    """Representation of tigers, a subclass of Animal."""
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes
    def say_great(self):
        return "It's GREEAAAAAT!"
    # Example of overriding
    def run(self):
        return 'Scamperwoosh!'


'''Here we created a class Baseball with a function __init__ The initialisation function will be called when an object of that initialised. '''
class Baseball:
    '''Takes imput from user about today's game and prints it'''
    def __init__(self, team, enemy):
        self.team = team
        self.enemy = enemy

game = Baseball(input('Type Home Team: '), input('Type Away Team: '))

print("\n     Todays's Game")
print("Home team is: " + game.team)
print('vs')
print('Away team is: ' + game.enemy)
