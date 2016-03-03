import argparse
import re
import deck
import time
import prob_functions



# Driver function which parses the command line arguments into hole cards,
# instantiates data structures to hold the intermediate results of the
# simulations, performs the simulations, and prints the results
def main():#list_of_cards):


    #list_of_cards should be of form [(r1,s1),(r2,s2),(r3,s3),(r4,s4)] etc
    #where each tuple represents a card




    a = deck.Card(0,14)
    b = deck.Card(1,14)
    c = deck.Card(2,4)
    d = deck.Card(2,3)
    hole_cards = ((a, b),(c,d)) 
    num_iterations = 10000
    exact = False
    given_board = None
    
    #generate deck that has the hole cards missing
    the_deck = prob_functions.generate_deck(hole_cards)


    print(the_deck)
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
    if exact or given_board is not None:
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
    prob_functions.print_results(hole_cards, winner_list)


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nTime elapsed(seconds): ", time.time() - start)
