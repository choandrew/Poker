import argparse
import re

import time
import prob_functions


def parse_args():
    # Define possible command line arguments
    parser = argparse.ArgumentParser(
        description="Find the odds that a Texas Hold'em hand will win. Note "
        "that cards must be given in the following format: As, Jc, Td, 3h.")

    parser.add_argument("cards", type=str, nargs="*", metavar="hole card",
        help="Hole cards you want to find the odds for.")

    parser.add_argument("-b", "--board", nargs="*", type=str, metavar="card",
        help="Add board cards")

    parser.add_argument("-e", "--exact", action="store_true",
        help="Find exact odds by enumerating every possible board")

    parser.add_argument("-n", type=int, default=10000,
        help="Run N Monte Carlo simulations")

    # Parse command line arguments and check for errors
    args = parser.parse_args()
    error_check(args)

    # Parse hole cards
    hole_cards = parse_hole_cards(args.cards)
    board = None

    # Create the deck. If the user has defined a board, parse the board.
    if args.board:
        board = parse_cards(args.board)
        all_cards = list(hole_cards)
        all_cards.append(board)
        deck = prob_functions.generate_deck(all_cards)
    else:
        deck = prob_functions.generate_deck(hole_cards)
    return hole_cards, args.n, args.exact, board, deck


# Error checking the command line arguments
def error_check(args):
    # Checking that the number of Monte Carlo simulations is a positive number
    if args.n <= 0:
        print("Number of Monte Carlo simulations must be positive.")
        exit()
    # Checking that there are an even number of hole cards
    if len(args.cards) <= 0 or len(args.cards) % 2:
        print(args.cards)
        print("You must provide a non-zero even number of hole cards")
        exit()
    all_cards = list(args.cards)
    # Checking that the board length is either 3 or 4 (flop or flop + turn)
    if args.board:
        if len(args.board) != 3 and len(args.board) != 4:
            print("Board must have a length of 3 or 4.")
            exit()
        all_cards.extend(args.board)
    # Checking that the hole cards + board are formatted properly and unique
    card_re = re.compile('[AKQJT98765432][scdh]')
    for card in all_cards:
        if not card_re.match(card):
            print("Invalid card given.")
            exit()
        else:
            if all_cards.count(card) != 1:
                print("The cards given must be unique.")
                exit()


# Returns tuple of two-tuple hole_cards: e.g. ((As, Ks), (Ad, Kd), (Jh, Th))
def parse_hole_cards(hole_cards):
    cards = parse_cards(hole_cards)
    # Create two-tuples out of hole cards
    hole_cards, current_hole_cards = [], []
    for hole_card in cards:
        current_hole_cards.append(hole_card)
        if len(current_hole_cards) == 2:
            hole_cards.append((current_hole_cards[0], current_hole_cards[1]))
            current_hole_cards = []
    return tuple(hole_cards)


# Instantiates new cards from the arguments and returns them in a tuple
def parse_cards(card_strings):
    return [prob_functions.Card(arg) for arg in card_strings]


# Driver function which parses the command line arguments into hole cards,
# instantiates data structures to hold the intermediate results of the
# simulations, performs the simulations, and prints the results
def calculate(list_of_cards):


    #list_of_cards should be of form [(r1,s1),(r2,s2),(r3,s3),(r4,s4)] etc
    #where each tuple represents a card


    # Parse command line arguments into hole cards and create deck
    (hole_cards, num_iterations,
                    exact, given_board, deck) = parse_args()
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
    for remaining_board in generate_boards(deck, num_iterations, board_length):
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
