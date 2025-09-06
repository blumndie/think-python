import random

class Card:
    """Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        rank_name = Card.rank_names[self.rank]
        suit_name = Card.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    def to_tuple(self):
        return (self.suit, self.rank)
    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()
    def __le__(self, other):
        return self.to_tuple() <= other.to_tuple()

class Deck:

    def __init__(self, cards):
        self.cards = cards
        
    def make_cards():
        cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                cards.append(card)
        return cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def take_card(self):
        return self.cards.pop()
    def put_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)
        
class Hand(Deck):
    def __init__(self, label=''):
        self.label = label
        self.cards = []
        
# the bad hand
'''     
cards = [Card(0, 2),
         Card(0, 3),
         Card(2, 4),
         Card(3, 5),
         Card(0, 7),
        ]

good_hand = PokerHand('good_hand')

suit = 0
for rank in range(10, 15):
    card = Card(suit, rank)
    good_hand.put_card(card)
'''