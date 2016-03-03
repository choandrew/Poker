
# name should be a number
# 0 is the human player

class Player(object):
    def __init__(self, name, starting_cash):
        self.name = name
        self.cash = starting_cash
        self.hand = (None, None) 

    def win(self, earnings):
        self.cash += earnings

    def loss(self, losings):
        self.cash -= losings

    def cash(self):
        return self.cash

    def name(self):
        return self.name

    def hand(self):
        return self.hand

    def assign_hand(self, c1, c2):
        self.hand = (c1,c2)

    def empty_hand(self):
        self.hand = (None, None)
