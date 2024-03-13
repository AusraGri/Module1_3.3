
class Cards:
    def __init__(self): 
        self.cardDeck = self.card_deck()  
    
    def card_deck(self):
        signs = ["\u2664", "\u2661", "\u2662", "\u2667"]
        card_name = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        card_deck = []
        for sign in signs:
            for name in card_name:
                card = f"{name}{sign}"
                card_deck.append(card)
        return card_deck

    def __str__(self):
        return str(self.cardDeck)
    
    def deck_shuffle(self):
        pass

    def card_split(self, number_of_players):
        # return deck1, deck2...
        pass
       
    def card_compare(self, card1, card2):
        pass


c = Cards()
print(c)