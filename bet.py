import scipy
import deceive
import probability

# f* = (bp-q)/b = (p(b+1) - 1) / b

"""
    f* is the fraction of the current bankroll to wager, i.e. how much to bet;
    b is the net odds received on the wager
    ("b to 1"); that is, you could win $b (on top of getting back your $1 wagered) for a $1 bet
    p is the probability of winning;
    q is the probability of losing, which is 1 − p.
"""

def kelly(b,p):
    return ((p*(b+1) - 1) /b)

#calculate probability here
def bet(current_pot,ante_value,current_bet, player,given_board):
    hand = player.get_hand()
    cards = (hand, )

    p = probability.calculate_prob(cards, 500, given_board)
    tie_prob = p[0]
    win_prob = p[1]


    k_tie = kelly(float(current_bet), tie_prob)
    k_win = kelly(float(current_bet), win_prob)

    print(k_tie, k_win)
    bet_frac = (k_tie + k_win)  /3

    bet_value = int( deceive.liar(tie_prob, win_prob) * bet_frac *player.get_cash() /100) *100
  
    #must bet above ante, so having less than ante in cash is essentially just all in
    if (bet_value > player.get_cash() - ante_value):
        bet_value = player.get_cash()

    if (current_bet == 0 and bet_value < ante_value + current_bet):
        return 0
    elif (current_bet != 0 and bet_value < ante_value + current_bet):
        return -1
    else:
        return bet_value
