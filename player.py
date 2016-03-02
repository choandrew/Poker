

class Player(object):
    def __init__(self, name ,starting_cash):
        self.name = name
        self.cash = starting_cash
        
    def win(self, earnings):
        self.cash += earnings

    def loss(self, losings):
        self.cash -= losings

    def cash(self):
        return self.cash
