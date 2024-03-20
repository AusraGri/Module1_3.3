class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def lay_card(self):
        card = self.hand[0]
        self.hand.remove(self.hand[0])
        return card
    
    def take_card(self, cards):
        for card in cards:
            self.hand.append(card)