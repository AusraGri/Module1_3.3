from random import shuffle

class Card:
    def __init__(self, sign, rank, value) -> None:
        self.sign = sign
        self.rank = rank
        self.value = value

    def __str__(self) -> str:
        return f"{self.sign}{self.rank}"


class CardDeck:
    def __init__(self): 
        self.cardDeck = self.card_deck()  
    
    def card_deck(self):
        signs = ["\u2664", "\u2661", "\u2662", "\u2667"]
        card_rank_value = {"A": 14, "K": 13, "Q": 12, "J": 11, 
                           "10": 10, "9": 9, "8": 8, "7": 7,
                            "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        card_deck = []
        for sign in signs:
            for rank in card_rank_value:
                card_deck.append(Card(sign, rank, card_rank_value[rank]))  
        return card_deck

    def __str__(self):
        """Only testing purpose, will return error"""
        for card in self.cardDeck:
            print(card)
    
    def deck_shuffle(self):
        shuffle(self.cardDeck)

    def card_split(self, number_of_players):
        # return deck1, deck2...
        pass
 
    def card_compare(self, card1, card2):
        pass


#c = Cards()
#print(c)
