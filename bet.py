import scipy
import bluff
import probability
import player as P

# f* = (bp-q)/b = (p(b+1) - 1) / b

"""
    f* is the fraction of the current bankroll to wager, i.e. how much to bet;
    b is the net odds received on the wager
    ("b to 1"); that is, you could win $b (on top of getting back your $1 wagered) for a $1 bet
    p is the probability of winning;
    q is the probability of losing, which is 1 − p.
"""

def kelly(b,p):
    return ((p(b+1) - 1) /b)

#calculate probability here
def bet(current_pot,ante_value,current_bet, player):
    return 10


