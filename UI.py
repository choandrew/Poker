import deck
import player as P
import bet
import copy

from multiprocessing import Process, Queue


def get_number_of_players():
    number_of_players = int(input("How many opponents? "))
    
    if (number_of_players > 5):
        print("Too many players.")
        exit(1)

    return number_of_players

def deal_cards(players_remaining_in_round, the_deck):
    for player in players_remaining_in_round:
        c1 = the_deck.pop_card()
        c2 = the_deck.pop_card()
        player.assign_hand(c1, c2)
    state = 1


def betting():
    pass

def main():
    
    #get number of players
    #there is always one player, the rest are AI
    
    number_of_players = get_number_of_players() + 1

    starting_cash     = 10000 #input("How much starting cash? ")
    blind             = 100 # input("What is the blind? ")

    players = []
    #player0 is always the human
    for i in range(0, number_of_players):
        players.append( P.Player(i, starting_cash) )

    win  = 0
    game = 1
    while (game == 1):
        pot = 0
        the_deck = deck.Deck()
        the_deck.shuffle()

        community_cards = []
        state = 0 

        players_remaining_in_round = []
        for player in players:
            players_remaining_in_round.append(player)

        #hand out cards and take ante
        deal_cards(players_remaining_in_round, the_deck)
        
        # first state of betting
        while (state == 1):
            pass

        #flop and flop betting
        while (state == 2):
            community_cards.append(the_deck.pop_card())
            community_cards.append(the_deck.pop_card())
            community_cards.append(the_deck.pop_card())
            
            print(community_card)

            state = 3

        # turn and turn betting
        while (state == 3):
            community_cards.append(the_deck.pop_card())
            pass
        
        # river and river betting
        while (state == 4):
            community_cards.append(the_deck.pop_card())
            pass
        
        # card reveal
        while (state == 5):
            pass
        
        #payout
        while (state == 6):
            pass
    
        #player elimination
        while (state == 7):
            pass

        #check for human loss
        game = check_for_human_loss(players)
    
    if (win == 0):
        print("You lose!")
    if (win == 1):
        print("You win!")

def check_for_human_loss(players):
    for player in players:
        if player.name() == 0:
            if (len(players) == 1):
                win = 1
                return 0
            else:
                return 1
    return 0


if __name__ == "__main__":
    main()
