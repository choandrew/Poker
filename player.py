
# name should be a number
# 0 is the human player

class Player(object):
    def __init__(self, player_name, starting_cash):
        self.name = player_name
        self.cash = starting_cash
        self.hand = (None, None)
        self.bet_this_round = 0

    def win(self, earnings):
        self.cash += earnings

    def loss(self, losings):
        self.cash -= losings




    def get_cash(self):
        return self.cash

    def get_name(self):
        return self.name




    def get_hand(self):
        return self.hand

    def assign_hand(self, c1, c2):
        self.hand = (c1,c2)

    def empty_hand(self):
        self.hand = (None, None)




    #amount bet this round
    def amount_bet_this_round(self):
        return self.bet_this_round

    def add_bet_this_round(self, bet):
        self.bet_this_round += bet

    def reset_bet_this_round(self):
        self.bet_this_round = 0
