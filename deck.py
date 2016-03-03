# the shuffle function is not very good
# shuffles the deck and pops the cards

import random

class Card(object):
# Represents a standard playing card.

    #suit and rank are stored as ints corresponding to the index of the list
    suit_names = {0:"c",1:"d",2:"h",3:"s"}
    rank_names = {2: "2", 3: "3", 4:"4", 5: "5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K", 14:"A"}

    def __init__(self, suit, rank):
        if 0 <= suit and suit <= 3:
            self.suit = suit
        else:
            print("Error: suit does not exist")

        if 2 <= rank and rank <= 14:
            self.rank = rank
        else:
            print(self.rank)
            print("Error:rank does not exist")

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s%s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __repr__(self):
        """Returns a human-readable string representation."""
        return '%s%s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by rank

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent. """

        t1 = self.rank
        t2 = other.rank

        return cmp(t1, t2)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class Deck(object):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(0,4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)
