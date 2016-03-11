import random

def liar(tie_prob, win_prob):
    if (tie_prob + win_prob) > 0.8:
        return slow_play(tie_prob, win_prob)
    elif (tie_prob + win_prob) < 0.4:
        return bluff(tie_prob, win_prob)
    elif 0.4 <= (tie_prob + win_prob) <= 0.5:
        return random.normalvariate(1, 0.3)
    else:
        return random.normalvariate(1, 0.1)

def bluff(tie_prob, win_prob):
    r = random.uniform(0, 1)
    if r < (tie_prob + win_prob):
        return random.uniform(1,2)
    else:
        return 1

def slow_play(tie_prob, win_prob):
    r = random.uniform(0, 1)
    if r > (tie_prob + win_prob):
        return 0
    else:
        return 1
