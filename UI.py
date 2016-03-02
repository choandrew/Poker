import deck
import player
import bet

from multiprocessing import Process, Queue


def main():
    
    #get number of players
    #there is always one player, the rest are AI
    
    number_of_players = input("How many opponents? ")
    starting_cash     = input("How much starting cash? ")
    blind             = input("What is the blind? ")

    players = []

    for i in range(0, number_of_players):
        players.append(player.Player(starting_cash))


    game = 1
    while (game == 1):
    
        pot = 0
        deck1 = deck.Deck()
        deck1.shuffle()
        community_cards = []
        hands = []
        state = 0 
        
        winner = None
        
        #hand out cards
        while (state == 0):
            pass
        
        # first state of betting
        while (state == 1):
            pass
        
        #flop and flop betting
        while (state == 2):
            community_cards.append(deck1.pop_card())
            community_cards.append(deck1.pop_card())
            community_cards.append(deck1.pop_card())
        
        # turn and turn betting
        while (state == 3):
            community_cards.append(deck1.pop_card())
            pass
        
        # river and river betting
        while (state == 4):
            community_cards.append(deck1.pop_card())
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

        #check for player loss
        while (state == 8):
            pass

if __name__ == "__main__":
    main()
