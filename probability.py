import argparse
import re
import time
import prob_functions
from multiprocessing import Process, Queue

# Driver function which parses the command line arguments into hole cards,
# instantiates data structures to hold the intermediate results of the
# simulations, performs the simulations, and prints the results


#hole_cards =((a,b),(c,d),...) where a,b,c,d,... are cards
#num_iterations is the number of monte carlo simulations
#exact is if you want to calculate the exact value
#given_board = [a,b,c,...] where len(given_board) = 3,4, or 5 and a,b,c are cards

def single_prob(hole_cards, num_iterations, given_board):

    if given_board == []:
        given_board = None

    #generate deck that has the hole cards missing
    the_deck = prob_functions.generate_deck(hole_cards)

    num_players = len(hole_cards)

    # Create results data structures which tracks results of comparisons
    # 1) result_histograms: a list for each player that shows the number of
    #    times each type of poker hand (e.g. flush, straight) was gotten
    # 2) winner_list: number of times each player wins the given round
    # 3) result_list: list of the best possible poker hand for each pair of
    #    hole cards for a given board
    result_list, winner_list = [None] * num_players, [0] * (num_players + 1)
    result_histograms = []
    for player in range(num_players):
        result_histograms.append([0] * 10)

    # Choose whether we're running a Monte Carlo or exhaustive simulation
    board_length = 0 if given_board == None else len(given_board)

    # When a board is given, exact calculation is much faster than Monte Carlo
    # simulation, so default to exact if a board is given
    if given_board is not None or num_iterations == "e":
        generate_boards = prob_functions.generate_exhaustive_boards
    else:
        generate_boards = prob_functions.generate_random_boards

    # Run simulations
    for remaining_board in generate_boards(the_deck, num_iterations, board_length):
        # Generate a new board
        if given_board:
            board = given_board[:]
            board.extend(remaining_board)
        else:
            board = remaining_board

        # Find the best possible poker hand given the created board and the
        # hole cards and save them in the results data structures
        (suit_histogram,
                histogram, max_suit) = prob_functions.preprocess_board(board)
        for index, hole_card in enumerate(hole_cards):
            result_list[index] = prob_functions.detect_hand(hole_card, board,
                                         suit_histogram, histogram, max_suit)

        # Find the winner of the hand and tabulate results
        winner_index = prob_functions.compare_hands(result_list)
        winner_list[winner_index] += 1

        # Increment what hand each player made
        for index, result in enumerate(result_list):
            result_histograms[index][result[0]] += 1
    return prob_functions.return_results(hole_cards, winner_list)

#in this case, hole cards is just one card
def calculate_prob(hole_cards, num_iterations, given_board):
    import itertools
    from multiprocess import Pool
    import dill as pickle
    p = Pool(4)

    deck_cards = prob_functions.generate_deck(hole_cards)
    possible_card_pairings = tuple(itertools.combinations(deck_cards, 2))
    card_combos = map( lambda x: tuple (list(hole_cards) + [x]), possible_card_pairings)

    s = pickle.dumps(lambda hc: single_prob(hc, num_iterations, given_board))
    f = pickle.loads(s) 
    prob_list = p.map( f , card_combos)
    tie = 0
    win = 0
    for prob in prob_list:
        tie += prob[0] 
        win += prob[1]
    l = len(prob_list)
    tie = tie / l
    win = win / l

    return (tie,win)

def get_winner(hole_cards, community_cards):

    #generate deck that has the hole cards missing
    the_deck = prob_functions.generate_deck(hole_cards)

    num_players = len(hole_cards)

    # Create results data structures which tracks results of comparisons
    # 1) result_histograms: a list for each player that shows the number of
    #    times each type of poker hand (e.g. flush, straight) was gotten
    # 2) winner_list: number of times each player wins the given round
    # 3) result_list: list of the best possible poker hand for each pair of
    #    hole cards for a given board
    result_list, winner_list = [None] * num_players, [0] * (num_players + 1)
    result_histograms = []
    for player in range(num_players):
        result_histograms.append([0] * 10)

    # Find the best possible poker hand given the created board and the
    # hole cards and save them in the results data structures
    (suit_histogram,
            histogram, max_suit) = prob_functions.preprocess_board(community_cards)
    for index, hole_card in enumerate(hole_cards):
        result_list[index] = prob_functions.detect_hand(hole_card, community_cards,
                                     suit_histogram, histogram, max_suit)

    # Find the winner of the hand and tabulate results
    winner_index = prob_functions.compare_hands(result_list)

    return [winner_index]

#tests
if __name__ == '__main__':
    import deck
    a1 = deck.Card(0,9)
    a2 = deck.Card(1,13)
    b1 = deck.Card(0,14)
    b2 = deck.Card(2,10)
    c1 = deck.Card(3,2)
    c2 = deck.Card(3,9)
    
    hole_cards = ((a1, a2),(b1,b2),(c1,c2)) 

    num_iterations = 1000
    exact = False
    given_board = []
   
    #test of func
    #print(single_prob(hole_cards, num_iterations, given_board))

    print("\n")

    d1 = deck.Card(1,7)
    d2 = deck.Card(2,2)
    d3 = deck.Card(2,3)
    d4 = deck.Card(2,4)
    d5 = deck.Card(1,5)
    community_cards  = [d1, d2, d3, d4, d5]

    print(community_cards)

    #test of func
    print(get_winner(hole_cards, community_cards), "\n")

    hole_cards = ((a1,a2),)

    calculate_prob(hole_cards, num_iterations, given_board)
